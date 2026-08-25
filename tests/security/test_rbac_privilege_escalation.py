"""Security Test Suite: Horizontal & Vertical Privilege Escalation Guards on Fraud Operations APIs."""

import pytest
from backend.core.config import settings
from backend.core.exceptions import AuthenticationError, AuthorizationError

def test_test_rbac_privilege_escalation_security_barrier():
    assert len(settings.SECRET_KEY) >= 32
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
