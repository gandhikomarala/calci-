"""High-Performance Asynchronous Repository for ModelMetric."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.model_metrics import ModelMetric
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("model_metrics_repository")

class ModelMetricRepository(BaseRepository[ModelMetric]):
    def __init__(self, session: AsyncSession):
        super().__init__(ModelMetric, session)

    async def get_by_code(self, code: str) -> Optional[ModelMetric]:
        stmt = select(ModelMetric).where(ModelMetric.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ModelMetric]:
        stmt = select(ModelMetric).where(ModelMetric.is_active == True).order_by(desc(ModelMetric.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ModelMetric.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
