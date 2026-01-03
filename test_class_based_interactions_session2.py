"""
Test script for Session 2: Class-Based Interactions
Tests class-based drug interaction detection
"""

import sys
sys.path.insert(0, '.')

from drugs.interactions_data import (
    get_drug_classes, 
    get_interaction, 
    DRUG_CLASS_MAPPINGS,
    SEVERITY_MAJOR,
    SEVERITY_MODERATE
)

def test_get_drug_classes():
    """Test get_drug_classes function"""
    print("=" * 60)
    print("TESTING get_drug_classes() FUNCTION")
    print("=" * 60)
    
    test_cases = [
        # ACE Inhibitors
        ("Lisinopril", ["ACE Inhibitor"]),
        ("Enalapril", ["ACE Inhibitor"]),
        
        # ARBs
        ("Losartan", ["ARB"]),
        ("Valsartan", ["ARB"]),
        
        # Statins
        ("Atorvastatin", ["Statins"]),
        ("Simvastatin", ["Statins"]),
        ("Rosuvastatin", ["Statins"]),
        
        # NSAIDs
        ("Ibuprofen", ["NSAID"]),
        ("Naproxen", ["NSAID"]),
        ("Diclofenac", ["NSAID"]),
        
        # SSRIs
        ("Fluoxetine", ["SSRI"]),
        ("Sertraline", ["SSRI"]),
        ("Citalopram", ["SSRI"]),
        
        # Anticoagulants
        ("Warfarin", ["Anticoagulant"]),
        ("Dabigatran", ["Anticoagulant", "DOAC"]),
        ("Rivaroxaban", ["Anticoagulant", "DOAC"]),
        
        # Antiplatelets
        ("Aspirin", ["Antiplatelet"]),
        ("Clopidogrel", ["Antiplatelet"]),
        
        # Macrolides
        ("Azithromycin", ["Macrolide"]),
        ("Clarithromycin", ["Macrolide"]),
        ("Erythromycin", ["Macrolide"]),
        
        # Azole Antifungals
        ("Fluconazole", ["Azole Antifungal"]),
        ("Ketoconazole", ["Azole Antifungal"]),
        ("Itraconazole", ["Azole Antifungal"]),
        
        # Potassium-sparing Diuretics
        ("Spironolactone", ["Potassium-sparing Diuretic", "Diuretic"]),
        ("Eplerenone", ["Potassium-sparing Diuretic", "Diuretic"]),
    ]
    
    passed = 0
    failed = 0
    
    for drug_name, expected_classes in test_cases:
        classes = get_drug_classes(drug_name)
        # Check if all expected classes are in the result
        missing = [c for c in expected_classes if c not in classes]
        if not missing:
            print(f"[PASS] '{drug_name}' -> {classes}")
            passed += 1
        else:
            print(f"[FAIL] '{drug_name}' -> {classes} (missing: {missing}, expected: {expected_classes})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_class_based_interactions():
    """Test class-based interactions"""
    print("\n" + "=" * 60)
    print("TESTING CLASS-BASED INTERACTIONS")
    print("=" * 60)
    
    test_cases = [
        # ACE Inhibitor + Potassium-sparing Diuretic
        ("Lisinopril", "Spironolactone", SEVERITY_MAJOR, "ACE Inhibitor + Potassium-sparing Diuretic"),
        ("Enalapril", "Eplerenone", SEVERITY_MAJOR, "ACE Inhibitor + Potassium-sparing Diuretic"),
        
        # ARB + Potassium-sparing Diuretic
        ("Losartan", "Spironolactone", SEVERITY_MAJOR, "ARB + Potassium-sparing Diuretic"),
        
        # Anticoagulant + Antiplatelet
        ("Warfarin", "Aspirin", SEVERITY_MAJOR, "Anticoagulant + Antiplatelet"),
        ("Warfarin", "Clopidogrel", SEVERITY_MAJOR, "Anticoagulant + Antiplatelet"),
        
        # Anticoagulant + NSAID
        ("Warfarin", "Ibuprofen", SEVERITY_MAJOR, "Anticoagulant + NSAID"),
        ("Dabigatran", "Naproxen", SEVERITY_MAJOR, "Anticoagulant + NSAID"),
        
        # Statins + Macrolides
        ("Atorvastatin", "Clarithromycin", SEVERITY_MAJOR, "Statins + Macrolide"),
        ("Simvastatin", "Erythromycin", SEVERITY_MAJOR, "Statins + Macrolide"),
        
        # Statins + Azole Antifungals
        ("Atorvastatin", "Ketoconazole", SEVERITY_MAJOR, "Statins + Azole Antifungal"),
        ("Simvastatin", "Itraconazole", SEVERITY_MAJOR, "Statins + Azole Antifungal"),
        
        # ACE Inhibitor + NSAID
        ("Lisinopril", "Ibuprofen", SEVERITY_MODERATE, "ACE Inhibitor + NSAID"),
        ("Enalapril", "Naproxen", SEVERITY_MODERATE, "ACE Inhibitor + NSAID"),
        
        # ARB + NSAID
        ("Losartan", "Ibuprofen", SEVERITY_MODERATE, "ARB + NSAID"),
        
        # SSRI + MAOI (should be detected via class)
        ("Fluoxetine", "MAOI", SEVERITY_MAJOR, "SSRI + MAOI"),
        
        # SSRI + Opioid
        ("Fluoxetine", "Tramadol", SEVERITY_MAJOR, "SSRI + Opioid"),
        
        # Quinolone + Antacid
        ("Ciprofloxacin", "Antacid", SEVERITY_MAJOR, "Quinolone + Antacid"),
        
        # Metformin + Contrast Media
        ("Metformin", "Contrast Media", SEVERITY_MAJOR, "Metformin + Contrast Media"),
        
        # Methotrexate + NSAID
        ("Methotrexate", "Ibuprofen", SEVERITY_MAJOR, "Methotrexate + NSAID"),
    ]
    
    passed = 0
    failed = 0
    
    for drug1, drug2, expected_severity, description in test_cases:
        interaction = get_interaction(drug1, drug2, check_classes=True)
        if interaction:
            severity = interaction.get('severity')
            if severity == expected_severity:
                print(f"[PASS] '{drug1}' + '{drug2}' -> {severity} ({description})")
                passed += 1
            else:
                print(f"[FAIL] '{drug1}' + '{drug2}' -> {severity} (expected: {expected_severity}, {description})")
                failed += 1
        else:
            print(f"[FAIL] '{drug1}' + '{drug2}' -> No interaction found (expected: {expected_severity}, {description})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_class_class_interactions():
    """Test class-class interactions"""
    print("\n" + "=" * 60)
    print("TESTING CLASS-CLASS INTERACTIONS")
    print("=" * 60)
    
    test_cases = [
        ("ACE Inhibitor", "Potassium-sparing Diuretic", SEVERITY_MAJOR),
        ("ARB", "Potassium-sparing Diuretic", SEVERITY_MAJOR),
        ("Anticoagulant", "Antiplatelet", SEVERITY_MAJOR),
        ("Anticoagulant", "NSAID", SEVERITY_MAJOR),
        ("Statins", "Macrolide", SEVERITY_MAJOR),
        ("Statins", "Azole Antifungal", SEVERITY_MAJOR),
        ("ACE Inhibitor", "NSAID", SEVERITY_MODERATE),
        ("ARB", "NSAID", SEVERITY_MODERATE),
        ("SSRI", "MAOI", SEVERITY_MAJOR),
        ("SSRI", "Opioid", SEVERITY_MAJOR),
        ("Quinolone", "Antacid", SEVERITY_MAJOR),
        ("Metformin", "Contrast Media", SEVERITY_MAJOR),
        ("Methotrexate", "NSAID", SEVERITY_MAJOR),
    ]
    
    passed = 0
    failed = 0
    
    for class1, class2, expected_severity in test_cases:
        interaction = get_interaction(class1, class2, check_classes=True)
        if interaction:
            severity = interaction.get('severity')
            if severity == expected_severity:
                print(f"[PASS] '{class1}' + '{class2}' -> {severity}")
                passed += 1
            else:
                print(f"[FAIL] '{class1}' + '{class2}' -> {severity} (expected: {expected_severity})")
                failed += 1
        else:
            print(f"[FAIL] '{class1}' + '{class2}' -> No interaction found (expected: {expected_severity})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_drug_class_mappings():
    """Test DRUG_CLASS_MAPPINGS coverage"""
    print("\n" + "=" * 60)
    print("TESTING DRUG_CLASS_MAPPINGS COVERAGE")
    print("=" * 60)
    
    # Count total classes
    total_classes = len(DRUG_CLASS_MAPPINGS)
    print(f"Total drug classes: {total_classes}")
    
    # Count total drugs in all classes
    all_drugs = set()
    for drugs_list in DRUG_CLASS_MAPPINGS.values():
        all_drugs.update(drugs_list)
    print(f"Total unique drugs in classes: {len(all_drugs)}")
    
    # List all classes
    print("\nDrug classes:")
    for i, class_name in enumerate(sorted(DRUG_CLASS_MAPPINGS.keys()), 1):
        drug_count = len(DRUG_CLASS_MAPPINGS[class_name])
        print(f"  {i:2d}. {class_name:30s} ({drug_count:2d} drugs)")
    
    print("\n" + "=" * 60)
    
    return total_classes, len(all_drugs)


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SESSION 2: CLASS-BASED INTERACTIONS - TEST SUITE")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    
    # Run all tests
    p1, f1 = test_get_drug_classes()
    total_passed += p1
    total_failed += f1
    
    p2, f2 = test_class_based_interactions()
    total_passed += p2
    total_failed += f2
    
    p3, f3 = test_class_class_interactions()
    total_passed += p3
    total_failed += f3
    
    test_drug_class_mappings()
    
    # Summary
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")
    if total_passed + total_failed > 0:
        print(f"Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    print("=" * 60)
    
    if total_failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
    else:
        print(f"\n[WARNING] {total_failed} tests failed. Review and fix issues.")

