"""High-Performance Asynchronous Repository for ExperimentParameter."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.experiment_parameters import ExperimentParameter
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("experiment_parameters_repository")

class ExperimentParameterRepository(BaseRepository[ExperimentParameter]):
    def __init__(self, session: AsyncSession):
        super().__init__(ExperimentParameter, session)

    async def get_by_code(self, code: str) -> Optional[ExperimentParameter]:
        stmt = select(ExperimentParameter).where(ExperimentParameter.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ExperimentParameter]:
        stmt = select(ExperimentParameter).where(ExperimentParameter.is_active == True).order_by(desc(ExperimentParameter.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ExperimentParameter.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
