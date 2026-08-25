"""JSON Schema Exporter & OpenAPI Contract Definition for FeatureVersion."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("feature_versions_exporter")

class FeatureVersionExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "FeatureVersion",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
