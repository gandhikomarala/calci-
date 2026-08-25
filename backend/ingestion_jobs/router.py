"""FastAPI REST Router for IngestionJob (Asynchronous file ingestion and ETL jobs)."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.ingestion_jobs.schemas import IngestionJobResponse, IngestionJobCreate, IngestionJobUpdate, IngestionJobFilterParams
from backend.ingestion_jobs.service import IngestionJobService

router = APIRouter(prefix="/ingestion_jobs", tags=["IngestionJob"])

@router.get("", response_model=PaginatedResponse[IngestionJobResponse])
async def list_all(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
    session: AsyncSession = Depends(get_db_session)
):
    service = IngestionJobService(session)
    params = IngestionJobFilterParams(page=page, page_size=page_size, search=search, sort_by=sort_by, sort_order=sort_order)
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=IngestionJobResponse)
async def get_single(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = IngestionJobService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=IngestionJobResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: IngestionJobCreate, session: AsyncSession = Depends(get_db_session)):
    service = IngestionJobService(session)
    return await service.create(req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = IngestionJobService(session)
    await service.delete(item_id)
