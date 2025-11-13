"""
Unit Tests for Ventilator Calculations - PHIÊN 6
"""

import unittest
from ventilator.comprehensive_calculator import calculate_pbw, calculate_driving_pressure
from ventilator.compliance import calculate_static_compliance, calculate_dynamic_compliance
from ventilator.abg_integration import calculate_pf_ratio, classify_ards


class TestCalculations(unittest.TestCase):
    """Test basic calculations"""
    
    def test_calculate_pbw_male(self):
        """Test PBW calculation for male"""
        result = calculate_pbw("Nam", 170)
        self.assertAlmostEqual(result, 66.0, places=1)
    
    def test_calculate_pbw_female(self):
        """Test PBW calculation for female"""
        result = calculate_pbw("Nữ", 160)
        self.assertAlmostEqual(result, 52.4, places=1)
    
    def test_calculate_driving_pressure(self):
        """Test driving pressure calculation"""
        result = calculate_driving_pressure(30, 10)
        self.assertEqual(result, 20)
    
    def test_calculate_driving_pressure_invalid(self):
        """Test driving pressure with invalid inputs"""
        result = calculate_driving_pressure(0, 10)
        self.assertIsNone(result)
    
    def test_calculate_static_compliance(self):
        """Test static compliance calculation"""
        result = calculate_static_compliance(500, 30, 10)
        self.assertAlmostEqual(result, 25.0, places=1)
    
    def test_calculate_dynamic_compliance(self):
        """Test dynamic compliance calculation"""
        result = calculate_dynamic_compliance(500, 35, 10)
        self.assertAlmostEqual(result, 20.0, places=1)
    
    def test_calculate_pf_ratio(self):
        """Test P/F ratio calculation"""
        result = calculate_pf_ratio(100, 50)
        self.assertEqual(result, 200)
    
    def test_classify_ards(self):
        """Test ARDS classification"""
        class_name, color, _ = classify_ards(150)
        self.assertEqual(class_name, "ARDS Trung Bình")
        self.assertEqual(color, "warning")


if __name__ == '__main__':
    unittest.main()

