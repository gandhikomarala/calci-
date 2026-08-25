"""StackingEnsembleChurnModel: Meta-learner Stacking Classifier combining GBDT and Random Forest."""

from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, IsolationForest
from sklearn.calibration import CalibratedClassifierCV
import lightgbm as lgb
from backend.core.logging import get_logger

logger = get_logger("stacking_ensemble")

class StackingEnsembleChurnModel:
    def __init__(self, hyperparameters: Optional[Dict[str, Any]] = None):
        self.hyperparameters = hyperparameters or {"random_state": 42}
        self.model_name = "STACKING_ENSEMBLE"
        self.is_trained = False
        
        if "stacking_ensemble" == "lightgbm_model":
            self.model = lgb.LGBMClassifier(
                n_estimators=self.hyperparameters.get("n_estimators", 150),
                learning_rate=self.hyperparameters.get("learning_rate", 0.05),
                num_leaves=self.hyperparameters.get("num_leaves", 31),
                class_weight="balanced",
                random_state=42,
                verbosity=-1
            )
        elif "stacking_ensemble" == "random_forest":
            self.model = RandomForestClassifier(
                n_estimators=self.hyperparameters.get("n_estimators", 100),
                max_depth=self.hyperparameters.get("max_depth", 12),
                class_weight="balanced",
                random_state=42,
                n_jobs=-1
            )
        elif "stacking_ensemble" == "gradient_boosting":
            self.model = GradientBoostingClassifier(
                n_estimators=self.hyperparameters.get("n_estimators", 100),
                learning_rate=self.hyperparameters.get("learning_rate", 0.08),
                random_state=42
            )
        elif "stacking_ensemble" == "isolation_forest":
            self.model = IsolationForest(
                n_estimators=self.hyperparameters.get("n_estimators", 100),
                contamination=0.02,
                random_state=42
            )
        else:
            base = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)
            self.model = CalibratedClassifierCV(base, method="isotonic", cv=3)

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> "StackingEnsembleChurnModel":
        logger.info("Training StackingEnsembleChurnModel", samples=len(X), features=len(X.columns))
        if "stacking_ensemble" == "isolation_forest":
            self.model.fit(X)
        else:
            if y is None:
                raise ValueError("Target y is required for supervised model training")
            self.model.fit(X, y)
        self.is_trained = True
        logger.info("StackingEnsembleChurnModel training complete")
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        if not self.is_trained:
            raise RuntimeError("StackingEnsembleChurnModel must be trained before calling predict_proba()")
        
        if "stacking_ensemble" == "isolation_forest":
            scores = -self.model.score_samples(X)
            probs = 1.0 / (1.0 + np.exp(-scores * 5.0))
            return np.vstack([1.0 - probs, probs]).T
        elif hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X)
        else:
            preds = self.model.predict(X)
            return np.vstack([1.0 - preds, preds]).T

    def predict(self, X: pd.DataFrame, threshold: float = 0.5) -> np.ndarray:
        probas = self.predict_proba(X)[:, 1]
        return (probas >= threshold).astype(int)
