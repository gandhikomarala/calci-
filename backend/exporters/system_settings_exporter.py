"""JSON Schema Exporter & OpenAPI Contract Definition for SystemSetting."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("system_settings_exporter")

class SystemSettingExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "SystemSetting",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
