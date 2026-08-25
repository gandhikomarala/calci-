"""Permission Domain Package for FinGuard AI (Granular system permissions for fraud operations)."""

from backend.permissions.router import router as permissions_router
from backend.permissions.service import PermissionService
from backend.permissions.repository import PermissionRepository
from backend.permissions.schemas import PermissionResponse, PermissionCreate, PermissionUpdate, PermissionFilterParams
