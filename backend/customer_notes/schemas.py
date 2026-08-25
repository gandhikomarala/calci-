"""Pydantic v2 Schemas for CustomerNote (Internal CSM notes and customer timeline remarks)."""

from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel, Field

class CustomerNoteBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

class CustomerNoteCreate(CustomerNoteBase):
    pass

class CustomerNoteUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class CustomerNoteResponse(CustomerNoteBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class CustomerNoteDetailResponse(CustomerNoteResponse):
    extra_details: Optional[Dict[str, Any]] = None

class CustomerNoteFilterParams(BaseModel):
    search: Optional[str] = None
    is_active: Optional[bool] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    sort_by: str = "created_at"
    sort_order: str = "desc"
