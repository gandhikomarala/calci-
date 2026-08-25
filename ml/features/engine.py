"""FinGuard AI Master Financial Feature Engineering Engine."""

from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from ml.features.velocity_5m import Velocity5mTransformer
from ml.features.velocity_1h import Velocity1hTransformer
from ml.features.amount_deviation import AmountDeviationTransformer
from ml.features.location_anomaly import LocationAnomalyTransformer
from ml.features.device_risk_scorer import DeviceRiskTransformer
from ml.features.failed_auth_velocity import FailedAuthVelocityTransformer
from ml.features.merchant_risk_index import MerchantRiskTransformer
from backend.core.logging import get_logger

logger = get_logger("feature_engine")

class FinGuardFeatureEngine:
    @staticmethod
    def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Executing FinGuard Feature Engineering Pipeline", input_records=len(df))
        df_out = df.copy()

        # Execute specialized financial transformers
        transformers = [
            Velocity5mTransformer(),
            Velocity1hTransformer(),
            AmountDeviationTransformer(),
            LocationAnomalyTransformer(),
            DeviceRiskTransformer(),
            FailedAuthVelocityTransformer(),
            MerchantRiskTransformer(),
        ]

        for trans in transformers:
            df_out = trans.fit(df_out).transform(df_out)

        # Interaction terms
        if "amount_deviation_val" in df_out.columns and "device_risk_scorer_val" in df_out.columns:
            df_out["composite_device_amount_risk"] = df_out["amount_deviation_val"] * df_out["device_risk_scorer_val"]
            
        if "velocity_1h_val" in df_out.columns and "failed_auth_velocity_val" in df_out.columns:
            df_out["burst_auth_failure_index"] = df_out["velocity_1h_val"] * (1.0 + df_out["failed_auth_velocity_val"])

        logger.info("Feature engineering complete", output_features=len(df_out.columns))
        return df_out
