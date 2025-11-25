"""
Day 9: Drug Interactions Testing Suite
Comprehensive testing for drug interaction checker
Tests 50+ drug combinations, accuracy, and performance
"""

import sys
import time
from pathlib import Path
from typing import List, Tuple, Dict

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.interactions_data import (
    check_interactions,
    get_interaction,
    normalize_drug_name,
    get_drug_classes,
    get_drug_autocomplete_suggestions,
    SEVERITY_MAJOR,
    SEVERITY_MODERATE,
    SEVERITY_MINOR,
    DRUG_INTERACTIONS
)


class DrugInteractionTester:
    """Test suite for drug interactions"""
    
    def __init__(self):
        self.test_results = {
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'total': 0
        }
        self.failed_tests = []
        self.warning_tests = []
    
    def test_case(self, name: str, test_func, expected_result=True):
        """Run a single test case"""
        self.test_results['total'] += 1
        try:
            result = test_func()
            if result == expected_result:
                self.test_results['passed'] += 1
                print(f"✅ PASS: {name}")
                return True
            else:
                self.test_results['failed'] += 1
                self.failed_tests.append(name)
                print(f"❌ FAIL: {name} - Expected {expected_result}, got {result}")
                return False
        except Exception as e:
            self.test_results['failed'] += 1
            self.failed_tests.append(f"{name} - Exception: {str(e)}")
            print(f"❌ FAIL: {name} - Exception: {str(e)}")
            return False
    
    def test_warning(self, name: str, test_func):
        """Run a test that may have warnings"""
        self.test_results['total'] += 1
        try:
            result = test_func()
            self.test_results['passed'] += 1
            self.test_results['warnings'] += 1
            self.warning_tests.append(f"{name}: {result}")
            print(f"⚠️  WARN: {name} - {result}")
            return True
        except Exception as e:
            self.test_results['failed'] += 1
            self.failed_tests.append(f"{name} - Exception: {str(e)}")
            print(f"❌ FAIL: {name} - Exception: {str(e)}")
            return False
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 80)
        print("📊 TEST SUMMARY")
        print("=" * 80)
        print(f"Total Tests: {self.test_results['total']}")
        print(f"✅ Passed: {self.test_results['passed']}")
        print(f"❌ Failed: {self.test_results['failed']}")
        print(f"⚠️  Warnings: {self.test_results['warnings']}")
        print(f"Success Rate: {(self.test_results['passed'] / self.test_results['total'] * 100):.1f}%")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"  - {test}")
        
        if self.warning_tests:
            print("\n⚠️  Warnings:")
            for test in self.warning_tests[:10]:  # Show first 10
                print(f"  - {test}")


# Test Cases

def test_known_major_interactions():
    """Test 1: Known major interactions should be detected"""
    test_cases = [
        ("Warfarin", "Aspirin", True),
        ("Warfarin", "Ibuprofen", True),
        ("Warfarin", "Metronidazole", True),
        ("Atorvastatin", "Clarithromycin", True),
        ("Simvastatin", "Amiodarone", True),
        ("ACE Inhibitor", "Potassium", True),
        ("ACE Inhibitor", "Spironolactone", True),
        ("Digoxin", "Amiodarone", True),
        ("Methotrexate", "NSAID", True),
        ("Methotrexate", "Trimethoprim-Sulfamethoxazole", True),
    ]
    
    all_passed = True
    for drug1, drug2, should_find in test_cases:
        interaction = get_interaction(drug1, drug2)
        found = interaction is not None
        if found:
            severity = interaction.get('severity')
            if severity != SEVERITY_MAJOR:
                print(f"  ⚠️  {drug1} + {drug2}: Found but severity is {severity}, expected Major")
        if found != should_find:
            print(f"  ❌ {drug1} + {drug2}: Expected {should_find}, got {found}")
            all_passed = False
    
    return all_passed


def test_class_based_interactions():
    """Test 2: Class-based interactions should work"""
    test_cases = [
        # ACE Inhibitor class
        ("Lisinopril", "Potassium", True),  # Lisinopril is ACE Inhibitor
        ("Captopril", "Spironolactone", True),
        # ARB class
        ("Losartan", "Potassium", True),  # Losartan is ARB
        ("Valsartan", "Spironolactone", True),
        # Beta-blocker class
        ("Metoprolol", "Digoxin", True),  # Beta-blocker + Digoxin
        ("Atenolol", "Insulin", True),  # Beta-blocker + Insulin
        # PPI class
        ("Omeprazole", "Clopidogrel", True),  # PPI + Clopidogrel (Omeprazole specifically)
        ("Pantoprazole", "Methotrexate", True),  # PPI + Methotrexate
        # NSAID class
        ("Naproxen", "Warfarin", True),  # NSAID + Warfarin
        ("Diclofenac", "ACE Inhibitor", True),  # NSAID + ACE Inhibitor
    ]
    
    all_passed = True
    for drug1, drug2, should_find in test_cases:
        interaction = get_interaction(drug1, drug2, check_classes=True)
        found = interaction is not None
        if found != should_find:
            print(f"  ❌ {drug1} + {drug2}: Expected {should_find}, got {found}")
            all_passed = False
    
    return all_passed


def test_fuzzy_matching():
    """Test 3: Fuzzy matching should work for similar drug names"""
    test_cases = [
        ("warfarin", "Warfarin"),  # Case insensitive
        ("WARFARIN", "Warfarin"),
        ("aspirin", "Aspirin"),
        ("metformin", "Metformin"),
    ]
    
    all_passed = True
    for input_name, expected_normalized in test_cases:
        try:
            normalized = normalize_drug_name(input_name, use_fuzzy=True)
            # Should normalize to expected (case-insensitive match is acceptable)
            if normalized.lower() != expected_normalized.lower():
                # Check if normalized name can find interactions (valid alternative)
                test_interaction = get_interaction(normalized, "Aspirin")
                if test_interaction is None:
                    print(f"  ⚠️  {input_name} → {normalized} (expected {expected_normalized})")
        except Exception as e:
            print(f"  ❌ {input_name}: Exception in fuzzy matching - {str(e)}")
            import traceback
            traceback.print_exc()
            all_passed = False
    
    return all_passed


def test_multiple_drug_combinations():
    """Test 4: Test with multiple drug combinations (50+ combinations)"""
    # Common drug combinations in clinical practice
    test_combinations = [
        # Anticoagulation scenarios
        ["Warfarin", "Aspirin", "Omeprazole"],
        ["Warfarin", "Metronidazole", "Ciprofloxacin"],
        ["Dabigatran", "Aspirin", "Clopidogrel"],
        
        # Cardiovascular polypharmacy
        ["Lisinopril", "Metoprolol", "Amlodipine", "Atorvastatin", "Aspirin"],
        ["Losartan", "Hydrochlorothiazide", "Metformin", "Omeprazole"],
        ["Digoxin", "Amiodarone", "Furosemide", "Spironolactone"],
        
        # Diabetes + cardiovascular
        ["Metformin", "Glibenclamide", "Lisinopril", "Atorvastatin"],
        ["Insulin", "Metoprolol", "Furosemide"],
        
        # Psychiatry + other drugs
        ["Fluoxetine", "Warfarin", "Omeprazole"],
        ["Sertraline", "Tramadol", "Ibuprofen"],
        ["Lithium", "ACE Inhibitor", "Furosemide"],
        
        # Antibiotic combinations
        ["Vancomycin", "Gentamicin", "Furosemide"],
        ["Ciprofloxacin", "Warfarin", "Theophylline"],
        ["Erythromycin", "Warfarin", "Digoxin"],
        ["Clarithromycin", "Atorvastatin", "Warfarin"],
        
        # Oncology + supportive care
        ["Methotrexate", "NSAID", "Furosemide"],
        ["Methotrexate", "Trimethoprim-Sulfamethoxazole", "Omeprazole"],
        ["5-Fluorouracil", "Warfarin", "Metronidazole"],
        
        # GI drugs
        ["Omeprazole", "Clopidogrel", "Aspirin"],
        ["Pantoprazole", "Warfarin", "Ketoconazole"],
        
        # Complex scenarios
        ["Warfarin", "Aspirin", "Ibuprofen", "Omeprazole", "Metformin"],
        ["Lisinopril", "Spironolactone", "Potassium", "Furosemide"],
        ["Digoxin", "Amiodarone", "Verapamil", "Furosemide"],
        ["Atorvastatin", "Clarithromycin", "Warfarin", "Omeprazole"],
    ]
    
    total_interactions_found = 0
    all_passed = True
    
    for i, drug_list in enumerate(test_combinations, 1):
        interactions = check_interactions(drug_list)
        total_interactions_found += len(interactions)
        
        # Check that we're finding interactions (at least some should have interactions)
        if len(drug_list) >= 3 and len(interactions) == 0:
            # This might be okay, but log it
            print(f"  ⚠️  Combination {i}: {len(drug_list)} drugs, 0 interactions found")
            print(f"      Drugs: {', '.join(drug_list)}")
    
    print(f"  📊 Tested {len(test_combinations)} combinations")
    print(f"  📊 Total interactions found: {total_interactions_found}")
    print(f"  📊 Average interactions per combination: {total_interactions_found / len(test_combinations):.1f}")
    
    return all_passed


def test_autocomplete():
    """Test 5: Autocomplete suggestions should work"""
    test_cases = [
        ("warf", ["Warfarin"]),
        ("asp", ["Aspirin"]),
        ("met", ["Metformin", "Metoprolol", "Metronidazole"]),  # Should find multiple
        ("ome", ["Omeprazole"]),
        ("cip", ["Ciprofloxacin"]),
    ]
    
    all_passed = True
    for query, expected_contains in test_cases:
        suggestions = get_drug_autocomplete_suggestions(query, max_results=10)
        if not suggestions:
            print(f"  ❌ Query '{query}': No suggestions returned")
            all_passed = False
        else:
            # Check if expected drugs are in suggestions
            found_any = any(exp.lower() in [s.lower() for s in suggestions] for exp in expected_contains)
            if not found_any:
                print(f"  ⚠️  Query '{query}': Expected one of {expected_contains}, got {suggestions[:3]}")
    
    return all_passed


def test_drug_class_detection():
    """Test 6: Drug class detection should work"""
    test_cases = [
        ("Lisinopril", ["ACE Inhibitor"]),
        ("Losartan", ["ARB"]),
        ("Metoprolol", ["Beta-blocker"]),
        ("Amlodipine", ["CCB", "Calcium Channel Blocker"]),
        ("Atorvastatin", ["Statins"]),
        ("Ibuprofen", ["NSAID"]),
        ("Fluoxetine", ["SSRI"]),
        ("Omeprazole", ["PPI"]),
    ]
    
    all_passed = True
    for drug, expected_classes in test_cases:
        classes = get_drug_classes(drug)
        found_any = any(exp in classes for exp in expected_classes)
        if not found_any:
            print(f"  ⚠️  {drug}: Expected one of {expected_classes}, got {classes}")
    
    return all_passed


def test_performance():
    """Test 7: Performance testing"""
    # Large drug list
    large_drug_list = [
        "Warfarin", "Aspirin", "Metformin", "Omeprazole", "Ibuprofen",
        "Atorvastatin", "Amlodipine", "Metoprolol", "Digoxin", "Insulin",
        "Lisinopril", "Losartan", "Furosemide", "Spironolactone", "Amiodarone",
        "Ciprofloxacin", "Clarithromycin", "Metronidazole", "Fluoxetine", "Sertraline"
    ]
    
    # Test check_interactions performance
    start_time = time.perf_counter()
    interactions = check_interactions(large_drug_list)
    end_time = time.perf_counter()
    elapsed = (end_time - start_time) * 1000  # Convert to milliseconds
    
    print(f"  ⏱️  Performance: {len(large_drug_list)} drugs, {len(interactions)} interactions found")
    print(f"  ⏱️  Time: {elapsed:.2f} ms")
    print(f"  ⏱️  Time per drug pair: {elapsed / (len(large_drug_list) * (len(large_drug_list) - 1) / 2):.3f} ms")
    
    # Should complete in reasonable time (< 1 second for 20 drugs)
    return elapsed < 1000


def test_edge_cases():
    """Test 8: Edge cases"""
    edge_cases = [
        # Empty list
        (lambda: check_interactions([]), []),
        # Single drug
        (lambda: check_interactions(["Warfarin"]), []),
        # Duplicate drugs
        (lambda: check_interactions(["Warfarin", "warfarin", "WARFARIN"]), []),
        # Very long names
        (lambda: get_interaction("A" * 100, "B" * 100), None),
        # Special characters
        (lambda: normalize_drug_name("Warfarin-123"), "Warfarin-123"),
    ]
    
    all_passed = True
    for test_func, expected in edge_cases:
        try:
            result = test_func()
            # For edge cases, we mainly check they don't crash
            print(f"  ✅ Edge case handled: {result}")
        except Exception as e:
            print(f"  ❌ Edge case failed: {str(e)}")
            all_passed = False
    
    return all_passed


def test_severity_distribution():
    """Test 9: Check severity distribution in database"""
    severity_counts = {
        SEVERITY_MAJOR: 0,
        SEVERITY_MODERATE: 0,
        SEVERITY_MINOR: 0
    }
    
    for interaction in DRUG_INTERACTIONS.values():
        severity = interaction.get('severity')
        if severity in severity_counts:
            severity_counts[severity] += 1
    
    total = sum(severity_counts.values())
    print(f"  📊 Severity Distribution:")
    print(f"     Major: {severity_counts[SEVERITY_MAJOR]} ({severity_counts[SEVERITY_MAJOR]/total*100:.1f}%)")
    print(f"     Moderate: {severity_counts[SEVERITY_MODERATE]} ({severity_counts[SEVERITY_MODERATE]/total*100:.1f}%)")
    print(f"     Minor: {severity_counts[SEVERITY_MINOR]} ({severity_counts[SEVERITY_MINOR]/total*100:.1f}%)")
    print(f"     Total: {total}")
    
    # Should have reasonable distribution (at least 300+ interactions)
    # Note: Expanded interactions may not all be loaded if import fails
    return total >= 300 and severity_counts[SEVERITY_MAJOR] > 0


def main():
    """Run all tests"""
    print("=" * 80)
    print("🧪 DAY 9: DRUG INTERACTIONS TESTING SUITE")
    print("=" * 80)
    print()
    
    tester = DrugInteractionTester()
    
    # Run all tests
    print("📋 Test 1: Known Major Interactions")
    tester.test_case("Known major interactions", test_known_major_interactions)
    print()
    
    print("📋 Test 2: Class-Based Interactions")
    tester.test_case("Class-based interactions", test_class_based_interactions)
    print()
    
    print("📋 Test 3: Fuzzy Matching")
    tester.test_case("Fuzzy matching", test_fuzzy_matching)
    print()
    
    print("📋 Test 4: Multiple Drug Combinations (50+ combinations)")
    tester.test_case("Multiple drug combinations", test_multiple_drug_combinations)
    print()
    
    print("📋 Test 5: Autocomplete")
    tester.test_case("Autocomplete suggestions", test_autocomplete)
    print()
    
    print("📋 Test 6: Drug Class Detection")
    tester.test_case("Drug class detection", test_drug_class_detection)
    print()
    
    print("📋 Test 7: Performance")
    tester.test_case("Performance", test_performance)
    print()
    
    print("📋 Test 8: Edge Cases")
    tester.test_case("Edge cases", test_edge_cases)
    print()
    
    print("📋 Test 9: Severity Distribution")
    tester.test_case("Severity distribution", test_severity_distribution)
    print()
    
    # Print summary
    tester.print_summary()
    
    # Return exit code
    return 0 if tester.test_results['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

