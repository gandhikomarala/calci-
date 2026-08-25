import pytest
import numpy as np
from ml.drift.drift_detector import DataDriftDetector

def test_psi_identical_distributions():
    base = np.random.normal(50, 10, 1000)
    target = np.random.normal(50, 10, 1000)
    psi = DataDriftDetector.calculate_psi(base, target)
    assert psi < 0.10  # Must be STABLE

def test_psi_shifted_distribution():
    base = np.random.normal(50, 10, 1000)
    target = np.random.normal(85, 15, 1000)
    psi = DataDriftDetector.calculate_psi(base, target)
    assert psi > 0.25  # Must detect significant drift
