from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from backend.auth.schemas import LoginRequest, RegisterRequest, TokenResponse, RefreshTokenRequest
from backend.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest, session: AsyncSession = Depends(get_db_session)):
    service = AuthService(session)
    return await service.authenticate(req)

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(req: RegisterRequest, session: AsyncSession = Depends(get_db_session)):
    service = AuthService(session)
    return await service.register(req)

@router.post("/logout")
async def logout():
    return {"message": "Logged out successfully"}
