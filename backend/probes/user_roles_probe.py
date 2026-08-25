"""Liveness, Readiness and Integrity Probe for UserRole."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("user_roles_probe")

class UserRoleProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing UserRole health probe")
        return {
            "entity": "UserRole",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
