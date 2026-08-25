"""Asynchronous Database Repository for DriftMetric."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, or_
from packages.database.models.drift_metrics import DriftMetric
from packages.database.repository import BaseRepository

class DriftMetricRepository(BaseRepository[DriftMetric]):
    def __init__(self, session: AsyncSession):
        super().__init__(DriftMetric, session)

    async def get_by_identifier(self, identifier: str) -> Optional[DriftMetric]:
        stmt = select(DriftMetric).where(DriftMetric.id == identifier)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_filtered(
        self,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None,
        sort_by: str = "created_at",
        sort_order: str = "desc"
    ) -> Tuple[Sequence[DriftMetric], int]:
        stmt = select(DriftMetric)
        
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(DriftMetric, sort_by, DriftMetric.created_at)
        if sort_order == "desc":
            stmt = stmt.order_by(desc(sort_col))
        else:
            stmt = stmt.order_by(sort_col)

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        return res.scalars().all(), total

    async def batch_create(self, entities: List[DriftMetric]) -> List[DriftMetric]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
