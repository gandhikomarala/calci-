"""High-Performance Asynchronous Repository for Account."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.accounts import Account
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("accounts_repository")

class AccountRepository(BaseRepository[Account]):
    def __init__(self, session: AsyncSession):
        super().__init__(Account, session)

    async def get_by_code(self, code: str) -> Optional[Account]:
        stmt = select(Account).where(Account.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Account]:
        stmt = select(Account).where(Account.is_active == True).order_by(desc(Account.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Account.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
