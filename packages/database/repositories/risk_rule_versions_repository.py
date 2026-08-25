"""High-Performance Asynchronous Repository for RiskRuleVersion."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.risk_rule_versions import RiskRuleVersion
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("risk_rule_versions_repository")

class RiskRuleVersionRepository(BaseRepository[RiskRuleVersion]):
    def __init__(self, session: AsyncSession):
        super().__init__(RiskRuleVersion, session)

    async def get_by_code(self, code: str) -> Optional[RiskRuleVersion]:
        stmt = select(RiskRuleVersion).where(RiskRuleVersion.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[RiskRuleVersion]:
        stmt = select(RiskRuleVersion).where(RiskRuleVersion.is_active == True).order_by(desc(RiskRuleVersion.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(RiskRuleVersion.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
