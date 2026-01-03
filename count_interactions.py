"""Count drug interactions in expanded database"""
import sys
sys.path.insert(0, '.')

try:
    from drugs.interactions_data_expanded.anticoagulants import ANTICOAGULANT_INTERACTIONS
    from drugs.interactions_data_expanded.antibiotics import ANTIBIOTIC_INTERACTIONS
    from drugs.interactions_data_expanded.cardiovascular import CARDIOVASCULAR_INTERACTIONS
    from drugs.interactions_data_expanded.antidiabetics import ANTIDIABETIC_INTERACTIONS
    from drugs.interactions_data_expanded.psychiatry import PSYCHIATRY_INTERACTIONS
    from drugs.interactions_data_expanded.gi import GI_INTERACTIONS
    from drugs.interactions_data_expanded.other import OTHER_INTERACTIONS
    from drugs.interactions_data_expanded.analgesics import ANALGESICS_INTERACTIONS
    from drugs.interactions_data_expanded.antifungals_antivirals import ANTIFUNGALS_ANTIVIRALS_INTERACTIONS
    from drugs.interactions_data_expanded.immunosuppressants_oncology import IMMUNOSUPPRESSANTS_ONCOLOGY_INTERACTIONS
    from drugs.interactions_data_expanded import EXPANDED_INTERACTIONS
    
    print("=" * 60)
    print("DRUG INTERACTIONS COUNT")
    print("=" * 60)
    print(f"Anticoagulants: {len(ANTICOAGULANT_INTERACTIONS)}")
    print(f"Antibiotics: {len(ANTIBIOTIC_INTERACTIONS)}")
    print(f"Cardiovascular: {len(CARDIOVASCULAR_INTERACTIONS)}")
    print(f"Antidiabetics: {len(ANTIDIABETIC_INTERACTIONS)}")
    print(f"Psychiatry: {len(PSYCHIATRY_INTERACTIONS)}")
    print(f"GI: {len(GI_INTERACTIONS)}")
    print(f"Other: {len(OTHER_INTERACTIONS)}")
    print(f"Analgesics: {len(ANALGESICS_INTERACTIONS)}")
    print(f"Antifungals/Antivirals: {len(ANTIFUNGALS_ANTIVIRALS_INTERACTIONS)}")
    print(f"Immunosuppressants/Oncology: {len(IMMUNOSUPPRESSANTS_ONCOLOGY_INTERACTIONS)}")
    print("-" * 60)
    print(f"TOTAL EXPANDED: {len(EXPANDED_INTERACTIONS)}")
    print("=" * 60)
    
    # Count by severity
    major = sum(1 for v in EXPANDED_INTERACTIONS.values() if v.get('severity') == 'Major')
    moderate = sum(1 for v in EXPANDED_INTERACTIONS.values() if v.get('severity') == 'Moderate')
    minor = sum(1 for v in EXPANDED_INTERACTIONS.values() if v.get('severity') == 'Minor')
    
    print(f"\nBy Severity:")
    print(f"  Major: {major}")
    print(f"  Moderate: {moderate}")
    print(f"  Minor: {minor}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

