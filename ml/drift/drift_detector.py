"""Statistical Data & Prediction Drift Detection using PSI and KS-Tests."""

from typing import Dict, Any, List
import numpy as np
import pandas as pd
from scipy import stats

class DataDriftDetector:
    @staticmethod
    def calculate_psi(baseline: np.ndarray, target: np.ndarray, num_buckets: int = 10) -> float:
        baseline = baseline[~np.isnan(baseline)]
        target = target[~np.isnan(target)]
        
        if len(baseline) == 0 or len(target) == 0:
            return 0.0

        quantiles = np.linspace(0, 100, num_buckets + 1)
        bins = np.percentile(baseline, quantiles)
        bins[0] = -np.inf
        bins[-1] = np.inf

        base_counts = np.histogram(baseline, bins=bins)[0]
        target_counts = np.histogram(target, bins=bins)[0]

        base_pct = np.maximum(base_counts / len(baseline), 1e-4)
        target_pct = np.maximum(target_counts / len(target), 1e-4)

        psi = np.sum((target_pct - base_pct) * np.log(target_pct / base_pct))
        return float(max(0.0, psi))

    @classmethod
    def evaluate_drift(cls, baseline_df: pd.DataFrame, target_df: pd.DataFrame, numeric_cols: List[str]) -> Dict[str, Any]:
        results = []
        drifted_count = 0
        psi_sum = 0.0

        for col in numeric_cols:
            if col in baseline_df.columns and col in target_df.columns:
                base_vals = baseline_df[col].dropna().to_numpy()
                target_vals = target_df[col].dropna().to_numpy()
                
                psi = cls.calculate_psi(base_vals, target_vals)
                psi_sum += psi
                
                ks_stat, p_val = stats.ks_2samp(base_vals, target_vals)
                is_drifted = psi > 0.10 or p_val < 0.05
                if is_drifted:
                    drifted_count += 1
                    
                results.append({
                    "feature_name": col,
                    "psi_value": round(psi, 4),
                    "ks_statistic": round(float(ks_stat), 4),
                    "ks_pvalue": round(float(p_val), 4),
                    "is_drifted": is_drifted,
                })

        overall_psi = round(psi_sum / max(len(results), 1), 4)
        
        if overall_psi >= 0.25 or drifted_count >= 5:
            drift_status = "CRITICAL"
        elif overall_psi >= 0.10 or drifted_count >= 2:
            drift_status = "WARNING"
        else:
            drift_status = "NORMAL"

        return {
            "drift_status": drift_status,
            "overall_psi": overall_psi,
            "features_drifted_count": drifted_count,
            "total_features_count": len(results),
            "feature_metrics": results
        }
