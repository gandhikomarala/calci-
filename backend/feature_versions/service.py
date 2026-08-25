"""Domain Business Logic Service for FeatureVersion."""

from typing import List, Tuple, Optional, Dict, Any, Sequence
import uuid
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.feature_versions import FeatureVersion
from backend.feature_versions.repository import FeatureVersionRepository
from backend.feature_versions.schemas import (
    FeatureVersionCreate,
    FeatureVersionUpdate,
    FeatureVersionResponse,
    FeatureVersionFilterParams
)
from backend.core.exceptions import NotFoundError, ValidationError, ConflictError
from backend.core.logging import get_logger

logger = get_logger("feature_versions_service")

class FeatureVersionService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = FeatureVersionRepository(session)

    async def list_items(self, params: FeatureVersionFilterParams) -> Tuple[Sequence[FeatureVersion], int]:
        skip = (params.page - 1) * params.page_size
        logger.info("Listing FeatureVersion items", page=params.page, page_size=params.page_size)
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            is_active=params.is_active,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> FeatureVersion:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            logger.warning("FeatureVersion not found", item_id=item_id)
            raise NotFoundError(f"FeatureVersion with ID '{item_id}' was not found")
        return entity

    async def create(self, req: FeatureVersionCreate) -> FeatureVersion:
        entity = FeatureVersion()
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
        logger.info("FeatureVersion created successfully", item_id=getattr(entity, "id", None))
        return entity

    async def update(self, item_id: str, req: FeatureVersionUpdate) -> FeatureVersion:
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
        logger.info("FeatureVersion updated successfully", item_id=item_id)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
        logger.info("FeatureVersion deleted successfully", item_id=item_id)
