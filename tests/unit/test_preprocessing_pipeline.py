import pytest
import pandas as pd
import numpy as np
from ml.preprocessing.transformer_pipeline import PreprocessingPipeline

def test_preprocessing_pipeline_fit_transform():
    df = pd.DataFrame({
        "num_a": [10.0, 20.0, np.nan, 40.0],
        "num_b": [1.0, 2.0, 3.0, 4.0],
        "cat_x": ["BASIC", "PREMIUM", None, "BASIC"],
        "cat_y": ["CARD", "PAYPAL", "CARD", "CARD"],
    })

    num_cols = ["num_a", "num_b"]
    cat_cols = ["cat_x", "cat_y"]

    pipeline = PreprocessingPipeline(num_cols, cat_cols)
    transformed_df = pipeline.fit(df).transform(df)

    assert transformed_df.isnull().sum().sum() == 0
    assert "num_a" in transformed_df.columns
    assert "num_b" in transformed_df.columns
    assert len(transformed_df.columns) > 4
