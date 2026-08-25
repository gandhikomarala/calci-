"""Query Specification and Filtering Predicate for MonitoringMetric."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.monitoring_metrics import MonitoringMetric

class MonitoringMetricSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(MonitoringMetric, "is_active"):
            predicates.append(MonitoringMetric.is_active == self.is_active)
        if self.search and hasattr(MonitoringMetric, "name"):
            predicates.append(MonitoringMetric.name.ilike(f"%{self.search}%"))
        return predicates
