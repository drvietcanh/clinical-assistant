#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check enhanced fields structure in drug database
"""

import sys
import json
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

def check_enhanced_fields():
    """Check enhanced fields structure for all drugs"""
    
    enhanced_drugs = []
    incomplete_drugs = []
    structure_issues = []
    quality_issues = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        fields_present = [f for f in ENHANCED_FIELDS if f in drug_data]
        
        if fields_present:
            enhanced_drugs.append({
                'name': drug_name,
                'fields': fields_present,
                'missing': [f for f in ENHANCED_FIELDS if f not in drug_data],
                'all_present': len(fields_present) == len(ENHANCED_FIELDS)
            })
            
            # Check structure issues
            for field in fields_present:
                value = drug_data[field]
                
                # Check mechanism_of_action (should be string)
                if field == 'mechanism_of_action':
                    if not isinstance(value, str):
                        structure_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Expected string, got {type(value).__name__}'
                        })
                    elif len(value) < 50:
                        quality_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Content too short ({len(value)} chars)'
                        })
                
                # Check monitoring (should be list)
                elif field == 'monitoring':
                    if not isinstance(value, list):
                        structure_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Expected list, got {type(value).__name__}'
                        })
                    elif len(value) == 0:
                        quality_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': 'Empty list'
                        })
                
                # Check precautions (should be list)
                elif field == 'precautions':
                    if not isinstance(value, list):
                        structure_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Expected list, got {type(value).__name__}'
                        })
                    elif len(value) == 0:
                        quality_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': 'Empty list'
                        })
                
                # Check pharmacokinetics (should be dict)
                elif field == 'pharmacokinetics':
                    if not isinstance(value, dict):
                        structure_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Expected dict, got {type(value).__name__}'
                        })
                    elif len(value) == 0:
                        quality_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': 'Empty dictionary'
                        })
                
                # Check storage (should be string)
                elif field == 'storage':
                    if not isinstance(value, str):
                        structure_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Expected string, got {type(value).__name__}'
                        })
                    elif len(value) < 10:
                        quality_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Content too short ({len(value)} chars)'
                        })
                
                # Check black_box_warnings (should be string or None)
                elif field == 'black_box_warnings':
                    if value is not None and not isinstance(value, str):
                        structure_issues.append({
                            'drug': drug_name,
                            'field': field,
                            'issue': f'Expected string or None, got {type(value).__name__}'
                        })
    
    # Print results
    print("=" * 80)
    print("ENHANCED FIELDS ANALYSIS")
    print("=" * 80)
    print(f"\nTotal drugs in database: {len(DRUG_DATABASE)}")
    print(f"Drugs with enhanced fields: {len(enhanced_drugs)}")
    print(f"Drugs with all enhanced fields: {sum(1 for d in enhanced_drugs if d['all_present'])}")
    print(f"Structure issues found: {len(structure_issues)}")
    print(f"Quality issues found: {len(quality_issues)}")
    
    print("\n" + "=" * 80)
    print("DRUGS WITH ENHANCED FIELDS:")
    print("=" * 80)
    for drug in enhanced_drugs:
        status = "✓ COMPLETE" if drug['all_present'] else "⚠ INCOMPLETE"
        print(f"\n{drug['name']} - {status}")
        print(f"  Present: {', '.join(drug['fields'])}")
        if drug['missing']:
            print(f"  Missing: {', '.join(drug['missing'])}")
    
    if structure_issues:
        print("\n" + "=" * 80)
        print("STRUCTURE ISSUES:")
        print("=" * 80)
        for issue in structure_issues:
            print(f"\n{issue['drug']} - {issue['field']}")
            print(f"  Issue: {issue['issue']}")
    
    if quality_issues:
        print("\n" + "=" * 80)
        print("QUALITY ISSUES:")
        print("=" * 80)
        for issue in quality_issues:
            print(f"\n{issue['drug']} - {issue['field']}")
            print(f"  Issue: {issue['issue']}")
    
    # Summary statistics
    print("\n" + "=" * 80)
    print("FIELD USAGE STATISTICS:")
    print("=" * 80)
    for field in ENHANCED_FIELDS:
        count = sum(1 for d in enhanced_drugs if field in d['fields'])
        print(f"  {field}: {count} drugs")
    
    # Check for drugs mentioned in summary that might be missing
    print("\n" + "=" * 80)
    print("CHECKING SPECIFIC DRUGS (from summary):")
    print("=" * 80)
    drugs_to_check = ['Amiodarone', 'Metoclopramide']
    for drug_name in drugs_to_check:
        if drug_name in DRUG_DATABASE:
            drug_data = DRUG_DATABASE[drug_name]
            fields_present = [f for f in ENHANCED_FIELDS if f in drug_data]
            if fields_present:
                print(f"\n{drug_name}: HAS {len(fields_present)} enhanced fields")
                print(f"  Fields: {', '.join(fields_present)}")
            else:
                print(f"\n{drug_name}: NO enhanced fields")
        else:
            print(f"\n{drug_name}: NOT FOUND in database")
    
    return {
        'enhanced_drugs': enhanced_drugs,
        'structure_issues': structure_issues,
        'quality_issues': quality_issues,
        'total_drugs': len(DRUG_DATABASE),
        'enhanced_count': len(enhanced_drugs),
        'complete_count': sum(1 for d in enhanced_drugs if d['all_present'])
    }

if __name__ == '__main__':
    try:
        results = check_enhanced_fields()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
