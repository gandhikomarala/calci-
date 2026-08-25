"""High-Performance Asynchronous Repository for CustomerLocation."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.customer_locations import CustomerLocation
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("customer_locations_repository")

class CustomerLocationRepository(BaseRepository[CustomerLocation]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomerLocation, session)

    async def get_by_code(self, code: str) -> Optional[CustomerLocation]:
        stmt = select(CustomerLocation).where(CustomerLocation.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[CustomerLocation]:
        stmt = select(CustomerLocation).where(CustomerLocation.is_active == True).order_by(desc(CustomerLocation.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(CustomerLocation.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
