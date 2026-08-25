"""Abstract base interface for all Churn Classification ML models."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple
import numpy as np
import pandas as pd

class BaseChurnModel(ABC):
    def __init__(self, algorithm_name: str, hyperparameters: Dict[str, Any]):
        self.algorithm_name = algorithm_name
        self.hyperparameters = hyperparameters
        self.model = None
        self.is_trained = False

    @abstractmethod
    def fit(self, X: pd.DataFrame, y: pd.Series) -> "BaseChurnModel":
        pass

    @abstractmethod
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        pass

    def predict(self, X: pd.DataFrame, threshold: float = 0.50) -> np.ndarray:
        probas = self.predict_proba(X)
        if probas.ndim == 2:
            return (probas[:, 1] >= threshold).astype(int)
        return (probas >= threshold).astype(int)
