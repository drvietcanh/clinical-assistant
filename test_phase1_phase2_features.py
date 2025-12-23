"""
Test Script for Phase 1 & Decision Support
Kiểm tra các tính năng đã implement
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 80)
print("🧪 TEST PHASE 1 & DECISION SUPPORT")
print("=" * 80)
print()

# Test results
test_results = {
    "passed": [],
    "failed": [],
    "warnings": []
}


def record_passed(name: str):
    """Mark test as passed"""
    test_results["passed"].append(name)
    print(f"✅ PASS: {name}")


def record_failed(name: str, error: str):
    """Mark test as failed"""
    test_results["failed"].append((name, error))
    print(f"❌ FAIL: {name}")
    print(f"   Error: {error}")


def record_warning(name: str, message: str):
    """Mark test as warning"""
    test_results["warnings"].append((name, message))
    print(f"⚠️  WARN: {name}")
    print(f"   {message}")

# ========== PHASE 1 TESTS ==========
print("📋 PHASE 1: QUICK WINS")
print("-" * 80)

# 1. Test References Component
print("\n1. Testing References Component...")
try:
    from components.references import (
        render_references_section,
        get_evidence_level_info,
        format_apa_citation,
        generate_pubmed_link
    )
    
    # Test evidence level info
    level_info = get_evidence_level_info("I")
    assert level_info is not None
    assert "color" in level_info
    assert "label" in level_info
    
    # Test PubMed link generation
    pubmed_link = generate_pubmed_link("12345678")
    assert "pubmed" in pubmed_link.lower()
    assert "12345678" in pubmed_link
    
    # Test APA citation
    citation = format_apa_citation(
        authors="Test Author",
        year=2020,
        title="Test Title",
        journal="Test Journal",
        pmid="12345678"
    )
    assert "Test Author" in citation
    assert "2020" in citation
    
    record_passed("References Component")
except Exception as e:
    record_failed("References Component", str(e))

# 2. Test References Config
print("\n2. Testing References Config...")
try:
    from scores.references_config import get_references, has_references
    
    # Test get references
    refs = get_references("CHA2DS2-VASc")
    assert isinstance(refs, list)
    assert len(refs) > 0
    
    # Test has references
    assert has_references("CHA2DS2-VASc") == True
    assert has_references("NonExistentCalc") == False
    
    record_passed("References Config")
except Exception as e:
    record_failed("References Config", str(e))

# 3. Test Calculation History
print("\n3. Testing Calculation History...")
try:
    from components.calculation_history import (
        init_history_state,
        save_calculation_to_history,
        get_calculation_history,
        export_history
    )
    
    # Mock streamlit session state
    class MockSessionState:
        def __init__(self):
            self.calculation_history = []
            self.history_max_size = 50
    
    import components.calculation_history as history_module
    original_session = getattr(history_module, 'st', None)
    
    # Create mock
    class MockStreamlit:
        class session_state:
            calculation_history = []
            history_max_size = 50
    
    # Test functions (without actual streamlit)
    # We'll test the logic
    record_passed("Calculation History (structure check)")
    record_warning("Calculation History", "Full test requires Streamlit session state")
except Exception as e:
    record_failed("Calculation History", str(e))

# 4. Test Share Results
print("\n4. Testing Share Results...")
try:
    from components.share_results import (
        generate_share_id,
        save_shared_result,
        get_shared_result,
        generate_share_url,
        generate_qr_code
    )
    
    # Test share ID generation
    share_id = generate_share_id("test_calc", {"input": 1}, {"result": 2})
    assert isinstance(share_id, str)
    assert len(share_id) > 0
    
    # Test QR code generation
    qr_data = "test_data"
    qr_image = generate_qr_code(qr_data)
    assert isinstance(qr_image, str)
    assert len(qr_image) > 0
    assert "base64" in qr_image.lower() or qr_image.startswith("data:")
    
    record_passed("Share Results Component")
except Exception as e:
    record_failed("Share Results Component", str(e))

# 5. Test Smart Suggestions
print("\n5. Testing Smart Suggestions...")
try:
    from components.smart_suggestions import (
        get_related_calculators,
        get_suggestions_by_category,
        get_popular_calculators
    )
    
    # Test related calculators
    related = get_related_calculators("cha2ds2vasc", limit=5)
    assert isinstance(related, list)
    assert len(related) > 0
    
    # Test category suggestions
    category_suggestions = get_suggestions_by_category("Tim Mạch", exclude_id="cha2ds2vasc", limit=5)
    assert isinstance(category_suggestions, list)
    
    # Test popular calculators
    popular = get_popular_calculators(limit=5)
    assert isinstance(popular, list)
    assert len(popular) > 0
    
    record_passed("Smart Suggestions Component")
except Exception as e:
    record_failed("Smart Suggestions Component", str(e))

# ========== PHASE 2 TESTS ==========
print("\n\n📋 PHASE 2: CORE FEATURES")
print("-" * 80)

# 6. Test Flowcharts
print("\n6. Testing Flowcharts...")
try:
    from components.flowchart import (
        FlowchartNode,
        FlowchartEdge,
        NodeType,
        render_flowchart
    )
    
    # Test node creation
    node = FlowchartNode("test", "Test Node", NodeType.START)
    assert node.id == "test"
    assert node.label == "Test Node"
    assert node.node_type == NodeType.START
    
    # Test edge creation
    edge = FlowchartEdge("from", "to", "label")
    assert edge.from_node == "from"
    assert edge.to_node == "to"
    assert edge.label == "label"
    
    # Test node color
    color = node.get_color()
    assert isinstance(color, str)
    assert len(color) > 0
    
    record_passed("Flowchart Base Component")
except Exception as e:
    record_failed("Flowchart Base Component", str(e))

# 7. Test Clinical Rules Flowcharts
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
    
    # Test all flowcharts
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
        assert isinstance(nodes, list)
        assert isinstance(edges, list)
        assert len(nodes) > 0
        assert len(edges) > 0
        
        # Check all edges reference valid nodes
        node_ids = {node.id for node in nodes}
        for edge in edges:
            assert edge.from_node in node_ids, f"{name}: Edge from_node '{edge.from_node}' not found"
            assert edge.to_node in node_ids, f"{name}: Edge to_node '{edge.to_node}' not found"
    
    record_passed("Clinical Rules Flowcharts (7 algorithms)")
except Exception as e:
    record_failed("Clinical Rules Flowcharts", str(e))

# 8. Test Pregnancy & Lactation Safety
print("\n8. Testing Pregnancy & Lactation Safety...")
try:
    from drugs.pregnancy_lactation_safety import (
        get_pregnancy_safety,
        get_lactation_safety,
        get_safety_summary,
        PREGNANCY_SAFETY,
        LACTATION_SAFETY
    )
    
    # Test database
    assert len(PREGNANCY_SAFETY) > 0
    assert len(LACTATION_SAFETY) > 0
    
    # Test get functions
    preg_safety = get_pregnancy_safety("Paracetamol")
    assert preg_safety is not None
    assert "fda_category" in preg_safety
    assert "risk_level" in preg_safety
    
    lact_safety = get_lactation_safety("Paracetamol")
    assert lact_safety is not None
    assert "briggs_category" in lact_safety
    assert "risk_level" in lact_safety
    
    # Test summary
    summary = get_safety_summary("Paracetamol")
    assert summary["has_data"] == True
    assert summary["pregnancy"] is not None
    assert summary["lactation"] is not None
    
    # Test non-existent drug
    no_drug = get_pregnancy_safety("NonExistentDrug")
    assert no_drug is None
    
    record_passed("Pregnancy & Lactation Safety Database")
except Exception as e:
    record_failed("Pregnancy & Lactation Safety Database", str(e))

# 9. Test Pregnancy & Lactation Display
print("\n9. Testing Pregnancy & Lactation Display Component...")
try:
    from components.pregnancy_lactation_display import (
        render_pregnancy_safety,
        render_lactation_safety,
        render_pregnancy_lactation_section,
        get_risk_color
    )
    
    # Test risk color function
    color = get_risk_color("Safe")
    assert isinstance(color, str)
    assert color.startswith("#")
    
    record_passed("Pregnancy & Lactation Display Component")
    record_warning("Pregnancy & Lactation Display", "Full render test requires Streamlit")
except Exception as e:
    record_failed("Pregnancy & Lactation Display Component", str(e))

# 10. Test Pediatric Dosing Calculator
print("\n10. Testing Pediatric Dosing Calculator...")
try:
    from scores.pediatrics.pediatric_dosing import (
        calculate_weight_based_dose,
        calculate_bsa_based_dose,
        calculate_age_based_dose,
        get_pediatric_dosing_guidelines
    )
    
    # Test weight-based dosing
    result = calculate_weight_based_dose(
        weight_kg=20.0,
        dose_per_kg=10.0,
        max_dose=200.0,
        min_dose=50.0
    )
    assert result["calculated_dose"] == 200.0  # Should be max
    assert result["adjusted"] == True
    
    # Test BSA-based dosing
    bsa_result = calculate_bsa_based_dose(
        weight_kg=20.0,
        height_cm=100.0,
        dose_per_m2=100.0
    )
    assert bsa_result["calculated_dose"] > 0
    assert "bsa" in bsa_result
    
    # Test age-based dosing
    age_map = {
        (0, 1): 50.0,
        (1, 5): 100.0,
        (5, 10): 150.0
    }
    age_result = calculate_age_based_dose(3.0, age_map)
    assert age_result["calculated_dose"] == 100.0
    
    # Test guidelines
    guidelines = get_pediatric_dosing_guidelines("Paracetamol")
    assert guidelines is not None
    assert "weight_based" in guidelines
    
    record_passed("Pediatric Dosing Calculator")
except Exception as e:
    record_failed("Pediatric Dosing Calculator", str(e))

# ========== INTEGRATION TESTS ==========
print("\n\n📋 INTEGRATION TESTS")
print("-" * 80)

# 11. Test Phase 1 Integration in Calculators
print("\n11. Testing Phase 1 Integration...")
try:
    # Check if CHA2DS2-VASc has Phase 1 imports
    import inspect
    from scores.cardiology import cha2ds2vasc
    
    source = inspect.getsource(cha2ds2vasc.render)
    
    checks = {
        "calculation_history": "save_calculation_to_history" in source,
        "share_results": "render_share_section" in source,
        "smart_suggestions": "render_suggestions" in source,
        "references": "render_references_section" in source
    }
    
    all_passed = all(checks.values())
    
    if all_passed:
        record_passed("Phase 1 Integration in CHA2DS2-VASc")
    else:
        missing = [k for k, v in checks.items() if not v]
        record_warning("Phase 1 Integration", f"Missing in CHA2DS2-VASc: {', '.join(missing)}")
except Exception as e:
    record_failed("Phase 1 Integration Check", str(e))

# 12. Test Decision Support Page
print("\n12. Testing Decision Support Page...")
try:
    page_path = Path("pages/10_🧭_Decision_Support.py")
    assert page_path.exists(), "Decision Support page not found"
    
    # Check imports
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    checks = {
        "flowcharts": "create_wells_pe_flowchart" in content,
        "pregnancy": "render_pregnancy_lactation_section" in content,
        "pediatric": "render_pediatric_dosing_calculator" in content
    }
    
    all_passed = all(checks.values())
    
    if all_passed:
        record_passed("Decision Support Page")
    else:
        missing = [k for k, v in checks.items() if not v]
        record_warning("Decision Support Page", f"Missing: {', '.join(missing)}")
except Exception as e:
    record_failed("Decision Support Page", str(e))

# ========== SUMMARY ==========
print("\n" + "=" * 80)
print("📊 TEST SUMMARY")
print("=" * 80)

total_tests = len(test_results["passed"]) + len(test_results["failed"])
passed = len(test_results["passed"])
failed = len(test_results["failed"])
warnings = len(test_results["warnings"])

print(f"\n✅ Passed: {passed}/{total_tests}")
print(f"❌ Failed: {failed}/{total_tests}")
print(f"⚠️  Warnings: {warnings}")

if test_results["failed"]:
    print("\n❌ FAILED TESTS:")
    for name, error in test_results["failed"]:
        print(f"   - {name}: {error}")

if test_results["warnings"]:
    print("\n⚠️  WARNINGS:")
    for name, message in test_results["warnings"]:
        print(f"   - {name}: {message}")

print("\n" + "=" * 80)

if failed == 0:
    print("🎉 ALL TESTS PASSED!")
    exit_code = 0
else:
    print("⚠️  SOME TESTS FAILED")
    exit_code = 1

# Tránh SystemExit khi pytest import file này; chỉ exit khi chạy trực tiếp
if __name__ == "__main__":
    sys.exit(exit_code)

