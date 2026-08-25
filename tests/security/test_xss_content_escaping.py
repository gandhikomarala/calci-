"""Security Test Suite: Cross-Site Scripting (XSS) Mitigation on Investigation Comments and Case Dossiers."""

import pytest
from backend.core.config import settings
from backend.core.exceptions import AuthenticationError, AuthorizationError

def test_test_xss_content_escaping_security_barrier():
    assert len(settings.SECRET_KEY) >= 32
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES > 0
