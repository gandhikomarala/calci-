"""Domain Business Logic Service for CustomerEvent."""

from typing import List, Tuple, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.customer_events import CustomerEvent
from backend.customer_events.repository import CustomerEventRepository
from backend.customer_events.schemas import CustomerEventCreate, CustomerEventUpdate, CustomerEventResponse, CustomerEventFilterParams
from packages.core.exceptions import NotFoundError, ValidationError

class CustomerEventService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = CustomerEventRepository(session)

    async def list_items(self, params: CustomerEventFilterParams) -> Tuple[Sequence[CustomerEvent], int]:
        skip = (params.page - 1) * params.page_size
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> CustomerEvent:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            raise NotFoundError(f"CustomerEvent with ID '{item_id}' not found")
        return entity

    async def create(self, req: CustomerEventCreate) -> CustomerEvent:
        entity = CustomerEvent()
        if hasattr(entity, "name") and req.name:
            entity.name = req.name
        if hasattr(entity, "description") and req.description:
            entity.description = req.description
        await self.repo.create(entity)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
