"""Domain Event Publisher and Audit Dispatcher for ModelMetric."""

import datetime
from typing import Dict, Any, Optional
from backend.core.logging import get_logger

logger = get_logger("model_metrics_events")

class ModelMetricEventHandler:
    @staticmethod
    async def publish_created(entity_id: str, payload: Dict[str, Any], actor_id: Optional[str] = None) -> None:
        logger.info("ModelMetric created event emitted", entity_id=entity_id, actor_id=actor_id)

    @staticmethod
    async def publish_updated(entity_id: str, changes: Dict[str, Any], actor_id: Optional[str] = None) -> None:
        logger.info("ModelMetric updated event emitted", entity_id=entity_id, actor_id=actor_id)

    @staticmethod
    async def publish_deleted(entity_id: str, actor_id: Optional[str] = None) -> None:
        logger.info("ModelMetric deleted event emitted", entity_id=entity_id, actor_id=actor_id)
