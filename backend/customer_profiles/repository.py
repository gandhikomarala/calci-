"""Asynchronous Database Repository for CustomerProfile."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.customer_profiles import CustomerProfile
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("customer_profiles_repo")

class CustomerProfileRepository(BaseRepository[CustomerProfile]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomerProfile, session)

    async def get_by_identifier(self, identifier: str) -> Optional[CustomerProfile]:
        stmt = select(CustomerProfile).where(CustomerProfile.id == identifier)
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
    ) -> Tuple[Sequence[CustomerProfile], int]:
        stmt = select(CustomerProfile)
        
        if is_active is not None and hasattr(CustomerProfile, "is_active"):
            stmt = stmt.where(CustomerProfile.is_active == is_active)
            
        if search and hasattr(CustomerProfile, "name"):
            stmt = stmt.where(CustomerProfile.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(CustomerProfile, sort_by, getattr(CustomerProfile, "created_at", CustomerProfile.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[CustomerProfile]) -> List[CustomerProfile]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
