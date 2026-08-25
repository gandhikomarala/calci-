"""Query Specification and Filtering Predicate for ModelMetric."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.model_metrics import ModelMetric

class ModelMetricSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(ModelMetric, "is_active"):
            predicates.append(ModelMetric.is_active == self.is_active)
        if self.search and hasattr(ModelMetric, "name"):
            predicates.append(ModelMetric.name.ilike(f"%{self.search}%"))
        return predicates
