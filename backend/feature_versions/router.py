"""FastAPI REST API Router for FeatureVersion (Versioned schemas of transformed feature spaces)."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.feature_versions.schemas import (
    FeatureVersionResponse,
    FeatureVersionDetailResponse,
    FeatureVersionCreate,
    FeatureVersionUpdate,
    FeatureVersionFilterParams
)
from backend.feature_versions.service import FeatureVersionService

router = APIRouter(prefix="/feature_versions", tags=["FeatureVersion"])

@router.get("", response_model=PaginatedResponse[FeatureVersionResponse])
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Full text search filter"),
    is_active: Optional[bool] = Query(None, description="Filter active/inactive"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    sort_order: str = Query("desc", description="Sort order (asc/desc)"),
    session: AsyncSession = Depends(get_db_session)
):
    service = FeatureVersionService(session)
    params = FeatureVersionFilterParams(
        page=page,
        page_size=page_size,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order
    )
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=FeatureVersionResponse)
async def get_by_id(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = FeatureVersionService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=FeatureVersionResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: FeatureVersionCreate, session: AsyncSession = Depends(get_db_session)):
    service = FeatureVersionService(session)
    return await service.create(req)

@router.put("/{item_id}", response_model=FeatureVersionResponse)
async def update_item(item_id: str, req: FeatureVersionUpdate, session: AsyncSession = Depends(get_db_session)):
    service = FeatureVersionService(session)
    return await service.update(item_id, req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = FeatureVersionService(session)
    await service.delete(item_id)
