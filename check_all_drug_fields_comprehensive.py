"""
Script kiểm tra field toàn diện cho tất cả thuốc
Kiểm tra 14 field chuẩn + 8 field bổ sung
Tạo báo cáo chi tiết và danh sách ưu tiên sửa
"""
import ast
import json
from pathlib import Path
from typing import Dict, List, Set, Any
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

def check_field_value(node: ast.AST, field_name: str) -> Dict[str, Any]:
    """Kiểm tra giá trị của field"""
    result = {
        'exists': False,
        'is_empty': False,
        'type': None,
        'value_preview': None,
    }
    
    if isinstance(node, ast.Dict):
        result['exists'] = True
        result['type'] = 'dict'
        if len(node.keys) == 0:
            result['is_empty'] = True
        else:
            # Lấy preview của value đầu tiên
            if node.keys:
                first_key = get_string_value(node.keys[0])
                if first_key:
                    result['value_preview'] = f"dict with keys: {first_key}..."
    
    elif isinstance(node, ast.List):
        result['exists'] = True
        result['type'] = 'list'
        if len(node.elts) == 0:
            result['is_empty'] = True
        else:
            # Lấy preview của phần tử đầu tiên
            if node.elts:
                first_elt = get_string_value(node.elts[0])
                if first_elt:
                    result['value_preview'] = f"list: {first_elt[:50]}..."
    
    elif isinstance(node, (ast.Constant, ast.Str)):
        result['exists'] = True
        value = get_string_value(node) if isinstance(node, ast.Constant) else node.s
        result['type'] = 'string'
        if not value or value.strip() == '':
            result['is_empty'] = True
        else:
            result['value_preview'] = value[:50] + "..." if len(value) > 50 else value
    
    elif isinstance(node, ast.NameConstant):  # None, True, False
        result['exists'] = True
        result['type'] = 'constant'
        result['value_preview'] = str(node.value)
        if node.value is None:
            result['is_empty'] = True
    
    return result

def find_drugs_with_field_details(file_path: Path) -> Dict[str, Dict[str, Any]]:
    """Tìm tất cả thuốc trong file và kiểm tra chi tiết field"""
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
                            for key_node, value_node in zip(node.value.keys, node.value.values):
                                drug_name = get_string_value(key_node)
                                
                                if drug_name and is_not_field_name(drug_name):
                                    if isinstance(value_node, ast.Dict):
                                        keys = extract_dict_keys(value_node)
                                        if is_drug_entry(keys):
                                            # Kiểm tra chi tiết từng field
                                            field_details = {}
                                            
                                            # Tạo mapping key_node -> value_node để tìm field
                                            field_nodes = {}
                                            for k_node, v_node in zip(value_node.keys, value_node.values):
                                                field_key = get_string_value(k_node)
                                                if field_key:
                                                    field_nodes[field_key] = v_node
                                            
                                            # Kiểm tra 14 field chuẩn
                                            for field in STANDARD_14_FIELDS:
                                                if field in field_nodes:
                                                    field_details[field] = check_field_value(field_nodes[field], field)
                                                else:
                                                    field_details[field] = {'exists': False}
                                            
                                            # Kiểm tra 8 field bổ sung
                                            for field in ADDITIONAL_8_FIELDS:
                                                if field in field_nodes:
                                                    field_details[field] = check_field_value(field_nodes[field], field)
                                                else:
                                                    field_details[field] = {'exists': False}
                                            
                                            # Tính toán thống kê
                                            missing_standard = [f for f in STANDARD_14_FIELDS if not field_details[f]['exists']]
                                            missing_additional = [f for f in ADDITIONAL_8_FIELDS if not field_details[f]['exists']]
                                            empty_fields = [f for f in ALL_FIELDS if field_details.get(f, {}).get('is_empty', False)]
                                            
                                            drugs[drug_name] = {
                                                'file': str(file_path),
                                                'fields': list(keys),
                                                'field_count': len(keys),
                                                'field_details': field_details,
                                                'has_all_14_fields': len(missing_standard) == 0,
                                                'has_all_22_fields': len(missing_standard) == 0 and len(missing_additional) == 0,
                                                'missing_standard_fields': missing_standard,
                                                'missing_additional_fields': missing_additional,
                                                'empty_fields': empty_fields,
                                                'missing_field_count': len(missing_standard) + len(missing_additional),
                                            }
        
        # Nếu không tìm thấy qua _DRUGS, tìm trực tiếp
        if not drugs:
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    for key_node, value_node in zip(node.keys, node.values):
                        drug_name = get_string_value(key_node)
                        if drug_name and is_not_field_name(drug_name):
                            if isinstance(value_node, ast.Dict):
                                keys = extract_dict_keys(value_node)
                                if is_drug_entry(keys):
                                    if drug_name not in drugs:
                                        field_details = {}
                                        field_nodes = {}
                                        for k_node, v_node in zip(value_node.keys, value_node.values):
                                            field_key = get_string_value(k_node)
                                            if field_key:
                                                field_nodes[field_key] = v_node
                                        
                                        for field in ALL_FIELDS:
                                            if field in field_nodes:
                                                field_details[field] = check_field_value(field_nodes[field], field)
                                            else:
                                                field_details[field] = {'exists': False}
                                        
                                        missing_standard = [f for f in STANDARD_14_FIELDS if not field_details[f]['exists']]
                                        missing_additional = [f for f in ADDITIONAL_8_FIELDS if not field_details[f]['exists']]
                                        empty_fields = [f for f in ALL_FIELDS if field_details.get(f, {}).get('is_empty', False)]
                                        
                                        drugs[drug_name] = {
                                            'file': str(file_path),
                                            'fields': list(keys),
                                            'field_count': len(keys),
                                            'field_details': field_details,
                                            'has_all_14_fields': len(missing_standard) == 0,
                                            'has_all_22_fields': len(missing_standard) == 0 and len(missing_additional) == 0,
                                            'missing_standard_fields': missing_standard,
                                            'missing_additional_fields': missing_additional,
                                            'empty_fields': empty_fields,
                                            'missing_field_count': len(missing_standard) + len(missing_additional),
                                        }
    
    except Exception as e:
        return {'_error': str(e)}
    
    return drugs

def scan_all_drugs() -> Dict[str, Dict[str, Any]]:
    """Quét tất cả thuốc trong hệ thống"""
    base_path = Path("drugs/drug_modules")
    all_drugs = {}
    
    def scan_directory(directory: Path):
        """Quét đệ quy một thư mục"""
        for item in sorted(directory.iterdir()):
            if item.name == '__init__.py' or item.name == '__pycache__' or item.name.endswith('.pyc'):
                continue
            
            if item.is_file() and item.suffix == '.py':
                drugs = find_drugs_with_field_details(item)
                if '_syntax_error' not in drugs and '_error' not in drugs:
                    all_drugs.update(drugs)
            elif item.is_dir():
                scan_directory(item)
    
    scan_directory(base_path)
    return all_drugs

def generate_priority_list(all_drugs: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Tạo danh sách ưu tiên sửa (thuốc thiếu nhiều field nhất)"""
    priority_list = []
    
    for drug_name, drug_info in all_drugs.items():
        priority_list.append({
            'drug_name': drug_name,
            'file': drug_info['file'],
            'missing_field_count': drug_info['missing_field_count'],
            'missing_standard': drug_info['missing_standard_fields'],
            'missing_additional': drug_info['missing_additional_fields'],
            'empty_fields': drug_info['empty_fields'],
        })
    
    # Sắp xếp theo số field thiếu (nhiều nhất trước)
    priority_list.sort(key=lambda x: x['missing_field_count'], reverse=True)
    
    return priority_list

def generate_statistics(all_drugs: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Tạo thống kê"""
    stats = {
        'total_drugs': len(all_drugs),
        'drugs_with_all_14_fields': 0,
        'drugs_with_all_22_fields': 0,
        'field_statistics': defaultdict(int),
        'missing_field_statistics': defaultdict(int),
        'empty_field_statistics': defaultdict(int),
        'module_statistics': defaultdict(lambda: {
            'total': 0,
            'with_all_14': 0,
            'with_all_22': 0,
            'missing_fields': 0,
        }),
    }
    
    for drug_name, drug_info in all_drugs.items():
        # Thống kê field
        for field in ALL_FIELDS:
            if drug_info['field_details'].get(field, {}).get('exists', False):
                stats['field_statistics'][field] += 1
            else:
                stats['missing_field_statistics'][field] += 1
            
            if drug_info['field_details'].get(field, {}).get('is_empty', False):
                stats['empty_field_statistics'][field] += 1
        
        # Thống kê tổng
        if drug_info['has_all_14_fields']:
            stats['drugs_with_all_14_fields'] += 1
        if drug_info['has_all_22_fields']:
            stats['drugs_with_all_22_fields'] += 1
        
        # Thống kê theo module (từ file path)
        module_name = Path(drug_info['file']).parts[1] if len(Path(drug_info['file']).parts) > 1 else 'unknown'
        stats['module_statistics'][module_name]['total'] += 1
        if drug_info['has_all_14_fields']:
            stats['module_statistics'][module_name]['with_all_14'] += 1
        if drug_info['has_all_22_fields']:
            stats['module_statistics'][module_name]['with_all_22'] += 1
        if drug_info['missing_field_count'] > 0:
            stats['module_statistics'][module_name]['missing_fields'] += 1
    
    return stats

def main():
    """Hàm chính"""
    import sys
    import io
    # Fix encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("Bat dau kiem tra field cho tat ca thuoc...")
    
    # Quét tất cả thuốc
    print("Dang quet tat ca file...")
    all_drugs = scan_all_drugs()
    print(f"Tim thay {len(all_drugs)} thuoc")
    
    # Tạo thống kê
    print("Dang tao thong ke...")
    stats = generate_statistics(all_drugs)
    
    # Tạo danh sách ưu tiên
    print("Dang tao danh sach uu tien...")
    priority_list = generate_priority_list(all_drugs)
    
    # Tạo báo cáo
    report = {
        'check_date': datetime.now().isoformat(),
        'statistics': stats,
        'all_drugs': all_drugs,
        'priority_list': priority_list,
        'drugs_missing_standard_fields': [
            {
                'drug_name': name,
                'file': info['file'],
                'missing_fields': info['missing_standard_fields'],
            }
            for name, info in all_drugs.items()
            if info['missing_standard_fields']
        ],
        'drugs_missing_additional_fields': [
            {
                'drug_name': name,
                'file': info['file'],
                'missing_fields': info['missing_additional_fields'],
            }
            for name, info in all_drugs.items()
            if info['missing_additional_fields']
        ],
    }
    
    # Lưu báo cáo JSON
    output_json = "comprehensive_field_check_report.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Da luu bao cao JSON: {output_json}")
    
    # Lưu danh sách ưu tiên
    priority_json = "field_priority_list.json"
    with open(priority_json, 'w', encoding='utf-8') as f:
        json.dump(priority_list, f, indent=2, ensure_ascii=False)
    print(f"Da luu danh sach uu tien: {priority_json}")
    
    # Tạo markdown report
    md_report = generate_markdown_report(report, stats, priority_list)
    output_md = "comprehensive_field_check_report.md"
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(md_report)
    print(f"Da luu bao cao Markdown: {output_md}")
    
    # In tóm tắt
    print("\n" + "="*60)
    print("TOM TAT KIEM TRA FIELD")
    print("="*60)
    print(f"Tong so thuoc: {stats['total_drugs']}")
    print(f"Thuoc co du 14 field chuan: {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)")
    print(f"Thuoc co du 22 field (14 + 8): {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)")
    print(f"\nTop 10 field thieu nhieu nhat:")
    sorted_missing = sorted(stats['missing_field_statistics'].items(), key=lambda x: x[1], reverse=True)
    for field, count in sorted_missing[:10]:
        print(f"  - {field}: {count} thuoc ({count/stats['total_drugs']*100:.1f}%)")
    print("="*60)

def generate_markdown_report(report: Dict, stats: Dict, priority_list: List) -> str:
    """Tạo báo cáo markdown"""
    md = f"""# Bao Cao Kiem Tra Field Toan Dien

**Ngay kiem tra:** {report['check_date']}

## Tong Quan

- **Tong so thuoc:** {stats['total_drugs']}
- **Thuoc co du 14 field chuan:** {stats['drugs_with_all_14_fields']} ({stats['drugs_with_all_14_fields']/stats['total_drugs']*100:.1f}%)
- **Thuoc co du 22 field (14 + 8):** {stats['drugs_with_all_22_fields']} ({stats['drugs_with_all_22_fields']/stats['total_drugs']*100:.1f}%)

## Thong Ke Field

### 14 Field Chuan

"""
    
    for field in STANDARD_14_FIELDS:
        has_count = stats['field_statistics'].get(field, 0)
        missing_count = stats['missing_field_statistics'].get(field, 0)
        empty_count = stats['empty_field_statistics'].get(field, 0)
        percentage = has_count / stats['total_drugs'] * 100 if stats['total_drugs'] > 0 else 0
        md += f"- `{field}`: {has_count} co ({percentage:.1f}%), {missing_count} thieu, {empty_count} rong\n"
    
    md += "\n### 8 Field Bo Sung\n\n"
    
    for field in ADDITIONAL_8_FIELDS:
        has_count = stats['field_statistics'].get(field, 0)
        missing_count = stats['missing_field_statistics'].get(field, 0)
        empty_count = stats['empty_field_statistics'].get(field, 0)
        percentage = has_count / stats['total_drugs'] * 100 if stats['total_drugs'] > 0 else 0
        md += f"- `{field}`: {has_count} co ({percentage:.1f}%), {missing_count} thieu, {empty_count} rong\n"
    
    md += f"""
## Danh Sach Uu Tien Sua

Top 20 thuoc thieu nhieu field nhat:

"""
    
    for i, item in enumerate(priority_list[:20], 1):
        md += f"{i}. **{item['drug_name']}** (thieu {item['missing_field_count']} field)\n"
        md += f"   - File: {item['file']}\n"
        if item['missing_standard']:
            md += f"   - Thieu field chuan: {', '.join(item['missing_standard'])}\n"
        if item['missing_additional']:
            md += f"   - Thieu field bo sung: {', '.join(item['missing_additional'])}\n"
        md += "\n"
    
    md += f"""
## Thong Ke Theo Module

"""
    
    for module_name, module_stats in sorted(stats['module_statistics'].items(), key=lambda x: x[1]['total'], reverse=True):
        if module_stats['total'] > 0:
            md += f"### {module_name}\n"
            md += f"- Tong so thuoc: {module_stats['total']}\n"
            md += f"- Co du 14 field: {module_stats['with_all_14']} ({module_stats['with_all_14']/module_stats['total']*100:.1f}%)\n"
            md += f"- Co du 22 field: {module_stats['with_all_22']} ({module_stats['with_all_22']/module_stats['total']*100:.1f}%)\n"
            md += f"- Co thieu field: {module_stats['missing_fields']}\n"
            md += "\n"
    
    return md

if __name__ == "__main__":
    main()

