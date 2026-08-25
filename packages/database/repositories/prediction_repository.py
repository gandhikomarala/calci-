from typing import Optional, List, Tuple, Sequence, Dict, Any
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc
from packages.database.models.predictions import Prediction, PredictionBatch, PredictionExplanation
from packages.database.repository import BaseRepository

class PredictionRepository(BaseRepository[Prediction]):
    def __init__(self, session: AsyncSession):
        super().__init__(Prediction, session)

    async def get_recent_predictions(self, limit: int = 50) -> Sequence[Prediction]:
        stmt = select(Prediction).order_by(desc(Prediction.prediction_timestamp)).limit(limit)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def get_prediction_distribution(self, days: int = 7) -> Dict[str, Any]:
        since = datetime.datetime.utcnow() - datetime.timedelta(days=days)
        stmt = select(
            Prediction.risk_level,
            func.count(Prediction.id).label("count"),
            func.avg(Prediction.churn_probability).label("avg_prob")
        ).where(Prediction.prediction_timestamp >= since).group_by(Prediction.risk_level)
        
        res = await self.session.execute(stmt)
        distribution = {}
        for row in res.all():
            distribution[row.risk_level] = {
                "count": row.count,
                "avg_probability": round(float(row.avg_prob or 0.0), 4)
            }
        return distribution
