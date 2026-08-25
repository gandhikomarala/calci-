"""High-Performance Asynchronous Repository for MonitoringMetric."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.monitoring_metrics import MonitoringMetric
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("monitoring_metrics_repository")

class MonitoringMetricRepository(BaseRepository[MonitoringMetric]):
    def __init__(self, session: AsyncSession):
        super().__init__(MonitoringMetric, session)

    async def get_by_code(self, code: str) -> Optional[MonitoringMetric]:
        stmt = select(MonitoringMetric).where(MonitoringMetric.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[MonitoringMetric]:
        stmt = select(MonitoringMetric).where(MonitoringMetric.is_active == True).order_by(desc(MonitoringMetric.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(MonitoringMetric.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
