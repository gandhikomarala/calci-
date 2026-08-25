"""Query Specification and Filtering Predicate for AuditLog."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.audit_logs import AuditLog

class AuditLogSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(AuditLog, "is_active"):
            predicates.append(AuditLog.is_active == self.is_active)
        if self.search and hasattr(AuditLog, "name"):
            predicates.append(AuditLog.name.ilike(f"%{self.search}%"))
        return predicates
