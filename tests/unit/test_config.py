import pytest
from backend.core.config import settings

def test_settings_loaded():
    assert settings.APP_PORT == 8000
    assert settings.API_V1_PREFIX == "/api/v1"
    assert settings.AUTO_BLOCK_RISK_THRESHOLD == 85.0
