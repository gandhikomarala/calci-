"""High-Performance Asynchronous Repository for FeatureDefinition."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.feature_definitions import FeatureDefinition
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("feature_definitions_repository")

class FeatureDefinitionRepository(BaseRepository[FeatureDefinition]):
    def __init__(self, session: AsyncSession):
        super().__init__(FeatureDefinition, session)

    async def get_by_code(self, code: str) -> Optional[FeatureDefinition]:
        stmt = select(FeatureDefinition).where(FeatureDefinition.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[FeatureDefinition]:
        stmt = select(FeatureDefinition).where(FeatureDefinition.is_active == True).order_by(desc(FeatureDefinition.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(FeatureDefinition.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
