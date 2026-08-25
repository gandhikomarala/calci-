import pytest
from packages.security.hashing import PasswordHasher
from packages.security.jwt import JwtTokenManager
from packages.security.rbac import RBACPermissionManager
from packages.core.enums import UserRoleEnum

def test_password_hashing_and_verification():
    password = "SuperSecretPassword123!"
    hashed = PasswordHasher.hash_password(password)
    assert hashed != password
    assert PasswordHasher.verify_password(password, hashed) is True
    assert PasswordHasher.verify_password("WrongPassword", hashed) is False

def test_jwt_token_generation_and_decoding():
    subject = "user-123"
    roles = ["ML_ENGINEER"]
    permissions = ["model.read", "model.train"]
    
    token = JwtTokenManager.create_access_token(subject, roles, permissions)
    decoded = JwtTokenManager.decode_token(token)
    
    assert decoded["sub"] == subject
    assert decoded["roles"] == roles
    assert "model.train" in decoded["permissions"]

def test_rbac_permission_resolution():
    admin_perms = RBACPermissionManager.get_permissions_for_roles([UserRoleEnum.ADMIN.value])
    assert RBACPermissionManager.has_permission(admin_perms, "customer.read") is True
    assert RBACPermissionManager.has_permission(admin_perms, "model.deploy") is True
    
    viewer_perms = RBACPermissionManager.get_permissions_for_roles([UserRoleEnum.VIEWER.value])
    assert RBACPermissionManager.has_permission(viewer_perms, "customer.read") is True
    assert RBACPermissionManager.has_permission(viewer_perms, "system.configure") is False
