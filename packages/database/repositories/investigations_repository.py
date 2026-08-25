"""High-Performance Asynchronous Repository for Investigation."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.investigations import Investigation
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("investigations_repository")

class InvestigationRepository(BaseRepository[Investigation]):
    def __init__(self, session: AsyncSession):
        super().__init__(Investigation, session)

    async def get_by_code(self, code: str) -> Optional[Investigation]:
        stmt = select(Investigation).where(Investigation.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Investigation]:
        stmt = select(Investigation).where(Investigation.is_active == True).order_by(desc(Investigation.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Investigation.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
