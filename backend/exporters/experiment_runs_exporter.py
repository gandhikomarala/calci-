"""JSON Schema Exporter & OpenAPI Contract Definition for ExperimentRun."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("experiment_runs_exporter")

class ExperimentRunExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "ExperimentRun",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
