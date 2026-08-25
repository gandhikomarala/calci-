import pytest
import pandas as pd
import numpy as np
from ml.features.engine import FeatureEngineeringEngine

def test_feature_engineering_transforms():
    df = pd.DataFrame({
        "tenure_months": [12, 24, 6],
        "monthly_charge": [50.0, 100.0, 30.0],
        "total_spend": [600.0, 2400.0, 180.0],
        "daily_usage_mins": [30.0, 60.0, 10.0],
        "weekly_usage_mins": [210.0, 420.0, 70.0],
        "session_count_last_30d": [20, 40, 5],
        "login_count_last_30d": [15, 30, 5],
        "ticket_count_last_12m": [2, 1, 5],
        "complaint_count_last_12m": [1, 0, 3],
        "satisfaction_score": [3.5, 4.8, 2.0],
        "payment_failures_last_12m": [1, 0, 3],
        "late_payments_last_12m": [0, 0, 2],
        "email_open_rate": [0.4, 0.8, 0.1],
        "notification_click_rate": [0.2, 0.6, 0.05],
        "days_since_last_activity": [5, 2, 45],
    })

    featured_df = FeatureEngineeringEngine.generate_features(df)

    assert "expected_lifetime_value" in featured_df.columns
    assert "cost_per_tenure_month" in featured_df.columns
    assert "dissatisfaction_index" in featured_df.columns
    assert "payment_risk_score" in featured_df.columns
    assert "digital_engagement_composite" in featured_df.columns
    assert "is_inactive_30d" in featured_df.columns
    assert featured_df["is_inactive_30d"].iloc[2] == 1
    assert featured_df["is_inactive_30d"].iloc[0] == 0
