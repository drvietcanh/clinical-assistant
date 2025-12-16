"""
Comprehensive Protocol Audit
Kiểm tra toàn diện tất cả các protocol: files, functions, imports, exports, routing, references, syntax
"""

import os
import ast
import importlib.util
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import traceback

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

class ComprehensiveProtocolAudit:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.protocols_path = self.base_path / "protocols"
        self.pages_path = self.base_path / "pages"
        self.issues = []
        self.warnings = []
        self.stats = {
            "total_protocols": 0,
            "protocols_checked": 0,
            "protocols_with_errors": 0,
            "protocols_with_warnings": 0,
            "syntax_errors": 0,
            "import_errors": 0,
            "missing_references": 0,
            "missing_routes": 0
        }
        
    def audit_all(self):
        """Run comprehensive audit"""
        print_header("KIỂM TRA TOÀN DIỆN TẤT CẢ CÁC PROTOCOL")
        
        # 1. Check all protocol files
        print_header("1. KIỂM TRA FILE PROTOCOL")
        protocol_files = self.check_all_protocol_files()
        
        # 2. Check syntax
        print_header("2. KIỂM TRA SYNTAX")
        syntax_results = self.check_syntax(protocol_files)
        
        # 3. Check imports/exports
        print_header("3. KIỂM TRA IMPORTS/EXPORTS")
        import_export_results = self.check_imports_exports()
        
        # 4. Check routing
        print_header("4. KIỂM TRA ROUTING")
        routing_results = self.check_routing_comprehensive()
        
        # 5. Check references
        print_header("5. KIỂM TRA REFERENCES")
        references_results = self.check_references_comprehensive()
        
        # 6. Check render functions
        print_header("6. KIỂM TRA RENDER FUNCTIONS")
        render_results = self.check_render_functions_comprehensive(protocol_files)
        
        # 7. Check interactive elements
        print_header("7. KIỂM TRA INTERACTIVE ELEMENTS")
        interactive_results = self.check_interactive_elements(protocol_files)
        
        # 8. Generate final report
        print_header("8. BÁO CÁO TỔNG KẾT")
        self.generate_comprehensive_report(
            protocol_files, syntax_results, import_export_results,
            routing_results, references_results, render_results, interactive_results
        )
        
    def check_all_protocol_files(self) -> Dict[str, Path]:
        """Check all protocol files exist"""
        protocol_files = {}
        
        # Get all Python files in protocols directory
        for py_file in self.protocols_path.rglob("*.py"):
            if py_file.name == "__init__.py" or py_file.name == "TEMPLATE_PROTOCOL.py":
                continue
            
            rel_path = py_file.relative_to(self.protocols_path)
            protocol_files[str(rel_path)] = py_file
            self.stats["total_protocols"] += 1
            print_success(f"Found: {rel_path}")
        
        return protocol_files
    
    def check_syntax(self, protocol_files: Dict[str, Path]) -> Dict[str, bool]:
        """Check syntax of all protocol files"""
        results = {}
        
        for rel_path, file_path in protocol_files.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Try to parse
                ast.parse(content)
                results[rel_path] = True
                print_success(f"Syntax OK: {rel_path}")
            except SyntaxError as e:
                results[rel_path] = False
                self.stats["syntax_errors"] += 1
                self.stats["protocols_with_errors"] += 1
                print_error(f"Syntax error in {rel_path}: {e}")
                self.issues.append(f"Syntax error in {rel_path}: {e}")
            except Exception as e:
                results[rel_path] = False
                self.stats["syntax_errors"] += 1
                print_warning(f"Error checking {rel_path}: {e}")
        
        return results
    
    def check_imports_exports(self) -> Dict[str, Any]:
        """Check imports and exports comprehensively"""
        results = {
            "exports": set(),
            "imports": set(),
            "missing_exports": [],
            "missing_imports": []
        }
        
        # Check main __init__.py
        main_init = self.protocols_path / "__init__.py"
        if main_init.exists():
            with open(main_init, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module and 'protocols' in node.module:
                            for alias in node.names:
                                results["exports"].add(alias.name)
            except Exception as e:
                print_error(f"Error parsing main __init__.py: {e}")
        
        # Check main page imports
        main_page = self.pages_path / "04_📋_Protocols.py"
        if main_page.exists():
            with open(main_page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module and 'protocols' in node.module:
                            for alias in node.names:
                                results["imports"].add(alias.name)
            except Exception as e:
                print_error(f"Error parsing main page: {e}")
        
        # Find missing
        missing_exports = results["imports"] - results["exports"]
        missing_imports = results["exports"] - results["imports"]
        
        if missing_exports:
            results["missing_exports"] = list(missing_exports)
            for func in missing_exports:
                print_warning(f"Imported but not exported: {func}")
        
        if missing_imports:
            results["missing_imports"] = list(missing_imports)
            for func in missing_imports:
                print_warning(f"Exported but not imported: {func}")
        
        print_info(f"Exports: {len(results['exports'])}, Imports: {len(results['imports'])}")
        
        return results
    
    def check_routing_comprehensive(self) -> Dict[str, Any]:
        """Check routing comprehensively"""
        results = {
            "routes_found": set(),
            "imports_found": set(),
            "missing_routes": []
        }
        
        main_page = self.pages_path / "04_📋_Protocols.py"
        if not main_page.exists():
            return results
        
        with open(main_page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all render_* function calls
        import re
        pattern = r'(\w+)\s*\(\)'
        matches = re.findall(pattern, content)
        render_calls = {m for m in matches if m.startswith('render_')}
        results["routes_found"] = render_calls
        
        # Find all imports
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    if node.module and 'protocols' in node.module:
                        for alias in node.names:
                            results["imports_found"].add(alias.name)
        except Exception as e:
            print_error(f"Error parsing routing: {e}")
        
        # Find missing routes
        missing = results["imports_found"] - results["routes_found"]
        if missing:
            results["missing_routes"] = list(missing)
            for func in missing:
                print_warning(f"Imported but not routed: {func}")
                self.stats["missing_routes"] += 1
        
        print_info(f"Routes: {len(results['routes_found'])}, Imports: {len(results['imports_found'])}")
        
        return results
    
    def check_references_comprehensive(self) -> Dict[str, Any]:
        """Check references comprehensively"""
        results = {
            "references_in_config": set(),
            "references_used": set(),
            "missing_references": []
        }
        
        # Check references_config.py
        ref_config = self.protocols_path / "references_config.py"
        if ref_config.exists():
            with open(ref_config, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all protocol names in PROTOCOL_REFERENCES
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Dict):
                        for key in node.keys:
                            if isinstance(key, ast.Constant):
                                results["references_in_config"].add(key.value)
            except Exception as e:
                print_error(f"Error parsing references_config: {e}")
        
        # Find all get_references() calls
        for py_file in self.protocols_path.rglob("*.py"):
            if py_file.name == "__init__.py" or py_file.name == "references_config.py":
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                import re
                pattern = r'get_references\(["\']([^"\']+)["\']\)'
                matches = re.findall(pattern, content)
                for match in matches:
                    results["references_used"].add(match)
            except Exception as e:
                pass
        
        # Check for missing (this is approximate)
        print_info(f"References in config: {len(results['references_in_config'])}, Used: {len(results['references_used'])}")
        
        return results
    
    def check_render_functions_comprehensive(self, protocol_files: Dict[str, Path]) -> Dict[str, Any]:
        """Check render functions comprehensively"""
        results = {
            "render_functions_found": set(),
            "files_with_render": []
        }
        
        for rel_path, file_path in protocol_files.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for render() function
                if 'def render(' in content:
                    results["files_with_render"].append(rel_path)
                    results["render_functions_found"].add("render")
                    
                    # Try to find the expected export name
                    # This is approximate - based on file path
                    if 'emergency' in rel_path:
                        module_name = Path(rel_path).stem
                        expected_name = f"render_{module_name}"
                        results["render_functions_found"].add(expected_name)
                
                self.stats["protocols_checked"] += 1
            except Exception as e:
                print_warning(f"Error checking {rel_path}: {e}")
        
        print_info(f"Files with render(): {len(results['files_with_render'])}")
        
        return results
    
    def check_interactive_elements(self, protocol_files: Dict[str, Path]) -> Dict[str, Any]:
        """Check for interactive elements"""
        results = {
            "calculators": 0,
            "radio_buttons": 0,
            "number_inputs": 0,
            "multiselect": 0,
            "tabs": 0
        }
        
        for rel_path, file_path in protocol_files.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Count interactive elements
                if 'st.number_input' in content:
                    results["number_inputs"] += content.count('st.number_input')
                if 'st.radio' in content:
                    results["radio_buttons"] += content.count('st.radio')
                if 'st.multiselect' in content:
                    results["multiselect"] += content.count('st.multiselect')
                if 'st.tabs' in content:
                    results["tabs"] += content.count('st.tabs')
                if 'calculator' in content.lower() or 'calculate' in content.lower():
                    results["calculators"] += 1
            except Exception as e:
                pass
        
        print_info(f"Interactive elements found: {results}")
        
        return results
    
    def generate_comprehensive_report(self, protocol_files, syntax_results, import_export_results,
                                     routing_results, references_results, render_results, interactive_results):
        """Generate comprehensive final report"""
        
        print("\n" + "="*80)
        print(f"{Colors.BOLD}THỐNG KÊ TỔNG KẾT{Colors.END}")
        print("="*80)
        
        print(f"\n{Colors.BOLD}Tổng số protocol files:{Colors.END} {self.stats['total_protocols']}")
        print(f"{Colors.BOLD}Protocols đã kiểm tra:{Colors.END} {self.stats['protocols_checked']}")
        print(f"{Colors.BOLD}Protocols có lỗi:{Colors.END} {self.stats['protocols_with_errors']}")
        print(f"{Colors.BOLD}Protocols có cảnh báo:{Colors.END} {self.stats['protocols_with_warnings']}")
        print(f"{Colors.BOLD}Lỗi syntax:{Colors.END} {self.stats['syntax_errors']}")
        print(f"{Colors.BOLD}Lỗi import:{Colors.END} {self.stats['import_errors']}")
        print(f"{Colors.BOLD}Thiếu routes:{Colors.END} {self.stats['missing_routes']}")
        print(f"{Colors.BOLD}Thiếu references:{Colors.END} {self.stats['missing_references']}")
        
        print(f"\n{Colors.BOLD}Exports:{Colors.END} {len(import_export_results['exports'])}")
        print(f"{Colors.BOLD}Imports:{Colors.END} {len(import_export_results['imports'])}")
        print(f"{Colors.BOLD}Routes:{Colors.END} {len(routing_results['routes_found'])}")
        print(f"{Colors.BOLD}References in config:{Colors.END} {len(references_results['references_in_config'])}")
        print(f"{Colors.BOLD}References used:{Colors.END} {len(references_results['references_used'])}")
        
        print(f"\n{Colors.BOLD}Interactive Elements:{Colors.END}")
        print(f"  - Calculators: {interactive_results['calculators']}")
        print(f"  - Radio buttons: {interactive_results['radio_buttons']}")
        print(f"  - Number inputs: {interactive_results['number_inputs']}")
        print(f"  - Multiselect: {interactive_results['multiselect']}")
        print(f"  - Tabs: {interactive_results['tabs']}")
        
        if self.issues:
            print(f"\n{Colors.BOLD}{Colors.RED}CÁC VẤN ĐỀ PHÁT HIỆN:{Colors.END}")
            for i, issue in enumerate(self.issues, 1):
                print(f"  {i}. {issue}")
        else:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ KHÔNG CÓ VẤN ĐỀ NGHIÊM TRỌNG!{Colors.END}")
        
        if import_export_results['missing_exports']:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  CẢNH BÁO:{Colors.END}")
            print(f"  - Imported but not exported: {len(import_export_results['missing_exports'])} functions")
        
        if import_export_results['missing_imports']:
            print(f"  - Exported but not imported: {len(import_export_results['missing_imports'])} functions")
        
        if routing_results['missing_routes']:
            print(f"  - Imported but not routed: {len(routing_results['missing_routes'])} functions")
        
        print("\n" + "="*80)
        
        # Calculate health score
        total_checks = (
            self.stats['total_protocols'] +
            len(import_export_results['exports']) +
            len(routing_results['routes_found']) +
            len(references_results['references_in_config'])
        )
        
        total_issues = (
            self.stats['syntax_errors'] +
            self.stats['import_errors'] +
            self.stats['missing_routes'] +
            self.stats['missing_references']
        )
        
        if total_checks > 0:
            health_score = ((total_checks - total_issues) / total_checks) * 100
            print(f"\n{Colors.BOLD}Health Score:{Colors.END} {health_score:.1f}%")
            
            if health_score >= 95:
                print(f"{Colors.GREEN}{Colors.BOLD}✅ EXCELLENT - Hệ thống protocols rất tốt!{Colors.END}")
            elif health_score >= 90:
                print(f"{Colors.GREEN}{Colors.BOLD}✅ VERY GOOD - Hệ thống protocols tốt!{Colors.END}")
            elif health_score >= 80:
                print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  GOOD - Có một số điểm cần cải thiện{Colors.END}")
            else:
                print(f"{Colors.RED}{Colors.BOLD}❌ NEEDS IMPROVEMENT - Cần sửa các vấn đề{Colors.END}")

if __name__ == "__main__":
    auditor = ComprehensiveProtocolAudit()
    auditor.audit_all()

