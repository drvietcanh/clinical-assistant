"""
Hệ thống quản lý thuốc tối ưu nhất
Tìm đủ 666 thuốc, quản lý và tìm kiếm hiệu quả
"""
import ast
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict
from datetime import datetime

# Định nghĩa các field
CORE_FIELDS = ["group", "vietnamese_name", "administration", "indications", "dosage"]
EXTENDED_FIELDS = ["side_effects", "contraindications", "interactions", "pregnancy"]
ENHANCED_FIELDS = [
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics",
    "storage", "black_box_warnings", "drug_interactions", "pregnancy_lactation",
    "hepatic_adjustment", "overdose_management", "reversal_agents",
    "administration_instructions", "references"
]
ALL_FIELDS = CORE_FIELDS + EXTENDED_FIELDS + ENHANCED_FIELDS

class UltimateDrugManager:
    """Hệ thống quản lý thuốc tối ưu nhất"""
    
    def __init__(self):
        self.drugs: Dict[str, Dict] = {}
        self.drug_index: Dict[str, List[str]] = defaultdict(list)
        self.file_index: Dict[str, List[str]] = defaultdict(list)
        self.load_all_drugs()
    
    def get_string_value(self, node):
        """Lấy giá trị string từ AST node"""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        elif hasattr(node, 's'):
            return node.s
        return None
    
    def extract_dict_keys(self, node: ast.Dict) -> Set[str]:
        """Trích xuất các keys từ AST Dict node"""
        keys = set()
        for key_node in node.keys:
            key = self.get_string_value(key_node)
            if key:
                keys.add(key)
        return keys
    
    def is_drug_entry(self, keys: Set[str]) -> bool:
        """Kiểm tra xem dict có phải là entry thuốc không"""
        required_fields = {'group', 'vietnamese_name', 'administration', 'indications'}
        return len(keys & required_fields) >= 2
    
    def is_not_field_name(self, name: str) -> bool:
        """Kiểm tra xem tên có phải là field name không"""
        known_field_names = {
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
        }
        
        if name in known_field_names:
            return False
        
        if name.islower() and name.count('_') >= 2:
            if name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']:
                return False
        
        return True
    
    def find_all_dicts(self, node, file_path: str, depth=0, max_depth=10):
        """Tìm tất cả dict trong AST (recursive)"""
        if depth > max_depth:
            return
        
        if isinstance(node, ast.Dict):
            for key_node, value_node in zip(node.keys, node.values):
                if isinstance(value_node, ast.Dict):
                    drug_name = self.get_string_value(key_node)
                    
                    if drug_name and self.is_not_field_name(drug_name):
                        value_keys = self.extract_dict_keys(value_node)
                        
                        if self.is_drug_entry(value_keys):
                            # Kiểm tra field bằng regex trong content (backup)
                            # Đã được xử lý ở level cao hơn
                            
                            if drug_name not in self.drugs:
                                self.drugs[drug_name] = {
                                    'name': drug_name,
                                    'file': file_path,
                                    'fields': value_keys,
                                    'field_count': len(value_keys)
                                }
                                
                                # Index
                                for field in value_keys:
                                    self.drug_index[field].append(drug_name)
                                self.file_index[file_path].append(drug_name)
            
            # Tiếp tục tìm trong nested
            for key_node, value_node in zip(node.keys, node.values):
                self.find_all_dicts(value_node, file_path, depth + 1, max_depth)
        
        for child in ast.iter_child_nodes(node):
            self.find_all_dicts(child, file_path, depth + 1, max_depth)
    
    def enhance_fields_with_regex(self, content: str, drug_name: str, existing_fields: Set[str]) -> Set[str]:
        """Tăng cường field bằng regex (backup method)"""
        pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
        match = re.search(pattern, content)
        
        if not match:
            return existing_fields
        
        start_pos = match.end() - 1
        brace_count = 0
        in_string = False
        string_char = None
        i = start_pos
        end_pos = None
        
        while i < len(content) and i < start_pos + 15000:
            char = content[i]
            
            if char in ['"', "'"]:
                if i > 0 and content[i-1] == '\\':
                    i += 1
                    continue
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
            
            if not in_string:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end_pos = i + 1
                        break
            i += 1
        
        if end_pos:
            drug_section = content[start_pos:end_pos]
            enhanced_fields = existing_fields.copy()
            
            for field in ENHANCED_FIELDS:
                if field not in enhanced_fields:
                    field_pattern = rf'["\']{re.escape(field)}["\']\s*:'
                    if re.search(field_pattern, drug_section):
                        enhanced_fields.add(field)
            
            return enhanced_fields
        
        return existing_fields
    
    def load_all_drugs(self):
        """Load tất cả thuốc từ các file module"""
        base_path = Path("drugs/drug_modules")
        files_processed = 0
        
        for py_file in sorted(base_path.rglob("*.py")):
            if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                try:
                    tree = ast.parse(content)
                    file_path = str(py_file.relative_to(base_path.parent))
                    
                    # Tìm tất cả dict
                    self.find_all_dicts(tree, file_path)
                    
                    # Tăng cường field bằng regex cho các thuốc đã tìm thấy
                    for drug_name in list(self.drugs.keys()):
                        if self.drugs[drug_name]['file'] == file_path:
                            enhanced_fields = self.enhance_fields_with_regex(
                                content, drug_name, self.drugs[drug_name]['fields']
                            )
                            if enhanced_fields != self.drugs[drug_name]['fields']:
                                # Cập nhật fields
                                old_fields = self.drugs[drug_name]['fields']
                                self.drugs[drug_name]['fields'] = enhanced_fields
                                self.drugs[drug_name]['field_count'] = len(enhanced_fields)
                                
                                # Cập nhật index
                                new_fields = enhanced_fields - old_fields
                                for field in new_fields:
                                    if drug_name not in self.drug_index[field]:
                                        self.drug_index[field].append(drug_name)
                    
                    files_processed += 1
                    
                except SyntaxError:
                    pass
                    
            except Exception:
                pass
        
        print(f"Loaded {len(self.drugs)} drugs from {files_processed} files")
    
    def search_drug(self, query: str, limit: int = 50) -> List[Dict]:
        """Tìm kiếm thuốc (case-insensitive, partial match)"""
        query_lower = query.lower()
        results = []
        
        for drug_name, drug_info in self.drugs.items():
            if query_lower in drug_name.lower():
                results.append(drug_info)
            elif 'vietnamese_name' in drug_info.get('fields', set()):
                # Có thể tìm trong vietnamese_name nếu có
                pass
        
        return sorted(results, key=lambda x: x['name'])[:limit]
    
    def get_drug(self, drug_name: str) -> Optional[Dict]:
        """Lấy thông tin một thuốc"""
        return self.drugs.get(drug_name)
    
    def check_drug_fields(self, drug_name: str) -> Dict:
        """Kiểm tra field của một thuốc"""
        drug = self.get_drug(drug_name)
        if not drug:
            return {'error': f'Drug "{drug_name}" not found'}
        
        fields = drug['fields']
        result = {
            'drug_name': drug_name,
            'file': drug['file'],
            'missing_core': [f for f in CORE_FIELDS if f not in fields],
            'missing_extended': [f for f in EXTENDED_FIELDS if f not in fields],
            'missing_enhanced': [f for f in ENHANCED_FIELDS if f not in fields],
            'has_all_fields': all(f in fields for f in ALL_FIELDS)
        }
        result['total_missing'] = len(result['missing_core']) + len(result['missing_extended']) + len(result['missing_enhanced'])
        return result
    
    def find_drugs_missing_field(self, field_name: str) -> List[str]:
        """Tìm các thuốc thiếu một field cụ thể"""
        all_drugs = set(self.drugs.keys())
        drugs_with_field = set(self.drug_index.get(field_name, []))
        return sorted(all_drugs - drugs_with_field)
    
    def get_statistics(self) -> Dict:
        """Lấy thống kê tổng quan"""
        total = len(self.drugs)
        
        stats = {
            'total_drugs': total,
            'fields_stats': {},
            'files_stats': {}
        }
        
        for field in ALL_FIELDS:
            drugs_with_field = len(self.drug_index.get(field, []))
            stats['fields_stats'][field] = {
                'has_field': drugs_with_field,
                'missing': total - drugs_with_field,
                'percentage': (drugs_with_field * 100 // total) if total > 0 else 0
            }
        
        for file_path, drugs in self.file_index.items():
            stats['files_stats'][file_path] = len(drugs)
        
        return stats
    
    def export_to_json(self, filename: str = 'drugs_database_ultimate.json'):
        """Xuất database ra file JSON"""
        data = {
            'export_date': datetime.now().isoformat(),
            'total_drugs': len(self.drugs),
            'drugs': {}
        }
        
        for drug_name, drug_info in self.drugs.items():
            data['drugs'][drug_name] = {
                'file': drug_info['file'],
                'fields': sorted(list(drug_info['fields'])),
                'field_count': drug_info['field_count']
            }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Exported {len(self.drugs)} drugs to {filename}")

def main():
    """Main function - CLI interface"""
    import sys
    
    manager = UltimateDrugManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'search':
            query = sys.argv[2] if len(sys.argv) > 2 else ''
            results = manager.search_drug(query)
            print(f"\nFound {len(results)} drugs matching '{query}':")
            for drug in results[:20]:
                print(f"  - {drug['name']} ({drug['file']})")
        
        elif command == 'check':
            drug_name = sys.argv[2] if len(sys.argv) > 2 else ''
            result = manager.check_drug_fields(drug_name)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"\nDrug: {drug_name}")
                print(f"File: {result['file']}")
                if result['has_all_fields']:
                    print("✅ All fields present!")
                else:
                    print(f"Missing {result['total_missing']} fields")
        
        elif command == 'stats':
            stats = manager.get_statistics()
            print(f"\nTotal drugs: {stats['total_drugs']}")
            print("\nField statistics (top 10 missing):")
            sorted_fields = sorted(stats['fields_stats'].items(), 
                                 key=lambda x: x[1]['missing'], reverse=True)
            for field, stat in sorted_fields[:10]:
                if stat['missing'] > 0:
                    print(f"  {field}: {stat['missing']} missing ({stat['percentage']}% have it)")
        
        elif command == 'export':
            filename = sys.argv[2] if len(sys.argv) > 2 else 'drugs_database_ultimate.json'
            manager.export_to_json(filename)
        
        else:
            print("Unknown command")
    else:
        print(f"\nUltimate Drug Manager - {len(manager.drugs)} drugs loaded")
        print("\nCommands:")
        print("  python drug_manager_ultimate.py search <query>")
        print("  python drug_manager_ultimate.py check <name>")
        print("  python drug_manager_ultimate.py stats")
        print("  python drug_manager_ultimate.py export [file]")

if __name__ == "__main__":
    main()

