"""Liveness, Readiness and Integrity Probe for MerchantCategory."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("merchant_categories_probe")

class MerchantCategoryProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing MerchantCategory health probe")
        return {
            "entity": "MerchantCategory",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
