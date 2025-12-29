"""
Hệ thống sắp xếp và tổ chức lại thuốc
Đảm bảo cấu trúc đồng bộ, khoa học, dễ tìm kiếm và sửa chữa
"""
import ast
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict
from datetime import datetime
import shutil

# 14 field chuẩn theo thứ tự khoa học
STANDARD_14_FIELDS_ORDER = [
    "group",                    # 1. Nhóm thuốc
    "vietnamese_name",          # 2. Tên tiếng Việt
    "administration",           # 3. Đường dùng
    "indications",              # 4. Chỉ định
    "dosage",                   # 5. Liều dùng
    "side_effects",             # 6. Tác dụng phụ
    "contraindications",        # 7. Chống chỉ định
    "interactions",             # 8. Tương tác thuốc
    "pregnancy",                # 9. Thai kỳ
    "mechanism_of_action",      # 10. Cơ chế tác dụng
    "monitoring",               # 11. Theo dõi
    "precautions",              # 12. Thận trọng
    "pharmacokinetics",         # 13. Dược động học
    "storage",                  # 14. Bảo quản
]

# Các field bổ sung (sau 14 field chuẩn)
ADDITIONAL_FIELDS_ORDER = [
    "black_box_warnings",
    "drug_interactions",
    "pregnancy_lactation",
    "hepatic_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions",
    "references",
]

ALL_FIELDS_ORDER = STANDARD_14_FIELDS_ORDER + ADDITIONAL_FIELDS_ORDER

class DrugOrganizerSystem:
    """Hệ thống sắp xếp và tổ chức thuốc"""
    
    def __init__(self):
        self.drugs = {}
        self.drugs_by_file = defaultdict(list)
        self.drugs_by_group = defaultdict(list)
        self.load_all_drugs()
        self.organize_drugs()
    
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
                                    'field_count': len(value_keys),
                                    'has_14_fields': len([f for f in STANDARD_14_FIELDS_ORDER if f in value_keys]) == 14
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
    
    def organize_drugs(self):
        """Tổ chức thuốc theo file và group"""
        for drug_name, drug_info in self.drugs.items():
            # Theo file
            self.drugs_by_file[drug_info['file']].append(drug_name)
            
            # Theo group (nếu có)
            # Có thể extract từ file path hoặc từ field 'group'
    
    def generate_organization_report(self) -> Dict:
        """Tạo báo cáo tổ chức"""
        report = {
            'total_drugs': len(self.drugs),
            'drugs_with_14_fields': sum(1 for d in self.drugs.values() if d['has_14_fields']),
            'drugs_by_file': {f: len(drugs) for f, drugs in self.drugs_by_file.items()},
            'structure_status': {
                'complete': sum(1 for d in self.drugs.values() if d['has_14_fields']),
                'incomplete': sum(1 for d in self.drugs.values() if not d['has_14_fields'])
            }
        }
        
        return report
    
    def print_organization_summary(self):
        """In tóm tắt tổ chức"""
        report = self.generate_organization_report()
        
        print("\n" + "=" * 70)
        print("TOM TAT TO CHUC THUOC")
        print("=" * 70)
        print(f"\nTong so thuoc: {report['total_drugs']}")
        print(f"Thuoc co du 14 field: {report['drugs_with_14_fields']} ({report['drugs_with_14_fields']*100//report['total_drugs'] if report['total_drugs'] > 0 else 0}%)")
        print(f"Thuoc chua du 14 field: {report['structure_status']['incomplete']}")
        
        print(f"\nPhan bo theo file (top 20):")
        sorted_files = sorted(report['drugs_by_file'].items(), key=lambda x: x[1], reverse=True)
        for file_path, count in sorted_files[:20]:
            print(f"  {file_path}: {count} thuoc")
        
        print("=" * 70)
    
    def save_organization_data(self, filename: str = 'drug_organization_data.json'):
        """Lưu dữ liệu tổ chức"""
        data = {
            'organization_date': datetime.now().isoformat(),
            'total_drugs': len(self.drugs),
            'standard_14_fields': STANDARD_14_FIELDS_ORDER,
            'additional_fields': ADDITIONAL_FIELDS_ORDER,
            'drugs': {name: {
                'file': info['file'],
                'has_14_fields': info['has_14_fields'],
                'field_count': info['field_count'],
                'fields': sorted(list(info['fields']))
            } for name, info in self.drugs.items()},
            'organization': {
                'by_file': {f: drugs for f, drugs in self.drugs_by_file.items()}
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\nDa luu du lieu to chuc: {filename}")

def main():
    """Main function"""
    print("=" * 70)
    print("HE THONG TO CHUC VA SAP XEP THUOC")
    print("=" * 70)
    print()
    
    organizer = DrugOrganizerSystem()
    organizer.print_organization_summary()
    organizer.save_organization_data()
    
    print("\n✅ He thong da san sang de quan ly va sap xep thuoc!")

if __name__ == "__main__":
    main()

