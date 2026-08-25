"""High-Performance Asynchronous Repository for InvestigationEvent."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.investigation_events import InvestigationEvent
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("investigation_events_repository")

class InvestigationEventRepository(BaseRepository[InvestigationEvent]):
    def __init__(self, session: AsyncSession):
        super().__init__(InvestigationEvent, session)

    async def get_by_code(self, code: str) -> Optional[InvestigationEvent]:
        stmt = select(InvestigationEvent).where(InvestigationEvent.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[InvestigationEvent]:
        stmt = select(InvestigationEvent).where(InvestigationEvent.is_active == True).order_by(desc(InvestigationEvent.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(InvestigationEvent.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
