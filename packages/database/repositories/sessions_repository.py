"""High-Performance Asynchronous Repository for UserSession."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.sessions import UserSession
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("sessions_repository")

class UserSessionRepository(BaseRepository[UserSession]):
    def __init__(self, session: AsyncSession):
        super().__init__(UserSession, session)

    async def get_by_code(self, code: str) -> Optional[UserSession]:
        stmt = select(UserSession).where(UserSession.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[UserSession]:
        stmt = select(UserSession).where(UserSession.is_active == True).order_by(desc(UserSession.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(UserSession.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
