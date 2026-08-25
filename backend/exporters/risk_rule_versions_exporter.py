"""JSON Schema Exporter & OpenAPI Contract Definition for RiskRuleVersion."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("risk_rule_versions_exporter")

class RiskRuleVersionExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "RiskRuleVersion",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
