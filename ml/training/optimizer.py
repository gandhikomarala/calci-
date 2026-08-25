"""Automated Hyperparameter Optimization Engine with Fast, Standard, and Full Search Modes."""

from typing import Dict, Any, List, Tuple
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from ml.models.lightgbm_model import LightGBMChurnModel
from ml.models.random_forest import RandomForestChurnModel
from ml.evaluation.evaluator import ModelEvaluator
from packages.logging.logger import get_logger

logger = get_logger("hpo_optimizer")

SEARCH_SPACES = {
    "LIGHTGBM": {
        "FAST": [
            {"n_estimators": 50, "learning_rate": 0.1, "num_leaves": 20, "verbosity": -1, "n_jobs": -1},
            {"n_estimators": 100, "learning_rate": 0.05, "num_leaves": 31, "verbosity": -1, "n_jobs": -1},
        ],
        "STANDARD": [
            {"n_estimators": 80, "learning_rate": 0.08, "num_leaves": 25, "subsample": 0.8, "verbosity": -1, "n_jobs": -1},
            {"n_estimators": 150, "learning_rate": 0.05, "num_leaves": 31, "subsample": 0.8, "verbosity": -1, "n_jobs": -1},
            {"n_estimators": 200, "learning_rate": 0.03, "num_leaves": 45, "subsample": 0.7, "verbosity": -1, "n_jobs": -1},
        ],
        "FULL": [
            {"n_estimators": 100, "learning_rate": 0.1, "num_leaves": 31, "min_child_samples": 20, "subsample": 0.8, "colsample_bytree": 0.8, "verbosity": -1, "n_jobs": -1},
            {"n_estimators": 150, "learning_rate": 0.05, "num_leaves": 40, "min_child_samples": 15, "subsample": 0.8, "colsample_bytree": 0.8, "verbosity": -1, "n_jobs": -1},
            {"n_estimators": 250, "learning_rate": 0.03, "num_leaves": 50, "min_child_samples": 10, "subsample": 0.7, "colsample_bytree": 0.7, "verbosity": -1, "n_jobs": -1},
            {"n_estimators": 300, "learning_rate": 0.02, "num_leaves": 63, "min_child_samples": 25, "subsample": 0.9, "colsample_bytree": 0.9, "verbosity": -1, "n_jobs": -1},
        ]
    },
    "RANDOM_FOREST": {
        "FAST": [
            {"n_estimators": 50, "max_depth": 8, "n_jobs": -1, "random_state": 42},
            {"n_estimators": 100, "max_depth": 12, "n_jobs": -1, "random_state": 42},
        ],
        "STANDARD": [
            {"n_estimators": 80, "max_depth": 10, "min_samples_split": 4, "n_jobs": -1, "random_state": 42},
            {"n_estimators": 150, "max_depth": 14, "min_samples_split": 2, "n_jobs": -1, "random_state": 42},
        ],
        "FULL": [
            {"n_estimators": 100, "max_depth": 10, "min_samples_split": 5, "min_samples_leaf": 2, "n_jobs": -1, "random_state": 42},
            {"n_estimators": 200, "max_depth": 15, "min_samples_split": 4, "min_samples_leaf": 1, "n_jobs": -1, "random_state": 42},
            {"n_estimators": 300, "max_depth": 20, "min_samples_split": 2, "min_samples_leaf": 1, "n_jobs": -1, "random_state": 42},
        ]
    }
}

class HyperparameterOptimizer:
    def __init__(self, algorithm: str = "LIGHTGBM", mode: str = "FAST", cv_folds: int = 3):
        self.algorithm = algorithm.upper()
        self.mode = mode.upper()
        self.cv_folds = cv_folds

    def optimize(self, X: pd.DataFrame, y: pd.Series) -> Tuple[Dict[str, Any], float]:
        param_candidates = SEARCH_SPACES.get(self.algorithm, {}).get(self.mode, [{}])
        skf = StratifiedKFold(n_splits=self.cv_folds, shuffle=True, random_state=42)

        best_params = param_candidates[0]
        best_score = -1.0

        for params in param_candidates:
            fold_scores = []
            for train_idx, val_idx in skf.split(X, y):
                X_tr, X_val = X.iloc[train_idx], X.iloc[val_idx]
                y_tr, y_val = y.iloc[train_idx], y.iloc[val_idx]

                if self.algorithm == "RANDOM_FOREST":
                    model = RandomForestChurnModel(params)
                else:
                    model = LightGBMChurnModel(params)

                model.fit(X_tr, y_tr)
                val_probas = model.predict_proba(X_val)
                metrics = ModelEvaluator.evaluate(y_val.to_numpy(), val_probas)
                fold_scores.append(metrics["roc_auc"])

            mean_auc = float(np.mean(fold_scores))
            logger.info("Evaluated hyperparameter candidate", algorithm=self.algorithm, params=params, cv_roc_auc=mean_auc)

            if mean_auc > best_score:
                best_score = mean_auc
                best_params = params

        return best_params, round(best_score, 4)
