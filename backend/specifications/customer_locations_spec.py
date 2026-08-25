"""Query Specification and Filtering Predicate for CustomerLocation."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.customer_locations import CustomerLocation

class CustomerLocationSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(CustomerLocation, "is_active"):
            predicates.append(CustomerLocation.is_active == self.is_active)
        if self.search and hasattr(CustomerLocation, "name"):
            predicates.append(CustomerLocation.name.ilike(f"%{self.search}%"))
        return predicates
