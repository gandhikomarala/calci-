"""High-Performance Asynchronous Repository for ModelDeployment."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.model_deployments import ModelDeployment
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("model_deployments_repository")

class ModelDeploymentRepository(BaseRepository[ModelDeployment]):
    def __init__(self, session: AsyncSession):
        super().__init__(ModelDeployment, session)

    async def get_by_code(self, code: str) -> Optional[ModelDeployment]:
        stmt = select(ModelDeployment).where(ModelDeployment.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[ModelDeployment]:
        stmt = select(ModelDeployment).where(ModelDeployment.is_active == True).order_by(desc(ModelDeployment.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(ModelDeployment.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
