"""Query Specification and Filtering Predicate for DataSource."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.data_sources import DataSource

class DataSourceSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(DataSource, "is_active"):
            predicates.append(DataSource.is_active == self.is_active)
        if self.search and hasattr(DataSource, "name"):
            predicates.append(DataSource.name.ilike(f"%{self.search}%"))
        return predicates
