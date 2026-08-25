"""Domain DTO Serialization & Hydration Mapper for InvestigationEvidence."""

from typing import Dict, Any, List, Optional
import datetime
from backend.investigation_evidence.schemas import InvestigationEvidenceResponse, InvestigationEvidenceDetailResponse

class InvestigationEvidenceMapper:
    @staticmethod
    def to_response_dto(model: Any) -> InvestigationEvidenceResponse:
        return InvestigationEvidenceResponse(
            id=str(getattr(model, "id", "")),
            name=getattr(model, "name", None),
            code=getattr(model, "code", None),
            description=getattr(model, "description", None),
            is_active=bool(getattr(model, "is_active", True)),
            metadata_json=getattr(model, "metadata_json", None),
            created_at=getattr(model, "created_at", datetime.datetime.utcnow()),
            updated_at=getattr(model, "updated_at", datetime.datetime.utcnow()),
        )

    @staticmethod
    def to_dict_summary(model: Any) -> Dict[str, Any]:
        return {
            "id": str(getattr(model, "id", "")),
            "code": getattr(model, "code", None),
            "name": getattr(model, "name", None),
            "is_active": bool(getattr(model, "is_active", True)),
            "created_at": getattr(model, "created_at", datetime.datetime.utcnow()).isoformat() + "Z",
        }
