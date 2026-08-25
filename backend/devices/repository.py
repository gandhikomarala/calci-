"""Asynchronous Database Repository for Device."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, or_
from packages.database.models.devices import Device
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("devices_repo")

class DeviceRepository(BaseRepository[Device]):
    def __init__(self, session: AsyncSession):
        super().__init__(Device, session)

    async def get_by_identifier(self, identifier: str) -> Optional[Device]:
        stmt = select(Device).where(Device.id == identifier)
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
    ) -> Tuple[Sequence[Device], int]:
        stmt = select(Device)
        
        if is_active is not None and hasattr(Device, "is_active"):
            stmt = stmt.where(Device.is_active == is_active)
            
        if search and hasattr(Device, "name"):
            stmt = stmt.where(Device.name.ilike(f"%{search}%"))

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar_one()

        sort_col = getattr(Device, sort_by, getattr(Device, "created_at", Device.id))
        stmt = stmt.order_by(desc(sort_col) if sort_order == "desc" else asc(sort_col))

        res = await self.session.execute(stmt.offset(skip).limit(limit))
        items = res.scalars().all()
        return items, total

    async def batch_upsert(self, entities: List[Device]) -> List[Device]:
        self.session.add_all(entities)
        await self.session.flush()
        return entities
