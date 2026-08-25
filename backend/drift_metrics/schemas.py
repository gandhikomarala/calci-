"""Pydantic v2 Schemas for DriftMetric (Feature-level Population Stability Index and KS-test metrics)."""

from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel, Field

class DriftMetricBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

class DriftMetricCreate(DriftMetricBase):
    pass

class DriftMetricUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class DriftMetricResponse(DriftMetricBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class DriftMetricDetailResponse(DriftMetricResponse):
    extra_details: Optional[Dict[str, Any]] = None

class DriftMetricFilterParams(BaseModel):
    search: Optional[str] = None
    is_active: Optional[bool] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    sort_by: str = "created_at"
    sort_order: str = "desc"
