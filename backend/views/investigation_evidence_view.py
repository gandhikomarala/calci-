"""Materialized Analytics View Definition for InvestigationEvidence."""

from typing import Dict, Any, List
from backend.core.logging import get_logger

logger = get_logger("investigation_evidence_view")

class InvestigationEvidenceAnalyticsView:
    @staticmethod
    def get_query_definition() -> str:
        return """
        SELECT
            id,
            name,
            code,
            is_active,
            created_at,
            DATE_TRUNC('hour', created_at) AS time_bucket,
            COUNT(*) OVER() AS total_count
        FROM investigation_evidence
        """

    @staticmethod
    def transform_record(row: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "id": row.get("id"),
            "code": row.get("code"),
            "name": row.get("name"),
            "is_active": bool(row.get("is_active", True)),
            "time_bucket": str(row.get("time_bucket", ""))
        }
