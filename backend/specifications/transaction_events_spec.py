"""Query Specification and Filtering Predicate for TransactionEvent."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.transaction_events import TransactionEvent

class TransactionEventSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(TransactionEvent, "is_active"):
            predicates.append(TransactionEvent.is_active == self.is_active)
        if self.search and hasattr(TransactionEvent, "name"):
            predicates.append(TransactionEvent.name.ilike(f"%{self.search}%"))
        return predicates
