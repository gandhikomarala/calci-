"""FinGuard AI — Main FastAPI Application Gateway."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.config import settings
from backend.core.logging import configure_logging, get_logger
from backend.health.router import router as health_router

configure_logging()
logger = get_logger("finguard_api")

app = FastAPI(
    title="FinGuard AI — Financial Fraud Detection & Risk Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    description="""
    ## FinGuard AI API Reference
    Enterprise financial transaction risk detection, fraud investigation, and MLOps platform.
    """
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Bind Routers
prefix = settings.API_V1_PREFIX
app.include_router(health_router, prefix=prefix)

@app.get("/")
async def root():
    return {
        "name": settings.APP_NAME,
        "status": "OPERATIONAL",
        "docs_url": "/docs",
        "api_prefix": settings.API_V1_PREFIX,
    }
