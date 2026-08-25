"""High-Performance Asynchronous Repository for FeatureVersion."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.feature_versions import FeatureVersion
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("feature_versions_repository")

class FeatureVersionRepository(BaseRepository[FeatureVersion]):
    def __init__(self, session: AsyncSession):
        super().__init__(FeatureVersion, session)

    async def get_by_code(self, code: str) -> Optional[FeatureVersion]:
        stmt = select(FeatureVersion).where(FeatureVersion.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[FeatureVersion]:
        stmt = select(FeatureVersion).where(FeatureVersion.is_active == True).order_by(desc(FeatureVersion.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(FeatureVersion.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
