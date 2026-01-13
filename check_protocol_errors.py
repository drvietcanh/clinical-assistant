"""
Comprehensive Protocol Error Checker
Kiểm tra toàn diện các lỗi trong hệ thống Protocol
"""

import os
import ast
import importlib.util
import sys
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any, Optional
from collections import defaultdict
import traceback

# Colors for output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*80}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(80)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*80}{Colors.END}\n")

def print_success(text: str):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text: str):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text: str):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text: str):
    print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")


class ProtocolErrorChecker:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.protocols_path = self.base_path / "protocols"
        self.pages_path = self.base_path / "pages"
        self.config_path = self.base_path / "config"
        self.components_path = self.base_path / "components"
        
        self.errors = []
        self.warnings = []
        self.info = []
        
        # Load configs
        self.load_configs()
        
    def load_configs(self):
        """Load configuration files"""
        try:
            # Load protocol_routing
            routing_file = self.config_path / "protocol_routing.py"
            if routing_file.exists():
                spec = importlib.util.spec_from_file_location("protocol_routing", routing_file)
                routing_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(routing_module)
                self.PROTOCOL_ROUTING = routing_module.PROTOCOL_ROUTING
            else:
                self.PROTOCOL_ROUTING = {}
                self.errors.append(f"File not found: {routing_file}")
            
            # Load protocol_lists
            lists_file = self.config_path / "protocol_lists.py"
            if lists_file.exists():
                spec = importlib.util.spec_from_file_location("protocol_lists", lists_file)
                lists_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(lists_module)
                self.PROTOCOL_LISTS = lists_module.PROTOCOL_LISTS
                self.SPECIALTY_LIST = lists_module.SPECIALTY_LIST
            else:
                self.PROTOCOL_LISTS = {}
                self.SPECIALTY_LIST = []
                self.errors.append(f"File not found: {lists_file}")
                
        except Exception as e:
            self.errors.append(f"Error loading configs: {e}")
            self.PROTOCOL_ROUTING = {}
            self.PROTOCOL_LISTS = {}
            self.SPECIALTY_LIST = []
    
    def check_all(self):
        """Run all checks"""
        print_header("KIỂM TRA TOÀN DIỆN CÁC LỖI TRANG PROTOCOL")
        
        # 1. Routing consistency
        print_header("1. KIỂM TRA ROUTING CONSISTENCY")
        self.check_routing_consistency()
        
        # 2. Imports/Exports
        print_header("2. KIỂM TRA IMPORTS/EXPORTS")
        self.check_imports_exports()
        
        # 3. Function existence
        print_header("3. KIỂM TRA FUNCTION EXISTENCE")
        self.check_function_existence()
        
        # 4. Routing logic
        print_header("4. KIỂM TRA ROUTING LOGIC")
        self.check_routing_logic()
        
        # 5. Article links
        print_header("5. KIỂM TRA ARTICLE LINKS")
        self.check_article_links()
        
        # 6. Deep linking
        print_header("6. KIỂM TRA DEEP LINKING")
        self.check_deep_linking()
        
        # 7. Syntax errors
        print_header("7. KIỂM TRA SYNTAX ERRORS")
        self.check_syntax_errors()
        
        # 8. Runtime imports
        print_header("8. KIỂM TRA RUNTIME IMPORTS")
        self.check_runtime_imports()
        
        # 9. UI components
        print_header("9. KIỂM TRA UI COMPONENTS")
        self.check_ui_components()
        
        # 10. Generate report
        print_header("10. BÁO CÁO TỔNG KẾT")
        self.generate_error_report()
    
    def check_routing_consistency(self):
        """Check consistency between PROTOCOL_ROUTING and PROTOCOL_LISTS"""
        # Get all protocol names from PROTOCOL_LISTS
        all_protocols_in_lists = set()
        for specialty, protocols in self.PROTOCOL_LISTS.items():
            for protocol in protocols:
                # Remove emoji and clean name
                protocol_clean = protocol.split(' ', 1)[-1] if ' ' in protocol else protocol
                all_protocols_in_lists.add(protocol_clean.lower())
        
        # Get all keywords from PROTOCOL_ROUTING
        all_keywords_in_routing = set()
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            keywords = config.get("keywords", [])
            for kw in keywords:
                all_keywords_in_routing.add(kw.lower())
        
        # Check protocols in lists that don't match routing
        unmatched_protocols = []
        for protocol in all_protocols_in_lists:
            found = False
            for kw in all_keywords_in_routing:
                if kw in protocol or protocol in kw:
                    found = True
                    break
            if not found:
                unmatched_protocols.append(protocol)
        
        if unmatched_protocols:
            for protocol in unmatched_protocols:
                self.warnings.append(f"Protocol trong PROTOCOL_LISTS không có routing entry: {protocol}")
                print_warning(f"Protocol trong PROTOCOL_LISTS không có routing entry: {protocol}")
        else:
            print_success("Tất cả protocols trong PROTOCOL_LISTS đều có routing entry")
        
        # Check specialty consistency
        specialty_keys = set(self.PROTOCOL_LISTS.keys())
        specialty_list_clean = set()
        for spec in self.SPECIALTY_LIST:
            # Extract Vietnamese name (before parentheses), remove emoji
            spec_clean = spec.split('(')[0].strip()
            # Remove emoji characters (non-ASCII)
            spec_clean = ''.join(c for c in spec_clean if ord(c) < 128).strip()
            specialty_list_clean.add(spec_clean)
        
        missing_in_lists = specialty_list_clean - specialty_keys
        missing_in_specialty_list = specialty_keys - specialty_list_clean
        
        # These are warnings, not errors, as emoji difference is expected
        if missing_in_lists:
            for spec in missing_in_lists:
                self.warnings.append(f"Specialty trong SPECIALTY_LIST không có trong PROTOCOL_LISTS: {spec}")
                print_warning(f"Specialty trong SPECIALTY_LIST không có trong PROTOCOL_LISTS: {spec}")
        
        if missing_in_specialty_list:
            for spec in missing_in_specialty_list:
                self.warnings.append(f"Specialty trong PROTOCOL_LISTS không có trong SPECIALTY_LIST: {spec}")
                print_warning(f"Specialty trong PROTOCOL_LISTS không có trong SPECIALTY_LIST: {spec}")
    
    def check_imports_exports(self):
        """Check imports/exports consistency"""
        # Get exports from protocols/__init__.py
        init_file = self.protocols_path / "__init__.py"
        exports = set()
        
        if init_file.exists():
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        for alias in node.names:
                            exports.add(alias.name)
            except Exception as e:
                self.errors.append(f"Error parsing protocols/__init__.py: {e}")
                print_error(f"Error parsing protocols/__init__.py: {e}")
        else:
            self.errors.append("File not found: protocols/__init__.py")
            print_error("File not found: protocols/__init__.py")
        
        # Get imports from protocol_routing.py
        routing_file = self.config_path / "protocol_routing.py"
        imports = set()
        
        if routing_file.exists():
            with open(routing_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module and 'protocols' in node.module:
                            for alias in node.names:
                                imports.add(alias.name)
            except Exception as e:
                self.errors.append(f"Error parsing protocol_routing.py: {e}")
                print_error(f"Error parsing protocol_routing.py: {e}")
        
        # Get render functions from PROTOCOL_ROUTING by checking render_func.__name__
        routing_functions = set()
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            render_func = config.get("render")
            if render_func and hasattr(render_func, '__name__'):
                func_name = render_func.__name__
                # Skip generic "render" function name (false positive)
                if func_name != "render":
                    routing_functions.add(func_name)
        
        # Check missing exports
        missing_exports = routing_functions - exports
        if missing_exports:
            for func in missing_exports:
                self.errors.append(f"Render function không được export trong protocols/__init__.py: {func}")
                print_error(f"Render function không được export trong protocols/__init__.py: {func}")
        
        # Check missing imports
        missing_imports = routing_functions - imports
        if missing_imports:
            for func in missing_imports:
                self.errors.append(f"Render function không được import trong protocol_routing.py: {func}")
                print_error(f"Render function không được import trong protocol_routing.py: {func}")
        
        # Check unused exports - only warn if function name suggests it's a render function
        unused_exports = exports - routing_functions
        truly_unused = {f for f in unused_exports if f.startswith('render_')}
        if truly_unused:
            for func in sorted(truly_unused):
                self.warnings.append(f"Function được export nhưng không được sử dụng trong routing: {func}")
                print_warning(f"Function được export nhưng không được sử dụng trong routing: {func}")
        
        if not missing_exports and not missing_imports:
            print_success(f"Tất cả {len(routing_functions)} render functions đều được export và import đúng")
    
    def check_function_existence(self):
        """Check if render functions actually exist in protocol files"""
        missing_functions = []
        
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            render_func = config.get("render")
            if render_func:
                func_name = render_func.__name__ if hasattr(render_func, '__name__') else None
                
                if func_name:
                    # Try to find the function in protocol files
                    found = False
                    for py_file in self.protocols_path.rglob("*.py"):
                        if py_file.name == "__init__.py" or py_file.name == "TEMPLATE_PROTOCOL.py":
                            continue
                        
                        try:
                            with open(py_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                            
                            # Check if function is defined
                            pattern = rf'def\s+{re.escape(func_name)}\s*\('
                            if re.search(pattern, content):
                                found = True
                                break
                        except Exception as e:
                            pass
                    
                    if not found:
                        missing_functions.append(func_name)
                        self.errors.append(f"Render function không tồn tại trong protocol files: {func_name}")
                        print_error(f"Render function không tồn tại trong protocol files: {func_name}")
        
        if not missing_functions:
            print_success("Tất cả render functions đều tồn tại trong protocol files")
    
    def check_routing_logic(self):
        """Check routing logic for issues"""
        # Check priority conflicts
        priority_map = defaultdict(list)
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            priority = config.get("priority", 0)
            priority_map[priority].append(protocol_id)
        
        duplicate_priorities = {p: ids for p, ids in priority_map.items() if len(ids) > 1}
        if duplicate_priorities:
            for priority, ids in duplicate_priorities.items():
                self.warnings.append(f"Duplicate priority {priority} cho protocols: {', '.join(ids)}")
                print_warning(f"Duplicate priority {priority} cho protocols: {', '.join(ids)}")
        
        # Check keywords matching conflicts - only warn if same protocol appears twice (duplicate keywords)
        keyword_to_protocols = defaultdict(list)
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            keywords = config.get("keywords", [])
            for kw in keywords:
                keyword_to_protocols[kw.lower()].append(protocol_id)
        
        # Only warn about actual conflicts (different protocols with same keyword and same priority)
        for kw, ids in keyword_to_protocols.items():
            if len(set(ids)) > 1:  # Different protocols
                # Check if priorities resolve the conflict
                unique_protocols = list(set(ids))
                priorities = [self.PROTOCOL_ROUTING[pid].get("priority", 0) for pid in unique_protocols]
                if len(set(priorities)) < len(unique_protocols):
                    # Same priority for different protocols - potential conflict
                    self.warnings.append(f"Keyword '{kw}' match nhiều protocols khác nhau với cùng priority: {', '.join(unique_protocols)}")
                    print_warning(f"Keyword '{kw}' match nhiều protocols khác nhau với cùng priority: {', '.join(unique_protocols)}")
        
        # Check exclude_keywords logic
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            exclude_keywords = config.get("exclude_keywords", [])
            keywords = config.get("keywords", [])
            
            # Check if exclude keywords conflict with include keywords
            for excl_kw in exclude_keywords:
                for kw in keywords:
                    if excl_kw.lower() in kw.lower() or kw.lower() in excl_kw.lower():
                        self.warnings.append(f"Protocol {protocol_id}: exclude_keyword '{excl_kw}' conflict với keyword '{kw}'")
                        print_warning(f"Protocol {protocol_id}: exclude_keyword '{excl_kw}' conflict với keyword '{kw}'")
        
        # Check require_all flag usage
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            require_all = config.get("require_all", False)
            keywords = config.get("keywords", [])
            
            if require_all and len(keywords) < 2:
                self.warnings.append(f"Protocol {protocol_id}: require_all=True nhưng chỉ có {len(keywords)} keyword")
                print_warning(f"Protocol {protocol_id}: require_all=True nhưng chỉ có {len(keywords)} keyword")
        
        print_info(f"Đã kiểm tra routing logic cho {len(self.PROTOCOL_ROUTING)} protocols")
    
    def check_article_links(self):
        """Check article links configuration"""
        missing_article_functions = []
        invalid_article_functions = []
        
        for protocol_id, config in self.PROTOCOL_ROUTING.items():
            has_article = config.get("has_article", False)
            article_function = config.get("article_function")
            
            if has_article:
                if not article_function:
                    missing_article_functions.append(protocol_id)
                    self.errors.append(f"Protocol {protocol_id}: has_article=True nhưng không có article_function")
                    print_error(f"Protocol {protocol_id}: has_article=True nhưng không có article_function")
                else:
                    # Check if article function exists (would need to check articles module)
                    # For now, just check if it's a string
                    if not isinstance(article_function, str):
                        invalid_article_functions.append(protocol_id)
                        self.warnings.append(f"Protocol {protocol_id}: article_function không phải string: {article_function}")
                        print_warning(f"Protocol {protocol_id}: article_function không phải string: {article_function}")
        
        if not missing_article_functions and not invalid_article_functions:
            article_count = sum(1 for c in self.PROTOCOL_ROUTING.values() if c.get("has_article", False))
            print_success(f"Tất cả {article_count} protocols với has_article=True đều có article_function hợp lệ")
    
    def check_deep_linking(self):
        """Check deep linking logic"""
        main_page = self.pages_path / "04_📋_Protocols.py"
        sidebar_file = self.components_path / "protocols_sidebar.py"
        
        if not main_page.exists():
            self.errors.append("File not found: pages/04_📋_Protocols.py")
            print_error("File not found: pages/04_📋_Protocols.py")
            return
        
        if not sidebar_file.exists():
            self.errors.append("File not found: components/protocols_sidebar.py")
            print_error("File not found: components/protocols_sidebar.py")
            return
        
        # Check if session state is cleared
        with open(main_page, 'r', encoding='utf-8') as f:
            main_content = f.read()
        
        # Check for state clearing
        if 'protocol_deep_link_processed' in main_content:
            if 'del st.session_state' in main_content:
                print_success("Deep link state được clear đúng cách")
            else:
                self.warnings.append("Deep link state được set nhưng không được clear")
                print_warning("Deep link state được set nhưng không được clear")
        
        # Check sidebar deep link handling
        with open(sidebar_file, 'r', encoding='utf-8') as f:
            sidebar_content = f.read()
        
        if 'protocol_specialty' in sidebar_content and 'protocol_to_open' in sidebar_content:
            print_success("Sidebar có xử lý deep linking")
        else:
            self.warnings.append("Sidebar có thể không xử lý deep linking đầy đủ")
            print_warning("Sidebar có thể không xử lý deep linking đầy đủ")
    
    def check_syntax_errors(self):
        """Check for syntax errors in all protocol-related files"""
        syntax_errors = []
        
        files_to_check = [
            self.pages_path / "04_📋_Protocols.py",
            self.config_path / "protocol_routing.py",
            self.config_path / "protocol_lists.py",
            self.components_path / "protocols_sidebar.py",
            self.protocols_path / "__init__.py"
        ]
        
        # Add all protocol files
        for py_file in self.protocols_path.rglob("*.py"):
            if py_file.name != "__init__.py":
                files_to_check.append(py_file)
        
        for file_path in files_to_check:
            if not file_path.exists():
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                ast.parse(content)
            except SyntaxError as e:
                syntax_errors.append((str(file_path), str(e)))
                self.errors.append(f"Syntax error in {file_path}: {e}")
                print_error(f"Syntax error in {file_path}: {e}")
            except Exception as e:
                # Other errors (like encoding) are warnings
                self.warnings.append(f"Error checking {file_path}: {e}")
                print_warning(f"Error checking {file_path}: {e}")
        
        if not syntax_errors:
            print_success(f"Không có syntax errors trong {len(files_to_check)} files đã kiểm tra")
    
    def check_runtime_imports(self):
        """Check if modules can be imported"""
        import_errors = []
        
        # Try importing main modules
        modules_to_check = [
            ("config.protocol_routing", "PROTOCOL_ROUTING"),
            ("config.protocol_lists", "PROTOCOL_LISTS"),
            ("protocols", None),  # Just check if module imports
        ]
        
        for module_name, attr_name in modules_to_check:
            try:
                module = __import__(module_name, fromlist=[''])
                if attr_name:
                    if not hasattr(module, attr_name):
                        import_errors.append(f"Module {module_name} không có attribute {attr_name}")
                        self.errors.append(f"Module {module_name} không có attribute {attr_name}")
                        print_error(f"Module {module_name} không có attribute {attr_name}")
            except ImportError as e:
                import_errors.append(f"Cannot import {module_name}: {e}")
                self.errors.append(f"Cannot import {module_name}: {e}")
                print_error(f"Cannot import {module_name}: {e}")
            except Exception as e:
                import_errors.append(f"Error importing {module_name}: {e}")
                self.warnings.append(f"Error importing {module_name}: {e}")
                print_warning(f"Error importing {module_name}: {e}")
        
        if not import_errors:
            print_success("Tất cả modules đều có thể import được")
    
    def check_ui_components(self):
        """Check UI component integration"""
        main_page = self.pages_path / "04_📋_Protocols.py"
        
        if not main_page.exists():
            self.errors.append("File not found: pages/04_📋_Protocols.py")
            return
        
        with open(main_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check required imports
        required_components = [
            "render_protocols_sidebar",
            "render_protocol_by_name",
            "render_article_link",
            "render_calculator_links",
            "render_export_section",
            "render_related_protocols",
            "render_version_history"
        ]
        
        missing_imports = []
        for component in required_components:
            if component not in content:
                missing_imports.append(component)
                self.warnings.append(f"Component có thể không được import: {component}")
                print_warning(f"Component có thể không được import: {component}")
        
        # Check function calls
        if 'render_protocol_by_name' in content:
            # Check if functions are passed correctly
            if 'render_article_link' in content and 'render_score_links_from_protocol' in content:
                print_success("render_protocol_by_name được gọi với đúng parameters")
            else:
                self.warnings.append("render_protocol_by_name có thể không được gọi với đúng parameters")
                print_warning("render_protocol_by_name có thể không được gọi với đúng parameters")
        
        if not missing_imports:
            print_success("Tất cả required components đều được import")
    
    def generate_error_report(self):
        """Generate comprehensive error report"""
        print("\n" + "="*80)
        print(f"{Colors.BOLD}THỐNG KÊ TỔNG KẾT{Colors.END}")
        print("="*80)
        
        total_errors = len(self.errors)
        total_warnings = len(self.warnings)
        total_info = len(self.info)
        
        print(f"\n{Colors.BOLD}Tổng số lỗi:{Colors.END} {Colors.RED}{total_errors}{Colors.END}")
        print(f"{Colors.BOLD}Tổng số cảnh báo:{Colors.END} {Colors.YELLOW}{total_warnings}{Colors.END}")
        print(f"{Colors.BOLD}Tổng số thông tin:{Colors.END} {Colors.CYAN}{total_info}{Colors.END}")
        
        if self.errors:
            print(f"\n{Colors.BOLD}{Colors.RED}CÁC LỖI PHÁT HIỆN:{Colors.END}")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")
        
        if self.warnings:
            print(f"\n{Colors.BOLD}{Colors.YELLOW}CÁC CẢNH BÁO:{Colors.END}")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")
        
        # Calculate health score
        total_checks = total_errors + total_warnings
        if total_checks > 0:
            health_score = max(0, 100 - (total_errors * 10) - (total_warnings * 2))
        else:
            health_score = 100
        
        print(f"\n{Colors.BOLD}Health Score:{Colors.END} {health_score:.1f}%")
        
        if health_score >= 95:
            print(f"{Colors.GREEN}{Colors.BOLD}✅ EXCELLENT - Hệ thống protocols rất tốt!{Colors.END}")
        elif health_score >= 90:
            print(f"{Colors.GREEN}{Colors.BOLD}✅ VERY GOOD - Hệ thống protocols tốt!{Colors.END}")
        elif health_score >= 80:
            print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  GOOD - Có một số điểm cần cải thiện{Colors.END}")
        else:
            print(f"{Colors.RED}{Colors.BOLD}❌ NEEDS IMPROVEMENT - Cần sửa các vấn đề{Colors.END}")
        
        # Generate markdown report
        self.generate_markdown_report()
        
        print("\n" + "="*80)
    
    def generate_markdown_report(self):
        """Generate markdown report file"""
        report_file = self.base_path / "PROTOCOL_ERROR_REPORT.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# Báo Cáo Kiểm Tra Lỗi Trang Protocol\n\n")
            f.write(f"**Ngày tạo:** {Path(__file__).stat().st_mtime}\n\n")
            
            f.write("## Tổng Quan\n\n")
            f.write(f"- **Tổng số lỗi:** {len(self.errors)}\n")
            f.write(f"- **Tổng số cảnh báo:** {len(self.warnings)}\n")
            f.write(f"- **Tổng số protocols:** {len(self.PROTOCOL_ROUTING)}\n\n")
            
            if self.errors:
                f.write("## Các Lỗi Phát Hiện\n\n")
                for i, error in enumerate(self.errors, 1):
                    f.write(f"{i}. {error}\n")
                f.write("\n")
            
            if self.warnings:
                f.write("## Các Cảnh Báo\n\n")
                for i, warning in enumerate(self.warnings, 1):
                    f.write(f"{i}. {warning}\n")
                f.write("\n")
            
            f.write("## Đề Xuất Sửa Lỗi\n\n")
            f.write("1. Sửa các lỗi được liệt kê ở trên\n")
            f.write("2. Xem xét các cảnh báo và cải thiện nếu cần\n")
            f.write("3. Chạy lại script để xác nhận đã sửa\n\n")
        
        print_success(f"Đã tạo báo cáo: {report_file}")


if __name__ == "__main__":
    checker = ProtocolErrorChecker()
    checker.check_all()
