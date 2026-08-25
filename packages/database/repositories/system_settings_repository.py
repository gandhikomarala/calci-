"""High-Performance Asynchronous Repository for SystemSetting."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.system_settings import SystemSetting
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("system_settings_repository")

class SystemSettingRepository(BaseRepository[SystemSetting]):
    def __init__(self, session: AsyncSession):
        super().__init__(SystemSetting, session)

    async def get_by_code(self, code: str) -> Optional[SystemSetting]:
        stmt = select(SystemSetting).where(SystemSetting.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[SystemSetting]:
        stmt = select(SystemSetting).where(SystemSetting.is_active == True).order_by(desc(SystemSetting.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(SystemSetting.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
