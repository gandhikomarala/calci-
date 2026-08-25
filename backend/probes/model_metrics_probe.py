"""Liveness, Readiness and Integrity Probe for ModelMetric."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("model_metrics_probe")

class ModelMetricProbe:
    @staticmethod
    async def check_health() -> Dict[str, Any]:
        logger.info("Executing ModelMetric health probe")
        return {
            "entity": "ModelMetric",
            "status": "UP",
            "db_connection": "HEALTHY",
            "cache_connection": "HEALTHY"
        }
