"""
Week 2 - Drug Interactions Validation Script
Test với 50+ drug combinations để validate database và matching
"""

import sys
from typing import List, Tuple, Dict
from itertools import combinations

# Import interaction checker
try:
    from drugs.interactions_data import (
        check_interactions,
        normalize_drug_name,
        get_interaction,
        SEVERITY_MAJOR,
        SEVERITY_MODERATE,
        SEVERITY_MINOR,
        get_drug_autocomplete_suggestions
    )
    from drugs.interaction_checker import DrugInteractionChecker
except ImportError:
    print("Error: Cannot import drug interaction modules")
    sys.exit(1)


# Test drug combinations - 50+ combinations covering various scenarios
TEST_COMBINATIONS = [
    # Anticoagulants + Common drugs
    (["Warfarin", "Aspirin"], "Major interaction expected"),
    (["Warfarin", "Ibuprofen"], "Major interaction expected"),
    (["Warfarin", "Metronidazole"], "Major interaction expected"),
    (["Warfarin", "Ciprofloxacin"], "Moderate interaction expected"),
    (["Warfarin", "Omeprazole"], "Moderate interaction expected"),
    (["Warfarin", "Fluoxetine"], "Moderate interaction expected"),
    (["Warfarin", "Clopidogrel"], "Major interaction expected"),
    
    # Antibiotics + Warfarin
    (["Warfarin", "Amoxicillin"], "Moderate interaction expected"),
    (["Warfarin", "Ceftriaxone"], "Moderate interaction expected"),
    (["Warfarin", "Vancomycin"], "Moderate interaction expected"),
    (["Warfarin", "Linezolid"], "Moderate interaction expected"),
    (["Warfarin", "Rifampin"], "Major interaction expected"),
    
    # Antibiotics + Other drugs
    (["Ciprofloxacin", "Antacid"], "Major interaction expected"),
    (["Ciprofloxacin", "Theophylline"], "Major interaction expected"),
    (["Ciprofloxacin", "Tizanidine"], "Major interaction expected"),
    (["Ceftriaxone", "Calcium"], "Major interaction expected"),
    (["Linezolid", "SSRI"], "Major interaction expected"),
    (["Metronidazole", "Alcohol"], "Major interaction expected"),
    (["Rifampin", "Oral Contraceptive"], "Major interaction expected"),
    
    # Cardiovascular
    (["ACE Inhibitor", "Spironolactone"], "Major interaction expected"),
    (["ACE Inhibitor", "Potassium"], "Major interaction expected"),
    (["ACE Inhibitor", "Lithium"], "Moderate interaction expected"),
    (["ARB", "Spironolactone"], "Major interaction expected"),
    (["Digoxin", "Amiodarone"], "Major interaction expected"),
    (["Digoxin", "Erythromycin"], "Moderate interaction expected"),
    (["ACE Inhibitor", "NSAID"], "Moderate interaction expected"),
    
    # Statins
    (["Atorvastatin", "Clarithromycin"], "Major interaction expected"),
    (["Simvastatin", "Amiodarone"], "Major interaction expected"),
    (["Statins", "Gemfibrozil"], "Major interaction expected"),
    (["Daptomycin", "Statins"], "Major interaction expected"),
    
    # Antidiabetics
    (["Metformin", "Contrast Media"], "Major interaction expected"),
    (["Metformin", "Iodinated Contrast"], "Major interaction expected"),
    
    # Psychiatry
    (["Fluoxetine", "Tramadol"], "Major interaction expected"),
    (["MAOIs", "SSRIs"], "Major interaction expected"),
    (["Linezolid", "Tramadol"], "Major interaction expected"),
    
    # Methotrexate
    (["Methotrexate", "NSAID"], "Major interaction expected"),
    (["Methotrexate", "Trimethoprim-Sulfamethoxazole"], "Major interaction expected"),
    (["Amoxicillin", "Methotrexate"], "Moderate interaction expected"),
    
    # Other important interactions
    (["Clopidogrel", "Omeprazole"], "Major interaction expected"),
    (["Aspirin", "Clopidogrel"], "Moderate interaction expected"),
    (["Levothyroxine", "Calcium"], "Moderate interaction expected"),
    (["Levothyroxine", "Iron"], "Moderate interaction expected"),
    (["Theophylline", "Ciprofloxacin"], "Major interaction expected"),
    
    # Multiple drug combinations (3+ drugs)
    (["Warfarin", "Aspirin", "Ibuprofen"], "Multiple major interactions expected"),
    (["Warfarin", "Metronidazole", "Ciprofloxacin"], "Multiple interactions expected"),
    (["ACE Inhibitor", "Spironolactone", "Potassium"], "Multiple major interactions expected"),
    (["Atorvastatin", "Clarithromycin", "Warfarin"], "Multiple interactions expected"),
    (["Metformin", "Contrast Media", "ACE Inhibitor"], "Multiple interactions expected"),
    
    # Edge cases - drugs that might not have interactions
    (["Paracetamol", "Ibuprofen"], "No major interaction expected"),
    (["Amoxicillin", "Paracetamol"], "No major interaction expected"),
    (["Metformin", "Insulin"], "No major interaction expected"),
    
    # Class-based interactions
    (["ACE Inhibitor", "Eplerenone"], "Major interaction expected"),
    (["ARB", "Potassium"], "Major interaction expected"),
    (["Beta-blocker", "Digoxin"], "Moderate interaction possible"),
    (["PPI", "Clopidogrel"], "Moderate interaction possible"),
    
    # Additional test cases
    (["Vancomycin", "Aminoglycoside"], "Major interaction expected"),
    (["Gentamicin", "Vancomycin"], "Major interaction expected"),
    (["Colistin", "Aminoglycoside"], "Major interaction expected"),
    (["Trimethoprim-Sulfamethoxazole", "Warfarin"], "Major interaction expected"),
    (["Trimethoprim-Sulfamethoxazole", "Methotrexate"], "Major interaction expected"),
    (["Erythromycin", "Theophylline"], "Moderate interaction expected"),
    (["Clarithromycin", "Theophylline"], "Moderate interaction expected"),
    (["Doxycycline", "Antacid"], "Major interaction expected"),
    (["Doxycycline", "Calcium"], "Major interaction expected"),
    (["Doxycycline", "Iron"], "Major interaction expected"),
]


def validate_combination(drug_list: List[str], expected_note: str) -> Dict:
    """
    Validate a drug combination
    
    Args:
        drug_list: List of drug names
        expected_note: Note about what interaction is expected
    
    Returns:
        Validation result dict
    """
    result = {
        "drugs": drug_list,
        "expected_note": expected_note,
        "interactions_found": [],
        "normalized_drugs": [],
        "total_interactions": 0,
        "major_count": 0,
        "moderate_count": 0,
        "minor_count": 0,
        "validation_passed": False,
        "errors": []
    }
    
    try:
        # Normalize drug names
        normalized = [normalize_drug_name(drug, use_fuzzy=True) for drug in drug_list]
        result["normalized_drugs"] = normalized
        
        # Check interactions
        interactions = check_interactions(normalized)
        result["interactions_found"] = interactions
        result["total_interactions"] = len(interactions)
        
        # Count by severity
        for interaction in interactions:
            severity = interaction.get("severity", "Unknown")
            if severity == SEVERITY_MAJOR:
                result["major_count"] += 1
            elif severity == SEVERITY_MODERATE:
                result["moderate_count"] += 1
            elif severity == SEVERITY_MINOR:
                result["minor_count"] += 1
        
        # Validation passed if we found interactions when expected, or no interactions when not expected
        if "expected" in expected_note.lower():
            result["validation_passed"] = result["total_interactions"] > 0
        else:
            result["validation_passed"] = result["total_interactions"] == 0 or result["major_count"] == 0
            
    except Exception as e:
        result["errors"].append(str(e))
        result["validation_passed"] = False
    
    return result


def run_validation():
    """Run validation on all test combinations"""
    print("=" * 80)
    print("DRUG INTERACTIONS VALIDATION - WEEK 2")
    print("=" * 80)
    print(f"\nTesting {len(TEST_COMBINATIONS)} drug combinations...\n")
    
    results = []
    passed = 0
    failed = 0
    
    for i, (drug_list, expected_note) in enumerate(TEST_COMBINATIONS, 1):
        print(f"[{i}/{len(TEST_COMBINATIONS)}] Testing: {', '.join(drug_list)}")
        result = validate_combination(drug_list, expected_note)
        results.append(result)
        
        if result["validation_passed"]:
            passed += 1
            status = "[PASS]"
        else:
            failed += 1
            status = "[FAIL]"
        
        print(f"  {status} - Found {result['total_interactions']} interactions "
              f"(Major: {result['major_count']}, Moderate: {result['moderate_count']}, "
              f"Minor: {result['minor_count']})")
        
        if result["errors"]:
            print(f"  [WARNING] Errors: {', '.join(result['errors'])}")
        
        if result["normalized_drugs"] != drug_list:
            print(f"  [NOTE] Normalized: {', '.join(result['normalized_drugs'])}")
    
    # Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print(f"Total combinations tested: {len(TEST_COMBINATIONS)}")
    print(f"[PASSED] {passed}")
    print(f"[FAILED] {failed}")
    print(f"Success rate: {passed/len(TEST_COMBINATIONS)*100:.1f}%")
    
    # Detailed statistics
    total_interactions_found = sum(r["total_interactions"] for r in results)
    total_major = sum(r["major_count"] for r in results)
    total_moderate = sum(r["moderate_count"] for r in results)
    total_minor = sum(r["minor_count"] for r in results)
    
    print(f"\nTotal interactions detected: {total_interactions_found}")
    print(f"  - Major: {total_major}")
    print(f"  - Moderate: {total_moderate}")
    print(f"  - Minor: {total_minor}")
    
    # Failed cases
    if failed > 0:
        print("\n" + "=" * 80)
        print("FAILED CASES")
        print("=" * 80)
        for i, result in enumerate(results, 1):
            if not result["validation_passed"]:
                print(f"\n{i}. Drugs: {', '.join(result['drugs'])}")
                print(f"   Expected: {result['expected_note']}")
                print(f"   Found: {result['total_interactions']} interactions")
                if result["errors"]:
                    print(f"   Errors: {', '.join(result['errors'])}")
    
    # Test fuzzy matching
    print("\n" + "=" * 80)
    print("FUZZY MATCHING TEST")
    print("=" * 80)
    
    fuzzy_test_cases = [
        ("warfarin", "Warfarin"),
        ("aspirin", "Aspirin"),
        ("ibuprofen", "Ibuprofen"),
        ("metronidazol", "Metronidazole"),  # Common misspelling
        ("ciprofloxacine", "Ciprofloxacin"),  # Common misspelling
        ("omeprazol", "Omeprazole"),  # Common misspelling
    ]
    
    for test_input, expected in fuzzy_test_cases:
        normalized = normalize_drug_name(test_input, use_fuzzy=True)
        match_status = "[OK]" if normalized == expected else "[FAIL]"
        print(f"{match_status} '{test_input}' -> '{normalized}' (expected: '{expected}')")
    
    # Test autocomplete
    print("\n" + "=" * 80)
    print("AUTOCOMPLETE TEST")
    print("=" * 80)
    
    autocomplete_tests = ["war", "asp", "met", "cip", "ome"]
    for query in autocomplete_tests:
        suggestions = get_drug_autocomplete_suggestions(query, max_results=5)
        print(f"Query: '{query}' -> {suggestions[:5]}")
    
    return results


if __name__ == "__main__":
    results = run_validation()
    print("\n" + "=" * 80)
    print("Validation complete!")
    print("=" * 80)

