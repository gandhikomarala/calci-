from typing import Optional, List, Tuple, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from packages.database.models.drift import DriftReport, DriftMetric, ModelPerformanceLog
from packages.database.repository import BaseRepository

class DriftRepository(BaseRepository[DriftReport]):
    def __init__(self, session: AsyncSession):
        super().__init__(DriftReport, session)

    async def get_latest_report(self) -> Optional[Tuple[DriftReport, Sequence[DriftMetric]]]:
        stmt = select(DriftReport).order_by(desc(DriftReport.created_at)).limit(1)
        res = await self.session.execute(stmt)
        report = res.scalars().first()
        if not report:
            return None

        metric_stmt = select(DriftMetric).where(DriftMetric.report_id == report.id)
        metric_res = await self.session.execute(metric_stmt)
        return report, metric_res.scalars().all()
