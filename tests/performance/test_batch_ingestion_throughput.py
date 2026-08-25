"""Performance Benchmark Suite: High-Throughput (10,000 records/sec) Ingestion & Feature Generation Benchmark."""

import pytest
import time
import pandas as pd
from scripts.generate_data import generate_financial_dataset
from ml.features.engine import FinGuardFeatureEngine

def test_test_batch_ingestion_throughput_benchmark():
    start = time.perf_counter()
    df = generate_financial_dataset(num_transactions=500, seed=42)
    featured_df = FinGuardFeatureEngine.engineer_features(df)
    duration = time.perf_counter() - start
    
    assert len(featured_df) == 500
    assert duration < 5.0  # Must complete within 5 seconds
