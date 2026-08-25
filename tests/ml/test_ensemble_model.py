import pytest
import numpy as np
import pandas as pd
from ml.models.ensemble import StackingEnsembleChurnModel
from ml.evaluation.evaluator import ModelEvaluator

def test_stacking_ensemble():
    np.random.seed(42)
    X = pd.DataFrame({
        "f1": np.random.normal(0, 1, 200),
        "f2": np.random.normal(1, 1.5, 200),
    })
    y = pd.Series((X["f1"] + X["f2"] > 0.8).astype(int))

    ensemble = StackingEnsembleChurnModel()
    ensemble.fit(X, y)
    probas = ensemble.predict_proba(X)

    assert probas.shape == (200, 2)
    metrics = ModelEvaluator.evaluate(y.to_numpy(), probas)
    assert metrics["roc_auc"] >= 0.75
