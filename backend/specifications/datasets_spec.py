"""Query Specification and Filtering Predicate for Dataset."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.datasets import Dataset

class DatasetSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(Dataset, "is_active"):
            predicates.append(Dataset.is_active == self.is_active)
        if self.search and hasattr(Dataset, "name"):
            predicates.append(Dataset.name.ilike(f"%{self.search}%"))
        return predicates
