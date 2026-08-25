"""High-Performance Asynchronous Repository for FeatureSet."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.feature_sets import FeatureSet
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("feature_sets_repository")

class FeatureSetRepository(BaseRepository[FeatureSet]):
    def __init__(self, session: AsyncSession):
        super().__init__(FeatureSet, session)

    async def get_by_code(self, code: str) -> Optional[FeatureSet]:
        stmt = select(FeatureSet).where(FeatureSet.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[FeatureSet]:
        stmt = select(FeatureSet).where(FeatureSet.is_active == True).order_by(desc(FeatureSet.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(FeatureSet.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
