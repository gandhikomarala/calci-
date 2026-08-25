"""Query Specification and Filtering Predicate for Investigation."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.investigations import Investigation

class InvestigationSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Investigation, "is_active"):
            predicates.append(Investigation.is_active == self.is_active)
        if self.search and hasattr(Investigation, "name"):
            predicates.append(Investigation.name.ilike(f"%{self.search}%"))
        return predicates
