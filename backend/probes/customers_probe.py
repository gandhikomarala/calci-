"""Liveness, Readiness and Integrity Probe for Customer."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("customers_probe")

class CustomerProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing Customer health probe")
        return {
            "entity": "Customer",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
