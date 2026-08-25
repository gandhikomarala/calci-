import pytest
import numpy as np
import pandas as pd
from ml.models.lightgbm_model import LightGBMChurnModel
from ml.explainability.shap_engine import ShapExplanationEngine

def test_shap_explanation_generation():
    np.random.seed(42)
    X = pd.DataFrame({
        "tenure_months": np.random.uniform(1, 60, 100),
        "monthly_charge": np.random.uniform(20, 120, 100),
        "payment_failures": np.random.choice([0, 1, 2], 100),
    })
    y = pd.Series((X["monthly_charge"] > 70).astype(int))

    model = LightGBMChurnModel({"n_estimators": 20, "verbosity": -1, "random_state": 42})
    model.fit(X, y)

    explainer = ShapExplanationEngine(model.model, list(X.columns))
    explanation = explainer.explain_instance(X.iloc[[0]])

    assert "base_value" in explanation
    assert "top_positive_factors" in explanation
    assert "top_negative_factors" in explanation
    assert "feature_contributions" in explanation
