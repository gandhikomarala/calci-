from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/overview")
async def get_analytics_overview():
    return {
        "total_customers": 10000,
        "churn_rate": 18.4,
        "high_risk_customers": 1420,
        "estimated_revenue_at_risk": 113580.0,
        "model_accuracy": 0.912,
        "model_roc_auc": 0.948,
        "drift_status": "NORMAL",
    }
