"""Strongly typed Pydantic v2 Application Configuration for FinGuard AI."""

from functools import lru_cache
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Server
    ENVIRONMENT: str = Field(default="development")
    DEBUG: bool = Field(default=True)
    APP_NAME: str = Field(default="FinGuard AI — Enterprise Fraud Detection & Risk Intelligence Platform")
    APP_HOST: str = Field(default="0.0.0.0")
    APP_PORT: int = Field(default=8000)
    API_V1_PREFIX: str = Field(default="/api/v1")
    SECRET_KEY: str = Field(default="finguard-ai-enterprise-secret-key-32-chars-long")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7)
    ALGORITHM: str = Field(default="HS256")

    # Database
    POSTGRES_SERVER: str = Field(default="localhost")
    POSTGRES_PORT: int = Field(default=5432)
    POSTGRES_USER: str = Field(default="finguard_admin")
    POSTGRES_PASSWORD: str = Field(default="finguard_secure_pwd_2026")
    POSTGRES_DB: str = Field(default="finguard_ai_db")
    DATABASE_URL: Optional[str] = Field(default=None)
    DATABASE_SYNC_URL: Optional[str] = Field(default=None)
    DB_POOL_SIZE: int = Field(default=20)
    DB_MAX_OVERFLOW: int = Field(default=10)
    DB_POOL_TIMEOUT: int = Field(default=30)

    # Redis & Celery
    REDIS_HOST: str = Field(default="localhost")
    REDIS_PORT: int = Field(default=6379)
    REDIS_DB: int = Field(default=0)
    REDIS_PASSWORD: Optional[str] = Field(default=None)
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/1")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/2")
    CELERY_TASK_ALWAYS_EAGER: bool = Field(default=False)

    # Storage
    STORAGE_BACKEND: str = Field(default="local")
    LOCAL_STORAGE_DIR: str = Field(default="./data_storage")
    ARTIFACTS_DIR: str = Field(default="./data_storage/artifacts")
    MODELS_DIR: str = Field(default="./data_storage/models")
    DATASETS_DIR: str = Field(default="./data_storage/datasets")
    REPORTS_DIR: str = Field(default="./data_storage/reports")

    # Risk Engine Thresholds
    FRAUD_RISK_LOW_THRESHOLD: float = Field(default=20.0)
    FRAUD_RISK_MEDIUM_THRESHOLD: float = Field(default=40.0)
    FRAUD_RISK_ELEVATED_THRESHOLD: float = Field(default=60.0)
    FRAUD_RISK_HIGH_THRESHOLD: float = Field(default=80.0)
    AUTO_BLOCK_RISK_THRESHOLD: float = Field(default=85.0)

    # Monitoring & Drift
    PROMETHEUS_METRICS_ENABLED: bool = Field(default=True)
    DRIFT_PSI_THRESHOLD_WARNING: float = Field(default=0.10)
    DRIFT_PSI_THRESHOLD_CRITICAL: float = Field(default=0.25)
    DRIFT_KS_PVALUE_THRESHOLD: float = Field(default=0.05)

    # Rate Limiting
    RATE_LIMIT_ANONYMOUS: str = Field(default="60/minute")
    RATE_LIMIT_AUTHENTICATED: str = Field(default="1000/minute")
    RATE_LIMIT_ADMIN: str = Field(default="5000/minute")

    # CORS
    CORS_ORIGINS: List[str] = Field(default=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000", "http://127.0.0.1:5173"])

    def get_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    def get_sync_database_url(self) -> str:
        if self.DATABASE_SYNC_URL:
            return self.DATABASE_SYNC_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
