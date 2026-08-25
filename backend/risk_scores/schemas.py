"""Pydantic v2 Schemas for RiskScore (Calculated transaction composite risk scores and decision outcomes)."""

from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel, Field, ConfigDict

class RiskScoreBase(BaseModel):
    name: Optional[str] = Field(default=None, description="Human readable name or title")
    description: Optional[str] = Field(default=None, description="Detailed description")
    code: Optional[str] = Field(default=None, description="Unique domain identifier or reference code")
    is_active: bool = Field(default=True, description="Active status flag")
    metadata_json: Optional[Dict[str, Any]] = Field(default=None, description="Extensible metadata attributes")

class RiskScoreCreate(RiskScoreBase):
    pass

class RiskScoreUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)
    metadata_json: Optional[Dict[str, Any]] = Field(default=None)

class RiskScoreResponse(RiskScoreBase):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(description="Primary UUID identifier")
    created_at: datetime.datetime = Field(description="Timestamp when record was created")
    updated_at: datetime.datetime = Field(description="Timestamp when record was last modified")

class RiskScoreDetailResponse(RiskScoreResponse):
    extra_attributes: Optional[Dict[str, Any]] = Field(default=None)
    audit_history: Optional[List[Dict[str, Any]]] = Field(default=None)

class RiskScoreFilterParams(BaseModel):
    search: Optional[str] = Field(default=None, description="Full text search filter")
    is_active: Optional[bool] = Field(default=None, description="Filter by active status")
    date_from: Optional[datetime.datetime] = Field(default=None, description="Created after timestamp")
    date_to: Optional[datetime.datetime] = Field(default=None, description="Created before timestamp")
    page: int = Field(default=1, ge=1, description="Page number")
    page_size: int = Field(default=20, ge=1, le=100, description="Items per page")
    sort_by: str = Field(default="created_at", description="Field to sort by")
    sort_order: str = Field(default="desc", pattern="^(asc|desc)$", description="Sort order direction")
