"""JSON Schema Exporter & OpenAPI Contract Definition for Experiment."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("experiments_exporter")

class ExperimentExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "Experiment",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
