"""Query Specification and Filtering Predicate for CustomerDevice."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.customer_devices import CustomerDevice

class CustomerDeviceSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(CustomerDevice, "is_active"):
            predicates.append(CustomerDevice.is_active == self.is_active)
        if self.search and hasattr(CustomerDevice, "name"):
            predicates.append(CustomerDevice.name.ilike(f"%{self.search}%"))
        return predicates
