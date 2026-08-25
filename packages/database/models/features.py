"""Feature Store, Feature Sets, and Feature Versioning Models."""

import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from packages.database.base import Base
from packages.database.mixins import TimestampMixin

class FeatureSet(Base, TimestampMixin):
    __tablename__ = "feature_sets"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(150), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    entity_name = Column(String(50), default="customer", nullable=False)

    features = relationship("Feature", back_populates="feature_set", cascade="all, delete-orphan")
    versions = relationship("FeatureVersion", back_populates="feature_set", cascade="all, delete-orphan")

class Feature(Base, TimestampMixin):
    __tablename__ = "features"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    feature_set_id = Column(String(36), ForeignKey("feature_sets.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(100), nullable=False, index=True)
    data_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    transformation_logic = Column(Text, nullable=True)
    is_target = Column(Boolean, default=False, nullable=False)

    feature_set = relationship("FeatureSet", back_populates="features")

class FeatureVersion(Base, TimestampMixin):
    __tablename__ = "feature_versions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    feature_set_id = Column(String(36), ForeignKey("feature_sets.id", ondelete="CASCADE"), nullable=False, index=True)
    version_number = Column(Integer, nullable=False)
    schema_definition = Column(Text, nullable=False)
    feature_count = Column(Integer, nullable=False)

    feature_set = relationship("FeatureSet", back_populates="versions")

class FeatureValue(Base, TimestampMixin):
    __tablename__ = "feature_values"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    feature_version_id = Column(String(36), ForeignKey("feature_versions.id", ondelete="CASCADE"), nullable=False, index=True)
    entity_id = Column(String(50), nullable=False, index=True)
    features_json = Column(Text, nullable=False)
