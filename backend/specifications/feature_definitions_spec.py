"""Query Specification and Filtering Predicate for FeatureDefinition."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.feature_definitions import FeatureDefinition

class FeatureDefinitionSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(FeatureDefinition, "is_active"):
            predicates.append(FeatureDefinition.is_active == self.is_active)
        if self.search and hasattr(FeatureDefinition, "name"):
            predicates.append(FeatureDefinition.name.ilike(f"%{self.search}%"))
        return predicates
