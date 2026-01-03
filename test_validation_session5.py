"""
Test script for Session 5: Testing & Validation
Tests 50+ drug combinations, performance, and accuracy
"""

import sys
import time
sys.path.insert(0, '.')

# Set encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from drugs.interaction_checker import DrugInteractionChecker
from drugs.interactions_data import (
    get_interaction,
    SEVERITY_MAJOR,
    SEVERITY_MODERATE,
    SEVERITY_MINOR
)


def test_50_plus_drug_combinations():
    """Test with 50+ real-world drug combinations"""
    print("=" * 60)
    print("TESTING 50+ DRUG COMBINATIONS")
    print("=" * 60)
    
    # Real-world drug combinations (common scenarios)
    test_combinations = [
        # Anticoagulation scenarios
        (["Warfarin", "Aspirin"], True, "Anticoagulant + Antiplatelet"),
        (["Warfarin", "Ibuprofen"], True, "Anticoagulant + NSAID"),
        (["Warfarin", "Clopidogrel"], True, "Anticoagulant + Antiplatelet"),
        (["Warfarin", "Metronidazole"], True, "Anticoagulant + Antibiotic"),
        (["Warfarin", "Fluconazole"], True, "Anticoagulant + Antifungal"),
        (["Dabigatran", "Aspirin"], True, "DOAC + Antiplatelet"),
        (["Rivaroxaban", "Ibuprofen"], True, "DOAC + NSAID"),
        
        # Cardiovascular scenarios
        (["Lisinopril", "Spironolactone"], True, "ACE-I + K-sparing diuretic"),
        (["Lisinopril", "Ibuprofen"], True, "ACE-I + NSAID"),
        (["Losartan", "Spironolactone"], True, "ARB + K-sparing diuretic"),
        (["Amlodipine", "Simvastatin"], True, "CCB + Statin"),
        (["Digoxin", "Amiodarone"], True, "Digoxin + Amiodarone"),
        (["Metoprolol", "Amlodipine"], False, "Beta-blocker + CCB (usually safe)"),
        
        # Statin interactions
        (["Atorvastatin", "Clarithromycin"], True, "Statin + Macrolide"),
        (["Simvastatin", "Amiodarone"], True, "Statin + Amiodarone"),
        (["Atorvastatin", "Ketoconazole"], True, "Statin + Azole antifungal"),
        (["Rosuvastatin", "Clarithromycin"], True, "Statin + Macrolide"),
        
        # Antidepressant interactions
        (["Fluoxetine", "Tramadol"], True, "SSRI + Opioid"),
        (["Fluoxetine", "Warfarin"], True, "SSRI + Anticoagulant"),
        (["Sertraline", "Warfarin"], True, "SSRI + Anticoagulant"),
        (["Fluoxetine", "MAOI"], True, "SSRI + MAOI"),
        
        # Antibiotic interactions
        (["Ciprofloxacin", "Warfarin"], True, "Quinolone + Anticoagulant"),
        (["Ciprofloxacin", "Antacid"], True, "Quinolone + Antacid"),
        (["Amoxicillin", "Warfarin"], True, "Penicillin + Anticoagulant"),
        (["Azithromycin", "Warfarin"], True, "Macrolide + Anticoagulant"),
        
        # Antidiabetic interactions
        (["Metformin", "Contrast Media"], True, "Metformin + Contrast"),
        (["Metformin", "Ibuprofen"], False, "Metformin + NSAID (usually safe)"),
        
        # Methotrexate interactions
        (["Methotrexate", "Ibuprofen"], True, "Methotrexate + NSAID"),
        (["Methotrexate", "Trimethoprim-Sulfamethoxazole"], True, "Methotrexate + TMP-SMX"),
        
        # PPI interactions
        (["Omeprazole", "Clopidogrel"], True, "PPI + Antiplatelet"),
        (["Pantoprazole", "Warfarin"], False, "Pantoprazole + Warfarin (usually safe)"),
        
        # Common safe combinations
        (["Paracetamol", "Aspirin"], False, "Paracetamol + Aspirin (usually safe)"),
        (["Metformin", "Glibenclamide"], False, "Metformin + Sulfonylurea (usually safe)"),
        (["Amlodipine", "Metoprolol"], False, "CCB + Beta-blocker (usually safe)"),
        (["Omeprazole", "Amoxicillin"], False, "PPI + Penicillin (usually safe)"),
        
        # Complex scenarios (3+ drugs)
        (["Warfarin", "Aspirin", "Ibuprofen"], True, "Triple anticoagulation risk"),
        (["Lisinopril", "Spironolactone", "Potassium"], True, "Triple hyperkalemia risk"),
        (["Atorvastatin", "Clarithromycin", "Warfarin"], True, "Multiple interactions"),
        (["Metformin", "Glibenclamide", "Insulin"], False, "Triple antidiabetic (usually safe)"),
        
        # More combinations
        (["Warfarin", "Fluconazole"], True, "Anticoagulant + Antifungal"),
        (["Warfarin", "Ciprofloxacin"], True, "Anticoagulant + Quinolone"),
        (["Warfarin", "Erythromycin"], True, "Anticoagulant + Macrolide"),
        (["Warfarin", "Omeprazole"], True, "Anticoagulant + PPI"),
        (["Warfarin", "Sertraline"], True, "Anticoagulant + SSRI"),
        
        (["ACE Inhibitor", "Potassium"], True, "ACE-I + Potassium supplement"),
        (["ACE Inhibitor", "Eplerenone"], True, "ACE-I + K-sparing diuretic"),
        (["ARB", "Potassium"], True, "ARB + Potassium supplement"),
        
        (["Statins", "Gemfibrozil"], True, "Statin + Fibrate"),
        (["Statins", "Macrolide"], True, "Statin + Macrolide class"),
        (["Statins", "Azole Antifungal"], True, "Statin + Azole class"),
        
        (["SSRI", "SNRI"], True, "SSRI + SNRI"),
        (["SSRI", "Opioid"], True, "SSRI + Opioid class"),
        
        (["Quinolone", "Antacid"], True, "Quinolone + Antacid class"),
        (["Metformin", "Contrast Media"], True, "Metformin + Contrast class"),
        (["Methotrexate", "NSAID"], True, "Methotrexate + NSAID class"),
        
        # Edge cases
        (["Unknown Drug", "Warfarin"], False, "Unknown drug (should handle gracefully)"),
        (["Warfarin", "Warfarin"], False, "Same drug (should not interact)"),
        ([], False, "Empty list"),
        (["Warfarin"], False, "Single drug"),
    ]
    
    checker = DrugInteractionChecker()
    passed = 0
    failed = 0
    total_interactions_found = 0
    
    for drugs, should_have_interaction, description in test_combinations:
        try:
            if len(drugs) < 2:
                interactions = []
            else:
                interactions = checker.check_multiple(drugs)
            
            has_interaction = len(interactions) > 0
            
            if should_have_interaction == has_interaction:
                status = "[PASS]"
                passed += 1
                if has_interaction:
                    total_interactions_found += len(interactions)
                    print(f"{status} {description}: Found {len(interactions)} interaction(s)")
                else:
                    print(f"{status} {description}: No interactions (as expected)")
            else:
                status = "[FAIL]"
                failed += 1
                print(f"{status} {description}: Expected interaction={should_have_interaction}, Got={has_interaction}")
        except Exception as e:
            print(f"[ERROR] {description}: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print(f"Total interactions detected: {total_interactions_found}")
    print("=" * 60)
    
    return passed, failed, total_interactions_found


def test_performance():
    """Test performance with large drug lists"""
    print("\n" + "=" * 60)
    print("TESTING PERFORMANCE")
    print("=" * 60)
    
    checker = DrugInteractionChecker()
    
    # Test with different list sizes
    test_sizes = [5, 10, 15, 20]
    
    # Common drugs for testing
    test_drugs = [
        "Warfarin", "Aspirin", "Metformin", "Lisinopril", "Atorvastatin",
        "Ibuprofen", "Omeprazole", "Amoxicillin", "Fluoxetine", "Digoxin",
        "Amlodipine", "Metoprolol", "Furosemide", "Paracetamol", "Clopidogrel",
        "Simvastatin", "Losartan", "Spironolactone", "Ciprofloxacin", "Clarithromycin"
    ]
    
    results = []
    
    for size in test_sizes:
        drug_list = test_drugs[:size]
        
        # Measure time
        start_time = time.time()
        interactions = checker.check_multiple(drug_list)
        end_time = time.time()
        
        elapsed = (end_time - start_time) * 1000  # Convert to milliseconds
        
        # Calculate expected pairs
        expected_pairs = size * (size - 1) // 2
        
        results.append({
            'size': size,
            'pairs': expected_pairs,
            'interactions': len(interactions),
            'time_ms': elapsed
        })
        
        print(f"[INFO] {size} drugs: {expected_pairs} pairs checked, {len(interactions)} interactions found, {elapsed:.2f}ms")
    
    # Performance criteria
    print("\nPerformance Criteria:")
    print("- <100ms for 10 drugs: ", "PASS" if results[1]['time_ms'] < 100 else "FAIL")
    print("- <500ms for 20 drugs: ", "PASS" if results[3]['time_ms'] < 500 else "FAIL")
    
    print("\n" + "=" * 60)
    
    return results


def test_accuracy_known_interactions():
    """Test accuracy with known interactions"""
    print("\n" + "=" * 60)
    print("TESTING ACCURACY - KNOWN INTERACTIONS")
    print("=" * 60)
    
    # Known interactions from literature (Micromedex/Lexicomp level)
    known_interactions = [
        {
            'drug1': 'Warfarin',
            'drug2': 'Aspirin',
            'expected_severity': SEVERITY_MAJOR,
            'expected_effect': 'bleeding'
        },
        {
            'drug1': 'Lisinopril',
            'drug2': 'Spironolactone',
            'expected_severity': SEVERITY_MAJOR,
            'expected_effect': 'hyperkalemia'
        },
        {
            'drug1': 'Atorvastatin',
            'drug2': 'Clarithromycin',
            'expected_severity': SEVERITY_MAJOR,
            'expected_effect': 'rhabdomyolysis'
        },
        {
            'drug1': 'Fluoxetine',
            'drug2': 'Tramadol',
            'expected_severity': SEVERITY_MAJOR,
            'expected_effect': 'serotonin'
        },
        {
            'drug1': 'Metformin',
            'drug2': 'Contrast Media',
            'expected_severity': SEVERITY_MAJOR,
            'expected_effect': 'lactic acidosis'
        },
    ]
    
    passed = 0
    failed = 0
    
    for test_case in known_interactions:
        interaction = get_interaction(test_case['drug1'], test_case['drug2'], check_classes=True)
        
        if interaction:
            severity = interaction.get('severity')
            effect = interaction.get('effect', interaction.get('description', '')).lower()
            
            severity_match = severity == test_case['expected_severity']
            effect_match = test_case['expected_effect'].lower() in effect
            
            if severity_match and effect_match:
                print(f"[PASS] {test_case['drug1']} + {test_case['drug2']}: Severity={severity}, Effect matches")
                passed += 1
            else:
                print(f"[FAIL] {test_case['drug1']} + {test_case['drug2']}: Severity={severity} (expected {test_case['expected_severity']}), Effect={effect[:50]}")
                failed += 1
        else:
            print(f"[FAIL] {test_case['drug1']} + {test_case['drug2']}: No interaction found")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES")
    print("=" * 60)
    
    checker = DrugInteractionChecker()
    
    edge_cases = [
        ([], "Empty list"),
        (["Warfarin"], "Single drug"),
        (["Warfarin", "Warfarin"], "Duplicate drugs"),
        (["", "Warfarin"], "Empty string drug"),
        (["Warfarin", "   "], "Whitespace drug"),
        (["Warfarin", "UnknownDrug123"], "Unknown drug"),
        (["Warfarin"] * 10, "Many duplicates"),
    ]
    
    passed = 0
    failed = 0
    
    for drug_list, description in edge_cases:
        try:
            interactions = checker.check_multiple(drug_list)
            print(f"[PASS] {description}: Handled gracefully ({len(interactions)} interactions)")
            passed += 1
        except Exception as e:
            print(f"[FAIL] {description}: Error - {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_class_based_detection():
    """Test class-based interaction detection"""
    print("\n" + "=" * 60)
    print("TESTING CLASS-BASED DETECTION")
    print("=" * 60)
    
    test_cases = [
        ("Lisinopril", "Spironolactone", True, "ACE-I + K-sparing"),
        ("Losartan", "Eplerenone", True, "ARB + K-sparing"),
        ("Atorvastatin", "Clarithromycin", True, "Statin + Macrolide"),
        ("Simvastatin", "Ketoconazole", True, "Statin + Azole"),
        ("Warfarin", "Ibuprofen", True, "Anticoagulant + NSAID"),
        ("Fluoxetine", "Tramadol", True, "SSRI + Opioid"),
    ]
    
    passed = 0
    failed = 0
    
    for drug1, drug2, should_detect, description in test_cases:
        interaction = get_interaction(drug1, drug2, check_classes=True)
        
        detected = interaction is not None
        
        if should_detect == detected:
            print(f"[PASS] {description}: Detected={detected}")
            passed += 1
        else:
            print(f"[FAIL] {description}: Detected={detected} (expected {should_detect})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SESSION 5: TESTING & VALIDATION - TEST SUITE")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    
    # Run all tests
    p1, f1, interactions_found = test_50_plus_drug_combinations()
    total_passed += p1
    total_failed += f1
    
    performance_results = test_performance()
    
    p3, f3 = test_accuracy_known_interactions()
    total_passed += p3
    total_failed += f3
    
    p4, f4 = test_edge_cases()
    total_passed += p4
    total_failed += f4
    
    p5, f5 = test_class_based_detection()
    total_passed += p5
    total_failed += f5
    
    # Summary
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")
    print(f"Total Interactions Detected: {interactions_found}")
    if total_passed + total_failed > 0:
        print(f"Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    print("=" * 60)
    
    # Performance summary
    if performance_results:
        print("\nPerformance Summary:")
        for result in performance_results:
            print(f"  {result['size']} drugs: {result['time_ms']:.2f}ms ({result['pairs']} pairs, {result['interactions']} interactions)")
    
    if total_failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
    else:
        print(f"\n[WARNING] {total_failed} tests failed. Review and fix issues.")

