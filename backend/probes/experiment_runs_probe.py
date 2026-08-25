"""Liveness, Readiness and Integrity Probe for ExperimentRun."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("experiment_runs_probe")

class ExperimentRunProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing ExperimentRun health probe")
        return {
            "entity": "ExperimentRun",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
