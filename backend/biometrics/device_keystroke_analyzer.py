"""
FinGuard AI — Keystroke Dynamics & Touch Jitter Analyzer.
"""
from typing import Dict, List, Any, Optional
import numpy as np
import structlog

logger = structlog.get_logger(__name__)

class KeystrokeDynamicsAnalyzer:
    """Calculates digraph and trigraph latencies for behavioral fraud detection."""
    
    def __init__(self, tolerance_ms: float = 35.0):
        self.tolerance_ms = tolerance_ms
        self._profiles: Dict[str, Dict[str, float]] = {}

    def extract_digraph_timing(self, key_events: List[Dict[str, Any]]) -> Dict[str, float]:
        if len(key_events) < 2:
            return {"mean_digraph_ms": 0.0, "latency_jitter": 0.0, "is_script_speed": 0.0}
            
        latencies = []
        for i in range(len(key_events) - 1):
            t1 = key_events[i].get("timestamp", 0.0)
            t2 = key_events[i + 1].get("timestamp", 0.0)
            dt = max(0.0, t2 - t1)
            latencies.append(dt)
            
        arr = np.array(latencies, dtype=np.float32)
        mean_lat = float(np.mean(arr))
        std_lat = float(np.std(arr))
        
        # Script / emulator check: uniform zero variance or inhuman speed (<5ms)
        is_script = 1.0 if (std_lat < 0.1 or mean_lat < 5.0) else 0.0
        
        return {
            "mean_digraph_ms": mean_lat,
            "latency_jitter": std_lat,
            "is_script_speed": is_script,
            "keystroke_risk_score": float(np.clip(is_script * 0.95 + (1.0 / max(1.0, std_lat)) * 0.05, 0.0, 1.0))
        }

    def train_user_keystroke_profile(self, user_id: str, sample_latencies: List[float]):
        if user_id not in self._profiles:
            self._profiles[user_id] = {"mean": float(np.mean(sample_latencies)), "std": float(np.std(sample_latencies))}
