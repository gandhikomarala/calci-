"""Query Specification and Filtering Predicate for Customer."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.customers import Customer

class CustomerSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Customer, "is_active"):
            predicates.append(Customer.is_active == self.is_active)
        if self.search and hasattr(Customer, "name"):
            predicates.append(Customer.name.ilike(f"%{self.search}%"))
        return predicates
