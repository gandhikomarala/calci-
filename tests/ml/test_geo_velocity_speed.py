"""Unit test for GeoVelocitySpeedTransformer."""

import pytest
import pandas as pd
import numpy as np
from ml.features.geo_velocity_speed import GeoVelocitySpeedTransformer

def test_geo_velocity_speed_fit_transform():
    df = pd.DataFrame({
        "amount": [50.0, 1200.0, 35.0],
        "customer_avg_amount": [60.0, 80.0, 40.0],
        "is_new_device": [0, 1, 0],
        "is_location_anomaly": [0, 1, 0],
        "velocity_last_1h": [1, 12, 0],
        "failed_attempts_last_24h": [0, 3, 0],
        "merchant_category": ["GROCERY_SUPERMARKET", "CRYPTO_EXCHANGE", "HEALTHCARE_PHARMACY"],
    })

    transformer = GeoVelocitySpeedTransformer()
    transformed_df = transformer.fit(df).transform(df)

    assert transformer.output_col in transformed_df.columns
    assert transformed_df[transformer.output_col].isnull().sum() == 0
