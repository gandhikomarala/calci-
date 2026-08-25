"""JSON Schema Exporter & OpenAPI Contract Definition for UserSession."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("sessions_exporter")

class UserSessionExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "UserSession",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
