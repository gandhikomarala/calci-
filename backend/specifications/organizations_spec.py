"""Query Specification and Filtering Predicate for Organization."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.organizations import Organization

class OrganizationSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Organization, "is_active"):
            predicates.append(Organization.is_active == self.is_active)
        if self.search and hasattr(Organization, "name"):
            predicates.append(Organization.name.ilike(f"%{self.search}%"))
        return predicates
