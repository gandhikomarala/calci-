"""Asynchronous Database Repository for Experiment."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.experiments import Experiment
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("experiments_repo")

class ExperimentRepository(BaseRepository[Experiment]):
    def __init__(self, session: AsyncSession):
        super().__init__(Experiment, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Experiment]:
        stmt = select(Experiment).where(Experiment.id == identifier)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_filtered(
        self,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None,
        is_active: Optional[bool] = None,
        sort_by: str = "created_at",
        sort_order: str = "desc"
    ) -> Tuple[Sequence[Experiment], int]:
        stmt = select(Experiment)
        
        if is_active is not None and hasattr(Experiment, "is_active"):
            stmt = stmt.where(Experiment.is_active == is_active)
            
        if search and hasattr(Experiment, "name"):
            stmt = stmt.where(Experiment.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Experiment, sort_by, getattr(Experiment, "created_at", Experiment.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Experiment]) -> List[Experiment]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
