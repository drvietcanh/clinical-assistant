"""
Script phân tích toàn diện cấu trúc hệ thống thuốc
Quét tất cả file, đếm thuốc, phát hiện vấn đề, kiểm tra field
"""
import ast
import json
import os
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from collections import defaultdict
from datetime import datetime

# 14 field chuẩn
STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

# 8 field bổ sung
ADDITIONAL_8_FIELDS = [
    "black_box_warnings", "drug_interactions", "pregnancy_lactation",
    "hepatic_adjustment", "overdose_management", "reversal_agents",
    "administration_instructions", "references"
]

ALL_FIELDS = STANDARD_14_FIELDS + ADDITIONAL_8_FIELDS

# Field names không phải là tên thuốc
KNOWN_NON_DRUGS = {
    'risk_flags', 'organ_toxicity', 'pediatric_dosing', 'geriatric_dosing',
    'brand_names', 'cost_estimate', 'contraindications_detail',
    'reversal_agents', 'dosage', 'renal_adjustment', 'pharmacokinetics',
    'drug_interactions', 'references', 'pregnancy_lactation',
    'hepatic_adjustment', 'overdose_management', 'administration_instructions',
    'contraindications', 'side_effects', 'interactions', 'pregnancy',
    'administration', 'indications', 'group', 'vietnamese_name',
    'oral', 'im', 'sc', 'inhaled', 'inhalation', 'iv', 'po',
    'normal', '30_60', 'under_30', 'mild', 'moderate', 'severe',
    'major', 'minor', 'tuyệt_đối', 'tương_đối',
    'adult_standard', 'adult_high_dose', 'pediatric', 'notes',
    'hypertension', 'heart_failure', 'common', 'vietnam',
}

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):  # ast.Str (deprecated)
        return node.s
    return None

def extract_dict_keys(node: ast.Dict) -> Set[str]:
    """Trích xuất các keys từ AST Dict node"""
    keys = set()
    for key_node in node.keys:
        key = get_string_value(key_node)
        if key:
            keys.add(key)
    return keys

def is_drug_entry(keys: Set[str]) -> bool:
    """Kiểm tra xem dict có phải là entry thuốc không"""
    required_fields = {'group', 'vietnamese_name', 'administration', 'indications'}
    return len(keys & required_fields) >= 2

def is_not_field_name(name: str) -> bool:
    """Kiểm tra xem tên có phải là field name không"""
    if name in KNOWN_NON_DRUGS:
        return False
    
    if name.islower() and name.count('_') >= 2:
        if name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']:
            return False
    
    return True

def find_drugs_in_file(file_path: Path) -> Dict[str, Dict[str, Any]]:
    """Tìm tất cả thuốc trong một file"""
    drugs = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            return {'_syntax_error': str(e)}
        
        # Tìm tất cả assignments to _DRUGS variables
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        if isinstance(node.value, ast.Dict):
                            # Đây là dictionary chứa thuốc
                            for key_node, value_node in zip(node.value.keys, node.value.values):
                                drug_name = get_string_value(key_node)
                                
                                if drug_name and is_not_field_name(drug_name):
                                    if isinstance(value_node, ast.Dict):
                                        keys = extract_dict_keys(value_node)
                                        if is_drug_entry(keys):
                                            # Kiểm tra field
                                            missing_standard = [f for f in STANDARD_14_FIELDS if f not in keys]
                                            missing_additional = [f for f in ADDITIONAL_8_FIELDS if f not in keys]
                                            
                                            drugs[drug_name] = {
                                                'file': str(file_path),
                                                'fields': list(keys),
                                                'field_count': len(keys),
                                                'has_all_14_fields': len(missing_standard) == 0,
                                                'missing_standard_fields': missing_standard,
                                                'missing_additional_fields': missing_additional,
                                                'has_all_22_fields': len(missing_standard) == 0 and len(missing_additional) == 0,
                                            }
        
        # Nếu không tìm thấy qua _DRUGS, tìm trực tiếp trong dict
        if not drugs:
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    for key_node, value_node in zip(node.keys, node.values):
                        drug_name = get_string_value(key_node)
                        if drug_name and is_not_field_name(drug_name):
                            if isinstance(value_node, ast.Dict):
                                keys = extract_dict_keys(value_node)
                                if is_drug_entry(keys):
                                    missing_standard = [f for f in STANDARD_14_FIELDS if f not in keys]
                                    missing_additional = [f for f in ADDITIONAL_8_FIELDS if f not in keys]
                                    
                                    if drug_name not in drugs:
                                        drugs[drug_name] = {
                                            'file': str(file_path),
                                            'fields': list(keys),
                                            'field_count': len(keys),
                                            'has_all_14_fields': len(missing_standard) == 0,
                                            'missing_standard_fields': missing_standard,
                                            'missing_additional_fields': missing_additional,
                                            'has_all_22_fields': len(missing_standard) == 0 and len(missing_additional) == 0,
                                        }
    
    except Exception as e:
        return {'_error': str(e)}
    
    return drugs

def analyze_module_structure(module_path: Path) -> Dict[str, Any]:
    """Phân tích cấu trúc một module"""
    module_info = {
        'path': str(module_path),
        'is_folder': module_path.is_dir(),
        'is_file': module_path.is_file(),
        'size_kb': 0,
        'drugs': {},
        'drug_count': 0,
        'files': [],
        'submodules': [],
        'has_syntax_errors': False,
        'syntax_errors': [],
        'large_files': [],  # Files > 100KB
    }
    
    if module_path.is_file():
        # File đơn
        size = module_path.stat().st_size / 1024
        module_info['size_kb'] = size
        if size > 100:
            module_info['large_files'].append({
                'file': str(module_path),
                'size_kb': size
            })
        
        drugs = find_drugs_in_file(module_path)
        if '_syntax_error' in drugs:
            module_info['has_syntax_errors'] = True
            module_info['syntax_errors'].append({
                'file': str(module_path),
                'error': drugs['_syntax_error']
            })
        elif '_error' in drugs:
            module_info['has_syntax_errors'] = True
            module_info['syntax_errors'].append({
                'file': str(module_path),
                'error': drugs['_error']
            })
        else:
            module_info['drugs'] = drugs
            module_info['drug_count'] = len(drugs)
    
    elif module_path.is_dir():
        # Folder với submodules
        for item in sorted(module_path.iterdir()):
            if item.name == '__init__.py' or item.name.endswith('.pyc') or item.name == '__pycache__':
                continue
            
            if item.is_file() and item.suffix == '.py':
                size = item.stat().st_size / 1024
                module_info['size_kb'] += size
                if size > 100:
                    module_info['large_files'].append({
                        'file': str(item),
                        'size_kb': size
                    })
                
                drugs = find_drugs_in_file(item)
                if '_syntax_error' in drugs:
                    module_info['has_syntax_errors'] = True
                    module_info['syntax_errors'].append({
                        'file': str(item),
                        'error': drugs['_syntax_error']
                    })
                elif '_error' in drugs:
                    module_info['has_syntax_errors'] = True
                    module_info['syntax_errors'].append({
                        'file': str(item),
                        'error': drugs['_error']
                    })
                else:
                    module_info['drugs'].update(drugs)
                    module_info['files'].append({
                        'file': str(item),
                        'size_kb': size,
                        'drug_count': len(drugs)
                    })
            
            elif item.is_dir():
                submodule_info = analyze_module_structure(item)
                module_info['submodules'].append(submodule_info)
                module_info['drugs'].update(submodule_info['drugs'])
                module_info['size_kb'] += submodule_info['size_kb']
                if submodule_info['has_syntax_errors']:
                    module_info['has_syntax_errors'] = True
                    module_info['syntax_errors'].extend(submodule_info['syntax_errors'])
                module_info['large_files'].extend(submodule_info['large_files'])
        
        module_info['drug_count'] = len(module_info['drugs'])
    
    return module_info

def find_duplicate_drugs(all_drugs: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    """Tìm thuốc trùng lặp (cùng tên nhưng ở file khác)"""
    drug_locations = defaultdict(list)
    
    for drug_name, drug_info in all_drugs.items():
        drug_locations[drug_name].append(drug_info['file'])
    
    duplicates = {name: files for name, files in drug_locations.items() if len(files) > 1}
    return duplicates

def generate_statistics(modules: Dict[str, Any], all_drugs: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Tạo thống kê tổng hợp"""
    stats = {
        'total_drugs': len(all_drugs),
        'total_modules': len(modules),
        'modules_with_subfolder': 0,
        'modules_as_single_file': 0,
        'total_files': 0,
        'files_with_syntax_errors': 0,
        'large_files_count': 0,
        'drugs_with_all_14_fields': 0,
        'drugs_with_all_22_fields': 0,
        'field_statistics': defaultdict(int),
        'module_statistics': {},
        'duplicate_drugs_count': 0,
    }
    
    # Thống kê module
    for module_name, module_info in modules.items():
        if module_info['is_folder']:
            stats['modules_with_subfolder'] += 1
        else:
            stats['modules_as_single_file'] += 1
        
        stats['total_files'] += len(module_info.get('files', []))
        if module_info['has_syntax_errors']:
            stats['files_with_syntax_errors'] += len(module_info['syntax_errors'])
        stats['large_files_count'] += len(module_info.get('large_files', []))
        
        stats['module_statistics'][module_name] = {
            'drug_count': module_info['drug_count'],
            'size_kb': module_info['size_kb'],
            'has_subfolder': module_info['is_folder'],
            'has_errors': module_info['has_syntax_errors'],
        }
    
    # Thống kê field
    for drug_name, drug_info in all_drugs.items():
        if drug_info['has_all_14_fields']:
            stats['drugs_with_all_14_fields'] += 1
        if drug_info['has_all_22_fields']:
            stats['drugs_with_all_22_fields'] += 1
        
        for field in drug_info['fields']:
            stats['field_statistics'][field] += 1
    
    # Tìm duplicate
    duplicates = find_duplicate_drugs(all_drugs)
    stats['duplicate_drugs_count'] = len(duplicates)
    
    return stats

def main():
    """Hàm chính"""
    import sys
    import io
    # Fix encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("Bat dau phan tich he thong thuoc...")
    
    base_path = Path("drugs/drug_modules")
    if not base_path.exists():
        print(f"Khong tim thay thu muc: {base_path}")
        return
    
    # Phân tích từng module
    modules = {}
    all_drugs = {}
    
    for item in sorted(base_path.iterdir()):
        if item.name == '__init__.py' or item.name == '__pycache__':
            continue
        
        if item.suffix == '.py' or item.is_dir():
            print(f"Dang phan tich: {item.name}")
            module_info = analyze_module_structure(item)
            modules[item.stem if item.is_file() else item.name] = module_info
            all_drugs.update(module_info['drugs'])
    
    # Tạo thống kê
    stats = generate_statistics(modules, all_drugs)
    
    # Tìm duplicate
    duplicates = find_duplicate_drugs(all_drugs)
    
    # Tạo báo cáo
    report = {
        'analysis_date': datetime.now().isoformat(),
        'statistics': stats,
        'modules': modules,
        'all_drugs': all_drugs,
        'duplicates': duplicates,
        'missing_fields_report': {
            drug_name: {
                'file': info['file'],
                'missing_standard': info['missing_standard_fields'],
                'missing_additional': info['missing_additional_fields'],
            }
            for drug_name, info in all_drugs.items()
            if info['missing_standard_fields'] or info['missing_additional_fields']
        }
    }
    
    # Lưu JSON report
    output_json = "drug_system_analysis_report.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Da luu bao cao JSON: {output_json}")
    
    # Lưu missing fields report
    missing_fields_json = "missing_fields_report.json"
    with open(missing_fields_json, 'w', encoding='utf-8') as f:
        json.dump(report['missing_fields_report'], f, indent=2, ensure_ascii=False)
    print(f"Da luu missing fields report: {missing_fields_json}")
    
    # Lưu duplicate report
    duplicate_json = "duplicate_drugs_report.json"
    with open(duplicate_json, 'w', encoding='utf-8') as f:
        json.dump(duplicates, f, indent=2, ensure_ascii=False)
    print(f"Da luu duplicate report: {duplicate_json}")
    
    # Tạo markdown report
    md_report = generate_markdown_report(report, stats)
    output_md = "drug_system_analysis_report.md"
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(md_report)
    print(f"Da luu bao cao Markdown: {output_md}")
    
    # In tóm tắt
    print("\n" + "="*60)
    print("TOM TAT PHAN TICH")
    print("="*60)
    print(f"Tổng số thuốc: {stats['total_drugs']}")
    print(f"Tổng số modules: {stats['total_modules']}")
    print(f"Modules có subfolder: {stats['modules_with_subfolder']}")
    print(f"Modules là file đơn: {stats['modules_as_single_file']}")
    print(f"Files có lỗi syntax: {stats['files_with_syntax_errors']}")
    print(f"Files lớn (>100KB): {stats['large_files_count']}")
    print(f"Thuốc có đủ 14 field: {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)")
    print(f"Thuốc có đủ 22 field: {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)")
    print(f"Thuốc trùng lặp: {stats['duplicate_drugs_count']}")
    print("="*60)

def generate_markdown_report(report: Dict, stats: Dict) -> str:
    """Tạo báo cáo markdown"""
    md = f"""# Báo Cáo Phân Tích Hệ Thống Thuốc

**Ngày phân tích:** {report['analysis_date']}

## 📊 Tổng Quan

- **Tổng số thuốc:** {stats['total_drugs']}
- **Tổng số modules:** {stats['total_modules']}
- **Modules có subfolder:** {stats['modules_with_subfolder']}
- **Modules là file đơn:** {stats['modules_as_single_file']}
- **Files có lỗi syntax:** {stats['files_with_syntax_errors']}
- **Files lớn (>100KB):** {stats['large_files_count']}

## 📈 Thống Kê Field

- **Thuốc có đủ 14 field chuẩn:** {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)
- **Thuốc có đủ 22 field (14 + 8):** {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)

### Thống kê từng field:

"""
    
    for field in ALL_FIELDS:
        count = stats['field_statistics'].get(field, 0)
        percentage = count / stats['total_drugs'] * 100 if stats['total_drugs'] > 0 else 0
        md += f"- `{field}`: {count} thuốc ({percentage:.1f}%)\n"
    
    md += f"""
## 📁 Thống Kê Module

"""
    
    for module_name, module_stats in sorted(stats['module_statistics'].items(), key=lambda x: x[1]['drug_count'], reverse=True):
        md += f"### {module_name}\n"
        md += f"- Số thuốc: {module_stats['drug_count']}\n"
        md += f"- Kích thước: {module_stats['size_kb']:.1f} KB\n"
        md += f"- Co subfolder: {'Co' if module_stats['has_subfolder'] else 'Khong'}\n"
        md += f"- Co loi: {'Co' if module_stats['has_errors'] else 'Khong'}\n"
        md += "\n"
    
    if report['duplicates']:
        md += f"""
## Thuoc Trung Lap

Tìm thấy {len(report['duplicates'])} thuốc trùng lặp:

"""
        for drug_name, files in list(report['duplicates'].items())[:20]:
            md += f"- **{drug_name}**: {len(files)} vị trí\n"
            for file in files:
                md += f"  - {file}\n"
    
    if stats['files_with_syntax_errors'] > 0:
        md += f"""
## Files Co Loi Syntax

Tìm thấy {stats['files_with_syntax_errors']} file có lỗi syntax. Xem chi tiết trong JSON report.

"""
    
    if stats['large_files_count'] > 0:
        md += f"""
## 📦 Files Lớn (>100KB)

Tìm thấy {stats['large_files_count']} file lớn. Nên tách thành subfolder.

"""
    
    md += f"""
## 📋 Thuốc Thiếu Field

Tìm thấy {len(report['missing_fields_report'])} thuốc thiếu field. Xem chi tiết trong `missing_fields_report.json`.

"""
    
    return md

if __name__ == "__main__":
    main()

