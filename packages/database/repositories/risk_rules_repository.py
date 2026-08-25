"""High-Performance Asynchronous Repository for RiskRule."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.risk_rules import RiskRule
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("risk_rules_repository")

class RiskRuleRepository(BaseRepository[RiskRule]):
    def __init__(self, session: AsyncSession):
        super().__init__(RiskRule, session)

    async def get_by_code(self, code: str) -> Optional[RiskRule]:
        stmt = select(RiskRule).where(RiskRule.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[RiskRule]:
        stmt = select(RiskRule).where(RiskRule.is_active == True).order_by(desc(RiskRule.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(RiskRule.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
