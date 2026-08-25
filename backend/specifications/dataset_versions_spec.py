"""Query Specification and Filtering Predicate for DatasetVersion."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.dataset_versions import DatasetVersion

class DatasetVersionSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(DatasetVersion, "is_active"):
            predicates.append(DatasetVersion.is_active == self.is_active)
        if self.search and hasattr(DatasetVersion, "name"):
            predicates.append(DatasetVersion.name.ilike(f"%{self.search}%"))
        return predicates
