"""High-Performance Asynchronous Repository for CustomerProfile."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.customer_profiles import CustomerProfile
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("customer_profiles_repository")

class CustomerProfileRepository(BaseRepository[CustomerProfile]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomerProfile, session)

    async def get_by_code(self, code: str) -> Optional[CustomerProfile]:
        stmt = select(CustomerProfile).where(CustomerProfile.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[CustomerProfile]:
        stmt = select(CustomerProfile).where(CustomerProfile.is_active == True).order_by(desc(CustomerProfile.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(CustomerProfile.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
