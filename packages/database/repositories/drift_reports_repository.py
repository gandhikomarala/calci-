"""High-Performance Asynchronous Repository for DriftReport."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.drift_reports import DriftReport
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("drift_reports_repository")

class DriftReportRepository(BaseRepository[DriftReport]):
    def __init__(self, session: AsyncSession):
        super().__init__(DriftReport, session)

    async def get_by_code(self, code: str) -> Optional[DriftReport]:
        stmt = select(DriftReport).where(DriftReport.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[DriftReport]:
        stmt = select(DriftReport).where(DriftReport.is_active == True).order_by(desc(DriftReport.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(DriftReport.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
