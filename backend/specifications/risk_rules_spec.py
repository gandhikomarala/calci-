"""Query Specification and Filtering Predicate for RiskRule."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.risk_rules import RiskRule

class RiskRuleSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(RiskRule, "is_active"):
            predicates.append(RiskRule.is_active == self.is_active)
        if self.search and hasattr(RiskRule, "name"):
            predicates.append(RiskRule.name.ilike(f"%{self.search}%"))
        return predicates
