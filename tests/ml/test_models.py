import pytest
import numpy as np
import pandas as pd
from ml.models.logistic_regression import LogisticRegressionChurnModel
from ml.models.random_forest import RandomForestChurnModel
from ml.models.lightgbm_model import LightGBMChurnModel
from ml.evaluation.evaluator import ModelEvaluator

@pytest.fixture
def sample_dataset():
    np.random.seed(42)
    X = pd.DataFrame({
        "f1": np.random.normal(0, 1, 200),
        "f2": np.random.normal(2, 1.5, 200),
        "f3": np.random.choice([0, 1], 200),
    })
    y = pd.Series((X["f1"] + X["f2"] > 2.0).astype(int))
    return X, y

def test_logistic_regression_fit_and_eval(sample_dataset):
    X, y = sample_dataset
    model = LogisticRegressionChurnModel()
    model.fit(X, y)
    probas = model.predict_proba(X)
    
    assert probas.shape == (200, 2)
    metrics = ModelEvaluator.evaluate(y.to_numpy(), probas)
    assert metrics["roc_auc"] >= 0.70
    assert metrics["accuracy"] >= 0.70

def test_random_forest_fit_and_eval(sample_dataset):
    X, y = sample_dataset
    model = RandomForestChurnModel({"n_estimators": 20, "random_state": 42})
    model.fit(X, y)
    probas = model.predict_proba(X)
    
    metrics = ModelEvaluator.evaluate(y.to_numpy(), probas)
    assert metrics["roc_auc"] >= 0.80

def test_lightgbm_fit_and_eval(sample_dataset):
    X, y = sample_dataset
    model = LightGBMChurnModel({"n_estimators": 30, "random_state": 42, "verbosity": -1})
    model.fit(X, y)
    probas = model.predict_proba(X)
    
    metrics = ModelEvaluator.evaluate(y.to_numpy(), probas)
    assert metrics["roc_auc"] >= 0.80
