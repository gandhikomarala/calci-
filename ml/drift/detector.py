"""FinGuard AI Statistical Data & Concept Drift Engine."""

from typing import Dict, Any, List, Tuple
import numpy as np
import pandas as pd
from scipy import stats
from backend.core.logging import get_logger

logger = get_logger("drift_detector")

class FinGuardDriftDetector:
    def __init__(self, baseline_df: pd.DataFrame, current_df: pd.DataFrame):
        self.baseline_df = baseline_df
        self.current_df = current_df

    def calculate_psi(self, baseline_series: pd.Series, current_series: pd.Series, num_buckets: int = 10) -> float:
        b_clean = baseline_series.dropna().to_numpy()
        c_clean = current_series.dropna().to_numpy()
        if len(b_clean) == 0 or len(c_clean) == 0:
            return 0.0

        percentiles = np.linspace(0, 100, num_buckets + 1)
        breakpoints = np.percentile(b_clean, percentiles)
        breakpoints[0] -= 1e-5
        breakpoints[-1] += 1e-5

        b_counts = np.histogram(b_clean, bins=breakpoints)[0]
        c_counts = np.histogram(c_clean, bins=breakpoints)[0]

        b_pct = np.maximum(b_counts / len(b_clean), 1e-4)
        c_pct = np.maximum(c_counts / len(c_clean), 1e-4)

        psi = float(np.sum((c_pct - b_pct) * np.log(c_pct / b_pct)))
        return round(psi, 4)

    def calculate_ks_test(self, baseline_series: pd.Series, current_series: pd.Series) -> Tuple[float, float]:
        b_clean = baseline_series.dropna()
        c_clean = current_series.dropna()
        if len(b_clean) == 0 or len(c_clean) == 0:
            return 0.0, 1.0
        stat, p_val = stats.ks_2samp(b_clean, c_clean)
        return round(float(stat), 4), round(float(p_val), 4)

    def run_drift_analysis(self) -> Dict[str, Any]:
        logger.info("Executing Statistical Drift Analysis across feature set")
        numeric_cols = self.baseline_df.select_dtypes(include=[np.number]).columns
        feature_metrics = {}
        max_psi = 0.0

        for col in numeric_cols:
            if col in self.current_df.columns:
                psi = self.calculate_psi(self.baseline_df[col], self.current_df[col])
                ks_stat, p_val = self.calculate_ks_test(self.baseline_df[col], self.current_df[col])
                
                status = "NORMAL"
                if psi >= 0.25 or p_val < 0.01:
                    status = "CRITICAL"
                elif psi >= 0.10 or p_val < 0.05:
                    status = "WARNING"

                feature_metrics[col] = {
                    "psi": psi,
                    "ks_statistic": ks_stat,
                    "p_value": p_val,
                    "status": status
                }
                max_psi = max(max_psi, psi)

        overall_status = "NORMAL"
        if max_psi >= 0.25:
            overall_status = "CRITICAL"
        elif max_psi >= 0.10:
            overall_status = "WARNING"

        return {
            "overall_status": overall_status,
            "max_psi": max_psi,
            "feature_metrics": feature_metrics,
            "evaluated_features_count": len(feature_metrics)
        }
