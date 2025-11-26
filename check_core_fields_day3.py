#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check core fields for Phase 2 Day 3
"""

from drugs.drug_database import DRUG_DATABASE

core_fields = ['mechanism_of_action', 'pharmacokinetics', 'monitoring', 'precautions', 'storage']

results = {}
for name, data in DRUG_DATABASE.items():
    missing = [f for f in core_fields if f not in data]
    has_all = all(f in data for f in core_fields)
    results[name] = {
        'missing': missing,
        'has_all': has_all
    }

missing_all = [name for name, info in results.items() if not info['has_all']]

print(f'Total drugs: {len(DRUG_DATABASE)}')
print(f'Drugs with all core fields: {len(results) - len(missing_all)}')
print(f'Drugs missing some core fields: {len(missing_all)}')

if missing_all:
    print(f'\nDrugs missing core fields (first 20):')
    for name in missing_all[:20]:
        missing = results[name]['missing']
        print(f'  {name}: missing {missing}')
else:
    print('\n✅ All drugs have all core fields!')

# Check field quality (if field exists but is empty or incomplete)
print('\n--- Checking field quality ---')
quality_issues = []
for name, data in DRUG_DATABASE.items():
    issues = []
    for field in core_fields:
        if field in data:
            value = data[field]
            if value is None or value == '' or (isinstance(value, dict) and len(value) == 0) or (isinstance(value, list) and len(value) == 0):
                issues.append(f'{field} (empty)')
    if issues:
        quality_issues.append((name, issues))

if quality_issues:
    print(f'Drugs with quality issues (first 10):')
    for name, issues in quality_issues[:10]:
        print(f'  {name}: {issues}')
else:
    print('✅ No quality issues found!')

