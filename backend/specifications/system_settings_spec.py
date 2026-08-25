"""Query Specification and Filtering Predicate for SystemSetting."""

from typing import Any, List, Optional
from sqlalchemy import and_, or_, select, Column
from packages.database.models.system_settings import SystemSetting

class SystemSettingSpecification:
    def __init__(self, search: Optional[str] = None, is_active: Optional[bool] = None):
        self.search = search
        self.is_active = is_active

    def to_predicates(self) -> List[Any]:
        predicates = []
        if self.is_active is not None and hasattr(SystemSetting, "is_active"):
            predicates.append(SystemSetting.is_active == self.is_active)
        if self.search and hasattr(SystemSetting, "name"):
            predicates.append(SystemSetting.name.ilike(f"%{self.search}%"))
        return predicates
