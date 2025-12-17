"""
Simple Test Script for Phase 1 & Phase 2 Features
Kiểm tra các tính năng đã implement (không cần Streamlit runtime)
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 80)
print("🧪 TEST PHASE 1 & PHASE 2 FEATURES (Simple)")
print("=" * 80)
print()

test_results = {"passed": [], "failed": [], "warnings": []}


def record_passed(name: str):
    test_results["passed"].append(name)
    print(f"✅ PASS: {name}")


def record_failed(name: str, error: str):
    test_results["failed"].append((name, error))
    print(f"❌ FAIL: {name}")
    print(f"   Error: {error}")


def record_warning(name: str, message: str):
    test_results["warnings"].append((name, message))
    print(f"⚠️  WARN: {name}: {message}")

# ========== PHASE 1 TESTS ==========
print("📋 PHASE 1: QUICK WINS")
print("-" * 80)

# 1. References Component
print("\n1. Testing References Component...")
try:
    from components.references import get_evidence_level_info, format_apa_citation, generate_pubmed_link
    
    level_info = get_evidence_level_info("I")
    assert level_info is not None and "color" in level_info
    
    pubmed_link = generate_pubmed_link("12345678")
    assert "pubmed" in pubmed_link.lower()
    
    citation = format_apa_citation("Test Author", 2020, "Test Title", "Test Journal", pmid="12345678")
    assert "Test Author" in citation
    
    record_passed("References Component")
except Exception as e:
    record_failed("References Component", str(e))

# 2. References Config
print("\n2. Testing References Config...")
try:
    from scores.references_config import get_references, has_references
    
    refs = get_references("CHA2DS2-VASc")
    assert isinstance(refs, list) and len(refs) > 0
    
    assert has_references("CHA2DS2-VASc") == True
    assert has_references("NonExistentCalc") == False
    
    record_passed("References Config")
except Exception as e:
    record_failed("References Config", str(e))

# 3. Share Results (without qrcode)
print("\n3. Testing Share Results (logic only)...")
try:
    from components.share_results import generate_share_id, generate_share_url
    
    share_id = generate_share_id("test_calc", {"input": 1}, {"result": 2})
    assert isinstance(share_id, str) and len(share_id) > 0
    
    url = generate_share_url("test_id")
    assert isinstance(url, str)
    
    record_passed("Share Results (logic)")
    record_warning("Share Results", "QR code test requires qrcode module")
except Exception as e:
    record_failed("Share Results", str(e))

# 4. Smart Suggestions
print("\n4. Testing Smart Suggestions...")
try:
    from components.smart_suggestions import (
        get_related_calculators,
        get_suggestions_by_category,
        get_popular_calculators
    )
    
    related = get_related_calculators("cha2ds2vasc", limit=5)
    assert isinstance(related, list) and len(related) > 0
    
    category_suggestions = get_suggestions_by_category("Tim Mạch", exclude_id="cha2ds2vasc", limit=5)
    assert isinstance(category_suggestions, list)
    
    popular = get_popular_calculators(limit=5)
    assert isinstance(popular, list) and len(popular) > 0
    
    record_passed("Smart Suggestions Component")
except Exception as e:
    record_failed("Smart Suggestions Component", str(e))

# 5. Calculation History (structure)
print("\n5. Testing Calculation History (structure)...")
try:
    import components.calculation_history as hist_module
    assert hasattr(hist_module, 'save_calculation_to_history')
    assert hasattr(hist_module, 'get_calculation_history')
    assert hasattr(hist_module, 'export_history')
    
    record_passed("Calculation History (structure)")
    record_warning("Calculation History", "Full test requires Streamlit session state")
except Exception as e:
    record_failed("Calculation History", str(e))

# ========== PHASE 2 TESTS ==========
print("\n\n📋 PHASE 2: CORE FEATURES")
print("-" * 80)

# 6. Flowcharts
print("\n6. Testing Flowcharts...")
try:
    from components.flowchart import FlowchartNode, FlowchartEdge, NodeType
    
    node = FlowchartNode("test", "Test Node", NodeType.START)
    assert node.id == "test" and node.node_type == NodeType.START
    
    edge = FlowchartEdge("from", "to", "label")
    assert edge.from_node == "from" and edge.to_node == "to"
    
    color = node.get_color()
    assert isinstance(color, str) and len(color) > 0
    
    record_passed("Flowchart Base Component")
except Exception as e:
    record_failed("Flowchart Base Component", str(e))

# 7. Clinical Rules Flowcharts
print("\n7. Testing Clinical Rules Flowcharts...")
try:
    from components.flowcharts.clinical_rules import (
        create_wells_pe_flowchart,
        create_perc_flowchart,
        create_cha2ds2vasc_flowchart,
        create_sepsis_flowchart,
        create_stroke_flowchart,
        create_aki_flowchart,
        create_curb65_flowchart
    )
    
    flowcharts = {
        "Wells PE": create_wells_pe_flowchart,
        "PERC": create_perc_flowchart,
        "CHA2DS2-VASc": create_cha2ds2vasc_flowchart,
        "Sepsis": create_sepsis_flowchart,
        "Stroke": create_stroke_flowchart,
        "AKI": create_aki_flowchart,
        "CURB-65": create_curb65_flowchart
    }
    
    for name, create_func in flowcharts.items():
        nodes, edges = create_func()
        assert isinstance(nodes, list) and len(nodes) > 0
        assert isinstance(edges, list) and len(edges) > 0
        
        node_ids = {node.id for node in nodes}
        for edge in edges:
            assert edge.from_node in node_ids, f"{name}: Invalid from_node '{edge.from_node}'"
            assert edge.to_node in node_ids, f"{name}: Invalid to_node '{edge.to_node}'"
    
    record_passed(f"Clinical Rules Flowcharts ({len(flowcharts)} algorithms)")
except Exception as e:
    record_failed("Clinical Rules Flowcharts", str(e))

# 8. Pregnancy & Lactation Safety
print("\n8. Testing Pregnancy & Lactation Safety...")
try:
    from drugs.pregnancy_lactation_safety import (
        get_pregnancy_safety,
        get_lactation_safety,
        get_safety_summary,
        PREGNANCY_SAFETY,
        LACTATION_SAFETY
    )
    
    assert len(PREGNANCY_SAFETY) > 0
    assert len(LACTATION_SAFETY) > 0
    
    preg_safety = get_pregnancy_safety("Paracetamol")
    assert preg_safety is not None and "fda_category" in preg_safety
    
    lact_safety = get_lactation_safety("Paracetamol")
    assert lact_safety is not None and "briggs_category" in lact_safety
    
    summary = get_safety_summary("Paracetamol")
    assert summary["has_data"] == True
    
    record_passed(f"Pregnancy & Lactation Safety ({len(PREGNANCY_SAFETY)} drugs)")
except Exception as e:
    record_failed("Pregnancy & Lactation Safety", str(e))

# 9. Pediatric Dosing Calculator
print("\n9. Testing Pediatric Dosing Calculator...")
try:
    from scores.pediatrics.pediatric_dosing import (
        calculate_weight_based_dose,
        calculate_bsa_based_dose,
        calculate_age_based_dose,
        get_pediatric_dosing_guidelines
    )
    
    # Test weight-based
    result = calculate_weight_based_dose(20.0, 10.0, max_dose=200.0, min_dose=50.0)
    assert result["calculated_dose"] == 200.0
    assert result["adjusted"] == True
    
    # Test BSA-based
    bsa_result = calculate_bsa_based_dose(20.0, 100.0, 100.0)
    assert bsa_result["calculated_dose"] > 0
    
    # Test age-based
    age_map = {(0, 1): 50.0, (1, 5): 100.0}
    age_result = calculate_age_based_dose(3.0, age_map)
    assert age_result["calculated_dose"] == 100.0
    
    # Test guidelines
    guidelines = get_pediatric_dosing_guidelines("Paracetamol")
    assert guidelines is not None
    
    record_passed("Pediatric Dosing Calculator")
except Exception as e:
    record_failed("Pediatric Dosing Calculator", str(e))

# ========== FILE EXISTENCE TESTS ==========
print("\n\n📋 FILE EXISTENCE TESTS")
print("-" * 80)

files_to_check = [
    ("components/share_results.py", "Share Results Component"),
    ("components/smart_suggestions.py", "Smart Suggestions Component"),
    ("components/calculation_history.py", "Calculation History Component"),
    ("components/flowcharts/clinical_rules.py", "Clinical Rules Flowcharts"),
    ("drugs/pregnancy_lactation_safety.py", "Pregnancy & Lactation Safety"),
    ("components/pregnancy_lactation_display.py", "Pregnancy & Lactation Display"),
    ("scores/pediatrics/pediatric_dosing.py", "Pediatric Dosing Calculator"),
    ("pages/10_📊_Phase2_Features.py", "Phase 2 Features Page"),
]

for file_path, name in files_to_check:
    print(f"\n10.{files_to_check.index((file_path, name)) + 1}. Checking {name}...")
    if Path(file_path).exists():
        record_passed(f"{name} file exists")
    else:
        record_failed(f"{name} file", "File not found")

# ========== INTEGRATION CHECKS ==========
print("\n\n📋 INTEGRATION CHECKS")
print("-" * 80)

# Check Phase 1 integration
print("\n11. Checking Phase 1 Integration...")
try:
    import inspect
    from scores.cardiology import cha2ds2vasc
    
    source = inspect.getsource(cha2ds2vasc.render)
    
    phase1_features = {
        "References": "render_references_section" in source,
        "History": "save_calculation_to_history" in source,
        "Share": "render_share_section" in source,
        "Suggestions": "render_suggestions" in source
    }
    
    integrated = sum(phase1_features.values())
    total = len(phase1_features)
    
    if integrated == total:
        record_passed(f"Phase 1 Integration in CHA2DS2-VASc ({integrated}/{total})")
    else:
        missing = [k for k, v in phase1_features.items() if not v]
        record_warning("Phase 1 Integration", f"CHA2DS2-VASc missing: {', '.join(missing)} ({integrated}/{total} integrated)")
except Exception as e:
    record_warning("Phase 1 Integration Check", f"Could not check: {str(e)}")

# Check Phase 2 page
print("\n12. Checking Phase 2 Features Page...")
try:
    page_path = Path("pages/10_📊_Phase2_Features.py")
    if page_path.exists():
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        phase2_features = {
            "Flowcharts": "create_wells_pe_flowchart" in content,
            "Pregnancy": "render_pregnancy_lactation_section" in content,
            "Pediatric": "render_pediatric_dosing_calculator" in content
        }
        
        if all(phase2_features.values()):
            record_passed("Phase 2 Features Page (all features)")
        else:
            missing = [k for k, v in phase2_features.items() if not v]
            record_warning("Phase 2 Features Page", f"Missing: {', '.join(missing)}")
    else:
        record_failed("Phase 2 Features Page", "File not found")
except Exception as e:
    record_failed("Phase 2 Features Page Check", str(e))

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
        print(f"     {error[:100]}...")

if test_results["warnings"]:
    print("\n⚠️  WARNINGS:")
    for name, message in test_results["warnings"]:
        print(f"   - {name}: {message}")

print("\n" + "=" * 80)

if failed == 0:
    print("🎉 ALL TESTS PASSED!")
    print("\n✅ Phase 1 & Phase 2 features are ready!")
else:
    print(f"⚠️  {failed} TEST(S) FAILED - Please check errors above")
    print("\n💡 Note: Some tests may require:")
    print("   - qrcode module: pip install qrcode Pillow")
    print("   - Streamlit runtime for full UI tests")

print("=" * 80)

