"""Complete Scikit-Learn compliant unified Preprocessing Pipeline."""

from typing import List, Tuple, Dict, Any, Optional
import pandas as pd
import numpy as np
from ml.preprocessing.imputer import DataImputer
from ml.preprocessing.encoder import CategoricalEncoder
from ml.preprocessing.scaler import NumericalScaler

class PreprocessingPipeline:
    def __init__(self, numeric_features: List[str], categorical_features: List[str]):
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features
        self.imputer = DataImputer()
        self.encoder = CategoricalEncoder(categorical_features)
        self.scaler = NumericalScaler(numeric_features)
        self.final_feature_names: List[str] = []
        self.is_fitted = False

    def fit(self, df: pd.DataFrame) -> "PreprocessingPipeline":
        df_imputed = self.imputer.fit(df, self.numeric_features, self.categorical_features).transform(df)
        self.encoder.fit(df_imputed)
        self.scaler.fit(df_imputed)
        
        self.final_feature_names = self.numeric_features + self.encoder.feature_names
        self.is_fitted = True
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self.is_fitted:
            raise RuntimeError("Pipeline must be fitted before calling transform()")
            
        df_imputed = self.imputer.transform(df)
        df_scaled = self.scaler.transform(df_imputed)
        df_encoded = self.encoder.transform(df_imputed)
        
        df_final = pd.concat([df_scaled, df_encoded], axis=1)
        return df_final
