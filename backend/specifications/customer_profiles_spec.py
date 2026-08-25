"""Query Specification and Filtering Predicate for CustomerProfile."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.customer_profiles import CustomerProfile

class CustomerProfileSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(CustomerProfile, "is_active"):
            predicates.append(CustomerProfile.is_active == self.is_active)
        if self.search and hasattr(CustomerProfile, "name"):
            predicates.append(CustomerProfile.name.ilike(f"%{self.search}%"))
        return predicates
