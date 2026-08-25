"""Pydantic v2 Schemas for CustomerPayment (Payment transaction history, failures, and late penalties)."""

from typing import Optional, List, Dict, Any
import datetime
from pydantic import BaseModel, Field

class CustomerPaymentBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

class CustomerPaymentCreate(CustomerPaymentBase):
    pass

class CustomerPaymentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class CustomerPaymentResponse(CustomerPaymentBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class CustomerPaymentDetailResponse(CustomerPaymentResponse):
    extra_details: Optional[Dict[str, Any]] = None

class CustomerPaymentFilterParams(BaseModel):
    search: Optional[str] = None
    is_active: Optional[bool] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    sort_by: str = "created_at"
    sort_order: str = "desc"
