from fastapi import APIRouter

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])

@router.get("/metrics")
async def get_monitoring_metrics():
    return {
        "model_version": "lightgbm-v1",
        "accuracy": 0.912,
        "f1_score": 0.894,
        "roc_auc": 0.948,
        "avg_latency_ms": 4.2,
        "p95_latency_ms": 8.5,
        "p99_latency_ms": 14.1,
        "total_predictions_today": 45120,
        "error_rate": 0.001,
    }
