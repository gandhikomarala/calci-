"""Asynchronous Database Repository for Permission."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.permissions import Permission
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("permissions_repo")

class PermissionRepository(BaseRepository[Permission]):
    def __init__(self, session: AsyncSession):
        super().__init__(Permission, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Permission]:
        stmt = select(Permission).where(Permission.id == identifier)
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
    ) -> Tuple[Sequence[Permission], int]:
        stmt = select(Permission)
        
        if is_active is not None and hasattr(Permission, "is_active"):
            stmt = stmt.where(Permission.is_active == is_active)
            
        if search and hasattr(Permission, "name"):
            stmt = stmt.where(Permission.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Permission, sort_by, getattr(Permission, "created_at", Permission.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Permission]) -> List[Permission]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
