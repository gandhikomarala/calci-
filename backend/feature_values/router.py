"""FastAPI REST Router for FeatureValue (Point-in-time materialized feature values)."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.feature_values.schemas import FeatureValueResponse, FeatureValueCreate, FeatureValueUpdate, FeatureValueFilterParams
from backend.feature_values.service import FeatureValueService

router = APIRouter(prefix="/feature_values", tags=["FeatureValue"])

@router.get("", response_model=PaginatedResponse[FeatureValueResponse])
async def list_all(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
    session: AsyncSession = Depends(get_db_session)
):
    service = FeatureValueService(session)
    params = FeatureValueFilterParams(page=page, page_size=page_size, search=search, sort_by=sort_by, sort_order=sort_order)
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=FeatureValueResponse)
async def get_single(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = FeatureValueService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=FeatureValueResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: FeatureValueCreate, session: AsyncSession = Depends(get_db_session)):
    service = FeatureValueService(session)
    return await service.create(req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = FeatureValueService(session)
    await service.delete(item_id)
