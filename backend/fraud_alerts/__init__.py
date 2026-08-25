"""FraudAlert Domain Package for FinGuard AI (Real-time fraud alerts triggered by ML scores or rule violations)."""

from backend.fraud_alerts.router import router as fraud_alerts_router
from backend.fraud_alerts.service import FraudAlertService
from backend.fraud_alerts.repository import FraudAlertRepository
from backend.fraud_alerts.schemas import FraudAlertResponse, FraudAlertCreate, FraudAlertUpdate, FraudAlertFilterParams
