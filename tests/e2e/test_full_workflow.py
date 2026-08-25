import pytest
import pandas as pd
from scripts.generate_data import generate_synthetic_dataset
from pipelines.training.training_pipeline import TrainingPipeline

def test_complete_platform_workflow(tmp_path):
    # 1. Generate Synthetic Data
    df = generate_synthetic_dataset(num_customers=300, seed=42)
    csv_path = tmp_path / "test_customers.csv"
    df.to_csv(csv_path, index=False)
    
    # 2. Run Training Pipeline
    pipeline = TrainingPipeline(dataset_path=str(csv_path), algorithm="LIGHTGBM")
    result = pipeline.run()
    
    assert result["algorithm"] == "LIGHTGBM"
    assert result["metrics"]["roc_auc"] >= 0.75
    assert result["metrics"]["accuracy"] >= 0.70
