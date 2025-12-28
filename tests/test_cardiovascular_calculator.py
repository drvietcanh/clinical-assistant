"""
Test cases for Cardiovascular Drugs Calculator
Compare with Medical Calculator and verify formulas
"""

import pytest
from drugs.cardiovascular_calculator import (
    calculate_vasopressor_infusion,
    calculate_drop_rate,
    calculate_infusion_time,
    calculate_complete_infusion,
    validate_dose_range
)


def test_adrenaline_basic_calculation():
    """Test Adrenaline calculation - compare with Medical Calculator"""
    # Input: 0.1 mcg/kg/min, 70kg, IV bag 500ml (4 mcg/ml)
    result = calculate_vasopressor_infusion(
        "Adrenaline", 0.1, 70, "iv_bag_500ml"
    )
    
    # Expected from Medical Calculator:
    # Total dose: 0.1 × 70 = 7 mcg/min = 420 mcg/h
    # Rate: 420 / 4 = 105 ml/h
    assert abs(result["total_dose_mcg_min"] - 7.0) < 0.1
    assert abs(result["total_dose_mcg_hour"] - 420.0) < 0.1
    assert abs(result["infusion_rate_ml_hour"] - 105.0) < 1.0  # Allow 1 ml/h tolerance
    assert abs(result["concentration_mcg_ml"] - 4.0) < 0.1


def test_noradrenaline_basic_calculation():
    """Test Noradrenaline calculation"""
    # Input: 0.1 mcg/kg/min, 70kg, IV bag 500ml (64 mcg/ml)
    result = calculate_vasopressor_infusion(
        "Noradrenaline", 0.1, 70, "iv_bag_500ml"
    )
    
    # Expected:
    # Total dose: 0.1 × 70 = 7 mcg/min = 420 mcg/h
    # Rate: 420 / 64 = 6.5625 ml/h
    assert abs(result["total_dose_mcg_min"] - 7.0) < 0.1
    assert abs(result["total_dose_mcg_hour"] - 420.0) < 0.1
    assert abs(result["infusion_rate_ml_hour"] - 6.56) < 0.5
    assert abs(result["concentration_mcg_ml"] - 64.0) < 0.1


def test_dopamine_calculation():
    """Test Dopamine calculation"""
    # Input: 5 mcg/kg/min, 70kg, IV bag 500ml (1600 mcg/ml)
    result = calculate_vasopressor_infusion(
        "Dopamine", 5, 70, "iv_bag_500ml"
    )
    
    # Expected:
    # Total dose: 5 × 70 = 350 mcg/min = 21000 mcg/h
    # Rate: 21000 / 1600 = 13.125 ml/h
    assert abs(result["total_dose_mcg_min"] - 350.0) < 0.1
    assert abs(result["total_dose_mcg_hour"] - 21000.0) < 1.0
    assert abs(result["infusion_rate_ml_hour"] - 13.125) < 0.5


def test_drop_rate_calculation():
    """Test drop rate calculation"""
    # Input: 105 ml/h, drop factor 20
    drop_rate = calculate_drop_rate(105, 20)
    
    # Expected: (105 × 20) / 60 = 35 gtt/min
    assert abs(drop_rate - 35.0) < 0.1


def test_infusion_time_calculation():
    """Test infusion time calculation"""
    # Input: 50 ml, 105 ml/h
    time_result = calculate_infusion_time(50, 105)
    
    # Expected: 50 / 105 = 0.476 hours = 28.6 minutes
    assert abs(time_result["time_hours"] - 0.476) < 0.01
    assert abs(time_result["time_minutes"] - 28.6) < 0.5


def test_complete_infusion_calculation():
    """Test complete infusion calculation with all details"""
    result = calculate_complete_infusion(
        "Adrenaline", 0.1, 70, "iv_bag_500ml", drop_factor=20
    )
    
    # Verify all fields present
    assert "total_dose_mcg_min" in result
    assert "total_dose_mcg_hour" in result
    assert "infusion_rate_ml_hour" in result
    assert "drop_rate_gtt_min" in result
    assert "time_hours" in result
    assert "time_minutes" in result
    assert "time_formatted" in result
    
    # Verify drop rate
    assert abs(result["drop_rate_gtt_min"] - 35.0) < 0.1


def test_validate_dose_range():
    """Test dose range validation"""
    # Valid dose
    validation = validate_dose_range("Adrenaline", 0.1)
    assert validation["is_valid"] == True
    
    # Invalid dose (too high)
    validation = validate_dose_range("Adrenaline", 3.0)
    assert validation["is_valid"] == False
    assert "vượt quá" in validation["warning"].lower()


def test_syringe_pump_vs_iv_bag():
    """Test difference between syringe pump and IV bag"""
    # Same drug, same dose, different methods
    result_syringe = calculate_vasopressor_infusion(
        "Adrenaline", 0.1, 70, "syringe_pump_50ml"
    )
    result_iv = calculate_vasopressor_infusion(
        "Adrenaline", 0.1, 70, "iv_bag_500ml"
    )
    
    # Total doses should be same
    assert abs(result_syringe["total_dose_mcg_min"] - result_iv["total_dose_mcg_min"]) < 0.1
    
    # But rates should be different (different concentrations)
    # Syringe: 20 mcg/ml, IV bag: 4 mcg/ml
    # So syringe rate should be lower
    assert result_syringe["infusion_rate_ml_hour"] < result_iv["infusion_rate_ml_hour"]


def test_edge_cases():
    """Test edge cases"""
    # Very low dose
    result = calculate_vasopressor_infusion("Adrenaline", 0.01, 70, "iv_bag_500ml")
    assert result["infusion_rate_ml_hour"] > 0
    
    # Very high weight
    result = calculate_vasopressor_infusion("Adrenaline", 0.1, 150, "iv_bag_500ml")
    assert result["total_dose_mcg_min"] == 15.0
    
    # Very high dose
    result = calculate_vasopressor_infusion("Adrenaline", 0.5, 70, "iv_bag_500ml")
    assert result["total_dose_mcg_min"] == 35.0


if __name__ == "__main__":
    # Run basic tests
    print("Testing Adrenaline calculation...")
    test_adrenaline_basic_calculation()
    print("✅ Adrenaline test passed")
    
    print("\nTesting drop rate calculation...")
    test_drop_rate_calculation()
    print("✅ Drop rate test passed")
    
    print("\nTesting infusion time calculation...")
    test_infusion_time_calculation()
    print("✅ Infusion time test passed")
    
    print("\nTesting complete infusion calculation...")
    test_complete_infusion_calculation()
    print("✅ Complete infusion test passed")
    
    print("\n✅ All basic tests passed!")

