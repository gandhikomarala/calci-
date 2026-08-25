"""FastAPI REST API Router for ModelVersion (Immutable model binary versions, artifact hashes, and metrics)."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.model_versions.schemas import (
    ModelVersionResponse,
    ModelVersionDetailResponse,
    ModelVersionCreate,
    ModelVersionUpdate,
    ModelVersionFilterParams
)
from backend.model_versions.service import ModelVersionService

router = APIRouter(prefix="/model_versions", tags=["ModelVersion"])

@router.get("", response_model=PaginatedResponse[ModelVersionResponse])
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Full text search filter"),
    is_active: Optional[bool] = Query(None, description="Filter active/inactive"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    sort_order: str = Query("desc", description="Sort order (asc/desc)"),
    session: AsyncSession = Depends(get_db_session)
):
    service = ModelVersionService(session)
    params = ModelVersionFilterParams(
        page=page,
        page_size=page_size,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order
    )
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=ModelVersionResponse)
async def get_by_id(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = ModelVersionService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=ModelVersionResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: ModelVersionCreate, session: AsyncSession = Depends(get_db_session)):
    service = ModelVersionService(session)
    return await service.create(req)

@router.put("/{item_id}", response_model=ModelVersionResponse)
async def update_item(item_id: str, req: ModelVersionUpdate, session: AsyncSession = Depends(get_db_session)):
    service = ModelVersionService(session)
    return await service.update(item_id, req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = ModelVersionService(session)
    await service.delete(item_id)
