"""ROC, Precision-Recall, Calibration, and Cumulative Gain Lift Curves."""

from typing import Dict, Any, List
import numpy as np
from sklearn.metrics import roc_curve, precision_recall_curve
from sklearn.calibration import calibration_curve

class ModelCurvesCalculator:
    @staticmethod
    def calculate_all_curves(y_true: np.ndarray, y_pred_proba: np.ndarray) -> Dict[str, Any]:
        if y_pred_proba.ndim == 2:
            probas = y_pred_proba[:, 1]
        else:
            probas = y_pred_proba

        # 1. ROC Curve
        fpr, tpr, roc_thresh = roc_curve(y_true, probas)
        
        # 2. PR Curve
        precision, recall, pr_thresh = precision_recall_curve(y_true, probas)
        
        # 3. Calibration Curve
        prob_true, prob_pred = calibration_curve(y_true, probas, n_bins=10, strategy="uniform")

        # 4. Decile Lift Curve
        df_lift = pd.DataFrame({"y_true": y_true, "proba": probas})
        df_lift["decile"] = pd.qcut(df_lift["proba"].rank(method="first"), q=10, labels=False)
        lift_data = []
        overall_churn = np.mean(y_true)
        for d in range(9, -1, -1):
            sub = df_lift[df_lift["decile"] == d]
            rate = float(np.mean(sub["y_true"]))
            lift_data.append({
                "decile": 10 - d,
                "churn_rate": round(rate * 100.0, 2),
                "lift": round(rate / max(overall_churn, 0.001), 2)
            })

        return {
            "roc": {
                "fpr": [round(float(x), 4) for x in fpr[::max(1, len(fpr)//20)]],
                "tpr": [round(float(x), 4) for x in tpr[::max(1, len(tpr)//20)]]
            },
            "pr": {
                "precision": [round(float(x), 4) for x in precision[::max(1, len(precision)//20)]],
                "recall": [round(float(x), 4) for x in recall[::max(1, len(recall)//20)]]
            },
            "calibration": {
                "prob_true": [round(float(x), 4) for x in prob_true],
                "prob_pred": [round(float(x), 4) for x in prob_pred]
            },
            "lift_curve": lift_data
        }
import pandas as pd
