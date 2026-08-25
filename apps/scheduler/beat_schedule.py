"""Celery Beat Periodic Task Schedules for FinGuard AI."""

from celery.schedules import crontab
from apps.worker.celery_app import celery_app

celery_app.conf.beat_schedule = {
    "run-hourly-drift-detection": {
        "task": "tasks.scheduled_drift_check",
        "schedule": crontab(minute=0),  # Every hour
    },
    "generate-daily-fraud-summary": {
        "task": "tasks.generate_executive_fraud_report",
        "schedule": crontab(hour=0, minute=30),  # Daily at 00:30 UTC
        "args": ("yesterday", "today"),
    },
}
