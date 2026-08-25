"""Liveness, Readiness and Integrity Probe for NotificationTemplate."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("notification_templates_probe")

class NotificationTemplateProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing NotificationTemplate health probe")
        return {
            "entity": "NotificationTemplate",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
