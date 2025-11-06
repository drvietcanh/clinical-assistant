"""
Test Script for Ventilator PHIÊN 1
Kiểm tra các chức năng đã triển khai
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
        from ventilator.abg_integration import (
            render_abg_panel,
            calculate_pf_ratio,
            classify_ards,
            analyze_acid_base,
            display_abg_summary
        )
        print("✅ ABG Integration imports: OK")
    except Exception as e:
        print(f"❌ ABG Integration imports: FAILED - {e}")
        return False
    
    try:
        from ventilator.comprehensive_calculator import (
            calculate_pbw,
            calculate_driving_pressure,
            calculate_compliance,
            interpret_compliance,
            render_comprehensive_calculator
        )
        print("✅ Comprehensive Calculator imports: OK")
    except Exception as e:
        print(f"❌ Comprehensive Calculator imports: FAILED - {e}")
        return False
    
    try:
        from ventilator import (
            render_ardsnet,
            render_initial_settings,
            render_peep_fio2_table,
            render_comprehensive_calculator
        )
        print("✅ Ventilator module imports: OK")
    except Exception as e:
        print(f"❌ Ventilator module imports: FAILED - {e}")
        return False
    
    return True


def test_pf_ratio():
    """Test P/F ratio calculation"""
    print("\n" + "=" * 60)
    print("TEST 2: Tính P/F Ratio")
    print("=" * 60)
    
    from ventilator.abg_integration import calculate_pf_ratio
    
    test_cases = [
        {"po2": 95, "fio2": 21, "expected": 452},  # Bình thường
        {"po2": 100, "fio2": 30, "expected": 333},  # Thiếu oxy nhẹ
        {"po2": 80, "fio2": 40, "expected": 200},   # ARDS nhẹ
        {"po2": 60, "fio2": 50, "expected": 120},  # ARDS trung bình
        {"po2": 50, "fio2": 100, "expected": 50},  # ARDS nặng
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_pf_ratio(case["po2"], case["fio2"])
        expected = case["expected"]
        if abs(result - expected) < 5:  # Allow small rounding differences
            print(f"✅ Test {i}: P/F = {result:.0f} (expected ~{expected})")
        else:
            print(f"❌ Test {i}: P/F = {result:.0f} (expected ~{expected})")
            all_passed = False
    
    return all_passed


def test_ards_classification():
    """Test ARDS classification"""
    print("\n" + "=" * 60)
    print("TEST 3: Phân Loại ARDS")
    print("=" * 60)
    
    from ventilator.abg_integration import classify_ards
    
    test_cases = [
        {"pf": 450, "expected_class": "Bình thường", "expected_color": "success"},
        {"pf": 350, "expected_class": "Thiếu oxy nhẹ", "expected_color": "info"},
        {"pf": 250, "expected_class": "ARDS nhẹ", "expected_color": "warning"},
        {"pf": 150, "expected_class": "ARDS trung bình", "expected_color": "error"},
        {"pf": 80, "expected_class": "ARDS nặng", "expected_color": "error"},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        class_name, color, _ = classify_ards(case["pf"])
        if class_name == case["expected_class"] and color == case["expected_color"]:
            print(f"✅ Test {i}: {class_name} ({color})")
        else:
            print(f"❌ Test {i}: Got {class_name} ({color}), expected {case['expected_class']} ({case['expected_color']})")
            all_passed = False
    
    return all_passed


def test_acid_base_analysis():
    """Test acid-base analysis"""
    print("\n" + "=" * 60)
    print("TEST 4: Phân Tích Acid-Base")
    print("=" * 60)
    
    from ventilator.abg_integration import analyze_acid_base
    
    test_cases = [
        {"ph": 7.20, "pco2": 50, "hco3": 20, "expected": "Respiratory Acidosis"},
        {"ph": 7.50, "pco2": 30, "hco3": 24, "expected": "Respiratory Alkalosis"},
        {"ph": 7.25, "pco2": 40, "hco3": 18, "expected": "Metabolic Acidosis"},
        {"ph": 7.55, "pco2": 40, "hco3": 30, "expected": "Metabolic Alkalosis"},
        {"ph": 7.40, "pco2": 40, "hco3": 24, "expected": None},  # Normal
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        disorders = analyze_acid_base(case["ph"], case["pco2"], case["hco3"])
        if case["expected"] is None:
            if len(disorders) == 0:
                print(f"✅ Test {i}: Normal (no disorders)")
            else:
                print(f"❌ Test {i}: Expected normal, got {len(disorders)} disorders")
                all_passed = False
        else:
            if len(disorders) > 0 and case["expected"] in disorders[0]["type"]:
                print(f"✅ Test {i}: {disorders[0]['type']}")
            else:
                print(f"❌ Test {i}: Expected {case['expected']}, got {disorders}")
                all_passed = False
    
    return all_passed


def test_pbw_calculation():
    """Test PBW calculation"""
    print("\n" + "=" * 60)
    print("TEST 5: Tính PBW")
    print("=" * 60)
    
    from ventilator.comprehensive_calculator import calculate_pbw
    
    test_cases = [
        {"sex": "Nam", "height": 170, "expected": 66.0},
        {"sex": "Nữ", "height": 160, "expected": 52.3},
        {"sex": "Nam", "height": 180, "expected": 75.1},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_pbw(case["sex"], case["height"])
        if abs(result - case["expected"]) < 0.5:
            print(f"✅ Test {i}: PBW = {result:.1f} kg (expected ~{case['expected']})")
        else:
            print(f"❌ Test {i}: PBW = {result:.1f} kg (expected ~{case['expected']})")
            all_passed = False
    
    return all_passed


def test_driving_pressure():
    """Test driving pressure calculation"""
    print("\n" + "=" * 60)
    print("TEST 6: Tính Driving Pressure")
    print("=" * 60)
    
    from ventilator.comprehensive_calculator import calculate_driving_pressure
    
    test_cases = [
        {"plateau": 25, "peep": 10, "expected": 15},
        {"plateau": 30, "peep": 10, "expected": 20},
        {"plateau": 20, "peep": 5, "expected": 15},
        {"plateau": 0, "peep": 5, "expected": None},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_driving_pressure(case["plateau"], case["peep"])
        if case["expected"] is None:
            if result is None:
                print(f"✅ Test {i}: Driving P = None (expected)")
            else:
                print(f"❌ Test {i}: Driving P = {result} (expected None)")
                all_passed = False
        else:
            if result == case["expected"]:
                print(f"✅ Test {i}: Driving P = {result} cmH2O")
            else:
                print(f"❌ Test {i}: Driving P = {result} cmH2O (expected {case['expected']})")
                all_passed = False
    
    return all_passed


def test_compliance():
    """Test compliance calculation"""
    print("\n" + "=" * 60)
    print("TEST 7: Tính Compliance")
    print("=" * 60)
    
    from ventilator.comprehensive_calculator import calculate_compliance, interpret_compliance
    
    test_cases = [
        {"vt": 420, "plateau": 25, "peep": 10, "expected": 28.0},  # Low compliance
        {"vt": 500, "plateau": 20, "peep": 5, "expected": 33.3},  # Normal compliance
        {"vt": 600, "plateau": 20, "peep": 5, "expected": 40.0},  # Normal compliance
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_compliance(case["vt"], case["plateau"], case["peep"])
        if result and abs(result - case["expected"]) < 2:
            interpretation, color = interpret_compliance(result)
            print(f"✅ Test {i}: Compliance = {result:.1f} mL/cmH2O ({interpretation})")
        else:
            print(f"❌ Test {i}: Compliance = {result} (expected ~{case['expected']})")
            all_passed = False
    
    return all_passed


def test_edge_cases():
    """Test edge cases"""
    print("\n" + "=" * 60)
    print("TEST 8: Edge Cases")
    print("=" * 60)
    
    from ventilator.abg_integration import calculate_pf_ratio, classify_ards
    from ventilator.comprehensive_calculator import calculate_driving_pressure, calculate_compliance
    
    all_passed = True
    
    # Test P/F ratio with FiO2 = 0
    result = calculate_pf_ratio(100, 0)
    if result is None:
        print("✅ P/F ratio với FiO2 = 0: None (correct)")
    else:
        print(f"❌ P/F ratio với FiO2 = 0: {result} (expected None)")
        all_passed = False
    
    # Test P/F ratio with None
    result = classify_ards(None)
    if result[0] is None:
        print("✅ ARDS classification với None: None (correct)")
    else:
        print(f"❌ ARDS classification với None: {result} (expected None)")
        all_passed = False
    
    # Test driving pressure with invalid values
    result = calculate_driving_pressure(0, 0)
    if result is None:
        print("✅ Driving pressure với 0,0: None (correct)")
    else:
        print(f"❌ Driving pressure với 0,0: {result} (expected None)")
        all_passed = False
    
    # Test compliance with invalid values
    result = calculate_compliance(0, 20, 10)
    if result is None:
        print("✅ Compliance với Vt = 0: None (correct)")
    else:
        print(f"❌ Compliance với Vt = 0: {result} (expected None)")
        all_passed = False
    
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("KIỂM TRA CHỨC NĂNG - VENTILATOR PHIÊN 1")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("P/F Ratio", test_pf_ratio()))
    results.append(("ARDS Classification", test_ards_classification()))
    results.append(("Acid-Base Analysis", test_acid_base_analysis()))
    results.append(("PBW Calculation", test_pbw_calculation()))
    results.append(("Driving Pressure", test_driving_pressure()))
    results.append(("Compliance", test_compliance()))
    results.append(("Edge Cases", test_edge_cases()))
    
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

