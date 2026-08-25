"""High-Performance Asynchronous Repository for PredictionExplanation."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.prediction_explanations import PredictionExplanation
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("prediction_explanations_repository")

class PredictionExplanationRepository(BaseRepository[PredictionExplanation]):
    def __init__(self, session: AsyncSession):
        super().__init__(PredictionExplanation, session)

    async def get_by_code(self, code: str) -> Optional[PredictionExplanation]:
        stmt = select(PredictionExplanation).where(PredictionExplanation.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[PredictionExplanation]:
        stmt = select(PredictionExplanation).where(PredictionExplanation.is_active == True).order_by(desc(PredictionExplanation.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(PredictionExplanation.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
