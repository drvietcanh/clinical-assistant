"""
Tìm tất cả thuốc bằng cách tối ưu nhất
Tìm trong tất cả các dict có thể chứa thuốc
"""
import ast
import re
from pathlib import Path
from typing import Dict, Set, List
from collections import defaultdict

class OptimizedDrugFinder:
    """Tìm thuốc tối ưu - tìm tất cả dict có thể là thuốc"""
    
    def __init__(self):
        self.all_drugs = {}  # drug_name -> info
        self.found_by_method = defaultdict(set)
    
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
        # Phải có ít nhất 2 trong các field: group, vietnamese_name, administration, indications
        required_fields = {'group', 'vietnamese_name', 'administration', 'indications'}
        return len(keys & required_fields) >= 2
    
    def is_not_field_name(self, name: str) -> bool:
        """Kiểm tra xem tên có phải là field name không"""
        # Loại bỏ các field names đã biết
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
        
        # Loại bỏ pattern: tất cả lowercase với nhiều underscore
        if name.islower() and name.count('_') >= 2:
            if name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']:
                return False
        
        return True
    
    def find_all_dicts(self, node, file_path: str, depth=0, max_depth=10):
        """Tìm tất cả dict trong AST (recursive)"""
        if depth > max_depth:
            return
        
        if isinstance(node, ast.Dict):
            # Kiểm tra từng key-value pair
            for key_node, value_node in zip(node.keys, node.values):
                if isinstance(value_node, ast.Dict):
                    drug_name = self.get_string_value(key_node)
                    
                    if drug_name and self.is_not_field_name(drug_name):
                        value_keys = self.extract_dict_keys(value_node)
                        
                        if self.is_drug_entry(value_keys):
                            # Đây là thuốc!
                            if drug_name not in self.all_drugs:
                                self.all_drugs[drug_name] = {
                                    'file': file_path,
                                    'keys': value_keys,
                                    'field_count': len(value_keys)
                                }
                                self.found_by_method['ast_dicts'].add(drug_name)
            
            # Tiếp tục tìm trong nested dicts
            for key_node, value_node in zip(node.keys, node.values):
                self.find_all_dicts(value_node, file_path, depth + 1, max_depth)
        
        # Tìm trong các node con
        for child in ast.iter_child_nodes(node):
            self.find_all_dicts(child, file_path, depth + 1, max_depth)
    
    def find_by_regex(self, content: str, file_path: str):
        """Tìm bằng regex - backup method"""
        # Pattern: "Name": { ... với ít nhất 2 field của thuốc
        pattern = r'["\']([^"\']+)["\']\s*:\s*\{'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            potential_name = match.group(1)
            
            if not self.is_not_field_name(potential_name):
                continue
            
            # Tìm section của dict này
            start = match.end() - 1
            brace_count = 0
            in_string = False
            string_char = None
            i = start
            end_pos = None
            
            while i < len(content) and i < start + 15000:
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
                section = content[start:end_pos]
                
                # Đếm số field của thuốc
                required_fields = ['group', 'vietnamese_name', 'administration', 'indications']
                field_count = sum(1 for field in required_fields 
                                if re.search(rf'["\']{re.escape(field)}["\']\s*:', section))
                
                if field_count >= 2:
                    # Tìm tất cả field
                    keys = set()
                    all_fields = ['group', 'vietnamese_name', 'administration', 'indications', 'dosage',
                                'side_effects', 'contraindications', 'interactions', 'pregnancy',
                                'mechanism_of_action', 'monitoring', 'precautions', 'pharmacokinetics',
                                'storage', 'black_box_warnings', 'drug_interactions', 'pregnancy_lactation',
                                'hepatic_adjustment', 'overdose_management', 'reversal_agents',
                                'administration_instructions', 'references']
                    
                    for field in all_fields:
                        if re.search(rf'["\']{re.escape(field)}["\']\s*:', section):
                            keys.add(field)
                    
                    if potential_name not in self.all_drugs:
                        self.all_drugs[potential_name] = {
                            'file': file_path,
                            'keys': keys,
                            'field_count': len(keys)
                        }
                        self.found_by_method['regex'].add(potential_name)
    
    def analyze_file(self, file_path: Path):
        """Phân tích một file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Method 1: AST
            try:
                tree = ast.parse(content)
                self.find_all_dicts(tree, str(file_path.relative_to(Path("drugs/drug_modules").parent)))
            except:
                pass
            
            # Method 2: Regex (backup)
            self.find_by_regex(content, str(file_path.relative_to(Path("drugs/drug_modules").parent)))
            
        except Exception:
            pass
    
    def analyze_all_files(self):
        """Phân tích tất cả files"""
        base_path = Path("drugs/drug_modules")
        files_processed = 0
        
        for py_file in sorted(base_path.rglob("*.py")):
            if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
                continue
            
            self.analyze_file(py_file)
            files_processed += 1
        
        print(f"Processed {files_processed} files")
    
    def print_statistics(self):
        """In thống kê"""
        print("\n" + "=" * 70)
        print("THONG KE TIM THUOC TOI UU")
        print("=" * 70)
        print(f"\nTong so thuoc tim thay: {len(self.all_drugs)}")
        
        # Thống kê theo method
        print(f"\nTim thay boi AST: {len(self.found_by_method['ast_dicts'])}")
        print(f"Tim thay boi Regex: {len(self.found_by_method['regex'])}")
        
        # Thống kê field
        has_group = sum(1 for d in self.all_drugs.values() if 'group' in d['keys'])
        has_vietnamese = sum(1 for d in self.all_drugs.values() if 'vietnamese_name' in d['keys'])
        has_admin = sum(1 for d in self.all_drugs.values() if 'administration' in d['keys'])
        has_indications = sum(1 for d in self.all_drugs.values() if 'indications' in d['keys'])
        has_dosage = sum(1 for d in self.all_drugs.values() if 'dosage' in d['keys'])
        
        total = len(self.all_drugs)
        print(f"\nThong ke field:")
        print(f"  - group: {has_group} ({has_group*100//total if total > 0 else 0}%)")
        print(f"  - vietnamese_name: {has_vietnamese} ({has_vietnamese*100//total if total > 0 else 0}%)")
        print(f"  - administration: {has_admin} ({has_admin*100//total if total > 0 else 0}%)")
        print(f"  - indications: {has_indications} ({has_indications*100//total if total > 0 else 0}%)")
        print(f"  - dosage: {has_dosage} ({has_dosage*100//total if total > 0 else 0}%)")
        
        # Lưu danh sách
        with open('all_drugs_optimized.txt', 'w', encoding='utf-8') as f:
            f.write(f"# DANH SACH THUOC TIM THAY (TOI UU)\n")
            f.write(f"# Tong so: {len(self.all_drugs)}\n\n")
            for drug_name in sorted(self.all_drugs.keys()):
                data = self.all_drugs[drug_name]
                f.write(f"{drug_name}\n")
        
        # Lưu chi tiết
        with open('all_drugs_optimized_detail.txt', 'w', encoding='utf-8') as f:
            f.write(f"# DANH SACH THUOC CHI TIET\n")
            f.write(f"# Tong so: {len(self.all_drugs)}\n\n")
            for drug_name in sorted(self.all_drugs.keys()):
                data = self.all_drugs[drug_name]
                f.write(f"{drug_name} | {data['file']} | {data['field_count']} fields\n")
        
        print(f"\nDa luu:")
        print(f"  - all_drugs_optimized.txt: Danh sach ten thuoc")
        print(f"  - all_drugs_optimized_detail.txt: Danh sach chi tiet")
        print("=" * 70)
        
        return self.all_drugs

def main():
    finder = OptimizedDrugFinder()
    print("Dang tim thuoc bang phuong phap toi uu...")
    finder.analyze_all_files()
    drugs = finder.print_statistics()
    
    print(f"\nKet qua: Tim thay {len(drugs)} thuoc")
    if len(drugs) < 666:
        print(f"Con thieu {666 - len(drugs)} thuoc.")
        print("Kiem tra xem co thuoc nao bi bo sot khong...")
    elif len(drugs) > 666:
        print(f"Tim thay nhieu hon {len(drugs) - 666} thuoc. Co the co duplicates hoac entries khong phai thuoc.")
    else:
        print("Tim du 666 thuoc!")

if __name__ == "__main__":
    main()

