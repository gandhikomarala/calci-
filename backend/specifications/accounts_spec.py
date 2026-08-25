"""Query Specification and Filtering Predicate for Account."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.accounts import Account

class AccountSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Account, "is_active"):
            predicates.append(Account.is_active == self.is_active)
        if self.search and hasattr(Account, "name"):
            predicates.append(Account.name.ilike(f"%{self.search}%"))
        return predicates
