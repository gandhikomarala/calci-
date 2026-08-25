"""High-Performance Asynchronous Repository for Device."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.devices import Device
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("devices_repository")

class DeviceRepository(BaseRepository[Device]):
    def __init__(self, session: AsyncSession):
        super().__init__(Device, session)

    async def get_by_code(self, code: str) -> Optional[Device]:
        stmt = select(Device).where(Device.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Device]:
        stmt = select(Device).where(Device.is_active == True).order_by(desc(Device.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Device.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
