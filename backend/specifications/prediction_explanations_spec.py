"""Query Specification and Filtering Predicate for PredictionExplanation."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.prediction_explanations import PredictionExplanation

class PredictionExplanationSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(PredictionExplanation, "is_active"):
            predicates.append(PredictionExplanation.is_active == self.is_active)
        if self.search and hasattr(PredictionExplanation, "name"):
            predicates.append(PredictionExplanation.name.ilike(f"%{self.search}%"))
        return predicates
