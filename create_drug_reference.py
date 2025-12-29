"""
Tạo file tham chiếu đầy đủ: danh sách thuốc, nhóm thuốc, cấu trúc
Để đảm bảo tính thống nhất khi thêm thuốc mới
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

class DrugReferenceCreator:
    """Tạo file tham chiếu đầy đủ"""
    
    def __init__(self):
        self.drugs = {}
        self.drugs_by_group = defaultdict(list)
        self.drugs_by_file = defaultdict(list)
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
        """Trích xuất các keys"""
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
                                # Lấy group nếu có
                                group = None
                                for k_node, v_node in zip(value_node.keys, value_node.values):
                                    k = self.get_string_value(k_node)
                                    if k == 'group':
                                        group = self.get_string_value(v_node)
                                        break
                                
                                self.drugs[drug_name] = {
                                    'name': drug_name,
                                    'file': file_path,
                                    'group': group,
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
    
    def organize_drugs(self):
        """Tổ chức thuốc"""
        for drug_name, drug_info in self.drugs.items():
            # Theo group
            if drug_info['group']:
                self.drugs_by_group[drug_info['group']].append(drug_name)
            
            # Theo file
            self.drugs_by_file[drug_info['file']].append(drug_name)
    
    def create_reference_file(self, filename: str = 'DRUG_REFERENCE_GUIDE.md'):
        """Tạo file tham chiếu đầy đủ"""
        content = []
        
        # Header
        content.append("# HƯỚNG DẪN THAM CHIẾU - THÊM THUỐC MỚI")
        content.append("")
        content.append("**Ngày tạo**: 2025-02-18")
        content.append("**Tổng số thuốc**: " + str(len(self.drugs)))
        content.append("")
        content.append("---")
        content.append("")
        content.append("## 📋 MỤC LỤC")
        content.append("")
        content.append("1. [Cấu trúc 14 field chuẩn](#cấu-trúc-14-field-chuẩn)")
        content.append("2. [Template thuốc mẫu](#template-thuốc-mẫu)")
        content.append("3. [Danh sách thuốc theo nhóm](#danh-sách-thuốc-theo-nhóm)")
        content.append("4. [Danh sách thuốc theo file](#danh-sách-thuốc-theo-file)")
        content.append("5. [Danh sách tất cả thuốc](#danh-sách-tất-cả-thuốc)")
        content.append("6. [Hướng dẫn thêm thuốc mới](#hướng-dẫn-thêm-thuốc-mới)")
        content.append("")
        content.append("---")
        content.append("")
        
        # Cấu trúc 14 field chuẩn
        content.append("## 1. CẤU TRÚC 14 FIELD CHUẨN")
        content.append("")
        content.append("### Thứ tự khoa học (BẮT BUỘC):")
        content.append("")
        for i, field in enumerate(STANDARD_14_FIELDS, 1):
            content.append(f"{i}. **{field}**")
        content.append("")
        content.append("### Mô tả từng field:")
        content.append("")
        field_descriptions = {
            "group": "Nhóm thuốc (ví dụ: 'Antibiotic - Aminoglycoside')",
            "vietnamese_name": "Tên tiếng Việt và biệt dược (ví dụ: 'Gentamicin, Garamycin')",
            "administration": "Đường dùng (list, ví dụ: ['IV', 'IM'])",
            "indications": "Chỉ định (list, ví dụ: ['Nhiễm khuẩn Gram-âm nặng', ...])",
            "dosage": "Liều dùng (dict với adult_standard, adult_maintenance, notes)",
            "side_effects": "Tác dụng phụ (list)",
            "contraindications": "Chống chỉ định (list)",
            "interactions": "Tương tác thuốc (list)",
            "pregnancy": "Phân loại thai kỳ (string, ví dụ: 'D - Độc thai nhi')",
            "mechanism_of_action": "Cơ chế tác dụng (string, mô tả chi tiết)",
            "monitoring": "Theo dõi (list)",
            "precautions": "Thận trọng (list)",
            "pharmacokinetics": "Dược động học (dict với half_life, onset, duration, protein_binding, clearance)",
            "storage": "Bảo quản (string)"
        }
        
        for field in STANDARD_14_FIELDS:
            content.append(f"- **{field}**: {field_descriptions.get(field, '')}")
        content.append("")
        content.append("---")
        content.append("")
        
        # Template thuốc mẫu
        content.append("## 2. TEMPLATE THUỐC MẪU")
        content.append("")
        content.append("```python")
        content.append('"DrugName": {')
        content.append('    # Core Fields (1-5)')
        content.append('    "group": "Antibiotic - Category",')
        content.append('    "vietnamese_name": "DrugName, BrandName",')
        content.append('    "administration": ["IV", "PO"],')
        content.append('    "indications": [')
        content.append('        "Chỉ định 1",')
        content.append('        "Chỉ định 2"')
        content.append('    ],')
        content.append('    "dosage": {')
        content.append('        "adult_standard": "Liều chuẩn",')
        content.append('        "adult_maintenance": "Liều duy trì",')
        content.append('        "notes": "Ghi chú"')
        content.append('    },')
        content.append('    ')
        content.append('    # Extended Fields (6-9)')
        content.append('    "side_effects": [')
        content.append('        "Tác dụng phụ 1",')
        content.append('        "Tác dụng phụ 2"')
        content.append('    ],')
        content.append('    "contraindications": [')
        content.append('        "Chống chỉ định 1",')
        content.append('        "Chống chỉ định 2"')
        content.append('    ],')
        content.append('    "interactions": [')
        content.append('        "Tương tác 1",')
        content.append('        "Tương tác 2"')
        content.append('    ],')
        content.append('    "pregnancy": "Category - Mô tả",')
        content.append('    ')
        content.append('    # Enhanced Fields (10-14)')
        content.append('    "mechanism_of_action": "Mô tả cơ chế tác dụng chi tiết...",')
        content.append('    "monitoring": [')
        content.append('        "Theo dõi 1",')
        content.append('        "Theo dõi 2"')
        content.append('    ],')
        content.append('    "precautions": [')
        content.append('        "Thận trọng 1",')
        content.append('        "Thận trọng 2"')
        content.append('    ],')
        content.append('    "pharmacokinetics": {')
        content.append('        "half_life": "...",')
        content.append('        "onset": "...",')
        content.append('        "duration": "...",')
        content.append('        "protein_binding": "...",')
        content.append('        "clearance": "..."')
        content.append('    },')
        content.append('    "storage": "Hướng dẫn bảo quản"')
        content.append('}')
        content.append("```")
        content.append("")
        content.append("---")
        content.append("")
        
        # Danh sách thuốc theo nhóm
        content.append("## 3. DANH SÁCH THUỐC THEO NHÓM")
        content.append("")
        content.append(f"**Tổng số nhóm**: {len(self.drugs_by_group)}")
        content.append("")
        
        sorted_groups = sorted(self.drugs_by_group.items(), key=lambda x: len(x[1]), reverse=True)
        
        for group, drugs in sorted_groups:
            content.append(f"### {group}")
            content.append(f"**Số lượng**: {len(drugs)} thuốc")
            content.append("")
            content.append("Danh sách:")
            for i, drug in enumerate(sorted(drugs), 1):
                drug_info = self.drugs[drug]
                content.append(f"{i:3d}. {drug} ({drug_info['file']})")
            content.append("")
        
        content.append("---")
        content.append("")
        
        # Danh sách thuốc theo file
        content.append("## 4. DANH SÁCH THUỐC THEO FILE")
        content.append("")
        content.append(f"**Tổng số file**: {len(self.drugs_by_file)}")
        content.append("")
        
        sorted_files = sorted(self.drugs_by_file.items(), key=lambda x: len(x[1]), reverse=True)
        
        for file_path, drugs in sorted_files:
            content.append(f"### {file_path}")
            content.append(f"**Số lượng**: {len(drugs)} thuốc")
            content.append("")
            for i, drug in enumerate(sorted(drugs), 1):
                content.append(f"{i:3d}. {drug}")
            content.append("")
        
        content.append("---")
        content.append("")
        
        # Danh sách tất cả thuốc
        content.append("## 5. DANH SÁCH TẤT CẢ THUỐC")
        content.append("")
        content.append(f"**Tổng số**: {len(self.drugs)} thuốc")
        content.append("")
        
        for i, drug_name in enumerate(sorted(self.drugs.keys()), 1):
            drug_info = self.drugs[drug_name]
            content.append(f"{i:3d}. **{drug_name}**")
            content.append(f"    - Nhóm: {drug_info['group'] or 'N/A'}")
            content.append(f"    - File: {drug_info['file']}")
            content.append(f"    - Fields: {drug_info['field_count']}")
            content.append("")
        
        content.append("---")
        content.append("")
        
        # Hướng dẫn thêm thuốc mới
        content.append("## 6. HƯỚNG DẪN THÊM THUỐC MỚI")
        content.append("")
        content.append("### Bước 1: Xác định nhóm thuốc")
        content.append("")
        content.append("Xem danh sách nhóm ở trên để xác định nhóm phù hợp.")
        content.append("Nếu không có nhóm phù hợp, tạo nhóm mới theo format: `'Category - Subcategory'`")
        content.append("")
        content.append("### Bước 2: Xác định file chứa")
        content.append("")
        content.append("Xem danh sách file ở trên để xác định file phù hợp.")
        content.append("Nếu không có file phù hợp, tạo file mới trong thư mục tương ứng.")
        content.append("")
        content.append("### Bước 3: Sử dụng template")
        content.append("")
        content.append("Copy template ở trên và điền thông tin:")
        content.append("1. Thay `DrugName` bằng tên thuốc")
        content.append("2. Điền đầy đủ 14 field chuẩn theo thứ tự")
        content.append("3. Đảm bảo tất cả field đều có giá trị (không để rỗng)")
        content.append("")
        content.append("### Bước 4: Kiểm tra")
        content.append("")
        content.append("```bash")
        content.append("# Kiểm tra thuốc mới")
        content.append("python comprehensive_drug_management_system.py check <DrugName>")
        content.append("")
        content.append("# Kiểm tra trạng thái")
        content.append("python comprehensive_drug_management_system.py stats")
        content.append("")
        content.append("# Cập nhật danh sách")
        content.append("python create_drug_lists.py")
        content.append("```")
        content.append("")
        content.append("### Bước 5: Cập nhật file tham chiếu")
        content.append("")
        content.append("Sau khi thêm thuốc mới, chạy lại script này để cập nhật file tham chiếu:")
        content.append("```bash")
        content.append("python create_drug_reference.py")
        content.append("```")
        content.append("")
        content.append("---")
        content.append("")
        content.append("## ⚠️ LƯU Ý QUAN TRỌNG")
        content.append("")
        content.append("1. **Bắt buộc có đủ 14 field chuẩn** - Không được thiếu field nào")
        content.append("2. **Thứ tự field** - Nên theo thứ tự chuẩn (có thể linh hoạt nhưng nên tuân thủ)")
        content.append("3. **Tên thuốc** - Phải là tên chính xác, không trùng lặp")
        content.append("4. **Nhóm thuốc** - Phải nhất quán với các thuốc cùng loại")
        content.append("5. **File chứa** - Nên đặt trong file phù hợp với nhóm")
        content.append("")
        content.append("---")
        content.append("")
        content.append("**Cập nhật lần cuối**: 2025-02-18")
        content.append("**Tổng số thuốc**: " + str(len(self.drugs)))
        content.append("")
        
        # Ghi file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        
        print(f"Created reference file: {filename}")
    
    def create_json_reference(self, filename: str = 'drug_reference_data.json'):
        """Tạo file JSON tham chiếu"""
        data = {
            'created_date': '2025-02-18',
            'total_drugs': len(self.drugs),
            'standard_14_fields': STANDARD_14_FIELDS,
            'drugs_by_group': {group: sorted(drugs) for group, drugs in self.drugs_by_group.items()},
            'drugs_by_file': {file_path: sorted(drugs) for file_path, drugs in self.drugs_by_file.items()},
            'all_drugs': {
                drug_name: {
                    'group': drug_info['group'],
                    'file': drug_info['file'],
                    'field_count': drug_info['field_count']
                }
                for drug_name, drug_info in sorted(self.drugs.items())
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Created JSON reference: {filename}")

def main():
    print("=" * 70)
    print("TAO FILE THAM CHIEU DAY DU")
    print("=" * 70)
    print()
    
    creator = DrugReferenceCreator()
    creator.create_reference_file()
    creator.create_json_reference()
    
    print()
    print("=" * 70)
    print("HOAN TAT!")
    print("=" * 70)
    print()
    print("Da tao:")
    print("  - DRUG_REFERENCE_GUIDE.md: File tham chieu day du")
    print("  - drug_reference_data.json: Du lieu JSON tham chieu")

if __name__ == "__main__":
    main()

