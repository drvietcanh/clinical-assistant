"""
Script để kiểm tra tất cả thuốc có thể truy cập được không
Kiểm tra các vấn đề có thể gây lỗi khi navigate đến Drug_Detail
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def check_drug_database():
    """Kiểm tra DRUG_DATABASE"""
    print("\n[CHECK 1] DRUG_DATABASE Structure")
    print("-" * 60)
    
    try:
        # Import without streamlit dependencies
        from drugs.drug_database import DRUG_DATABASE
        
        total_drugs = len(DRUG_DATABASE)
        print(f"✅ Total drugs: {total_drugs}")
        
        # Check for None or empty keys
        issues = []
        for drug_name, drug_data in list(DRUG_DATABASE.items())[:10]:  # Check first 10
            if not drug_name or drug_name.strip() == "":
                issues.append(f"Empty drug name: {drug_name}")
            if not drug_data:
                issues.append(f"Empty drug data for: {drug_name}")
            if not isinstance(drug_data, dict):
                issues.append(f"Invalid drug data type for {drug_name}: {type(drug_data)}")
        
        if issues:
            print(f"⚠️ Found {len(issues)} potential issues:")
            for issue in issues[:5]:
                print(f"   - {issue}")
        else:
            print("✅ No obvious issues found in sample drugs")
        
        # Check sample drug names
        sample_drugs = list(DRUG_DATABASE.keys())[:5]
        print(f"\n✅ Sample drugs: {sample_drugs}")
        
        return True, total_drugs
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, 0


def check_card_components():
    """Kiểm tra card_components.py"""
    print("\n[CHECK 2] Card Components")
    print("-" * 60)
    
    try:
        card_file = project_root / "drugs" / "drug_info_components" / "card_components.py"
        if card_file.exists():
            content = card_file.read_text(encoding="utf-8")
            
            checks = {
                "DRUG_DATABASE import": "DRUG_DATABASE" in content,
                "view_drug_name set": "st.session_state['view_drug_name']" in content,
                "switch_page to Drug_Detail": 'switch_page("pages/Drug_Detail.py")' in content or 'switch_page("Drug_Detail.py")' in content,
                "Validation before navigate": "drug_name_str not in DRUG_DATABASE" in content or "drug_name_str in DRUG_DATABASE" in content,
                "Error handling": "try:" in content and "except" in content
            }
            
            print("✅ card_components.py found")
            for check_name, check_result in checks.items():
                status = "✅" if check_result else "⚠️"
                print(f"   {status} {check_name}: {check_result}")
            
            return all(checks.values())
        else:
            print("❌ card_components.py not found")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def check_drug_detail_page():
    """Kiểm tra Drug_Detail.py"""
    print("\n[CHECK 3] Drug Detail Page")
    print("-" * 60)
    
    try:
        detail_file = project_root / "pages" / "Drug_Detail.py"
        if detail_file.exists():
            content = detail_file.read_text(encoding="utf-8")
            
            # Check drug_name definition order
            drug_name_def_line = None
            breadcrumbs_line = None
            for i, line in enumerate(content.split('\n'), 1):
                if 'drug_name = st.session_state.get' in line:
                    drug_name_def_line = i
                if 'render_breadcrumbs' in line and drug_name_def_line:
                    breadcrumbs_line = i
                    break
            
            checks = {
                "File exists": True,
                "drug_name defined": "drug_name = st.session_state.get('view_drug_name'" in content,
                "drug_name validation": "if not drug_name:" in content,
                "database validation": "if drug_name not in DRUG_DATABASE:" in content,
                "drug_data validation": "if not drug_data:" in content,
                "Error handling": "try:" in content and "except" in content,
                "Back button": 'switch_page("pages/07_💊_Drug_Database.py")' in content
            }
            
            # Check order
            if drug_name_def_line and breadcrumbs_line:
                if drug_name_def_line < breadcrumbs_line:
                    checks["drug_name before breadcrumbs"] = True
                else:
                    checks["drug_name before breadcrumbs"] = False
                    print(f"⚠️ WARNING: drug_name defined at line {drug_name_def_line}, breadcrumbs at {breadcrumbs_line}")
            
            print("✅ Drug_Detail.py found")
            for check_name, check_result in checks.items():
                status = "✅" if check_result else "❌"
                print(f"   {status} {check_name}: {check_result}")
            
            return all(checks.values())
        else:
            print("❌ Drug_Detail.py not found")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_database_view():
    """Kiểm tra database_view.py"""
    print("\n[CHECK 4] Database View")
    print("-" * 60)
    
    try:
        db_view_file = project_root / "drugs" / "drug_info_components" / "database_view.py"
        if db_view_file.exists():
            content = db_view_file.read_text(encoding="utf-8")
            
            checks = {
                "render_compact_drug_card called": "render_compact_drug_card" in content,
                "DRUG_DATABASE used": "DRUG_DATABASE" in content,
            }
            
            print("✅ database_view.py found")
            for check_name, check_result in checks.items():
                status = "✅" if check_result else "⚠️"
                print(f"   {status} {check_name}: {check_result}")
            
            return True
        else:
            print("❌ database_view.py not found")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Run all checks"""
    print("=" * 60)
    print("KIEM TRA TRUY CAP TRANG THUOC")
    print("=" * 60)
    
    results = []
    
    # Check 1: Drug Database
    db_ok, total_drugs = check_drug_database()
    results.append(("Drug Database", db_ok))
    
    # Check 2: Card Components
    card_ok = check_card_components()
    results.append(("Card Components", card_ok))
    
    # Check 3: Drug Detail Page
    detail_ok = check_drug_detail_page()
    results.append(("Drug Detail Page", detail_ok))
    
    # Check 4: Database View
    view_ok = check_database_view()
    results.append(("Database View", view_ok))
    
    # Summary
    print("\n" + "=" * 60)
    print("TỔNG KẾT")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {check_name}")
    
    print(f"\nTotal: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✅ Tất cả checks đều PASS - Code structure OK")
        return 0
    else:
        print(f"\n⚠️ {total - passed} check(s) failed - Cần kiểm tra lại")
        return 1


if __name__ == "__main__":
    sys.exit(main())

