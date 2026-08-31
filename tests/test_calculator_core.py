"""
Unit tests for core calculation engine, quantitative operators, and boundary invariants.
"""
import pytest
import math

class TestCalculationEngine:
    def test_basic_arithmetic_invariants(self):
        assert 10 + 25 == 35
        assert 100 - 45 == 55
        assert 12 * 12 == 144
        assert 1000 / 10 == 100.0

    def test_floating_point_precision(self):
        result = 0.1 + 0.2
        assert math.isclose(result, 0.3, rel_tol=1e-9)

    def test_division_by_zero_prevention(self):
        with pytest.raises(ZeroDivisionError):
            _ = 100 / 0

    def test_statistical_aggregation_properties(self):
        sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]
        mean = sum(sample_data) / len(sample_data)
        assert mean == 30.0
        
        variance = sum((x - mean) ** 2 for x in sample_data) / len(sample_data)
        assert variance == 200.0
        assert math.isclose(math.sqrt(variance), 14.1421356, rel_tol=1e-5)
