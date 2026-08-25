"""Query Specification and Filtering Predicate for RiskScore."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.risk_scores import RiskScore

class RiskScoreSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(RiskScore, "is_active"):
            predicates.append(RiskScore.is_active == self.is_active)
        if self.search and hasattr(RiskScore, "name"):
            predicates.append(RiskScore.name.ilike(f"%{self.search}%"))
        return predicates
