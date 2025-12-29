"""
Hệ thống quản lý thuốc tối ưu nhất
Xử lý mọi cấu trúc, tìm kiếm, sắp xếp, quản lý hiệu quả
"""
import ast
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict
from datetime import datetime
import unicodedata

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

class UltimateDrugManagementSystem:
    """Hệ thống quản lý thuốc tối ưu nhất"""
    
    def __init__(self):
        self.drugs: Dict[str, Dict] = {}
        self.drug_index: Dict[str, List[str]] = defaultdict(list)
        self.file_index: Dict[str, List[str]] = defaultdict(list)
        self.group_index: Dict[str, List[str]] = defaultdict(list)
        self.search_index: Dict[str, Set[str]] = defaultdict(set)  # search_term -> {drug_names}
        self.load_all_drugs()
        self.build_search_index()
    
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
    
    def normalize_text(self, text: str) -> str:
        """Chuẩn hóa text để tìm kiếm (loại bỏ dấu, lowercase)"""
        # Loại bỏ dấu tiếng Việt
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        return text.lower()
    
    def is_drug_entry(self, keys: Set[str]) -> bool:
        """Kiểm tra xem dict có phải là entry thuốc không"""
        required_fields = {'group', 'vietnamese_name', 'administration', 'indications'}
        return len(keys & required_fields) >= 2
    
    def is_not_field_name(self, name: str) -> bool:
        """Kiểm tra xem tên có phải là field name không"""
        known_non_drugs = {
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
        
        if name in known_non_drugs:
            return False
        
        if name.islower() and name.count('_') >= 2:
            if name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']:
                return False
        
        return True
    
    def find_all_dicts_recursive(self, node, file_path: str, depth=0, max_depth=15):
        """Tìm tất cả dict trong AST"""
        if depth > max_depth:
            return
        
        if isinstance(node, ast.Dict):
            for key_node, value_node in zip(node.keys, node.values):
                if isinstance(value_node, ast.Dict):
                    drug_name = self.get_string_value(key_node)
                    
                    if drug_name and self.is_not_field_name(drug_name):
                        value_keys = self.extract_dict_keys(value_node)
                        
                        if self.is_drug_entry(value_keys):
                            if drug_name not in self.drugs:
                                self.drugs[drug_name] = {
                                    'name': drug_name,
                                    'file': file_path,
                                    'fields': value_keys,
                                    'field_count': len(value_keys)
                                }
            
            for key_node, value_node in zip(node.keys, node.values):
                self.find_all_dicts_recursive(value_node, file_path, depth + 1, max_depth)
        
        for child in ast.iter_child_nodes(node):
            self.find_all_dicts_recursive(child, file_path, depth + 1, max_depth)
    
    def enhance_fields_with_regex(self, content: str, drug_name: str, existing_fields: Set[str]) -> Set[str]:
        """Tăng cường field bằng regex"""
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
        
        while i < len(content) and i < start_pos + 20000:
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
        """Load tất cả thuốc"""
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
                    
                    self.find_all_dicts_recursive(tree, file_path)
                    
                    # Enhance fields
                    for drug_name in list(self.drugs.keys()):
                        if self.drugs[drug_name]['file'] == file_path:
                            enhanced_fields = self.enhance_fields_with_regex(
                                content, drug_name, self.drugs[drug_name]['fields']
                            )
                            if enhanced_fields != self.drugs[drug_name]['fields']:
                                self.drugs[drug_name]['fields'] = enhanced_fields
                                self.drugs[drug_name]['field_count'] = len(enhanced_fields)
                    
                    files_processed += 1
                    
                except SyntaxError:
                    pass
                    
            except Exception:
                pass
        
        # Build indexes
        for drug_name, drug_info in self.drugs.items():
            for field in drug_info['fields']:
                self.drug_index[field].append(drug_name)
            self.file_index[drug_info['file']].append(drug_name)
            
            # Index by group
            if 'group' in drug_info['fields']:
                # Extract group from content if needed
                pass
        
        print(f"Loaded {len(self.drugs)} drugs from {files_processed} files")
    
    def build_search_index(self):
        """Xây dựng index tìm kiếm"""
        for drug_name, drug_info in self.drugs.items():
            # Index by name (normalized)
            normalized_name = self.normalize_text(drug_name)
            words = normalized_name.split()
            for word in words:
                if len(word) >= 2:
                    self.search_index[word].add(drug_name)
            
            # Index by partial name
            for i in range(len(normalized_name)):
                for j in range(i + 2, len(normalized_name) + 1):
                    substring = normalized_name[i:j]
                    if len(substring) >= 2:
                        self.search_index[substring].add(drug_name)
    
    def search_drug(self, query: str, limit: int = 50, sort_by: str = 'name') -> List[Dict]:
        """Tìm kiếm thuốc (nhiều cách)"""
        query_normalized = self.normalize_text(query)
        
        # Tìm trong search index
        matching_drugs = set()
        query_words = query_normalized.split()
        
        if len(query_words) == 1:
            # Single word - tìm trong index
            if query_normalized in self.search_index:
                matching_drugs.update(self.search_index[query_normalized])
        else:
            # Multiple words - tìm intersection
            if query_words:
                matching_drugs = self.search_index.get(query_words[0], set()).copy()
                for word in query_words[1:]:
                    matching_drugs &= self.search_index.get(word, set())
        
        # Fallback: tìm trực tiếp
        if not matching_drugs:
            for drug_name in self.drugs.keys():
                if query_normalized in self.normalize_text(drug_name):
                    matching_drugs.add(drug_name)
        
        # Convert to list of drug info
        results = [self.drugs[name] for name in matching_drugs]
        
        # Sort
        if sort_by == 'name':
            results.sort(key=lambda x: x['name'])
        elif sort_by == 'field_count':
            results.sort(key=lambda x: x['field_count'], reverse=True)
        elif sort_by == 'file':
            results.sort(key=lambda x: x['file'])
        
        return results[:limit]
    
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
            'has_all_fields': all(f in fields for f in ALL_FIELDS),
            'field_count': drug['field_count']
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
            'files_stats': {},
            'structure_stats': {}
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
        
        # Structure stats
        field_count_dist = defaultdict(int)
        for drug_info in self.drugs.values():
            field_count_dist[drug_info['field_count']] += 1
        stats['structure_stats'] = dict(field_count_dist)
        
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
    
    def list_drugs(self, sort_by: str = 'name', filter_by: Optional[Dict] = None) -> List[Dict]:
        """Liệt kê thuốc với sắp xếp và lọc"""
        results = list(self.drugs.values())
        
        # Filter
        if filter_by:
            if 'has_field' in filter_by:
                field = filter_by['has_field']
                results = [d for d in results if field in d['fields']]
            if 'missing_field' in filter_by:
                field = filter_by['missing_field']
                results = [d for d in results if field not in d['fields']]
            if 'min_fields' in filter_by:
                min_count = filter_by['min_fields']
                results = [d for d in results if d['field_count'] >= min_count]
        
        # Sort
        if sort_by == 'name':
            results.sort(key=lambda x: x['name'])
        elif sort_by == 'field_count':
            results.sort(key=lambda x: x['field_count'], reverse=True)
        elif sort_by == 'file':
            results.sort(key=lambda x: x['file'])
        
        return results

def main():
    """Main function - CLI interface"""
    import sys
    
    manager = UltimateDrugManagementSystem()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'search':
            query = sys.argv[2] if len(sys.argv) > 2 else ''
            results = manager.search_drug(query)
            print(f"\nFound {len(results)} drugs matching '{query}':")
            for drug in results[:20]:
                print(f"  - {drug['name']} ({drug['file']}) - {drug['field_count']} fields")
        
        elif command == 'check':
            drug_name = sys.argv[2] if len(sys.argv) > 2 else ''
            result = manager.check_drug_fields(drug_name)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"\nDrug: {drug_name}")
                print(f"File: {result['file']}")
                print(f"Fields: {result['field_count']}")
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
        
        elif command == 'list':
            sort_by = sys.argv[2] if len(sys.argv) > 2 else 'name'
            results = manager.list_drugs(sort_by=sort_by)
            print(f"\nTotal: {len(results)} drugs")
            for drug in results[:30]:
                print(f"  - {drug['name']} ({drug['field_count']} fields)")
        
        elif command == 'export':
            filename = sys.argv[2] if len(sys.argv) > 2 else 'drugs_database_ultimate.json'
            manager.export_to_json(filename)
        
        else:
            print("Unknown command")
    else:
        print(f"\nUltimate Drug Management System - {len(manager.drugs)} drugs loaded")
        print("\nCommands:")
        print("  python ultimate_drug_management_system.py search <query>")
        print("  python ultimate_drug_management_system.py check <name>")
        print("  python ultimate_drug_management_system.py stats")
        print("  python ultimate_drug_management_system.py list [sort_by]")
        print("  python ultimate_drug_management_system.py export [file]")

if __name__ == "__main__":
    main()

