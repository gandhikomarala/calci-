"""Query Specification and Filtering Predicate for Merchant."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.merchants import Merchant

class MerchantSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Merchant, "is_active"):
            predicates.append(Merchant.is_active == self.is_active)
        if self.search and hasattr(Merchant, "name"):
            predicates.append(Merchant.name.ilike(f"%{self.search}%"))
        return predicates
