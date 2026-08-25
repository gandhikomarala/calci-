import datetime
from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from packages.database.models.users import User, Role, UserRole, RefreshToken
from packages.security.hashing import PasswordHasher
from packages.security.jwt import JwtTokenManager
from packages.security.rbac import RBACPermissionManager
from packages.configuration.settings import settings
from packages.core.exceptions import AuthenticationError, ConflictError, NotFoundError
from backend.auth.schemas import LoginRequest, RegisterRequest, TokenResponse

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def authenticate(self, req: LoginRequest) -> TokenResponse:
        result = await self.session.execute(select(User).where(User.email == req.email.lower()))
        user = result.scalars().first()
        
        if not user or not PasswordHasher.verify_password(req.password, user.hashed_password):
            raise AuthenticationError("Invalid email or password")
            
        if not user.is_active:
            raise AuthenticationError("User account is inactive or locked")

        # Fetch roles & permissions
        role_result = await self.session.execute(
            select(Role.name).join(UserRole, UserRole.role_id == Role.id).where(UserRole.user_id == user.id)
        )
        roles = list(role_result.scalars().all()) or ["VIEWER"]
        permissions = list(RBACPermissionManager.get_permissions_for_roles(roles))

        access_token = JwtTokenManager.create_access_token(
            subject=user.id,
            roles=roles,
            permissions=permissions,
            extra_claims={"email": user.email, "org_id": user.organization_id}
        )
        refresh_token = JwtTokenManager.create_refresh_token(subject=user.id)

        # Update last login
        user.last_login = datetime.datetime.utcnow()
        await self.session.flush()

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            user_id=user.id,
            email=user.email,
            roles=roles,
            permissions=permissions,
        )

    async def register(self, req: RegisterRequest) -> TokenResponse:
        existing = await self.session.execute(select(User).where(User.email == req.email.lower()))
        if existing.scalars().first():
            raise ConflictError(f"User with email '{req.email}' already exists")

        new_user = User(
            email=req.email.lower(),
            hashed_password=PasswordHasher.hash_password(req.password),
            first_name=req.first_name,
            last_name=req.last_name,
            is_active=True,
            is_verified=True,
        )
        self.session.add(new_user)
        await self.session.flush()

        # Assign default ML_ENGINEER role
        role_res = await self.session.execute(select(Role).where(Role.name == "ML_ENGINEER"))
        role = role_res.scalars().first()
        if role:
            user_role = UserRole(user_id=new_user.id, role_id=role.id)
            self.session.add(user_role)
            await self.session.flush()

        roles = ["ML_ENGINEER"]
        permissions = list(RBACPermissionManager.get_permissions_for_roles(roles))

        access_token = JwtTokenManager.create_access_token(subject=new_user.id, roles=roles, permissions=permissions)
        refresh_token = JwtTokenManager.create_refresh_token(subject=new_user.id)

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            user_id=new_user.id,
            email=new_user.email,
            roles=roles,
            permissions=permissions,
        )
