"""Pydantic v2 Schemas for ModelPerformanceLog (Real-time production accuracy, latency, and throughput logs)."""

from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel, Field

class ModelPerformanceLogBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

class ModelPerformanceLogCreate(ModelPerformanceLogBase):
    pass

class ModelPerformanceLogUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class ModelPerformanceLogResponse(ModelPerformanceLogBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ModelPerformanceLogDetailResponse(ModelPerformanceLogResponse):
    extra_details: Optional[Dict[str, Any]] = None

class ModelPerformanceLogFilterParams(BaseModel):
    search: Optional[str] = None
    is_active: Optional[bool] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    sort_by: str = "created_at"
    sort_order: str = "desc"
