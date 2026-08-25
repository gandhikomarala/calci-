"""Query Specification and Filtering Predicate for Transaction."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.transactions import Transaction

class TransactionSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Transaction, "is_active"):
            predicates.append(Transaction.is_active == self.is_active)
        if self.search and hasattr(Transaction, "name"):
            predicates.append(Transaction.name.ilike(f"%{self.search}%"))
        return predicates
