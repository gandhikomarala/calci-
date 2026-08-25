"""Query Specification and Filtering Predicate for Permission."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.permissions import Permission

class PermissionSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Permission, "is_active"):
            predicates.append(Permission.is_active == self.is_active)
        if self.search and hasattr(Permission, "name"):
            predicates.append(Permission.name.ilike(f"%{self.search}%"))
        return predicates
