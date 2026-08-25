import pytest
import numpy as np
import pandas as pd
from ml.training.optimizer import HyperparameterOptimizer

def test_hpo_fast_mode():
    np.random.seed(42)
    X = pd.DataFrame({
        "f1": np.random.normal(0, 1, 150),
        "f2": np.random.normal(1, 2, 150),
    })
    y = pd.Series((X["f1"] + X["f2"] > 1.0).astype(int))

    optimizer = HyperparameterOptimizer(algorithm="LIGHTGBM", mode="FAST", cv_folds=2)
    best_params, score = optimizer.optimize(X, y)

    assert "n_estimators" in best_params
    assert score >= 0.70
