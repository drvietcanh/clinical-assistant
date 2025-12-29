"""
Hệ thống quản lý thuốc tổng hợp - Tối ưu nhất
Quản lý, sắp xếp, tìm kiếm, chuẩn hóa cấu trúc
Đảm bảo mỗi thuốc có 14 field chuẩn, cấu trúc đồng bộ
"""
import ast
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict
from datetime import datetime
import unicodedata

# 14 field chuẩn theo thứ tự khoa học
STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

# Field bổ sung
ADDITIONAL_FIELDS = [
    "black_box_warnings", "drug_interactions", "pregnancy_lactation",
    "hepatic_adjustment", "overdose_management", "reversal_agents",
    "administration_instructions", "references"
]

ALL_FIELDS = STANDARD_14_FIELDS + ADDITIONAL_FIELDS

class ComprehensiveDrugManagementSystem:
    """Hệ thống quản lý thuốc tổng hợp"""
    
    def __init__(self):
        self.drugs: Dict[str, Dict] = {}
        self.drug_index: Dict[str, List[str]] = defaultdict(list)
        self.file_index: Dict[str, List[str]] = defaultdict(list)
        self.search_index: Dict[str, Set[str]] = defaultdict(set)
        self.load_all_drugs()
        self.build_indexes()
    
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
        """Chuẩn hóa text để tìm kiếm"""
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
                                # Sắp xếp fields theo thứ tự chuẩn
                                ordered_fields = []
                                for field in ALL_FIELDS:
                                    if field in value_keys:
                                        ordered_fields.append(field)
                                
                                self.drugs[drug_name] = {
                                    'name': drug_name,
                                    'file': file_path,
                                    'fields': value_keys,
                                    'ordered_fields': ordered_fields,
                                    'field_count': len(value_keys),
                                    'has_14_fields': len([f for f in STANDARD_14_FIELDS if f in value_keys]) == 14,
                                    'missing_14_fields': [f for f in STANDARD_14_FIELDS if f not in value_keys]
                                }
            
            for key_node, value_node in zip(node.keys, node.values):
                self.find_all_dicts_recursive(value_node, file_path, depth + 1, max_depth)
        
        for child in ast.iter_child_nodes(node):
            self.find_all_dicts_recursive(child, file_path, depth + 1, max_depth)
    
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
                    files_processed += 1
                except SyntaxError:
                    pass
            except Exception:
                pass
        
        print(f"Loaded {len(self.drugs)} drugs from {files_processed} files")
    
    def build_indexes(self):
        """Xây dựng các index"""
        for drug_name, drug_info in self.drugs.items():
            # Index theo field
            for field in drug_info['fields']:
                self.drug_index[field].append(drug_name)
            
            # Index theo file
            self.file_index[drug_info['file']].append(drug_name)
            
            # Index tìm kiếm
            normalized_name = self.normalize_text(drug_name)
            words = normalized_name.split()
            for word in words:
                if len(word) >= 2:
                    self.search_index[word].add(drug_name)
    
    def search_drug(self, query: str, limit: int = 50) -> List[Dict]:
        """Tìm kiếm thuốc"""
        query_normalized = self.normalize_text(query)
        matching_drugs = set()
        
        query_words = query_normalized.split()
        if query_words:
            matching_drugs = self.search_index.get(query_words[0], set()).copy()
            for word in query_words[1:]:
                matching_drugs &= self.search_index.get(word, set())
        
        if not matching_drugs:
            for drug_name in self.drugs.keys():
                if query_normalized in self.normalize_text(drug_name):
                    matching_drugs.add(drug_name)
        
        results = [self.drugs[name] for name in matching_drugs]
        results.sort(key=lambda x: x['name'])
        return results[:limit]
    
    def check_drug_structure(self, drug_name: str) -> Dict:
        """Kiểm tra cấu trúc thuốc"""
        drug = self.drugs.get(drug_name)
        if not drug:
            return {'error': f'Drug "{drug_name}" not found'}
        
        return {
            'drug_name': drug_name,
            'file': drug['file'],
            'has_14_fields': drug['has_14_fields'],
            'field_count': drug['field_count'],
            'missing_14_fields': drug['missing_14_fields'],
            'ordered_fields': drug['ordered_fields']
        }
    
    def get_statistics(self) -> Dict:
        """Lấy thống kê tổng quan"""
        total = len(self.drugs)
        
        stats = {
            'total_drugs': total,
            'drugs_with_14_fields': sum(1 for d in self.drugs.values() if d['has_14_fields']),
            'drugs_missing_14_fields': sum(1 for d in self.drugs.values() if not d['has_14_fields']),
            'field_statistics': {},
            'files_statistics': {}
        }
        
        for field in STANDARD_14_FIELDS:
            count = len(self.drug_index.get(field, []))
            stats['field_statistics'][field] = {
                'has_field': count,
                'missing': total - count,
                'percentage': (count * 100 // total) if total > 0 else 0
            }
        
        for file_path, drugs in self.file_index.items():
            stats['files_statistics'][file_path] = len(drugs)
        
        return stats
    
    def export_comprehensive_report(self, filename: str = 'comprehensive_drug_report.json'):
        """Xuất báo cáo tổng hợp"""
        report = {
            'report_date': datetime.now().isoformat(),
            'total_drugs': len(self.drugs),
            'standard_14_fields': STANDARD_14_FIELDS,
            'additional_fields': ADDITIONAL_FIELDS,
            'statistics': self.get_statistics(),
            'drugs': {name: {
                'file': info['file'],
                'has_14_fields': info['has_14_fields'],
                'field_count': info['field_count'],
                'missing_14_fields': info['missing_14_fields'],
                'ordered_fields': info['ordered_fields']
            } for name, info in self.drugs.items()}
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"Exported comprehensive report: {filename}")

def main():
    """Main function"""
    import sys
    
    system = ComprehensiveDrugManagementSystem()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'search':
            query = sys.argv[2] if len(sys.argv) > 2 else ''
            results = system.search_drug(query)
            print(f"\nFound {len(results)} drugs matching '{query}':")
            for drug in results[:20]:
                status = "✅" if drug['has_14_fields'] else "⚠️"
                print(f"  {status} {drug['name']} ({drug['file']}) - {drug['field_count']} fields")
        
        elif command == 'check':
            drug_name = sys.argv[2] if len(sys.argv) > 2 else ''
            result = system.check_drug_structure(drug_name)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"\nDrug: {drug_name}")
                print(f"File: {result['file']}")
                print(f"Has 14 fields: {'✅ Yes' if result['has_14_fields'] else '❌ No'}")
                print(f"Field count: {result['field_count']}")
                if result['missing_14_fields']:
                    print(f"Missing: {', '.join(result['missing_14_fields'])}")
        
        elif command == 'stats':
            stats = system.get_statistics()
            print(f"\nTotal drugs: {stats['total_drugs']}")
            print(f"Drugs with 14 fields: {stats['drugs_with_14_fields']} ({stats['drugs_with_14_fields']*100//stats['total_drugs'] if stats['total_drugs'] > 0 else 0}%)")
            print(f"Drugs missing 14 fields: {stats['drugs_missing_14_fields']}")
            print("\nField statistics (14 standard fields):")
            for field, stat in stats['field_statistics'].items():
                if stat['missing'] > 0:
                    print(f"  {field}: {stat['missing']} missing ({stat['percentage']}% have it)")
        
        elif command == 'export':
            filename = sys.argv[2] if len(sys.argv) > 2 else 'comprehensive_drug_report.json'
            system.export_comprehensive_report(filename)
        
        else:
            print("Unknown command")
    else:
        print(f"\nComprehensive Drug Management System - {len(system.drugs)} drugs loaded")
        print("\nCommands:")
        print("  python comprehensive_drug_management_system.py search <query>")
        print("  python comprehensive_drug_management_system.py check <name>")
        print("  python comprehensive_drug_management_system.py stats")
        print("  python comprehensive_drug_management_system.py export [file]")

if __name__ == "__main__":
    main()

