"""Query Specification and Filtering Predicate for DriftReport."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.drift_reports import DriftReport

class DriftReportSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(DriftReport, "is_active"):
            predicates.append(DriftReport.is_active == self.is_active)
        if self.search and hasattr(DriftReport, "name"):
            predicates.append(DriftReport.name.ilike(f"%{self.search}%"))
        return predicates
