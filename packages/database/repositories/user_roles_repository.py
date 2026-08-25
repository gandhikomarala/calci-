"""High-Performance Asynchronous Repository for UserRole."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.user_roles import UserRole
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("user_roles_repository")

class UserRoleRepository(BaseRepository[UserRole]):
    def __init__(self, session: AsyncSession):
        super().__init__(UserRole, session)

    async def get_by_code(self, code: str) -> Optional[UserRole]:
        stmt = select(UserRole).where(UserRole.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[UserRole]:
        stmt = select(UserRole).where(UserRole.is_active == True).order_by(desc(UserRole.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(UserRole.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
