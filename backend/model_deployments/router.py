"""FastAPI REST API Router for ModelDeployment (Active deployment environments (Staging, Production, Canary))."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.model_deployments.schemas import (
    ModelDeploymentResponse,
    ModelDeploymentDetailResponse,
    ModelDeploymentCreate,
    ModelDeploymentUpdate,
    ModelDeploymentFilterParams
)
from backend.model_deployments.service import ModelDeploymentService

router = APIRouter(prefix="/model_deployments", tags=["ModelDeployment"])

@router.get("", response_model=PaginatedResponse[ModelDeploymentResponse])
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Full text search filter"),
    is_active: Optional[bool] = Query(None, description="Filter active/inactive"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    sort_order: str = Query("desc", description="Sort order (asc/desc)"),
    session: AsyncSession = Depends(get_db_session)
):
    service = ModelDeploymentService(session)
    params = ModelDeploymentFilterParams(
        page=page,
        page_size=page_size,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order
    )
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=ModelDeploymentResponse)
async def get_by_id(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = ModelDeploymentService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=ModelDeploymentResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: ModelDeploymentCreate, session: AsyncSession = Depends(get_db_session)):
    service = ModelDeploymentService(session)
    return await service.create(req)

@router.put("/{item_id}", response_model=ModelDeploymentResponse)
async def update_item(item_id: str, req: ModelDeploymentUpdate, session: AsyncSession = Depends(get_db_session)):
    service = ModelDeploymentService(session)
    return await service.update(item_id, req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = ModelDeploymentService(session)
    await service.delete(item_id)
