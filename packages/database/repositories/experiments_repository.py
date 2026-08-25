"""High-Performance Asynchronous Repository for Experiment."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.experiments import Experiment
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("experiments_repository")

class ExperimentRepository(BaseRepository[Experiment]):
    def __init__(self, session: AsyncSession):
        super().__init__(Experiment, session)

    async def get_by_code(self, code: str) -> Optional[Experiment]:
        stmt = select(Experiment).where(Experiment.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Experiment]:
        stmt = select(Experiment).where(Experiment.is_active == True).order_by(desc(Experiment.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Experiment.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
