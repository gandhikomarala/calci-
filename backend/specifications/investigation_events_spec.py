"""Query Specification and Filtering Predicate for InvestigationEvent."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.investigation_events import InvestigationEvent

class InvestigationEventSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(InvestigationEvent, "is_active"):
            predicates.append(InvestigationEvent.is_active == self.is_active)
        if self.search and hasattr(InvestigationEvent, "name"):
            predicates.append(InvestigationEvent.name.ilike(f"%{self.search}%"))
        return predicates
