"""Numerical and categorical missing value imputation."""

from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np

class DataImputer:
    def __init__(self):
        self.numeric_fill_values: Dict[str, float] = {}
        self.categorical_fill_values: Dict[str, str] = {}

    def fit(self, df: pd.DataFrame, numeric_cols: List[str], categorical_cols: List[str]) -> "DataImputer":
        for col in numeric_cols:
            if col in df.columns:
                self.numeric_fill_values[col] = float(df[col].median(skipna=True)) if not np.isnan(df[col].median(skipna=True)) else 0.0
                
        for col in categorical_cols:
            if col in df.columns:
                mode_val = df[col].mode(dropna=True)
                self.categorical_fill_values[col] = str(mode_val[0]) if not mode_val.empty else "UNKNOWN"
                
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        for col, val in self.numeric_fill_values.items():
            if col in df_out.columns:
                df_out[col] = df_out[col].fillna(val)
                
        for col, val in self.categorical_fill_values.items():
            if col in df_out.columns:
                df_out[col] = df_out[col].fillna(val)
                
        return df_out
