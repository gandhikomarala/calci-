"""High-Performance Asynchronous Repository for ModelPerformance."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.model_performance import ModelPerformance
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("model_performance_repository")

class ModelPerformanceRepository(BaseRepository[ModelPerformance]):
    def __init__(self, session: AsyncSession):
        super().__init__(ModelPerformance, session)

    async def get_by_code(self, code: str) -> Optional[ModelPerformance]:
        stmt = select(ModelPerformance).where(ModelPerformance.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ModelPerformance]:
        stmt = select(ModelPerformance).where(ModelPerformance.is_active == True).order_by(desc(ModelPerformance.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ModelPerformance.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
