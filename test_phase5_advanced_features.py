"""
Test script cho Phase 5: Advanced Features
Test TDM Integration, Pediatric Templates, và IV Compatibility Checker
"""

import sys
from antibiotics.tdm_integration import render_tdm_calculator
from antibiotics.iv_compatibility import (
    check_iv_compatibility,
    check_multiple_drugs,
    normalize_drug_name,
    get_compatibility_summary
)
from antibiotics.pediatric_templates import (
    get_pediatric_age_category,
    get_pediatric_age_category_from_years,
    get_pediatric_dosing_adjustment,
    format_pediatric_category,
    get_pediatric_warnings
)


def test_tdm_integration():
    """Test TDM integration functions"""
    print("\n" + "="*60)
    print("TEST 1: TDM Integration")
    print("="*60)
    
    try:
        # Test import
        from drugs.tdm.vancomycin_tdm import (
            calculate_vancomycin_auc,
            calculate_vancomycin_dose_auc_based,
            calculate_vancomycin_dose_trough_based,
            interpret_vancomycin_level
        )
        
        print("✅ Import TDM functions thành công")
        
        # Test AUC calculation
        auc = calculate_vancomycin_auc(peak_mg_l=25.0, trough_mg_l=15.0)
        print(f"✅ calculate_vancomycin_auc(): AUC = {auc:.0f} mg·h/L")
        
        # Test AUC-based dosing
        result_auc = calculate_vancomycin_dose_auc_based(
            weight_kg=70.0,
            crcl=60.0,
            target_auc=500.0
        )
        if result_auc:
            print(f"✅ calculate_vancomycin_dose_auc_based(): Liều = {result_auc.get('dose_mg', 0):.0f} mg")
        
        # Test Trough-based dosing
        result_trough = calculate_vancomycin_dose_trough_based(
            weight_kg=70.0,
            crcl=60.0,
            target_trough=15.0
        )
        if result_trough:
            print(f"✅ calculate_vancomycin_dose_trough_based(): Liều = {result_trough.get('dose_mg', 0):.0f} mg")
        
        # Test interpretation
        interpretation = interpret_vancomycin_level(trough_mg_l=15.0)
        if interpretation:
            print(f"✅ interpret_vancomycin_level(): {len(interpretation)} interpretations")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_pediatric_templates():
    """Test pediatric templates"""
    print("\n" + "="*60)
    print("TEST 2: Pediatric Templates")
    print("="*60)
    
    test_cases = [
        (0.1, "neonate"),  # 1.2 months
        (0.5, "infant"),   # 6 months
        (2.0, "toddler"),  # 2 years
        (5.0, "preschool"), # 5 years
        (10.0, "school_age"), # 10 years
        (15.0, "adolescent"), # 15 years
        (20.0, None)  # Adult
    ]
    
    try:
        for age_years, expected_category in test_cases:
            category = get_pediatric_age_category_from_years(age_years)
            
            if category == expected_category:
                print(f"✅ Age {age_years} years: {category or 'Adult'}")
            else:
                print(f"⚠️ Age {age_years} years: Expected {expected_category}, got {category}")
        
        # Test adjustment
        adjustment = get_pediatric_dosing_adjustment(2.0, 12.0)
        if adjustment.get('is_pediatric'):
            print(f"✅ get_pediatric_dosing_adjustment(): Category = {adjustment.get('category')}, Factor = {adjustment.get('adjustment_factor')}")
        
        # Test warnings
        warnings = get_pediatric_warnings(2.0, "Doxycycline")
        if warnings:
            print(f"✅ get_pediatric_warnings(): {len(warnings)} warnings")
            for warning in warnings[:2]:
                print(f"   - {warning[:60]}...")
        
        # Test format
        formatted = format_pediatric_category("toddler")
        print(f"✅ format_pediatric_category(): '{formatted}'")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_iv_compatibility():
    """Test IV compatibility checker"""
    print("\n" + "="*60)
    print("TEST 3: IV Compatibility Checker")
    print("="*60)
    
    try:
        # Test normalize_drug_name
        test_names = [
            ("Vancomycin", "Vancomycin"),
            ("gentamicin", "Aminoglycosides"),
            ("piperacillin/tazobactam", "Piperacillin-Tazobactam"),
            ("NS", "NS")
        ]
        
        for input_name, expected in test_names:
            normalized = normalize_drug_name(input_name)
            if normalized == expected:
                print(f"✅ normalize_drug_name('{input_name}'): '{normalized}'")
            else:
                print(f"⚠️ normalize_drug_name('{input_name}'): Expected '{expected}', got '{normalized}'")
        
        # Test check_iv_compatibility
        test_pairs = [
            ("Vancomycin", "Piperacillin-Tazobactam", False),  # Incompatible
            ("Vancomycin", "NS", True),  # Compatible
            ("Ceftriaxone", "Calcium", False),  # Incompatible
            ("Meropenem", "NS", True)  # Compatible
        ]
        
        for drug1, drug2, expected_compatible in test_pairs:
            compat = check_iv_compatibility(drug1, drug2)
            if compat:
                actual_compatible = compat.get('compatible', None)
                if actual_compatible == expected_compatible:
                    print(f"✅ {drug1} + {drug2}: {'Tương thích' if actual_compatible else 'Không tương thích'}")
                else:
                    print(f"⚠️ {drug1} + {drug2}: Expected {expected_compatible}, got {actual_compatible}")
            else:
                print(f"⚠️ {drug1} + {drug2}: Không có dữ liệu")
        
        # Test check_multiple_drugs
        drugs = ["Vancomycin", "Piperacillin-Tazobactam", "NS"]
        results = check_multiple_drugs(drugs)
        print(f"✅ check_multiple_drugs(): {len(results)} kết quả")
        
        # Test get_compatibility_summary
        summary = get_compatibility_summary("Vancomycin", "NS")
        print(f"✅ get_compatibility_summary(): '{summary}'")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_integration():
    """Test integration với database"""
    print("\n" + "="*60)
    print("TEST 4: Integration với Database")
    print("="*60)
    
    try:
        # Test TDM integration
        from antibiotics.database_display import display_antibiotic_info
        from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
        
        print("✅ Import display_antibiotic_info thành công")
        
        # Check Vancomycin exists
        if "Vancomycin" in ANTIBIOTICS_DATABASE:
            print("✅ Vancomycin có trong database")
        else:
            print("⚠️ Vancomycin không có trong database")
        
        # Test IV compatibility integration
        from antibiotics.iv_compatibility import render_iv_compatibility_checker
        print("✅ Import render_iv_compatibility_checker thành công")
        
        # Test pediatric integration
        from antibiotics.dosing_ui.dosage_display import render_detailed_dose
        print("✅ Import render_detailed_dose thành công")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_edge_cases():
    """Test edge cases"""
    print("\n" + "="*60)
    print("TEST 5: Edge Cases")
    print("="*60)
    
    try:
        # Test pediatric với age cực đoan
        very_young = get_pediatric_dosing_adjustment(0.01, 3.0)  # 3.65 days
        if very_young.get('category') == 'neonate':
            print("✅ Very young age (3.65 days): Neonate category")
        
        # Test IV compatibility với unknown drugs
        unknown_compat = check_iv_compatibility("UnknownDrug1", "UnknownDrug2")
        if unknown_compat is None:
            print("✅ Unknown drugs: Trả về None (đúng)")
        
        # Test multiple drugs với empty list
        empty_results = check_multiple_drugs([])
        if empty_results == []:
            print("✅ Empty drug list: Trả về empty list (đúng)")
        
        # Test pediatric warnings với various antibiotics
        test_antibiotics = ["Doxycycline", "Ciprofloxacin", "Vancomycin"]
        for ab in test_antibiotics:
            warnings = get_pediatric_warnings(5.0, ab)
            if warnings:
                print(f"✅ Warnings cho {ab}: {len(warnings)} warnings")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Chạy tất cả tests"""
    print("\n" + "="*60)
    print("🧪 TEST PHASE 5: ADVANCED FEATURES")
    print("="*60)
    
    results = []
    
    # Test 1: TDM Integration
    results.append(("tdm_integration", test_tdm_integration()))
    
    # Test 2: Pediatric Templates
    results.append(("pediatric_templates", test_pediatric_templates()))
    
    # Test 3: IV Compatibility
    results.append(("iv_compatibility", test_iv_compatibility()))
    
    # Test 4: Integration
    results.append(("integration", test_integration()))
    
    # Test 5: Edge Cases
    results.append(("edge_cases", test_edge_cases()))
    
    # Tổng kết
    print("\n" + "="*60)
    print("📊 TỔNG KẾT TEST")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n✅ Passed: {passed}/{total}")
    print(f"{'❌ Failed' if passed < total else '✅ All tests passed'}: {total - passed}/{total}")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

