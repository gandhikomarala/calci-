"""Asynchronous Database Repository for Dataset."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.datasets import Dataset
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("datasets_repo")

class DatasetRepository(BaseRepository[Dataset]):
    def __init__(self, session: AsyncSession):
        super().__init__(Dataset, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Dataset]:
        stmt = select(Dataset).where(Dataset.id == identifier)
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
    ) -> Tuple[Sequence[Dataset], int]:
        stmt = select(Dataset)
        
        if is_active is not None and hasattr(Dataset, "is_active"):
            stmt = stmt.where(Dataset.is_active == is_active)
            
        if search and hasattr(Dataset, "name"):
            stmt = stmt.where(Dataset.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Dataset, sort_by, getattr(Dataset, "created_at", Dataset.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Dataset]) -> List[Dataset]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
