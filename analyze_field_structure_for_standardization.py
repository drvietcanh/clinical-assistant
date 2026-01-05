"""
Phân tích chi tiết các biến thể cấu trúc field để chuẩn hóa
Tạo báo cáo chi tiết với danh sách thuốc cần sửa cho từng field
"""
import sys
import json
import ast
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from collections import defaultdict
import io

sys.path.insert(0, str(Path.cwd()))

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_string_value(node):
    """Lấy giá trị string từ AST node"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    elif hasattr(node, 's'):
        return node.s
    return None

def extract_dict_keys(node: ast.Dict) -> Set[str]:
    """Trích xuất tất cả keys của dict"""
    keys = set()
    for key_node in node.keys:
        key = get_string_value(key_node)
        if key:
            keys.add(key)
    return keys

def get_dict_value(node: ast.Dict, key: str) -> Optional[Any]:
    """Lấy giá trị của một key trong dict"""
    for key_node, value_node in zip(node.keys, node.values):
        if get_string_value(key_node) == key:
            if isinstance(value_node, ast.Constant):
                return value_node.value
            elif isinstance(value_node, ast.Str):
                return value_node.s
            elif isinstance(value_node, ast.NameConstant):
                return value_node.value
            elif isinstance(value_node, ast.Dict):
                return extract_dict_keys(value_node)
            elif isinstance(value_node, ast.List):
                return [get_string_value(elt) for elt in value_node.elts if get_string_value(elt)]
            else:
                return type(value_node).__name__
    return None

def analyze_field_structure(drug_name: str, field_name: str, value_node: ast.AST, file_path: str) -> Dict[str, Any]:
    """Phân tích cấu trúc của một field"""
    structure_info = {
        'drug': drug_name,
        'file': file_path,
        'field': field_name,
        'type': type(value_node).__name__,
        'needs_fix': False,
        'fix_type': None,
        'current_structure': {}
    }
    
    if isinstance(value_node, ast.Dict):
        keys = extract_dict_keys(value_node)
        structure_info['current_structure'] = {
            'type': 'dict',
            'keys': sorted(list(keys)),
            'key_count': len(keys)
        }
        
        # Kiểm tra nested dicts
        nested_info = {}
        for key_node, value_node_nested in zip(value_node.keys, value_node.values):
            key = get_string_value(key_node)
            if key and isinstance(value_node_nested, ast.Dict):
                nested_keys = extract_dict_keys(value_node_nested)
                nested_info[key] = sorted(list(nested_keys))
        if nested_info:
            structure_info['current_structure']['nested_keys'] = nested_info
        
        # Xác định cấu trúc và cần sửa không
        structure_info.update(determine_fix_needed(field_name, structure_info['current_structure'], value_node))
        
    elif isinstance(value_node, ast.List):
        structure_info['current_structure'] = {
            'type': 'list',
            'length': len(value_node.elts),
            'is_empty': len(value_node.elts) == 0
        }
        structure_info.update(determine_fix_needed(field_name, structure_info['current_structure'], value_node))
        
    elif isinstance(value_node, (ast.Constant, ast.Str, ast.NameConstant)):
        if isinstance(value_node, ast.Constant):
            value = value_node.value
        elif hasattr(value_node, 's'):
            value = value_node.s
        elif isinstance(value_node, ast.NameConstant):
            value = value_node.value
        else:
            value = None
        
        structure_info['current_structure'] = {
            'type': type(value).__name__ if value is not None else "None",
            'value': str(value)[:100] if value else None
        }
        structure_info.update(determine_fix_needed(field_name, structure_info['current_structure'], value_node))
    
    return structure_info

def determine_fix_needed(field_name: str, current_structure: Dict, value_node: ast.AST) -> Dict[str, Any]:
    """Xác định field có cần sửa không và loại sửa"""
    result = {
        'needs_fix': False,
        'fix_type': None,
        'fix_details': {}
    }
    
    # Định nghĩa cấu trúc chuẩn cho từng field
    standard_structures = {
        'pregnancy_lactation': {
            'type': 'dict',
            'required_keys': {'fda_category', 'pregnancy_details', 'lactation'},
            'nested_keys': {
                'lactation': {'safety', 'details', 'recommendation'}
            }
        },
        'hepatic_adjustment': {
            'type': 'dict',
            'required_keys': {'mild', 'moderate', 'severe', 'notes'}
        },
        'overdose_management': {
            'type': 'dict',
            'required_keys': {'symptoms', 'antidote', 'treatment', 'monitoring'}
        },
        'drug_interactions': {
            'type': 'dict',
            'required_keys': {'major', 'moderate', 'minor'}
        },
        'references': {
            'type': 'dict',
            'required_keys': {'primary_sources', 'last_updated', 'evidence_level'}
        }
    }
    
    if field_name not in standard_structures:
        return result
    
    standard = standard_structures[field_name]
    
    # Kiểm tra type
    if current_structure.get('type') != standard['type']:
        result['needs_fix'] = True
        result['fix_type'] = f"convert_{current_structure.get('type')}_to_{standard['type']}"
        result['fix_details'] = {
            'current_type': current_structure.get('type'),
            'required_type': standard['type']
        }
        return result
    
    # Kiểm tra keys cho dict
    if current_structure.get('type') == 'dict':
        current_keys = set(current_structure.get('keys', []))
        required_keys = standard.get('required_keys', set())
        
        missing_keys = required_keys - current_keys
        extra_keys = current_keys - required_keys
        
        # Kiểm tra nested keys
        nested_issues = {}
        if 'nested_keys' in standard:
            current_nested = current_structure.get('nested_keys', {})
            for nested_key, nested_required in standard['nested_keys'].items():
                if nested_key in current_nested:
                    nested_current = set(current_nested[nested_key])
                    nested_missing = nested_required - nested_current
                    if nested_missing:
                        nested_issues[nested_key] = {
                            'missing': list(nested_missing),
                            'current': list(nested_current)
                        }
                else:
                    nested_issues[nested_key] = {'missing': list(nested_required), 'current': []}
        
        # Xác định cần sửa
        if missing_keys or extra_keys or nested_issues:
            result['needs_fix'] = True
            
            if missing_keys:
                result['fix_type'] = 'add_missing_keys'
                result['fix_details']['missing_keys'] = list(missing_keys)
            
            if extra_keys:
                # Kiểm tra nếu là key cần đổi tên
                rename_map = {
                    'pregnancy_lactation': {
                        'lactation_details': 'lactation',
                        'pregnancy_category': 'fda_category',
                        'pregnancy_notes': 'pregnancy_details'
                    },
                    'hepatic_adjustment': {
                        'adjustment': None  # Cần chuyển đổi đặc biệt
                    },
                    'contraindications': {
                        'absolute': 'tuyệt_đối',
                        'relative': 'tương_đối'
                    },
                    'references': {
                        'guidelines': 'primary_sources',
                        'primary': 'primary_sources'
                    }
                }
                
                if field_name in rename_map:
                    for extra_key in extra_keys:
                        if extra_key in rename_map[field_name]:
                            result['fix_type'] = 'rename_keys'
                            if 'rename_keys' not in result['fix_details']:
                                result['fix_details']['rename_keys'] = {}
                            result['fix_details']['rename_keys'][extra_key] = rename_map[field_name][extra_key]
            
            if nested_issues:
                result['fix_type'] = 'fix_nested_structure'
                result['fix_details']['nested_issues'] = nested_issues
    
    return result

def analyze_all_drugs():
    """Phân tích tất cả thuốc"""
    base_path = Path("drugs/drug_modules")
    
    # Các field cần phân tích
    target_fields = [
        'pregnancy_lactation',
        'hepatic_adjustment',
        'overdose_management',
        'contraindications',
        'drug_interactions',
        'administration_instructions',
        'references'
    ]
    
    field_analysis = {field: {
        'total_drugs': 0,
        'needs_fix': [],
        'structure_variations': defaultdict(list)
    } for field in target_fields}
    
    def scan_directory(directory: Path):
        """Quét đệ quy một thư mục"""
        for item in sorted(directory.iterdir()):
            if item.name == '__init__.py' or item.name == '__pycache__' or item.name.endswith('.pyc'):
                continue
            
            if item.is_file() and item.suffix == '.py':
                try:
                    with open(item, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    tree = ast.parse(content)
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name) and (target.id.endswith('_DRUGS') or target.id.isupper()):
                                    if isinstance(node.value, ast.Dict):
                                        for key_node, value_node in zip(node.value.keys, node.value.values):
                                            drug_name = get_string_value(key_node)
                                            if drug_name and isinstance(value_node, ast.Dict):
                                                # Phân tích từng field
                                                for field_key_node, field_value_node in zip(value_node.keys, value_node.values):
                                                    field_name = get_string_value(field_key_node)
                                                    if field_name in target_fields:
                                                        field_analysis[field_name]['total_drugs'] += 1
                                                        analysis = analyze_field_structure(
                                                            drug_name, field_name, field_value_node, str(item)
                                                        )
                                                        
                                                        # Nhóm theo cấu trúc
                                                        if analysis['current_structure'].get('type') == 'dict':
                                                            keys_str = json.dumps(
                                                                sorted(analysis['current_structure'].get('keys', [])),
                                                                sort_keys=True
                                                            )
                                                            structure_key = f"dict:{keys_str}"
                                                        elif analysis['current_structure'].get('type') == 'list':
                                                            structure_key = "list"
                                                        else:
                                                            structure_key = f"{analysis['current_structure'].get('type')}"
                                                        
                                                        field_analysis[field_name]['structure_variations'][structure_key].append(analysis)
                                                        
                                                        # Thêm vào danh sách cần sửa
                                                        if analysis['needs_fix']:
                                                            field_analysis[field_name]['needs_fix'].append(analysis)
                except Exception as e:
                    print(f"Error reading {item}: {e}")
                    continue
            elif item.is_dir():
                scan_directory(item)
    
    scan_directory(base_path)
    
    return field_analysis

def generate_report(field_analysis: Dict) -> Dict[str, Any]:
    """Tạo báo cáo từ phân tích"""
    report = {
        'summary': {},
        'detailed_analysis': {},
        'drugs_need_fix': {}
    }
    
    for field_name, analysis in field_analysis.items():
        # Summary
        report['summary'][field_name] = {
            'total_drugs': analysis['total_drugs'],
            'drugs_need_fix': len(analysis['needs_fix']),
            'structure_variations': len(analysis['structure_variations']),
            'fix_percentage': round(len(analysis['needs_fix']) / analysis['total_drugs'] * 100, 2) if analysis['total_drugs'] > 0 else 0
        }
        
        # Detailed analysis
        report['detailed_analysis'][field_name] = {}
        for structure_key, drugs in analysis['structure_variations'].items():
            report['detailed_analysis'][field_name][structure_key] = {
                'count': len(drugs),
                'percentage': round(len(drugs) / analysis['total_drugs'] * 100, 2) if analysis['total_drugs'] > 0 else 0,
                'examples': [{'drug': d['drug'], 'file': d['file']} for d in drugs[:3]]
            }
        
        # Drugs need fix
        report['drugs_need_fix'][field_name] = []
        for drug_info in analysis['needs_fix']:
            report['drugs_need_fix'][field_name].append({
                'drug': drug_info['drug'],
                'file': drug_info['file'],
                'fix_type': drug_info['fix_type'],
                'fix_details': drug_info['fix_details'],
                'current_structure': drug_info['current_structure']
            })
    
    return report

def main():
    print("="*70)
    print("PHAN TICH CHI TIET CAU TRUC FIELD DE CHUAN HOA")
    print("="*70)
    
    print("\nDang quet tat ca file thuoc...")
    field_analysis = analyze_all_drugs()
    
    print("\nDang tao bao cao...")
    report = generate_report(field_analysis)
    
    # In summary
    print("\n" + "="*70)
    print("TOM TAT")
    print("="*70)
    for field_name, summary in report['summary'].items():
        print(f"\n{field_name}:")
        print(f"  - Tong so thuoc: {summary['total_drugs']}")
        print(f"  - Can sua: {summary['drugs_need_fix']} ({summary['fix_percentage']}%)")
        print(f"  - So cau truc khac nhau: {summary['structure_variations']}")
    
    # Lưu báo cáo JSON
    with open('field_standardization_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Tạo báo cáo Markdown
    md_content = generate_markdown_report(report)
    with open('field_standardization_analysis.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"\nDa luu:")
    print(f"  - field_standardization_analysis.json")
    print(f"  - field_standardization_analysis.md")
    print("="*70)

def generate_markdown_report(report: Dict) -> str:
    """Tạo báo cáo Markdown"""
    md = ["# Báo Cáo Phân Tích Cấu Trúc Field Để Chuẩn Hóa\n"]
    md.append(f"**Ngày tạo:** {Path('field_standardization_analysis.json').stat().st_mtime if Path('field_standardization_analysis.json').exists() else 'N/A'}\n")
    
    # Summary
    md.append("## Tóm Tắt\n")
    md.append("| Field | Tổng Thuốc | Cần Sửa | % Cần Sửa | Số Cấu Trúc Khác Nhau |")
    md.append("|-------|------------|---------|-----------|----------------------|")
    for field_name, summary in report['summary'].items():
        md.append(f"| {field_name} | {summary['total_drugs']} | {summary['drugs_need_fix']} | {summary['fix_percentage']}% | {summary['structure_variations']} |")
    
    # Chi tiết từng field
    md.append("\n## Chi Tiết Từng Field\n")
    for field_name in report['summary'].keys():
        md.append(f"### {field_name}\n")
        md.append(f"**Tổng số thuốc:** {report['summary'][field_name]['total_drugs']}\n")
        md.append(f"**Số thuốc cần sửa:** {report['summary'][field_name]['drugs_need_fix']}\n")
        
        # Các cấu trúc khác nhau
        md.append("\n#### Các Cấu Trúc Khác Nhau:\n")
        for structure_key, info in report['detailed_analysis'][field_name].items():
            md.append(f"- **{structure_key}**: {info['count']} thuốc ({info['percentage']}%)")
            if info['examples']:
                md.append(f"  - Ví dụ: {', '.join([ex['drug'] for ex in info['examples']])}")
        
        # Danh sách thuốc cần sửa
        if report['drugs_need_fix'][field_name]:
            md.append(f"\n#### Danh Sách Thuốc Cần Sửa ({len(report['drugs_need_fix'][field_name])} thuốc):\n")
            md.append("| Thuốc | File | Loại Sửa | Chi Tiết |")
            md.append("|-------|------|----------|----------|")
            for drug_info in report['drugs_need_fix'][field_name][:50]:  # Giới hạn 50 dòng đầu
                fix_type = drug_info['fix_type'] or 'N/A'
                fix_details = json.dumps(drug_info['fix_details'], ensure_ascii=False)[:50]
                file_short = drug_info['file'].replace('drugs\\drug_modules\\', '').replace('drugs/drug_modules/', '')
                md.append(f"| {drug_info['drug']} | {file_short} | {fix_type} | {fix_details} |")
            
            if len(report['drugs_need_fix'][field_name]) > 50:
                md.append(f"\n*... và {len(report['drugs_need_fix'][field_name]) - 50} thuốc khác*")
        
        md.append("\n---\n")
    
    return "\n".join(md)

if __name__ == "__main__":
    main()

