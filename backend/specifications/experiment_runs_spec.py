"""Query Specification and Filtering Predicate for ExperimentRun."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.experiment_runs import ExperimentRun

class ExperimentRunSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(ExperimentRun, "is_active"):
            predicates.append(ExperimentRun.is_active == self.is_active)
        if self.search and hasattr(ExperimentRun, "name"):
            predicates.append(ExperimentRun.name.ilike(f"%{self.search}%"))
        return predicates
