"""Target leakage and future data contamination detector."""

from typing import List, Dict, Any
import pandas as pd
import numpy as np

class TargetLeakageDetector:
    @staticmethod
    def detect_leakage(df: pd.DataFrame, target_col: str = "churn", correlation_threshold: float = 0.95) -> List[Dict[str, Any]]:
        suspects: List[Dict[str, Any]] = []
        if target_col not in df.columns:
            return suspects
            
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if col == target_col:
                continue
            corr = abs(float(df[col].corr(df[target_col])))
            if not np.isnan(corr) and corr >= correlation_threshold:
                suspects.append({
                    "column": col,
                    "correlation": round(corr, 4),
                    "reason": f"Extremely high correlation ({corr:.4f}) with target '{target_col}' indicates potential target leakage."
                })
        return suspects
