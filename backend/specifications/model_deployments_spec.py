"""Query Specification and Filtering Predicate for ModelDeployment."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.model_deployments import ModelDeployment

class ModelDeploymentSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(ModelDeployment, "is_active"):
            predicates.append(ModelDeployment.is_active == self.is_active)
        if self.search and hasattr(ModelDeployment, "name"):
            predicates.append(ModelDeployment.name.ilike(f"%{self.search}%"))
        return predicates
