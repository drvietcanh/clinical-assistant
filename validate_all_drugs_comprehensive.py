#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to comprehensively validate all drug data and enhanced fields
Kiểm tra toàn diện dữ liệu thuốc và enhanced fields
"""

import sys
from collections import defaultdict
from drugs.drug_database import DRUG_DATABASE
from drugs.enhanced_fields_schema import validate_enhanced_fields

# 6 Fields cơ bản (bắt buộc)
REQUIRED_FIELDS = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings'
]

# 8 Fields bổ sung (tùy chọn)
OPTIONAL_FIELDS = [
    'drug_interactions',
    'contraindications',
    'pregnancy_lactation',
    'hepatic_adjustment',
    'overdose_management',
    'reversal_agents',
    'administration_instructions',
    'references'
]

ALL_ENHANCED_FIELDS = REQUIRED_FIELDS + OPTIONAL_FIELDS

def validate_drug_comprehensive(drug_name, drug_data):
    """Validate a single drug comprehensively"""
    results = {
        'name': drug_name,
        'has_enhanced': False,
        'required_fields': {},
        'optional_fields': {},
        'validation_errors': [],
        'structure_errors': [],
        'quality_warnings': [],
        'completeness_score': 0
    }
    
    # Check if drug has any enhanced fields
    has_any_enhanced = any(field in drug_data for field in ALL_ENHANCED_FIELDS)
    results['has_enhanced'] = has_any_enhanced
    
    if not has_any_enhanced:
        return results
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field in drug_data:
            value = drug_data[field]
            results['required_fields'][field] = {
                'present': True,
                'type': type(value).__name__,
                'valid': True,
                'issues': []
            }
            
            # Type validation
            if field == 'mechanism_of_action':
                if not isinstance(value, str):
                    results['structure_errors'].append(f"{field}: Expected string, got {type(value).__name__}")
                    results['required_fields'][field]['valid'] = False
                elif len(value) < 50:
                    results['quality_warnings'].append(f"{field}: Content too short ({len(value)} chars, minimum 50)")
                elif len(value.strip()) == 0:
                    results['structure_errors'].append(f"{field}: Empty string")
                    results['required_fields'][field]['valid'] = False
                    
            elif field == 'monitoring':
                if not isinstance(value, list):
                    results['structure_errors'].append(f"{field}: Expected list, got {type(value).__name__}")
                    results['required_fields'][field]['valid'] = False
                elif len(value) == 0:
                    results['quality_warnings'].append(f"{field}: Empty list")
                    
            elif field == 'precautions':
                if not isinstance(value, list):
                    results['structure_errors'].append(f"{field}: Expected list, got {type(value).__name__}")
                    results['required_fields'][field]['valid'] = False
                elif len(value) == 0:
                    results['quality_warnings'].append(f"{field}: Empty list")
                    
            elif field == 'pharmacokinetics':
                if not isinstance(value, dict):
                    results['structure_errors'].append(f"{field}: Expected dict, got {type(value).__name__}")
                    results['required_fields'][field]['valid'] = False
                else:
                    required_pk_fields = ['half_life', 'onset', 'duration', 'protein_binding', 'clearance']
                    missing_pk = [f for f in required_pk_fields if f not in value or not value[f]]
                    if missing_pk:
                        results['quality_warnings'].append(f"{field}: Missing subfields: {', '.join(missing_pk)}")
                        
            elif field == 'storage':
                if not isinstance(value, str):
                    results['structure_errors'].append(f"{field}: Expected string, got {type(value).__name__}")
                    results['required_fields'][field]['valid'] = False
                elif len(value) < 10:
                    results['quality_warnings'].append(f"{field}: Content too short ({len(value)} chars, minimum 10)")
                elif len(value.strip()) == 0:
                    results['structure_errors'].append(f"{field}: Empty string")
                    results['required_fields'][field]['valid'] = False
                    
            elif field == 'black_box_warnings':
                if value is not None and not isinstance(value, str):
                    results['structure_errors'].append(f"{field}: Expected string or None, got {type(value).__name__}")
                    results['required_fields'][field]['valid'] = False
        else:
            results['required_fields'][field] = {
                'present': False,
                'valid': False,
                'issues': ['Missing required field']
            }
    
    # Check optional fields
    for field in OPTIONAL_FIELDS:
        if field in drug_data:
            value = drug_data[field]
            results['optional_fields'][field] = {
                'present': True,
                'type': type(value).__name__
            }
        else:
            results['optional_fields'][field] = {
                'present': False
            }
    
    # Run schema validation
    enhanced_fields_dict = {k: drug_data[k] for k in REQUIRED_FIELDS if k in drug_data}
    if len(enhanced_fields_dict) == len(REQUIRED_FIELDS):
        is_valid, errors = validate_enhanced_fields(drug_name, enhanced_fields_dict)
        if not is_valid:
            results['validation_errors'].extend(errors)
    
    # Calculate completeness score
    required_present = sum(1 for f in REQUIRED_FIELDS if f in drug_data)
    required_valid = sum(1 for f in REQUIRED_FIELDS 
                        if f in drug_data and results['required_fields'].get(f, {}).get('valid', False))
    optional_present = sum(1 for f in OPTIONAL_FIELDS if f in drug_data)
    
    results['completeness_score'] = {
        'required_present': required_present,
        'required_total': len(REQUIRED_FIELDS),
        'required_valid': required_valid,
        'optional_present': optional_present,
        'optional_total': len(OPTIONAL_FIELDS),
        'percentage': round((required_present / len(REQUIRED_FIELDS)) * 100, 1)
    }
    
    return results

def validate_all_drugs():
    """Validate all drugs in database"""
    print("=" * 100)
    print("KIỂM TRA TOÀN DIỆN DỮ LIỆU THUỐC VÀ ENHANCED FIELDS")
    print("=" * 100)
    
    all_results = []
    stats = {
        'total_drugs': len(DRUG_DATABASE),
        'drugs_with_enhanced': 0,
        'drugs_with_all_required': 0,
        'drugs_with_all_valid': 0,
        'drugs_with_issues': 0,
        'field_statistics': defaultdict(int),
        'structure_errors': [],
        'validation_errors': [],
        'quality_warnings': []
    }
    
    # Validate each drug
    for drug_name, drug_data in sorted(DRUG_DATABASE.items()):
        result = validate_drug_comprehensive(drug_name, drug_data)
        all_results.append(result)
        
        if result['has_enhanced']:
            stats['drugs_with_enhanced'] += 1
            
        if result['completeness_score']['required_present'] == len(REQUIRED_FIELDS):
            stats['drugs_with_all_required'] += 1
            
        if (result['completeness_score']['required_present'] == len(REQUIRED_FIELDS) and
            result['completeness_score']['required_valid'] == len(REQUIRED_FIELDS) and
            len(result['structure_errors']) == 0 and
            len(result['validation_errors']) == 0):
            stats['drugs_with_all_valid'] += 1
        
        if (len(result['structure_errors']) > 0 or 
            len(result['validation_errors']) > 0 or
            len(result['quality_warnings']) > 0):
            stats['drugs_with_issues'] += 1
        
        # Collect errors
        stats['structure_errors'].extend([(drug_name, e) for e in result['structure_errors']])
        stats['validation_errors'].extend([(drug_name, e) for e in result['validation_errors']])
        stats['quality_warnings'].extend([(drug_name, e) for e in result['quality_warnings']])
        
        # Field statistics
        for field in ALL_ENHANCED_FIELDS:
            if field in drug_data:
                stats['field_statistics'][field] += 1
    
    # Print summary
    print(f"\n📊 TỔNG QUAN:")
    print(f"  Tổng số thuốc: {stats['total_drugs']}")
    print(f"  Thuốc có enhanced fields: {stats['drugs_with_enhanced']} ({stats['drugs_with_enhanced']/stats['total_drugs']*100:.1f}%)")
    print(f"  Thuốc có đủ 6 fields cơ bản: {stats['drugs_with_all_required']} ({stats['drugs_with_all_required']/stats['total_drugs']*100:.1f}%)")
    print(f"  Thuốc có đủ và hợp lệ: {stats['drugs_with_all_valid']} ({stats['drugs_with_all_valid']/stats['total_drugs']*100:.1f}%)")
    print(f"  Thuốc có vấn đề: {stats['drugs_with_issues']} ({stats['drugs_with_issues']/stats['total_drugs']*100:.1f}%)")
    
    # Print field statistics
    print(f"\n📋 THỐNG KÊ CÁC FIELD:")
    print(f"\n  === 6 FIELDS CƠ BẢN (Bắt buộc) ===")
    for field in REQUIRED_FIELDS:
        count = stats['field_statistics'][field]
        percentage = (count / stats['total_drugs']) * 100
        status = "✓" if count == stats['total_drugs'] else "⚠"
        print(f"  {status} {field:<30} {count:>4}/{stats['total_drugs']} ({percentage:>5.1f}%)")
    
    print(f"\n  === 8 FIELDS BỔ SUNG (Tùy chọn) ===")
    for field in OPTIONAL_FIELDS:
        count = stats['field_statistics'][field]
        percentage = (count / stats['total_drugs']) * 100
        print(f"    {field:<30} {count:>4}/{stats['total_drugs']} ({percentage:>5.1f}%)")
    
    # Print drugs without enhanced fields
    drugs_without = [r for r in all_results if not r['has_enhanced']]
    if drugs_without:
        print(f"\n⚠️  THUỐC CHƯA CÓ ENHANCED FIELDS ({len(drugs_without)} thuốc):")
        for i, result in enumerate(drugs_without[:50], 1):  # Show first 50
            print(f"  {i:>3}. {result['name']}")
        if len(drugs_without) > 50:
            print(f"  ... và {len(drugs_without) - 50} thuốc khác")
    
    # Print drugs with incomplete required fields
    incomplete = [r for r in all_results 
                  if r['has_enhanced'] and r['completeness_score']['required_present'] < len(REQUIRED_FIELDS)]
    if incomplete:
        print(f"\n⚠️  THUỐC THIẾU FIELDS CƠ BẢN ({len(incomplete)} thuốc):")
        for result in sorted(incomplete, key=lambda x: x['completeness_score']['required_present']):
            missing = [f for f in REQUIRED_FIELDS if f not in result['required_fields'] or not result['required_fields'][f].get('present', False)]
            print(f"  {result['name']:<40} - Thiếu: {', '.join(missing)}")
    
    # Print structure errors
    if stats['structure_errors']:
        print(f"\n❌ LỖI CẤU TRÚC ({len(stats['structure_errors'])} lỗi):")
        for drug_name, error in stats['structure_errors'][:20]:  # Show first 20
            print(f"  {drug_name}: {error}")
        if len(stats['structure_errors']) > 20:
            print(f"  ... và {len(stats['structure_errors']) - 20} lỗi khác")
    
    # Print validation errors
    if stats['validation_errors']:
        print(f"\n❌ LỖI VALIDATION ({len(stats['validation_errors'])} lỗi):")
        for drug_name, error in stats['validation_errors'][:20]:  # Show first 20
            print(f"  {drug_name}: {error}")
        if len(stats['validation_errors']) > 20:
            print(f"  ... và {len(stats['validation_errors']) - 20} lỗi khác")
    
    # Print quality warnings
    if stats['quality_warnings']:
        print(f"\n⚠️  CẢNH BÁO CHẤT LƯỢNG ({len(stats['quality_warnings'])} cảnh báo):")
        for drug_name, warning in stats['quality_warnings'][:20]:  # Show first 20
            print(f"  {drug_name}: {warning}")
        if len(stats['quality_warnings']) > 20:
            print(f"  ... và {len(stats['quality_warnings']) - 20} cảnh báo khác")
    
    # Print drugs with all fields complete
    complete_drugs = [r for r in all_results 
                     if r['completeness_score']['required_present'] == len(REQUIRED_FIELDS) and
                        r['completeness_score']['required_valid'] == len(REQUIRED_FIELDS) and
                        len(r['structure_errors']) == 0 and
                        len(r['validation_errors']) == 0]
    
    if complete_drugs:
        print(f"\n✓ THUỐC HOÀN CHỈNH ({len(complete_drugs)} thuốc):")
        for result in sorted(complete_drugs, key=lambda x: x['name']):
            optional_count = result['completeness_score']['optional_present']
            print(f"  {result['name']:<40} - Optional fields: {optional_count}/{len(OPTIONAL_FIELDS)}")
    
    # Detailed report for drugs with issues
    drugs_with_issues = [r for r in all_results 
                        if len(r['structure_errors']) > 0 or 
                           len(r['validation_errors']) > 0 or
                           len(r['quality_warnings']) > 0]
    
    if drugs_with_issues:
        print(f"\n📝 CHI TIẾT CÁC THUỐC CÓ VẤN ĐỀ:")
        for result in sorted(drugs_with_issues, key=lambda x: x['name']):
            print(f"\n  {result['name']}:")
            if result['structure_errors']:
                for error in result['structure_errors']:
                    print(f"    ❌ Structure: {error}")
            if result['validation_errors']:
                for error in result['validation_errors']:
                    print(f"    ❌ Validation: {error}")
            if result['quality_warnings']:
                for warning in result['quality_warnings']:
                    print(f"    ⚠️  Quality: {warning}")
            print(f"    Completeness: {result['completeness_score']['required_present']}/{len(REQUIRED_FIELDS)} required fields")
    
    print("\n" + "=" * 100)
    print("KẾT THÚC KIỂM TRA")
    print("=" * 100)
    
    return {
        'all_results': all_results,
        'stats': stats,
        'complete_drugs': complete_drugs,
        'incomplete_drugs': incomplete,
        'drugs_without_enhanced': drugs_without,
        'drugs_with_issues': drugs_with_issues
    }

if __name__ == '__main__':
    try:
        results = validate_all_drugs()
        
        # Exit code based on issues found
        if results['stats']['structure_errors'] or results['stats']['validation_errors']:
            print("\n⚠️  Có lỗi cấu trúc hoặc validation. Vui lòng kiểm tra và sửa.")
            sys.exit(1)
        elif results['stats']['quality_warnings']:
            print("\n⚠️  Có cảnh báo chất lượng. Nên kiểm tra và cải thiện.")
            sys.exit(0)
        else:
            print("\n✓ Tất cả thuốc đều hợp lệ!")
            sys.exit(0)
    except Exception as e:
        print(f"\n❌ Lỗi khi chạy validation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

