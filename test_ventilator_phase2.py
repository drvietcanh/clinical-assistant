"""
Test Script for Ventilator PHIÊN 2
Kiểm tra các chức năng tư vấn thông minh & cảnh báo
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
        from ventilator.abg_advisor import (
            analyze_abg_for_ventilator,
            recommend_ventilator_adjustments,
            display_abg_recommendations,
            display_ventilator_adjustments
        )
        print("✅ ABG Advisor imports: OK")
    except Exception as e:
        print(f"❌ ABG Advisor imports: FAILED - {e}")
        return False
    
    try:
        from ventilator.alerts import (
            check_ventilator_alerts,
            display_alerts,
            get_alert_summary
        )
        print("✅ Alerts imports: OK")
    except Exception as e:
        print(f"❌ Alerts imports: FAILED - {e}")
        return False
    
    try:
        from ventilator.protocols import (
            get_ardsnet_recommendations,
            get_sepsis_guidelines_recommendations,
            display_protocol_recommendations
        )
        print("✅ Protocols imports: OK")
    except Exception as e:
        print(f"❌ Protocols imports: FAILED - {e}")
        return False
    
    return True


def test_abg_advisor():
    """Test ABG advisor"""
    print("\n" + "=" * 60)
    print("TEST 2: ABG Advisor")
    print("=" * 60)
    
    from ventilator.abg_advisor import analyze_abg_for_ventilator
    
    test_cases = [
        {
            "name": "Respiratory Acidosis",
            "abg": {"ph": 7.20, "pco2": 50, "hco3": 24, "po2": 80, "fio2": 50, "sao2": 95},
            "expected": "Toan Hô Hấp"
        },
        {
            "name": "Metabolic Acidosis",
            "abg": {"ph": 7.25, "pco2": 40, "hco3": 18, "po2": 100, "fio2": 40, "sao2": 98},
            "expected": "Toan Chuyển Hóa"
        },
        {
            "name": "Respiratory Alkalosis",
            "abg": {"ph": 7.50, "pco2": 30, "hco3": 24, "po2": 100, "fio2": 40, "sao2": 98},
            "expected": "Kiềm Hô Hấp"
        },
        {
            "name": "Normal",
            "abg": {"ph": 7.40, "pco2": 40, "hco3": 24, "po2": 95, "fio2": 21, "sao2": 98},
            "expected": None
        }
    ]
    
    all_passed = True
    for case in test_cases:
        recommendations = analyze_abg_for_ventilator(case["abg"])
        if case["expected"] is None:
            if len(recommendations) == 0:
                print(f"✅ {case['name']}: No recommendations (normal)")
            else:
                print(f"❌ {case['name']}: Expected no recommendations, got {len(recommendations)}")
                all_passed = False
        else:
            if len(recommendations) > 0 and case["expected"] in recommendations[0]["title"]:
                print(f"✅ {case['name']}: {recommendations[0]['title']}")
            else:
                print(f"❌ {case['name']}: Expected {case['expected']}, got {recommendations}")
                all_passed = False
    
    return all_passed


def test_ventilator_adjustments():
    """Test ventilator adjustments recommendations"""
    print("\n" + "=" * 60)
    print("TEST 3: Ventilator Adjustments")
    print("=" * 60)
    
    from ventilator.abg_advisor import recommend_ventilator_adjustments
    
    # Test hypoxemia
    abg_hypoxemia = {"po2": 60, "fio2": 50, "pco2": 40, "ph": 7.40, "hco3": 24, "sao2": 90}
    vent_settings = {"peep": 10, "fio2": 50, "rr": 20, "vt": 400, "plateau": 25}
    recommendations = recommend_ventilator_adjustments(abg_hypoxemia, vent_settings, 70)
    
    has_peep_rec = any("PEEP" in rec["parameter"] for rec in recommendations)
    has_fio2_rec = any("FiO₂" in rec["parameter"] for rec in recommendations)
    
    if has_peep_rec or has_fio2_rec:
        print("✅ Hypoxemia: Recommendations generated")
    else:
        print("❌ Hypoxemia: No recommendations")
        return False
    
    # Test hypercapnia
    abg_hypercapnia = {"po2": 80, "fio2": 40, "pco2": 50, "ph": 7.30, "hco3": 24, "sao2": 95}
    recommendations = recommend_ventilator_adjustments(abg_hypercapnia, vent_settings, 70)
    
    has_rr_rec = any("RR" in rec["parameter"] for rec in recommendations)
    
    if has_rr_rec:
        print("✅ Hypercapnia: RR adjustment recommended")
    else:
        print("❌ Hypercapnia: No RR adjustment")
        return False
    
    return True


def test_alerts():
    """Test alerts system"""
    print("\n" + "=" * 60)
    print("TEST 4: Alerts System")
    print("=" * 60)
    
    from ventilator.alerts import check_ventilator_alerts, get_alert_summary
    
    # Test critical alerts
    vent_settings = {"plateau": 35, "peep": 10, "vt": 500, "rr": 20, "fio2": 60}
    abg_data = {"po2": 50, "fio2": 60, "pco2": 45, "ph": 7.10, "hco3": 20, "sao2": 85}
    calculations = {"driving_pressure": 25, "pf_ratio": 83, "compliance": 20, "vt_per_kg": 7.1}
    
    alerts = check_ventilator_alerts(vent_settings, abg_data, calculations, 70)
    summary = get_alert_summary(alerts)
    
    if summary["critical"] > 0:
        print(f"✅ Critical alerts: {summary['critical']} alerts generated")
    else:
        print("❌ Critical alerts: No critical alerts")
        return False
    
    # Test warning alerts
    vent_settings2 = {"plateau": 25, "peep": 10, "vt": 600, "rr": 20, "fio2": 50}
    abg_data2 = {"po2": 80, "fio2": 50, "pco2": 48, "ph": 7.35, "hco3": 24, "sao2": 95}
    calculations2 = {"driving_pressure": 15, "pf_ratio": 160, "compliance": 25, "vt_per_kg": 8.6}
    
    alerts2 = check_ventilator_alerts(vent_settings2, abg_data2, calculations2, 70)
    summary2 = get_alert_summary(alerts2)
    
    if summary2["warning"] > 0:
        print(f"✅ Warning alerts: {summary2['warning']} alerts generated")
    else:
        print("❌ Warning alerts: No warning alerts")
        return False
    
    return True


def test_protocols():
    """Test protocol recommendations"""
    print("\n" + "=" * 60)
    print("TEST 5: Protocol Recommendations")
    print("=" * 60)
    
    from ventilator.protocols import get_ardsnet_recommendations, get_sepsis_guidelines_recommendations
    
    # Test ARDSNet
    recommendations = get_ardsnet_recommendations(70, 150, True)
    if len(recommendations) > 0:
        print(f"✅ ARDSNet: {len(recommendations)} recommendations")
    else:
        print("❌ ARDSNet: No recommendations")
        return False
    
    # Test Sepsis guidelines
    sepsis_recs = get_sepsis_guidelines_recommendations()
    if len(sepsis_recs) > 0:
        print(f"✅ Sepsis Guidelines: {len(sepsis_recs)} recommendations")
    else:
        print("❌ Sepsis Guidelines: No recommendations")
        return False
    
    return True


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
            analyze_abg_for_ventilator,
            check_ventilator_alerts,
            display_protocol_recommendations
        )
        print("✅ Ventilator module exports OK")
    except Exception as e:
        print(f"❌ Ventilator module exports: FAILED - {e}")
        return False
    
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("KIỂM TRA CHỨC NĂNG - VENTILATOR PHIÊN 2")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("ABG Advisor", test_abg_advisor()))
    results.append(("Ventilator Adjustments", test_ventilator_adjustments()))
    results.append(("Alerts System", test_alerts()))
    results.append(("Protocols", test_protocols()))
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

