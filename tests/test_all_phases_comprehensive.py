"""
Comprehensive Test Script for All Phases
Test all core functions without Streamlit UI
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Avoid importing __init__ files that require streamlit
import importlib.util

def test_phase1_vial_management():
    """Test Phase 1: Vial Management"""
    print("\n" + "="*60)
    print("TESTING PHASE 1: VIAL MANAGEMENT")
    print("="*60)
    
    try:
        # Import directly from file to avoid __init__ issues
        vial_manager_path = Path(__file__).parent.parent / "drugs" / "vial_manager.py"
        spec = importlib.util.spec_from_file_location("vial_manager", vial_manager_path)
        vial_manager = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vial_manager)
        calculate_vials_needed = vial_manager.calculate_vials_needed
        get_vial_info = vial_manager.get_vial_info
        
        # Test 1: Calculate vials needed
        result = calculate_vials_needed("Adrenaline", 1.0, "1mg/1ml")
        assert result["vials_needed"] == 1, "Test 1 failed"
        print("[OK] Test 1: Calculate vials needed - PASS")
        
        # Test 2: Calculate with different vial
        result2 = calculate_vials_needed("Adrenaline", 2.0, "1mg/1ml")
        assert result2["vials_needed"] == 2, "Test 2 failed"
        print("[OK] Test 2: Calculate multiple vials - PASS")
        
        print("[OK] Phase 1: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 1: FAILED - {str(e)}")
        return False


def test_phase2_cardiovascular():
    """Test Phase 2: Cardiovascular Drugs"""
    print("\n" + "="*60)
    print("TESTING PHASE 2: CARDIOVASCULAR DRUGS")
    print("="*60)
    
    try:
        # Import directly from file
        cv_path = Path(__file__).parent.parent / "drugs" / "cardiovascular_calculator.py"
        spec = importlib.util.spec_from_file_location("cv_calc", cv_path)
        cv_calc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cv_calc)
        calculate_complete_infusion = cv_calc.calculate_complete_infusion
        get_drug_names = cv_calc.get_drug_names
        validate_dose_range = cv_calc.validate_dose_range
        
        # Test 1: Get drug names
        drugs = get_drug_names()
        assert len(drugs) > 0, "Test 1 failed"
        print(f"[OK] Test 1: Get drug names - PASS ({len(drugs)} drugs)")
        
        # Test 2: Validate dose range
        validation = validate_dose_range("Noradrenaline", 0.1)
        assert validation.get("is_valid", False), "Test 2 failed"
        print("[OK] Test 2: Validate dose range - PASS")
        
        # Test 3: Calculate complete infusion
        result = calculate_complete_infusion(
            "Noradrenaline", 0.1, 70.0, "syringe_pump_50ml"
        )
        assert result.get("infusion_rate_ml_hour", 0) > 0, "Test 3 failed"
        print("[OK] Test 3: Calculate complete infusion - PASS")
        
        print("[OK] Phase 2: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 2: FAILED - {str(e)}")
        return False


def test_phase3_enhanced_infusion():
    """Test Phase 3: Enhanced Infusion"""
    print("\n" + "="*60)
    print("TESTING PHASE 3: ENHANCED INFUSION")
    print("="*60)
    
    try:
        from critical_care.enhanced_infusion import (
            calculate_infusion_rate,
            calculate_infusion_time,
            calculate_volume_needed
        )
        
        # Test 1: Calculate infusion rate
        rate = calculate_infusion_rate(500, 10)
        assert rate == 50.0, "Test 1 failed"
        print("[OK] Test 1: Calculate infusion rate - PASS")
        
        # Test 2: Calculate infusion time
        time = calculate_infusion_time(500, 50)
        assert time["time_hours"] == 10.0, "Test 2 failed"
        print("[OK] Test 2: Calculate infusion time - PASS")
        
        # Test 3: Calculate volume needed
        volume = calculate_volume_needed(50, 10)
        assert volume == 500.0, "Test 3 failed"
        print("[OK] Test 3: Calculate volume needed - PASS")
        
        print("[OK] Phase 3: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 3: FAILED - {str(e)}")
        return False


def test_phase4_unit_converter():
    """Test Phase 4: Unit Converter"""
    print("\n" + "="*60)
    print("TESTING PHASE 4: UNIT CONVERTER")
    print("="*60)
    
    try:
        from utils.unit_converter_enhanced import (
            convert_weight,
            convert_volume,
            convert_concentration
        )
        
        # Test 1: Convert weight
        result = convert_weight(1.0, "kg", "g")
        assert result == 1000.0, "Test 1 failed"
        print("[OK] Test 1: Convert weight - PASS")
        
        # Test 2: Convert volume
        result = convert_volume(1.0, "L", "ml")
        assert result == 1000.0, "Test 2 failed"
        print("[OK] Test 2: Convert volume - PASS")
        
        # Test 3: Convert concentration
        result = convert_concentration(1.0, "mg/ml", "mcg/ml")
        assert result == 1000.0, "Test 3 failed"
        print("[OK] Test 3: Convert concentration - PASS")
        
        print("[OK] Phase 4: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 4: FAILED - {str(e)}")
        return False


def test_phase5_multiple_infusions():
    """Test Phase 5.1: Multiple Infusions"""
    print("\n" + "="*60)
    print("TESTING PHASE 5.1: MULTIPLE INFUSIONS")
    print("="*60)
    
    try:
        from critical_care.multiple_infusions import calculate_multiple_infusions
        
        # Test 1: Calculate multiple infusions
        infusions = [
            {"rate_ml_hour": 50, "volume_ml": 500},
            {"rate_ml_hour": 30, "volume_ml": 300}
        ]
        result = calculate_multiple_infusions(infusions)
        assert result["total_rate_ml_hour"] == 80.0, "Test 1 failed"
        assert result["total_volume_ml"] == 800.0, "Test 1 failed"
        print("[OK] Test 1: Calculate multiple infusions - PASS")
        
        print("[OK] Phase 5.1: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 5.1: FAILED - {str(e)}")
        return False


def test_phase5_compatibility():
    """Test Phase 5.2: Compatibility Checker"""
    print("\n" + "="*60)
    print("TESTING PHASE 5.2: COMPATIBILITY CHECKER")
    print("="*60)
    
    try:
        from drugs.compatibility_checker import check_compatibility
        
        # Test 1: Check compatibility
        result = check_compatibility("Noradrenaline", "Dopamine")
        assert "compatible" in result, "Test 1 failed"
        print("[OK] Test 1: Check compatibility - PASS")
        
        print("[OK] Phase 5.2: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 5.2: FAILED - {str(e)}")
        return False


def test_phase5_electrolyte():
    """Test Phase 5.3: Electrolyte Calculator"""
    print("\n" + "="*60)
    print("TESTING PHASE 5.3: ELECTROLYTE CALCULATOR")
    print("="*60)
    
    try:
        from critical_care.electrolyte_calculator import (
            calculate_sodium_correction,
            calculate_potassium_correction
        )
        
        # Test 1: Calculate sodium correction
        result = calculate_sodium_correction(130, 140, 70)
        assert result["volume_ml"] > 0, "Test 1 failed"
        print("[OK] Test 1: Calculate sodium correction - PASS")
        
        # Test 2: Calculate potassium correction
        result = calculate_potassium_correction(3.0, 4.0, 70)
        assert result["volume_ml"] > 0, "Test 2 failed"
        print("[OK] Test 2: Calculate potassium correction - PASS")
        
        print("[OK] Phase 5.3: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 5.3: FAILED - {str(e)}")
        return False


def test_phase6_pediatric():
    """Test Phase 6.1: Pediatric Dosing"""
    print("\n" + "="*60)
    print("TESTING PHASE 6.1: PEDIATRIC DOSING")
    print("="*60)
    
    try:
        from drugs.pediatric_dosing import calculate_pediatric_dose
        
        # Test 1: Calculate pediatric dose
        result = calculate_pediatric_dose("Paracetamol", 10.0, "child")
        assert result["adjusted_dose_mg"] > 0, "Test 1 failed"
        print("[OK] Test 1: Calculate pediatric dose - PASS")
        
        print("[OK] Phase 6.1: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 6.1: FAILED - {str(e)}")
        return False


def test_phase6_renal():
    """Test Phase 6.2: Renal Dose Adjustment"""
    print("\n" + "="*60)
    print("TESTING PHASE 6.2: RENAL DOSE ADJUSTMENT")
    print("="*60)
    
    try:
        from drugs.renal_dosing import (
            calculate_egfr,
            adjust_dose_for_renal_function
        )
        
        # Test 1: Calculate eGFR
        egfr = calculate_egfr(70, 1.0, "male", 30)
        assert egfr > 0, "Test 1 failed"
        print("[OK] Test 1: Calculate eGFR - PASS")
        
        # Test 2: Adjust dose for renal function
        result = adjust_dose_for_renal_function("Vancomycin", 1000, egfr)
        assert result["adjusted_dose_mg"] > 0, "Test 2 failed"
        print("[OK] Test 2: Adjust dose for renal function - PASS")
        
        print("[OK] Phase 6.2: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 6.2: FAILED - {str(e)}")
        return False


def test_phase7_titration():
    """Test Phase 7.1: Titration Guide"""
    print("\n" + "="*60)
    print("TESTING PHASE 7.1: TITRATION GUIDE")
    print("="*60)
    
    try:
        from critical_care.titration_guide import (
            calculate_titration,
            get_titration_summary
        )
        
        # Test 1: Calculate titration
        result = calculate_titration(
            "Noradrenaline", 0.1, 0.15, 70.0, "syringe_pump_50ml"
        )
        assert result["dose_change"] > 0, "Test 1 failed"
        print("[OK] Test 1: Calculate titration - PASS")
        
        # Test 2: Get titration summary
        history = [result]
        summary = get_titration_summary(history)
        assert summary["total_steps"] == 1, "Test 2 failed"
        print("[OK] Test 2: Get titration summary - PASS")
        
        print("[OK] Phase 7.1: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 7.1: FAILED - {str(e)}")
        return False


def test_phase7_safety():
    """Test Phase 7.2: Safety Checker"""
    print("\n" + "="*60)
    print("TESTING PHASE 7.2: SAFETY CHECKER")
    print("="*60)
    
    try:
        from critical_care.safety_checker import (
            check_complete_infusion_safety,
            get_safety_checklist
        )
        
        # Test 1: Check complete infusion safety
        result = check_complete_infusion_safety(
            "Noradrenaline", 0.1, 70.0, "syringe_pump_50ml"
        )
        assert result.score >= 0, "Test 1 failed"
        print("[OK] Test 1: Check complete infusion safety - PASS")
        
        # Test 2: Get safety checklist
        checklist = get_safety_checklist()
        assert len(checklist) > 0, "Test 2 failed"
        print(f"[OK] Test 2: Get safety checklist - PASS ({len(checklist)} items)")
        
        print("[OK] Phase 7.2: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 7.2: FAILED - {str(e)}")
        return False


def test_phase8_custom_presets():
    """Test Phase 8.2: Custom Presets"""
    print("\n" + "="*60)
    print("TESTING PHASE 8.2: CUSTOM PRESETS")
    print("="*60)
    
    try:
        from drugs.custom_presets import (
            add_custom_preset,
            get_custom_preset,
            delete_custom_preset
        )
        
        # Test 1: Add custom preset
        success = add_custom_preset(
            "test_preset", "Noradrenaline", 0.1, 70.0, "syringe_pump_50ml"
        )
        assert success, "Test 1 failed"
        print("[OK] Test 1: Add custom preset - PASS")
        
        # Test 2: Get custom preset
        preset = get_custom_preset("test_preset")
        assert preset is not None, "Test 2 failed"
        print("[OK] Test 2: Get custom preset - PASS")
        
        # Test 3: Delete custom preset
        success = delete_custom_preset("test_preset")
        assert success, "Test 3 failed"
        print("[OK] Test 3: Delete custom preset - PASS")
        
        print("[OK] Phase 8.2: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 8.2: FAILED - {str(e)}")
        return False


def test_phase8_time_remaining():
    """Test Phase 8.3: Time Remaining"""
    print("\n" + "="*60)
    print("TESTING PHASE 8.3: TIME REMAINING")
    print("="*60)
    
    try:
        from critical_care.time_remaining import calculate_remaining_time
        
        # Test 1: Calculate remaining time
        result = calculate_remaining_time(500, 250, 50)
        assert result["remaining_volume_ml"] == 250.0, "Test 1 failed"
        assert result["remaining_time_hours"] == 5.0, "Test 1 failed"
        print("[OK] Test 1: Calculate remaining time - PASS")
        
        print("[OK] Phase 8.3: All tests PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Phase 8.3: FAILED - {str(e)}")
        return False


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("COMPREHENSIVE TEST SUITE - ALL PHASES")
    print("="*60)
    
    results = {}
    
    # Phase 1
    results["Phase 1"] = test_phase1_vial_management()
    
    # Phase 2
    results["Phase 2"] = test_phase2_cardiovascular()
    
    # Phase 3
    results["Phase 3"] = test_phase3_enhanced_infusion()
    
    # Phase 4
    results["Phase 4"] = test_phase4_unit_converter()
    
    # Phase 5
    results["Phase 5.1"] = test_phase5_multiple_infusions()
    results["Phase 5.2"] = test_phase5_compatibility()
    results["Phase 5.3"] = test_phase5_electrolyte()
    
    # Phase 6
    results["Phase 6.1"] = test_phase6_pediatric()
    results["Phase 6.2"] = test_phase6_renal()
    
    # Phase 7
    results["Phase 7.1"] = test_phase7_titration()
    results["Phase 7.2"] = test_phase7_safety()
    
    # Phase 8
    results["Phase 8.2"] = test_phase8_custom_presets()
    results["Phase 8.3"] = test_phase8_time_remaining()
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for phase, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{phase:15s}: {status}")
    
    print("="*60)
    print(f"Total: {passed}/{total} phases passed ({passed*100//total}%)")
    print("="*60)
    
    if passed == total:
        print("\n[SUCCESS] ALL TESTS PASSED!")
        return 0
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    exit(main())

