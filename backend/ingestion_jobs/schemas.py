"""Pydantic v2 Schemas for IngestionJob (Asynchronous file ingestion and ETL jobs)."""

from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel, Field

class IngestionJobBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

class IngestionJobCreate(IngestionJobBase):
    pass

class IngestionJobUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class IngestionJobResponse(IngestionJobBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class IngestionJobDetailResponse(IngestionJobResponse):
    extra_details: Optional[Dict[str, Any]] = None

class IngestionJobFilterParams(BaseModel):
    search: Optional[str] = None
    is_active: Optional[bool] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    sort_by: str = "created_at"
    sort_order: str = "desc"
