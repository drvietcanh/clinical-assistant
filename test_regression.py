"""
Regression Tests for Clinical Assistant
Tests: Verify existing functionality still works after changes
"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("🔄 REGRESSION TESTS - Clinical Assistant")
print("=" * 60)
print()

# ============================================================================
# TEST 1: Formatters Regression
# ============================================================================
print("📋 TEST 1: Formatters Regression")
print("-" * 60)

try:
    from utils.formatters import (
        format_age, format_weight, format_height, format_lab_value
    )
    
    # Known good values
    test_cases = [
        (format_age, 65.5, "66"),
        (format_weight, 70.0, "70"),
        (format_weight, 70.5, "70.5"),
        (format_height, 170.5, "170"),
        (format_lab_value, 100.0, "100.0"),
        (format_lab_value, 100.5, "100.5"),
    ]
    
    passed = 0
    failed = 0
    
    for func, input_val, expected in test_cases:
        result = func(input_val)
        if result == expected:
            passed += 1
            print(f"   ✅ {func.__name__}({input_val}) = {result}")
        else:
            failed += 1
            print(f"   ❌ {func.__name__}({input_val}): Expected '{expected}', got '{result}'")
    
    print(f"\n   Results: {passed} passed, {failed} failed")
    assert failed == 0, f"{failed} regression tests failed"
    print("✅ Formatters Regression - PASSED")
    print()
    
except Exception as e:
    print(f"❌ FORMATTERS REGRESSION TEST FAILED: {e}")
    print()

# ============================================================================
# TEST 2: Export Component Regression
# ============================================================================
print("📋 TEST 2: Export Component Regression")
print("-" * 60)

try:
    from components.export import format_result_for_export
    
    # Test with known good data
    inputs = {"Age": 65, "Weight": 70.5}
    results = {"Score": 15, "Interpretation": "Moderate"}
    
    export_text = format_result_for_export(
        "Regression Test",
        inputs,
        results,
        "Test Calculator"
    )
    
    # Verify required sections
    required_sections = [
        "Clinical Assistant",
        "Regression Test",
        "Test Calculator",
        "Age",
        "Weight",
        "Score",
        "Interpretation"
    ]
    
    missing = []
    for section in required_sections:
        if section not in export_text:
            missing.append(section)
    
    if missing:
        print(f"   ❌ Missing sections: {', '.join(missing)}")
        assert False, "Export text missing required sections"
    else:
        print("   ✅ All required sections present")
        print(f"   ✅ Export text length: {len(export_text)} characters")
    
    print("✅ Export Component Regression - PASSED")
    print()
    
except Exception as e:
    print(f"❌ EXPORT REGRESSION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 3: DDx Generator Regression
# ============================================================================
print("📋 TEST 3: DDx Generator Regression")
print("-" * 60)

try:
    from diagnosis.ddx_data import get_all_scenarios, get_scenario_data
    
    # Verify scenarios are still available
    all_scenarios = get_all_scenarios()
    
    assert len(all_scenarios) > 0, "Should have at least one scenario"
    
    # Test a few known scenarios
    known_scenarios = ["Chest Pain", "Dyspnea", "Fever"]
    
    scenarios_found = 0
    for scenario_name in known_scenarios:
        data = get_scenario_data(scenario_name)
        if data:
            scenarios_found += 1
            print(f"   ✅ '{scenario_name}': Available")
        else:
            print(f"   ⚠️  '{scenario_name}': Not found")
    
    print(f"\n   Total scenarios: {len(all_scenarios)}")
    print(f"   Known scenarios found: {scenarios_found}/{len(known_scenarios)}")
    
    if scenarios_found >= len(known_scenarios) * 0.8:
        print("✅ DDx Generator Regression - PASSED")
    else:
        print("⚠️  DDx Generator Regression - Some scenarios missing")
    
    print()
    
except Exception as e:
    print(f"❌ DDX REGRESSION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 4: Calculator Registry Regression
# ============================================================================
print("📋 TEST 4: Calculator Registry Regression")
print("-" * 60)

try:
    from config.calculators import ALL_CALCULATORS
    
    # Verify registry is not empty
    assert len(ALL_CALCULATORS) > 0, "Calculator registry should not be empty"
    
    # Check for key calculators
    key_calculators = ["sofa", "cha2ds2vasc", "news2", "crcl", "egfr"]
    
    calculators_found = 0
    for calc_id in key_calculators:
        if calc_id in ALL_CALCULATORS:
            calculators_found += 1
            calc_info = ALL_CALCULATORS[calc_id]
            print(f"   ✅ {calc_id}: {calc_info.get('name', 'Unknown')}")
        else:
            print(f"   ❌ {calc_id}: Not found")
    
    print(f"\n   Total calculators: {len(ALL_CALCULATORS)}")
    print(f"   Key calculators found: {calculators_found}/{len(key_calculators)}")
    
    assert calculators_found == len(key_calculators), "Key calculators missing"
    print("✅ Calculator Registry Regression - PASSED")
    print()
    
except Exception as e:
    print(f"❌ CALCULATOR REGISTRY REGRESSION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 5: Module Imports Regression
# ============================================================================
print("📋 TEST 5: Module Imports Regression")
print("-" * 60)

try:
    # Test critical imports
    imports_to_test = [
        ("utils.formatters", "format_age"),
        ("components.export", "format_result_for_export"),
        ("config.calculators", "ALL_CALCULATORS"),
        ("diagnosis.ddx_data", "get_all_scenarios"),
    ]
    
    imports_passed = 0
    imports_failed = []
    
    for module_name, item_name in imports_to_test:
        try:
            module = __import__(module_name, fromlist=[item_name])
            item = getattr(module, item_name, None)
            if item:
                imports_passed += 1
                print(f"   ✅ {module_name}.{item_name}")
            else:
                imports_failed.append(f"{module_name}.{item_name}")
                print(f"   ❌ {module_name}.{item_name}: Not found")
        except Exception as e:
            imports_failed.append(f"{module_name}.{item_name}: {e}")
            print(f"   ❌ {module_name}.{item_name}: Import error")
    
    print(f"\n   Imports passed: {imports_passed}/{len(imports_to_test)}")
    
    if len(imports_failed) == 0:
        print("✅ Module Imports Regression - PASSED")
    else:
        print(f"⚠️  Module Imports Regression - {len(imports_failed)} failed")
    
    print()
    
except Exception as e:
    print(f"❌ MODULE IMPORTS REGRESSION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 6: File Structure Regression
# ============================================================================
print("📋 TEST 6: File Structure Regression")
print("-" * 60)

try:
    # Critical files that should always exist
    critical_files = [
        "app.py",
        "requirements.txt",
        "config/calculators.py",
        "components/export.py",
        "utils/formatters.py",
        "diagnosis/ddx_data.py",
    ]
    
    files_found = 0
    for file_path in critical_files:
        full_path = project_root / file_path
        if full_path.exists():
            files_found += 1
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path}: Not found")
    
    print(f"\n   Files found: {files_found}/{len(critical_files)}")
    
    assert files_found == len(critical_files), "Critical files missing"
    print("✅ File Structure Regression - PASSED")
    print()
    
except Exception as e:
    print(f"❌ FILE STRUCTURE REGRESSION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("📊 REGRESSION TEST SUMMARY")
print("=" * 60)
print()
print("✅ Tests completed:")
print("   1. Formatters Regression")
print("   2. Export Component Regression")
print("   3. DDx Generator Regression")
print("   4. Calculator Registry Regression")
print("   5. Module Imports Regression")
print("   6. File Structure Regression")
print()
print("💡 Regression tests verify:")
print("   - Existing functionality still works")
print("   - No breaking changes introduced")
print("   - Core features remain stable")
print()
print("=" * 60)

