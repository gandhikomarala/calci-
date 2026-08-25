import pytest
import numpy as np
from ml.models.lightgbm_model import LightGBMFraudClassifier
from ml.models.random_forest import RandomForestFraudClassifier
from ml.features.financial_graph_network_features import FinancialTransactionGraph
from ml.features.device_biometrics_transformer import DeviceBiometricsTransformer

def test_suite_04_end_to_end_scoring():
    graph = FinancialTransactionGraph()
    biometrics = DeviceBiometricsTransformer(min_samples_for_baseline=2)
    
    # Ingest entities
    graph.add_node("cust_4", "customer", risk_prior=0.05)
    graph.add_node("merchant_4", "merchant", risk_prior=0.01)
    graph.add_edge("cust_4", "merchant_4", "payment", timestamp=1000.0, amount=150.0)
    
    biometrics.update_profile("cust_4", {
        "flight_time_ms": 110.0,
        "dwell_time_ms": 80.0,
        "swipe_velocity": 400.0,
        "touch_pressure": 0.6
    })
    
    bio_res = biometrics.calculate_anomaly_score("cust_4", {
        "flight_time_ms": 112.0,
        "dwell_time_ms": 78.0,
        "swipe_velocity": 395.0,
        "touch_pressure": 0.58
    })
    
    ego_res = graph.calculate_ego_network_fraud_density("cust_4", depth=2)
    
    assert bio_res["biometric_anomaly_score"] <= 1.0
    assert ego_res["ego_size"] == 2
    assert ego_res["ego_fraud_ratio"] == 0.0
