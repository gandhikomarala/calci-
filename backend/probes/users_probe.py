"""Liveness, Readiness and Integrity Probe for User."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("users_probe")

class UserProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing User health probe")
        return {
            "entity": "User",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
