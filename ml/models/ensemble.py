"""Weighted Voting and Stacking Ensemble Churn Classifier."""

from typing import List, Tuple, Dict, Any
import numpy as np
import pandas as pd
from ml.models.base_model import BaseChurnModel
from ml.models.logistic_regression import LogisticRegressionChurnModel
from ml.models.random_forest import RandomForestChurnModel
from ml.models.lightgbm_model import LightGBMChurnModel

class StackingEnsembleChurnModel(BaseChurnModel):
    def __init__(self, weights: List[float] = None):
        super().__init__("ENSEMBLE", {"weights": weights or [0.15, 0.35, 0.50]})
        self.weights = weights or [0.15, 0.35, 0.50]
        self.m1 = LogisticRegressionChurnModel()
        self.m2 = RandomForestChurnModel({"n_estimators": 80, "random_state": 42})
        self.m3 = LightGBMChurnModel({"n_estimators": 100, "verbosity": -1, "random_state": 42})

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "StackingEnsembleChurnModel":
        self.m1.fit(X, y)
        self.m2.fit(X, y)
        self.m3.fit(X, y)
        self.is_trained = True
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        p1 = self.m1.predict_proba(X)
        p2 = self.m2.predict_proba(X)
        p3 = self.m3.predict_proba(X)

        w = np.array(self.weights)
        w = w / np.sum(w)

        ensemble_proba = (w[0] * p1) + (w[1] * p2) + (w[2] * p3)
        return ensemble_proba
