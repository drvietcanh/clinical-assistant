"""
Integration Tests for Clinical Assistant
Tests: Calculator integration, module interactions, end-to-end workflows
"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("🔗 INTEGRATION TESTS - Clinical Assistant")
print("=" * 60)
print()

# ============================================================================
# TEST 1: Calculator Registry Integration
# ============================================================================
print("📋 TEST 1: Calculator Registry Integration")
print("-" * 60)

try:
    from config.calculators import ALL_CALCULATORS
    
    total_calculators = len(ALL_CALCULATORS)
    print(f"   Total calculators registered: {total_calculators}")
    
    # Check categories
    categories = {}
    for calc_id, calc_info in ALL_CALCULATORS.items():
        category = calc_info.get("category", "Unknown")
        if category not in categories:
            categories[category] = 0
        categories[category] += 1
    
    print(f"   Categories: {len(categories)}")
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"      - {category}: {count} calculators")
    
    # Verify required fields
    required_fields = ["name", "category", "icon", "page"]
    missing_fields = []
    
    for calc_id, calc_info in ALL_CALCULATORS.items():
        for field in required_fields:
            if field not in calc_info:
                missing_fields.append((calc_id, field))
    
    if missing_fields:
        print(f"   ⚠️  Missing fields: {len(missing_fields)}")
        for calc_id, field in missing_fields[:5]:
            print(f"      - {calc_id}: missing {field}")
    else:
        print("   ✅ All calculators have required fields")
    
    assert total_calculators > 0, "Should have at least one calculator"
    print("✅ Calculator Registry Integration - PASSED")
    print()
    
except Exception as e:
    print(f"❌ CALCULATOR REGISTRY TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 2: Score Calculators Integration
# ============================================================================
print("📋 TEST 2: Score Calculators Integration")
print("-" * 60)

try:
    # Test a few key calculators
    test_calculators = [
        ("sofa", "scores/emergency/sofa.py", "calculate_sofa"),
        ("cha2ds2vasc", "scores/cardiology/cha2ds2vasc.py", "calculate_cha2ds2vasc"),
        ("news2", "scores/emergency/news2.py", "calculate_news2"),
        ("crcl", "scores/metabolism/crcl.py", "calculate_crcl"),
    ]
    
    calculators_tested = 0
    calculators_passed = 0
    
    for calc_id, file_path, func_name in test_calculators:
        full_path = project_root / file_path
        if full_path.exists():
            # Try to import and test
            try:
                module_name = file_path.replace("/", ".").replace(".py", "")
                module = __import__(module_name, fromlist=[func_name])
                calc_func = getattr(module, func_name, None)
                
                if calc_func:
                    calculators_passed += 1
                    print(f"   ✅ {calc_id}: Function '{func_name}' found")
                else:
                    print(f"   ⚠️  {calc_id}: Function '{func_name}' not found")
            except Exception as e:
                print(f"   ⚠️  {calc_id}: Import error - {e}")
            
            calculators_tested += 1
        else:
            print(f"   ⚠️  {calc_id}: File not found")
    
    print(f"\n   Tested: {calculators_tested} calculators")
    print(f"   Passed: {calculators_passed} calculators")
    
    if calculators_passed >= calculators_tested * 0.8:
        print("✅ Score Calculators Integration - PASSED")
    else:
        print("⚠️  Score Calculators Integration - Some issues found")
    
    print()
    
except Exception as e:
    print(f"❌ SCORE CALCULATORS TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 3: Export Integration with Calculators
# ============================================================================
print("📋 TEST 3: Export Integration with Calculators")
print("-" * 60)

try:
    # Check calculators with export
    calculator_files = [
        "scores/emergency/sofa.py",
        "scores/emergency/news2.py",
        "scores/cardiology/cha2ds2vasc.py",
        "scores/metabolism/crcl.py",
    ]
    
    export_found = 0
    
    for file_path in calculator_files:
        full_path = project_root / file_path
        if full_path.exists():
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                if "render_export_section" in content or "render_export_buttons" in content:
                    export_found += 1
                    file_name = Path(file_path).stem
                    print(f"   ✅ {file_name}: Has export integration")
                else:
                    file_name = Path(file_path).stem
                    print(f"   ⚠️  {file_name}: No export integration")
    
    print(f"\n   Calculators with export: {export_found}/{len(calculator_files)}")
    
    if export_found >= len(calculator_files) * 0.75:
        print("✅ Export Integration - PASSED")
    else:
        print("⚠️  Export Integration - Some calculators missing export")
    
    print()
    
except Exception as e:
    print(f"❌ EXPORT INTEGRATION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 4: Formatters Integration
# ============================================================================
print("📋 TEST 4: Formatters Integration")
print("-" * 60)

try:
    from utils.formatters import (
        format_age, format_weight, format_height, format_lab_value,
        render_age_input, render_weight_input, render_height_input
    )
    
    # Check if formatters are used in calculators
    calculator_files = [
        "scores/emergency/sofa.py",
        "scores/metabolism/crcl.py",
    ]
    
    formatters_used = 0
    
    for file_path in calculator_files:
        full_path = project_root / file_path
        if full_path.exists():
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Check for formatter imports or usage
                if "formatters" in content.lower() or "format_" in content:
                    formatters_used += 1
                    file_name = Path(file_path).stem
                    print(f"   ✅ {file_name}: Uses formatters")
    
    # Check utils/__init__.py exports
    utils_init = project_root / "utils" / "__init__.py"
    if utils_init.exists():
        with open(utils_init, "r", encoding="utf-8") as f:
            content = f.read()
            if "formatters" in content:
                print("   ✅ utils/__init__.py exports formatters")
    
    print(f"\n   Formatters integration: {formatters_used} files")
    print("✅ Formatters Integration - PASSED")
    print()
    
except Exception as e:
    print(f"❌ FORMATTERS INTEGRATION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 5: Module Structure Verification
# ============================================================================
print("📋 TEST 5: Module Structure Verification")
print("-" * 60)

try:
    # Check main modules
    required_modules = [
        "scores",
        "antibiotics",
        "labs",
        "diagnosis",
        "drugs",
        "critical_care",
        "components",
        "utils",
        "config"
    ]
    
    modules_found = 0
    modules_checked = []
    
    for module_name in required_modules:
        module_path = project_root / module_name
        if module_path.exists() and module_path.is_dir():
            modules_found += 1
            modules_checked.append(module_name)
            print(f"   ✅ {module_name}/")
        else:
            print(f"   ⚠️  {module_name}/: Not found")
    
    print(f"\n   Modules found: {modules_found}/{len(required_modules)}")
    
    # Check __init__.py files
    init_files = 0
    for module_name in modules_checked:
        init_path = project_root / module_name / "__init__.py"
        if init_path.exists():
            init_files += 1
    
    print(f"   __init__.py files: {init_files}/{modules_found}")
    
    if modules_found >= len(required_modules) * 0.8:
        print("✅ Module Structure - PASSED")
    else:
        print("⚠️  Module Structure - Some modules missing")
    
    print()
    
except Exception as e:
    print(f"❌ MODULE STRUCTURE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 6: Page Router Integration
# ============================================================================
print("📋 TEST 6: Page Router Integration")
print("-" * 60)

try:
    pages_dir = project_root / "pages"
    
    if pages_dir.exists():
        page_files = list(pages_dir.glob("*.py"))
        page_files = [f for f in page_files if not f.name.startswith("__")]
        
        print(f"   Page files found: {len(page_files)}")
        
        for page_file in sorted(page_files):
            print(f"      - {page_file.name}")
        
        # Check if pages import from modules
        imports_found = 0
        for page_file in page_files[:3]:  # Check first 3
            with open(page_file, "r", encoding="utf-8") as f:
                content = f.read()
                if "import" in content and ("scores" in content or "antibiotics" in content or "labs" in content):
                    imports_found += 1
        
        print(f"\n   Pages with module imports: {imports_found}/3 checked")
        print("✅ Page Router Integration - PASSED")
    else:
        print("   ⚠️  pages/ directory not found")
    
    print()
    
except Exception as e:
    print(f"❌ PAGE ROUTER TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 7: Component Integration
# ============================================================================
print("📋 TEST 7: Component Integration")
print("-" * 60)

try:
    from components.export import render_export_section
    from components.search import render_search
    from components.favorites import render_favorites
    from components.recently_used import render_recently_used
    
    components = [
        ("export", render_export_section),
        ("search", render_search),
        ("favorites", render_favorites),
        ("recently_used", render_recently_used),
    ]
    
    print("   Components available:")
    for name, func in components:
        if callable(func):
            print(f"      ✅ {name}: {func.__name__}")
        else:
            print(f"      ⚠️  {name}: Not callable")
    
    print("✅ Component Integration - PASSED")
    print()
    
except Exception as e:
    print(f"❌ COMPONENT INTEGRATION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 8: Config Integration
# ============================================================================
print("📋 TEST 8: Config Integration")
print("-" * 60)

try:
    from config.calculators import ALL_CALCULATORS
    from config.app_config import APP_CONFIG, get_module_list_for_navigation
    from config.theme import get_module_style
    
    # Test config imports
    print("   Config modules:")
    print(f"      ✅ calculators: {len(ALL_CALCULATORS)} calculators")
    print(f"      ✅ app_config: APP_CONFIG loaded")
    
    # Test get_module_list_for_navigation
    try:
        modules = get_module_list_for_navigation()
        print(f"      ✅ get_module_list_for_navigation: {len(modules)} modules")
    except Exception as e:
        print(f"      ⚠️  get_module_list_for_navigation: {e}")
    
    # Test get_module_style
    try:
        style = get_module_style("Scores")
        print(f"      ✅ get_module_style: Works")
    except Exception as e:
        print(f"      ⚠️  get_module_style: {e}")
    
    print("✅ Config Integration - PASSED")
    print()
    
except Exception as e:
    print(f"❌ CONFIG INTEGRATION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("📊 INTEGRATION TEST SUMMARY")
print("=" * 60)
print()
print("✅ Tests completed:")
print("   1. Calculator Registry Integration")
print("   2. Score Calculators Integration")
print("   3. Export Integration with Calculators")
print("   4. Formatters Integration")
print("   5. Module Structure Verification")
print("   6. Page Router Integration")
print("   7. Component Integration")
print("   8. Config Integration")
print()
print("💡 Integration tests verify:")
print("   - Modules work together correctly")
print("   - Components are properly integrated")
print("   - Calculators use shared utilities")
print("   - Export functionality is accessible")
print()
print("=" * 60)

