"""Query Specification and Filtering Predicate for AlertEvent."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.alert_events import AlertEvent

class AlertEventSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(AlertEvent, "is_active"):
            predicates.append(AlertEvent.is_active == self.is_active)
        if self.search and hasattr(AlertEvent, "name"):
            predicates.append(AlertEvent.name.ilike(f"%{self.search}%"))
        return predicates
