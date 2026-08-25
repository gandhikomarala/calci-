"""Asynchronous Database Repository for Investigation."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.investigations import Investigation
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("investigations_repo")

class InvestigationRepository(BaseRepository[Investigation]):
    def __init__(self, session: AsyncSession):
        super().__init__(Investigation, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Investigation]:
        stmt = select(Investigation).where(Investigation.id == identifier)
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
    ) -> Tuple[Sequence[Investigation], int]:
        stmt = select(Investigation)
        
        if is_active is not None and hasattr(Investigation, "is_active"):
            stmt = stmt.where(Investigation.is_active == is_active)
            
        if search and hasattr(Investigation, "name"):
            stmt = stmt.where(Investigation.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Investigation, sort_by, getattr(Investigation, "created_at", Investigation.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Investigation]) -> List[Investigation]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
