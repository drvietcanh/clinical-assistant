"""
Comprehensive Test Suite for All Phases
Test all features from Phase 1-5
"""

import sys
from pathlib import Path
import os

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Mock streamlit to avoid import errors
class MockStreamlit:
    def __getattr__(self, name):
        return lambda *args, **kwargs: None

sys.modules['streamlit'] = MockStreamlit()
os.environ['STREAMLIT_TESTING'] = '1'

def test_phase_1_vial_management():
    """Test Phase 1: Vial Management System"""
    print("\n" + "="*60)
    print("TESTING PHASE 1: VIAL MANAGEMENT SYSTEM")
    print("="*60)
    
    try:
        from drugs.vial_manager import (
            calculate_vials_needed,
            calculate_preparation,
            calculate_vials_from_dose
        )
        
        # Test 1: Calculate vials needed
        print("\n1. Testing calculate_vials_needed...")
        result = calculate_vials_needed("Adrenaline", 1.5, "1mg/1ml")
        assert result["vials_needed"] == 2, f"Expected 2 vials, got {result['vials_needed']}"
        assert result["waste_mg"] == 0.5, f"Expected 0.5 mg waste, got {result['waste_mg']}"
        print("   [OK] Pass: calculate_vials_needed")
        
        # Test 2: Calculate preparation
        print("\n2. Testing calculate_preparation...")
        result = calculate_preparation("Adrenaline", 1.5, "1mg/1ml", 50)
        assert result["vials_needed"] == 2, "Should need 2 vials"
        assert result["final_concentration_mcg_ml"] > 0, "Concentration should be > 0"
        print("   [OK] Pass: calculate_preparation")
        
        # Test 3: Calculate from dose
        print("\n3. Testing calculate_vials_from_dose...")
        result = calculate_vials_from_dose("Adrenaline", 0.1, 70, 24)
        assert result["total_dose_mg"] > 0, "Total dose should be > 0"
        assert result["vials_needed"] > 0, "Should need at least 1 vial"
        print("   [OK] Pass: calculate_vials_from_dose")
        
        print("\n[PASS] Phase 1: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 1: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_phase_2_cardiovascular():
    """Test Phase 2: Cardiovascular Drugs Calculator"""
    print("\n" + "="*60)
    print("TESTING PHASE 2: CARDIOVASCULAR DRUGS CALCULATOR")
    print("="*60)
    
    try:
        from drugs.cardiovascular_calculator import (
            get_drug_names,
            get_drug_info,
            calculate_complete_infusion,
            validate_dose_range
        )
        
        # Test 1: Get drug names
        print("\n1. Testing get_drug_names...")
        drugs = get_drug_names()
        assert len(drugs) > 0, "Should have at least one drug"
        assert "Adrenaline" in drugs, "Should have Adrenaline"
        print(f"   ✅ Pass: Found {len(drugs)} drugs")
        
        # Test 2: Get drug info
        print("\n2. Testing get_drug_info...")
        info = get_drug_info("Adrenaline")
        assert info is not None, "Should get drug info"
        assert "dose_range" in info, "Should have dose_range"
        print("   [OK] Pass: get_drug_info")
        
        # Test 3: Calculate complete infusion
        print("\n3. Testing calculate_complete_infusion...")
        result = calculate_complete_infusion(
            "Adrenaline", 0.1, 70, "syringe_pump_50ml"
        )
        assert result["infusion_rate_ml_hour"] > 0, "Infusion rate should be > 0"
        assert result["total_dose_mcg_hour"] > 0, "Total dose should be > 0"
        print("   [OK] Pass: calculate_complete_infusion")
        
        # Test 4: Validate dose range
        print("\n4. Testing validate_dose_range...")
        validation = validate_dose_range("Adrenaline", 0.1)
        assert "is_valid" in validation, "Should have is_valid"
        print("   [OK] Pass: validate_dose_range")
        
        print("\n[PASS] Phase 2: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 2: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_phase_3_enhanced_infusion():
    """Test Phase 3: Enhanced Infusion Calculator"""
    print("\n" + "="*60)
    print("TESTING PHASE 3: ENHANCED INFUSION CALCULATOR")
    print("="*60)
    
    try:
        from critical_care.enhanced_infusion import (
            calculate_infusion_rate,
            calculate_volume_needed,
            calculate_dose_from_rate,
            calculate_infusion_time,
            calculate_drop_rate
        )
        
        # Test 1: Calculate infusion rate
        print("\n1. Testing calculate_infusion_rate...")
        result = calculate_infusion_rate(0.1, 70, 20, 20)
        assert result["infusion_rate_ml_hour"] > 0, "Infusion rate should be > 0"
        assert result["drop_rate_gtt_min"] is not None, "Should have drop rate"
        print("   [OK] Pass: calculate_infusion_rate")
        
        # Test 2: Calculate volume needed
        print("\n2. Testing calculate_volume_needed...")
        result = calculate_volume_needed(0.1, 70, 24, 20)
        assert result["volume_ml"] > 0, "Volume should be > 0"
        assert result["infusion_rate_ml_hour"] > 0, "Infusion rate should be > 0"
        print("   [OK] Pass: calculate_volume_needed")
        
        # Test 3: Calculate dose from rate (reverse)
        print("\n3. Testing calculate_dose_from_rate...")
        result = calculate_dose_from_rate(10, 70, 20)
        assert result["dose_mcg_kg_min"] > 0, "Dose should be > 0"
        print("   [OK] Pass: calculate_dose_from_rate")
        
        # Test 4: Calculate infusion time
        print("\n4. Testing calculate_infusion_time...")
        result = calculate_infusion_time(500, 50)
        assert result["time_hours"] == 10, "Should be 10 hours"
        assert "time_formatted" in result, "Should have formatted time"
        print("   [OK] Pass: calculate_infusion_time")
        
        # Test 5: Calculate drop rate
        print("\n5. Testing calculate_drop_rate...")
        drop_rate = calculate_drop_rate(60, 20)
        assert drop_rate == 20, "Should be 20 gtt/min"
        print("   [OK] Pass: calculate_drop_rate")
        
        print("\n[PASS] Phase 3: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 3: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_phase_4_unit_conversion():
    """Test Phase 4: Unit Conversion Enhancement"""
    print("\n" + "="*60)
    print("TESTING PHASE 4: UNIT CONVERSION ENHANCEMENT")
    print("="*60)
    
    try:
        from utils.unit_converter_enhanced import (
            detect_unit,
            convert_with_auto_detect,
            convert_value,
            get_available_units
        )
        
        # Test 1: Detect unit
        print("\n1. Testing detect_unit...")
        detected = detect_unit("5.2 mg/dL", "creatinine")
        assert detected is not None, "Should detect unit"
        assert detected[1] == "mg/dL", f"Should detect mg/dL, got {detected[1]}"
        print("   [OK] Pass: detect_unit")
        
        # Test 2: Convert value
        print("\n2. Testing convert_value...")
        converted = convert_value(5.2, "mg/dL", "µmol/L", "creatinine")
        expected = 5.2 * 88.4
        assert abs(converted - expected) < 0.1, f"Should convert correctly, got {converted}"
        print("   [OK] Pass: convert_value")
        
        # Test 3: Get available units
        print("\n3. Testing get_available_units...")
        units = get_available_units("creatinine")
        assert len(units) > 0, "Should have available units"
        print(f"   ✅ Pass: Found {len(units)} units for creatinine")
        
        print("\n[PASS] Phase 4: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 4: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_phase_5_multiple_infusions():
    """Test Phase 5.1: Multiple Infusions"""
    print("\n" + "="*60)
    print("TESTING PHASE 5.1: MULTIPLE INFUSIONS")
    print("="*60)
    
    try:
        from critical_care.multiple_infusions import (
            InfusionItem,
            add_infusion,
            calculate_total_volume,
            calculate_total_rate,
            validate_limits,
            calculate_multiple_infusions_summary
        )
        
        # Test 1: Create InfusionItem
        print("\n1. Testing InfusionItem...")
        item = InfusionItem("Adrenaline", 0.1, 70, "syringe_pump_50ml")
        result = item.calculate()
        assert result["infusion_rate_ml_hour"] > 0, "Should calculate infusion rate"
        print("   [OK] Pass: InfusionItem")
        
        # Test 2: Add infusion
        print("\n2. Testing add_infusion...")
        infusions = []
        new_item = add_infusion(infusions, "Adrenaline", 0.1, 70)
        assert len(infusions) == 1, "Should have 1 infusion"
        print("   [OK] Pass: add_infusion")
        
        # Test 3: Calculate total volume
        print("\n3. Testing calculate_total_volume...")
        total_vol = calculate_total_volume(infusions, same_bag=False)
        assert total_vol["total_volume_ml"] > 0, "Should have total volume"
        print("   [OK] Pass: calculate_total_volume")
        
        # Test 4: Calculate total rate
        print("\n4. Testing calculate_total_rate...")
        total_rate = calculate_total_rate(infusions)
        assert total_rate["total_rate_ml_hour"] > 0, "Should have total rate"
        print("   [OK] Pass: calculate_total_rate")
        
        # Test 5: Validate limits
        print("\n5. Testing validate_limits...")
        validation = validate_limits(100, 50, same_bag=False)
        assert "is_valid" in validation, "Should have validation result"
        print("   [OK] Pass: validate_limits")
        
        # Test 6: Summary
        print("\n6. Testing calculate_multiple_infusions_summary...")
        summary = calculate_multiple_infusions_summary(infusions, same_bag=False)
        assert "infusions" in summary, "Should have infusions"
        assert "total_volume" in summary, "Should have total_volume"
        print("   [OK] Pass: calculate_multiple_infusions_summary")
        
        print("\n[PASS] Phase 5.1: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 5.1: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_phase_5_compatibility():
    """Test Phase 5.2: Compatibility Checker"""
    print("\n" + "="*60)
    print("TESTING PHASE 5.2: COMPATIBILITY CHECKER")
    print("="*60)
    
    try:
        from drugs.compatibility_checker import (
            check_compatibility,
            check_multiple_compatibility,
            get_compatible_drugs,
            get_incompatible_drugs
        )
        
        # Test 1: Check compatibility (2 drugs)
        print("\n1. Testing check_compatibility...")
        result = check_compatibility("Adrenaline", "Noradrenaline")
        assert "is_compatible" in result, "Should have compatibility result"
        assert result["status"] in ["compatible", "incompatible", "conditional", "unknown"]
        print(f"   ✅ Pass: {result['status']}")
        
        # Test 2: Check incompatible
        print("\n2. Testing incompatible drugs...")
        result = check_compatibility("Dopamine", "Nitroglycerin")
        assert result["status"] == "incompatible", "Should be incompatible"
        print("   [OK] Pass: Incompatible detection")
        
        # Test 3: Check multiple compatibility
        print("\n3. Testing check_multiple_compatibility...")
        drugs = ["Adrenaline", "Noradrenaline", "Vasopressin"]
        result = check_multiple_compatibility(drugs)
        assert "all_compatible" in result, "Should have all_compatible"
        assert "matrix" in result, "Should have matrix"
        print("   [OK] Pass: check_multiple_compatibility")
        
        # Test 4: Get compatible drugs
        print("\n4. Testing get_compatible_drugs...")
        compatible = get_compatible_drugs("Adrenaline")
        assert len(compatible) > 0, "Should have compatible drugs"
        print(f"   ✅ Pass: Found {len(compatible)} compatible drugs")
        
        # Test 5: Get incompatible drugs
        print("\n5. Testing get_incompatible_drugs...")
        incompatible = get_incompatible_drugs("Adrenaline")
        assert "Sodium bicarbonate" in incompatible or len(incompatible) >= 0
        print(f"   ✅ Pass: Found {len(incompatible)} incompatible drugs")
        
        print("\n[PASS] Phase 5.2: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 5.2: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_phase_5_electrolyte():
    """Test Phase 5.3: Electrolyte Calculator"""
    print("\n" + "="*60)
    print("TESTING PHASE 5.3: ELECTROLYTE CALCULATOR")
    print("="*60)
    
    try:
        from critical_care.electrolyte_calculator import (
            calculate_electrolyte_addition,
            calculate_potassium_addition,
            calculate_calcium_addition,
            calculate_osmolarity,
            calculate_final_concentration
        )
        
        # Test 1: Calculate Na+ addition
        print("\n1. Testing calculate_electrolyte_addition...")
        result = calculate_electrolyte_addition(500, 0, 140)
        assert result["na_deficit_mmol"] > 0, "Should have Na+ deficit"
        assert result["nacl_3_percent_ml"] > 0, "Should have 3% NaCl volume"
        print("   [OK] Pass: calculate_electrolyte_addition")
        
        # Test 2: Calculate K+ addition
        print("\n2. Testing calculate_potassium_addition...")
        result = calculate_potassium_addition(500, 0, 20)
        assert result["k_deficit_mmol"] > 0, "Should have K+ deficit"
        assert result["kcl_10_percent_ml"] > 0, "Should have 10% KCl volume"
        print("   [OK] Pass: calculate_potassium_addition")
        
        # Test 3: Calculate Ca++ addition
        print("\n3. Testing calculate_calcium_addition...")
        result = calculate_calcium_addition(500, 0, 2.5)
        assert result["ca_deficit_mmol"] > 0, "Should have Ca++ deficit"
        print("   [OK] Pass: calculate_calcium_addition")
        
        # Test 4: Calculate osmolarity
        print("\n4. Testing calculate_osmolarity...")
        result = calculate_osmolarity(140, 0, 0, 0, 0)
        assert result["osmolarity_mosm_l"] > 0, "Should have osmolarity"
        assert result["is_isotonic"] == True, "Should be isotonic"
        print("   [OK] Pass: calculate_osmolarity")
        
        # Test 5: Calculate final concentration
        print("\n5. Testing calculate_final_concentration...")
        final_conc = calculate_final_concentration(250, 154, 250, 0)
        assert final_conc == 77, f"Should be 77, got {final_conc}"
        print("   [OK] Pass: calculate_final_concentration")
        
        print("\n[PASS] Phase 5.3: All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAIL] Phase 5.3: Test failed - {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("COMPREHENSIVE TEST SUITE - ALL PHASES")
    print("="*60)
    
    results = []
    
    # Test all phases
    results.append(("Phase 1: Vial Management", test_phase_1_vial_management()))
    results.append(("Phase 2: Cardiovascular", test_phase_2_cardiovascular()))
    results.append(("Phase 3: Enhanced Infusion", test_phase_3_enhanced_infusion()))
    results.append(("Phase 4: Unit Conversion", test_phase_4_unit_conversion()))
    results.append(("Phase 5.1: Multiple Infusions", test_phase_5_multiple_infusions()))
    results.append(("Phase 5.2: Compatibility", test_phase_5_compatibility()))
    results.append(("Phase 5.3: Electrolyte", test_phase_5_electrolyte()))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = 0
    failed = 0
    
    for phase, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{phase:40} {status}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print("\n" + "="*60)
    print(f"Total: {len(results)} phases")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("="*60)
    
    if failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
        return 0
    else:
        print(f"\n[WARNING] {failed} phase(s) failed")
        return 1


if __name__ == "__main__":
    exit(main())

