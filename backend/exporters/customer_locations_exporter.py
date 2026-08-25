"""JSON Schema Exporter & OpenAPI Contract Definition for CustomerLocation."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("customer_locations_exporter")

class CustomerLocationExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "CustomerLocation",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
