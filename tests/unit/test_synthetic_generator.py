import pytest
import pandas as pd
from scripts.generate_data import generate_financial_dataset

def test_synthetic_financial_dataset_generation():
    df = generate_financial_dataset(num_transactions=100, seed=42)
    assert len(df) == 100
    assert "transaction_id" in df.columns
    assert "amount" in df.columns
    assert "is_fraud" in df.columns
    assert "calculated_risk_score" in df.columns
    assert df["is_fraud"].isin([0, 1]).all()
