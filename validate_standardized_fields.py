"""
Script validation sau khi chuẩn hóa cấu trúc field
Kiểm tra tất cả field sau khi chuẩn hóa, đảm bảo không mất dữ liệu
"""
import sys
import json
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict
from datetime import datetime
import io

sys.path.insert(0, str(Path.cwd()))

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from drugs.field_validator import get_field_validator, STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS
from drugs.field_standardizer import get_field_standardizer
from field_structure_mapping_rules import STANDARD_STRUCTURES

def validate_field_structure(field_name: str, value: Any) -> Dict[str, Any]:
    """
    Validate cấu trúc của một field
    
    Returns:
        Dict với kết quả validation
    """
    result = {
        'field': field_name,
        'is_valid': True,
        'errors': [],
        'warnings': []
    }
    
    if field_name not in STANDARD_STRUCTURES:
        return result
    
    standard = STANDARD_STRUCTURES[field_name]
    
    # Kiểm tra type
    if standard['type'] == 'dict':
        if not isinstance(value, dict):
            result['is_valid'] = False
            result['errors'].append(f"Field phải là dict, nhận được {type(value).__name__}")
            return result
        
        # Kiểm tra required keys
        current_keys = set(value.keys())
        required_keys = set(standard['required_keys'])
        missing_keys = required_keys - current_keys
        
        if missing_keys:
            result['is_valid'] = False
            result['errors'].append(f"Thiếu keys: {', '.join(missing_keys)}")
        
        # Kiểm tra nested keys
        if 'lactation_nested_keys' in standard and 'lactation' in value:
            if isinstance(value['lactation'], dict):
                nested_keys = set(value['lactation'].keys())
                required_nested = set(standard['lactation_nested_keys'])
                missing_nested = required_nested - nested_keys
                
                if missing_nested:
                    result['is_valid'] = False
                    result['errors'].append(f"Thiếu nested keys trong lactation: {', '.join(missing_nested)}")
            else:
                result['is_valid'] = False
                result['errors'].append("lactation phải là dict")
    
    return result

def validate_all_drugs():
    """
    Validate tất cả thuốc sau khi chuẩn hóa
    """
    base_path = Path.cwd() / "drugs" / "drug_modules"
    validator = get_field_validator()
    
    results = {
        'total_drugs': 0,
        'valid_drugs': 0,
        'invalid_drugs': 0,
        'drugs_with_errors': [],
        'field_validation_summary': defaultdict(lambda: {'valid': 0, 'invalid': 0, 'errors': []})
    }
    
    def scan_directory(directory: Path):
        """Quét đệ quy một thư mục"""
        for item in sorted(directory.iterdir()):
            if item.name == '__init__.py' or item.name == '__pycache__' or item.name.endswith('.pyc'):
                continue
            
            if item.is_file() and item.suffix == '.py':
                try:
                    # Import module
                    rel_path = item.relative_to(Path.cwd())
                    module_name = rel_path.as_posix().replace('/', '.').replace('.py', '')
                    spec = __import__(module_name, fromlist=[''])
                    
                    # Tìm dict chứa drugs
                    drugs_dict = None
                    for attr_name in dir(spec):
                        if attr_name.endswith('_DRUGS') or (attr_name.isupper() and not attr_name.startswith('_')):
                            attr = getattr(spec, attr_name)
                            if isinstance(attr, dict):
                                drugs_dict = attr
                                break
                    
                    if not drugs_dict:
                        continue
                    
                    # Validate từng drug
                    for drug_name, drug_data in drugs_dict.items():
                        results['total_drugs'] += 1
                        drug_valid = True
                        drug_errors = []
                        
                        # Validate các field cần chuẩn hóa
                        for field_name in STANDARD_STRUCTURES.keys():
                            if field_name in drug_data:
                                field_validation = validate_field_structure(field_name, drug_data[field_name])
                                
                                if field_validation['is_valid']:
                                    results['field_validation_summary'][field_name]['valid'] += 1
                                else:
                                    results['field_validation_summary'][field_name]['invalid'] += 1
                                    drug_valid = False
                                    drug_errors.extend([
                                        f"{field_name}: {err}" 
                                        for err in field_validation['errors']
                                    ])
                        
                        if drug_valid:
                            results['valid_drugs'] += 1
                        else:
                            results['invalid_drugs'] += 1
                            results['drugs_with_errors'].append({
                                'drug': drug_name,
                                'file': str(item),
                                'errors': drug_errors
                            })
                
                except Exception as e:
                    print(f"Error reading {item}: {e}")
                    continue
            elif item.is_dir():
                scan_directory(item)
    
    print("Đang validate tất cả thuốc...")
    scan_directory(base_path)
    
    # Tạo báo cáo
    report = {
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'total_drugs': results['total_drugs'],
            'valid_drugs': results['valid_drugs'],
            'invalid_drugs': results['invalid_drugs'],
            'validation_rate': round(results['valid_drugs'] / results['total_drugs'] * 100, 2) if results['total_drugs'] > 0 else 0
        },
        'field_validation': dict(results['field_validation_summary']),
        'drugs_with_errors': results['drugs_with_errors'][:100]  # Giới hạn 100 đầu tiên
    }
    
    report_file = f'field_standardization_validation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # In summary
    print("\n" + "="*70)
    print("KẾT QUẢ VALIDATION")
    print("="*70)
    print(f"Tổng số thuốc: {results['total_drugs']}")
    print(f"Thuốc hợp lệ: {results['valid_drugs']} ({report['summary']['validation_rate']}%)")
    print(f"Thuốc không hợp lệ: {results['invalid_drugs']}")
    
    print("\nValidation theo field:")
    for field_name, stats in results['field_validation_summary'].items():
        total = stats['valid'] + stats['invalid']
        if total > 0:
            rate = round(stats['valid'] / total * 100, 2)
            print(f"  {field_name}: {stats['valid']}/{total} ({rate}%)")
            if stats['invalid'] > 0:
                print(f"    - Lỗi: {stats['invalid']}")
    
    if results['drugs_with_errors']:
        print(f"\nThuốc có lỗi (hiển thị {min(10, len(results['drugs_with_errors']))} đầu tiên):")
        for drug_error in results['drugs_with_errors'][:10]:
            print(f"  - {drug_error['drug']}: {', '.join(drug_error['errors'][:2])}")
    
    print(f"\nBáo cáo chi tiết: {report_file}")
    print("="*70)
    
    return report

if __name__ == "__main__":
    validate_all_drugs()

