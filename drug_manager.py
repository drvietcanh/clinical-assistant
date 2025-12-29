"""
Hệ thống quản lý và tìm kiếm thuốc
Dễ dàng tìm kiếm, kiểm tra field, và quản lý thuốc
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

class DrugManager:
    """Quản lý và tìm kiếm thuốc"""
    
    def __init__(self):
        self.drugs: Dict[str, Dict] = {}
        self.drug_index: Dict[str, List[str]] = defaultdict(list)  # index by field
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
    
    def is_real_drug(self, drug_name: str, value_keys: Set[str]) -> bool:
        """Kiểm tra xem entry có phải là thuốc thực sự không"""
        # Phải có ít nhất 2 trong: group, vietnamese_name, administration, indications
        has_group = 'group' in value_keys
        has_vietnamese_name = 'vietnamese_name' in value_keys
        has_administration = 'administration' in value_keys
        has_indications = 'indications' in value_keys
        
        required_count = sum([has_group, has_vietnamese_name, has_administration, has_indications])
        
        if required_count < 2:
            return False
        
        # Loại bỏ field names
        if drug_name.islower() and '_' in drug_name and drug_name.count('_') >= 2:
            if drug_name not in ['iv', 'po', 'im', 'sc']:
                if not (has_group or has_vietnamese_name):
                    return False
        
        return True
    
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
                    
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                                    if isinstance(node.value, ast.Dict):
                                        for key_node, value_node in zip(node.value.keys, node.value.values):
                                            drug_name = self.get_string_value(key_node)
                                            
                                            if drug_name and isinstance(value_node, ast.Dict):
                                                value_keys = self.extract_dict_keys(value_node)
                                                
                                                if self.is_real_drug(drug_name, value_keys):
                                                    # Tìm file chứa thuốc
                                                    file_path = str(py_file.relative_to(base_path.parent))
                                                    
                                                    # Kiểm tra field bằng regex (backup)
                                                    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
                                                    match = re.search(pattern, content)
                                                    if match:
                                                        start_pos = match.end() - 1
                                                        brace_count = 0
                                                        in_string = False
                                                        string_char = None
                                                        i = start_pos
                                                        
                                                        while i < len(content) and i < start_pos + 10000:
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
                                                                        drug_section = content[start_pos:end_pos]
                                                                        
                                                                        # Kiểm tra field bằng regex
                                                                        for field in ENHANCED_FIELDS:
                                                                            if field not in value_keys:
                                                                                field_pattern = rf'["\']{re.escape(field)}["\']\s*:'
                                                                                if re.search(field_pattern, drug_section):
                                                                                    value_keys.add(field)
                                                                        break
                                                            i += 1
                                                    
                                                    self.drugs[drug_name] = {
                                                        'name': drug_name,
                                                        'file': file_path,
                                                        'fields': value_keys,
                                                        'field_count': len(value_keys)
                                                    }
                                                    
                                                    # Index by fields
                                                    for field in value_keys:
                                                        self.drug_index[field].append(drug_name)
                                    
                    files_processed += 1
                    
                except SyntaxError:
                    pass
                    
            except Exception:
                pass
        
        print(f"Loaded {len(self.drugs)} drugs from {files_processed} files")
    
    def search_drug(self, query: str) -> List[Dict]:
        """Tìm kiếm thuốc theo tên (case-insensitive, partial match)"""
        query_lower = query.lower()
        results = []
        
        for drug_name, drug_info in self.drugs.items():
            if query_lower in drug_name.lower() or query_lower in drug_info.get('vietnamese_name', '').lower():
                results.append(drug_info)
        
        return sorted(results, key=lambda x: x['name'])
    
    def get_drug(self, drug_name: str) -> Optional[Dict]:
        """Lấy thông tin một thuốc cụ thể"""
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
            'has_all_fields': len([f for f in ALL_FIELDS if f not in fields]) == 0
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
            'fields_stats': {}
        }
        
        for field in ALL_FIELDS:
            drugs_with_field = len(self.drug_index.get(field, []))
            stats['fields_stats'][field] = {
                'has_field': drugs_with_field,
                'missing': total - drugs_with_field,
                'percentage': (drugs_with_field * 100 // total) if total > 0 else 0
            }
        
        return stats
    
    def export_to_json(self, filename: str = 'drugs_database.json'):
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
    
    manager = DrugManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'search':
            if len(sys.argv) > 2:
                query = sys.argv[2]
                results = manager.search_drug(query)
                print(f"\nFound {len(results)} drugs matching '{query}':")
                for drug in results[:20]:
                    print(f"  - {drug['name']} ({drug['file']})")
                if len(results) > 20:
                    print(f"  ... and {len(results) - 20} more")
        
        elif command == 'check':
            if len(sys.argv) > 2:
                drug_name = sys.argv[2]
                result = manager.check_drug_fields(drug_name)
                if 'error' in result:
                    print(f"Error: {result['error']}")
                else:
                    print(f"\nDrug: {drug_name}")
                    print(f"File: {result['file']}")
                    print(f"\nMissing fields:")
                    if result['missing_core']:
                        print(f"  Core: {', '.join(result['missing_core'])}")
                    if result['missing_extended']:
                        print(f"  Extended: {', '.join(result['missing_extended'])}")
                    if result['missing_enhanced']:
                        print(f"  Enhanced: {', '.join(result['missing_enhanced'])}")
                    if result['has_all_fields']:
                        print("  ✅ All fields present!")
        
        elif command == 'missing':
            if len(sys.argv) > 2:
                field_name = sys.argv[2]
                drugs = manager.find_drugs_missing_field(field_name)
                print(f"\nDrugs missing '{field_name}': {len(drugs)}")
                for drug in drugs[:20]:
                    print(f"  - {drug}")
                if len(drugs) > 20:
                    print(f"  ... and {len(drugs) - 20} more")
        
        elif command == 'stats':
            stats = manager.get_statistics()
            print(f"\nTotal drugs: {stats['total_drugs']}")
            print(f"\nField statistics:")
            for field, stat in sorted(stats['fields_stats'].items(), 
                                    key=lambda x: x[1]['missing'], reverse=True):
                if stat['missing'] > 0:
                    print(f"  {field}: {stat['missing']} missing ({stat['percentage']}% have it)")
        
        elif command == 'export':
            filename = sys.argv[2] if len(sys.argv) > 2 else 'drugs_database.json'
            manager.export_to_json(filename)
        
        else:
            print("Unknown command")
    else:
        # Interactive mode
        print(f"\nDrug Manager - {len(manager.drugs)} drugs loaded")
        print("\nCommands:")
        print("  python drug_manager.py search <query>  - Search drugs")
        print("  python drug_manager.py check <name>   - Check drug fields")
        print("  python drug_manager.py missing <field> - Find drugs missing field")
        print("  python drug_manager.py stats          - Show statistics")
        print("  python drug_manager.py export [file]  - Export to JSON")

if __name__ == "__main__":
    main()

