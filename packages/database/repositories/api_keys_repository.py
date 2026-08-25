"""High-Performance Asynchronous Repository for ApiKey."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.api_keys import ApiKey
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("api_keys_repository")

class ApiKeyRepository(BaseRepository[ApiKey]):
    def __init__(self, session: AsyncSession):
        super().__init__(ApiKey, session)

    async def get_by_code(self, code: str) -> Optional[ApiKey]:
        stmt = select(ApiKey).where(ApiKey.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ApiKey]:
        stmt = select(ApiKey).where(ApiKey.is_active == True).order_by(desc(ApiKey.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ApiKey.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
