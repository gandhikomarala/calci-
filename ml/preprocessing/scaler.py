"""Robust & Standard numerical feature scaling."""

from typing import List
import pandas as pd
from sklearn.preprocessing import RobustScaler, StandardScaler

class NumericalScaler:
    def __init__(self, numeric_cols: List[str], use_robust: bool = True):
        self.numeric_cols = numeric_cols
        self.scaler = RobustScaler() if use_robust else StandardScaler()
        self.is_fitted = False

    def fit(self, df: pd.DataFrame) -> "NumericalScaler":
        cols = [c for c in self.numeric_cols if c in df.columns]
        if cols:
            self.scaler.fit(df[cols])
            self.is_fitted = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted or not self.numeric_cols:
            return pd.DataFrame(index=df.index)
            
        cols = [c for c in self.numeric_cols if c in df.columns]
        scaled_array = self.scaler.transform(df[cols])
        return pd.DataFrame(scaled_array, columns=cols, index=df.index)
