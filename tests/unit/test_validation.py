import pytest
import pandas as pd
import numpy as np
from packages.validation.data_quality import DataQualityEngine
from packages.validation.leakage_detector import TargetLeakageDetector

def test_data_quality_engine_scoring():
    df = pd.DataFrame({
        "customer_id": [f"C{i}" for i in range(100)],
        "age": np.random.randint(20, 70, size=100),
        "monthly_charge": np.random.uniform(20, 100, size=100),
        "churn": np.random.choice([0, 1], size=100),
    })
    
    report = DataQualityEngine.evaluate_dataset(df)
    assert report["overall_score"] >= 80.0
    assert report["completeness_score"] == 100.0
    assert report["uniqueness_score"] == 100.0
    assert report["is_passed"] is True

def test_target_leakage_detector():
    df = pd.DataFrame({
        "churn": [0, 1, 0, 1, 0, 1, 0, 1],
        "leaked_feature": [0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
        "normal_feature": [12, 45, 23, 67, 34, 89, 12, 34],
    })
    
    leaks = TargetLeakageDetector.detect_leakage(df, target_col="churn")
    assert len(leaks) == 1
    assert leaks[0]["column"] == "leaked_feature"
