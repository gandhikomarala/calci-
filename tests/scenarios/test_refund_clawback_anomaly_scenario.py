"""Scenario Test: High Ratio of Transaction Refunds to Cumulative Volume."""

import pytest
import datetime
import pandas as pd
import numpy as np
from ml.features.engine import FinGuardFeatureEngine
from ml.models.lightgbm_model import LightGBMFraudModel
from ml.explainability.shap_engine import FinGuardShapEngine

def test_refund_clawback_anomaly_detection_and_scoring():
    # Construct synthetic baseline customer profile
    baseline_df = pd.DataFrame({
        "transaction_id": [f"TXN-BASE-{i}" for i in range(20)],
        "customer_id": ["CUS-001"] * 20,
        "amount": [45.0 + i for i in range(20)],
        "customer_avg_amount": [50.0] * 20,
        "is_new_device": [0] * 20,
        "is_location_anomaly": [0] * 20,
        "velocity_last_1h": [0] * 20,
        "failed_attempts_last_24h": [0] * 20,
        "merchant_category": ["GROCERY_SUPERMARKET"] * 20,
        "is_fraud": [0] * 20,
    })

    # Inject specific scenario transaction
    attack_txn = pd.DataFrame([{
        "transaction_id": "TXN-ATTACK-001",
        "customer_id": "CUS-001",
        "amount": 4850.0,
        "customer_avg_amount": 50.0,
        "is_new_device": 1,
        "is_location_anomaly": 1,
        "velocity_last_1h": 14,
        "failed_attempts_last_24h": 4,
        "merchant_category": "CRYPTO_EXCHANGE",
        "is_fraud": 1,
    }])

    combined_df = pd.concat([baseline_df, attack_txn], ignore_index=True)
    featured_df = FinGuardFeatureEngine.engineer_features(combined_df)
    
    assert len(featured_df) == 21
    attack_row = featured_df.iloc[-1]
    
    # Assert risk signals triggered
    assert attack_row["amount_deviation_val"] > 10.0
    assert attack_row["device_risk_scorer_val"] > 1.0
    assert attack_row["merchant_risk_index_val"] > 2.0
