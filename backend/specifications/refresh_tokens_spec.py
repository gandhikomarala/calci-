"""Query Specification and Filtering Predicate for RefreshToken."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.refresh_tokens import RefreshToken

class RefreshTokenSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(RefreshToken, "is_active"):
            predicates.append(RefreshToken.is_active == self.is_active)
        if self.search and hasattr(RefreshToken, "name"):
            predicates.append(RefreshToken.name.ilike(f"%{self.search}%"))
        return predicates
