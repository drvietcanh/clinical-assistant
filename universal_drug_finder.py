"""
Hệ thống tìm kiếm thuốc phổ quát - xử lý mọi cấu trúc
Tìm đủ thuốc bất kể cấu trúc như thế nào
"""
import ast
import re
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional
from collections import defaultdict
import json

class UniversalDrugFinder:
    """Tìm thuốc với mọi cấu trúc có thể"""
    
    def __init__(self):
        self.all_drugs = {}  # drug_name -> {info}
        self.structure_patterns = defaultdict(list)  # pattern -> [drug_names]
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
    
    def is_likely_drug_name(self, name: str) -> bool:
        """Kiểm tra xem tên có phải là tên thuốc không (linh hoạt)"""
        if not name or len(name) < 2:
            return False
        
        # Loại bỏ field names đã biết
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
        
        # Loại bỏ pattern: tất cả lowercase với nhiều underscore
        if name.islower() and name.count('_') >= 2:
            if name not in ['iv', 'po', 'im', 'sc', 'iv_bolus', 'iv_infusion']:
                return False
        
        return True
    
    def is_drug_entry(self, keys: Set[str], strict: bool = False) -> bool:
        """Kiểm tra xem dict có phải là entry thuốc không (linh hoạt)"""
        # Phương pháp 1: Strict - phải có ít nhất 2 trong các field bắt buộc
        required_fields = {'group', 'vietnamese_name', 'administration', 'indications'}
        if len(keys & required_fields) >= 2:
            return True
        
        # Phương pháp 2: Flexible - có ít nhất 1 field bắt buộc + 1 field khác của thuốc
        if not strict:
            drug_indicators = {'group', 'vietnamese_name', 'administration', 'indications', 
                             'dosage', 'side_effects', 'contraindications', 'interactions',
                             'pregnancy', 'mechanism_of_action', 'monitoring', 'precautions'}
            has_required = bool(keys & required_fields)
            has_other = len(keys & drug_indicators) >= 2
            if has_required and has_other:
                return True
        
        return False
    
    def find_all_dicts_recursive(self, node, file_path: str, depth=0, max_depth=15):
        """Tìm tất cả dict trong AST (recursive, không giới hạn)"""
        if depth > max_depth:
            return
        
        if isinstance(node, ast.Dict):
            for key_node, value_node in zip(node.keys, node.values):
                if isinstance(value_node, ast.Dict):
                    drug_name = self.get_string_value(key_node)
                    
                    if drug_name and self.is_likely_drug_name(drug_name):
                        value_keys = self.extract_dict_keys(value_node)
                        
                        # Thử cả strict và flexible
                        if self.is_drug_entry(value_keys, strict=True) or self.is_drug_entry(value_keys, strict=False):
                            if drug_name not in self.all_drugs:
                                self.all_drugs[drug_name] = {
                                    'file': file_path,
                                    'keys': value_keys,
                                    'field_count': len(value_keys),
                                    'structure_type': self.detect_structure_type(value_keys)
                                }
                                self.found_by_method['ast_recursive'].add(drug_name)
            
            # Tiếp tục tìm trong nested
            for key_node, value_node in zip(node.keys, node.values):
                self.find_all_dicts_recursive(value_node, file_path, depth + 1, max_depth)
        
        # Tìm trong tất cả node con
        for child in ast.iter_child_nodes(node):
            self.find_all_dicts_recursive(child, file_path, depth + 1, max_depth)
    
    def detect_structure_type(self, keys: Set[str]) -> str:
        """Phát hiện loại cấu trúc của thuốc"""
        if 'group' in keys and 'vietnamese_name' in keys:
            if len(keys) >= 15:
                return 'full_structure'
            elif len(keys) >= 10:
                return 'standard_structure'
            else:
                return 'minimal_structure'
        elif 'group' in keys or 'vietnamese_name' in keys:
            return 'partial_structure'
        else:
            return 'alternative_structure'
    
    def find_by_regex_comprehensive(self, content: str, file_path: str):
        """Tìm bằng regex toàn diện - backup method"""
        # Pattern 1: "Name": { với field của thuốc
        pattern1 = r'["\']([^"\']+)["\']\s*:\s*\{'
        matches = re.finditer(pattern1, content)
        
        for match in matches:
            potential_name = match.group(1)
            
            if not self.is_likely_drug_name(potential_name):
                continue
            
            # Tìm section
            start = match.end() - 1
            brace_count = 0
            in_string = False
            string_char = None
            i = start
            end_pos = None
            
            while i < len(content) and i < start + 20000:
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
                
                # Tìm tất cả field
                keys = set()
                all_possible_fields = [
                    'group', 'vietnamese_name', 'administration', 'indications', 'dosage',
                    'side_effects', 'contraindications', 'interactions', 'pregnancy',
                    'mechanism_of_action', 'monitoring', 'precautions', 'pharmacokinetics',
                    'storage', 'black_box_warnings', 'drug_interactions', 'pregnancy_lactation',
                    'hepatic_adjustment', 'overdose_management', 'reversal_agents',
                    'administration_instructions', 'references'
                ]
                
                for field in all_possible_fields:
                    if re.search(rf'["\']{re.escape(field)}["\']\s*:', section):
                        keys.add(field)
                
                # Kiểm tra xem có phải thuốc không
                if self.is_drug_entry(keys, strict=False):
                    if potential_name not in self.all_drugs:
                        self.all_drugs[potential_name] = {
                            'file': file_path,
                            'keys': keys,
                            'field_count': len(keys),
                            'structure_type': self.detect_structure_type(keys)
                        }
                        self.found_by_method['regex_comprehensive'].add(potential_name)
    
    def find_in_assignments(self, tree, file_path: str):
        """Tìm trong tất cả assignments (không chỉ _DRUGS)"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                # Tìm tất cả dict assignments
                if isinstance(node.value, ast.Dict):
                    for key_node, value_node in zip(node.value.keys, node.value.values):
                        if isinstance(value_node, ast.Dict):
                            drug_name = self.get_string_value(key_node)
                            
                            if drug_name and self.is_likely_drug_name(drug_name):
                                value_keys = self.extract_dict_keys(value_node)
                                
                                if self.is_drug_entry(value_keys, strict=False):
                                    if drug_name not in self.all_drugs:
                                        self.all_drugs[drug_name] = {
                                            'file': file_path,
                                            'keys': value_keys,
                                            'field_count': len(value_keys),
                                            'structure_type': self.detect_structure_type(value_keys)
                                        }
                                        self.found_by_method['assignments'].add(drug_name)
    
    def analyze_file(self, file_path: Path):
        """Phân tích một file bằng tất cả phương pháp"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_path_str = str(file_path.relative_to(Path("drugs/drug_modules").parent))
            
            # Method 1: AST recursive
            try:
                tree = ast.parse(content)
                self.find_all_dicts_recursive(tree, file_path_str)
                self.find_in_assignments(tree, file_path_str)
            except:
                pass
            
            # Method 2: Regex comprehensive
            self.find_by_regex_comprehensive(content, file_path_str)
            
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
        """In thống kê chi tiết"""
        print("\n" + "=" * 70)
        print("THONG KE TIM THUOC PHO QUAT (MOI CAU TRUC)")
        print("=" * 70)
        print(f"\nTong so thuoc tim thay: {len(self.all_drugs)}")
        
        # Thống kê theo method
        print(f"\nTim thay boi:")
        for method, drugs in self.found_by_method.items():
            print(f"  {method}: {len(drugs)} thuoc")
        
        # Thống kê theo cấu trúc
        by_structure = defaultdict(int)
        for drug_info in self.all_drugs.values():
            by_structure[drug_info['structure_type']] += 1
        
        print(f"\nPhan bo theo cau truc:")
        for struct_type, count in sorted(by_structure.items(), key=lambda x: x[1], reverse=True):
            print(f"  {struct_type}: {count} thuoc")
        
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
        with open('all_drugs_universal.txt', 'w', encoding='utf-8') as f:
            f.write(f"# DANH SACH THUOC TIM THAY (PHO QUAT - MOI CAU TRUC)\n")
            f.write(f"# Tong so: {len(self.all_drugs)}\n\n")
            for drug_name in sorted(self.all_drugs.keys()):
                data = self.all_drugs[drug_name]
                f.write(f"{drug_name} | {data['file']} | {data['structure_type']} | {data['field_count']} fields\n")
        
        # Lưu JSON
        with open('all_drugs_universal.json', 'w', encoding='utf-8') as f:
            json.dump({
                'total': len(self.all_drugs),
                'drugs': {name: {
                    'file': info['file'],
                    'structure_type': info['structure_type'],
                    'fields': sorted(list(info['keys'])),
                    'field_count': info['field_count']
                } for name, info in self.all_drugs.items()}
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\nDa luu:")
        print(f"  - all_drugs_universal.txt: Danh sach chi tiet")
        print(f"  - all_drugs_universal.json: Database JSON")
        print("=" * 70)
        
        return self.all_drugs

def main():
    finder = UniversalDrugFinder()
    print("Dang tim thuoc bang phuong phap pho quat (xu ly moi cau truc)...")
    finder.analyze_all_files()
    drugs = finder.print_statistics()
    
    print(f"\nKet qua: Tim thay {len(drugs)} thuoc")
    if len(drugs) >= 666:
        print(f"✅ Tim du hoac nhieu hon 666 thuoc!")
    else:
        print(f"Con thieu {666 - len(drugs)} thuoc.")

if __name__ == "__main__":
    main()

