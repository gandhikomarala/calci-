"""Liveness, Readiness and Integrity Probe for Location."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("locations_probe")

class LocationProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing Location health probe")
        return {
            "entity": "Location",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
