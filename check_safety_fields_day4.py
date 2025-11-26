#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check safety fields for Phase 2 Day 4
"""

from drugs.drug_database import DRUG_DATABASE

safety_fields = {
    'black_box_warnings': 'Black Box Warnings',
    'contraindications': 'Contraindications (enhanced)',
    'overdose_management': 'Overdose Management',
    'reversal_agents': 'Reversal Agents'
}

results = {}
for name, data in DRUG_DATABASE.items():
    missing = []
    has_enhanced = {}
    
    # Check black_box_warnings
    if 'black_box_warnings' not in data:
        missing.append('black_box_warnings')
    elif data['black_box_warnings'] is None or data['black_box_warnings'] == '':
        missing.append('black_box_warnings (empty)')
    
    # Check contraindications (enhanced format)
    if 'contraindications' not in data:
        missing.append('contraindications')
    elif isinstance(data['contraindications'], list):
        # Old format - needs enhancement
        has_enhanced['contraindications'] = False
    elif isinstance(data['contraindications'], dict):
        # Check if it has tuyệt_đối/tương_đối structure
        if 'tuyệt_đối' in data['contraindications'] or 'tương_đối' in data['contraindications']:
            has_enhanced['contraindications'] = True
        else:
            has_enhanced['contraindications'] = False
    
    # Check overdose_management
    if 'overdose_management' not in data:
        missing.append('overdose_management')
    elif isinstance(data['overdose_management'], str):
        # Old format - needs enhancement
        has_enhanced['overdose_management'] = False
    elif isinstance(data['overdose_management'], dict):
        has_enhanced['overdose_management'] = True
    
    # Check reversal_agents
    if 'reversal_agents' not in data:
        missing.append('reversal_agents')
    elif isinstance(data['reversal_agents'], list) and len(data['reversal_agents']) == 0:
        # Empty list is OK (no reversal agents available)
        pass
    elif isinstance(data['reversal_agents'], dict) and data['reversal_agents'].get('available') == False:
        # Explicitly marked as not available is OK
        pass
    
    results[name] = {
        'missing': missing,
        'needs_enhancement': has_enhanced
    }

# Count statistics
missing_bbw = [name for name, info in results.items() if 'black_box_warnings' in info['missing']]
missing_contra = [name for name, info in results.items() if 'contraindications' in info['missing'] or info.get('needs_enhancement', {}).get('contraindications') == False]
missing_overdose = [name for name, info in results.items() if 'overdose_management' in info['missing'] or info.get('needs_enhancement', {}).get('overdose_management') == False]
missing_reversal = [name for name, info in results.items() if 'reversal_agents' in info['missing']]

print(f'Total drugs: {len(DRUG_DATABASE)}')
print(f'\n=== Safety Fields Status ===')
print(f'Drugs missing black_box_warnings: {len(missing_bbw)}')
print(f'Drugs missing/enhanced contraindications: {len(missing_contra)}')
print(f'Drugs missing/enhanced overdose_management: {len(missing_overdose)}')
print(f'Drugs missing reversal_agents: {len(missing_reversal)}')

# Show examples
if missing_bbw:
    print(f'\nDrugs missing black_box_warnings (first 15):')
    for name in missing_bbw[:15]:
        print(f'  - {name}')

if missing_contra:
    print(f'\nDrugs needing contraindications enhancement (first 15):')
    for name in missing_contra[:15]:
        print(f'  - {name}')

if missing_overdose:
    print(f'\nDrugs needing overdose_management enhancement (first 15):')
    for name in missing_overdose[:15]:
        print(f'  - {name}')

# Priority drugs (high-risk drugs that should have all safety fields)
priority_drugs = ['Warfarin', 'Digoxin', 'Lithium', 'Methotrexate', 'Phenytoin', 
                  'Carbamazepine', 'Amiodarone', 'Cyclosporine', 'Tacrolimus']
print(f'\n=== Priority High-Risk Drugs ===')
for drug in priority_drugs:
    if drug in results:
        info = results[drug]
        missing = info['missing']
        if missing:
            print(f'{drug}: missing {missing}')
        else:
            print(f'{drug}: ✅ All safety fields present')

