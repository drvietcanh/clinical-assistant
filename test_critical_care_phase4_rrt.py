"""
Test Script for Critical Care Phase 4: RRT Calculator
Kiểm tra các chức năng RRT (CRRT, IHD, SLED, Anticoagulation)
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
        from critical_care.rrt import (
            calculate_crrt_dosing,
            calculate_ihd_dosing,
            calculate_sled_dosing,
            calculate_anticoagulation_rrt,
            render_rrt_calculator
        )
        print("✅ RRT imports: OK")
    except Exception as e:
        print(f"❌ RRT imports: FAILED - {e}")
        return False
    
    try:
        from critical_care import (
            calculate_crrt_dosing,
            calculate_ihd_dosing,
            calculate_sled_dosing,
            calculate_anticoagulation_rrt
        )
        print("✅ Critical Care module exports: OK")
    except Exception as e:
        print(f"❌ Critical Care module exports: FAILED - {e}")
        return False
    
    return True


def test_crrt_calculation():
    """Test CRRT dosing calculation"""
    print("\n" + "=" * 60)
    print("TEST 2: CRRT Calculation")
    print("=" * 60)
    
    from critical_care.rrt import calculate_crrt_dosing
    
    test_cases = [
        {"weight": 70.0, "clearance": 25.0, "expected_flow": 1750.0},  # 70 * 25 = 1750 ml/h
        {"weight": 80.0, "clearance": 30.0, "expected_flow": 2400.0},  # 80 * 30 = 2400 ml/h
        {"weight": 60.0, "clearance": 35.0, "expected_flow": 2100.0},  # 60 * 35 = 2100 ml/h
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_crrt_dosing(case["weight"], case["clearance"])
        
        # Check key fields
        checks = [
            (result["weight_kg"] == case["weight"], f"Weight: {result['weight_kg']} == {case['weight']}"),
            (result["target_clearance"] == case["clearance"], f"Clearance: {result['target_clearance']} == {case['clearance']}"),
            (abs(result["total_flow_ml_h"] - case["expected_flow"]) < 1, f"Total flow: {result['total_flow_ml_h']:.0f} ≈ {case['expected_flow']}"),
            (abs(result["dialysate_flow_ml_h"] - case["expected_flow"] * 0.5) < 1, f"Dialysate: {result['dialysate_flow_ml_h']:.0f} ≈ {case['expected_flow'] * 0.5}"),
            (abs(result["replacement_flow_ml_h"] - case["expected_flow"] * 0.5) < 1, f"Replacement: {result['replacement_flow_ml_h']:.0f} ≈ {case['expected_flow'] * 0.5}"),
        ]
        
        passed = all(check[0] for check in checks)
        if passed:
            print(f"✅ Test {i}: Weight {case['weight']}kg, Clearance {case['clearance']} ml/kg/h")
            print(f"   Total flow: {result['total_flow_ml_h']:.0f} ml/h ({result['total_flow_l_h']:.2f} L/h)")
        else:
            print(f"❌ Test {i}: Weight {case['weight']}kg, Clearance {case['clearance']} ml/kg/h")
            for check, msg in checks:
                if not check:
                    print(f"   FAILED: {msg}")
            all_passed = False
    
    return all_passed


def test_ihd_calculation():
    """Test IHD dosing calculation"""
    print("\n" + "=" * 60)
    print("TEST 3: IHD Calculation")
    print("=" * 60)
    
    from critical_care.rrt import calculate_ihd_dosing
    
    test_cases = [
        {"weight": 70.0, "kt_v": 1.2},
        {"weight": 80.0, "kt_v": 1.5},
        {"weight": 60.0, "kt_v": 1.0},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_ihd_dosing(case["weight"], case["kt_v"])
        
        # Check key fields
        expected_v_urea = case["weight"] * 0.58
        checks = [
            (result["weight_kg"] == case["weight"], f"Weight: {result['weight_kg']} == {case['weight']}"),
            (result["target_kt_v"] == case["kt_v"], f"Kt/V: {result['target_kt_v']} == {case['kt_v']}"),
            (abs(result["v_urea_liters"] - expected_v_urea) < 0.1, f"V (urea): {result['v_urea_liters']:.2f} ≈ {expected_v_urea:.2f}"),
            (result["dialysate_flow_ml_min"] == 500, f"Dialysate flow: {result['dialysate_flow_ml_min']} == 500"),
            (result["time_hours"] > 0, f"Time: {result['time_hours']:.1f} hours > 0"),
        ]
        
        passed = all(check[0] for check in checks)
        if passed:
            print(f"✅ Test {i}: Weight {case['weight']}kg, Kt/V {case['kt_v']}")
            print(f"   V (urea): {result['v_urea_liters']:.1f} L, Time: {result['time_hours']:.1f} hours")
        else:
            print(f"❌ Test {i}: Weight {case['weight']}kg, Kt/V {case['kt_v']}")
            for check, msg in checks:
                if not check:
                    print(f"   FAILED: {msg}")
            all_passed = False
    
    return all_passed


def test_sled_calculation():
    """Test SLED dosing calculation"""
    print("\n" + "=" * 60)
    print("TEST 4: SLED Calculation")
    print("=" * 60)
    
    from critical_care.rrt import calculate_sled_dosing
    
    test_cases = [
        {"weight": 70.0, "duration": 8.0},
        {"weight": 80.0, "duration": 10.0},
        {"weight": 60.0, "duration": 6.0},
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_sled_dosing(case["weight"], case["duration"])
        
        # Check key fields
        expected_v_urea = case["weight"] * 0.58
        expected_flow_l_h = 15.0  # 250 ml/min * 60 / 1000 = 15 L/h
        checks = [
            (result["weight_kg"] == case["weight"], f"Weight: {result['weight_kg']} == {case['weight']}"),
            (result["duration_hours"] == case["duration"], f"Duration: {result['duration_hours']} == {case['duration']}"),
            (result["dialysate_flow_ml_min"] == 250, f"Dialysate flow: {result['dialysate_flow_ml_min']} == 250"),
            (abs(result["dialysate_flow_l_h"] - expected_flow_l_h) < 0.1, f"Dialysate flow L/h: {result['dialysate_flow_l_h']:.1f} ≈ {expected_flow_l_h}"),
            (result["kt_v"] > 0, f"Kt/V: {result['kt_v']:.2f} > 0"),
        ]
        
        passed = all(check[0] for check in checks)
        if passed:
            print(f"✅ Test {i}: Weight {case['weight']}kg, Duration {case['duration']}h")
            print(f"   Dialysate: {result['dialysate_flow_ml_min']} ml/min, Kt/V: {result['kt_v']:.2f}")
        else:
            print(f"❌ Test {i}: Weight {case['weight']}kg, Duration {case['duration']}h")
            for check, msg in checks:
                if not check:
                    print(f"   FAILED: {msg}")
            all_passed = False
    
    return all_passed


def test_anticoagulation_calculation():
    """Test anticoagulation calculation"""
    print("\n" + "=" * 60)
    print("TEST 5: Anticoagulation Calculation")
    print("=" * 60)
    
    from critical_care.rrt import calculate_anticoagulation_rrt
    
    test_cases = [
        {
            "weight": 70.0,
            "rrt_type": "CRRT",
            "bleeding": False,
            "expected_heparin": 525.0,  # 70 * 7.5
            "expected_citrate": 3.0
        },
        {
            "weight": 80.0,
            "rrt_type": "IHD",
            "bleeding": False,
            "expected_heparin_bolus": 4000.0,  # 80 * 50
            "expected_heparin_maintenance": 800.0  # 80 * 10
        },
        {
            "weight": 70.0,
            "rrt_type": "CRRT",
            "bleeding": True,
            "expected_anticoagulation": "No anticoagulation (bleeding risk)"
        },
    ]
    
    all_passed = True
    for i, case in enumerate(test_cases, 1):
        result = calculate_anticoagulation_rrt(
            case["weight"],
            case["rrt_type"],
            case["bleeding"]
        )
        
        if case["bleeding"]:
            # Check no anticoagulation
            checks = [
                (result["anticoagulation"] == case["expected_anticoagulation"], 
                 f"Anticoagulation: {result['anticoagulation']} == {case['expected_anticoagulation']}"),
                (result["heparin_dose"] is None, "Heparin dose is None"),
                (result["color"] == "warning", f"Color: {result['color']} == warning"),
            ]
        elif case["rrt_type"] == "CRRT":
            # Check CRRT anticoagulation
            checks = [
                (abs(result["heparin_dose_u_h"] - case["expected_heparin"]) < 1,
                 f"Heparin: {result['heparin_dose_u_h']:.0f} ≈ {case['expected_heparin']}"),
                (result["citrate_dose_mmol_l"] == case["expected_citrate"],
                 f"Citrate: {result['citrate_dose_mmol_l']} == {case['expected_citrate']}"),
            ]
        else:  # IHD or SLED
            # Check IHD/SLED anticoagulation
            checks = [
                (abs(result["heparin_bolus_u"] - case["expected_heparin_bolus"]) < 1,
                 f"Heparin bolus: {result['heparin_bolus_u']:.0f} ≈ {case['expected_heparin_bolus']}"),
                (abs(result["heparin_maintenance_u_h"] - case["expected_heparin_maintenance"]) < 1,
                 f"Heparin maintenance: {result['heparin_maintenance_u_h']:.0f} ≈ {case['expected_heparin_maintenance']}"),
            ]
        
        passed = all(check[0] for check in checks)
        if passed:
            print(f"✅ Test {i}: {case['rrt_type']}, Weight {case['weight']}kg, Bleeding: {case['bleeding']}")
            if not case["bleeding"]:
                if case["rrt_type"] == "CRRT":
                    print(f"   Heparin: {result['heparin_dose_u_h']:.0f} U/h, Citrate: {result['citrate_dose_mmol_l']:.1f} mmol/L")
                else:
                    print(f"   Heparin: {result['heparin_bolus_u']:.0f} U bolus + {result['heparin_maintenance_u_h']:.0f} U/h")
            else:
                print(f"   No anticoagulation (bleeding risk)")
        else:
            print(f"❌ Test {i}: {case['rrt_type']}, Weight {case['weight']}kg, Bleeding: {case['bleeding']}")
            for check, msg in checks:
                if not check:
                    print(f"   FAILED: {msg}")
            all_passed = False
    
    return all_passed


def test_integration():
    """Test integration with critical_care module"""
    print("\n" + "=" * 60)
    print("TEST 6: Integration Test")
    print("=" * 60)
    
    try:
        # Test that functions can be imported from critical_care module
        from critical_care import (
            calculate_crrt_dosing,
            calculate_ihd_dosing,
            calculate_sled_dosing,
            calculate_anticoagulation_rrt
        )
        
        # Test a simple calculation
        result = calculate_crrt_dosing(70.0, 25.0)
        if result and "total_flow_ml_h" in result:
            print("✅ Integration: Functions can be imported and used")
            print(f"   Sample CRRT result: {result['total_flow_ml_h']:.0f} ml/h")
            return True
        else:
            print("❌ Integration: Function returned invalid result")
            return False
            
    except Exception as e:
        print(f"❌ Integration: FAILED - {e}")
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("🧪 TEST CRITICAL CARE PHASE 4: RRT CALCULATOR")
    print("=" * 60)
    print()
    
    tests = [
        ("Imports", test_imports),
        ("CRRT Calculation", test_crrt_calculation),
        ("IHD Calculation", test_ihd_calculation),
        ("SLED Calculation", test_sled_calculation),
        ("Anticoagulation Calculation", test_anticoagulation_calculation),
        ("Integration", test_integration),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name}: EXCEPTION - {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print("\n" + "=" * 60)
    print(f"Results: {passed}/{total} tests passed ({passed*100//total}%)")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 All tests passed! Phase 4 RRT Calculator is working correctly.")
        return 0
    else:
        print(f"\n⚠️ {total - passed} test(s) failed. Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

