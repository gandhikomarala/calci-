"""Asynchronous Database Repository for CustomerPayment."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, or_
from packages.database.models.customer_payments import CustomerPayment
from packages.database.repository import BaseRepository

class CustomerPaymentRepository(BaseRepository[CustomerPayment]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomerPayment, session)

    async def get_by_identifier(self, identifier: str) -> Optional[CustomerPayment]:
        stmt = select(CustomerPayment).where(CustomerPayment.id == identifier)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_filtered(
        self,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None,
        sort_by: str = "created_at",
        sort_order: str = "desc"
    ) -> Tuple[Sequence[CustomerPayment], int]:
        stmt = select(CustomerPayment)
        
        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(CustomerPayment, sort_by, CustomerPayment.created_at)
        if sort_order == "desc":
            stmt = stmt.order_by(desc(sort_col))
        else:
            stmt = stmt.order_by(sort_col)

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        return res.scalars().all(), total

    async def batch_create(self, entities: List[CustomerPayment]) -> List[CustomerPayment]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
