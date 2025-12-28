"""
Simple Core Functions Test
Test core calculation functions without Streamlit dependencies
"""

import sys
from pathlib import Path
import importlib.util

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def load_module(module_path):
    """Load module directly from file path."""
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_phase2():
    """Test Phase 2: Cardiovascular Drugs"""
    print("\n=== Phase 2: Cardiovascular Drugs ===")
    try:
        cv_path = Path(__file__).parent.parent / "drugs" / "cardiovascular_calculator.py"
        cv = load_module(cv_path)
        
        drugs = cv.get_drug_names()
        print(f"[OK] Get drug names: {len(drugs)} drugs")
        
        validation = cv.validate_dose_range("Noradrenaline", 0.1)
        assert validation.get("is_valid", False)
        print("[OK] Validate dose range")
        
        result = cv.calculate_complete_infusion("Noradrenaline", 0.1, 70.0, "syringe_pump_50ml")
        assert result.get("infusion_rate_ml_hour", 0) > 0
        print(f"[OK] Calculate infusion: {result['infusion_rate_ml_hour']:.2f} ml/h")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def test_phase3():
    """Test Phase 3: Enhanced Infusion"""
    print("\n=== Phase 3: Enhanced Infusion ===")
    try:
        ei_path = Path(__file__).parent.parent / "critical_care" / "enhanced_infusion.py"
        ei = load_module(ei_path)
        
        rate = ei.calculate_infusion_rate(500, 10)
        assert rate == 50.0
        print(f"[OK] Calculate rate: {rate} ml/h")
        
        time = ei.calculate_infusion_time(500, 50)
        assert time["time_hours"] == 10.0
        print(f"[OK] Calculate time: {time['time_hours']} hours")
        
        volume = ei.calculate_volume_needed(50, 10)
        assert volume == 500.0
        print(f"[OK] Calculate volume: {volume} ml")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def test_phase5_multiple():
    """Test Phase 5.1: Multiple Infusions"""
    print("\n=== Phase 5.1: Multiple Infusions ===")
    try:
        mi_path = Path(__file__).parent.parent / "critical_care" / "multiple_infusions.py"
        mi = load_module(mi_path)
        
        infusions = [
            {"rate_ml_hour": 50, "volume_ml": 500},
            {"rate_ml_hour": 30, "volume_ml": 300}
        ]
        result = mi.calculate_multiple_infusions(infusions)
        assert result["total_rate_ml_hour"] == 80.0
        print(f"[OK] Total rate: {result['total_rate_ml_hour']} ml/h")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def test_phase5_compatibility():
    """Test Phase 5.2: Compatibility"""
    print("\n=== Phase 5.2: Compatibility ===")
    try:
        comp_path = Path(__file__).parent.parent / "drugs" / "compatibility_checker.py"
        comp = load_module(comp_path)
        
        result = comp.check_compatibility("Noradrenaline", "Dopamine")
        assert "compatible" in result
        print(f"[OK] Compatibility check: {result.get('status', 'N/A')}")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def test_phase7_titration():
    """Test Phase 7.1: Titration"""
    print("\n=== Phase 7.1: Titration ===")
    try:
        tit_path = Path(__file__).parent.parent / "critical_care" / "titration_guide.py"
        tit = load_module(tit_path)
        
        result = tit.calculate_titration("Noradrenaline", 0.1, 0.15, 70.0, "syringe_pump_50ml")
        assert result["dose_change"] > 0
        print(f"[OK] Dose change: {result['dose_change']:.3f} mcg/kg/min")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def test_phase7_safety():
    """Test Phase 7.2: Safety"""
    print("\n=== Phase 7.2: Safety ===")
    try:
        safe_path = Path(__file__).parent.parent / "critical_care" / "safety_checker.py"
        safe = load_module(safe_path)
        
        result = safe.check_complete_infusion_safety("Noradrenaline", 0.1, 70.0, "syringe_pump_50ml")
        assert result.score >= 0
        print(f"[OK] Safety score: {result.score}/100")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def test_phase8_time():
    """Test Phase 8.3: Time Remaining"""
    print("\n=== Phase 8.3: Time Remaining ===")
    try:
        time_path = Path(__file__).parent.parent / "critical_care" / "time_remaining.py"
        time_mod = load_module(time_path)
        
        result = time_mod.calculate_remaining_time(500, 250, 50)
        assert result["remaining_volume_ml"] == 250.0
        assert result["remaining_time_hours"] == 5.0
        print(f"[OK] Remaining time: {result['remaining_time_formatted']}")
        return True
    except Exception as e:
        print(f"[FAIL] {str(e)}")
        return False

def main():
    """Run all tests"""
    print("="*60)
    print("CORE FUNCTIONS TEST SUITE")
    print("="*60)
    
    results = {}
    results["Phase 2"] = test_phase2()
    results["Phase 3"] = test_phase3()
    results["Phase 5.1"] = test_phase5_multiple()
    results["Phase 5.2"] = test_phase5_compatibility()
    results["Phase 7.1"] = test_phase7_titration()
    results["Phase 7.2"] = test_phase7_safety()
    results["Phase 8.3"] = test_phase8_time()
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for phase, result in results.items():
        status = "PASS" if result else "FAIL"
        print(f"{phase:15s}: {status}")
    
    print("="*60)
    print(f"Total: {passed}/{total} passed ({passed*100//total}%)")
    print("="*60)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    exit(main())

