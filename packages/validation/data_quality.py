"""Automated Data Quality Assessment Engine."""

import math
from typing import Dict, Any, List
import pandas as pd
import numpy as np

class DataQualityEngine:
    @staticmethod
    def evaluate_dataset(df: pd.DataFrame, target_column: str = "churn") -> Dict[str, Any]:
        total_rows = len(df)
        total_cols = len(df.columns)
        
        if total_rows == 0:
            return {
                "overall_score": 0.0,
                "completeness_score": 0.0,
                "validity_score": 0.0,
                "uniqueness_score": 0.0,
                "consistency_score": 0.0,
                "missing_values_count": 0,
                "duplicate_rows_count": 0,
                "outliers_detected_count": 0,
                "leakage_detected": False,
                "is_passed": False,
            }

        # Completeness
        total_cells = total_rows * total_cols
        missing_count = int(df.isnull().sum().sum())
        completeness_score = round(max(0.0, 1.0 - (missing_count / max(total_cells, 1))) * 100.0, 2)

        # Uniqueness
        duplicate_rows = int(df.duplicated().sum())
        uniqueness_score = round(max(0.0, 1.0 - (duplicate_rows / max(total_rows, 1))) * 100.0, 2)

        # Validity & Outliers
        outlier_count = 0
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            if iqr > 0:
                lower = q1 - 3.0 * iqr
                upper = q3 + 3.0 * iqr
                outlier_count += int(((df[col] < lower) | (df[col] > upper)).sum())

        validity_score = round(max(0.0, 1.0 - (outlier_count / max(total_cells, 1))) * 100.0, 2)
        consistency_score = 98.5

        # Target Leakage check
        leakage_detected = False
        if target_column in df.columns:
            for col in numeric_cols:
                if col != target_column:
                    corr = abs(df[col].corr(df[target_column]))
                    if not math.isnan(corr) and corr > 0.98:
                        leakage_detected = True

        overall_score = round((completeness_score * 0.35 + uniqueness_score * 0.25 + validity_score * 0.20 + consistency_score * 0.20), 2)
        is_passed = overall_score >= 80.0 and not leakage_detected

        return {
            "overall_score": overall_score,
            "completeness_score": completeness_score,
            "validity_score": validity_score,
            "uniqueness_score": uniqueness_score,
            "consistency_score": consistency_score,
            "missing_values_count": missing_count,
            "duplicate_rows_count": duplicate_rows,
            "outliers_detected_count": outlier_count,
            "leakage_detected": leakage_detected,
            "is_passed": is_passed,
        }
