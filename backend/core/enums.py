"""FinGuard AI System Enumerations."""

from enum import Enum

class UserRole(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    FRAUD_ANALYST = "FRAUD_ANALYST"
    SENIOR_ANALYST = "SENIOR_ANALYST"
    ML_ENGINEER = "ML_ENGINEER"
    DATA_ENGINEER = "DATA_ENGINEER"
    MANAGER = "MANAGER"
    AUDITOR = "AUDITOR"
    VIEWER = "VIEWER"

class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    ELEVATED = "ELEVATED"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class RiskDecision(str, Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_MONITORING = "ALLOW_WITH_MONITORING"
    REVIEW = "REVIEW"
    CHALLENGE = "CHALLENGE"
    BLOCK = "BLOCK"

class AlertStatus(str, Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    UNDER_REVIEW = "UNDER_REVIEW"
    ESCALATED = "ESCALATED"
    RESOLVED = "RESOLVED"
    DISMISSED = "DISMISSED"

class InvestigationDecision(str, Enum):
    CONFIRMED_FRAUD = "CONFIRMED_FRAUD"
    LIKELY_FRAUD = "LIKELY_FRAUD"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    LEGITIMATE = "LEGITIMATE"
    INCONCLUSIVE = "INCONCLUSIVE"
    ESCALATED = "ESCALATED"

class ModelStage(str, Enum):
    EXPERIMENTAL = "EXPERIMENTAL"
    VALIDATED = "VALIDATED"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"
    ARCHIVED = "ARCHIVED"
    REJECTED = "REJECTED"

class DriftStatus(str, Enum):
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
