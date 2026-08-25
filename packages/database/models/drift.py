"""Data Drift, Population Stability Index (PSI), and Model Degradation Monitoring."""

import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from packages.database.base import Base
from packages.database.mixins import TimestampMixin

class DriftReport(Base, TimestampMixin):
    __tablename__ = "drift_reports"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    model_version_tag = Column(String(50), nullable=False, index=True)
    drift_status = Column(String(30), default="NORMAL", nullable=False, index=True)
    overall_psi = Column(Float, nullable=False)
    features_drifted_count = Column(Integer, default=0, nullable=False)
    total_features_count = Column(Integer, nullable=False)
    p_value_threshold = Column(Float, default=0.05, nullable=False)
    report_json = Column(Text, nullable=False)

    metrics = relationship("DriftMetric", back_populates="report", cascade="all, delete-orphan")

class DriftMetric(Base, TimestampMixin):
    __tablename__ = "drift_metrics"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    report_id = Column(String(36), ForeignKey("drift_reports.id", ondelete="CASCADE"), nullable=False, index=True)
    feature_name = Column(String(100), nullable=False, index=True)
    psi_value = Column(Float, nullable=False)
    ks_statistic = Column(Float, nullable=True)
    ks_pvalue = Column(Float, nullable=True)
    is_drifted = Column(Boolean, default=False, nullable=False)

    report = relationship("DriftReport", back_populates="metrics")

class ModelPerformanceLog(Base, TimestampMixin):
    __tablename__ = "model_performance_logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    model_version_tag = Column(String(50), nullable=False, index=True)
    timestamp = Column(DateTime(timezone=True), nullable=False, index=True)
    accuracy = Column(Float, nullable=True)
    precision = Column(Float, nullable=True)
    recall = Column(Float, nullable=True)
    f1_score = Column(Float, nullable=True)
    roc_auc = Column(Float, nullable=True)
    avg_latency_ms = Column(Float, nullable=False)
    p95_latency_ms = Column(Float, nullable=False)
    p99_latency_ms = Column(Float, nullable=False)
    total_predictions = Column(Integer, default=0, nullable=False)
    error_count = Column(Integer, default=0, nullable=False)
