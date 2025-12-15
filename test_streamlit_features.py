"""
Test Script for Streamlit App - Phase 1 & Phase 2 Features
Kiểm tra các components có thể import và render được trong Streamlit
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 80)
print("🧪 STREAMLIT APP TEST - PHASE 1 & PHASE 2")
print("=" * 80)
print()

test_results = {"passed": [], "failed": [], "warnings": []}

def test_passed(name: str):
    test_results["passed"].append(name)
    print(f"✅ PASS: {name}")

def test_failed(name: str, error: str):
    test_results["failed"].append((name, error))
    print(f"❌ FAIL: {name}")
    print(f"   Error: {error}")

def test_warning(name: str, message: str):
    test_results["warnings"].append((name, message))
    print(f"⚠️  WARN: {name}: {message}")

# ========== TEST IMPORTS ==========
print("📋 TESTING IMPORTS")
print("-" * 80)

# Test Phase 1 imports
print("\n1. Testing Phase 1 Components...")
try:
    from components.references import render_references_section, get_evidence_level_info
    from components.share_results import render_share_section, generate_qr_code
    from components.smart_suggestions import render_suggestions, get_related_calculators
    from components.calculation_history import render_history_ui, save_calculation_to_history
    test_passed("Phase 1 Components Import")
except Exception as e:
    test_failed("Phase 1 Components Import", str(e))

# Test Phase 2 imports
print("\n2. Testing Phase 2 Components...")
try:
    from components.flowchart import render_flowchart, FlowchartNode, FlowchartEdge, NodeType
    from components.flowcharts.clinical_rules import (
        create_wells_pe_flowchart,
        create_perc_flowchart,
        create_cha2ds2vasc_flowchart
    )
    from components.pregnancy_lactation_display import render_pregnancy_lactation_section
    from scores.pediatrics.pediatric_dosing import render_pediatric_dosing_calculator
    test_passed("Phase 2 Components Import")
except Exception as e:
    test_failed("Phase 2 Components Import", str(e))

# Test Page imports
print("\n3. Testing Page Files...")
try:
    # Check if Phase 2 page exists and can be imported
    page_path = Path("pages/10_📊_Phase2_Features.py")
    if page_path.exists():
        # Try to read and check structure
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "render_pediatric_dosing_calculator" in content:
                test_passed("Phase 2 Features Page Structure")
            else:
                test_warning("Phase 2 Features Page", "Missing some imports")
    else:
        test_failed("Phase 2 Features Page", "File not found")
except Exception as e:
    test_failed("Phase 2 Features Page Check", str(e))

# Test Calculator integrations
print("\n4. Testing Calculator Integrations...")
try:
    from scores.cardiology import cha2ds2vasc
    from scores.emergency import sofa
    from scores.neurology import gcs
    
    # Check if they have Phase 1 imports
    import inspect
    
    cha2ds2vasc_source = inspect.getsource(cha2ds2vasc.render)
    sofa_source = inspect.getsource(sofa.render)
    gcs_source = inspect.getsource(gcs.render)
    
    integrated_features = {
        "CHA2DS2-VASc": {
            "references": "render_references_section" in cha2ds2vasc_source,
            "history": "save_calculation_to_history" in cha2ds2vasc_source,
            "share": "render_share_section" in cha2ds2vasc_source,
            "suggestions": "render_suggestions" in cha2ds2vasc_source
        },
        "SOFA": {
            "references": "render_references_section" in sofa_source,
            "history": "save_calculation_to_history" in sofa_source,
            "share": "render_share_section" in sofa_source,
            "suggestions": "render_suggestions" in sofa_source
        },
        "GCS": {
            "references": "render_references_section" in gcs_source,
            "history": "save_calculation_to_history" in gcs_source,
            "share": "render_share_section" in gcs_source,
            "suggestions": "render_suggestions" in gcs_source
        }
    }
    
    for calc_name, features in integrated_features.items():
        integrated_count = sum(features.values())
        total = len(features)
        if integrated_count == total:
            test_passed(f"{calc_name} Integration ({integrated_count}/{total})")
        else:
            missing = [k for k, v in features.items() if not v]
            test_warning(f"{calc_name} Integration", f"Missing: {', '.join(missing)} ({integrated_count}/{total})")
except Exception as e:
    test_failed("Calculator Integration Check", str(e))

# ========== TEST FUNCTIONALITY ==========
print("\n\n📋 TESTING FUNCTIONALITY")
print("-" * 80)

# Test QR code generation
print("\n5. Testing QR Code Generation...")
try:
    from components.share_results import generate_qr_code
    qr_image = generate_qr_code("test_data_12345")
    assert isinstance(qr_image, str)
    assert len(qr_image) > 0
    # Should be base64 encoded image
    assert "data:image" in qr_image.lower() or qr_image.startswith("data:")
    test_passed("QR Code Generation")
except Exception as e:
    test_failed("QR Code Generation", str(e))

# Test Flowchart creation
print("\n6. Testing Flowchart Creation...")
try:
    from components.flowcharts.clinical_rules import create_wells_pe_flowchart
    nodes, edges = create_wells_pe_flowchart()
    assert len(nodes) > 0
    assert len(edges) > 0
    # Check all edges reference valid nodes
    node_ids = {node.id for node in nodes}
    for edge in edges:
        assert edge.from_node in node_ids
        assert edge.to_node in node_ids
    test_passed("Flowchart Creation (Wells PE)")
except Exception as e:
    test_failed("Flowchart Creation", str(e))

# Test Pregnancy Safety
print("\n7. Testing Pregnancy Safety Database...")
try:
    from drugs.pregnancy_lactation_safety import get_pregnancy_safety, get_lactation_safety
    preg = get_pregnancy_safety("Paracetamol")
    lact = get_lactation_safety("Paracetamol")
    assert preg is not None
    assert lact is not None
    assert "fda_category" in preg
    assert "briggs_category" in lact
    test_passed("Pregnancy & Lactation Safety Database")
except Exception as e:
    test_failed("Pregnancy & Lactation Safety", str(e))

# Test Pediatric Dosing
print("\n8. Testing Pediatric Dosing Calculator...")
try:
    from scores.pediatrics.pediatric_dosing import (
        calculate_weight_based_dose,
        calculate_bsa_based_dose,
        get_pediatric_dosing_guidelines
    )
    
    # Test weight-based
    result = calculate_weight_based_dose(20.0, 10.0, max_dose=200.0)
    assert result["calculated_dose"] == 200.0
    
    # Test BSA-based
    bsa_result = calculate_bsa_based_dose(20.0, 100.0, 100.0)
    assert bsa_result["calculated_dose"] > 0
    
    # Test guidelines
    guidelines = get_pediatric_dosing_guidelines("Paracetamol")
    assert guidelines is not None
    
    test_passed("Pediatric Dosing Calculator")
except Exception as e:
    test_failed("Pediatric Dosing Calculator", str(e))

# ========== TEST APP STRUCTURE ==========
print("\n\n📋 TESTING APP STRUCTURE")
print("-" * 80)

# Check app.py exists
print("\n9. Checking App Structure...")
try:
    app_path = Path("app.py")
    if app_path.exists():
        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Check for Phase 1/2 related imports or usage
            if "Phase" in content or "phase" in content.lower():
                test_passed("App.py Structure")
            else:
                test_warning("App.py", "May not reference Phase features directly")
    else:
        test_failed("App.py", "File not found")
except Exception as e:
    test_failed("App Structure Check", str(e))

# Check config
print("\n10. Checking Config...")
try:
    from config.app_config import APP_CONFIG, get_module_info
    phase2_module = get_module_info("phase2_features")
    if phase2_module:
        test_passed("Phase 2 Module in Config")
    else:
        test_warning("Config", "Phase 2 module not found in config")
except Exception as e:
    test_failed("Config Check", str(e))

# ========== SUMMARY ==========
print("\n" + "=" * 80)
print("📊 TEST SUMMARY")
print("=" * 80)

total = len(test_results["passed"]) + len(test_results["failed"])
passed = len(test_results["passed"])
failed = len(test_results["failed"])
warnings = len(test_results["warnings"])

print(f"\n✅ Passed: {passed}/{total} ({passed*100//total if total > 0 else 0}%)")
print(f"❌ Failed: {failed}/{total}")
print(f"⚠️  Warnings: {warnings}")

if test_results["failed"]:
    print("\n❌ FAILED TESTS:")
    for name, error in test_results["failed"]:
        print(f"   - {name}")
        if len(error) > 100:
            print(f"     {error[:100]}...")
        else:
            print(f"     {error}")

if test_results["warnings"]:
    print("\n⚠️  WARNINGS:")
    for name, message in test_results["warnings"]:
        print(f"   - {name}: {message}")

print("\n" + "=" * 80)

if failed == 0:
    print("🎉 ALL TESTS PASSED!")
    print("\n✅ Streamlit app components are ready!")
    print("\n📝 Next Steps:")
    print("   1. Run: streamlit run app.py")
    print("   2. Navigate to Phase 2 Features page")
    print("   3. Test all features in browser")
else:
    print(f"⚠️  {failed} TEST(S) FAILED")
    print("\n💡 Please check errors above before running Streamlit app")

print("=" * 80)

