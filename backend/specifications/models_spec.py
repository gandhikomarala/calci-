"""Query Specification and Filtering Predicate for MLModel."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.models import MLModel

class MLModelSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(MLModel, "is_active"):
            predicates.append(MLModel.is_active == self.is_active)
        if self.search and hasattr(MLModel, "name"):
            predicates.append(MLModel.name.ilike(f"%{self.search}%"))
        return predicates
