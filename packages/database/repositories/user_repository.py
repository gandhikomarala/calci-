from typing import Optional, List, Tuple, Sequence
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, or_
from packages.database.models.users import User, Role, UserRole, Organization, ApiKey, RefreshToken
from packages.database.repository import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email.lower(), User.is_deleted == False)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def get_with_roles(self, user_id: str) -> Optional[Tuple[User, List[str]]]:
        stmt = select(User).where(User.id == user_id, User.is_deleted == False)
        user_res = await self.session.execute(stmt)
        user = user_res.scalars().first()
        if not user:
            return None

        role_stmt = select(Role.name).join(UserRole, UserRole.role_id == Role.id).where(UserRole.user_id == user.id)
        role_res = await self.session.execute(role_stmt)
        roles = list(role_res.scalars().all())
        return user, roles

    async def list_users(self, skip: int = 0, limit: int = 20, search: Optional[str] = None, role: Optional[str] = None) -> Tuple[Sequence[User], int]:
        stmt = select(User).where(User.is_deleted == False)
        if search:
            stmt = stmt.where(or_(
                User.first_name.ilike(f"%{search}%"),
                User.last_name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%")
            ))
        if role:
            stmt = stmt.join(UserRole).join(Role).where(Role.name == role)

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        res = await self.session.execute(stmt.offset(skip).limit(limit).order_by(User.created_at.desc()))
        return res.scalars().all(), total

    async def update_last_login(self, user_id: str) -> None:
        stmt = update(User).where(User.id == user_id).values(last_login=datetime.datetime.utcnow(), failed_login_attempts=0)
        await self.session.execute(stmt)

    async def record_failed_login(self, user_id: str, max_attempts: int = 5, lock_minutes: int = 15) -> bool:
        stmt = select(User).where(User.id == user_id)
        res = await self.session.execute(stmt)
        user = res.scalars().first()
        if not user:
            return False

        user.failed_login_attempts += 1
        if user.failed_login_attempts >= max_attempts:
            user.locked_until = datetime.datetime.utcnow() + datetime.timedelta(minutes=lock_minutes)
        await self.session.flush()
        return user.failed_login_attempts >= max_attempts
