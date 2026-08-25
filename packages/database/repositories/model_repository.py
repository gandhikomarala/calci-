from typing import Optional, List, Tuple, Sequence, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func, desc
from packages.database.models.models import MLModel, ModelVersion, ModelArtifact, ModelDeployment, DeploymentHistory
from packages.database.repository import BaseRepository

class ModelRepository(BaseRepository[MLModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(MLModel, session)

    async def get_production_model(self) -> Optional[Tuple[MLModel, ModelVersion, ModelDeployment]]:
        stmt = select(MLModel, ModelVersion, ModelDeployment).join(
            ModelVersion, ModelVersion.model_id == MLModel.id
        ).join(
            ModelDeployment, ModelDeployment.model_version_id == ModelVersion.id
        ).where(
            ModelVersion.is_production == True,
            ModelDeployment.is_current == True
        )
        res = await self.session.execute(stmt)
        return res.first()

    async def promote_model(self, version_id: str, stage: str, actor: str) -> None:
        # Demote previous production versions if promoting to PRODUCTION
        if stage == "PRODUCTION":
            await self.session.execute(
                update(ModelVersion).values(is_production=False, stage="STAGING").where(ModelVersion.is_production == True)
            )
            await self.session.execute(
                update(ModelDeployment).values(is_current=False).where(ModelDeployment.is_current == True)
            )
            
            # Set new production version
            await self.session.execute(
                update(ModelVersion).values(is_production=True, stage="PRODUCTION").where(ModelVersion.id == version_id)
            )
            
            deployment = ModelDeployment(
                model_version_id=version_id,
                environment="production",
                deployed_by=actor,
                deployed_at=func.now(),
                is_current=True
            )
            self.session.add(deployment)
        else:
            await self.session.execute(
                update(ModelVersion).values(stage=stage).where(ModelVersion.id == version_id)
            )

        # Log history
        history = DeploymentHistory(
            model_version_id=version_id,
            action=f"PROMOTE_TO_{stage}",
            actor=actor,
            notes=f"Model version transitioned to {stage}"
        )
        self.session.add(history)
        await self.session.flush()
