"""Role-Based Access Control and Permission Resolution Engine."""

from typing import List, Set, Callable
from fastapi import Depends, HTTPException, status
from packages.core.enums import UserRoleEnum
from packages.core.exceptions import AuthorizationError

ROLE_PERMISSIONS: dict[str, Set[str]] = {
    UserRoleEnum.SUPER_ADMIN.value: {"*"},
    UserRoleEnum.ADMIN.value: {
        "customer.*", "dataset.*", "model.*", "experiment.*", "prediction.*",
        "analytics.*", "user.read", "user.manage", "system.configure", "audit.read"
    },
    UserRoleEnum.ML_ENGINEER.value: {
        "customer.read", "dataset.read", "dataset.upload", "dataset.validate",
        "model.read", "model.train", "model.deploy", "model.archive",
        "experiment.read", "experiment.create", "prediction.read", "prediction.create",
        "analytics.read", "drift.read", "drift.retrain"
    },
    UserRoleEnum.DATA_ENGINEER.value: {
        "customer.*", "dataset.*", "feature.*", "analytics.read"
    },
    UserRoleEnum.ANALYST.value: {
        "customer.read", "dataset.read", "model.read", "prediction.read",
        "prediction.create", "analytics.read", "reports.generate"
    },
    UserRoleEnum.MANAGER.value: {
        "customer.read", "model.read", "prediction.read", "analytics.read",
        "reports.generate", "audit.read"
    },
    UserRoleEnum.VIEWER.value: {
        "customer.read", "dataset.read", "model.read", "analytics.read"
    },
}

class RBACPermissionManager:
    @staticmethod
    def get_permissions_for_roles(roles: List[str]) -> Set[str]:
        permissions: Set[str] = set()
        for role in roles:
            if role in ROLE_PERMISSIONS:
                permissions.update(ROLE_PERMISSIONS[role])
        return permissions

    @staticmethod
    def has_permission(user_permissions: Set[str], required_permission: str) -> bool:
        if "*" in user_permissions:
            return True
        if required_permission in user_permissions:
            return True
        
        # Check wildcard domains e.g. "customer.*" matches "customer.read"
        domain = required_permission.split(".")[0]
        if f"{domain}.*" in user_permissions:
            return True
            
        return False

def require_permission(permission: str) -> Callable:
    def dependency(current_user: dict = Depends(lambda: {})) -> None:
        user_perms = set(current_user.get("permissions", []))
        if not RBACPermissionManager.has_permission(user_perms, permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Forbidden: Missing required permission '{permission}'"
            )
    return dependency

def require_role(allowed_roles: List[str]) -> Callable:
    def dependency(current_user: dict = Depends(lambda: {})) -> None:
        user_roles = set(current_user.get("roles", []))
        if not user_roles.intersection(set(allowed_roles)):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Forbidden: Requires one of roles {allowed_roles}"
            )
    return dependency
