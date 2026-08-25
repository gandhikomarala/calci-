"""Domain Business Logic Service for ModelPerformance."""

from typing import List, Tuple, Optional, Dict, Any, Sequence
import uuid
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.model_performance import ModelPerformance
from backend.model_performance.repository import ModelPerformanceRepository
from backend.model_performance.schemas import (
    ModelPerformanceCreate,
    ModelPerformanceUpdate,
    ModelPerformanceResponse,
    ModelPerformanceFilterParams
)
from backend.core.exceptions import NotFoundError, ValidationError, ConflictError
from backend.core.logging import get_logger

logger = get_logger("model_performance_service")

class ModelPerformanceService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = ModelPerformanceRepository(session)

    async def list_items(self, params: ModelPerformanceFilterParams) -> Tuple[Sequence[ModelPerformance], int]:
        skip = (params.page - 1) * params.page_size
        logger.info("Listing ModelPerformance items", page=params.page, page_size=params.page_size)
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            is_active=params.is_active,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> ModelPerformance:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            logger.warning("ModelPerformance not found", item_id=item_id)
            raise NotFoundError(f"ModelPerformance with ID '{item_id}' was not found")
        return entity

    async def create(self, req: ModelPerformanceCreate) -> ModelPerformance:
        entity = ModelPerformance()
        if hasattr(entity, "id"):
            entity.id = str(uuid.uuid4())
        if hasattr(entity, "name") and req.name is not None:
            entity.name = req.name
        if hasattr(entity, "description") and req.description is not None:
            entity.description = req.description
        if hasattr(entity, "code") and req.code is not None:
            entity.code = req.code
        if hasattr(entity, "is_active"):
            entity.is_active = req.is_active
        if hasattr(entity, "created_at"):
            entity.created_at = datetime.datetime.utcnow()
        if hasattr(entity, "updated_at"):
            entity.updated_at = datetime.datetime.utcnow()

        await self.repo.create(entity)
        logger.info("ModelPerformance created successfully", item_id=getattr(entity, "id", None))
        return entity

    async def update(self, item_id: str, req: ModelPerformanceUpdate) -> ModelPerformance:
        entity = await self.get_by_id(item_id)
        if req.name is not None and hasattr(entity, "name"):
            entity.name = req.name
        if req.description is not None and hasattr(entity, "description"):
            entity.description = req.description
        if req.is_active is not None and hasattr(entity, "is_active"):
            entity.is_active = req.is_active
        if hasattr(entity, "updated_at"):
            entity.updated_at = datetime.datetime.utcnow()

        await self.repo.update(entity)
        logger.info("ModelPerformance updated successfully", item_id=item_id)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
        logger.info("ModelPerformance deleted successfully", item_id=item_id)
