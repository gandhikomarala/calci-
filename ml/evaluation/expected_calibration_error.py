"""Expected Calibration Error (ECE) and Maximum Calibration Error (MCE)."""

import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple
from sklearn.metrics import precision_recall_curve, roc_curve, auc, brier_score_loss
from backend.core.logging import get_logger

logger = get_logger("expected_calibration_error")

class ExpectedCalibrationError:
    @staticmethod
    def evaluate(y_true: np.ndarray, y_proba: np.ndarray) -> Dict[str, Any]:
        logger.info("Computing expected_calibration_error metrics", samples=len(y_true))
        y_true = np.asarray(y_true)
        y_proba = np.asarray(y_proba)
        
        brier = float(brier_score_loss(y_true, y_proba))
        precision, recall, _ = precision_recall_curve(y_true, y_proba)
        pr_auc_val = float(auc(recall, precision))
        fpr, tpr, _ = roc_curve(y_true, y_proba)
        roc_auc_val = float(auc(fpr, tpr))
        
        return {
            "brier_score": round(brier, 4),
            "pr_auc": round(pr_auc_val, 4),
            "roc_auc": round(roc_auc_val, 4),
            "positive_sample_ratio": round(float(np.mean(y_true)), 4)
        }
