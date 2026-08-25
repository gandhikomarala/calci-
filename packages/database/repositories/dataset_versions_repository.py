"""High-Performance Asynchronous Repository for DatasetVersion."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.dataset_versions import DatasetVersion
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("dataset_versions_repository")

class DatasetVersionRepository(BaseRepository[DatasetVersion]):
    def __init__(self, session: AsyncSession):
        super().__init__(DatasetVersion, session)

    async def get_by_code(self, code: str) -> Optional[DatasetVersion]:
        stmt = select(DatasetVersion).where(DatasetVersion.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[DatasetVersion]:
        stmt = select(DatasetVersion).where(DatasetVersion.is_active == True).order_by(desc(DatasetVersion.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(DatasetVersion.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
