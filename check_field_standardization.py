"""
Kiểm tra chi tiết xem có thuốc nào cần chuẩn hóa field không
Kiểm tra: thứ tự field, thiếu field, field không chuẩn
"""
import ast
import json
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

# 14 field chuẩn theo thứ tự
STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

class FieldStandardizationChecker:
    """Kiểm tra chuẩn hóa field"""
    
    def __init__(self):
        self.drugs = {}
        self.issues = {
            'missing_fields': [],
            'wrong_order': [],
            'extra_fields_before_standard': []
        }
        self.load_all_drugs()
        self.check_all()
    
    def get_string_value(self, node):
        """Lấy giá trị string từ AST node"""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        elif hasattr(node, 's'):
            return node.s
        return None
    
    def extract_dict_keys_ordered(self, node: ast.Dict) -> List[str]:
        """Trích xuất các keys theo thứ tự từ AST Dict node"""
        keys = []
        for key_node in node.keys:
            key = self.get_string_value(key_node)
            if key:
                keys.append(key)
        return keys
    
    def extract_dict_keys(self, node: ast.Dict) -> Set[str]:
        """Trích xuất các keys từ AST Dict node"""
        return set(self.extract_dict_keys_ordered(node))
    
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
                        value_keys_ordered = self.extract_dict_keys_ordered(value_node)
                        
                        if self.is_drug_entry(value_keys):
                            if drug_name not in self.drugs:
                                self.drugs[drug_name] = {
                                    'name': drug_name,
                                    'file': file_path,
                                    'fields': value_keys,
                                    'fields_ordered': value_keys_ordered,
                                    'field_count': len(value_keys)
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
    
    def check_field_order(self, drug_name: str, fields_ordered: List[str]) -> Dict:
        """Kiểm tra thứ tự field"""
        issues = []
        
        # Tìm vị trí của các field chuẩn
        standard_positions = {}
        for i, field in enumerate(fields_ordered):
            if field in STANDARD_14_FIELDS:
                if field not in standard_positions:
                    standard_positions[field] = i
        
        # Kiểm tra xem các field chuẩn có đúng thứ tự không
        standard_fields_found = [f for f in fields_ordered if f in STANDARD_14_FIELDS]
        expected_order = [f for f in STANDARD_14_FIELDS if f in standard_fields_found]
        
        if standard_fields_found != expected_order:
            issues.append({
                'type': 'wrong_order',
                'current_order': standard_fields_found,
                'expected_order': expected_order
            })
        
        # Kiểm tra xem có field không chuẩn nào xuất hiện trước field chuẩn không
        non_standard_before_standard = []
        first_standard_pos = None
        for i, field in enumerate(fields_ordered):
            if field in STANDARD_14_FIELDS:
                if first_standard_pos is None:
                    first_standard_pos = i
                    break
        
        if first_standard_pos is not None and first_standard_pos > 0:
            non_standard_before = fields_ordered[:first_standard_pos]
            non_standard_before_standard = [f for f in non_standard_before if f not in STANDARD_14_FIELDS]
        
        if non_standard_before_standard:
            issues.append({
                'type': 'extra_fields_before_standard',
                'fields': non_standard_before_standard
            })
        
        return issues
    
    def check_all(self):
        """Kiểm tra tất cả thuốc"""
        for drug_name, drug_info in self.drugs.items():
            fields = drug_info['fields']
            fields_ordered = drug_info['fields_ordered']
            
            # Kiểm tra thiếu field
            missing = [f for f in STANDARD_14_FIELDS if f not in fields]
            if missing:
                self.issues['missing_fields'].append({
                    'name': drug_name,
                    'file': drug_info['file'],
                    'missing': missing
                })
            
            # Kiểm tra thứ tự field
            order_issues = self.check_field_order(drug_name, fields_ordered)
            if order_issues:
                for issue in order_issues:
                    if issue['type'] == 'wrong_order':
                        self.issues['wrong_order'].append({
                            'name': drug_name,
                            'file': drug_info['file'],
                            'current_order': issue['current_order'],
                            'expected_order': issue['expected_order']
                        })
                    elif issue['type'] == 'extra_fields_before_standard':
                        self.issues['extra_fields_before_standard'].append({
                            'name': drug_name,
                            'file': drug_info['file'],
                            'fields': issue['fields']
                        })
    
    def print_report(self):
        """In báo cáo"""
        print("\n" + "=" * 70)
        print("BAO CAO KIEM TRA CHUAN HOA FIELD")
        print("=" * 70)
        
        total_issues = (len(self.issues['missing_fields']) + 
                       len(self.issues['wrong_order']) + 
                       len(self.issues['extra_fields_before_standard']))
        
        print(f"\nTong so thuoc: {len(self.drugs)}")
        print(f"Tong so van de: {total_issues}")
        
        if self.issues['missing_fields']:
            print(f"\n⚠️  THUOC THIEU FIELD: {len(self.issues['missing_fields'])}")
            for drug in self.issues['missing_fields'][:10]:
                print(f"  - {drug['name']}: thieu {len(drug['missing'])} fields")
                print(f"    File: {drug['file']}")
                print(f"    Thieu: {', '.join(drug['missing'][:5])}{'...' if len(drug['missing']) > 5 else ''}")
        
        if self.issues['wrong_order']:
            print(f"\n⚠️  THUOC CO FIELD SAI THU TU: {len(self.issues['wrong_order'])}")
            for drug in self.issues['wrong_order'][:5]:
                print(f"  - {drug['name']}")
                print(f"    File: {drug['file']}")
                print(f"    Can sap xep lai field theo thu tu chuan")
        
        if self.issues['extra_fields_before_standard']:
            print(f"\n⚠️  THUOC CO FIELD KHONG CHUAN TRUOC FIELD CHUAN: {len(self.issues['extra_fields_before_standard'])}")
            for drug in self.issues['extra_fields_before_standard'][:5]:
                print(f"  - {drug['name']}")
                print(f"    File: {drug['file']}")
                print(f"    Field truoc: {', '.join(drug['fields'][:3])}{'...' if len(drug['fields']) > 3 else ''}")
        
        if total_issues == 0:
            print("\n✅ KHONG CO VAN DE NAO! Tat ca thuoc da duoc chuan hoa.")
        
        print("=" * 70)
    
    def save_report(self, filename: str = 'field_standardization_check.json'):
        """Lưu báo cáo"""
        report = {
            'total_drugs': len(self.drugs),
            'total_issues': (len(self.issues['missing_fields']) + 
                            len(self.issues['wrong_order']) + 
                            len(self.issues['extra_fields_before_standard'])),
            'issues': self.issues
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\nDa luu bao cao: {filename}")

def main():
    checker = FieldStandardizationChecker()
    checker.print_report()
    checker.save_report()

if __name__ == "__main__":
    main()

