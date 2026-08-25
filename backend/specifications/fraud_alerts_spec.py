"""Query Specification and Filtering Predicate for FraudAlert."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.fraud_alerts import FraudAlert

class FraudAlertSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(FraudAlert, "is_active"):
            predicates.append(FraudAlert.is_active == self.is_active)
        if self.search and hasattr(FraudAlert, "name"):
            predicates.append(FraudAlert.name.ilike(f"%{self.search}%"))
        return predicates
