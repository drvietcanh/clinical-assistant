"""
Hệ thống chuẩn hóa cấu trúc thuốc
Đảm bảo mỗi thuốc có cấu trúc đồng bộ, khoa học, dễ tìm kiếm và sửa chữa
"""
import ast
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict
from datetime import datetime
import shutil

# Định nghĩa 14 field chuẩn (theo thứ tự khoa học)
STANDARD_14_FIELDS = [
    # Core fields (5)
    "group",                    # 1. Nhóm thuốc
    "vietnamese_name",          # 2. Tên tiếng Việt
    "administration",           # 3. Đường dùng
    "indications",              # 4. Chỉ định
    "dosage",                   # 5. Liều dùng
    
    # Extended fields (4)
    "side_effects",             # 6. Tác dụng phụ
    "contraindications",        # 7. Chống chỉ định
    "interactions",             # 8. Tương tác thuốc
    "pregnancy",                # 9. Thai kỳ
    
    # Enhanced fields (5 - quan trọng nhất)
    "mechanism_of_action",      # 10. Cơ chế tác dụng
    "monitoring",               # 11. Theo dõi
    "precautions",              # 12. Thận trọng
    "pharmacokinetics",         # 13. Dược động học
    "storage",                  # 14. Bảo quản
]

# Các field bổ sung (không bắt buộc nhưng nên có)
ADDITIONAL_FIELDS = [
    "black_box_warnings",
    "drug_interactions",
    "pregnancy_lactation",
    "hepatic_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions",
    "references",
]

ALL_STANDARD_FIELDS = STANDARD_14_FIELDS + ADDITIONAL_FIELDS

# Template cho từng field (cấu trúc chuẩn)
FIELD_TEMPLATES = {
    "group": '        "group": "",',
    "vietnamese_name": '        "vietnamese_name": "",',
    "administration": '        "administration": [],',
    "indications": '        "indications": [],',
    "dosage": '''        "dosage": {
            "adult_standard": "",
            "adult_maintenance": "",
            "notes": ""
        },''',
    "side_effects": '        "side_effects": [],',
    "contraindications": '        "contraindications": [],',
    "interactions": '        "interactions": [],',
    "pregnancy": '        "pregnancy": "",',
    "mechanism_of_action": '        "mechanism_of_action": "",',
    "monitoring": '        "monitoring": [],',
    "precautions": '        "precautions": [],',
    "pharmacokinetics": '''        "pharmacokinetics": {
            "half_life": "",
            "onset": "",
            "duration": "",
            "protein_binding": "",
            "clearance": ""
        },''',
    "storage": '        "storage": "",',
    "black_box_warnings": '        "black_box_warnings": None,',
    "drug_interactions": '''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },''',
    "pregnancy_lactation": '''        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },''',
    "hepatic_adjustment": '''        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },''',
    "overdose_management": '''        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },''',
    "reversal_agents": '''        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },''',
    "administration_instructions": '''        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },''',
    "references": '''        "references": {
            "primary_sources": [],
            "guidelines": [],
            "other": []
        },''',
}

class DrugStructureStandardizer:
    """Chuẩn hóa cấu trúc thuốc"""
    
    def __init__(self):
        self.drugs = {}
        self.analysis_results = {}
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
    
    def analyze_structure(self):
        """Phân tích cấu trúc hiện tại"""
        analysis = {
            'total_drugs': len(self.drugs),
            'drugs_with_14_fields': 0,
            'drugs_missing_fields': [],
            'field_statistics': defaultdict(int),
            'structure_variations': defaultdict(list)
        }
        
        for drug_name, drug_info in self.drugs.items():
            fields = drug_info['fields']
            
            # Đếm số field chuẩn có
            standard_fields_count = len([f for f in STANDARD_14_FIELDS if f in fields])
            
            if standard_fields_count == 14:
                analysis['drugs_with_14_fields'] += 1
            else:
                missing = [f for f in STANDARD_14_FIELDS if f not in fields]
                analysis['drugs_missing_fields'].append({
                    'name': drug_name,
                    'file': drug_info['file'],
                    'missing': missing,
                    'missing_count': len(missing),
                    'has_count': standard_fields_count
                })
            
            # Thống kê field
            for field in ALL_STANDARD_FIELDS:
                if field in fields:
                    analysis['field_statistics'][field] += 1
            
            # Phân loại cấu trúc
            structure_type = self.classify_structure(fields)
            analysis['structure_variations'][structure_type].append(drug_name)
        
        self.analysis_results = analysis
        return analysis
    
    def classify_structure(self, fields: Set[str]) -> str:
        """Phân loại cấu trúc thuốc"""
        standard_count = len([f for f in STANDARD_14_FIELDS if f in fields])
        additional_count = len([f for f in ADDITIONAL_FIELDS if f in fields])
        
        if standard_count == 14 and additional_count >= 5:
            return 'complete_structure'
        elif standard_count == 14:
            return 'standard_14_fields'
        elif standard_count >= 10:
            return 'partial_structure'
        else:
            return 'minimal_structure'
    
    def print_analysis_report(self):
        """In báo cáo phân tích"""
        analysis = self.analysis_results
        
        print("\n" + "=" * 70)
        print("BAO CAO PHAN TICH CAU TRUC THUOC")
        print("=" * 70)
        
        print(f"\nTong so thuoc: {analysis['total_drugs']}")
        print(f"Thuoc co du 14 field chuan: {analysis['drugs_with_14_fields']} ({analysis['drugs_with_14_fields']*100//analysis['total_drugs'] if analysis['total_drugs'] > 0 else 0}%)")
        print(f"Thuoc thieu field: {len(analysis['drugs_missing_fields'])} ({len(analysis['drugs_missing_fields'])*100//analysis['total_drugs'] if analysis['total_drugs'] > 0 else 0}%)")
        
        print(f"\nPhan bo theo cau truc:")
        for struct_type, drugs in sorted(analysis['structure_variations'].items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  {struct_type}: {len(drugs)} thuoc")
        
        print(f"\nThong ke field (14 field chuan):")
        for field in STANDARD_14_FIELDS:
            count = analysis['field_statistics'][field]
            pct = count * 100 // analysis['total_drugs'] if analysis['total_drugs'] > 0 else 0
            print(f"  {field}: {count} ({pct}%)")
        
        # Top 10 thuốc thiếu nhiều field nhất
        if analysis['drugs_missing_fields']:
            sorted_missing = sorted(analysis['drugs_missing_fields'], 
                                  key=lambda x: x['missing_count'], reverse=True)
            print(f"\nTop 10 thuoc thieu nhieu field nhat:")
            for i, drug in enumerate(sorted_missing[:10], 1):
                print(f"  {i}. {drug['name']}: thieu {drug['missing_count']} fields (co {drug['has_count']}/14)")
                print(f"     File: {drug['file']}")
                print(f"     Thieu: {', '.join(drug['missing'][:5])}{'...' if len(drug['missing']) > 5 else ''}")
        
        print("=" * 70)
    
    def generate_standardization_plan(self) -> Dict:
        """Tạo kế hoạch chuẩn hóa"""
        plan = {
            'total_drugs': len(self.drugs),
            'drugs_to_standardize': [],
            'priority_order': []
        }
        
        analysis = self.analysis_results
        
        # Sắp xếp theo mức độ ưu tiên
        # 1. Thuốc thiếu ít field nhất (dễ chuẩn hóa)
        # 2. Thuốc thiếu nhiều field (cần bổ sung)
        
        sorted_missing = sorted(analysis['drugs_missing_fields'],
                              key=lambda x: (x['missing_count'], -x['has_count']))
        
        plan['drugs_to_standardize'] = sorted_missing
        plan['priority_order'] = [d['name'] for d in sorted_missing]
        
        return plan
    
    def save_analysis_report(self, filename: str = 'drug_structure_analysis.json'):
        """Lưu báo cáo phân tích"""
        report = {
            'analysis_date': datetime.now().isoformat(),
            'analysis': self.analysis_results,
            'standardization_plan': self.generate_standardization_plan(),
            'standard_14_fields': STANDARD_14_FIELDS,
            'additional_fields': ADDITIONAL_FIELDS
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\nDa luu bao cao phan tich: {filename}")

def main():
    """Main function"""
    print("=" * 70)
    print("HE THONG CHUAN HOA CAU TRUC THUOC")
    print("=" * 70)
    print()
    
    standardizer = DrugStructureStandardizer()
    standardizer.analyze_structure()
    standardizer.print_analysis_report()
    standardizer.save_analysis_report()
    
    plan = standardizer.generate_standardization_plan()
    print(f"\nKe hoach chuan hoa:")
    print(f"  - Tong so thuoc can chuan hoa: {len(plan['drugs_to_standardize'])}")
    print(f"  - Uu tien: Bat dau voi {len([d for d in plan['drugs_to_standardize'] if d['missing_count'] <= 3])} thuoc thieu it field nhat")

if __name__ == "__main__":
    main()

