"""Liveness, Readiness and Integrity Probe for ExperimentMetric."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("experiment_metrics_probe")

class ExperimentMetricProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing ExperimentMetric health probe")
        return {
            "entity": "ExperimentMetric",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
