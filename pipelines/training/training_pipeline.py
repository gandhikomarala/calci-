"""End-to-End Orchestrated ML Model Training Pipeline."""

import time
from typing import Dict, Any, Tuple
import pandas as pd
import numpy as np
from ml.data.dataset_loader import DatasetLoader
from ml.data.dataset_splitter import DatasetSplitter
from ml.features.engine import FeatureEngineeringEngine
from ml.preprocessing.transformer_pipeline import PreprocessingPipeline
from ml.models.logistic_regression import LogisticRegressionChurnModel
from ml.models.random_forest import RandomForestChurnModel
from ml.models.gradient_boosting import GradientBoostingChurnModel
from ml.models.lightgbm_model import LightGBMChurnModel
from ml.evaluation.evaluator import ModelEvaluator
from packages.logging.logger import get_logger

logger = get_logger("training_pipeline")

class TrainingPipeline:
    def __init__(self, dataset_path: str, algorithm: str = "LIGHTGBM", mode: str = "FAST"):
        self.dataset_path = dataset_path
        self.algorithm = algorithm.upper()
        self.mode = mode.upper()

    def run(self) -> Dict[str, Any]:
        start_time = time.time()
        logger.info("Starting training pipeline", dataset=self.dataset_path, algorithm=self.algorithm)

        # 1. Ingestion
        df_raw = DatasetLoader.load(self.dataset_path)
        
        # 2. Feature Engineering
        df_featured = FeatureEngineeringEngine.generate_features(df_raw)
        
        # 3. Train/Val/Test Split
        train_df, val_df, test_df = DatasetSplitter.split(df_featured, target_column="churn")
        
        num_cols, cat_cols = FeatureEngineeringEngine.get_feature_column_lists()
        
        # 4. Preprocessing Pipeline
        preprocessor = PreprocessingPipeline(num_cols, cat_cols)
        X_train = preprocessor.fit(train_df).transform(train_df)
        y_train = train_df["churn"]
        
        X_test = preprocessor.transform(test_df)
        y_test = test_df["churn"]

        # 5. Algorithm Selection & Training
        if self.algorithm == "LOGISTIC_REGRESSION":
            model = LogisticRegressionChurnModel()
        elif self.algorithm == "RANDOM_FOREST":
            model = RandomForestChurnModel()
        elif self.algorithm == "GRADIENT_BOOSTING":
            model = GradientBoostingChurnModel()
        else:
            model = LightGBMChurnModel()

        model.fit(X_train, y_train)

        # 6. Evaluation
        y_pred_proba = model.predict_proba(X_test)
        metrics = ModelEvaluator.evaluate(y_test.to_numpy(), y_pred_proba)
        
        duration = round(time.time() - start_time, 2)
        logger.info("Training pipeline finished", duration_sec=duration, metrics=metrics)

        return {
            "algorithm": self.algorithm,
            "training_duration_seconds": duration,
            "metrics": metrics,
            "test_sample_size": len(test_df),
        }
