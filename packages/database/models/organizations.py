"""SQLAlchemy 2.0 Mapped Entity Model for Organization (Company and institutional tenant registry)."""

import uuid
import datetime
from typing import Optional, Dict, Any, List
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, ForeignKey, Index, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from packages.database.base import Base
from packages.database.mixins import TimestampMixin, SoftDeleteMixin

class Organization(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "organizations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, index=True)
    code: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, unique=True, index=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    metadata_json: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSON, nullable=True)

    __table_args__ = (
        Index("ix_organizations_created_active", "created_at", "is_active"),
    )

    def __repr__(self) -> str:
        return f"<Organization(id='{self.id}', code='{self.code}', is_active={self.is_active})>"
