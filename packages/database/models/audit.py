"""Immutable Audit Logging Model."""

import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text
from packages.database.base import Base
from packages.database.mixins import TimestampMixin

class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    actor = Column(String(100), nullable=False, index=True)
    action = Column(String(100), nullable=False, index=True)
    resource = Column(String(100), nullable=False, index=True)
    resource_id = Column(String(100), nullable=True, index=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(300), nullable=True)
    status = Column(String(30), default="SUCCESS", nullable=False)
    details_json = Column(Text, nullable=True)
