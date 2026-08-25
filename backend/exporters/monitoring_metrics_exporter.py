"""JSON Schema Exporter & OpenAPI Contract Definition for MonitoringMetric."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("monitoring_metrics_exporter")

class MonitoringMetricExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "MonitoringMetric",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
