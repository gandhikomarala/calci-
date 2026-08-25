"""Unit test for CalibratedChurnModel."""

import pytest
import pandas as pd
import numpy as np
from ml.models.calibrated_classifier import CalibratedChurnModel

@pytest.fixture
def sample_financial_data():
    np.random.seed(42)
    X = pd.DataFrame({
        "amount_deviation_val": np.random.uniform(0.5, 5.0, 150),
        "velocity_1h_val": np.random.poisson(1.5, 150),
        "device_risk_scorer_val": np.random.choice([0.0, 1.5, 3.5], 150),
    })
    y = pd.Series((X["amount_deviation_val"] * X["device_risk_scorer_val"] > 4.0).astype(int))
    return X, y

def test_calibrated_classifier_lifecycle(sample_financial_data):
    X, y = sample_financial_data
    model = CalibratedChurnModel()
    
    if "calibrated_classifier" == "isolation_forest":
        model.fit(X)
    else:
        model.fit(X, y)
        
    assert model.is_trained is True

    probas = model.predict_proba(X)
    assert probas.shape == (150, 2)
    assert np.all(probas >= 0.0) and np.all(probas <= 1.0)
