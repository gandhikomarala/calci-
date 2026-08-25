"""FastAPI REST API Router for MerchantCategory (Merchant MCC classification and high-risk category definitions)."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.merchant_categories.schemas import (
    MerchantCategoryResponse,
    MerchantCategoryDetailResponse,
    MerchantCategoryCreate,
    MerchantCategoryUpdate,
    MerchantCategoryFilterParams
)
from backend.merchant_categories.service import MerchantCategoryService

router = APIRouter(prefix="/merchant_categories", tags=["MerchantCategory"])

@router.get("", response_model=PaginatedResponse[MerchantCategoryResponse])
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Full text search filter"),
    is_active: Optional[bool] = Query(None, description="Filter active/inactive"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    sort_order: str = Query("desc", description="Sort order (asc/desc)"),
    session: AsyncSession = Depends(get_db_session)
):
    service = MerchantCategoryService(session)
    params = MerchantCategoryFilterParams(
        page=page,
        page_size=page_size,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order
    )
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=MerchantCategoryResponse)
async def get_by_id(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = MerchantCategoryService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=MerchantCategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: MerchantCategoryCreate, session: AsyncSession = Depends(get_db_session)):
    service = MerchantCategoryService(session)
    return await service.create(req)

@router.put("/{item_id}", response_model=MerchantCategoryResponse)
async def update_item(item_id: str, req: MerchantCategoryUpdate, session: AsyncSession = Depends(get_db_session)):
    service = MerchantCategoryService(session)
    return await service.update(item_id, req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = MerchantCategoryService(session)
    await service.delete(item_id)
