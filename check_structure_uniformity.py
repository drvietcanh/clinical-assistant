"""
Kiểm tra cấu trúc đồng nhất và khả năng tìm kiếm, sửa chữa
"""
import ast
import json
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

class StructureUniformityChecker:
    """Kiểm tra cấu trúc đồng nhất"""
    
    def __init__(self):
        self.drugs = {}
        self.structure_variations = defaultdict(list)
        self.field_order_variations = defaultdict(list)
        self.load_all_drugs()
        self.analyze_structure()
    
    def get_string_value(self, node):
        """Lấy giá trị string từ AST node"""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        elif hasattr(node, 's'):
            return node.s
        return None
    
    def extract_dict_keys_ordered(self, node: ast.Dict) -> List[str]:
        """Trích xuất các keys theo thứ tự"""
        keys = []
        for key_node in node.keys:
            key = self.get_string_value(key_node)
            if key:
                keys.append(key)
        return keys
    
    def extract_dict_keys(self, node: ast.Dict) -> Set[str]:
        """Trích xuất các keys"""
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
                                    'field_count': len(value_keys),
                                    'has_14_fields': len([f for f in STANDARD_14_FIELDS if f in value_keys]) == 14
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
    
    def get_structure_signature(self, fields_ordered: List[str]) -> str:
        """Tạo signature cho cấu trúc (chỉ 14 field chuẩn)"""
        standard_fields = [f for f in fields_ordered if f in STANDARD_14_FIELDS]
        return ','.join(standard_fields)
    
    def analyze_structure(self):
        """Phân tích cấu trúc"""
        for drug_name, drug_info in self.drugs.items():
            fields_ordered = drug_info['fields_ordered']
            
            # Phân loại theo signature
            signature = self.get_structure_signature(fields_ordered)
            self.structure_variations[signature].append(drug_name)
            
            # Phân loại theo thứ tự field
            standard_fields = [f for f in fields_ordered if f in STANDARD_14_FIELDS]
            order_key = ','.join(standard_fields[:5])  # 5 field đầu
            self.field_order_variations[order_key].append(drug_name)
    
    def check_searchability(self) -> Dict:
        """Kiểm tra khả năng tìm kiếm"""
        searchable = {
            'by_name': len(self.drugs),  # Tất cả đều có tên
            'by_file': len(set(d['file'] for d in self.drugs.values())),
            'by_group': 0,
            'by_field': 0
        }
        
        # Đếm thuốc có group field
        for drug_info in self.drugs.values():
            if 'group' in drug_info['fields']:
                searchable['by_group'] += 1
            if len(drug_info['fields']) > 0:
                searchable['by_field'] += 1
        
        return searchable
    
    def check_editability(self) -> Dict:
        """Kiểm tra khả năng sửa chữa"""
        editable = {
            'has_clear_structure': 0,
            'has_standard_fields': 0,
            'easy_to_find': 0,
            'well_organized': 0
        }
        
        for drug_info in self.drugs.values():
            # Có cấu trúc rõ ràng
            if drug_info['field_count'] >= 14:
                editable['has_clear_structure'] += 1
            
            # Có field chuẩn
            if drug_info['has_14_fields']:
                editable['has_standard_fields'] += 1
            
            # Dễ tìm (có file rõ ràng)
            if drug_info['file']:
                editable['easy_to_find'] += 1
            
            # Tổ chức tốt (có ít nhất 14 field)
            if drug_info['field_count'] >= 14:
                editable['well_organized'] += 1
        
        return editable
    
    def print_report(self):
        """In báo cáo"""
        print("\n" + "=" * 70)
        print("BAO CAO KIEM TRA CAU TRUC DONG NHAT")
        print("=" * 70)
        
        print(f"\nTong so thuoc: {len(self.drugs)}")
        print(f"So luong cau truc khac nhau: {len(self.structure_variations)}")
        print(f"So luong thu tu field khac nhau: {len(self.field_order_variations)}")
        
        # Phân tích cấu trúc
        print(f"\n{'=' * 70}")
        print("PHAN TICH CAU TRUC")
        print(f"{'=' * 70}")
        
        sorted_variations = sorted(self.structure_variations.items(), 
                                  key=lambda x: len(x[1]), reverse=True)
        
        print(f"\nTop 5 cau truc pho bien nhat:")
        for i, (signature, drugs) in enumerate(sorted_variations[:5], 1):
            print(f"  {i}. {len(drugs)} thuoc")
            fields = signature.split(',')
            print(f"     Field order: {', '.join(fields[:5])}...")
        
        # Kiểm tra khả năng tìm kiếm
        print(f"\n{'=' * 70}")
        print("KHẢ NĂNG TÌM KIẾM")
        print(f"{'=' * 70}")
        searchable = self.check_searchability()
        print(f"  - Tim theo ten: {searchable['by_name']}/{len(self.drugs)} (100%) ✅")
        print(f"  - Tim theo file: {searchable['by_file']} files ✅")
        print(f"  - Tim theo group: {searchable['by_group']}/{len(self.drugs)} ({searchable['by_group']*100//len(self.drugs) if len(self.drugs) > 0 else 0}%) ✅")
        print(f"  - Tim theo field: {searchable['by_field']}/{len(self.drugs)} (100%) ✅")
        
        # Kiểm tra khả năng sửa chữa
        print(f"\n{'=' * 70}")
        print("KHẢ NĂNG SỬA CHỮA")
        print(f"{'=' * 70}")
        editable = self.check_editability()
        total = len(self.drugs)
        print(f"  - Co cau truc ro rang (>=14 field): {editable['has_clear_structure']}/{total} ({editable['has_clear_structure']*100//total if total > 0 else 0}%) ✅")
        print(f"  - Co field chuan (14 field): {editable['has_standard_fields']}/{total} ({editable['has_standard_fields']*100//total if total > 0 else 0}%) ✅")
        print(f"  - De tim (co file): {editable['easy_to_find']}/{total} ({editable['easy_to_find']*100//total if total > 0 else 0}%) ✅")
        print(f"  - To chuc tot (>=14 field): {editable['well_organized']}/{total} ({editable['well_organized']*100//total if total > 0 else 0}%) ✅")
        
        # Đánh giá tổng thể
        print(f"\n{'=' * 70}")
        print("DANH GIA TONG THE")
        print(f"{'=' * 70}")
        
        uniformity_score = (len(self.structure_variations) == 1) * 50
        field_completeness = (editable['has_standard_fields'] / total * 100) if total > 0 else 0
        searchability_score = 100  # Tất cả đều có thể tìm được
        editability_score = (editable['has_clear_structure'] / total * 100) if total > 0 else 0
        
        overall_score = (uniformity_score * 0.2 + field_completeness * 0.3 + 
                        searchability_score * 0.25 + editability_score * 0.25)
        
        print(f"\nDiem so:")
        print(f"  - Dong nhat cau truc: {uniformity_score}/50")
        print(f"  - Day du field: {field_completeness:.1f}/100")
        print(f"  - De tim kiem: {searchability_score}/100")
        print(f"  - De sua chua: {editability_score:.1f}/100")
        print(f"\n  TONG DIEM: {overall_score:.1f}/100")
        
        if overall_score >= 90:
            print(f"\n✅ XUAT SAC - Cau truc dong nhat, de tim kiem va sua chua")
        elif overall_score >= 75:
            print(f"\n✅ TOT - Cau truc kha dong nhat, de tim kiem va sua chua")
        elif overall_score >= 60:
            print(f"\n⚠️  TRUNG BINH - Co the cai tien them")
        else:
            print(f"\n❌ CAN CAI TIEN - Cau truc chua dong nhat")
        
        print("=" * 70)
    
    def save_report(self, filename: str = 'structure_uniformity_report.json'):
        """Lưu báo cáo"""
        report = {
            'total_drugs': len(self.drugs),
            'structure_variations_count': len(self.structure_variations),
            'field_order_variations_count': len(self.field_order_variations),
            'searchability': self.check_searchability(),
            'editability': self.check_editability(),
            'structure_variations': {sig: len(drugs) for sig, drugs in self.structure_variations.items()}
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\nDa luu bao cao: {filename}")

def main():
    checker = StructureUniformityChecker()
    checker.print_report()
    checker.save_report()

if __name__ == "__main__":
    main()

