"""Database model mixins for timestamps, audit logs, and soft deletes."""

import datetime
from sqlalchemy import Column, DateTime, Boolean, String
from sqlalchemy.sql import func

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False, nullable=False, index=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    deleted_by = Column(String(100), nullable=True)

class AuditMixin:
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)
