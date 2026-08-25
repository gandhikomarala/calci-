"""High-Performance Asynchronous Repository for Merchant."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.merchants import Merchant
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("merchants_repository")

class MerchantRepository(BaseRepository[Merchant]):
    def __init__(self, session: AsyncSession):
        super().__init__(Merchant, session)

    async def get_by_code(self, code: str) -> Optional[Merchant]:
        stmt = select(Merchant).where(Merchant.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[Merchant]:
        stmt = select(Merchant).where(Merchant.is_active == True).order_by(desc(Merchant.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(Merchant.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
