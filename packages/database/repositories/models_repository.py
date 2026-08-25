"""High-Performance Asynchronous Repository for MLModel."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.models import MLModel
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("models_repository")

class MLModelRepository(BaseRepository[MLModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(MLModel, session)

    async def get_by_code(self, code: str) -> Optional[MLModel]:
        stmt = select(MLModel).where(MLModel.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[MLModel]:
        stmt = select(MLModel).where(MLModel.is_active == True).order_by(desc(MLModel.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(MLModel.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
