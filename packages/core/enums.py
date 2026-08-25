"""System enumeration types."""

from enum import Enum

class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"

class UserRoleEnum(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    ML_ENGINEER = "ML_ENGINEER"
    DATA_ENGINEER = "DATA_ENGINEER"
    ANALYST = "ANALYST"
    MANAGER = "MANAGER"
    VIEWER = "VIEWER"

class ChurnRiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class SubscriptionType(str, Enum):
    BASIC = "BASIC"
    STANDARD = "STANDARD"
    PREMIUM = "PREMIUM"
    ENTERPRISE = "ENTERPRISE"

class ContractType(str, Enum):
    MONTH_TO_MONTH = "MONTH_TO_MONTH"
    ONE_YEAR = "ONE_YEAR"
    TWO_YEAR = "TWO_YEAR"

class PaymentMethod(str, Enum):
    CREDIT_CARD = "CREDIT_CARD"
    BANK_TRANSFER = "BANK_TRANSFER"
    PAYPAL = "PAYPAL"
    CRYPTO = "CRYPTO"

class DataFormat(str, Enum):
    CSV = "CSV"
    JSON = "JSON"
    PARQUET = "PARQUET"
    DATABASE = "DATABASE"

class IngestionStatus(str, Enum):
    PENDING = "PENDING"
    UPLOADING = "UPLOADING"
    VALIDATING = "VALIDATING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REJECTED = "REJECTED"

class ModelAlgorithm(str, Enum):
    LOGISTIC_REGRESSION = "LOGISTIC_REGRESSION"
    RANDOM_FOREST = "RANDOM_FOREST"
    GRADIENT_BOOSTING = "GRADIENT_BOOSTING"
    LIGHTGBM = "LIGHTGBM"
    ENSEMBLE = "ENSEMBLE"

class ModelLifecycleStage(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    VALIDATION = "VALIDATION"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"
    ARCHIVED = "ARCHIVED"
    REJECTED = "REJECTED"

class TrainingStatus(str, Enum):
    QUEUED = "QUEUED"
    PREPROCESSING = "PREPROCESSING"
    TRAINING = "TRAINING"
    OPTIMIZING = "OPTIMIZING"
    EVALUATING = "EVALUATING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

class BatchStatus(str, Enum):
    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    PARTIALLY_COMPLETED = "PARTIALLY_COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

class DriftStatus(str, Enum):
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

class AuditAction(str, Enum):
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    CREATE_USER = "CREATE_USER"
    UPDATE_USER = "UPDATE_USER"
    DELETE_USER = "DELETE_USER"
    UPLOAD_DATASET = "UPLOAD_DATASET"
    VALIDATE_DATASET = "VALIDATE_DATASET"
    DELETE_DATASET = "DELETE_DATASET"
    TRAIN_MODEL = "TRAIN_MODEL"
    DEPLOY_MODEL = "DEPLOY_MODEL"
    ROLLBACK_MODEL = "ROLLBACK_MODEL"
    CREATE_PREDICTION = "CREATE_PREDICTION"
    CREATE_BATCH_PREDICTION = "CREATE_BATCH_PREDICTION"
    CHANGE_SETTINGS = "CHANGE_SETTINGS"
    CHANGE_PERMISSIONS = "CHANGE_PERMISSIONS"

class NotificationChannel(str, Enum):
    IN_APP = "IN_APP"
    EMAIL = "EMAIL"
    WEBHOOK = "WEBHOOK"

class NotificationPriority(str, Enum):
    LOW = "LOW"
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
