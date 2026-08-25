"""UserRole Domain Package for FinGuard AI (Role binding matrix and tenant assignment)."""

from backend.user_roles.router import router as user_roles_router
from backend.user_roles.service import UserRoleService
from backend.user_roles.repository import UserRoleRepository
from backend.user_roles.schemas import UserRoleResponse, UserRoleCreate, UserRoleUpdate, UserRoleFilterParams
