"""Asynchronous Database Repository for Transaction."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.transactions import Transaction
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("transactions_repo")

class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self, session: AsyncSession):
        super().__init__(Transaction, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Transaction]:
        stmt = select(Transaction).where(Transaction.id == identifier)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_filtered(
        self,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None,
        is_active: Optional[bool] = None,
        sort_by: str = "created_at",
        sort_order: str = "desc"
    ) -> Tuple[Sequence[Transaction], int]:
        stmt = select(Transaction)
        
        if is_active is not None and hasattr(Transaction, "is_active"):
            stmt = stmt.where(Transaction.is_active == is_active)
            
        if search and hasattr(Transaction, "name"):
            stmt = stmt.where(Transaction.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Transaction, sort_by, getattr(Transaction, "created_at", Transaction.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Transaction]) -> List[Transaction]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
