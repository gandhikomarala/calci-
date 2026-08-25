"""High-Performance Asynchronous Repository for NotificationTemplate."""

from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc, asc, and_, or_
from packages.database.models.notification_templates import NotificationTemplate
from packages.database.repository import BaseRepository
from backend.core.logging import get_logger

logger = get_logger("notification_templates_repository")

class NotificationTemplateRepository(BaseRepository[NotificationTemplate]):
    def __init__(self, session: AsyncSession):
        super().__init__(NotificationTemplate, session)

    async def get_by_code(self, code: str) -> Optional[NotificationTemplate]:
        stmt = select(NotificationTemplate).where(NotificationTemplate.code == code)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def list_active(self, skip: int = 0, limit: int = 50) -> Sequence[NotificationTemplate]:
        stmt = select(NotificationTemplate).where(NotificationTemplate.is_active == True).order_by(desc(NotificationTemplate.created_at)).offset(skip).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def count_total(self) -> int:
        stmt = select(func.count(NotificationTemplate.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()
