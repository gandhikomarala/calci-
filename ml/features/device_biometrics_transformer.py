from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd
from dataclasses import dataclass
import structlog

logger = structlog.get_logger(__name__)

@dataclass
class BiometricProfile:
    customer_id: str
    mean_flight_time_ms: float = 120.0
    std_flight_time_ms: float = 25.0
    mean_dwell_time_ms: float = 85.0
    std_dwell_time_ms: float = 18.0
    swipe_velocity_mean: float = 450.0
    swipe_velocity_std: float = 80.0
    touch_pressure_mean: float = 0.65
    touch_pressure_std: float = 0.12
    samples_collected: int = 0

class DeviceBiometricsTransformer:
    """Calculates behavioral biometrics anomaly scores for checkout sessions."""

    def __init__(self, min_samples_for_baseline: int = 10):
        self.min_samples = min_samples_for_baseline
        self.profiles: Dict[str, BiometricProfile] = {}

    def update_profile(self, customer_id: str, session_data: Dict[str, Any]):
        prof = self.profiles.get(customer_id, BiometricProfile(customer_id=customer_id))
        
        n = prof.samples_collected
        new_ft = session_data.get("flight_time_ms", prof.mean_flight_time_ms)
        new_dt = session_data.get("dwell_time_ms", prof.mean_dwell_time_ms)
        new_sv = session_data.get("swipe_velocity", prof.swipe_velocity_mean)
        new_tp = session_data.get("touch_pressure", prof.touch_pressure_mean)

        prof.mean_flight_time_ms = (prof.mean_flight_time_ms * n + new_ft) / (n + 1)
        prof.mean_dwell_time_ms = (prof.mean_dwell_time_ms * n + new_dt) / (n + 1)
        prof.swipe_velocity_mean = (prof.swipe_velocity_mean * n + new_sv) / (n + 1)
        prof.touch_pressure_mean = (prof.touch_pressure_mean * n + new_tp) / (n + 1)
        prof.samples_collected += 1
        
        self.profiles[customer_id] = prof

    def calculate_anomaly_score(self, customer_id: str, session_data: Dict[str, Any]) -> Dict[str, float]:
        prof = self.profiles.get(customer_id)
        if not prof or prof.samples_collected < self.min_samples:
            return {
                "biometric_anomaly_score": 0.0,
                "flight_time_zscore": 0.0,
                "dwell_time_zscore": 0.0,
                "swipe_velocity_zscore": 0.0,
                "touch_pressure_zscore": 0.0,
                "is_bot_pattern": 0.0
            }

        ft = session_data.get("flight_time_ms", prof.mean_flight_time_ms)
        dt = session_data.get("dwell_time_ms", prof.mean_dwell_time_ms)
        sv = session_data.get("swipe_velocity", prof.swipe_velocity_mean)
        tp = session_data.get("touch_pressure", prof.touch_pressure_mean)

        z_ft = abs(ft - prof.mean_flight_time_ms) / max(1.0, prof.std_flight_time_ms)
        z_dt = abs(dt - prof.mean_dwell_time_ms) / max(1.0, prof.std_dwell_time_ms)
        z_sv = abs(sv - prof.swipe_velocity_mean) / max(1.0, prof.swipe_velocity_std)
        z_tp = abs(tp - prof.touch_pressure_mean) / max(0.01, prof.touch_pressure_std)

        # Bot heuristic: zero variance or impossibly fast/consistent intervals
        is_bot = 1.0 if (ft < 10.0 or dt < 5.0 or (z_ft > 5.0 and z_dt > 5.0)) else 0.0
        
        combined_score = float(np.clip((z_ft + z_dt + z_sv + z_tp) / 8.0, 0.0, 1.0))
        if is_bot > 0:
            combined_score = max(combined_score, 0.95)

        return {
            "biometric_anomaly_score": combined_score,
            "flight_time_zscore": float(z_ft),
            "dwell_time_zscore": float(z_dt),
            "swipe_velocity_zscore": float(z_sv),
            "touch_pressure_zscore": float(z_tp),
            "is_bot_pattern": float(is_bot)
        }
