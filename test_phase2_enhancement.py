"""
Phase 2: Enhanced Drug Database - Test Suite
Tests for enhancement utilities and analyzer
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_utils.enhanced_fields_template import (
    get_enhanced_fields_list,
    check_drug_enhancement_status,
    get_priority_fields,
    get_safety_fields,
    get_special_population_fields,
    ENHANCED_FIELDS_TEMPLATE,
)
from drugs.drug_utils.enhancement_analyzer import (
    analyze_drug_database,
    get_enhancement_priority_list,
)
from drugs.drug_database import DRUG_DATABASE


class EnhancementTester:
    """Test suite for enhancement utilities"""
    
    def __init__(self):
        self.test_results = {
            'passed': 0,
            'failed': 0,
            'total': 0
        }
        self.failed_tests = []
    
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
            import traceback
            traceback.print_exc()
            return False
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 80)
        print("📊 TEST SUMMARY")
        print("=" * 80)
        print(f"Total Tests: {self.test_results['total']}")
        print(f"✅ Passed: {self.test_results['passed']}")
        print(f"❌ Failed: {self.test_results['failed']}")
        if self.test_results['total'] > 0:
            print(f"Success Rate: {(self.test_results['passed'] / self.test_results['total'] * 100):.1f}%")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"  - {test}")


# Test Cases

def test_enhanced_fields_list():
    """Test 1: Enhanced fields list should be non-empty"""
    fields = get_enhanced_fields_list()
    return len(fields) > 0 and isinstance(fields, list)


def test_template_structure():
    """Test 2: Template structure should be valid"""
    return isinstance(ENHANCED_FIELDS_TEMPLATE, dict) and len(ENHANCED_FIELDS_TEMPLATE) > 0


def test_check_drug_status():
    """Test 3: Check drug enhancement status should work"""
    # Test with a drug that has some fields (Captopril)
    test_drug = {
        "name": "Test Drug",
        "mechanism_of_action": "Test mechanism",
        "pharmacokinetics": {"half_life": "2 hours"},
        "monitoring": ["Test monitoring"],
    }
    
    status = check_drug_enhancement_status(test_drug)
    return (
        isinstance(status, dict) and
        "total_fields" in status and
        "present_fields" in status and
        "missing_fields" in status and
        status["total_fields"] > 0
    )


def test_priority_fields():
    """Test 4: Priority fields should be returned"""
    fields = get_priority_fields()
    return len(fields) > 0 and all(isinstance(f, str) for f in fields)


def test_safety_fields():
    """Test 5: Safety fields should be returned"""
    fields = get_safety_fields()
    return len(fields) > 0 and all(isinstance(f, str) for f in fields)


def test_special_population_fields():
    """Test 6: Special population fields should be returned"""
    fields = get_special_population_fields()
    return len(fields) > 0 and all(isinstance(f, str) for f in fields)


def test_analyze_database():
    """Test 7: Database analysis should work"""
    analysis = analyze_drug_database(DRUG_DATABASE)
    return (
        isinstance(analysis, dict) and
        "total_drugs" in analysis and
        "drugs_analyzed" in analysis and
        analysis["total_drugs"] > 0
    )


def test_priority_list():
    """Test 8: Priority list should be generated"""
    priority_list = get_enhancement_priority_list(DRUG_DATABASE, top_n=10)
    return (
        isinstance(priority_list, list) and
        len(priority_list) > 0 and
        all(len(item) == 3 for item in priority_list)  # (name, score, missing_fields)
    )


def test_captopril_enhancement():
    """Test 9: Captopril should have high completeness"""
    # Get Captopril from database
    if "Captopril" in DRUG_DATABASE:
        captopril = DRUG_DATABASE["Captopril"]
        status = check_drug_enhancement_status(captopril)
        # Captopril should have many fields (it's one of the enhanced ones)
        return status["completeness_percent"] >= 50
    return False


def test_missing_fields_detection():
    """Test 10: Missing fields should be detected correctly"""
    test_drug = {
        "name": "Test Drug",
        # Missing most fields
    }
    status = check_drug_enhancement_status(test_drug)
    return (
        len(status["missing_fields"]) > 0 and
        status["completeness_percent"] < 50
    )


def main():
    """Run all tests"""
    print("=" * 80)
    print("🧪 PHASE 2: ENHANCEMENT UTILITIES TEST SUITE")
    print("=" * 80)
    print()
    
    tester = EnhancementTester()
    
    # Run all tests
    print("📋 Test 1: Enhanced Fields List")
    tester.test_case("Enhanced fields list", test_enhanced_fields_list)
    print()
    
    print("📋 Test 2: Template Structure")
    tester.test_case("Template structure", test_template_structure)
    print()
    
    print("📋 Test 3: Check Drug Status")
    tester.test_case("Check drug enhancement status", test_check_drug_status)
    print()
    
    print("📋 Test 4: Priority Fields")
    tester.test_case("Priority fields", test_priority_fields)
    print()
    
    print("📋 Test 5: Safety Fields")
    tester.test_case("Safety fields", test_safety_fields)
    print()
    
    print("📋 Test 6: Special Population Fields")
    tester.test_case("Special population fields", test_special_population_fields)
    print()
    
    print("📋 Test 7: Database Analysis")
    tester.test_case("Database analysis", test_analyze_database)
    print()
    
    print("📋 Test 8: Priority List")
    tester.test_case("Priority list generation", test_priority_list)
    print()
    
    print("📋 Test 9: Captopril Enhancement")
    tester.test_case("Captopril has high completeness", test_captopril_enhancement)
    print()
    
    print("📋 Test 10: Missing Fields Detection")
    tester.test_case("Missing fields detection", test_missing_fields_detection)
    print()
    
    # Print summary
    tester.print_summary()
    
    # Return exit code
    return 0 if tester.test_results['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

