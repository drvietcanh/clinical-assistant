"""
Script chuẩn hóa cấu trúc field cho tất cả thuốc
Sử dụng add_fields_helper để load và write file
"""
import sys
import json
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from collections import defaultdict
from datetime import datetime
import io

sys.path.insert(0, str(Path.cwd()))

# Setup encoding for Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

from field_structure_mapping_rules import standardize_all_fields
from add_fields_helper import load_drug_from_file, update_drug_in_file, format_drug_dict

def load_drugs_need_fix() -> Dict[str, List[Dict]]:
    """Load danh sách thuốc cần sửa từ báo cáo"""
    try:
        with open('field_standardization_analysis.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('drugs_need_fix', {})
    except FileNotFoundError:
        print("Warning: field_standardization_analysis.json not found.")
        return {}

def standardize_drugs(dry_run: bool = True, limit: Optional[int] = None):
    """
    Chuẩn hóa cấu trúc field cho tất cả thuốc cần sửa
    """
    drugs_need_fix = load_drugs_need_fix()
    
    if not drugs_need_fix:
        print("Không có thuốc nào cần chuẩn hóa.")
        return
    
    # Nhóm thuốc theo file
    drugs_by_file = defaultdict(lambda: defaultdict(list))
    for field_name, drugs in drugs_need_fix.items():
        for drug_info in drugs:
            file_path = drug_info['file'].replace('\\', '/')
            drug_name = drug_info['drug']
            drugs_by_file[file_path][drug_name].append({
                'field': field_name,
                'fix_type': drug_info.get('fix_type'),
                'fix_details': drug_info.get('fix_details', {})
            })
    
    total_files = len(drugs_by_file)
    processed_files = 0
    all_changes = []
    
    print(f"\n{'DRY RUN - ' if dry_run else ''}Chuẩn hóa cấu trúc field")
    print(f"Số file cần xử lý: {total_files}")
    if limit:
        print(f"Giới hạn: {limit} file đầu tiên")
    print("="*70)
    
    for file_path_str, drugs_dict in list(drugs_by_file.items())[:limit] if limit else drugs_by_file.items():
        file_path = Path(file_path_str)
        if not file_path.exists():
            # Thử với đường dẫn tương đối
            file_path = Path("drugs/drug_modules") / file_path_str.replace("drugs\\drug_modules\\", "").replace("drugs/drug_modules/", "")
            if not file_path.exists():
                print(f"Warning: File không tồn tại: {file_path_str}")
                continue
        
        processed_files += 1
        print(f"\n[{processed_files}/{total_files}] {file_path.name}")
        
        file_changes = {
            'file': str(file_path),
            'drugs': []
        }
        
        for drug_name, fields_info in drugs_dict.items():
            try:
                # Load drug
                drug_data = load_drug_from_file(file_path, drug_name)
                if not drug_data:
                    print(f"  ✗ Không load được: {drug_name}")
                    continue
                
                # Chuẩn hóa các field
                drug_changes = {
                    'drug': drug_name,
                    'fields': []
                }
                
                original_drug = drug_data.copy()
                standardized_drug = standardize_all_fields(drug_data)
                
                # Kiểm tra thay đổi
                for field_name in fields_info:
                    field_name_str = field_name['field']
                    if field_name_str in original_drug:
                        old_value = original_drug[field_name_str]
                        new_value = standardized_drug.get(field_name_str)
                        
                        if old_value != new_value:
                            drug_changes['fields'].append({
                                'field': field_name_str,
                                'fix_type': field_name.get('fix_type'),
                                'old_value_preview': str(old_value)[:100] if old_value else None,
                                'new_value_preview': str(new_value)[:100] if new_value else None
                            })
                            drug_data[field_name_str] = new_value
                
                if drug_changes['fields']:
                    file_changes['drugs'].append(drug_changes)
                    print(f"  ✓ {drug_name}: {len(drug_changes['fields'])} field(s)")
                    
                    # Apply changes
                    if not dry_run:
                        success = update_drug_in_file(file_path, drug_name, drug_data, dry_run=False)
                        if success:
                            print(f"    → Đã cập nhật file")
                        else:
                            print(f"    ✗ Lỗi khi cập nhật file")
                
            except Exception as e:
                print(f"  ✗ Lỗi với {drug_name}: {e}")
                import traceback
                traceback.print_exc()
        
        if file_changes['drugs']:
            all_changes.append(file_changes)
    
    # Tạo báo cáo
    report = {
        'timestamp': datetime.now().isoformat(),
        'dry_run': dry_run,
        'total_files_processed': processed_files,
        'total_drugs_changed': sum(len(fc['drugs']) for fc in all_changes),
        'total_fields_changed': sum(
            len(drug['fields']) 
            for fc in all_changes 
            for drug in fc['drugs']
        ),
        'changes': all_changes
    }
    
    report_file = f'field_standardization_report_{"dryrun" if dry_run else "applied"}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*70}")
    print(f"Hoàn thành!")
    print(f"  - Files đã xử lý: {processed_files}")
    print(f"  - Thuốc đã thay đổi: {report['total_drugs_changed']}")
    print(f"  - Field đã thay đổi: {report['total_fields_changed']}")
    print(f"  - Báo cáo: {report_file}")
    print(f"{'='*70}")
    
    return report

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Chuẩn hóa cấu trúc field cho tất cả thuốc')
    parser.add_argument('--apply', action='store_true', help='Áp dụng thay đổi (mặc định là dry-run)')
    parser.add_argument('--limit', type=int, help='Giới hạn số file xử lý')
    args = parser.parse_args()
    
    dry_run = not args.apply
    
    if dry_run:
        print("="*70)
        print("CHẾ ĐỘ DRY-RUN - Không thay đổi file")
        print("="*70)
    else:
        print("="*70)
        print("CHẾ ĐỘ APPLY - Sẽ thay đổi file và tạo backup")
        print("="*70)
        response = input("Bạn có chắc chắn muốn tiếp tục? (yes/no): ")
        if response.lower() != 'yes':
            print("Đã hủy.")
            return
    
    report = standardize_drugs(dry_run=dry_run, limit=args.limit)
    
    if dry_run:
        print("\nChạy với --apply để áp dụng thay đổi.")

if __name__ == "__main__":
    main()

