"""Query Specification and Filtering Predicate for RiskRuleVersion."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.risk_rule_versions import RiskRuleVersion

class RiskRuleVersionSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(RiskRuleVersion, "is_active"):
            predicates.append(RiskRuleVersion.is_active == self.is_active)
        if self.search and hasattr(RiskRuleVersion, "name"):
            predicates.append(RiskRuleVersion.name.ilike(f"%{self.search}%"))
        return predicates
