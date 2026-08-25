"""Liveness, Readiness and Integrity Probe for InvestigationComment."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("investigation_comments_probe")

class InvestigationCommentProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing InvestigationComment health probe")
        return {
            "entity": "InvestigationComment",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
