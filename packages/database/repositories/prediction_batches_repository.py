"""High-Performance Asynchronous Repository for PredictionBatch."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.prediction_batches import PredictionBatch
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("prediction_batches_repository")

class PredictionBatchRepository(BaseRepository[PredictionBatch]):
    def __init__(self, session: AsyncSession):
        super().__init__(PredictionBatch, session)

    async def get_by_code(self, code: str) -> Optional[PredictionBatch]:
        stmt = select(PredictionBatch).where(PredictionBatch.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[PredictionBatch]:
        stmt = select(PredictionBatch).where(PredictionBatch.is_active == True).order_by(desc(PredictionBatch.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(PredictionBatch.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
