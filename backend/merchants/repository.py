"""Asynchronous Database Repository for Merchant."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.merchants import Merchant
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("merchants_repo")

class MerchantRepository(BaseRepository[Merchant]):
    def __init__(self, session: AsyncSession):
        super().__init__(Merchant, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Merchant]:
        stmt = select(Merchant).where(Merchant.id == identifier)
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
    ) -> Tuple[Sequence[Merchant], int]:
        stmt = select(Merchant)
        
        if is_active is not None and hasattr(Merchant, "is_active"):
            stmt = stmt.where(Merchant.is_active == is_active)
            
        if search and hasattr(Merchant, "name"):
            stmt = stmt.where(Merchant.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Merchant, sort_by, getattr(Merchant, "created_at", Merchant.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Merchant]) -> List[Merchant]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
