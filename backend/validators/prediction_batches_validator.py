"""Domain Business Validation & Integrity Guard for PredictionBatch."""

from typing import Dict, Any, List, Optional
from backend.core.exceptions import ValidationError
from backend.core.logging import get_logger

logger = get_logger("prediction_batches_validator")

class PredictionBatchValidator:
    @staticmethod
    def validate_create_payload(data: Dict[str, Any]) -> None:
        logger.info("Validating PredictionBatch creation payload")
        if not isinstance(data, dict):
            raise ValidationError("Payload must be a dictionary")
        if "name" in data and data["name"] is not None:
            if len(data["name"].strip()) == 0:
                raise ValidationError("Field 'name' cannot be blank")
        if "code" in data and data["code"] is not None:
            if len(data["code"].strip()) < 2:
                raise ValidationError("Field 'code' must have at least 2 characters")

    @staticmethod
    def validate_state_transition(current_state: str, new_state: str) -> bool:
        logger.info("Validating PredictionBatch state transition", current=current_state, target=new_state)
        valid_transitions = {
            "NEW": ["ASSIGNED", "DISMISSED"],
            "ASSIGNED": ["UNDER_REVIEW", "ESCALATED"],
            "UNDER_REVIEW": ["RESOLVED", "ESCALATED", "DISMISSED"],
            "ESCALATED": ["RESOLVED", "DISMISSED"],
            "RESOLVED": [],
            "DISMISSED": [],
        }
        allowed = valid_transitions.get(current_state, [])
        if new_state not in allowed and allowed:
            raise ValidationError(f"Invalid transition from '{current_state}' to '{new_state}'")
        return True
