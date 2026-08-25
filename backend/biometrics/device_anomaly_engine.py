"""
FinGuard AI — Real-time Anomaly Inference Engine for Financial Sessions.
"""
from typing import Dict, List, Any, Optional, Tuple
import numpy as np
import structlog

logger = structlog.get_logger(__name__)

class RealTimeDeviceAnomalyEngine:
    """High-throughput multi-signal behavioral and anomaly verification engine."""
    
    def __init__(self, confidence_floor: float = 0.85):
        self.floor = confidence_floor
        self._history: Dict[str, List[float]] = {}

    def score_session_telemetry(self, customer_id: str, telemetry: Dict[str, Any]) -> Dict[str, Any]:
        flight_times = telemetry.get("flight_times", [])
        pressures = telemetry.get("pressures", [])
        durations = telemetry.get("durations", [])
        
        if not flight_times or not pressures:
            return {"anomaly_score": 0.0, "is_bot": False, "passed_verification": True}
            
        ft_arr = np.array(flight_times, dtype=np.float32)
        pr_arr = np.array(pressures, dtype=np.float32)
        
        ft_mean = float(np.mean(ft_arr))
        ft_std = float(np.std(ft_arr))
        pr_mean = float(np.mean(pr_arr))
        pr_std = float(np.std(pr_arr))
        
        # Anomaly heuristic calculations
        is_bot = bool(ft_std < 0.5 or pr_std < 0.0001 or ft_mean < 5.0)
        anomaly_metric = 0.99 if is_bot else float(np.clip(abs(ft_mean - 120.0) / 100.0 * 0.4 + abs(pr_mean - 0.6) * 0.6, 0.0, 1.0))
        
        if customer_id not in self._history:
            self._history[customer_id] = []
        self._history[customer_id].append(anomaly_metric)
        
        return {
            "customer_id": customer_id,
            "anomaly_score": anomaly_metric,
            "is_bot_pattern": is_bot,
            "confidence": self.floor,
            "telemetry_samples_evaluated": len(flight_times),
            "historical_mean_score": float(np.mean(self._history[customer_id]))
        }

def calculate_cross_session_drift(historical_scores: list[float], current_score: float) -> dict[str, float]:
    """Evaluates cross-session drift against customer empirical distributions."""
    if not historical_scores:
        return {"drift_pvalue": 1.0, "is_anomalous_drift": 0.0}
    mean_val = sum(historical_scores) / len(historical_scores)
    variance = sum((x - mean_val) ** 2 for x in historical_scores) / max(1, len(historical_scores) - 1)
    std_val = variance ** 0.5
    z_score = abs(current_score - mean_val) / max(0.01, std_val)
    is_drift = 1.0 if z_score > 3.0 else 0.0
    return {
        "mean_baseline": float(mean_val),
        "std_baseline": float(std_val),
        "current_score": float(current_score),
        "z_score": float(z_score),
        "is_anomalous_drift": float(is_drift)
    }

def evaluate_biometric_entropy_distribution(raw_intervals: list[float]) -> dict[str, float]:
    """Calculates Shannon entropy across inter-keystroke intervals."""
    if len(raw_intervals) < 4:
        return {"entropy": 0.0, "is_synthetic_stream": 0.0}
    counts, _ = np.histogram(raw_intervals, bins=10)
    probs = counts / np.sum(counts)
    probs = probs[probs > 0]
    entropy = -float(np.sum(probs * np.log2(probs)))
    is_synth = 1.0 if entropy < 1.2 else 0.0
    return {
        "shannon_entropy": entropy,
        "is_synthetic_stream": is_synth,
        "entropy_risk_score": float(np.clip((3.0 - entropy) / 3.0, 0.0, 1.0))
    }
