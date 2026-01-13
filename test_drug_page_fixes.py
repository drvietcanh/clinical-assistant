"""
Test script để kiểm tra các fix đã thực hiện cho trang thuốc
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_drug_detail_page_structure():
    """Test cấu trúc _Drug_Detail.py"""
    print("\n[TEST 1] _Drug_Detail.py Structure")
    print("-" * 60)
    
    try:
        detail_file = project_root / "pages" / "_Drug_Detail.py"
        if not detail_file.exists():
            print("❌ _Drug_Detail.py not found")
            return False
        
        content = detail_file.read_text(encoding="utf-8")
        
        tests = {
            "File exists": True,
            "drug_name validation early": "drug_name = st.session_state.get('view_drug_name', None)" in content,
            "drug_name validation check": "if not drug_name:" in content,
            "database validation": "if drug_name not in DRUG_DATABASE:" in content,
            "drug_data validation": "if not drug_data:" in content,
            "No duplicate drug_data get": content.count("drug_data = DRUG_DATABASE.get(drug_name)") == 1,
            "Back button uses switch_page": 'st.switch_page("pages/07_💊_Drug_Database.py")' in content,
            "Related drugs use switch_page": 'st.switch_page("pages/_Drug_Detail.py")' in content or 'st.switch_page("pages/07_💊_Drug_Database.py")' in content,
            "Related drugs validate before navigate": "if rel_name in DRUG_DATABASE:" in content or "if alt_name in DRUG_DATABASE:" in content,
            "Swipe gesture uses location.href": "window.location.href = '/pages/07_💊_Drug_Database'" in content,
            "No window.history.back()": "window.history.back()" not in content,
            "No st.rerun() for related drugs": not ("st.rerun()" in content and ("related_same_group" in content or "related_alternative" in content))
        }
        
        passed = 0
        total = len(tests)
        
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"   {status} {test_name}: {result}")
            if result:
                passed += 1
        
        print(f"\n   Result: {passed}/{total} tests passed")
        return passed == total
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_card_components():
    """Test card_components.py"""
    print("\n[TEST 2] Card Components")
    print("-" * 60)
    
    try:
        card_file = project_root / "drugs" / "drug_info_components" / "card_components.py"
        if not card_file.exists():
            print("❌ card_components.py not found")
            return False
        
        content = card_file.read_text(encoding="utf-8")
        
        tests = {
            "File exists": True,
            "Validation before navigate": "drug_name_str not in DRUG_DATABASE" in content,
            "Error handling": "try:" in content and "except" in content,
            "Uses switch_page": 'st.switch_page("pages/_Drug_Detail.py")' in content or 'st.switch_page("pages/07_💊_Drug_Database.py")' in content,
            "Sets session_state": "st.session_state['view_drug_name']" in content
        }
        
        passed = 0
        total = len(tests)
        
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"   {status} {test_name}: {result}")
            if result:
                passed += 1
        
        print(f"\n   Result: {passed}/{total} tests passed")
        return passed == total
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_navigation_consistency():
    """Test navigation consistency"""
    print("\n[TEST 3] Navigation Consistency")
    print("-" * 60)
    
    try:
        detail_file = project_root / "pages" / "_Drug_Detail.py"
        content = detail_file.read_text(encoding="utf-8")
        
        # Check all navigation uses switch_page
        navigation_patterns = [
            'st.switch_page("pages/07_💊_Drug_Database.py")',
            'st.switch_page("pages/_Drug_Detail.py")',
            'st.switch_page("pages/00_🏠_Main_Menu.py")'
        ]
        
        # Check no problematic patterns
        problematic_patterns = [
            'window.history.back()',
            'st.rerun()'  # Should not be used for navigation to different pages
        ]
        
        tests = {
            "Uses switch_page for back navigation": 'st.switch_page("pages/07_💊_Drug_Database.py")' in content,
            "Uses switch_page for related drugs": 'st.switch_page("pages/_Drug_Detail.py")' in content or 'st.switch_page("pages/07_💊_Drug_Database.py")' in content,
            "No window.history.back()": "window.history.back()" not in content,
            "Swipe gesture uses location.href": "window.location.href = '/pages/07_💊_Drug_Database'" in content
        }
        
        passed = 0
        total = len(tests)
        
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"   {status} {test_name}: {result}")
            if result:
                passed += 1
        
        print(f"\n   Result: {passed}/{total} tests passed")
        return passed == total
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_error_handling():
    """Test error handling"""
    print("\n[TEST 4] Error Handling")
    print("-" * 60)
    
    try:
        detail_file = project_root / "pages" / "_Drug_Detail.py"
        content = detail_file.read_text(encoding="utf-8")
        
        tests = {
            "Try-except for session_state": "try:" in content and "except Exception" in content,
            "Validates drug_name early": "if not drug_name:" in content,
            "Validates drug in database": "if drug_name not in DRUG_DATABASE:" in content,
            "Validates drug_data": "if not drug_data:" in content,
            "Error messages with navigation": "Quay lại trang tra cứu thuốc" in content,
            "Related drugs validation": "if rel_name in DRUG_DATABASE:" in content or "if alt_name in DRUG_DATABASE:" in content
        }
        
        passed = 0
        total = len(tests)
        
        for test_name, result in tests.items():
            status = "✅" if result else "❌"
            print(f"   {status} {test_name}: {result}")
            if result:
                passed += 1
        
        print(f"\n   Result: {passed}/{total} tests passed")
        return passed == total
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("TEST CÁC FIX CHO TRANG THUỐC")
    print("=" * 60)
    
    results = []
    
    # Test 1: Drug Detail Page Structure
    result1 = test_drug_detail_page_structure()
    results.append(("Drug Detail Structure", result1))
    
    # Test 2: Card Components
    result2 = test_card_components()
    results.append(("Card Components", result2))
    
    # Test 3: Navigation Consistency
    result3 = test_navigation_consistency()
    results.append(("Navigation Consistency", result3))
    
    # Test 4: Error Handling
    result4 = test_error_handling()
    results.append(("Error Handling", result4))
    
    # Summary
    print("\n" + "=" * 60)
    print("TỔNG KẾT")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} test suites passed")
    
    if passed == total:
        print("\n✅ Tất cả tests đều PASS - Code structure OK")
        return 0
    else:
        print(f"\n⚠️ {total - passed} test suite(s) failed - Cần kiểm tra lại")
        return 1


if __name__ == "__main__":
    sys.exit(main())

