"""Asynchronous Database Repository for InvestigationEvent."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.investigation_events import InvestigationEvent
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("investigation_events_repo")

class InvestigationEventRepository(BaseRepository[InvestigationEvent]):
    def __init__(self, session: AsyncSession):
        super().__init__(InvestigationEvent, session)

    async def get_by_identifier(self, identifier: str) -> Optional[InvestigationEvent]:
        stmt = select(InvestigationEvent).where(InvestigationEvent.id == identifier)
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
    ) -> Tuple[Sequence[InvestigationEvent], int]:
        stmt = select(InvestigationEvent)
        
        if is_active is not None and hasattr(InvestigationEvent, "is_active"):
            stmt = stmt.where(InvestigationEvent.is_active == is_active)
            
        if search and hasattr(InvestigationEvent, "name"):
            stmt = stmt.where(InvestigationEvent.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(InvestigationEvent, sort_by, getattr(InvestigationEvent, "created_at", InvestigationEvent.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[InvestigationEvent]) -> List[InvestigationEvent]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
