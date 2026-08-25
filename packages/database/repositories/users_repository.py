"""High-Performance Asynchronous Repository for User."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.users import User
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("users_repository")

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_code(self, code: str) -> Optional[User]:
        stmt = select(User).where(User.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[User]:
        stmt = select(User).where(User.is_active == True).order_by(desc(User.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(User.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
