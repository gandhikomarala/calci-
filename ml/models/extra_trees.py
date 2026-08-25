"""ExtraTreesChurnModel: Extremely Randomized Trees ensemble classifier."""

from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, AdaBoostClassifier
from sklearn.linear_model import RidgeClassifier, LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from ml.models.base_model import BaseChurnModel
from packages.logging.logger import get_logger

logger = get_logger("extra_trees")

class ExtraTreesChurnModel(BaseChurnModel):
    def __init__(self, hyperparameters: Optional[Dict[str, Any]] = None):
        params = hyperparameters or {"random_state": 42}
        super().__init__("EXTRA_TREES", params)
        self.is_trained = False
        
        # Instantiate underlying model
        if "extra_trees" == "extra_trees":
            self.model = ExtraTreesClassifier(n_estimators=params.get("n_estimators", 100), random_state=42, n_jobs=-1)
        elif "extra_trees" == "adaboost_model":
            self.model = AdaBoostClassifier(n_estimators=params.get("n_estimators", 50), random_state=42)
        elif "extra_trees" == "ridge_classifier":
            base = LogisticRegression(penalty="l2", C=params.get("C", 1.0), max_iter=1000, random_state=42)
            self.model = CalibratedClassifierCV(base, cv=3)
        elif "extra_trees" == "lasso_classifier":
            base = LogisticRegression(penalty="l1", solver="saga", C=params.get("C", 0.5), max_iter=1000, random_state=42)
            self.model = CalibratedClassifierCV(base, cv=3)
        elif "extra_trees" == "calibrated_model":
            base = LogisticRegression(max_iter=1000, random_state=42)
            self.model = CalibratedClassifierCV(base, method="isotonic", cv=3)
        else:
            self.model = LogisticRegression(max_iter=1000, random_state=42)

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "ExtraTreesChurnModel":
        logger.info("Fitting ExtraTreesChurnModel", samples=len(X), features=len(X.columns))
        self.model.fit(X, y)
        self.is_trained = True
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        if not self.is_trained:
            raise RuntimeError("ExtraTreesChurnModel must be trained before calling predict_proba()")
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X)
        elif hasattr(self.model, "decision_function"):
            df = self.model.decision_function(X)
            probs = 1.0 / (1.0 + np.exp(-df))
            return np.vstack([1.0 - probs, probs]).T
        else:
            preds = self.model.predict(X)
            return np.vstack([1.0 - preds, preds]).T
