"""JSON Schema Exporter & OpenAPI Contract Definition for InvestigationEvidence."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("investigation_evidence_exporter")

class InvestigationEvidenceExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "InvestigationEvidence",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
