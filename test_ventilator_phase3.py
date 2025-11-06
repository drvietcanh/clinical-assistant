"""
Test Script for Ventilator PHIÊN 3
Kiểm tra các chức năng Compliance & Auto-PEEP
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
        from ventilator.compliance import (
            calculate_static_compliance,
            calculate_dynamic_compliance,
            interpret_compliance,
            display_compliance_analysis
        )
        print("✅ Compliance imports: OK")
    except Exception as e:
        print(f"❌ Compliance imports: FAILED - {e}")
        return False
    
    try:
        from ventilator.auto_peep import (
            estimate_auto_peep,
            interpret_auto_peep,
            display_auto_peep_analysis
        )
        print("✅ Auto-PEEP imports: OK")
    except Exception as e:
        print(f"❌ Auto-PEEP imports: FAILED - {e}")
        return False
    
    return True


def test_static_compliance():
    """Test static compliance calculation"""
    print("\n" + "=" * 60)
    print("TEST 2: Static Compliance")
    print("=" * 60)
    
    from ventilator.compliance import calculate_static_compliance, interpret_compliance
    
    test_cases = [
        {"vt": 420, "plateau": 25, "peep": 10, "expected": 28.0},
        {"vt": 500, "plateau": 20, "peep": 5, "expected": 33.3},
        {"vt": 600, "plateau": 30, "peep": 10, "expected": 30.0},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_static_compliance(case["vt"], case["plateau"], case["peep"])
        if result and abs(result - case["expected"]) < 2:
            interpretation, color, _ = interpret_compliance(result, "static")
            print(f"✅ Test {i}: Compliance = {result:.1f} mL/cmH2O ({interpretation})")
        else:
            print(f"❌ Test {i}: Compliance = {result} (expected ~{case['expected']})")
            all_passed = False
    
    # Test edge cases
    result = calculate_static_compliance(0, 25, 10)
    if result is None:
        print("✅ Edge case: Vt = 0 → None (correct)")
    else:
        print(f"❌ Edge case: Vt = 0 → {result} (expected None)")
        all_passed = False
    
    return all_passed


def test_dynamic_compliance():
    """Test dynamic compliance calculation"""
    print("\n" + "=" * 60)
    print("TEST 3: Dynamic Compliance")
    print("=" * 60)
    
    from ventilator.compliance import calculate_dynamic_compliance
    
    test_cases = [
        {"vt": 420, "peak": 30, "peep": 10, "expected": 21.0},
        {"vt": 500, "peak": 25, "peep": 5, "expected": 25.0},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_dynamic_compliance(case["vt"], case["peak"], case["peep"])
        if result and abs(result - case["expected"]) < 2:
            print(f"✅ Test {i}: Dynamic Compliance = {result:.1f} mL/cmH2O")
        else:
            print(f"❌ Test {i}: Dynamic Compliance = {result} (expected ~{case['expected']})")
            all_passed = False
    
    return all_passed


def test_compliance_interpretation():
    """Test compliance interpretation"""
    print("\n" + "=" * 60)
    print("TEST 4: Compliance Interpretation")
    print("=" * 60)
    
    from ventilator.compliance import interpret_compliance
    
    test_cases = [
        {"compliance": 15, "expected": "Rất thấp", "color": "error"},
        {"compliance": 25, "expected": "Thấp", "color": "error"},
        {"compliance": 40, "expected": "Bình thường", "color": "success"},
        {"compliance": 70, "expected": "Cao", "color": "info"},
        {"compliance": 100, "expected": "Rất cao", "color": "warning"},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        interpretation, color, _ = interpret_compliance(case["compliance"], "static")
        if interpretation == case["expected"] and color == case["color"]:
            print(f"✅ Test {i}: {interpretation} ({color})")
        else:
            print(f"❌ Test {i}: Got {interpretation} ({color}), expected {case['expected']} ({case['color']})")
            all_passed = False
    
    return all_passed


def test_auto_peep():
    """Test auto-PEEP estimation"""
    print("\n" + "=" * 60)
    print("TEST 5: Auto-PEEP Estimation")
    print("=" * 60)
    
    from ventilator.auto_peep import estimate_auto_peep, interpret_auto_peep
    
    # Test with end-expiratory pause
    auto_peep = estimate_auto_peep(25, 10, 15)
    if auto_peep == 5.0:
        print(f"✅ Auto-PEEP với end-expiratory pause: {auto_peep:.1f} cmH2O")
    else:
        print(f"❌ Auto-PEEP với end-expiratory pause: {auto_peep} (expected 5.0)")
        return False
    
    # Test interpretation
    test_cases = [
        {"auto_peep": 1, "expected": "Không đáng kể", "color": "success"},
        {"auto_peep": 3, "expected": "Nhẹ", "color": "info"},
        {"auto_peep": 7, "expected": "Trung bình", "color": "warning"},
        {"auto_peep": 12, "expected": "Nặng", "color": "error"},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        interpretation, color, _ = interpret_auto_peep(case["auto_peep"])
        if interpretation == case["expected"] and color == case["color"]:
            print(f"✅ Test {i}: {interpretation} ({color})")
        else:
            print(f"❌ Test {i}: Got {interpretation} ({color}), expected {case['expected']} ({case['color']})")
            all_passed = False
    
    return all_passed


def test_integration():
    """Test integration"""
    print("\n" + "=" * 60)
    print("TEST 6: Integration Test")
    print("=" * 60)
    
    try:
        from ventilator.comprehensive_calculator import render_comprehensive_calculator
        print("✅ Comprehensive calculator imports OK")
    except Exception as e:
        print(f"❌ Comprehensive calculator imports: FAILED - {e}")
        return False
    
    try:
        from ventilator import (
            calculate_static_compliance,
            calculate_dynamic_compliance,
            estimate_auto_peep
        )
        print("✅ Ventilator module exports OK")
    except Exception as e:
        print(f"❌ Ventilator module exports: FAILED - {e}")
        return False
    
    # Test that functions work together
    from ventilator.compliance import calculate_static_compliance
    from ventilator.auto_peep import estimate_auto_peep
    
    compliance = calculate_static_compliance(420, 25, 10)
    auto_peep = estimate_auto_peep(25, 10, 15)
    
    if compliance and auto_peep:
        print(f"✅ Integration: Compliance = {compliance:.1f}, Auto-PEEP = {auto_peep:.1f}")
    else:
        print("❌ Integration: Functions not working together")
        return False
    
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("KIỂM TRA CHỨC NĂNG - VENTILATOR PHIÊN 3")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Static Compliance", test_static_compliance()))
    results.append(("Dynamic Compliance", test_dynamic_compliance()))
    results.append(("Compliance Interpretation", test_compliance_interpretation()))
    results.append(("Auto-PEEP", test_auto_peep()))
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

