from typing import List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from packages.database.models.predictions import PredictionBatch
from backend.batches.schemas import BatchJobCreate, BatchJobResponse

class BatchPredictionService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_batches(self, limit: int = 50) -> List[PredictionBatch]:
        stmt = select(PredictionBatch).order_by(desc(PredictionBatch.created_at)).limit(limit)
        res = await self.session.execute(stmt)
        return list(res.scalars().all())

    async def create_batch_job(self, req: BatchJobCreate) -> PredictionBatch:
        batch = PredictionBatch(
            batch_name=req.batch_name,
            model_version_tag=req.model_version_tag,
            input_file_path=req.input_file_path,
            status="QUEUED",
            total_records=0,
            processed_records=0,
            successful_records=0,
            failed_records=0,
        )
        self.session.add(batch)
        await self.session.flush()
        return batch
