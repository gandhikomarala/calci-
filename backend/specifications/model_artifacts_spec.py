"""Query Specification and Filtering Predicate for ModelArtifact."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.model_artifacts import ModelArtifact

class ModelArtifactSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(ModelArtifact, "is_active"):
            predicates.append(ModelArtifact.is_active == self.is_active)
        if self.search and hasattr(ModelArtifact, "name"):
            predicates.append(ModelArtifact.name.ilike(f"%{self.search}%"))
        return predicates
