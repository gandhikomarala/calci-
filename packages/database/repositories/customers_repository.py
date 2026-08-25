"""High-Performance Asynchronous Repository for Customer."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.customers import Customer
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("customers_repository")

class CustomerRepository(BaseRepository[Customer]):
    def __init__(self, session: AsyncSession):
        super().__init__(Customer, session)

    async def get_by_code(self, code: str) -> Optional[Customer]:
        stmt = select(Customer).where(Customer.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Customer]:
        stmt = select(Customer).where(Customer.is_active == True).order_by(desc(Customer.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Customer.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
