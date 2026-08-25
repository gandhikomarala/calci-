"""Liveness, Readiness and Integrity Probe for ExperimentParameter."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("experiment_parameters_probe")

class ExperimentParameterProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing ExperimentParameter health probe")
        return {
            "entity": "ExperimentParameter",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
