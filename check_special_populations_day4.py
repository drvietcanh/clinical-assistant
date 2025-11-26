#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check special populations and localization fields for Phase 2 Day 4
"""

from drugs.drug_database import DRUG_DATABASE

special_pop_fields = {
    'pediatric_dosing': 'Pediatric Dosing',
    'geriatric_dosing': 'Geriatric Dosing',
    'pregnancy_lactation': 'Pregnancy/Lactation (enhanced)',
    'renal_adjustment': 'Renal Adjustment (enhanced)',
    'hepatic_adjustment': 'Hepatic Adjustment (enhanced)'
}

localization_fields = {
    'brand_names': 'Brand Names (Vietnamese)',
    'cost_estimate': 'Cost Estimate (VN market)'
}

results = {}
for name, data in DRUG_DATABASE.items():
    missing_special = []
    missing_localization = []
    needs_enhancement = {}
    
    # Check special populations
    if 'pediatric_dosing' not in data:
        missing_special.append('pediatric_dosing')
    elif isinstance(data['pediatric_dosing'], str):
        needs_enhancement['pediatric_dosing'] = True
    
    if 'geriatric_dosing' not in data:
        missing_special.append('geriatric_dosing')
    
    if 'pregnancy_lactation' not in data:
        missing_special.append('pregnancy_lactation')
    elif isinstance(data['pregnancy_lactation'], str):
        needs_enhancement['pregnancy_lactation'] = True
    
    if 'renal_adjustment' not in data:
        missing_special.append('renal_adjustment')
    elif isinstance(data['renal_adjustment'], str):
        needs_enhancement['renal_adjustment'] = True
    
    if 'hepatic_adjustment' not in data:
        missing_special.append('hepatic_adjustment')
    elif isinstance(data['hepatic_adjustment'], str):
        needs_enhancement['hepatic_adjustment'] = True
    
    # Check localization
    if 'brand_names' not in data:
        missing_localization.append('brand_names')
    elif isinstance(data['brand_names'], list):
        needs_enhancement['brand_names'] = True
    
    if 'cost_estimate' not in data:
        missing_localization.append('cost_estimate')
    
    results[name] = {
        'missing_special': missing_special,
        'missing_localization': missing_localization,
        'needs_enhancement': needs_enhancement
    }

# Count statistics
missing_pediatric = [name for name, info in results.items() if 'pediatric_dosing' in info['missing_special']]
missing_geriatric = [name for name, info in results.items() if 'geriatric_dosing' in info['missing_special']]
missing_pregnancy = [name for name, info in results.items() if 'pregnancy_lactation' in info['missing_special']]
missing_renal = [name for name, info in results.items() if 'renal_adjustment' in info['missing_special']]
missing_hepatic = [name for name, info in results.items() if 'hepatic_adjustment' in info['missing_special']]
missing_brands = [name for name, info in results.items() if 'brand_names' in info['missing_localization']]
missing_cost = [name for name, info in results.items() if 'cost_estimate' in info['missing_localization']]

print(f'Total drugs: {len(DRUG_DATABASE)}')
print(f'\n=== Special Populations Fields Status ===')
print(f'Drugs missing pediatric_dosing: {len(missing_pediatric)}')
print(f'Drugs missing geriatric_dosing: {len(missing_geriatric)}')
print(f'Drugs missing pregnancy_lactation: {len(missing_pregnancy)}')
print(f'Drugs missing renal_adjustment: {len(missing_renal)}')
print(f'Drugs missing hepatic_adjustment: {len(missing_hepatic)}')

print(f'\n=== Localization Fields Status ===')
print(f'Drugs missing brand_names: {len(missing_brands)}')
print(f'Drugs missing cost_estimate: {len(missing_cost)}')

# Show examples
if missing_pediatric:
    print(f'\nDrugs missing pediatric_dosing (first 10):')
    for name in missing_pediatric[:10]:
        print(f'  - {name}')

if missing_brands:
    print(f'\nDrugs missing brand_names (first 10):')
    for name in missing_brands[:10]:
        print(f'  - {name}')

# Check common drugs
common_drugs = ['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Metformin', 'Amlodipine']
print(f'\n=== Common Drugs Status ===')
for drug in common_drugs:
    if drug in results:
        info = results[drug]
        missing = info['missing_special'] + info['missing_localization']
        if missing:
            print(f'{drug}: missing {missing}')
        else:
            print(f'{drug}: ✅ All special populations and localization fields present')

