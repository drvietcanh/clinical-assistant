"""
Comprehensive Error Checker for Clinical Assistant App
Kiểm tra tự động: syntax errors, import errors, HTML structure, và các lỗi khác
"""

import ast
import importlib
import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime
from html.parser import HTMLParser
from collections import defaultdict


class HTMLValidator(HTMLParser):
    """HTML Parser để kiểm tra thẻ đóng/mở"""
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.self_closing_tags = {
            'img', 'br', 'hr', 'input', 'meta', 'link', 'area', 'base',
            'col', 'embed', 'source', 'track', 'wbr'
        }
    
    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.self_closing_tags:
            self.stack.append(tag.lower())
    
    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.self_closing_tags:
            return
        
        if not self.stack:
            self.errors.append(f"Thẻ đóng </{tag}> không có thẻ mở tương ứng")
            return
        
        if self.stack[-1] != tag_lower:
            # Tìm thẻ mở tương ứng
            if tag_lower in self.stack:
                idx = len(self.stack) - 1 - self.stack[::-1].index(tag_lower)
                missing_tags = self.stack[idx+1:]
                self.errors.append(
                    f"Thẻ đóng </{tag}> không khớp. "
                    f"Thiếu đóng các thẻ: {', '.join(f'</{t}>' for t in missing_tags)}"
                )
                self.stack = self.stack[:idx]
            else:
                self.errors.append(f"Thẻ đóng </{tag}> không có thẻ mở tương ứng")
        else:
            self.stack.pop()
    
    def check_complete(self):
        """Kiểm tra xem còn thẻ nào chưa đóng"""
        if self.stack:
            self.errors.append(
                f"Các thẻ chưa đóng: {', '.join(f'<{t}>' for t in self.stack)}"
            )
        return len(self.errors) == 0


class ErrorChecker:
    """Main error checker class"""
    
    def __init__(self, root_dir: Path):
        self.root_dir = Path(root_dir)
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.stats = {
            'files_checked': 0,
            'syntax_errors': 0,
            'import_errors': 0,
            'html_errors': 0,
            'total_errors': 0
        }
        
        # Directories to check
        self.check_dirs = ['pages', 'components', 'config', 'utils', 'drugs', 'scores', 'protocols']
        
    def find_python_files(self) -> List[Path]:
        """Tìm tất cả file Python cần kiểm tra"""
        python_files = []
        for dir_name in self.check_dirs:
            dir_path = self.root_dir / dir_name
            if dir_path.exists():
                python_files.extend(dir_path.rglob('*.py'))
        
        # Also check root level important files
        root_files = ['app.py']
        for file_name in root_files:
            file_path = self.root_dir / file_name
            if file_path.exists():
                python_files.append(file_path)
        
        return python_files
    
    def check_syntax(self, file_path: Path) -> List[str]:
        """Kiểm tra syntax errors"""
        errors = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            try:
                ast.parse(content, filename=str(file_path))
            except SyntaxError as e:
                errors.append(
                    f"Syntax error tại dòng {e.lineno}: {e.msg}\n"
                    f"  Text: {e.text.strip() if e.text else 'N/A'}"
                )
        except Exception as e:
            errors.append(f"Lỗi khi đọc file: {str(e)}")
        
        return errors
    
    def check_imports(self, file_path: Path) -> List[str]:
        """Kiểm tra import errors"""
        errors = []
        
        # Đọc file và tìm các import statements
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    try:
                        # Thử import module
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                module_name = alias.name.split('.')[0]
                                # Skip standard library và third-party
                                if not self._is_standard_lib(module_name):
                                    try:
                                        importlib.import_module(module_name)
                                    except ImportError:
                                        # Có thể là local module, kiểm tra xem file có tồn tại không
                                        if not self._module_exists(module_name, file_path):
                                            errors.append(
                                                f"Không thể import module '{module_name}' "
                                                f"(dòng {node.lineno})"
                                            )
                        elif isinstance(node, ast.ImportFrom):
                            module_name = node.module.split('.')[0] if node.module else ''
                            if module_name and not self._is_standard_lib(module_name):
                                if not self._module_exists(module_name, file_path):
                                    errors.append(
                                        f"Không thể import từ module '{node.module}' "
                                        f"(dòng {node.lineno})"
                                    )
                    except Exception as e:
                        errors.append(f"Lỗi khi kiểm tra import (dòng {node.lineno}): {str(e)}")
        except SyntaxError:
            # Syntax errors đã được báo ở check_syntax
            pass
        except Exception as e:
            errors.append(f"Lỗi khi kiểm tra imports: {str(e)}")
        
        return errors
    
    def _is_standard_lib(self, module_name: str) -> bool:
        """Kiểm tra xem module có phải standard library không"""
        standard_libs = {
            'os', 'sys', 'json', 're', 'pathlib', 'datetime', 'typing',
            'collections', 'functools', 'itertools', 'math', 'random',
            'string', 'io', 'csv', 'html', 'urllib', 'http', 'email',
            'base64', 'hashlib', 'uuid', 'time', 'calendar', 'locale',
            'ast', 'inspect', 'traceback', 'logging', 'warnings',
            'dataclasses', 'enum', 'abc', 'copy', 'pickle', 'sqlite3',
            'threading', 'multiprocessing', 'queue', 'subprocess',
            'socket', 'ssl', 'smtplib', 'xml', 'html', 'html.parser'
        }
        return module_name in standard_libs or module_name.startswith('_')
    
    def _module_exists(self, module_name: str, file_path: Path) -> bool:
        """Kiểm tra xem module có tồn tại trong project không"""
        # Tìm module trong các thư mục check_dirs
        for dir_name in self.check_dirs:
            # Thử tìm file module
            possible_paths = [
                self.root_dir / dir_name / f"{module_name}.py",
                self.root_dir / dir_name / module_name / "__init__.py",
            ]
            for path in possible_paths:
                if path.exists():
                    return True
        
        # Kiểm tra trong cùng thư mục với file hiện tại
        possible_paths = [
            file_path.parent / f"{module_name}.py",
            file_path.parent / module_name / "__init__.py",
        ]
        for path in possible_paths:
            if path.exists():
                return True
        
        return False
    
    def extract_html_strings(self, file_path: Path) -> List[Tuple[int, str]]:
        """Trích xuất các HTML strings từ file"""
        html_strings = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Tìm các pattern: st.markdown(..., unsafe_allow_html=True)
            # hoặc các f-string/f"""...""" chứa HTML tags
            html_pattern = re.compile(r'<[^>]+>')
            
            in_multiline_string = False
            multiline_start = 0
            current_string = []
            
            for i, line in enumerate(lines, 1):
                # Kiểm tra unsafe_allow_html
                if 'unsafe_allow_html' in line.lower():
                    # Tìm HTML string trước đó
                    for j in range(max(0, i-5), i):
                        if html_pattern.search(lines[j]):
                            html_strings.append((j+1, lines[j]))
                
                # Tìm HTML trong strings
                if html_pattern.search(line):
                    # Kiểm tra xem có phải string literal không
                    if '"""' in line or "'''" in line or 'f"""' in line or "f'''" in line:
                        in_multiline_string = True
                        multiline_start = i
                        current_string = [line]
                    elif in_multiline_string:
                        current_string.append(line)
                        if '"""' in line or "'''" in line:
                            html_strings.append((multiline_start, ''.join(current_string)))
                            in_multiline_string = False
                            current_string = []
                    else:
                        # Single line string với HTML
                        html_strings.append((i, line))
        
        except Exception as e:
            self.warnings[str(file_path)].append(f"Lỗi khi trích xuất HTML: {str(e)}")
        
        return html_strings
    
    def check_html_structure(self, file_path: Path) -> List[str]:
        """Kiểm tra cấu trúc HTML"""
        errors = []
        html_strings = self.extract_html_strings(file_path)
        
        for line_num, html_content in html_strings:
            # Trích xuất HTML từ string
            html_match = re.search(r'<[^>]+>.*?</[^>]+>', html_content, re.DOTALL)
            if not html_match:
                # Tìm HTML tags đơn lẻ
                html_match = re.search(r'<[^>]+>', html_content)
            
            if html_match:
                html_text = html_match.group(0)
                # Loại bỏ các thẻ script và style
                html_text = re.sub(r'<script[^>]*>.*?</script>', '', html_text, flags=re.DOTALL | re.IGNORECASE)
                html_text = re.sub(r'<style[^>]*>.*?</style>', '', html_text, flags=re.DOTALL | re.IGNORECASE)
                
                if html_text.strip():
                    validator = HTMLValidator()
                    try:
                        validator.feed(html_text)
                        validator.check_complete()
                        if validator.errors:
                            for error in validator.errors:
                                errors.append(f"Dòng {line_num}: {error}")
                    except Exception as e:
                        errors.append(f"Dòng {line_num}: Lỗi khi parse HTML: {str(e)}")
        
        return errors
    
    def check_file(self, file_path: Path):
        """Kiểm tra một file"""
        relative_path = file_path.relative_to(self.root_dir)
        self.stats['files_checked'] += 1
        
        # Check syntax
        syntax_errors = self.check_syntax(file_path)
        if syntax_errors:
            self.errors[str(relative_path)].extend([
                {'type': 'syntax', 'message': err} for err in syntax_errors
            ])
            self.stats['syntax_errors'] += len(syntax_errors)
        
        # Check imports (chỉ nếu không có syntax errors)
        if not syntax_errors:
            import_errors = self.check_imports(file_path)
            if import_errors:
                self.errors[str(relative_path)].extend([
                    {'type': 'import', 'message': err} for err in import_errors
                ])
                self.stats['import_errors'] += len(import_errors)
        
        # Check HTML
        html_errors = self.check_html_structure(file_path)
        if html_errors:
            self.errors[str(relative_path)].extend([
                {'type': 'html', 'message': err} for err in html_errors
            ])
            self.stats['html_errors'] += len(html_errors)
    
    def run(self):
        """Chạy kiểm tra trên tất cả files"""
        print("🔍 Bắt đầu kiểm tra lỗi toàn bộ app...")
        print(f"📁 Thư mục gốc: {self.root_dir}")
        print(f"📂 Thư mục kiểm tra: {', '.join(self.check_dirs)}")
        print("-" * 80)
        
        python_files = self.find_python_files()
        print(f"📄 Tìm thấy {len(python_files)} file Python để kiểm tra\n")
        
        for file_path in python_files:
            relative_path = file_path.relative_to(self.root_dir)
            print(f"✓ Đang kiểm tra: {relative_path}")
            self.check_file(file_path)
        
        self.stats['total_errors'] = sum(len(errs) for errs in self.errors.values())
        
        print("\n" + "=" * 80)
        print("📊 KẾT QUẢ KIỂM TRA")
        print("=" * 80)
        print(f"Files đã kiểm tra: {self.stats['files_checked']}")
        print(f"Lỗi syntax: {self.stats['syntax_errors']}")
        print(f"Lỗi import: {self.stats['import_errors']}")
        print(f"Lỗi HTML: {self.stats['html_errors']}")
        print(f"Tổng lỗi: {self.stats['total_errors']}")
        print("=" * 80)
    
    def generate_json_report(self, output_path: Path):
        """Generate JSON report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats,
            'errors': dict(self.errors),
            'warnings': dict(self.warnings)
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 JSON report đã lưu tại: {output_path}")
    
    def generate_html_report(self, output_path: Path):
        """Generate HTML report"""
        html_content = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo cáo kiểm tra lỗi - Clinical Assistant</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-value {{
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }}
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        .error-section {{
            margin: 30px 0;
        }}
        .file-errors {{
            background: #fff;
            border-left: 4px solid #e74c3c;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
        }}
        .file-name {{
            font-weight: bold;
            color: #e74c3c;
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        .error-item {{
            margin: 8px 0;
            padding: 8px;
            background: #fef5f5;
            border-radius: 4px;
        }}
        .error-type {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: bold;
            margin-right: 10px;
        }}
        .error-type.syntax {{
            background: #e74c3c;
            color: white;
        }}
        .error-type.import {{
            background: #f39c12;
            color: white;
        }}
        .error-type.html {{
            background: #9b59b6;
            color: white;
        }}
        .no-errors {{
            text-align: center;
            padding: 40px;
            color: #27ae60;
            font-size: 1.2em;
        }}
        .timestamp {{
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Báo cáo kiểm tra lỗi</h1>
        <div class="timestamp">Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-label">Files đã kiểm tra</div>
                <div class="stat-value">{self.stats['files_checked']}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Lỗi Syntax</div>
                <div class="stat-value">{self.stats['syntax_errors']}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Lỗi Import</div>
                <div class="stat-value">{self.stats['import_errors']}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Lỗi HTML</div>
                <div class="stat-value">{self.stats['html_errors']}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Tổng lỗi</div>
                <div class="stat-value">{self.stats['total_errors']}</div>
            </div>
        </div>
"""
        
        if self.errors:
            html_content += '<div class="error-section"><h2>📋 Chi tiết lỗi</h2>'
            for file_path, file_errors in sorted(self.errors.items()):
                html_content += f'''
                <div class="file-errors">
                    <div class="file-name">📄 {file_path}</div>
'''
                for error in file_errors:
                    error_type = error['type']
                    message = error['message'].replace('<', '&lt;').replace('>', '&gt;')
                    html_content += f'''
                    <div class="error-item">
                        <span class="error-type {error_type}">{error_type.upper()}</span>
                        <span>{message}</span>
                    </div>
'''
                html_content += '</div>'
            html_content += '</div>'
        else:
            html_content += '<div class="no-errors">✅ Không tìm thấy lỗi nào!</div>'
        
        html_content += '''
    </div>
</body>
</html>
'''
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"🌐 HTML report đã lưu tại: {output_path}")


def main():
    """Main function"""
    root_dir = Path(__file__).parent.parent
    checker = ErrorChecker(root_dir)
    
    checker.run()
    
    # Generate reports
    reports_dir = root_dir / 'reports'
    reports_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    json_report = reports_dir / f'error_report_{timestamp}.json'
    html_report = reports_dir / f'error_report_{timestamp}.html'
    
    checker.generate_json_report(json_report)
    checker.generate_html_report(html_report)
    
    # Exit code
    if checker.stats['total_errors'] > 0:
        print("\n⚠️  Tìm thấy lỗi! Vui lòng xem báo cáo chi tiết.")
        sys.exit(1)
    else:
        print("\n✅ Không tìm thấy lỗi!")
        sys.exit(0)


if __name__ == '__main__':
    main()
