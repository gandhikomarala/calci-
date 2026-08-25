"""High-Performance Asynchronous Repository for ExperimentMetric."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.experiment_metrics import ExperimentMetric
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("experiment_metrics_repository")

class ExperimentMetricRepository(BaseRepository[ExperimentMetric]):
    def __init__(self, session: AsyncSession):
        super().__init__(ExperimentMetric, session)

    async def get_by_code(self, code: str) -> Optional[ExperimentMetric]:
        stmt = select(ExperimentMetric).where(ExperimentMetric.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ExperimentMetric]:
        stmt = select(ExperimentMetric).where(ExperimentMetric.is_active == True).order_by(desc(ExperimentMetric.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ExperimentMetric.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
