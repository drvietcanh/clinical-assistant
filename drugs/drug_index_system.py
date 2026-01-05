"""
Hệ thống index thuốc
Index tất cả thuốc theo tên, nhóm, chỉ định, module, field
Hỗ trợ tìm kiếm fuzzy và cache index
"""
import json
import pickle
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
from collections import defaultdict
import unicodedata
import re

try:
    from difflib import SequenceMatcher
    FUZZY_AVAILABLE = True
except ImportError:
    FUZZY_AVAILABLE = False

class DrugIndex:
    """Hệ thống index thuốc"""
    
    def __init__(self, cache_file: Optional[str] = None):
        """
        Khởi tạo index
        
        Args:
            cache_file: Đường dẫn file cache (nếu có)
        """
        self.drugs: Dict[str, Dict[str, Any]] = {}
        self.name_index: Dict[str, List[str]] = defaultdict(list)  # normalized_name -> [drug_names]
        self.group_index: Dict[str, Set[str]] = defaultdict(set)  # group -> {drug_names}
        self.indication_index: Dict[str, Set[str]] = defaultdict(set)  # indication -> {drug_names}
        self.module_index: Dict[str, Set[str]] = defaultdict(set)  # module -> {drug_names}
        self.field_index: Dict[str, Set[str]] = defaultdict(set)  # field -> {drug_names}
        self.cache_file = cache_file
        self._load_all_drugs()
        self._build_indexes()
    
    def _normalize_text(self, text: str) -> str:
        """Chuẩn hóa text để tìm kiếm (loại bỏ dấu, lowercase)"""
        if not text:
            return ""
        # Loại bỏ dấu
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        # Lowercase và loại bỏ khoảng trắng thừa
        text = text.lower().strip()
        return text
    
    def _extract_module_from_path(self, file_path: str) -> str:
        """Trích xuất module name từ file path"""
        parts = Path(file_path).parts
        if len(parts) >= 3 and parts[1] == 'drug_modules':
            return parts[2]  # drugs/drug_modules/MODULE_NAME/...
        return "unknown"
    
    def _load_all_drugs(self):
        """Load tất cả thuốc từ drug_database"""
        try:
            from drugs.drug_database import DRUG_DATABASE
            self.drugs = DRUG_DATABASE.copy()
        except ImportError:
            # Fallback: load từ modules trực tiếp
            try:
                from drugs.drug_modules import ALL_DRUGS
                self.drugs = ALL_DRUGS.copy()
            except ImportError:
                # Fallback: scan files manually
                self._load_drugs_from_files()
    
    def _load_drugs_from_files(self):
        """Load thuốc bằng cách scan files (fallback)"""
        import ast
        from drugs.drug_modules import __path__ as module_paths
        
        base_path = Path(module_paths[0])
        
        for py_file in sorted(base_path.rglob("*.py")):
            if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                tree = ast.parse(content)
                
                # Tìm _DRUGS assignments
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                                # Try to get the dict
                                if isinstance(node.value, ast.Dict):
                                    file_path = str(py_file.relative_to(base_path.parent.parent))
                                    for key_node, value_node in zip(node.value.keys, node.value.values):
                                        drug_name = self._get_string_value(key_node)
                                        if drug_name and isinstance(value_node, ast.Dict):
                                            # Extract basic info
                                            drug_info = {
                                                'name': drug_name,
                                                'file': file_path,
                                                'module': self._extract_module_from_path(file_path),
                                            }
                                            
                                            # Extract group, indications
                                            for k, v in zip(value_node.keys, value_node.values):
                                                field_name = self._get_string_value(k)
                                                if field_name == 'group':
                                                    drug_info['group'] = self._get_string_value(v)
                                                elif field_name == 'indications':
                                                    if isinstance(v, (ast.List, ast.Tuple)):
                                                        drug_info['indications'] = [
                                                            self._get_string_value(item) 
                                                            for item in v.elts
                                                            if self._get_string_value(item)
                                                        ]
                                            
                                            self.drugs[drug_name] = drug_info
            except Exception:
                continue
    
    def _get_string_value(self, node) -> Optional[str]:
        """Lấy giá trị string từ AST node"""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        elif hasattr(node, 's'):
            return node.s
        return None
    
    def _build_indexes(self):
        """Xây dựng tất cả indexes"""
        for drug_name, drug_info in self.drugs.items():
            # Index theo tên
            normalized_name = self._normalize_text(drug_name)
            self.name_index[normalized_name].append(drug_name)
            
            # Index theo group
            group = drug_info.get('group', '')
            if group:
                self.group_index[group].add(drug_name)
            
            # Index theo indications
            indications = drug_info.get('indications', [])
            if isinstance(indications, list):
                for indication in indications:
                    if indication:
                        normalized_ind = self._normalize_text(str(indication))
                        self.indication_index[normalized_ind].add(drug_name)
            
            # Index theo module
            module = drug_info.get('module', self._extract_module_from_path(drug_info.get('file', '')))
            if module:
                self.module_index[module].add(drug_name)
            
            # Index theo field (từ drug_info keys)
            for field in drug_info.keys():
                if field not in ['name', 'file', 'module']:
                    self.field_index[field].add(drug_name)
    
    def search(self, query: str, fuzzy: bool = True) -> List[str]:
        """
        Tìm kiếm thuốc theo tên
        
        Args:
            query: Từ khóa tìm kiếm
            fuzzy: Có dùng fuzzy search không
        
        Returns:
            Danh sách tên thuốc
        """
        query_normalized = self._normalize_text(query)
        results = set()
        
        # Exact match
        if query_normalized in self.name_index:
            results.update(self.name_index[query_normalized])
        
        # Partial match
        for normalized_name, drug_names in self.name_index.items():
            if query_normalized in normalized_name or normalized_name in query_normalized:
                results.update(drug_names)
        
        # Fuzzy match
        if fuzzy and FUZZY_AVAILABLE and len(results) < 10:
            for normalized_name, drug_names in self.name_index.items():
                similarity = SequenceMatcher(None, query_normalized, normalized_name).ratio()
                if similarity > 0.6:  # Threshold
                    results.update(drug_names)
        
        return list(results)
    
    def search_by_module(self, module: str) -> List[str]:
        """
        Tìm thuốc theo module
        
        Args:
            module: Tên module
        
        Returns:
            Danh sách tên thuốc
        """
        module_normalized = self._normalize_text(module)
        results = set()
        
        for mod_name, drug_names in self.module_index.items():
            if module_normalized in self._normalize_text(mod_name):
                results.update(drug_names)
        
        return list(results)
    
    def search_by_group(self, group: str) -> List[str]:
        """
        Tìm thuốc theo group
        
        Args:
            group: Tên group
        
        Returns:
            Danh sách tên thuốc
        """
        group_normalized = self._normalize_text(group)
        results = set()
        
        for grp_name, drug_names in self.group_index.items():
            if group_normalized in self._normalize_text(grp_name):
                results.update(drug_names)
        
        return list(results)
    
    def search_by_indication(self, indication: str) -> List[str]:
        """
        Tìm thuốc theo chỉ định
        
        Args:
            indication: Chỉ định
        
        Returns:
            Danh sách tên thuốc
        """
        indication_normalized = self._normalize_text(indication)
        results = set()
        
        for ind_name, drug_names in self.indication_index.items():
            if indication_normalized in ind_name or ind_name in indication_normalized:
                results.update(drug_names)
        
        return list(results)
    
    def search_by_field(self, field: str) -> List[str]:
        """
        Tìm thuốc có field cụ thể
        
        Args:
            field: Tên field
        
        Returns:
            Danh sách tên thuốc
        """
        field_normalized = self._normalize_text(field)
        results = set()
        
        for field_name, drug_names in self.field_index.items():
            if field_normalized in self._normalize_text(field_name):
                results.update(drug_names)
        
        return list(results)
    
    def get_drug_info(self, drug_name: str) -> Optional[Dict[str, Any]]:
        """
        Lấy thông tin chi tiết của một thuốc
        
        Args:
            drug_name: Tên thuốc
        
        Returns:
            Dict chứa thông tin thuốc hoặc None
        """
        return self.drugs.get(drug_name)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Lấy thống kê về index"""
        return {
            'total_drugs': len(self.drugs),
            'total_groups': len(self.group_index),
            'total_indications': len(self.indication_index),
            'total_modules': len(self.module_index),
            'total_fields': len(self.field_index),
            'modules': {mod: len(drugs) for mod, drugs in self.module_index.items()},
            'groups': {grp: len(drugs) for grp, drugs in self.group_index.items()},
        }
    
    def save_cache(self, file_path: Optional[str] = None):
        """Lưu index vào cache file"""
        cache_path = file_path or self.cache_file
        if not cache_path:
            return
        
        cache_data = {
            'drugs': self.drugs,
            'name_index': dict(self.name_index),
            'group_index': {k: list(v) for k, v in self.group_index.items()},
            'indication_index': {k: list(v) for k, v in self.indication_index.items()},
            'module_index': {k: list(v) for k, v in self.module_index.items()},
            'field_index': {k: list(v) for k, v in self.field_index.items()},
        }
        
        with open(cache_path, 'wb') as f:
            pickle.dump(cache_data, f)
    
    def load_cache(self, file_path: Optional[str] = None) -> bool:
        """Load index từ cache file"""
        cache_path = file_path or self.cache_file
        if not cache_path or not Path(cache_path).exists():
            return False
        
        try:
            with open(cache_path, 'rb') as f:
                cache_data = pickle.load(f)
            
            self.drugs = cache_data['drugs']
            self.name_index = defaultdict(list, cache_data['name_index'])
            self.group_index = {k: set(v) for k, v in cache_data['group_index'].items()}
            self.indication_index = {k: set(v) for k, v in cache_data['indication_index'].items()}
            self.module_index = {k: set(v) for k, v in cache_data['module_index'].items()}
            self.field_index = {k: set(v) for k, v in cache_data['field_index'].items()}
            
            return True
        except Exception:
            return False


# Convenience function
def get_drug_index(cache_file: Optional[str] = "drug_index_cache.pkl") -> DrugIndex:
    """
    Lấy hoặc tạo DrugIndex instance
    
    Args:
        cache_file: Đường dẫn file cache
    
    Returns:
        DrugIndex instance
    """
    index = DrugIndex(cache_file=cache_file)
    
    # Try to load from cache first
    if cache_file and index.load_cache():
        # Still rebuild to ensure freshness
        index._build_indexes()
    
    return index


if __name__ == "__main__":
    # Test
    index = get_drug_index()
    print(f"Loaded {len(index.drugs)} drugs")
    
    # Test search
    results = index.search("metformin")
    print(f"Search 'metformin': {results[:5]}")
    
    # Test by module
    results = index.search_by_module("diabetes")
    print(f"Drugs in diabetes module: {len(results)}")
    
    # Statistics
    stats = index.get_statistics()
    print(f"Statistics: {stats}")

