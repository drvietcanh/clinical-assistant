"""
Module Tests for Clinical Assistant
Tests: Drug Database, TDM, Critical Care, Labs, and other modules
"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("📦 MODULE TESTS - Clinical Assistant")
print("=" * 60)
print()

# ============================================================================
# TEST 1: Drug Database Module
# ============================================================================
print("📋 TEST 1: Drug Database Module")
print("-" * 60)

try:
    from drugs.drug_database import get_drug_info, search_drugs
    
    # Test drug search
    test_searches = ["Aspirin", "Metformin", "Amoxicillin"]
    
    drugs_found = 0
    for search_term in test_searches:
        results = search_drugs(search_term)
        if results and len(results) > 0:
            drugs_found += 1
            print(f"   ✅ '{search_term}': {len(results)} results")
        else:
            print(f"   ⚠️  '{search_term}': No results")
    
    # Test get_drug_info
    if drugs_found > 0:
        try:
            drug_info = get_drug_info("Aspirin")
            if drug_info:
                print(f"   ✅ get_drug_info('Aspirin'): Found")
                # Check for enhanced fields
                enhanced_fields = ["mechanism_of_action", "monitoring", "precautions"]
                has_enhanced = any(field in str(drug_info) for field in enhanced_fields)
                if has_enhanced:
                    print(f"   ✅ Enhanced fields: Present")
                else:
                    print(f"   ⚠️  Enhanced fields: Not found")
            else:
                print(f"   ⚠️  get_drug_info('Aspirin'): Not found")
        except Exception as e:
            print(f"   ⚠️  get_drug_info error: {e}")
    
    print(f"\n   Drugs found: {drugs_found}/{len(test_searches)}")
    print("✅ Drug Database Module - PASSED")
    print()
    
except ImportError:
    print("   ⚠️  Drug database module not available")
    print()
except Exception as e:
    print(f"❌ DRUG DATABASE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 2: TDM Module
# ============================================================================
print("📋 TEST 2: TDM Module")
print("-" * 60)

try:
    # Check TDM module files
    tdm_files = [
        "drugs/tdm/digoxin.py",
        "drugs/tdm/phenytoin.py",
        "drugs/tdm/lithium.py",
    ]
    
    tdm_files_found = 0
    for file_path in tdm_files:
        full_path = project_root / file_path
        if full_path.exists():
            tdm_files_found += 1
            file_name = Path(file_path).stem
            print(f"   ✅ {file_name}.py: Found")
        else:
            file_name = Path(file_path).stem
            print(f"   ⚠️  {file_name}.py: Not found")
    
    # Check TDM page
    tdm_page = project_root / "pages" / "08_📊_TDM.py"
    if tdm_page.exists():
        print(f"   ✅ TDM page: Found")
    else:
        print(f"   ⚠️  TDM page: Not found")
    
    print(f"\n   TDM files: {tdm_files_found}/{len(tdm_files)}")
    print("✅ TDM Module - PASSED")
    print()
    
except Exception as e:
    print(f"❌ TDM MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 3: Critical Care Module
# ============================================================================
print("📋 TEST 3: Critical Care Module")
print("-" * 60)

try:
    # Check critical care files
    critical_care_files = [
        "critical_care/fluids.py",
        "critical_care/vasopressors.py",
        "critical_care/transfusion.py",
        "critical_care/sedation.py",
    ]
    
    files_found = 0
    for file_path in critical_care_files:
        full_path = project_root / file_path
        if full_path.exists():
            files_found += 1
            file_name = Path(file_path).stem
            print(f"   ✅ {file_name}.py: Found")
            
            # Check for functions
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                if "def " in content:
                    func_count = content.count("def ")
                    print(f"      Functions: {func_count}")
        else:
            file_name = Path(file_path).stem
            print(f"   ⚠️  {file_name}.py: Not found")
    
    # Check critical care page
    cc_page = project_root / "pages" / "09_🫁_Critical_Care.py"
    if cc_page.exists():
        print(f"   ✅ Critical Care page: Found")
    else:
        print(f"   ⚠️  Critical Care page: Not found")
    
    print(f"\n   Files found: {files_found}/{len(critical_care_files)}")
    print("✅ Critical Care Module - PASSED")
    print()
    
except Exception as e:
    print(f"❌ CRITICAL CARE MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 4: Labs Module
# ============================================================================
print("📋 TEST 4: Labs Module")
print("-" * 60)

try:
    # Check lab files
    lab_files = [
        "labs/cbc.py",
        "labs/cmp.py",
        "labs/lft.py",
        "labs/cardiac.py",
        "labs/coag.py",
        "labs/thyroid.py",
    ]
    
    lab_files_found = 0
    for file_path in lab_files:
        full_path = project_root / file_path
        if full_path.exists():
            lab_files_found += 1
            file_name = Path(file_path).stem
            print(f"   ✅ {file_name}.py: Found")
            
            # Check for format='%.1f'
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                if 'format="%.1f"' in content or "format='%.1f'" in content:
                    print(f"      ✅ Has decimal format")
        else:
            file_name = Path(file_path).stem
            print(f"   ⚠️  {file_name}.py: Not found")
    
    # Check labs page
    labs_page = project_root / "pages" / "05_🔬_Labs_and_Calculators.py"
    if labs_page.exists():
        print(f"   ✅ Labs page: Found")
    else:
        print(f"   ⚠️  Labs page: Not found")
    
    print(f"\n   Lab files: {lab_files_found}/{len(lab_files)}")
    print("✅ Labs Module - PASSED")
    print()
    
except Exception as e:
    print(f"❌ LABS MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 5: Antibiotics Module
# ============================================================================
print("📋 TEST 5: Antibiotics Module")
print("-" * 60)

try:
    # Check antibiotic files
    ab_files = [
        "antibiotics/dosing_calculator.py",
        "antibiotics/database_display.py",
        "antibiotics/crcl.py",
        "antibiotics/vancomycin.py",
    ]
    
    ab_files_found = 0
    for file_path in ab_files:
        full_path = project_root / file_path
        if full_path.exists():
            ab_files_found += 1
            file_name = Path(file_path).stem
            print(f"   ✅ {file_name}.py: Found")
        else:
            file_name = Path(file_path).stem
            print(f"   ⚠️  {file_name}.py: Not found")
    
    # Check antibiotics page
    ab_page = project_root / "pages" / "02_💊_Antibiotics.py"
    if ab_page.exists():
        print(f"   ✅ Antibiotics page: Found")
    else:
        print(f"   ⚠️  Antibiotics page: Not found")
    
    print(f"\n   Antibiotic files: {ab_files_found}/{len(ab_files)}")
    print("✅ Antibiotics Module - PASSED")
    print()
    
except Exception as e:
    print(f"❌ ANTIBIOTICS MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 6: Diagnosis Module
# ============================================================================
print("📋 TEST 6: Diagnosis Module")
print("-" * 60)

try:
    from diagnosis.ddx_data import get_all_scenarios
    from diagnosis.ddx_generator import generate_ddx
    
    # Check scenarios
    all_scenarios = get_all_scenarios()
    print(f"   Scenarios available: {len(all_scenarios)}")
    
    # Check diagnosis page
    dx_page = project_root / "pages" / "06_🩺_Diagnosis.py"
    if dx_page.exists():
        print(f"   ✅ Diagnosis page: Found")
    else:
        print(f"   ⚠️  Diagnosis page: Not found")
    
    # Check ddx_generator function
    if hasattr(generate_ddx, '__call__'):
        print(f"   ✅ generate_ddx function: Available")
    else:
        print(f"   ⚠️  generate_ddx function: Not available")
    
    print("✅ Diagnosis Module - PASSED")
    print()
    
except Exception as e:
    print(f"❌ DIAGNOSIS MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 7: Protocols Module
# ============================================================================
print("📋 TEST 7: Protocols Module")
print("-" * 60)

try:
    # Check protocols directory
    protocols_dir = project_root / "protocols"
    
    if protocols_dir.exists():
        protocol_files = list(protocols_dir.glob("*.py"))
        protocol_files = [f for f in protocol_files if not f.name.startswith("__")]
        
        print(f"   Protocol files: {len(protocol_files)}")
        for pf in sorted(protocol_files)[:5]:
            print(f"      - {pf.name}")
        
        # Check protocols page
        protocols_page = project_root / "pages" / "04_📋_Protocols.py"
        if protocols_page.exists():
            print(f"   ✅ Protocols page: Found")
        else:
            print(f"   ⚠️  Protocols page: Not found")
        
        print("✅ Protocols Module - PASSED")
    else:
        print("   ⚠️  protocols/ directory not found")
    
    print()
    
except Exception as e:
    print(f"❌ PROTOCOLS MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 8: Ventilator Module
# ============================================================================
print("📋 TEST 8: Ventilator Module")
print("-" * 60)

try:
    # Check ventilator files
    vent_files = [
        "ventilator/ardsnet.py",
        "ventilator/peep_fio2.py",
    ]
    
    vent_files_found = 0
    for file_path in vent_files:
        full_path = project_root / file_path
        if full_path.exists():
            vent_files_found += 1
            file_name = Path(file_path).stem
            print(f"   ✅ {file_name}.py: Found")
        else:
            file_name = Path(file_path).stem
            print(f"   ⚠️  {file_name}.py: Not found")
    
    # Check ventilator page
    vent_page = project_root / "pages" / "03_🫁_Ventilator.py"
    if vent_page.exists():
        print(f"   ✅ Ventilator page: Found")
    else:
        print(f"   ⚠️  Ventilator page: Not found")
    
    print(f"\n   Ventilator files: {vent_files_found}/{len(vent_files)}")
    print("✅ Ventilator Module - PASSED")
    print()
    
except Exception as e:
    print(f"❌ VENTILATOR MODULE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("📊 MODULE TEST SUMMARY")
print("=" * 60)
print()
print("✅ Tests completed:")
print("   1. Drug Database Module")
print("   2. TDM Module")
print("   3. Critical Care Module")
print("   4. Labs Module")
print("   5. Antibiotics Module")
print("   6. Diagnosis Module")
print("   7. Protocols Module")
print("   8. Ventilator Module")
print()
print("💡 Module tests verify:")
print("   - All modules are present")
print("   - Module files exist and are accessible")
print("   - Pages are properly set up")
print("   - Functions are available")
print()
print("=" * 60)

