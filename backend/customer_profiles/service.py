"""Domain Business Logic Service for CustomerProfile."""

from typing import List, Tuple, Optional, Dict, Any, Sequence
import uuid
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.customer_profiles import CustomerProfile
from backend.customer_profiles.repository import CustomerProfileRepository
from backend.customer_profiles.schemas import (
    CustomerProfileCreate,
    CustomerProfileUpdate,
    CustomerProfileResponse,
    CustomerProfileFilterParams
)
from backend.core.exceptions import NotFoundError, ValidationError, ConflictError
from backend.core.logging import get_logger

logger = get_logger("customer_profiles_service")

class CustomerProfileService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = CustomerProfileRepository(session)

    async def list_items(self, params: CustomerProfileFilterParams) -> Tuple[Sequence[CustomerProfile], int]:
        skip = (params.page - 1) * params.page_size
        logger.info("Listing CustomerProfile items", page=params.page, page_size=params.page_size)
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            is_active=params.is_active,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> CustomerProfile:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            logger.warning("CustomerProfile not found", item_id=item_id)
            raise NotFoundError(f"CustomerProfile with ID '{item_id}' was not found")
        return entity

    async def create(self, req: CustomerProfileCreate) -> CustomerProfile:
        entity = CustomerProfile()
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
        logger.info("CustomerProfile created successfully", item_id=getattr(entity, "id", None))
        return entity

    async def update(self, item_id: str, req: CustomerProfileUpdate) -> CustomerProfile:
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
        logger.info("CustomerProfile updated successfully", item_id=item_id)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
        logger.info("CustomerProfile deleted successfully", item_id=item_id)
