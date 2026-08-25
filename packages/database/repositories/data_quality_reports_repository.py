"""High-Performance Asynchronous Repository for DataQualityReport."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.data_quality_reports import DataQualityReport
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("data_quality_reports_repository")

class DataQualityReportRepository(BaseRepository[DataQualityReport]):
    def __init__(self, session: AsyncSession):
        super().__init__(DataQualityReport, session)

    async def get_by_code(self, code: str) -> Optional[DataQualityReport]:
        stmt = select(DataQualityReport).where(DataQualityReport.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[DataQualityReport]:
        stmt = select(DataQualityReport).where(DataQualityReport.is_active == True).order_by(desc(DataQualityReport.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(DataQualityReport.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
