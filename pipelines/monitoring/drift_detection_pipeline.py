"""Scheduled Automated Data Drift & Prediction Drift Pipeline."""

from typing import Dict, Any, List
import pandas as pd
from ml.data.dataset_loader import DatasetLoader
from ml.features.engine import FeatureEngineeringEngine
from ml.drift.drift_detector import DataDriftDetector
from packages.logging.logger import get_logger

logger = get_logger("drift_pipeline")

class DriftDetectionPipeline:
    def __init__(self, baseline_csv_path: str, inference_csv_path: str):
        self.baseline_path = baseline_csv_path
        self.inference_path = inference_csv_path

    def run(self) -> Dict[str, Any]:
        logger.info("Executing drift pipeline", baseline=self.baseline_path, inference=self.inference_path)
        
        base_df = DatasetLoader.load(self.baseline_path)
        inf_df = DatasetLoader.load(self.inference_path)

        num_cols, _ = FeatureEngineeringEngine.get_feature_column_lists()
        
        results = DataDriftDetector.evaluate_drift(base_df, inf_df, num_cols)
        logger.info("Drift evaluation completed", status=results["drift_status"], overall_psi=results["overall_psi"])

        return results
