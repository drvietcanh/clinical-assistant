"""
Phân tích toàn diện để tìm đủ 666 thuốc
Sử dụng nhiều cách tiếp cận khác nhau
"""
import ast
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class ComprehensiveDrugFinder:
    """Tìm thuốc bằng nhiều phương pháp"""
    
    def __init__(self):
        self.all_found_drugs = {}  # drug_name -> {methods: [], info: {}}
        self.methods_used = []
    
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
        """Kiểm tra xem tên có phải là tên thuốc không"""
        # Loại bỏ field names
        non_drug_patterns = [
            r'^[a-z_]+$',  # Tất cả lowercase với underscore
            r'^(oral|im|sc|iv|po|inhaled|inhalation)$',
            r'^(normal|30_60|under_30|mild|moderate|severe)$',
            r'^(major|minor|tuyệt_đối|tương_đối)$',
        ]
        
        for pattern in non_drug_patterns:
            if re.match(pattern, name, re.IGNORECASE):
                return False
        
        # Tên thuốc thường có chữ hoa hoặc chứa số
        if name[0].isupper() or any(c.isdigit() for c in name):
            return True
        
        # Hoặc có dấu gạch chéo (combination drugs)
        if '/' in name:
            return True
        
        return False
    
    def method1_find_drugs_variables(self, content: str, file_path: Path) -> Dict[str, Dict]:
        """Method 1: Tìm trong các biến _DRUGS"""
        drugs = {}
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                            if isinstance(node.value, ast.Dict):
                                for key_node, value_node in zip(node.value.keys, node.value.values):
                                    drug_name = self.get_string_value(key_node)
                                    if drug_name and isinstance(value_node, ast.Dict):
                                        value_keys = self.extract_dict_keys(value_node)
                                        if self.is_likely_drug_name(drug_name):
                                            drugs[drug_name] = {
                                                'method': 'method1_variables',
                                                'file': str(file_path),
                                                'keys': value_keys
                                            }
        except:
            pass
        return drugs
    
    def method2_find_drugs_regex(self, content: str, file_path: Path) -> Dict[str, Dict]:
        """Method 2: Tìm bằng regex pattern"""
        drugs = {}
        # Pattern: "DrugName": { ... với ít nhất một field của thuốc
        pattern = r'["\']([^"\']+)["\']\s*:\s*\{[^}]*["\'](group|vietnamese_name|administration|indications)["\']'
        matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            drug_name = match.group(1)
            if self.is_likely_drug_name(drug_name):
                # Tìm các field trong section này
                start = match.start()
                end = min(start + 5000, len(content))
                section = content[start:end]
                
                keys = set()
                for field in ['group', 'vietnamese_name', 'administration', 'indications', 'dosage']:
                    if re.search(rf'["\']{field}["\']\s*:', section):
                        keys.add(field)
                
                if len(keys) >= 2:  # Có ít nhất 2 field
                    drugs[drug_name] = {
                        'method': 'method2_regex',
                        'file': str(file_path),
                        'keys': keys
                    }
        
        return drugs
    
    def method3_find_drugs_ast_dicts(self, content: str, file_path: Path) -> Dict[str, Dict]:
        """Method 3: Tìm tất cả dict có key là string và value là dict"""
        drugs = {}
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    for key_node, value_node in zip(node.keys, node.values):
                        if isinstance(value_node, ast.Dict):
                            drug_name = self.get_string_value(key_node)
                            if drug_name and self.is_likely_drug_name(drug_name):
                                value_keys = self.extract_dict_keys(value_node)
                                # Phải có ít nhất 2 field của thuốc
                                drug_fields = {'group', 'vietnamese_name', 'administration', 'indications', 'dosage'}
                                if len(value_keys & drug_fields) >= 2:
                                    drugs[drug_name] = {
                                        'method': 'method3_ast_dicts',
                                        'file': str(file_path),
                                        'keys': value_keys
                                    }
        except:
            pass
        return drugs
    
    def method4_find_drugs_nested_dicts(self, content: str, file_path: Path) -> Dict[str, Dict]:
        """Method 4: Tìm trong nested dicts (không chỉ top-level)"""
        drugs = {}
        try:
            tree = ast.parse(content)
            
            def find_dicts_in_node(node, depth=0):
                if depth > 5:  # Giới hạn độ sâu
                    return
                
                if isinstance(node, ast.Dict):
                    for key_node, value_node in zip(node.keys, node.values):
                        if isinstance(value_node, ast.Dict):
                            drug_name = self.get_string_value(key_node)
                            if drug_name and self.is_likely_drug_name(drug_name):
                                value_keys = self.extract_dict_keys(value_node)
                                drug_fields = {'group', 'vietnamese_name', 'administration', 'indications', 'dosage'}
                                if len(value_keys & drug_fields) >= 2:
                                    if drug_name not in drugs:
                                        drugs[drug_name] = {
                                            'method': 'method4_nested',
                                            'file': str(file_path),
                                            'keys': value_keys
                                        }
                            
                            # Tiếp tục tìm trong nested
                            find_dicts_in_node(value_node, depth + 1)
                
                # Tìm trong các node con
                for child in ast.iter_child_nodes(node):
                    find_dicts_in_node(child, depth + 1)
            
            find_dicts_in_node(tree)
        except:
            pass
        return drugs
    
    def method5_find_drugs_by_content(self, content: str, file_path: Path) -> Dict[str, Dict]:
        """Method 5: Tìm bằng phân tích nội dung (tìm pattern thuốc)"""
        drugs = {}
        # Tìm tất cả string keys có thể là tên thuốc
        # Pattern: "Name": { ... với nhiều field
        pattern = r'["\']([A-Z][^"\']*?)["\']\s*:\s*\{'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            potential_name = match.group(1)
            if self.is_likely_drug_name(potential_name):
                # Kiểm tra section này có phải là thuốc không
                start = match.end() - 1
                brace_count = 0
                in_string = False
                string_char = None
                i = start
                end_pos = None
                
                while i < len(content) and i < start + 10000:
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
                    drug_field_count = 0
                    for field in ['group', 'vietnamese_name', 'administration', 'indications', 'dosage']:
                        if re.search(rf'["\']{field}["\']\s*:', section):
                            drug_field_count += 1
                    
                    if drug_field_count >= 2:
                        keys = set()
                        for field in ['group', 'vietnamese_name', 'administration', 'indications', 'dosage', 
                                    'side_effects', 'contraindications', 'interactions', 'pregnancy']:
                            if re.search(rf'["\']{field}["\']\s*:', section):
                                keys.add(field)
                        
                        drugs[potential_name] = {
                            'method': 'method5_content',
                            'file': str(file_path),
                            'keys': keys
                        }
        
        return drugs
    
    def analyze_all_files(self):
        """Phân tích tất cả files bằng tất cả methods"""
        base_path = Path("drugs/drug_modules")
        files_processed = 0
        
        for py_file in sorted(base_path.rglob("*.py")):
            if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Method 1: Variables
                drugs1 = self.method1_find_drugs_variables(content, py_file)
                self.add_drugs(drugs1, 'method1')
                
                # Method 2: Regex
                drugs2 = self.method2_find_drugs_regex(content, py_file)
                self.add_drugs(drugs2, 'method2')
                
                # Method 3: AST Dicts
                drugs3 = self.method3_find_drugs_ast_dicts(content, py_file)
                self.add_drugs(drugs3, 'method3')
                
                # Method 4: Nested Dicts
                drugs4 = self.method4_find_drugs_nested_dicts(content, py_file)
                self.add_drugs(drugs4, 'method4')
                
                # Method 5: Content Analysis
                drugs5 = self.method5_find_drugs_by_content(content, py_file)
                self.add_drugs(drugs5, 'method5')
                
                files_processed += 1
                
            except Exception as e:
                pass
        
        print(f"Processed {files_processed} files")
    
    def add_drugs(self, drugs: Dict, method: str):
        """Thêm thuốc vào danh sách tổng hợp"""
        for drug_name, info in drugs.items():
            if drug_name not in self.all_found_drugs:
                self.all_found_drugs[drug_name] = {
                    'methods': [],
                    'info': info
                }
            
            if method not in self.all_found_drugs[drug_name]['methods']:
                self.all_found_drugs[drug_name]['methods'].append(method)
    
    def get_final_drugs(self) -> Dict[str, Dict]:
        """Lấy danh sách thuốc cuối cùng (loại bỏ duplicates và non-drugs)"""
        final_drugs = {}
        
        for drug_name, data in self.all_found_drugs.items():
            info = data['info']
            keys = info.get('keys', set())
            
            # Kiểm tra lại xem có phải thuốc không
            drug_fields = {'group', 'vietnamese_name', 'administration', 'indications', 'dosage'}
            has_required = len(keys & drug_fields) >= 2
            
            if has_required:
                final_drugs[drug_name] = {
                    'file': info['file'],
                    'keys': keys,
                    'methods': data['methods'],
                    'field_count': len(keys)
                }
        
        return final_drugs
    
    def print_statistics(self):
        """In thống kê"""
        final_drugs = self.get_final_drugs()
        
        print("\n" + "=" * 70)
        print("THONG KE TIM THUOC BANG NHIEU PHUONG PHAP")
        print("=" * 70)
        print(f"\nTong so thuoc tim thay: {len(final_drugs)}")
        
        # Thống kê theo method
        by_method = defaultdict(int)
        for drug_name, data in final_drugs.items():
            for method in data['methods']:
                by_method[method] += 1
        
        print("\nSo luong thuoc tim thay boi moi method:")
        for method, count in sorted(by_method.items(), key=lambda x: x[1], reverse=True):
            print(f"  {method}: {count} thuoc")
        
        # Thống kê field
        print("\nThong ke field:")
        has_group = sum(1 for d in final_drugs.values() if 'group' in d['keys'])
        has_vietnamese = sum(1 for d in final_drugs.values() if 'vietnamese_name' in d['keys'])
        has_admin = sum(1 for d in final_drugs.values() if 'administration' in d['keys'])
        has_indications = sum(1 for d in final_drugs.values() if 'indications' in d['keys'])
        has_dosage = sum(1 for d in final_drugs.values() if 'dosage' in d['keys'])
        
        total = len(final_drugs)
        print(f"  - group: {has_group} ({has_group*100//total if total > 0 else 0}%)")
        print(f"  - vietnamese_name: {has_vietnamese} ({has_vietnamese*100//total if total > 0 else 0}%)")
        print(f"  - administration: {has_admin} ({has_admin*100//total if total > 0 else 0}%)")
        print(f"  - indications: {has_indications} ({has_indications*100//total if total > 0 else 0}%)")
        print(f"  - dosage: {has_dosage} ({has_dosage*100//total if total > 0 else 0}%)")
        
        # Lưu danh sách
        with open('all_drugs_comprehensive.txt', 'w', encoding='utf-8') as f:
            f.write(f"# DANH SACH THUOC TIM THAY BANG NHIEU PHUONG PHAP\n")
            f.write(f"# Tong so: {len(final_drugs)}\n\n")
            for drug_name in sorted(final_drugs.keys()):
                data = final_drugs[drug_name]
                f.write(f"{drug_name} | {data['file']} | Methods: {', '.join(data['methods'])}\n")
        
        print(f"\nDa luu danh sach vao: all_drugs_comprehensive.txt")
        print("=" * 70)
        
        return final_drugs

def main():
    finder = ComprehensiveDrugFinder()
    print("Dang phan tich bang nhieu phuong phap...")
    finder.analyze_all_files()
    final_drugs = finder.print_statistics()
    
    print(f"\nKet qua: Tim thay {len(final_drugs)} thuoc")
    if len(final_drugs) < 666:
        print(f"Con thieu {666 - len(final_drugs)} thuoc. Can kiem tra them.")

if __name__ == "__main__":
    main()

