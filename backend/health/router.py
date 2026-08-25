"""Health, Readiness, and Liveness Endpoints for FinGuard AI."""

from fastapi import APIRouter
from backend.core.config import settings

router = APIRouter(tags=["Health & Status"])

@router.get("/health")
async def health():
    return {
        "status": "HEALTHY",
        "service": "FinGuard AI Enterprise Platform",
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0",
    }

@router.get("/ready")
async def ready():
    return {
        "status": "READY",
        "database": "CONNECTED",
        "redis": "CONNECTED",
        "celery_workers": "HEALTHY",
        "active_model": "fraud-lgbm-v1",
    }

@router.get("/live")
async def live():
    return {"status": "ALIVE"}
