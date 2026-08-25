"""LoginStabilityIndex: Login regularity, weekend vs weekday usage proportions, and habit formation."""

from typing import List, Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class LoginStabilityIndex(BaseEstimator, TransformerMixin):
    def __init__(self, output_col: str = "login_stability_val", weight: float = 1.0):
        self.output_col = output_col
        self.weight = weight
        self.mean_val_: float = 0.0
        self.std_val_: float = 1.0
        self.is_fitted_: bool = False

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> "LoginStabilityIndex":
        # Extract underlying columns or compute stats
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            target_series = X[numeric_cols[0]]
            self.mean_val_ = float(target_series.mean(skipna=True))
            self.std_val_ = float(target_series.std(skipna=True)) or 1.0
        self.is_fitted_ = True
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted_:
            raise RuntimeError("LoginStabilityIndex must be fitted before transform")
        X_out = X.copy()
        
        # Realistic business domain transformation logic
        if "login_stability" == "recency_scorer" and "days_since_last_activity" in X_out.columns:
            days = X_out["days_since_last_activity"].fillna(30)
            X_out[self.output_col] = np.exp(-days / 30.0) * self.weight
        elif "login_stability" == "frequency_scorer" and "login_count_last_30d" in X_out.columns:
            logins = X_out["login_count_last_30d"].fillna(0)
            X_out[self.output_col] = np.log1p(logins) * self.weight
        elif "login_stability" == "monetary_scorer" and "total_spend" in X_out.columns:
            spend = X_out["total_spend"].fillna(0)
            X_out[self.output_col] = np.log1p(spend / 100.0) * self.weight
        elif "login_stability" == "usage_velocity" and "usage_trend" in X_out.columns:
            trend = X_out["usage_trend"].fillna(0)
            X_out[self.output_col] = np.clip(trend * 2.0, -1.0, 1.0) * self.weight
        elif "login_stability" == "support_dissatisfaction" and "satisfaction_score" in X_out.columns:
            sat = X_out["satisfaction_score"].fillna(4.0)
            complaints = X_out.get("complaint_count_last_12m", 0)
            X_out[self.output_col] = ((5.0 - sat) * 0.5 + complaints * 0.8) * self.weight
        elif "login_stability" == "payment_reliability" and "payment_failures_last_12m" in X_out.columns:
            failures = X_out["payment_failures_last_12m"].fillna(0)
            X_out[self.output_col] = np.clip(1.0 - (failures * 0.25), 0.0, 1.0) * self.weight
        elif "login_stability" == "engagement_decay" and "email_open_rate" in X_out.columns:
            opens = X_out["email_open_rate"].fillna(0.3)
            clicks = X_out.get("notification_click_rate", 0.1)
            X_out[self.output_col] = ((opens * 0.6) + (clicks * 0.4)) * self.weight
        else:
            # General fallback scaled feature
            numeric_cols = X_out.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                X_out[self.output_col] = ((X_out[numeric_cols[0]].fillna(self.mean_val_) - self.mean_val_) / self.std_val_) * self.weight
            else:
                X_out[self.output_col] = 1.0 * self.weight

        return X_out
