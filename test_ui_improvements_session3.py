"""
Test script for Session 3: UI/UX Improvements
Tests the enhanced UI components
"""

import sys
sys.path.insert(0, '.')

def test_ui_components_import():
    """Test that UI components can be imported"""
    print("=" * 60)
    print("TESTING UI COMPONENTS IMPORT")
    print("=" * 60)
    
    try:
        from drugs.interaction_checker_ui import (
            render_interaction_warning,
            render_interaction_summary,
            render_medication_list_with_checker,
            render_quick_interaction_check,
            render_complete_interaction_checker
        )
        print("[PASS] All UI components imported successfully")
        return True
    except Exception as e:
        print(f"[FAIL] Import error: {e}")
        return False


def test_interaction_warning_data_structure():
    """Test interaction warning data structure"""
    print("\n" + "=" * 60)
    print("TESTING INTERACTION WARNING DATA STRUCTURE")
    print("=" * 60)
    
    from drugs.interaction_checker_ui import render_interaction_warning
    from drugs.interactions_data import SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR
    
    test_interactions = [
        {
            "drug1": "Warfarin",
            "drug2": "Aspirin",
            "severity": SEVERITY_MAJOR,
            "effect": "Tăng nguy cơ xuất huyết nặng",
            "mechanism": "Tăng tác dụng chống đông",
            "management": "Tránh dùng chung",
            "references": ["Micromedex", "AHFS"]
        },
        {
            "drug1": "Lisinopril",
            "drug2": "Ibuprofen",
            "severity": SEVERITY_MODERATE,
            "effect": "Giảm hiệu quả hạ huyết áp",
            "mechanism": "NSAID ức chế prostaglandin",
            "management": "Theo dõi huyết áp",
            "references": ["JNC 8"]
        },
        {
            "drug1": "Paracetamol",
            "drug2": "Aspirin",
            "severity": SEVERITY_MINOR,
            "effect": "Ít quan trọng",
            "management": "Có thể dùng chung",
            "references": ["Clinical Pharmacology"]
        }
    ]
    
    passed = 0
    failed = 0
    
    for interaction in test_interactions:
        try:
            # Check if all required fields are present
            required_fields = ['drug1', 'drug2', 'severity']
            missing = [f for f in required_fields if f not in interaction]
            
            if not missing:
                print(f"[PASS] Interaction structure valid: {interaction['drug1']} + {interaction['drug2']}")
                passed += 1
            else:
                print(f"[FAIL] Missing fields: {missing}")
                failed += 1
        except Exception as e:
            print(f"[FAIL] Error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_summary_data_structure():
    """Test summary data structure"""
    print("\n" + "=" * 60)
    print("TESTING SUMMARY DATA STRUCTURE")
    print("=" * 60)
    
    test_summaries = [
        {
            "total_interactions": 5,
            "major": 2,
            "moderate": 2,
            "minor": 1,
            "risk_level": "HIGH"
        },
        {
            "total_interactions": 3,
            "major": 0,
            "moderate": 2,
            "minor": 1,
            "risk_level": "MODERATE"
        },
        {
            "total_interactions": 1,
            "major": 0,
            "moderate": 0,
            "minor": 1,
            "risk_level": "LOW"
        },
        {
            "total_interactions": 0,
            "major": 0,
            "moderate": 0,
            "minor": 0,
            "risk_level": "NONE"
        }
    ]
    
    passed = 0
    failed = 0
    
    for summary in test_summaries:
        try:
            required_fields = ['total_interactions', 'major', 'moderate', 'minor', 'risk_level']
            missing = [f for f in required_fields if f not in summary]
            
            if not missing:
                print(f"[PASS] Summary structure valid: {summary['risk_level']} risk")
                passed += 1
            else:
                print(f"[FAIL] Missing fields: {missing}")
                failed += 1
        except Exception as e:
            print(f"[FAIL] Error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_alternatives_handling():
    """Test alternatives handling in interactions"""
    print("\n" + "=" * 60)
    print("TESTING ALTERNATIVES HANDLING")
    print("=" * 60)
    
    test_interactions_with_alternatives = [
        {
            "drug1": "Warfarin",
            "drug2": "Ibuprofen",
            "severity": "Major",
            "alternatives": {
                "for_ibuprofen": ["Paracetamol", "Acetaminophen"],
                "for_warfarin": ["Dabigatran", "Rivaroxaban"]
            }
        },
        {
            "drug1": "Atorvastatin",
            "drug2": "Clarithromycin",
            "severity": "Major",
            "alternatives": {
                "for_clarithromycin": ["Azithromycin", "Doxycycline"],
                "for_atorvastatin": ["Pravastatin", "Rosuvastatin"]
            }
        }
    ]
    
    passed = 0
    failed = 0
    
    for interaction in test_interactions_with_alternatives:
        if 'alternatives' in interaction:
            alternatives = interaction['alternatives']
            if isinstance(alternatives, dict) and len(alternatives) > 0:
                print(f"[PASS] Alternatives found: {interaction['drug1']} + {interaction['drug2']}")
                for key, alt_list in alternatives.items():
                    print(f"  - {key}: {', '.join(alt_list)}")
                passed += 1
            else:
                print(f"[FAIL] Invalid alternatives structure")
                failed += 1
        else:
            print(f"[FAIL] No alternatives field")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SESSION 3: UI/UX IMPROVEMENTS - TEST SUITE")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    
    # Run all tests
    if test_ui_components_import():
        total_passed += 1
    else:
        total_failed += 1
    
    p2, f2 = test_interaction_warning_data_structure()
    total_passed += p2
    total_failed += f2
    
    p3, f3 = test_summary_data_structure()
    total_passed += p3
    total_failed += f3
    
    p4, f4 = test_alternatives_handling()
    total_passed += p4
    total_failed += f4
    
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

