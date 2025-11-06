"""
Test Script for Ventilator PHIÊN 4
Kiểm tra các chức năng Weaning Protocol
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test imports"""
    print("=" * 60)
    print("TEST 1: Kiểm tra Imports")
    print("=" * 60)
    
    try:
        from ventilator.weaning import (
            calculate_rsbi,
            interpret_rsbi,
            assess_weaning_readiness,
            render_weaning_calculator
        )
        print("✅ Weaning imports: OK")
    except Exception as e:
        print(f"❌ Weaning imports: FAILED - {e}")
        return False
    
    try:
        from ventilator import (
            calculate_rsbi,
            interpret_rsbi,
            assess_weaning_readiness
        )
        print("✅ Ventilator module exports: OK")
    except Exception as e:
        print(f"❌ Ventilator module exports: FAILED - {e}")
        return False
    
    return True


def test_rsbi_calculation():
    """Test RSBI calculation"""
    print("\n" + "=" * 60)
    print("TEST 2: RSBI Calculation")
    print("=" * 60)
    
    from ventilator.weaning import calculate_rsbi
    
    test_cases = [
        {"rr": 20, "vt_ml": 500, "expected": 40},  # Good RSBI
        {"rr": 30, "vt_ml": 300, "expected": 100},  # Borderline
        {"rr": 40, "vt_ml": 250, "expected": 160},  # Poor RSBI
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        vt_liters = case["vt_ml"] / 1000
        result = calculate_rsbi(case["rr"], vt_liters)
        if result and abs(result - case["expected"]) < 5:
            print(f"✅ Test {i}: RSBI = {result:.0f} (expected ~{case['expected']})")
        else:
            print(f"❌ Test {i}: RSBI = {result} (expected ~{case['expected']})")
            all_passed = False
    
    # Test edge case
    result = calculate_rsbi(20, 0)
    if result is None:
        print("✅ Edge case: Vt = 0 → None (correct)")
    else:
        print(f"❌ Edge case: Vt = 0 → {result} (expected None)")
        all_passed = False
    
    return all_passed


def test_rsbi_interpretation():
    """Test RSBI interpretation"""
    print("\n" + "=" * 60)
    print("TEST 3: RSBI Interpretation")
    print("=" * 60)
    
    from ventilator.weaning import interpret_rsbi
    
    test_cases = [
        {"rsbi": 50, "expected": "Tốt", "color": "success"},
        {"rsbi": 100, "expected": "Tốt", "color": "success"},
        {"rsbi": 110, "expected": "Trung bình", "color": "warning"},
        {"rsbi": 125, "expected": "Trung bình", "color": "warning"},
        {"rsbi": 150, "expected": "Kém", "color": "error"},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        interpretation, color, _ = interpret_rsbi(case["rsbi"])
        if interpretation == case["expected"] and color == case["color"]:
            print(f"✅ Test {i}: {interpretation} ({color})")
        else:
            print(f"❌ Test {i}: Got {interpretation} ({color}), expected {case['expected']} ({case['color']})")
            all_passed = False
    
    return all_passed


def test_weaning_readiness():
    """Test weaning readiness assessment"""
    print("\n" + "=" * 60)
    print("TEST 4: Weaning Readiness Assessment")
    print("=" * 60)
    
    from ventilator.weaning import assess_weaning_readiness
    
    # Test case 1: Ready
    abg_ready = {"ph": 7.40, "pco2": 40, "po2": 100, "hco3": 24, "fio2": 40}
    vent_ready = {"peep": 5, "fio2": 40}
    vitals_ready = {"hr": 80, "bp_systolic": 120, "temp": 37}
    neuro_ready = {"gcs": 15}
    other_ready = {"no_sepsis": True, "no_acidosis": True, "hemodynamically_stable": True}
    
    criteria, readiness, readiness_color, passed_ratio = assess_weaning_readiness(
        abg_ready, vent_ready, vitals_ready, neuro_ready, other_ready
    )
    
    if readiness == "Sẵn sàng" and readiness_color == "success":
        print(f"✅ Ready case: {readiness} ({readiness_color}) - {len(criteria['passed'])} criteria passed")
    else:
        print(f"❌ Ready case: Got {readiness} ({readiness_color}), expected Sẵn sàng (success)")
        return False
    
    # Test case 2: Not ready
    abg_not_ready = {"ph": 7.25, "pco2": 55, "po2": 80, "hco3": 20, "fio2": 60}
    vent_not_ready = {"peep": 12, "fio2": 60}
    vitals_not_ready = {"hr": 120, "bp_systolic": 85, "temp": 38.5}
    neuro_not_ready = {"gcs": 10}
    other_not_ready = {"no_sepsis": False, "no_acidosis": False, "hemodynamically_stable": False}
    
    criteria2, readiness2, readiness_color2, passed_ratio2 = assess_weaning_readiness(
        abg_not_ready, vent_not_ready, vitals_not_ready, neuro_not_ready, other_not_ready
    )
    
    if readiness2 == "Chưa sẵn sàng" and readiness_color2 == "error":
        print(f"✅ Not ready case: {readiness2} ({readiness_color2}) - {len(criteria2['failed'])} criteria failed")
    else:
        print(f"❌ Not ready case: Got {readiness2} ({readiness_color2}), expected Chưa sẵn sàng (error)")
        return False
    
    return True


def test_sbt_protocol():
    """Test SBT protocol"""
    print("\n" + "=" * 60)
    print("TEST 5: SBT Protocol")
    print("=" * 60)
    
    from ventilator.weaning import sbt_protocol
    
    protocol = sbt_protocol()
    
    if "steps" in protocol and len(protocol["steps"]) == 4:
        print(f"✅ SBT Protocol: {len(protocol['steps'])} steps defined")
    else:
        print(f"❌ SBT Protocol: Expected 4 steps, got {len(protocol.get('steps', []))}")
        return False
    
    if "success_criteria" in protocol and len(protocol["success_criteria"]) > 0:
        print(f"✅ Success criteria: {len(protocol['success_criteria'])} criteria")
    else:
        print("❌ Success criteria: Not found or empty")
        return False
    
    if "failure_criteria" in protocol and len(protocol["failure_criteria"]) > 0:
        print(f"✅ Failure criteria: {len(protocol['failure_criteria'])} criteria")
    else:
        print("❌ Failure criteria: Not found or empty")
        return False
    
    return True


def test_integration():
    """Test integration"""
    print("\n" + "=" * 60)
    print("TEST 6: Integration Test")
    print("=" * 60)
    
    try:
        from ventilator.weaning import render_weaning_calculator
        print("✅ Weaning calculator imports OK")
    except Exception as e:
        print(f"❌ Weaning calculator imports: FAILED - {e}")
        return False
    
    # Test that functions work together
    from ventilator.weaning import calculate_rsbi, interpret_rsbi, assess_weaning_readiness
    
    rsbi = calculate_rsbi(25, 0.4)  # RR=25, Vt=400mL
    interpretation, color, _ = interpret_rsbi(rsbi)
    
    if rsbi and interpretation:
        print(f"✅ Integration: RSBI = {rsbi:.0f} ({interpretation})")
    else:
        print("❌ Integration: Functions not working together")
        return False
    
    # Test readiness assessment
    abg = {"ph": 7.40, "pco2": 40, "po2": 100, "hco3": 24, "fio2": 40}
    vent = {"peep": 5, "fio2": 40}
    vitals = {"hr": 80, "bp_systolic": 120, "temp": 37}
    neuro = {"gcs": 15}
    other = {"no_sepsis": True, "no_acidosis": True, "hemodynamically_stable": True}
    
    criteria, readiness, _, _ = assess_weaning_readiness(abg, vent, vitals, neuro, other)
    
    if readiness:
        print(f"✅ Integration: Readiness assessment = {readiness}")
    else:
        print("❌ Integration: Readiness assessment failed")
        return False
    
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("KIỂM TRA CHỨC NĂNG - VENTILATOR PHIÊN 4")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("RSBI Calculation", test_rsbi_calculation()))
    results.append(("RSBI Interpretation", test_rsbi_interpretation()))
    results.append(("Weaning Readiness", test_weaning_readiness()))
    results.append(("SBT Protocol", test_sbt_protocol()))
    results.append(("Integration", test_integration()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TỔNG KẾT")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nKết quả: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 TẤT CẢ TESTS ĐÃ PASS!")
        return 0
    else:
        print(f"\n⚠️ Có {total - passed} tests failed. Vui lòng kiểm tra lại.")
        return 1


if __name__ == "__main__":
    exit(main())

