from typing import Optional, List, Tuple, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc
from packages.database.models.datasets import Dataset, DatasetVersion, DataSource, DataQualityReport, IngestionJob
from packages.database.repository import BaseRepository

class DatasetRepository(BaseRepository[Dataset]):
    def __init__(self, session: AsyncSession):
        super().__init__(Dataset, session)

    async def get_with_versions(self, dataset_id: str) -> Optional[Tuple[Dataset, Sequence[DatasetVersion]]]:
        stmt = select(Dataset).where(Dataset.id == dataset_id, Dataset.is_deleted == False)
        res = await self.session.execute(stmt)
        dataset = res.scalars().first()
        if not dataset:
            return None

        ver_stmt = select(DatasetVersion).where(DatasetVersion.dataset_id == dataset.id).order_by(desc(DatasetVersion.version_number))
        ver_res = await self.session.execute(ver_stmt)
        return dataset, ver_res.scalars().all()

    async def get_latest_version(self, dataset_id: str) -> Optional[DatasetVersion]:
        stmt = select(DatasetVersion).where(
            DatasetVersion.dataset_id == dataset_id
        ).order_by(desc(DatasetVersion.version_number)).limit(1)
        res = await self.session.execute(stmt)
        return res.scalars().first()

    async def get_quality_report(self, version_id: str) -> Optional[DataQualityReport]:
        stmt = select(DataQualityReport).where(DataQualityReport.dataset_version_id == version_id)
        res = await self.session.execute(stmt)
        return res.scalars().first()
