"""JSON Schema Exporter & OpenAPI Contract Definition for Transaction."""

from typing import Dict, Any
from backend.core.logging import get_logger

logger = get_logger("transactions_exporter")

class TransactionExporter:
    @staticmethod
    def export_openapi_schema() -> Dict[str, Any]:
        return {
            "title": "Transaction",
            "type": "object",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "name": {"type": "string"},
                "code": {"type": "string"},
                "is_active": {"type": "boolean", "default": True}
            },
            "required": ["id"]
        }
