"""High-Performance Asynchronous Repository for RefreshToken."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.refresh_tokens import RefreshToken
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("refresh_tokens_repository")

class RefreshTokenRepository(BaseRepository[RefreshToken]):
    def __init__(self, session: AsyncSession):
        super().__init__(RefreshToken, session)

    async def get_by_code(self, code: str) -> Optional[RefreshToken]:
        stmt = select(RefreshToken).where(RefreshToken.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[RefreshToken]:
        stmt = select(RefreshToken).where(RefreshToken.is_active == True).order_by(desc(RefreshToken.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(RefreshToken.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
