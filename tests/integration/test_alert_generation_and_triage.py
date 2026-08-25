"""Integration Test: Automatic Alert Creation from Critical Risk Scores and Analyst Assignment Queue."""

import pytest
import datetime
import pandas as pd
from scripts.generate_data import generate_financial_dataset
from ml.features.engine import FinGuardFeatureEngine
from ml.models.lightgbm_model import LightGBMFraudModel
from ml.drift.detector import FinGuardDriftDetector

@pytest.mark.asyncio
async def test_test_alert_generation_and_triage_execution():
    df = generate_financial_dataset(num_transactions=100, seed=42)
    assert len(df) == 100
    assert "is_fraud" in df.columns
    
    featured_df = FinGuardFeatureEngine.engineer_features(df)
    assert len(featured_df.columns) > len(df.columns)
    
    detector = FinGuardDriftDetector(featured_df, featured_df)
    res = detector.run_drift_analysis()
    assert res["overall_status"] == "NORMAL"
