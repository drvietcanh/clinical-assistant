"""
Test script để kiểm tra các calculator vừa thêm Phase 1
"""

import sys
import traceback
from pathlib import Path

# List các calculator vừa thêm Phase 1
CALCULATORS_TO_TEST = [
    ("scores.surgery.koivuranta_ponv", "koivuranta_ponv"),
    ("scores.surgery.gupta_cardiac", "gupta_cardiac"),
    ("scores.surgery.padss", "padss"),
    ("scores.surgery.riker_sas", "riker_sas"),
    ("scores.surgery.wilson_risk", "wilson_risk"),
    ("scores.surgery.sort", "sort"),
    ("scores.surgery.surgical_apgar", "surgical_apgar"),
    ("scores.metabolism.hba1c_eag", "hba1c_eag"),
]

def test_import(module_path, calculator_name):
    """Test import module"""
    try:
        module = __import__(module_path, fromlist=[''])
        return True, None
    except Exception as e:
        return False, str(e)

def test_phase1_imports(module_path, calculator_name):
    """Test Phase 1 imports có trong file không"""
    try:
        # Convert module path to file path
        file_path = module_path.replace('.', '/') + '.py'
        file_path = Path(file_path)
        
        if not file_path.exists():
            return False, f"File không tồn tại: {file_path}"
        
        content = file_path.read_text(encoding='utf-8')
        
        # Check Phase 1 imports
        checks = {
            "PHASE 1 IMPORTS comment": "# ========== PHASE 1 IMPORTS ==========" in content,
            "get_references": "from scores.references_config import get_references" in content,
            "render_references_section": "from components.references import render_references_section" in content,
            "save_calculation_to_history": "from components.calculation_history import save_calculation_to_history" in content,
            "render_history_ui": "render_history_ui" in content and ("from components.calculation_history import" in content or "import render_history_ui" in content),
            "load_shared_result_from_url": "load_shared_result_from_url" in content and ("from components.share_results import" in content),
            "render_share_section": "render_share_section" in content and ("from components.share_results import" in content),
            "render_suggestions": "from components.smart_suggestions import render_suggestions" in content,
            "render_export_section": "from components.export import render_export_section" in content,
        }
        
        missing = [key for key, value in checks.items() if not value]
        
        if missing:
            return False, f"Thiếu: {', '.join(missing)}"
        
        return True, "Tất cả Phase 1 imports đều có"
        
    except Exception as e:
        return False, f"Lỗi đọc file: {str(e)}"

def test_render_function(module_path, calculator_name):
    """Test render function có tồn tại không"""
    try:
        module = __import__(module_path, fromlist=[''])
        
        if not hasattr(module, 'render'):
            return False, "Không có hàm render()"
        
        render_func = getattr(module, 'render')
        if not callable(render_func):
            return False, "render không phải là function"
        
        return True, "Hàm render() tồn tại"
        
    except Exception as e:
        return False, f"Lỗi kiểm tra render: {str(e)}"

def test_phase1_features(module_path, calculator_name):
    """Test Phase 1 features có trong code không"""
    try:
        file_path = module_path.replace('.', '/') + '.py'
        file_path = Path(file_path)
        
        if not file_path.exists():
            return False, f"File không tồn tại: {file_path}"
        
        content = file_path.read_text(encoding='utf-8')
        
        checks = {
            "load_shared_result_from_url call": "load_shared_result_from_url()" in content,
            "save_calculation_to_history call": "save_calculation_to_history(" in content,
            "render_share_section call": "render_share_section(" in content,
            "render_history_ui call": "render_history_ui(" in content,
            "render_export_section call": "render_export_section(" in content,
            "render_suggestions call": "render_suggestions(" in content,
            "render_references_section call": "render_references_section(" in content,
        }
        
        missing = [key for key, value in checks.items() if not value]
        
        if missing:
            return False, f"Thiếu features: {', '.join(missing)}"
        
        return True, "Tất cả Phase 1 features đều có"
        
    except Exception as e:
        return False, f"Lỗi kiểm tra features: {str(e)}"

def main():
    """Main test function"""
    print("="*70)
    print("🧪 TEST CÁC CALCULATOR VỪA THÊM PHASE 1")
    print("="*70)
    print()
    
    results = []
    
    for module_path, calculator_name in CALCULATORS_TO_TEST:
        print(f"📋 Testing: {calculator_name}")
        print("-" * 70)
        
        # Test 1: Import
        print("1️⃣ Test import...", end=" ")
        import_ok, import_msg = test_import(module_path, calculator_name)
        if import_ok:
            print("✅ PASSED")
        else:
            print(f"❌ FAILED: {import_msg}")
        results.append(("import", calculator_name, import_ok, import_msg))
        
        # Test 2: Phase 1 imports
        print("2️⃣ Test Phase 1 imports...", end=" ")
        imports_ok, imports_msg = test_phase1_imports(module_path, calculator_name)
        if imports_ok:
            print("✅ PASSED")
        else:
            print(f"❌ FAILED: {imports_msg}")
        results.append(("imports", calculator_name, imports_ok, imports_msg))
        
        # Test 3: Render function
        print("3️⃣ Test render function...", end=" ")
        render_ok, render_msg = test_render_function(module_path, calculator_name)
        if render_ok:
            print("✅ PASSED")
        else:
            print(f"❌ FAILED: {render_msg}")
        results.append(("render", calculator_name, render_ok, render_msg))
        
        # Test 4: Phase 1 features
        print("4️⃣ Test Phase 1 features...", end=" ")
        features_ok, features_msg = test_phase1_features(module_path, calculator_name)
        if features_ok:
            print("✅ PASSED")
        else:
            print(f"❌ FAILED: {features_msg}")
        results.append(("features", calculator_name, features_ok, features_msg))
        
        print()
    
    # Summary
    print("="*70)
    print("📊 TỔNG KẾT")
    print("="*70)
    
    total_tests = len(results)
    passed_tests = sum(1 for _, _, ok, _ in results if ok)
    failed_tests = total_tests - passed_tests
    
    print(f"Tổng số test: {total_tests}")
    print(f"✅ PASSED: {passed_tests}")
    print(f"❌ FAILED: {failed_tests}")
    print(f"📈 Tỷ lệ thành công: {passed_tests/total_tests*100:.1f}%")
    print()
    
    # Failed tests details
    failed = [(test_type, name, msg) for test_type, name, ok, msg in results if not ok]
    if failed:
        print("❌ CHI TIẾT CÁC TEST FAILED:")
        print("-" * 70)
        for test_type, name, msg in failed:
            print(f"  - {name} ({test_type}): {msg}")
        print()
    
    # Group by calculator
    print("📋 KẾT QUẢ THEO CALCULATOR:")
    print("-" * 70)
    for module_path, calculator_name in CALCULATORS_TO_TEST:
        calc_results = [r for r in results if r[1] == calculator_name]
        all_passed = all(ok for _, _, ok, _ in calc_results)
        status = "✅ PASSED" if all_passed else "❌ FAILED"
        print(f"  {calculator_name}: {status}")
    
    print()
    print("="*70)
    
    return failed_tests == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
