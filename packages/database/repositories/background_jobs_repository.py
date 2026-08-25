"""High-Performance Asynchronous Repository for BackgroundJob."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.background_jobs import BackgroundJob
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("background_jobs_repository")

class BackgroundJobRepository(BaseRepository[BackgroundJob]):
    def __init__(self, session: AsyncSession):
        super().__init__(BackgroundJob, session)

    async def get_by_code(self, code: str) -> Optional[BackgroundJob]:
        stmt = select(BackgroundJob).where(BackgroundJob.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[BackgroundJob]:
        stmt = select(BackgroundJob).where(BackgroundJob.is_active == True).order_by(desc(BackgroundJob.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(BackgroundJob.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
