"""Categorical encoding: One-Hot and Ordinal with unknown category handling."""

from typing import List, Dict, Any
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class CategoricalEncoder:
    def __init__(self, categorical_cols: List[str]):
        self.categorical_cols = categorical_cols
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        self.feature_names: List[str] = []
        self.is_fitted = False

    def fit(self, df: pd.DataFrame) -> "CategoricalEncoder":
        cols = [c for c in self.categorical_cols if c in df.columns]
        if cols:
            self.encoder.fit(df[cols].astype(str))
            self.feature_names = list(self.encoder.get_feature_names_out(cols))
            self.is_fitted = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted or not self.categorical_cols:
            return pd.DataFrame(index=df.index)
            
        cols = [c for c in self.categorical_cols if c in df.columns]
        encoded_array = self.encoder.transform(df[cols].astype(str))
        return pd.DataFrame(encoded_array, columns=self.feature_names, index=df.index)
