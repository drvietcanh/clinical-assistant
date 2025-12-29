"""
Tạo danh sách thuốc ở nhiều định dạng
Để dễ dàng truy cập, tìm kiếm, sửa chữa trong các phiên sau
"""
import ast
import json
import csv
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict
from datetime import datetime

# 14 field chuẩn
STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

class DrugListCreator:
    """Tạo danh sách thuốc ở nhiều định dạng"""
    
    def __init__(self):
        self.drugs = {}
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
    
    def create_simple_list(self, filename: str = 'drugs_list_simple.txt'):
        """Tạo danh sách đơn giản (chỉ tên thuốc)"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# DANH SACH THUOC - CHI TEN\n")
            f.write(f"# Tong so: {len(self.drugs)}\n")
            f.write(f"# Ngay tao: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for drug_name in sorted(self.drugs.keys()):
                f.write(f"{drug_name}\n")
        
        print(f"Created: {filename}")
    
    def create_detailed_list(self, filename: str = 'drugs_list_detailed.txt'):
        """Tạo danh sách chi tiết (tên + file + field count)"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# DANH SACH THUOC - CHI TIET\n")
            f.write(f"# Tong so: {len(self.drugs)}\n")
            f.write(f"# Ngay tao: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for drug_name in sorted(self.drugs.keys()):
                drug_info = self.drugs[drug_name]
                status = "✅" if drug_info['has_14_fields'] else "⚠️"
                f.write(f"{status} {drug_name}\n")
                f.write(f"   File: {drug_info['file']}\n")
                f.write(f"   Fields: {drug_info['field_count']} ({'14/14' if drug_info['has_14_fields'] else f'{14-len(drug_info['missing_14_fields'])}/14'})\n")
                if drug_info['missing_14_fields']:
                    f.write(f"   Missing: {', '.join(drug_info['missing_14_fields'])}\n")
                f.write("\n")
        
        print(f"Created: {filename}")
    
    def create_csv_list(self, filename: str = 'drugs_list.csv'):
        """Tạo danh sách CSV (dễ import vào Excel)"""
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Drug Name', 'File', 'Field Count', 'Has 14 Fields', 'Missing Fields', 'Status'])
            
            for drug_name in sorted(self.drugs.keys()):
                drug_info = self.drugs[drug_name]
                missing = ', '.join(drug_info['missing_14_fields']) if drug_info['missing_14_fields'] else 'None'
                status = 'Complete' if drug_info['has_14_fields'] else 'Incomplete'
                writer.writerow([
                    drug_name,
                    drug_info['file'],
                    drug_info['field_count'],
                    'Yes' if drug_info['has_14_fields'] else 'No',
                    missing,
                    status
                ])
        
        print(f"Created: {filename}")
    
    def create_json_list(self, filename: str = 'drugs_list.json'):
        """Tạo danh sách JSON (dễ xử lý bằng code)"""
        data = {
            'created_date': datetime.now().isoformat(),
            'total_drugs': len(self.drugs),
            'drugs': {}
        }
        
        for drug_name, drug_info in sorted(self.drugs.items()):
            data['drugs'][drug_name] = {
                'file': drug_info['file'],
                'field_count': drug_info['field_count'],
                'has_14_fields': drug_info['has_14_fields'],
                'missing_14_fields': drug_info['missing_14_fields'],
                'fields': sorted(list(drug_info['fields']))
            }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Created: {filename}")
    
    def create_by_file_list(self, filename: str = 'drugs_list_by_file.txt'):
        """Tạo danh sách theo file (dễ tìm thuốc trong file)"""
        drugs_by_file = defaultdict(list)
        for drug_name, drug_info in self.drugs.items():
            drugs_by_file[drug_info['file']].append(drug_name)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# DANH SACH THUOC THEO FILE\n")
            f.write(f"# Tong so: {len(self.drugs)} thuoc trong {len(drugs_by_file)} files\n")
            f.write(f"# Ngay tao: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for file_path in sorted(drugs_by_file.keys()):
                drugs = sorted(drugs_by_file[file_path])
                f.write(f"\n{'=' * 70}\n")
                f.write(f"FILE: {file_path}\n")
                f.write(f"So luong: {len(drugs)} thuoc\n")
                f.write(f"{'=' * 70}\n")
                for i, drug_name in enumerate(drugs, 1):
                    drug_info = self.drugs[drug_name]
                    status = "✅" if drug_info['has_14_fields'] else "⚠️"
                    f.write(f"{i:3d}. {status} {drug_name} ({drug_info['field_count']} fields)\n")
        
        print(f"Created: {filename}")
    
    def create_search_index(self, filename: str = 'drugs_search_index.txt'):
        """Tạo index tìm kiếm (theo chữ cái đầu)"""
        drugs_by_letter = defaultdict(list)
        for drug_name in self.drugs.keys():
            first_letter = drug_name[0].upper() if drug_name else 'OTHER'
            drugs_by_letter[first_letter].append(drug_name)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# DANH SACH THUOC - INDEX TIM KIEM\n")
            f.write(f"# Tong so: {len(self.drugs)}\n")
            f.write(f"# Ngay tao: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for letter in sorted(drugs_by_letter.keys()):
                drugs = sorted(drugs_by_letter[letter])
                f.write(f"\n{'=' * 70}\n")
                f.write(f"CHU CAI: {letter}\n")
                f.write(f"So luong: {len(drugs)} thuoc\n")
                f.write(f"{'=' * 70}\n")
                for i, drug_name in enumerate(drugs, 1):
                    drug_info = self.drugs[drug_name]
                    status = "✅" if drug_info['has_14_fields'] else "⚠️"
                    f.write(f"{i:3d}. {status} {drug_name}\n")
        
        print(f"Created: {filename}")
    
    def create_missing_fields_list(self, filename: str = 'drugs_missing_fields.txt'):
        """Tạo danh sách thuốc thiếu field"""
        drugs_missing = [d for d in self.drugs.values() if not d['has_14_fields']]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# DANH SACH THUOC THIEU FIELD\n")
            f.write(f"# Tong so: {len(drugs_missing)}\n")
            f.write(f"# Ngay tao: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if not drugs_missing:
                f.write("✅ Khong co thuoc nao thieu field!\n")
            else:
                for drug_info in sorted(drugs_missing, key=lambda x: len(x['missing_14_fields']), reverse=True):
                    f.write(f"\n{'=' * 70}\n")
                    f.write(f"THUOC: {drug_info['name']}\n")
                    f.write(f"File: {drug_info['file']}\n")
                    f.write(f"Field count: {drug_info['field_count']} (co {14-len(drug_info['missing_14_fields'])}/14 field chuan)\n")
                    f.write(f"Thieu {len(drug_info['missing_14_fields'])} fields:\n")
                    for field in drug_info['missing_14_fields']:
                        f.write(f"  - {field}\n")
        
        print(f"Created: {filename}")
    
    def create_all_lists(self):
        """Tạo tất cả danh sách"""
        print("\n" + "=" * 70)
        print("TAO DANH SACH THUOC O NHIEU DINH DANG")
        print("=" * 70)
        print()
        
        self.create_simple_list()
        self.create_detailed_list()
        self.create_csv_list()
        self.create_json_list()
        self.create_by_file_list()
        self.create_search_index()
        self.create_missing_fields_list()
        
        print("\n" + "=" * 70)
        print("HOAN TAT!")
        print("=" * 70)
        print("\nDa tao cac file danh sach:")
        print("  - drugs_list_simple.txt: Danh sach don gian (chi ten)")
        print("  - drugs_list_detailed.txt: Danh sach chi tiet (ten + file + field)")
        print("  - drugs_list.csv: Danh sach CSV (de import Excel)")
        print("  - drugs_list.json: Danh sach JSON (de xu ly bang code)")
        print("  - drugs_list_by_file.txt: Danh sach theo file")
        print("  - drugs_search_index.txt: Index tim kiem theo chu cai")
        print("  - drugs_missing_fields.txt: Danh sach thuoc thieu field")
        print()

def main():
    creator = DrugListCreator()
    creator.create_all_lists()

if __name__ == "__main__":
    main()

