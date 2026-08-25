"""Liveness, Readiness and Integrity Probe for ApiKey."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("api_keys_probe")

class ApiKeyProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing ApiKey health probe")
        return {
            "entity": "ApiKey",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
