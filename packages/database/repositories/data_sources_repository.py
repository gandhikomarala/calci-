"""High-Performance Asynchronous Repository for DataSource."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.data_sources import DataSource
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("data_sources_repository")

class DataSourceRepository(BaseRepository[DataSource]):
    def __init__(self, session: AsyncSession):
        super().__init__(DataSource, session)

    async def get_by_code(self, code: str) -> Optional[DataSource]:
        stmt = select(DataSource).where(DataSource.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[DataSource]:
        stmt = select(DataSource).where(DataSource.is_active == True).order_by(desc(DataSource.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(DataSource.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
