#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to find all drugs without enhanced fields and divide into batches
"""

from drugs.drug_database import DRUG_DATABASE

# Standard enhanced fields
ENHANCED_FIELDS = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings'
]

def find_drugs_without_enhanced():
    """Find all drugs without enhanced fields"""
    
    drugs_without = []
    drugs_with = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        has_all = all(field in drug_data for field in ENHANCED_FIELDS)
        
        if has_all:
            drugs_with.append(drug_name)
        else:
            missing_fields = [f for f in ENHANCED_FIELDS if f not in drug_data]
            drugs_without.append({
                'name': drug_name,
                'missing': missing_fields,
                'has_some': len([f for f in ENHANCED_FIELDS if f in drug_data]) > 0
            })
    
    print("=" * 80)
    print("DRUGS WITHOUT ENHANCED FIELDS ANALYSIS")
    print("=" * 80)
    print(f"\nTotal drugs in database: {len(DRUG_DATABASE)}")
    print(f"Drugs WITH all enhanced fields: {len(drugs_with)}")
    print(f"Drugs WITHOUT enhanced fields: {len(drugs_without)}")
    
    # Group by category
    print("\n" + "=" * 80)
    print("DRUGS WITHOUT ENHANCED FIELDS (grouped by missing count):")
    print("=" * 80)
    
    drugs_without_sorted = sorted(drugs_without, key=lambda x: (len(x['missing']), x['name']))
    
    for drug in drugs_without_sorted:
        missing_count = len(drug['missing'])
        status = "PARTIAL" if drug['has_some'] else "NONE"
        print(f"{drug['name']:<40} - Missing {missing_count} fields ({status})")
    
    # Divide into batches
    batch_size = 15
    batches = []
    for i in range(0, len(drugs_without_sorted), batch_size):
        batch = drugs_without_sorted[i:i + batch_size]
        batches.append(batch)
    
    print("\n" + "=" * 80)
    print(f"DIVIDED INTO {len(batches)} BATCHES (max {batch_size} drugs per batch):")
    print("=" * 80)
    
    for i, batch in enumerate(batches, 1):
        print(f"\nBatch {i} ({len(batch)} drugs):")
        for drug in batch:
            print(f"  - {drug['name']}")
    
    return {
        'drugs_without': drugs_without_sorted,
        'drugs_with': drugs_with,
        'batches': batches
    }

if __name__ == '__main__':
    try:
        results = find_drugs_without_enhanced()
        print(f"\n\nReady to process {len(results['drugs_without'])} drugs in {len(results['batches'])} batches")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
