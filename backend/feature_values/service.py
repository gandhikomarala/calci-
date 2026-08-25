"""Domain Business Logic Service for FeatureValue."""

from typing import List, Tuple, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.feature_values import FeatureValue
from backend.feature_values.repository import FeatureValueRepository
from backend.feature_values.schemas import FeatureValueCreate, FeatureValueUpdate, FeatureValueResponse, FeatureValueFilterParams
from packages.core.exceptions import NotFoundError, ValidationError

class FeatureValueService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = FeatureValueRepository(session)

    async def list_items(self, params: FeatureValueFilterParams) -> Tuple[Sequence[FeatureValue], int]:
        skip = (params.page - 1) * params.page_size
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> FeatureValue:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            raise NotFoundError(f"FeatureValue with ID '{item_id}' not found")
        return entity

    async def create(self, req: FeatureValueCreate) -> FeatureValue:
        entity = FeatureValue()
        if hasattr(entity, "name") and req.name:
            entity.name = req.name
        if hasattr(entity, "description") and req.description:
            entity.description = req.description
        await self.repo.create(entity)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
