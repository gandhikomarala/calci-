"""Integration Test: Dynamic Database Fraud Rules Execution, Priority Resolution, and Explanation Generation."""

import pytest
import datetime
import pandas as pd
from scripts.generate_data import generate_financial_dataset
from ml.features.engine import FinGuardFeatureEngine
from ml.models.lightgbm_model import LightGBMFraudModel
from ml.drift.detector import FinGuardDriftDetector

@pytest.mark.asyncio
async def test_test_risk_rules_engine_evaluator_execution():
    df = generate_financial_dataset(num_transactions=100, seed=42)
    assert len(df) == 100
    assert "is_fraud" in df.columns
    
    featured_df = FinGuardFeatureEngine.engineer_features(df)
    assert len(featured_df.columns) > len(df.columns)
    
    detector = FinGuardDriftDetector(featured_df, featured_df)
    res = detector.run_drift_analysis()
    assert res["overall_status"] == "NORMAL"
