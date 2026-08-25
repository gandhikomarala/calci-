"""Query Specification and Filtering Predicate for InvestigationAssignment."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.investigation_assignments import InvestigationAssignment

class InvestigationAssignmentSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(InvestigationAssignment, "is_active"):
            predicates.append(InvestigationAssignment.is_active == self.is_active)
        if self.search and hasattr(InvestigationAssignment, "name"):
            predicates.append(InvestigationAssignment.name.ilike(f"%{self.search}%"))
        return predicates
