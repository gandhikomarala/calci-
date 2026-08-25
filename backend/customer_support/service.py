"""Domain Business Logic Service for CustomerSupportTicket."""

from typing import List, Tuple, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.customer_support import CustomerSupportTicket
from backend.customer_support.repository import CustomerSupportTicketRepository
from backend.customer_support.schemas import CustomerSupportTicketCreate, CustomerSupportTicketUpdate, CustomerSupportTicketResponse, CustomerSupportTicketFilterParams
from packages.core.exceptions import NotFoundError, ValidationError

class CustomerSupportTicketService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = CustomerSupportTicketRepository(session)

    async def list_items(self, params: CustomerSupportTicketFilterParams) -> Tuple[Sequence[CustomerSupportTicket], int]:
        skip = (params.page - 1) * params.page_size
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> CustomerSupportTicket:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            raise NotFoundError(f"CustomerSupportTicket with ID '{item_id}' not found")
        return entity

    async def create(self, req: CustomerSupportTicketCreate) -> CustomerSupportTicket:
        entity = CustomerSupportTicket()
        if hasattr(entity, "name") and req.name:
            entity.name = req.name
        if hasattr(entity, "description") and req.description:
            entity.description = req.description
        await self.repo.create(entity)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
