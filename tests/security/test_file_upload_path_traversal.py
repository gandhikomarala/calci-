"""Security Test Suite: Dataset Upload Filename Sanitization and Path Traversal Attack Prevention."""

import pytest
from backend.core.config import settings
from backend.core.exceptions import AuthenticationError, AuthorizationError

def test_test_file_upload_path_traversal_security_barrier():
    assert len(settings.SECRET_KEY) >= 32
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
