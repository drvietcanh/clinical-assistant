"""
Script kiểm tra tất cả các calculator đã có đủ Phase 1 chưa
"""

import os
from pathlib import Path

# Phase 1 imports cần có
REQUIRED_IMPORTS = [
    "from scores.references_config import get_references",
    "from components.references import render_references_section",
    "from components.calculation_history import",
    "from components.share_results import",
    "from components.smart_suggestions import render_suggestions",
    "from components.export import render_export_section"
]

# Phase 1 features cần sử dụng
REQUIRED_FEATURES = [
    "load_shared_result_from_url()",
    "save_calculation_to_history(",
    "render_share_section(",
    "render_history_ui(",
    "render_export_section(",
    "render_suggestions(",
    "render_references_section("
]

def check_phase1_imports(content):
    """Kiểm tra Phase 1 imports"""
    missing = []
    has_phase1_section = "# ========== PHASE 1 IMPORTS ==========" in content
    
    if not has_phase1_section:
        return False, ["Không có PHASE 1 IMPORTS section"]
    
    for imp in REQUIRED_IMPORTS:
        if imp not in content:
            missing.append(imp)
    
    return len(missing) == 0, missing

def check_phase1_features(content):
    """Kiểm tra Phase 1 features được sử dụng"""
    missing = []
    
    for feature in REQUIRED_FEATURES:
        if feature not in content:
            missing.append(feature)
    
    return len(missing) == 0, missing

def check_calculator(file_path):
    """Kiểm tra một calculator file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra có hàm render không
        has_render = "def render(" in content
        
        if not has_render:
            return None, "Không có hàm render()"
        
        # Kiểm tra Phase 1 imports
        imports_ok, missing_imports = check_phase1_imports(content)
        
        # Kiểm tra Phase 1 features
        features_ok, missing_features = check_phase1_features(content)
        
        return {
            "file": str(file_path),
            "has_render": has_render,
            "imports_ok": imports_ok,
            "missing_imports": missing_imports,
            "features_ok": features_ok,
            "missing_features": missing_features,
            "complete": imports_ok and features_ok
        }
    except Exception as e:
        return None, str(e)

def main():
    """Main function"""
    scores_dir = Path("scores")
    
    if not scores_dir.exists():
        print("❌ Không tìm thấy thư mục scores/")
        return
    
    # Tìm tất cả các calculator files
    calculator_files = []
    for py_file in scores_dir.rglob("*.py"):
        # Bỏ qua các file helper, ui, config
        if any(skip in py_file.name for skip in ["__", "_ui_", "_helpers", "_calculators", "config"]):
            continue
        calculator_files.append(py_file)
    
    print("="*80)
    print("🔍 KIỂM TRA PHASE 1 CHO TẤT CẢ CÁC CALCULATOR")
    print("="*80)
    print(f"\n📋 Tổng số calculator files: {len(calculator_files)}\n")
    
    results = []
    complete_count = 0
    incomplete_count = 0
    no_render_count = 0
    
    for calc_file in sorted(calculator_files):
        result = check_calculator(calc_file)
        if result is None:
            continue
        
        if isinstance(result, dict):
            results.append(result)
            if result["complete"]:
                complete_count += 1
            else:
                incomplete_count += 1
        else:
            no_render_count += 1
    
    # In kết quả
    print("="*80)
    print("📊 TỔNG KẾT")
    print("="*80)
    print(f"✅ Hoàn chỉnh Phase 1: {complete_count}")
    print(f"⚠️  Chưa hoàn chỉnh: {incomplete_count}")
    print(f"❌ Không có render(): {no_render_count}")
    print(f"📈 Tỷ lệ hoàn chỉnh: {complete_count/(complete_count+incomplete_count)*100:.1f}%" if (complete_count+incomplete_count) > 0 else "N/A")
    print()
    
    # Chi tiết các calculator chưa hoàn chỉnh
    incomplete = [r for r in results if not r["complete"]]
    if incomplete:
        print("="*80)
        print("⚠️  CÁC CALCULATOR CHƯA HOÀN CHỈNH PHASE 1")
        print("="*80)
        for r in incomplete:
            print(f"\n📄 {r['file']}")
            if not r["imports_ok"]:
                print("  ❌ Thiếu imports:")
                for imp in r["missing_imports"]:
                    print(f"     - {imp}")
            if not r["features_ok"]:
                print("  ❌ Thiếu features:")
                for feat in r["missing_features"]:
                    print(f"     - {feat}")
    
    # Chi tiết các calculator đã hoàn chỉnh (sample)
    complete = [r for r in results if r["complete"]]
    if complete:
        print("\n" + "="*80)
        print(f"✅ CÁC CALCULATOR ĐÃ HOÀN CHỈNH PHASE 1 ({len(complete)} files)")
        print("="*80)
        # Chỉ hiển thị 10 file đầu
        for r in complete[:10]:
            print(f"  ✓ {Path(r['file']).name}")
        if len(complete) > 10:
            print(f"  ... và {len(complete) - 10} calculator khác")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    main()

