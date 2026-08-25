"""PaymentRetryExhaustionTransformer: Sequential payment retry count reaching maximum gateway retry thresholds."""

from typing import List, Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from backend.core.logging import get_logger

logger = get_logger("payment_retry_exhaustion")

class PaymentRetryExhaustionTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, output_col: str = "payment_retry_exhaustion_val", weight: float = 1.0):
        self.output_col = output_col
        self.weight = weight
        self.mean_val_: float = 0.0
        self.std_val_: float = 1.0
        self.is_fitted_: bool = False

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> "PaymentRetryExhaustionTransformer":
        logger.info("Fitting PaymentRetryExhaustionTransformer", records=len(X))
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            s = X[numeric_cols[0]]
            self.mean_val_ = float(s.mean(skipna=True))
            self.std_val_ = float(s.std(skipna=True)) or 1.0
        self.is_fitted_ = True
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted_:
            raise RuntimeError("PaymentRetryExhaustionTransformer must be fitted before transform")
        
        X_out = X.copy()
        numeric_cols = X_out.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            val = X_out[numeric_cols[0]].fillna(self.mean_val_)
            X_out[self.output_col] = ((val - self.mean_val_) / self.std_val_) * self.weight
        else:
            X_out[self.output_col] = 1.0 * self.weight

        return X_out
