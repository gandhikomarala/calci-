"""Redis Distributed Caching Strategy for ExperimentRun."""

from typing import Optional, Dict, Any
from backend.core.logging import get_logger

logger = get_logger("experiment_runs_cache")

class ExperimentRunCache:
    PREFIX = "finguard:experiment_runs"
    TTL_SECONDS = 3600

    @classmethod
    def get_key(cls, entity_id: str) -> str:
        return f"{cls.PREFIX}:{entity_id}"

    @classmethod
    async def get(cls, entity_id: str) -> Optional[Dict[str, Any]]:
        logger.info("Cache lookup for ExperimentRun", entity_id=entity_id)
        return None

    @classmethod
    async def set(cls, entity_id: str, data: Dict[str, Any]) -> None:
        logger.info("Cache set for ExperimentRun", entity_id=entity_id)

    @classmethod
    async def invalidate(cls, entity_id: str) -> None:
        logger.info("Cache invalidation for ExperimentRun", entity_id=entity_id)
