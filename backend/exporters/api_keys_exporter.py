"""JSON Schema Exporter & OpenAPI Contract Definition for ApiKey."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("api_keys_exporter")

class ApiKeyExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "ApiKey",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
