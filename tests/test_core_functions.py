"""
Core Functions Test - Test core calculation functions without Streamlit
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_vial_manager():
    """Test vial manager core functions"""
    print("\n=== Testing Vial Manager ===")
    try:
        # Import directly, avoid __init__.py
        from drugs.vial_manager import calculate_vials_needed, calculate_preparation
        
        result = calculate_vials_needed("Adrenaline", 1.5, "1mg/1ml")
        assert result["vials_needed"] == 2
        print("[OK] calculate_vials_needed")
        
        result = calculate_preparation("Adrenaline", 1.5, "1mg/1ml", 50)
        assert result["vials_needed"] == 2
        print("[OK] calculate_preparation")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def test_cardiovascular_calculator():
    """Test cardiovascular calculator"""
    print("\n=== Testing Cardiovascular Calculator ===")
    try:
        from drugs.cardiovascular_calculator import (
            get_drug_names,
            calculate_complete_infusion
        )
        
        drugs = get_drug_names()
        assert len(drugs) > 0
        print(f"[OK] get_drug_names: {len(drugs)} drugs")
        
        result = calculate_complete_infusion("Adrenaline", 0.1, 70, "syringe_pump_50ml")
        assert result["infusion_rate_ml_hour"] > 0
        print("[OK] calculate_complete_infusion")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def test_enhanced_infusion():
    """Test enhanced infusion"""
    print("\n=== Testing Enhanced Infusion ===")
    try:
        from critical_care.enhanced_infusion import (
            calculate_infusion_rate,
            calculate_dose_from_rate
        )
        
        result = calculate_infusion_rate(0.1, 70, 20, 20)
        assert result["infusion_rate_ml_hour"] > 0
        print("[OK] calculate_infusion_rate")
        
        result = calculate_dose_from_rate(10, 70, 20)
        assert result["dose_mcg_kg_min"] > 0
        print("[OK] calculate_dose_from_rate (reverse)")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def test_unit_converter():
    """Test unit converter"""
    print("\n=== Testing Unit Converter ===")
    try:
        from utils.unit_converter_enhanced import (
            detect_unit,
            convert_value
        )
        
        detected = detect_unit("5.2 mg/dL", "creatinine")
        assert detected[1] == "mg/dL"
        print("[OK] detect_unit")
        
        converted = convert_value(5.2, "mg/dL", "µmol/L", "creatinine")
        expected = 5.2 * 88.4
        assert abs(converted - expected) < 0.1
        print("[OK] convert_value")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def test_multiple_infusions():
    """Test multiple infusions"""
    print("\n=== Testing Multiple Infusions ===")
    try:
        from critical_care.multiple_infusions import (
            InfusionItem,
            calculate_total_rate
        )
        
        item = InfusionItem("Adrenaline", 0.1, 70, "syringe_pump_50ml")
        result = item.calculate()
        assert result["infusion_rate_ml_hour"] > 0
        print("[OK] InfusionItem")
        
        infusions = [item]
        total = calculate_total_rate(infusions)
        assert total["total_rate_ml_hour"] > 0
        print("[OK] calculate_total_rate")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def test_compatibility():
    """Test compatibility checker"""
    print("\n=== Testing Compatibility Checker ===")
    try:
        from drugs.compatibility_checker import (
            check_compatibility,
            check_multiple_compatibility
        )
        
        result = check_compatibility("Adrenaline", "Noradrenaline")
        assert result["status"] in ["compatible", "incompatible", "conditional", "unknown"]
        print(f"[OK] check_compatibility: {result['status']}")
        
        result = check_multiple_compatibility(["Adrenaline", "Noradrenaline"])
        assert "all_compatible" in result
        print("[OK] check_multiple_compatibility")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def test_electrolyte():
    """Test electrolyte calculator"""
    print("\n=== Testing Electrolyte Calculator ===")
    try:
        from critical_care.electrolyte_calculator import (
            calculate_electrolyte_addition,
            calculate_osmolarity
        )
        
        result = calculate_electrolyte_addition(500, 0, 140)
        assert result["na_deficit_mmol"] > 0
        print("[OK] calculate_electrolyte_addition")
        
        result = calculate_osmolarity(140, 0, 0, 0, 0)
        assert result["osmolarity_mosm_l"] > 0
        print("[OK] calculate_osmolarity")
        
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("CORE FUNCTIONS TEST SUITE")
    print("="*60)
    
    tests = [
        ("Vial Manager", test_vial_manager),
        ("Cardiovascular Calculator", test_cardiovascular_calculator),
        ("Enhanced Infusion", test_enhanced_infusion),
        ("Unit Converter", test_unit_converter),
        ("Multiple Infusions", test_multiple_infusions),
        ("Compatibility Checker", test_compatibility),
        ("Electrolyte Calculator", test_electrolyte),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"[ERROR] {name}: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, r in results if r)
    failed = len(results) - passed
    
    for name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{name:30} {status}")
    
    print("\n" + "="*60)
    print(f"Total: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("="*60)
    
    if failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
        return 0
    else:
        print(f"\n[WARNING] {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    exit(main())

