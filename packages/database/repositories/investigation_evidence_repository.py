"""High-Performance Asynchronous Repository for InvestigationEvidence."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.investigation_evidence import InvestigationEvidence
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("investigation_evidence_repository")

class InvestigationEvidenceRepository(BaseRepository[InvestigationEvidence]):
    def __init__(self, session: AsyncSession):
        super().__init__(InvestigationEvidence, session)

    async def get_by_code(self, code: str) -> Optional[InvestigationEvidence]:
        stmt = select(InvestigationEvidence).where(InvestigationEvidence.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[InvestigationEvidence]:
        stmt = select(InvestigationEvidence).where(InvestigationEvidence.is_active == True).order_by(desc(InvestigationEvidence.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(InvestigationEvidence.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
