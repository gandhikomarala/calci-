"""Query Specification and Filtering Predicate for NotificationTemplate."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.notification_templates import NotificationTemplate

class NotificationTemplateSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(NotificationTemplate, "is_active"):
            predicates.append(NotificationTemplate.is_active == self.is_active)
        if self.search and hasattr(NotificationTemplate, "name"):
            predicates.append(NotificationTemplate.name.ilike(f"%{self.search}%"))
        return predicates
