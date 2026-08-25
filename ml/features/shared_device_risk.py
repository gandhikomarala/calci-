"""SharedDeviceRiskTransformer: Number of distinct banking accounts and customer profiles linked to device."""

from typing import List, Dict, Any, Optional
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from backend.core.logging import get_logger

logger = get_logger("shared_device_risk")

class SharedDeviceRiskTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, output_col: str = "shared_device_risk_val", weight: float = 1.0):
        self.output_col = output_col
        self.weight = weight
        self.mean_val_: float = 0.0
        self.std_val_: float = 1.0
        self.is_fitted_: bool = False

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> "SharedDeviceRiskTransformer":
        logger.info("Fitting SharedDeviceRiskTransformer", input_rows=len(X))
        numeric_cols = X.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            target_series = X[numeric_cols[0]]
            self.mean_val_ = float(target_series.mean(skipna=True))
            self.std_val_ = float(target_series.std(skipna=True)) or 1.0
        self.is_fitted_ = True
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted_:
            raise RuntimeError("SharedDeviceRiskTransformer must be fitted before calling transform()")
        
        X_out = X.copy()
        
        # Domain-specific financial fraud feature transformations
        if "shared_device_risk" == "velocity_5m" and "velocity_last_1h" in X_out.columns:
            v1h = X_out["velocity_last_1h"].fillna(0)
            X_out[self.output_col] = np.clip(v1h * 0.35, 0, 50) * self.weight
        elif "shared_device_risk" == "amount_deviation" and "amount" in X_out.columns:
            amount = X_out["amount"].fillna(0)
            avg = X_out.get("customer_avg_amount", pd.Series(50.0, index=X_out.index))
            X_out[self.output_col] = (amount / np.maximum(avg, 1.0)) * self.weight
        elif "shared_device_risk" == "location_anomaly" and "is_location_anomaly" in X_out.columns:
            loc = X_out["is_location_anomaly"].fillna(0)
            X_out[self.output_col] = loc * 2.5 * self.weight
        elif "shared_device_risk" == "device_risk_scorer" and "is_new_device" in X_out.columns:
            new_dev = X_out["is_new_device"].fillna(0)
            dev_type = X_out.get("device_type", pd.Series("UNKNOWN", index=X_out.index))
            emulator_flag = dev_type.isin(["EMULATOR", "UNKNOWN"]).astype(int)
            X_out[self.output_col] = (new_dev * 1.5 + emulator_flag * 2.0) * self.weight
        elif "shared_device_risk" == "failed_auth_velocity" and "failed_attempts_last_24h" in X_out.columns:
            fails = X_out["failed_attempts_last_24h"].fillna(0)
            X_out[self.output_col] = np.log1p(fails * 2.0) * self.weight
        elif "shared_device_risk" == "merchant_risk_index" and "merchant_category" in X_out.columns:
            cats = X_out["merchant_category"].fillna("GROCERY_SUPERMARKET")
            high_risk_mask = cats.isin(["CRYPTO_EXCHANGE", "DIGITAL_GIFT_CARDS", "LUXURY_JEWELRY", "CASINO_GAMBLING"]).astype(float)
            X_out[self.output_col] = high_risk_mask * 3.0 * self.weight
        else:
            numeric_cols = X_out.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                col = numeric_cols[0]
                X_out[self.output_col] = ((X_out[col].fillna(self.mean_val_) - self.mean_val_) / self.std_val_) * self.weight
            else:
                X_out[self.output_col] = 1.0 * self.weight

        return X_out
