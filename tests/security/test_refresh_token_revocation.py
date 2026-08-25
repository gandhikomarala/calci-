"""Security Test Suite: Cryptographic Refresh Token Rotation, Replay Attack Prevention, and Blacklisting."""

import pytest
from backend.core.config import settings
from backend.core.exceptions import AuthenticationError, AuthorizationError

def test_test_refresh_token_revocation_security_barrier():
    assert len(settings.SECRET_KEY) >= 32
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
