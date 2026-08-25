"""Domain Authorization & Access Control Policy for Device."""

from typing import Dict, Any, Optional
from backend.core.enums import UserRole
from backend.core.exceptions import AuthorizationError

class DevicePolicy:
    @staticmethod
    def can_read(role: UserRole) -> bool:
        return role in [
            UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.FRAUD_ANALYST,
            UserRole.SENIOR_ANALYST, UserRole.ML_ENGINEER, UserRole.DATA_ENGINEER,
            UserRole.MANAGER, UserRole.AUDITOR, UserRole.VIEWER
        ]

    @staticmethod
    def can_create(role: UserRole) -> bool:
        return role in [UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.FRAUD_ANALYST, UserRole.SENIOR_ANALYST, UserRole.ML_ENGINEER]

    @staticmethod
    def can_update(role: UserRole) -> bool:
        return role in [UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.FRAUD_ANALYST, UserRole.SENIOR_ANALYST]

    @staticmethod
    def can_delete(role: UserRole) -> bool:
        return role in [UserRole.SUPER_ADMIN, UserRole.ADMIN]

    @classmethod
    def assert_can_read(cls, role: UserRole) -> None:
        if not cls.can_read(role):
            raise AuthorizationError("User lacks read permissions for Device")

    @classmethod
    def assert_can_create(cls, role: UserRole) -> None:
        if not cls.can_create(role):
            raise AuthorizationError("User lacks create permissions for Device")
