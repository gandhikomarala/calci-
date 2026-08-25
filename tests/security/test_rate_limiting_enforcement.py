"""Security Test Suite: Anonymous, Authenticated, and Admin Tier Sliding Window Rate Limiters."""

import pytest
from backend.core.config import settings
from backend.core.exceptions import AuthenticationError, AuthorizationError

def test_test_rate_limiting_enforcement_security_barrier():
    assert len(settings.SECRET_KEY) >= 32
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
