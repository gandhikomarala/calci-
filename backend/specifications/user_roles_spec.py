"""Query Specification and Filtering Predicate for UserRole."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.user_roles import UserRole

class UserRoleSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(UserRole, "is_active"):
            predicates.append(UserRole.is_active == self.is_active)
        if self.search and hasattr(UserRole, "name"):
            predicates.append(UserRole.name.ilike(f"%{self.search}%"))
        return predicates
