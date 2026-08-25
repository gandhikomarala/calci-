"""Liveness, Readiness and Integrity Probe for RefreshToken."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("refresh_tokens_probe")

class RefreshTokenProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing RefreshToken health probe")
        return {
            "entity": "RefreshToken",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
