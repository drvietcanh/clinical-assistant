"""
Test script để kiểm tra các calculator đã thêm Phase 1 trong session này
"""

import sys
import importlib
from pathlib import Path

# Danh sách các calculator đã thêm Phase 1 trong session này
PHASE1_NEW_CALCULATORS = [
    # Pediatrics
    ("scores.pediatrics.pim2", "PIM2"),
    ("scores.pediatrics.pelod2", "PELOD-2"),
    ("scores.pediatrics.prism3", "PRISM3"),
    
    # Nephrology
    ("scores.nephrology.rifle", "RIFLE"),
    ("scores.nephrology.kdigo", "KDIGO"),
    ("scores.nephrology.akin", "AKIN"),
    
    # Hematology
    ("scores.hematology.dic_score", "DIC Score"),
    
    # Surgery
    ("scores.surgery.aldrete", "Aldrete Score"),
    
    # Infectious
    ("scores.infectious.sirs", "SIRS"),
    ("scores.infectious.centor", "Centor Score"),
    
    # Pain
    ("scores.pain.vas", "VAS"),
    ("scores.pain.nrs", "NRS"),
    ("scores.pain.dn4", "DN4"),
    
    # Oncology
    ("scores.oncology.ecog", "ECOG"),
    ("scores.oncology.karnofsky", "Karnofsky"),
    
    # Nursing
    ("scores.nursing.braden", "Braden Scale"),
    ("scores.nursing.morse", "Morse Fall Scale"),
    
    # Rheumatology
    ("scores.rheumatology.das28", "DAS28"),
    ("scores.rheumatology.sledai", "SLEDAI"),
    ("scores.rheumatology.gout", "Gout Classification"),
    
    # Respiratory
    ("scores.respiratory.bode", "BODE Index"),
    ("scores.respiratory.smartcop", "SMART-COP"),
    ("scores.respiratory.ards_berlin", "ARDS Berlin Definition"),
]

def check_phase1_imports(module_path):
    """Kiểm tra xem module có Phase 1 imports không"""
    try:
        module = importlib.import_module(module_path)
        source_code = Path(module.__file__).read_text(encoding='utf-8')
        
        checks = {
            "references_config": "from scores.references_config import get_references" in source_code,
            "references_component": "from components.references import render_references_section" in source_code,
            "calculation_history": "from components.calculation_history import" in source_code,
            "share_results": "from components.share_results import" in source_code,
            "smart_suggestions": "from components.smart_suggestions import render_suggestions" in source_code,
        }
        
        return checks
    except Exception as e:
        return {"error": str(e)}

def check_phase1_features(module_path):
    """Kiểm tra xem module có Phase 1 features không"""
    try:
        module = importlib.import_module(module_path)
        source_code = Path(module.__file__).read_text(encoding='utf-8')
        
        checks = {
            "load_shared_result": "load_shared_result_from_url" in source_code,
            "render_suggestions": "render_suggestions(" in source_code,
            "save_calculation": "save_calculation_to_history(" in source_code,
            "render_share_section": "render_share_section(" in source_code,
            "render_export_section": "render_export_section(" in source_code,
            "render_history_ui": "render_history_ui(" in source_code,
            "render_references_section": "render_references_section(" in source_code,
        }
        
        return checks
    except Exception as e:
        return {"error": str(e)}

def test_calculator(module_path, calculator_name):
    """Test một calculator"""
    print(f"\n{'='*70}")
    print(f"Testing: {calculator_name} ({module_path})")
    print('='*70)
    
    # Check imports
    import_checks = check_phase1_imports(module_path)
    if "error" in import_checks:
        print(f"❌ ERROR: {import_checks['error']}")
        return False
    
    print("\n📦 Phase 1 Imports:")
    all_imports_ok = True
    for check_name, passed in import_checks.items():
        status = "✅" if passed else "❌"
        print(f"   {status} {check_name}")
        if not passed:
            all_imports_ok = False
    
    # Check features
    feature_checks = check_phase1_features(module_path)
    if "error" in feature_checks:
        print(f"❌ ERROR: {feature_checks['error']}")
        return False
    
    print("\n🔧 Phase 1 Features:")
    all_features_ok = True
    for check_name, passed in feature_checks.items():
        status = "✅" if passed else "❌"
        print(f"   {status} {check_name}")
        if not passed:
            all_features_ok = False
    
    # Overall status
    if all_imports_ok and all_features_ok:
        print(f"\n✅ {calculator_name}: PASSED")
        return True
    else:
        print(f"\n❌ {calculator_name}: FAILED")
        return False

def main():
    """Main test function"""
    print("="*70)
    print("🧪 TEST PHASE 1 NEW CALCULATORS")
    print("="*70)
    print(f"\nTesting {len(PHASE1_NEW_CALCULATORS)} calculators...")
    
    results = []
    for module_path, calculator_name in PHASE1_NEW_CALCULATORS:
        passed = test_calculator(module_path, calculator_name)
        results.append((calculator_name, passed))
    
    # Summary
    print("\n" + "="*70)
    print("📊 TEST SUMMARY")
    print("="*70)
    
    passed_count = sum(1 for _, passed in results if passed)
    failed_count = len(results) - passed_count
    
    print(f"\n✅ Passed: {passed_count}/{len(results)}")
    print(f"❌ Failed: {failed_count}/{len(results)}")
    
    if failed_count > 0:
        print("\n❌ Failed Calculators:")
        for name, passed in results:
            if not passed:
                print(f"   - {name}")
    
    print("\n" + "="*70)
    if failed_count == 0:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("⚠️  SOME TESTS FAILED")
    print("="*70)
    
    return failed_count == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

