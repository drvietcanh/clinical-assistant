"""
Test cases for Vial Management System
Compare with Medical Calculator and verify formulas
"""

import pytest
from drugs.vial_manager import (
    calculate_vials_needed,
    calculate_preparation,
    calculate_vials_from_dose,
    get_drug_vials
)


def test_calculate_vials_needed_basic():
    """Test basic vial calculation"""
    # Test: Need 150 mg, vial has 100 mg
    result = calculate_vials_needed("Adrenaline", 150, "1mg/1ml")
    
    # Expected: Need 150 vials of 1mg each
    assert result["vials_needed"] == 150
    assert result["total_available_mg"] == 150.0
    assert result["waste_mg"] == 0.0


def test_calculate_vials_needed_with_waste():
    """Test vial calculation with waste"""
    # Test: Need 150 mg, but vials are 100 mg each
    # Since Adrenaline vials are 1mg, we need to test with a different scenario
    # Let's test with a hypothetical: if we need 1.5 mg and vial is 1mg
    result = calculate_vials_needed("Adrenaline", 1.5, "1mg/1ml")
    
    # Expected: Need 2 vials (1.5 / 1 = 1.5, ceil = 2)
    assert result["vials_needed"] == 2
    assert result["total_available_mg"] == 2.0
    assert result["waste_mg"] == 0.5
    assert abs(result["waste_percent"] - 25.0) < 0.1  # 0.5 / 2 = 25%


def test_calculate_preparation():
    """Test preparation calculation"""
    result = calculate_preparation("Adrenaline", 1.5, "1mg/1ml", 50)
    
    # Should have preparation instructions
    assert "preparation_instructions" in result
    assert result["vials_needed"] == 2
    assert result["final_concentration_mg_ml"] > 0
    assert result["final_concentration_mcg_ml"] > 0


def test_calculate_vials_from_dose():
    """Test calculating vials from dose and duration"""
    # Test: 0.1 mcg/kg/min, 70kg, 24 hours
    result = calculate_vials_from_dose("Adrenaline", 0.1, 70, 24)
    
    # Calculate expected:
    # Total dose: 0.1 × 70 × 60 × 24 = 10080 mcg = 10.08 mg
    # Vials needed: ceil(10.08 / 1) = 11 vials
    assert result["total_dose_mg"] > 0
    assert result["vials_needed"] > 0
    assert "waste_mg" in result


def test_get_drug_vials():
    """Test getting vials for a drug"""
    vials = get_drug_vials("Adrenaline")
    assert len(vials) > 0
    assert "size" in vials[0]
    assert "total_mg" in vials[0]


def test_edge_cases():
    """Test edge cases"""
    # Exact match (no waste)
    result = calculate_vials_needed("Adrenaline", 1.0, "1mg/1ml")
    assert result["waste_mg"] == 0.0
    
    # Very small dose
    result = calculate_vials_needed("Adrenaline", 0.1, "1mg/1ml")
    assert result["vials_needed"] == 1  # Always need at least 1 vial
    
    # Very large dose
    result = calculate_vials_needed("Adrenaline", 1000, "1mg/1ml")
    assert result["vials_needed"] == 1000


if __name__ == "__main__":
    # Run basic tests
    print("Testing vial calculation...")
    test_calculate_vials_needed_basic()
    print("✅ Basic test passed")
    
    print("\nTesting with waste...")
    test_calculate_vials_needed_with_waste()
    print("✅ Waste test passed")
    
    print("\nTesting preparation...")
    test_calculate_preparation()
    print("✅ Preparation test passed")
    
    print("\n✅ All basic tests passed!")

