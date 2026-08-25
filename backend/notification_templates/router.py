"""FastAPI REST API Router for NotificationTemplate (Configurable alert notification message templates)."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.notification_templates.schemas import (
    NotificationTemplateResponse,
    NotificationTemplateDetailResponse,
    NotificationTemplateCreate,
    NotificationTemplateUpdate,
    NotificationTemplateFilterParams
)
from backend.notification_templates.service import NotificationTemplateService

router = APIRouter(prefix="/notification_templates", tags=["NotificationTemplate"])

@router.get("", response_model=PaginatedResponse[NotificationTemplateResponse])
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Full text search filter"),
    is_active: Optional[bool] = Query(None, description="Filter active/inactive"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    sort_order: str = Query("desc", description="Sort order (asc/desc)"),
    session: AsyncSession = Depends(get_db_session)
):
    service = NotificationTemplateService(session)
    params = NotificationTemplateFilterParams(
        page=page,
        page_size=page_size,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order
    )
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=NotificationTemplateResponse)
async def get_by_id(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = NotificationTemplateService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=NotificationTemplateResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: NotificationTemplateCreate, session: AsyncSession = Depends(get_db_session)):
    service = NotificationTemplateService(session)
    return await service.create(req)

@router.put("/{item_id}", response_model=NotificationTemplateResponse)
async def update_item(item_id: str, req: NotificationTemplateUpdate, session: AsyncSession = Depends(get_db_session)):
    service = NotificationTemplateService(session)
    return await service.update(item_id, req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = NotificationTemplateService(session)
    await service.delete(item_id)
