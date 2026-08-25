"""High-Performance Asynchronous Repository for Organization."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.organizations import Organization
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("organizations_repository")

class OrganizationRepository(BaseRepository[Organization]):
    def __init__(self, session: AsyncSession):
        super().__init__(Organization, session)

    async def get_by_code(self, code: str) -> Optional[Organization]:
        stmt = select(Organization).where(Organization.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Organization]:
        stmt = select(Organization).where(Organization.is_active == True).order_by(desc(Organization.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Organization.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
