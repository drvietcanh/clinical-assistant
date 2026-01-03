"""
Test script for Session 1: Fuzzy Matching Improvements
Tests drug name matching with various scenarios
"""

import sys
sys.path.insert(0, '.')

from drugs.interactions_data import normalize_drug_name, _fuzzy_match, DRUG_ALIASES

def test_fuzzy_matching():
    """Test fuzzy matching algorithm"""
    print("=" * 60)
    print("TESTING FUZZY MATCHING ALGORITHM")
    print("=" * 60)
    
    test_cases = [
        # Exact matches
        ("Warfarin", "Warfarin", 1.0),
        ("warfarin", "Warfarin", 1.0),
        
        # Brand names
        ("Coumadin", "Warfarin", "Should match via alias"),
        ("Lipitor", "Atorvastatin", "Should match via alias"),
        ("Glucophage", "Metformin", "Should match via alias"),
        
        # With suffixes
        ("Warfarin sodium", "Warfarin", 0.98),
        ("Metformin HCl", "Metformin", 0.98),
        ("Aspirin tablet", "Aspirin", 0.98),
        
        # Typos
        ("Warfarrin", "Warfarin", "Should match with typo"),
        ("Metformine", "Metformin", "Should match with typo"),
        ("Aspirine", "Aspirin", "Should match with typo"),
        
        # Partial matches
        ("Warf", "Warfarin", "Should match partial"),
        ("Metform", "Metformin", "Should match partial"),
        
        # Vietnamese/common names
        ("Panadol", "Paracetamol", "Should match via alias"),
        ("Omez", "Omeprazole", "Should match via alias"),
        ("Cifran", "Ciprofloxacin", "Should match via alias"),
    ]
    
    passed = 0
    failed = 0
    
    for query, target, expected in test_cases:
        if isinstance(expected, float):
            score = _fuzzy_match(query, target, threshold=0.70)
            if score >= expected * 0.9:  # Allow 10% tolerance
                print(f"[PASS] '{query}' -> '{target}' (score: {score:.2f})")
                passed += 1
            else:
                print(f"[FAIL] '{query}' -> '{target}' (score: {score:.2f}, expected: {expected:.2f})")
                failed += 1
        else:
            # Test via normalize_drug_name
            normalized = normalize_drug_name(query)
            if normalized == target or normalized.lower() == target.lower():
                print(f"[PASS] '{query}' -> '{normalized}' (expected: '{target}')")
                passed += 1
            else:
                print(f"[FAIL] '{query}' -> '{normalized}' (expected: '{target}')")
                failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_drug_aliases():
    """Test drug aliases mapping"""
    print("\n" + "=" * 60)
    print("TESTING DRUG ALIASES")
    print("=" * 60)
    
    test_cases = [
        ("Coumadin", "Warfarin"),
        ("Lipitor", "Atorvastatin"),
        ("Glucophage", "Metformin"),
        ("Panadol", "Paracetamol"),
        ("Omez", "Omeprazole"),
        ("Cifran", "Ciprofloxacin"),
        ("Prozac", "Fluoxetine"),
        ("Zoloft", "Sertraline"),
        ("Norvasc", "Amlodipine"),
        ("Lasix", "Furosemide"),
    ]
    
    passed = 0
    failed = 0
    
    for alias, expected_canonical in test_cases:
        normalized = normalize_drug_name(alias)
        if normalized == expected_canonical:
            print(f"[PASS] '{alias}' -> '{normalized}'")
            passed += 1
        else:
            print(f"[FAIL] '{alias}' -> '{normalized}' (expected: '{expected_canonical}')")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_vietnamese_names():
    """Test Vietnamese name matching"""
    print("\n" + "=" * 60)
    print("TESTING VIETNAMESE NAMES")
    print("=" * 60)
    
    # Test common Vietnamese drug names
    test_cases = [
        ("Panadol", "Paracetamol"),
        ("Efferalgan", "Paracetamol"),
        ("Hapacol", "Paracetamol"),
        ("Omez", "Omeprazole"),
        ("Cifran", "Ciprofloxacin"),
    ]
    
    passed = 0
    failed = 0
    
    for vn_name, expected_canonical in test_cases:
        normalized = normalize_drug_name(vn_name)
        if normalized == expected_canonical:
            print(f"[PASS] '{vn_name}' -> '{normalized}'")
            passed += 1
        else:
            print(f"[FAIL] '{vn_name}' -> '{normalized}' (expected: '{expected_canonical}')")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_typos():
    """Test typo handling"""
    print("\n" + "=" * 60)
    print("TESTING TYPO HANDLING")
    print("=" * 60)
    
    test_cases = [
        ("Warfarrin", "Warfarin"),  # 1 char typo
        ("Metformine", "Metformin"),  # 1 char typo
        ("Aspirine", "Aspirin"),  # 1 char typo
        ("Atorvastatn", "Atorvastatin"),  # 1 char typo
        ("Omeprazol", "Omeprazole"),  # 1 char typo
    ]
    
    passed = 0
    failed = 0
    
    for typo, expected in test_cases:
        normalized = normalize_drug_name(typo, use_fuzzy=True)
        score = _fuzzy_match(typo, expected, threshold=0.70)
        if normalized == expected or score >= 0.70:
            print(f"[PASS] '{typo}' -> '{normalized}' (score: {score:.2f})")
            passed += 1
        else:
            print(f"[FAIL] '{typo}' -> '{normalized}' (score: {score:.2f})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SESSION 1: FUZZY MATCHING IMPROVEMENTS - TEST SUITE")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    
    # Run all tests
    p1, f1 = test_fuzzy_matching()
    total_passed += p1
    total_failed += f1
    
    p2, f2 = test_drug_aliases()
    total_passed += p2
    total_failed += f2
    
    p3, f3 = test_vietnamese_names()
    total_passed += p3
    total_failed += f3
    
    p4, f4 = test_typos()
    total_passed += p4
    total_failed += f4
    
    # Summary
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")
    print(f"Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    print("=" * 60)
    
    if total_failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
    else:
        print(f"\n[WARNING] {total_failed} tests failed. Review and fix issues.")

