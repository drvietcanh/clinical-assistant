"""
Script to check which drugs in DRUG_DATABASE are missing risk_flags and guideline_tags
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError as e:
    print(f"Error: Could not import DRUG_DATABASE: {e}")
    sys.exit(1)

def main():
    """Check which drugs are missing risk_flags and guideline_tags"""
    total_drugs = len(DRUG_DATABASE)
    missing_both = []
    missing_risk_flags = []
    missing_guideline_tags = []
    has_both = []
    
    print(f"Checking {total_drugs} drugs in DRUG_DATABASE...")
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        has_rf = 'risk_flags' in drug_data and drug_data.get('risk_flags') is not None
        has_gt = 'guideline_tags' in drug_data and drug_data.get('guideline_tags') is not None
        
        if not has_rf and not has_gt:
            missing_both.append(drug_name)
        elif not has_rf:
            missing_risk_flags.append(drug_name)
        elif not has_gt:
            missing_guideline_tags.append(drug_name)
        else:
            has_both.append(drug_name)
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total drugs: {total_drugs}")
    print(f"Has both risk_flags and guideline_tags: {len(has_both)} ({len(has_both)/total_drugs*100:.1f}%)")
    print(f"Missing both: {len(missing_both)} ({len(missing_both)/total_drugs*100:.1f}%)")
    print(f"Missing only risk_flags: {len(missing_risk_flags)} ({len(missing_risk_flags)/total_drugs*100:.1f}%)")
    print(f"Missing only guideline_tags: {len(missing_guideline_tags)} ({len(missing_guideline_tags)/total_drugs*100:.1f}%)")
    
    print("\n" + "="*80)
    print("MISSING BOTH (First 50)")
    print("="*80)
    for drug in missing_both[:50]:
        print(f"  - {drug}")
    if len(missing_both) > 50:
        print(f"  ... and {len(missing_both) - 50} more")
    
    if missing_risk_flags:
        print("\n" + "="*80)
        print("MISSING ONLY RISK_FLAGS")
        print("="*80)
        for drug in missing_risk_flags:
            print(f"  - {drug}")
    
    if missing_guideline_tags:
        print("\n" + "="*80)
        print("MISSING ONLY GUIDELINE_TAGS")
        print("="*80)
        for drug in missing_guideline_tags:
            print(f"  - {drug}")
    
    # Save to file
    with open("missing_risk_flags_direct_report.txt", "w", encoding="utf-8") as f:
        f.write("MISSING BOTH\n")
        f.write("="*80 + "\n")
        for drug in missing_both:
            f.write(f"{drug}\n")
        
        if missing_risk_flags:
            f.write("\n\nMISSING ONLY RISK_FLAGS\n")
            f.write("="*80 + "\n")
            for drug in missing_risk_flags:
                f.write(f"{drug}\n")
        
        if missing_guideline_tags:
            f.write("\n\nMISSING ONLY GUIDELINE_TAGS\n")
            f.write("="*80 + "\n")
            for drug in missing_guideline_tags:
                f.write(f"{drug}\n")
    
    print(f"\nReport saved to: missing_risk_flags_direct_report.txt")
    print(f"\nRemaining drugs to complete: {len(missing_both) + len(missing_risk_flags) + len(missing_guideline_tags)}")

if __name__ == "__main__":
    main()

