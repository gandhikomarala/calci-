"""Redis Distributed Caching Strategy for InvestigationComment."""

from typing import Optional, Dict, Any
from backend.core.logging import get_logger

logger = get_logger("investigation_comments_cache")

class InvestigationCommentCache:
    PREFIX = "finguard:investigation_comments"
    TTL_SECONDS = 3600

    @classmethod
    def get_key(cls, entity_id: str) -> str:
        return f"{cls.PREFIX}:{entity_id}"

    @classmethod
    async def get(cls, entity_id: str) -> Optional[Dict[str, Any]]:
        logger.info("Cache lookup for InvestigationComment", entity_id=entity_id)
        return None

    @classmethod
    async def set(cls, entity_id: str, data: Dict[str, Any]) -> None:
        logger.info("Cache set for InvestigationComment", entity_id=entity_id)

    @classmethod
    async def invalidate(cls, entity_id: str) -> None:
        logger.info("Cache invalidation for InvestigationComment", entity_id=entity_id)
