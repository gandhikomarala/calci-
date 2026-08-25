import pytest
from ml.features.device_biometrics_transformer import DeviceBiometricsTransformer

def test_device_biometrics_anomaly_calculation():
    transformer = DeviceBiometricsTransformer(min_samples_for_baseline=3)
    
    # Train baseline
    for _ in range(5):
        transformer.update_profile("user_100", {
            "flight_time_ms": 120.0,
            "dwell_time_ms": 85.0,
            "swipe_velocity": 450.0,
            "touch_pressure": 0.65
        })
        
    # Test normal session
    res_normal = transformer.calculate_anomaly_score("user_100", {
        "flight_time_ms": 122.0,
        "dwell_time_ms": 84.0,
        "swipe_velocity": 448.0,
        "touch_pressure": 0.64
    })
    assert res_normal["biometric_anomaly_score"] < 0.3
    assert res_normal["is_bot_pattern"] == 0.0

    # Test bot pattern
    res_bot = transformer.calculate_anomaly_score("user_100", {
        "flight_time_ms": 2.0,
        "dwell_time_ms": 1.0,
        "swipe_velocity": 1200.0,
        "touch_pressure": 0.99
    })
    assert res_bot["is_bot_pattern"] == 1.0
    assert res_bot["biometric_anomaly_score"] >= 0.95
