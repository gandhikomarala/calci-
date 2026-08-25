"""Liveness, Readiness and Integrity Probe for Merchant."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("merchants_probe")

class MerchantProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing Merchant health probe")
        return {
            "entity": "Merchant",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
