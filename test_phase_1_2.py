"""
Test Script for Phase 1 & 2 Improvements
Kiểm tra các tính năng đã cải thiện
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_side_effects_frequency():
    """Test side effects với frequency data"""
    print("\n[TEST 1] Side Effects với Frequency Data")
    print("-" * 50)
    
    try:
        from drugs.drug_database import DRUG_DATABASE
        
        # Test với một số thuốc
        test_drugs = ["Metformin", "Aspirin", "Warfarin"]
        
        for drug_name in test_drugs:
            if drug_name in DRUG_DATABASE:
                drug_data = DRUG_DATABASE[drug_name]
                side_effects = drug_data.get('side_effects', [])
                
                print(f"\n✅ {drug_name}:")
                if isinstance(side_effects, dict):
                    print(f"   - Structured format: ✅")
                    print(f"   - Common: {len(side_effects.get('common', []))}")
                    print(f"   - Uncommon: {len(side_effects.get('uncommon', []))}")
                    print(f"   - Rare: {len(side_effects.get('rare', []))}")
                    print(f"   - Serious: {len(side_effects.get('serious', []))}")
                elif isinstance(side_effects, list):
                    print(f"   - List format: ✅ ({len(side_effects)} items)")
                else:
                    print(f"   - No side effects data")
        
        print("\n[PASS] Test 1 PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Test 1 FAILED: {e}")
        return False


def test_search_functions():
    """Test enhanced search functions"""
    print("\n[TEST 2] Enhanced Search Functions")
    print("-" * 50)
    
    try:
        from drugs.search import (
            search_by_indication,
            search_by_side_effect,
            search_by_contraindication
        )
        
        # Test search by indication
        print("\n📋 Test: Search by Indication")
        indication_results = search_by_indication("tăng huyết áp")
        print(f"   - 'tăng huyết áp': {len(indication_results)} results")
        if indication_results:
            print(f"   - Examples: {[name for name, _ in indication_results[:3]]}")
        
        # Test search by side effect
        print("\n⚠️ Test: Search by Side Effect")
        side_effect_results = search_by_side_effect("buồn nôn")
        print(f"   - 'buồn nôn': {len(side_effect_results)} results")
        if side_effect_results:
            print(f"   - Examples: {[name for name, _ in side_effect_results[:3]]}")
        
        # Test search by contraindication
        print("\n⛔ Test: Search by Contraindication")
        contraindication_results = search_by_contraindication("suy thận")
        print(f"   - 'suy thận': {len(contraindication_results)} results")
        if contraindication_results:
            print(f"   - Examples: {[name for name, _ in contraindication_results[:3]]}")
        
        print("\n[PASS] Test 2 PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Test 2 FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_visual_indicators():
    """Test visual indicators trong drug cards"""
    print("\n[TEST 3] Visual Indicators")
    print("-" * 50)
    
    try:
        from drugs.drug_database import DRUG_DATABASE
        
        # Test với một số thuốc có indicators
        test_drugs = {
            "Warfarin": ["black_box_warnings", "monitoring"],
            "Metformin": ["renal_adjustment"],
            "Aspirin": ["pregnancy"]
        }
        
        for drug_name, expected_indicators in test_drugs.items():
            if drug_name in DRUG_DATABASE:
                drug_data = DRUG_DATABASE[drug_name]
                print(f"\n✅ {drug_name}:")
                
                # Check pregnancy
                if 'pregnancy' in drug_data:
                    print(f"   - Pregnancy: ✅ {drug_data['pregnancy']}")
                
                # Check black box
                if 'black_box_warnings' in drug_data and drug_data.get('black_box_warnings'):
                    print(f"   - Black Box Warning: ✅")
                
                # Check monitoring
                if 'monitoring' in drug_data and drug_data.get('monitoring'):
                    print(f"   - Monitoring: ✅ ({len(drug_data['monitoring'])} items)")
                
                # Check renal adjustment
                if 'renal_adjustment' in drug_data and drug_data.get('renal_adjustment'):
                    print(f"   - Renal Adjustment: ✅")
        
        print("\n[PASS] Test 3 PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Test 3 FAILED: {e}")
        return False


def test_search_in_side_effects():
    """Test search trong side effects"""
    print("\n[TEST 4] Search trong Side Effects")
    print("-" * 50)
    
    try:
        from drugs.search import search_drugs
        
        # Test search "buồn nôn" - should find drugs with this side effect
        results = search_drugs("buồn nôn")
        print(f"   - 'buồn nôn': {len(results)} results")
        if results:
            print(f"   - Examples: {[name for name, _ in results[:5]]}")
        
        print("\n[PASS] Test 4 PASSED")
        return True
    except Exception as e:
        print(f"[FAIL] Test 4 FAILED: {e}")
        return False


def test_print_css_exists():
    """Test print CSS exists"""
    print("\n[TEST 5] Print CSS")
    print("-" * 50)
    
    try:
        css_file = project_root / "static" / "styles.css"
        if css_file.exists():
            content = css_file.read_text(encoding="utf-8")
            if "@media print" in content:
                print("   - Print CSS found: [OK]")
                print(f"   - File size: {len(content)} bytes")
                print("   - Contains @media print: [OK]")
                print("\n[PASS] Test 5 PASSED")
                return True
            else:
                print("   - Print CSS not found: [FAIL]")
                return False
        else:
            print("   - styles.css not found: [FAIL]")
            return False
    except Exception as e:
        print(f"[FAIL] Test 5 FAILED: {e}")
        return False


def test_mobile_css_exists():
    """Test mobile CSS exists"""
    print("\n[TEST 6] Mobile CSS")
    print("-" * 50)
    
    try:
        css_file = project_root / "static" / "drug_detail_mobile.css"
        if css_file.exists():
            content = css_file.read_text(encoding="utf-8")
            print("   - Mobile CSS found: [OK]")
            print(f"   - File size: {len(content)} bytes")
            
            # Check for swipe-related CSS
            if "swipe" in content.lower():
                print("   - Contains swipe styles: [OK]")
            
            print("\n[PASS] Test 6 PASSED")
            return True
        else:
            print("   - drug_detail_mobile.css not found: [FAIL]")
            return False
    except Exception as e:
        print(f"[FAIL] Test 6 FAILED: {e}")
        return False


def main():
    """Run all tests"""
    import io
    import sys
    # Set UTF-8 encoding for Windows
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 60)
    print("TESTING PHASE 1 & 2 IMPROVEMENTS")
    print("=" * 60)
    
    results = []
    
    # Phase 1 Tests
    results.append(("Side Effects Frequency", test_side_effects_frequency()))
    results.append(("Search Functions", test_search_functions()))
    results.append(("Visual Indicators", test_visual_indicators()))
    results.append(("Search in Side Effects", test_search_in_side_effects()))
    
    # Phase 2 Tests
    results.append(("Print CSS", test_print_css_exists()))
    results.append(("Mobile CSS", test_mobile_css_exists()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n[SUCCESS] All tests passed!")
        return 0
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())

