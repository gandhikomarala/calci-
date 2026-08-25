"""High-Performance Asynchronous Repository for Permission."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.permissions import Permission
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("permissions_repository")

class PermissionRepository(BaseRepository[Permission]):
    def __init__(self, session: AsyncSession):
        super().__init__(Permission, session)

    async def get_by_code(self, code: str) -> Optional[Permission]:
        stmt = select(Permission).where(Permission.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Permission]:
        stmt = select(Permission).where(Permission.is_active == True).order_by(desc(Permission.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Permission.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
