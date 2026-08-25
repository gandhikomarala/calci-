"""System Runtime Settings and Risk Threshold Configuration."""

import uuid
from sqlalchemy import Column, String, Text, Boolean
from packages.database.base import Base
from packages.database.mixins import TimestampMixin

class SystemSetting(Base, TimestampMixin):
    __tablename__ = "system_settings"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    setting_key = Column(String(100), unique=True, nullable=False, index=True)
    setting_value = Column(Text, nullable=False)
    data_type = Column(String(30), default="string", nullable=False)
    category = Column(String(50), default="GENERAL", nullable=False, index=True)
    description = Column(Text, nullable=True)
    is_secret = Column(Boolean, default=False, nullable=False)
