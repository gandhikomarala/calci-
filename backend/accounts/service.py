"""Domain Business Logic Service for Account."""

from typing import List, Tuple, Optional, Dict, Any, Sequence
import uuid
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.models.accounts import Account
from backend.accounts.repository import AccountRepository
from backend.accounts.schemas import (
    AccountCreate,
    AccountUpdate,
    AccountResponse,
    AccountFilterParams
)
from backend.core.exceptions import NotFoundError, ValidationError, ConflictError
from backend.core.logging import get_logger

logger = get_logger("accounts_service")

class AccountService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = AccountRepository(session)

    async def list_items(self, params: AccountFilterParams) -> Tuple[Sequence[Account], int]:
        skip = (params.page - 1) * params.page_size
        logger.info("Listing Account items", page=params.page, page_size=params.page_size)
        return await self.repo.list_filtered(
            skip=skip,
            limit=params.page_size,
            search=params.search,
            is_active=params.is_active,
            sort_by=params.sort_by,
            sort_order=params.sort_order
        )

    async def get_by_id(self, item_id: str) -> Account:
        entity = await self.repo.get_by_id(item_id)
        if not entity:
            logger.warning("Account not found", item_id=item_id)
            raise NotFoundError(f"Account with ID '{item_id}' was not found")
        return entity

    async def create(self, req: AccountCreate) -> Account:
        entity = Account()
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
        logger.info("Account created successfully", item_id=getattr(entity, "id", None))
        return entity

    async def update(self, item_id: str, req: AccountUpdate) -> Account:
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
        logger.info("Account updated successfully", item_id=item_id)
        return entity

    async def delete(self, item_id: str) -> None:
        entity = await self.get_by_id(item_id)
        await self.repo.delete(entity)
        logger.info("Account deleted successfully", item_id=item_id)
