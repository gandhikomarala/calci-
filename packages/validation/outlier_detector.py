"""Extreme statistical outlier detector using IQR & Z-scores."""

from typing import Dict, List, Any
import pandas as pd
import numpy as np

class OutlierDetector:
    @staticmethod
    def detect_outliers_iqr(df: pd.DataFrame, multiplier: float = 3.0) -> Dict[str, int]:
        outliers: Dict[str, int] = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            if iqr > 0:
                lower = q1 - multiplier * iqr
                upper = q3 + multiplier * iqr
                count = int(((df[col] < lower) | (df[col] > upper)).sum())
                if count > 0:
                    outliers[col] = count
        return outliers
