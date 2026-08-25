"""Comprehensive model evaluation metrics calculation."""

from typing import Dict, Any
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix,
    brier_score_loss, roc_curve, precision_recall_curve
)

class ModelEvaluator:
    @staticmethod
    def evaluate(y_true: np.ndarray, y_pred_proba: np.ndarray, threshold: float = 0.50) -> Dict[str, Any]:
        if y_pred_proba.ndim == 2:
            probas = y_pred_proba[:, 1]
        else:
            probas = y_pred_proba

        preds = (probas >= threshold).astype(int)

        acc = float(accuracy_score(y_true, preds))
        prec = float(precision_score(y_true, preds, zero_division=0))
        rec = float(recall_score(y_true, preds, zero_division=0))
        f1 = float(f1_score(y_true, preds, zero_division=0))
        roc_auc = float(roc_auc_score(y_true, probas))
        pr_auc = float(average_precision_score(y_true, probas))
        brier = float(brier_score_loss(y_true, probas))
        
        cm = confusion_matrix(y_true, preds).tolist()

        return {
            "accuracy": round(acc, 4),
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1_score": round(f1, 4),
            "roc_auc": round(roc_auc, 4),
            "pr_auc": round(pr_auc, 4),
            "brier_score": round(brier, 4),
            "confusion_matrix": cm,
            "threshold_used": threshold,
        }
