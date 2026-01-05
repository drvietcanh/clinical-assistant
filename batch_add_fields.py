"""
Script bổ sung field hàng loạt
Đọc danh sách thuốc từ report, bổ sung theo batch, tạo báo cáo tiến độ
"""
import sys
import json
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict
import io

# Setup path
sys.path.insert(0, str(Path.cwd()))

from add_fields_helper import (
    add_standard_fields, add_additional_fields, add_all_missing_fields,
    preview_changes
)
from field_templates_by_category import fill_missing_fields_with_template

# Setup encoding for Windows - only if not already set
if sys.platform == 'win32' and not isinstance(sys.stdout, io.TextIOWrapper):
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except:
        pass  # Already set or not needed

def load_drugs_report() -> Dict[str, Any]:
    """Load báo cáo thuốc cần bổ sung field"""
    report_file = Path('drugs_need_fields_report.json')
    if not report_file.exists():
        print(f"Khong tim thay file: {report_file}")
        return None
    
    with open(report_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def batch_add_standard_fields(dry_run: bool = True, limit: int = None) -> Dict[str, Any]:
    """
    Bổ sung field chuẩn cho tất cả thuốc thiếu
    
    Args:
        dry_run: Chỉ preview, không apply
        limit: Giới hạn số thuốc (None = tất cả)
    
    Returns:
        Dict chứa kết quả
    """
    report = load_drugs_report()
    if not report:
        return {'success': False, 'error': 'Cannot load report'}
    
    drugs_missing_standard = report.get('drugs_missing_standard_fields', [])
    
    if limit:
        drugs_missing_standard = drugs_missing_standard[:limit]
    
    results = {
        'total': len(drugs_missing_standard),
        'success': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }
    
    print("="*60)
    print(f"BAT DAU BO SUNG FIELD CHUAN")
    print(f"Tong so thuoc: {results['total']}")
    print(f"Dry run: {dry_run}")
    print("="*60)
    
    for i, drug_info in enumerate(drugs_missing_standard, 1):
        drug_name = drug_info['name']
        file_path = drug_info['file']
        missing_fields = drug_info.get('missing_standard', [])
        
        print(f"\n[{i}/{results['total']}] {drug_name}")
        print(f"  File: {file_path}")
        print(f"  Thieu {len(missing_fields)} field: {', '.join(missing_fields[:5])}")
        if len(missing_fields) > 5:
            print(f"  ... va {len(missing_fields) - 5} field khac")
        
        try:
            result = add_standard_fields(drug_name, file_path, dry_run=dry_run)
            
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
                    results['details'].append({
                        'drug_name': drug_name,
                        'file': file_path,
                        'status': 'skipped',
                        'reason': result.get('message', 'No fields to add')
                    })
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

def batch_add_specific_field(field_name: str, dry_run: bool = True, limit: int = None) -> Dict[str, Any]:
    """
    Bổ sung một field cụ thể cho tất cả thuốc thiếu field đó
    
    Args:
        field_name: Tên field cần bổ sung
        dry_run: Chỉ preview, không apply
        limit: Giới hạn số thuốc
    
    Returns:
        Dict chứa kết quả
    """
    report = load_drugs_report()
    if not report:
        return {'success': False, 'error': 'Cannot load report'}
    
    # Tìm tất cả thuốc thiếu field này
    drugs_missing_field = []
    for drug in report.get('drugs_missing_standard_fields', []):
        if field_name in drug.get('missing_standard', []):
            drugs_missing_field.append(drug)
    
    if limit:
        drugs_missing_field = drugs_missing_field[:limit]
    
    results = {
        'field_name': field_name,
        'total': len(drugs_missing_field),
        'success': 0,
        'failed': 0,
        'skipped': 0,
        'details': []
    }
    
    print("="*60)
    print(f"BAT DAU BO SUNG FIELD: {field_name}")
    print(f"Tong so thuoc: {results['total']}")
    print(f"Dry run: {dry_run}")
    print("="*60)
    
    for i, drug_info in enumerate(drugs_missing_field, 1):
        drug_name = drug_info['name']
        file_path = drug_info['file']
        
        print(f"\n[{i}/{results['total']}] {drug_name}")
        print(f"  File: {file_path}")
        
        try:
            # Preview để xem field có thiếu không
            preview = preview_changes(drug_name, file_path)
            
            if field_name in preview.get('missing_standard_fields', []):
                # Bổ sung tất cả field chuẩn (sẽ bao gồm field này)
                result = add_standard_fields(drug_name, file_path, dry_run=dry_run)
                
                if result['success']:
                    if field_name in result.get('added_fields', []):
                        results['success'] += 1
                        print(f"  ✓ Da bo sung field {field_name}")
                        results['details'].append({
                            'drug_name': drug_name,
                            'file': file_path,
                            'status': 'success'
                        })
                    else:
                        results['skipped'] += 1
                        print(f"  - Field {field_name} khong duoc bo sung")
                        results['details'].append({
                            'drug_name': drug_name,
                            'file': file_path,
                            'status': 'skipped',
                            'reason': f'Field {field_name} not in added fields'
                        })
                else:
                    results['failed'] += 1
                    print(f"  ✗ Loi: {result.get('error', 'Unknown error')}")
                    results['details'].append({
                        'drug_name': drug_name,
                        'file': file_path,
                        'status': 'failed',
                        'error': result.get('error', 'Unknown error')
                    })
            else:
                results['skipped'] += 1
                print(f"  - Field {field_name} khong thieu")
                results['details'].append({
                    'drug_name': drug_name,
                    'file': file_path,
                    'status': 'skipped',
                    'reason': f'Field {field_name} not missing'
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
    print(f"Field: {field_name}")
    print(f"Thanh cong: {results['success']}")
    print(f"Loi: {results['failed']}")
    print(f"Bo qua: {results['skipped']}")
    print(f"Tong: {results['total']}")
    
    return results

def generate_progress_report(results: Dict[str, Any], output_file: str = 'batch_add_fields_report.json'):
    """Tạo báo cáo tiến độ"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nDa luu bao cao: {output_file}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch add fields to drugs')
    parser.add_argument('--field', type=str, help='Field name to add (e.g., pregnancy)')
    parser.add_argument('--all-standard', action='store_true', help='Add all missing standard fields')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default: dry run)')
    parser.add_argument('--limit', type=int, help='Limit number of drugs to process')
    
    args = parser.parse_args()
    
    dry_run = not args.apply
    
    if args.field:
        # Bổ sung một field cụ thể
        results = batch_add_specific_field(args.field, dry_run=dry_run, limit=args.limit)
        generate_progress_report(results, f'batch_add_{args.field}_report.json')
    elif args.all_standard:
        # Bổ sung tất cả field chuẩn
        results = batch_add_standard_fields(dry_run=dry_run, limit=args.limit)
        generate_progress_report(results, 'batch_add_standard_fields_report.json')
    else:
        print("Usage:")
        print("  python batch_add_fields.py --field pregnancy --apply")
        print("  python batch_add_fields.py --all-standard --apply")
        print("  python batch_add_fields.py --field pregnancy --limit 10  # Dry run, limit 10 drugs")

