"""FastAPI REST API Router for InvestigationEvidence (Evidence items (transaction screenshots, IP logs, device traces))."""

from typing import Optional, List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from packages.core.pagination import paginate_sequence
from packages.core.types import PaginatedResponse
from backend.investigation_evidence.schemas import (
    InvestigationEvidenceResponse,
    InvestigationEvidenceDetailResponse,
    InvestigationEvidenceCreate,
    InvestigationEvidenceUpdate,
    InvestigationEvidenceFilterParams
)
from backend.investigation_evidence.service import InvestigationEvidenceService

router = APIRouter(prefix="/investigation_evidence", tags=["InvestigationEvidence"])

@router.get("", response_model=PaginatedResponse[InvestigationEvidenceResponse])
async def list_items(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Full text search filter"),
    is_active: Optional[bool] = Query(None, description="Filter active/inactive"),
    sort_by: str = Query("created_at", description="Field to sort by"),
    sort_order: str = Query("desc", description="Sort order (asc/desc)"),
    session: AsyncSession = Depends(get_db_session)
):
    service = InvestigationEvidenceService(session)
    params = InvestigationEvidenceFilterParams(
        page=page,
        page_size=page_size,
        search=search,
        is_active=is_active,
        sort_by=sort_by,
        sort_order=sort_order
    )
    items, total = await service.list_items(params)
    return paginate_sequence(items, total, page, page_size)

@router.get("/{item_id}", response_model=InvestigationEvidenceResponse)
async def get_by_id(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = InvestigationEvidenceService(session)
    return await service.get_by_id(item_id)

@router.post("", response_model=InvestigationEvidenceResponse, status_code=status.HTTP_201_CREATED)
async def create_item(req: InvestigationEvidenceCreate, session: AsyncSession = Depends(get_db_session)):
    service = InvestigationEvidenceService(session)
    return await service.create(req)

@router.put("/{item_id}", response_model=InvestigationEvidenceResponse)
async def update_item(item_id: str, req: InvestigationEvidenceUpdate, session: AsyncSession = Depends(get_db_session)):
    service = InvestigationEvidenceService(session)
    return await service.update(item_id, req)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str, session: AsyncSession = Depends(get_db_session)):
    service = InvestigationEvidenceService(session)
    await service.delete(item_id)
