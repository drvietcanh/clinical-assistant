"""
Validation script to check all drugs have risk_flags and guideline_tags
"""
import sys
import os
sys.path.insert(0, '.')

try:
    from drugs.drug_database import DRUG_DATABASE
    
    missing_risk_flags = []
    missing_guideline_tags = []
    missing_both = []
    
    # Handle both dict and list formats
    if isinstance(DRUG_DATABASE, list):
        drug_items = [(drug.get('name', 'Unknown'), drug) for drug in DRUG_DATABASE if isinstance(drug, dict)]
    else:
        drug_items = DRUG_DATABASE.items()
    
    for drug_name, drug_data in drug_items:
        if not isinstance(drug_data, dict):
            continue
        has_risk_flags = 'risk_flags' in drug_data and drug_data.get('risk_flags') is not None
        has_guideline_tags = 'guideline_tags' in drug_data and drug_data.get('guideline_tags') is not None
        
        if not has_risk_flags and not has_guideline_tags:
            missing_both.append(drug_name)
        elif not has_risk_flags:
            missing_risk_flags.append(drug_name)
        elif not has_guideline_tags:
            missing_guideline_tags.append(drug_name)
    
    total_drugs = len(drug_items)
    complete_drugs = total_drugs - len(missing_both) - len(missing_risk_flags) - len(missing_guideline_tags)
    completion_rate = (complete_drugs / total_drugs * 100) if total_drugs > 0 else 0
    
    print("="*80)
    print("VALIDATION REPORT: Risk Flags & Guideline Tags")
    print("="*80)
    print(f"\nTotal drugs: {total_drugs}")
    print(f"Complete (both fields): {complete_drugs} ({completion_rate:.1f}%)")
    print(f"Missing both: {len(missing_both)}")
    print(f"Missing only risk_flags: {len(missing_risk_flags)}")
    print(f"Missing only guideline_tags: {len(missing_guideline_tags)}")
    
    if missing_both:
        print(f"\n⚠️  Missing BOTH risk_flags and guideline_tags ({len(missing_both)}):")
        for drug in sorted(missing_both)[:20]:
            print(f"  - {drug}")
        if len(missing_both) > 20:
            print(f"  ... and {len(missing_both) - 20} more")
    
    if missing_risk_flags:
        print(f"\n⚠️  Missing ONLY risk_flags ({len(missing_risk_flags)}):")
        for drug in sorted(missing_risk_flags)[:10]:
            print(f"  - {drug}")
        if len(missing_risk_flags) > 10:
            print(f"  ... and {len(missing_risk_flags) - 10} more")
    
    if missing_guideline_tags:
        print(f"\n⚠️  Missing ONLY guideline_tags ({len(missing_guideline_tags)}):")
        for drug in sorted(missing_guideline_tags)[:10]:
            print(f"  - {drug}")
        if len(missing_guideline_tags) > 10:
            print(f"  ... and {len(missing_guideline_tags) - 10} more")
    
    if not missing_both and not missing_risk_flags and not missing_guideline_tags:
        print("\n✅ SUCCESS: All drugs have both risk_flags and guideline_tags!")
    
    # Save full list to file
    with open("missing_drugs_full_list.txt", "w", encoding="utf-8") as f:
        f.write("DRUGS MISSING RISK_FLAGS AND/OR GUIDELINE_TAGS\n")
        f.write("="*80 + "\n\n")
        f.write(f"Total drugs: {total_drugs}\n")
        f.write(f"Complete: {complete_drugs} ({completion_rate:.1f}%)\n")
        f.write(f"Missing both: {len(missing_both)}\n")
        f.write(f"Missing only risk_flags: {len(missing_risk_flags)}\n")
        f.write(f"Missing only guideline_tags: {len(missing_guideline_tags)}\n\n")
        
        if missing_both:
            f.write("MISSING BOTH:\n")
            f.write("-"*80 + "\n")
            for drug in sorted(missing_both):
                f.write(f"{drug}\n")
        
        if missing_risk_flags:
            f.write("\n\nMISSING ONLY RISK_FLAGS:\n")
            f.write("-"*80 + "\n")
            for drug in sorted(missing_risk_flags):
                f.write(f"{drug}\n")
        
        if missing_guideline_tags:
            f.write("\n\nMISSING ONLY GUIDELINE_TAGS:\n")
            f.write("-"*80 + "\n")
            for drug in sorted(missing_guideline_tags):
                f.write(f"{drug}\n")
    
    print(f"\n📄 Full list saved to: missing_drugs_full_list.txt")
    print("\n" + "="*80)
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
