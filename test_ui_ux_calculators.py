"""
Script để test tất cả các calculators đã cải thiện UI/UX
Kiểm tra imports, syntax, và sử dụng components đúng cách
"""

import os
import ast
import sys
from pathlib import Path

# Danh sách các calculators đã cải thiện UI/UX (từ TIEN_TRINH_VALIDATION_VA_UI_UX.md)
CALCULATORS = {
    # Emergency & Critical Care
    "scores/emergency/apache2.py": ["render_score_result", "render_score_breakdown"],
    "scores/emergency/apache3.py": ["render_score_result", "render_score_breakdown"],
    "scores/emergency/saps2.py": ["render_score_result"],
    "scores/emergency/saps3.py": ["render_result_box"],
    "scores/emergency/sofa.py": ["render_score_result", "render_score_breakdown"],
    "scores/emergency/mods.py": ["render_score_result", "render_score_breakdown"],
    "scores/emergency/lods.py": ["render_result_box"],
    "scores/emergency/news2.py": ["render_score_result"],
    "scores/emergency/mews.py": ["render_score_result"],
    "scores/emergency/qsofa.py": ["render_score_result"],
    
    # Cardiology
    "scores/cardiology/grace.py": ["render_score_result"],
    "scores/cardiology/ascvd.py": ["render_result_box"],
    "scores/cardiology/qtc.py": ["render_result_box"],
    "scores/cardiology/framingham.py": ["render_result_box"],
    "scores/cardiology/heart.py": ["render_score_result"],
    
    # Respiratory
    "scores/respiratory/curb65.py": ["render_score_result"],
    "scores/respiratory/wells_pe.py": ["render_score_result"],
    "scores/respiratory/pesi.py": ["render_score_result"],
    "scores/respiratory/psi_port.py": ["render_score_result"],
    
    # GI
    "scores/gi/meld.py": ["render_score_result"],
    "scores/gi/child_pugh.py": ["render_score_result"],
    "scores/gi/glasgow_blatchford.py": ["render_score_result"],
    "scores/gi/aims65.py": ["render_score_result", "render_score_breakdown"],
    "scores/gi/bisap.py": ["render_score_result", "render_score_breakdown"],
    "scores/gi/rockall.py": ["render_score_result"],
    
    # Metabolism
    "scores/metabolism/bmi_ibw_bsa.py": ["render_result_card"],
    "scores/metabolism/corrected_calcium.py": ["render_result_box"],
    "scores/metabolism/anion_gap.py": ["render_result_box"],
    "scores/metabolism/winter_formula.py": ["render_result_box"],
    "scores/metabolism/osmolality.py": ["render_result_box"],
    "scores/metabolism/crcl.py": ["render_result_box"],
    
    # Neurology
    "scores/neurology/gcs.py": ["render_score_result", "render_score_breakdown"],
    "scores/neurology/four_score.py": ["render_score_result", "render_score_breakdown"],
    "scores/neurology/ich_score.py": ["render_score_result"],
    
    # Trauma
    "scores/trauma/rts.py": ["render_score_result", "render_score_breakdown"],
    "scores/trauma/iss.py": ["render_score_result", "render_score_breakdown"],
    "scores/trauma/triss.py": ["render_result_box"],
    
    # Pediatrics
    "scores/pediatrics/pews.py": ["render_score_result"],
    "scores/pediatrics/pediatric_gcs.py": ["render_score_result"],
    "scores/pediatrics/pim2.py": ["render_score_result"],
    
    # Hematology
    "scores/hematology/dic_score.py": ["render_score_result", "render_score_breakdown"],
    "scores/hematology/four_ts.py": ["render_score_result", "render_score_breakdown"],
    "scores/hematology/wells_dvt.py": ["render_score_result"],
    
    # Infectious
    "scores/infectious/mascc.py": ["render_score_result", "render_score_breakdown"],
    "scores/infectious/pitt_bacteremia.py": ["render_score_result", "render_score_breakdown"],
}

def check_file(filepath, expected_components):
    """Kiểm tra một file calculator"""
    results = {
        "file": filepath,
        "exists": False,
        "syntax_ok": False,
        "imports_ok": False,
        "components_used": False,
        "errors": []
    }
    
    if not os.path.exists(filepath):
        results["errors"].append(f"File không tồn tại: {filepath}")
        return results
    
    results["exists"] = True
    
    # Kiểm tra syntax
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        results["syntax_ok"] = True
    except SyntaxError as e:
        results["errors"].append(f"Syntax error: {e}")
        return results
    except Exception as e:
        results["errors"].append(f"Error reading file: {e}")
        return results
    
    # Kiểm tra imports - tìm trong toàn bộ code
    imports_found = []
    components_found = []
    
    # Kiểm tra imports - tìm tất cả các dòng có "from components.ui" và "import"
    import re
    # Pattern để tìm import statements (có thể nhiều dòng)
    import_blocks = re.findall(r'from\s+components\.ui\.\w+\s+import\s+\(?([^)]+)\)?', code, re.DOTALL)
    
    for block in import_blocks:
        # Parse các components được import
        imported = block.strip()
        # Xử lý multi-line imports - loại bỏ newlines và normalize
        imported = re.sub(r'\s+', ' ', imported)
        imported = imported.replace(',', ' ')
        # Tách các components
        imported_list = [item.strip() for item in imported.split() if item.strip()]
        for comp in expected_components:
            if comp in imported_list or comp in imported:
                imports_found.append(comp)
    
    # Nếu không tìm thấy qua pattern, thử tìm trực tiếp trong code
    if len(imports_found) < len(expected_components):
        for comp in expected_components:
            # Tìm import statement có chứa component name
            if re.search(rf'from\s+components\.ui\.\w+\s+import[^)]*{comp}', code, re.MULTILINE | re.DOTALL):
                if comp not in imports_found:
                    imports_found.append(comp)
    
    # Kiểm tra sử dụng components trong code
    for comp in expected_components:
        if f'{comp}(' in code:
            components_found.append(comp)
    
    # Kiểm tra tất cả components được import
    missing_imports = set(expected_components) - set(imports_found)
    if missing_imports:
        results["errors"].append(f"Thiếu imports: {missing_imports}")
    else:
        results["imports_ok"] = True
    
    # Kiểm tra components được sử dụng
    missing_usage = set(expected_components) - set(components_found)
    if missing_usage:
        results["errors"].append(f"Components không được sử dụng: {missing_usage}")
    else:
        results["components_used"] = True
    
    return results

def main():
    """Main function"""
    print("=" * 80)
    print("KIỂM TRA TẤT CẢ CALCULATORS ĐÃ CẢI THIỆN UI/UX")
    print("=" * 80)
    print()
    
    base_dir = Path(__file__).parent
    total = len(CALCULATORS)
    passed = 0
    failed = 0
    results_list = []
    
    for filepath, expected_components in CALCULATORS.items():
        full_path = base_dir / filepath
        print(f"Đang kiểm tra: {filepath}...", end=" ")
        
        result = check_file(str(full_path), expected_components)
        results_list.append(result)
        
        if result["exists"] and result["syntax_ok"] and result["imports_ok"] and result["components_used"]:
            print("✅ PASS")
            passed += 1
        else:
            print("❌ FAIL")
            failed += 1
            if result["errors"]:
                for error in result["errors"]:
                    print(f"    ⚠️  {error}")
    
    print()
    print("=" * 80)
    print("TỔNG KẾT")
    print("=" * 80)
    print(f"Tổng số calculators: {total}")
    print(f"✅ Pass: {passed}")
    print(f"❌ Fail: {failed}")
    print(f"Tỷ lệ thành công: {passed/total*100:.1f}%")
    print()
    
    # Chi tiết các file fail
    if failed > 0:
        print("=" * 80)
        print("CHI TIẾT CÁC FILE FAIL:")
        print("=" * 80)
        for result in results_list:
            if not (result["exists"] and result["syntax_ok"] and result["imports_ok"] and result["components_used"]):
                print(f"\n📄 {result['file']}:")
                for error in result["errors"]:
                    print(f"   ❌ {error}")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

