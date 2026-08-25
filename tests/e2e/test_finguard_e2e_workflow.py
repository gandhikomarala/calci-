"""FinGuard AI Master End-to-End Integration Scenario Test."""

import pytest
import datetime
import pandas as pd
from scripts.generate_data import generate_financial_dataset
from ml.features.engine import FinGuardFeatureEngine
from ml.models.lightgbm_model import LightGBMFraudModel
from ml.explainability.shap_engine import FinGuardShapEngine
from ml.drift.detector import FinGuardDriftDetector

def test_full_finguard_e2e_lifecycle():
    # 1. Ingest & Generate Synthetic Financial Dataset
    df = generate_financial_dataset(num_transactions=500, seed=42)
    assert len(df) == 500
    assert "is_fraud" in df.columns

    # 2. Feature Engineering Pipeline
    featured_df = FinGuardFeatureEngine.engineer_features(df)
    assert "velocity_1h_val" in featured_df.columns
    assert "amount_deviation_val" in featured_df.columns
    assert "device_risk_scorer_val" in featured_df.columns

    # 3. Train Production LightGBM Classifier
    feature_cols = [c for c in featured_df.columns if c.endswith("_val")]
    X = featured_df[feature_cols]
    y = featured_df["is_fraud"]

    model = LightGBMFraudModel({"n_estimators": 25, "random_state": 42})
    model.fit(X, y)
    assert model.is_trained is True

    # 4. Real-time Transaction Scoring
    sample_txn = X.iloc[[0]]
    probs = model.predict_proba(sample_txn)
    assert probs.shape == (1, 2)
    fraud_prob = float(probs[0, 1])
    assert 0.0 <= fraud_prob <= 1.0

    # 5. Explain Prediction with SHAP
    explainer = FinGuardShapEngine(model.model, feature_cols)
    explanation = explainer.explain_transaction(sample_txn)
    assert "top_positive_factors" in explanation
    assert "feature_contributions" in explanation

    # 6. Statistical Drift Detection
    detector = FinGuardDriftDetector(X, X)
    drift_report = detector.run_drift_analysis()
    assert drift_report["overall_status"] == "NORMAL"
    assert drift_report["max_psi"] == 0.0
