"""FinGuard Domain Exceptions."""

from typing import Any, Dict, Optional

class FinGuardBaseException(Exception):
    def __init__(self, message: str, code: str = "INTERNAL_ERROR", details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

class AuthenticationError(FinGuardBaseException):
    def __init__(self, message: str = "Authentication failed", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="AUTHENTICATION_ERROR", details=details)

class AuthorizationError(FinGuardBaseException):
    def __init__(self, message: str = "Permission denied", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="AUTHORIZATION_ERROR", details=details)

class ValidationError(FinGuardBaseException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="VALIDATION_ERROR", details=details)

class NotFoundError(FinGuardBaseException):
    def __init__(self, message: str = "Resource not found", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="NOT_FOUND", details=details)

class ConflictError(FinGuardBaseException):
    def __init__(self, message: str = "Resource conflict", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="CONFLICT_ERROR", details=details)

class DatasetError(FinGuardBaseException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="DATASET_ERROR", details=details)

class ModelError(FinGuardBaseException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="MODEL_ERROR", details=details)

class PredictionError(FinGuardBaseException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="PREDICTION_ERROR", details=details)

class RiskEngineError(FinGuardBaseException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message, code="RISK_ENGINE_ERROR", details=details)
