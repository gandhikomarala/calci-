"""High-Performance Asynchronous Repository for ExperimentRun."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.experiment_runs import ExperimentRun
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("experiment_runs_repository")

class ExperimentRunRepository(BaseRepository[ExperimentRun]):
    def __init__(self, session: AsyncSession):
        super().__init__(ExperimentRun, session)

    async def get_by_code(self, code: str) -> Optional[ExperimentRun]:
        stmt = select(ExperimentRun).where(ExperimentRun.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ExperimentRun]:
        stmt = select(ExperimentRun).where(ExperimentRun.is_active == True).order_by(desc(ExperimentRun.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ExperimentRun.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
