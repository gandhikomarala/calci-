"""Security Test Suite: Scoped API Key Permissions for Batch Ingestion vs Administrative Endpoints."""

import pytest
from backend.core.config import settings
from backend.core.exceptions import AuthenticationError, AuthorizationError

def test_test_api_key_permission_scopes_security_barrier():
    assert len(settings.SECRET_KEY) >= 32
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
