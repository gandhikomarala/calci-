"""High-Performance Asynchronous Repository for RiskScore."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.risk_scores import RiskScore
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("risk_scores_repository")

class RiskScoreRepository(BaseRepository[RiskScore]):
    def __init__(self, session: AsyncSession):
        super().__init__(RiskScore, session)

    async def get_by_code(self, code: str) -> Optional[RiskScore]:
        stmt = select(RiskScore).where(RiskScore.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[RiskScore]:
        stmt = select(RiskScore).where(RiskScore.is_active == True).order_by(desc(RiskScore.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(RiskScore.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
