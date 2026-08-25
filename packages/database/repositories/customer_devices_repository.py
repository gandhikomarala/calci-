"""High-Performance Asynchronous Repository for CustomerDevice."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.customer_devices import CustomerDevice
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("customer_devices_repository")

class CustomerDeviceRepository(BaseRepository[CustomerDevice]):
    def __init__(self, session: AsyncSession):
        super().__init__(CustomerDevice, session)

    async def get_by_code(self, code: str) -> Optional[CustomerDevice]:
        stmt = select(CustomerDevice).where(CustomerDevice.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[CustomerDevice]:
        stmt = select(CustomerDevice).where(CustomerDevice.is_active == True).order_by(desc(CustomerDevice.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(CustomerDevice.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
