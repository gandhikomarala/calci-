"""Domain DTO Serialization & Hydration Mapper for ModelPerformance."""

from typing import Dict, Any, List, Optional
import datetime
from backend.model_performance.schemas import ModelPerformanceResponse, ModelPerformanceDetailResponse

class ModelPerformanceMapper:
    @staticmethod
    def to_response_dto(model: Any) -> ModelPerformanceResponse:
        return ModelPerformanceResponse(
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
