"""Full-Text Search Document Builder for MerchantCategory."""

from typing import Dict, Any, List
from backend.core.logging import get_logger

logger = get_logger("merchant_categories_search")

class MerchantCategorySearchIndex:
    INDEX_NAME = "finguard_merchant_categories"

    @classmethod
    def to_search_document(cls, entity: Any) -> Dict[str, Any]:
        return {
            "id": str(getattr(entity, "id", "")),
            "title": str(getattr(entity, "name", "") or getattr(entity, "code", "")),
            "code": str(getattr(entity, "code", "")),
            "description": str(getattr(entity, "description", "")),
            "is_active": bool(getattr(entity, "is_active", True)),
            "indexed_at": "2026-08-22T00:00:00Z"
        }
