from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from packages.database.session import get_db_session
from backend.batches.schemas import BatchJobCreate, BatchJobResponse
from backend.batches.service import BatchPredictionService

router = APIRouter(prefix="/batches", tags=["Batch Predictions"])

@router.get("", response_model=List[BatchJobResponse])
async def list_batches(session: AsyncSession = Depends(get_db_session)):
    service = BatchPredictionService(session)
    return await service.list_batches()

@router.post("", response_model=BatchJobResponse, status_code=status.HTTP_201_CREATED)
async def submit_batch(req: BatchJobCreate, session: AsyncSession = Depends(get_db_session)):
    service = BatchPredictionService(session)
    return await service.create_batch_job(req)
