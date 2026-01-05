"""
Script bổ sung field bổ sung cho các thuốc đã có đủ field chuẩn
"""
import sys
import json
from pathlib import Path
from typing import Dict, List, Any
import io

# Setup path
sys.path.insert(0, str(Path.cwd()))

from add_fields_helper import add_additional_fields, preview_changes
from drugs.field_validator import get_field_validator, STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS

# Setup encoding for Windows
if sys.platform == 'win32' and not isinstance(sys.stdout, io.TextIOWrapper):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except:
        pass

def find_drugs_missing_additional_fields() -> List[Dict[str, Any]]:
    """Tìm các thuốc thiếu field bổ sung nhưng đã có đủ field chuẩn"""
    from drugs.drug_database import DRUG_DATABASE
    from drugs.drug_manager_tool import get_drug_manager
    
    manager = get_drug_manager()
    validator = get_field_validator()
    
    drugs_to_update = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Validate
        result = validator.validate_all_fields(drug_data)
        
        # Check if has all standard fields
        if len(result.get('missing_standard_fields', [])) == 0:
            # Check missing additional fields
            missing_additional = result.get('missing_additional_fields', [])
            if missing_additional:
                # Find file
                files = manager.find_drug_file(drug_name)
                if files:
                    drugs_to_update.append({
                        'name': drug_name,
                        'file': files[0],
                        'missing_additional': missing_additional
                    })
    
    return drugs_to_update

def batch_add_additional_fields(dry_run: bool = True, limit: int = None) -> Dict[str, Any]:
    """Bổ sung field bổ sung cho các thuốc đã có đủ field chuẩn"""
    drugs_to_update = find_drugs_missing_additional_fields()
    
    if limit:
        drugs_to_update = drugs_to_update[:limit]
    
    results = {
        'total': len(drugs_to_update),
        'success': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }
    
    print("="*60)
    print(f"BAT DAU BO SUNG FIELD BO SUNG")
    print(f"Tong so thuoc: {results['total']}")
    print(f"Dry run: {dry_run}")
    print("="*60)
    
    for i, drug_info in enumerate(drugs_to_update, 1):
        drug_name = drug_info['name']
        file_path = drug_info['file']
        missing_fields = drug_info.get('missing_additional', [])
        
        print(f"\n[{i}/{results['total']}] {drug_name}")
        print(f"  File: {file_path}")
        print(f"  Thieu {len(missing_fields)} field bo sung: {', '.join(missing_fields[:5])}")
        if len(missing_fields) > 5:
            print(f"  ... va {len(missing_fields) - 5} field khac")
        
        try:
            result = add_additional_fields(drug_name, file_path, dry_run=dry_run)
            
            if result['success']:
                if result.get('added_fields'):
                    results['success'] += 1
                    print(f"  ✓ Da bo sung {len(result['added_fields'])} field")
                    results['details'].append({
                        'drug_name': drug_name,
                        'file': file_path,
                        'status': 'success',
                        'added_fields': result['added_fields']
                    })
                else:
                    results['skipped'] += 1
                    print(f"  - Khong co field nao can bo sung")
            else:
                results['failed'] += 1
                print(f"  ✗ Loi: {result.get('error', 'Unknown error')}")
                results['details'].append({
                    'drug_name': drug_name,
                    'file': file_path,
                    'status': 'failed',
                    'error': result.get('error', 'Unknown error')
                })
        except Exception as e:
            results['failed'] += 1
            print(f"  ✗ Exception: {e}")
            results['details'].append({
                'drug_name': drug_name,
                'file': file_path,
                'status': 'failed',
                'error': str(e)
            })
    
    print("\n" + "="*60)
    print("KET QUA")
    print("="*60)
    print(f"Thanh cong: {results['success']}")
    print(f"Loi: {results['failed']}")
    print(f"Bo qua: {results['skipped']}")
    print(f"Tong: {results['total']}")
    
    return results

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch add additional fields to drugs')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default: dry run)')
    parser.add_argument('--limit', type=int, help='Limit number of drugs to process')
    
    args = parser.parse_args()
    
    dry_run = not args.apply
    
    results = batch_add_additional_fields(dry_run=dry_run, limit=args.limit)
    
    # Save report
    output_file = 'batch_add_additional_fields_report.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nDa luu bao cao: {output_file}")

