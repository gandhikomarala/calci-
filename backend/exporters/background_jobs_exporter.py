"""JSON Schema Exporter & OpenAPI Contract Definition for BackgroundJob."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("background_jobs_exporter")

class BackgroundJobExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "BackgroundJob",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
