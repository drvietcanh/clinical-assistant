"""
Module Analyzer - Phân tích độ dài và đề xuất tách module
Tự động kiểm tra các file Python và đề xuất cách tách hợp lý
"""

import os
import ast
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class ModuleAnalysis:
    """Kết quả phân tích một module"""
    file_path: str
    lines: int
    code_lines: int  # Loại bỏ comments và blank lines
    classes: List[str]
    functions: List[str]
    imports: List[str]
    has_data_dict: bool
    data_dict_size: int  # Số keys trong dict lớn nhất (nếu có)
    suggestions: List[str]
    split_recommendation: Optional[str] = None


class ModuleAnalyzer:
    """Phân tích các module Python và đề xuất tách"""
    
    # Ngưỡng đề xuất tách module
    MAX_LINES_RECOMMENDED = 500
    MAX_LINES_CRITICAL = 800
    MAX_FUNCTIONS_RECOMMENDED = 20
    MAX_CLASSES_RECOMMENDED = 5
    
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.results: List[ModuleAnalysis] = []
        
    def analyze_file(self, file_path: Path) -> ModuleAnalysis:
        """Phân tích một file Python"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
            # Đếm dòng code thực (không tính comment và blank)
            code_lines = sum(1 for line in lines 
                           if line.strip() and not line.strip().startswith('#'))
            
            # Parse AST để tìm classes, functions
            classes = []
            functions = []
            try:
                tree = ast.parse(content)
                
                # Visitor để track context (có đang trong class không)
                class FunctionVisitor(ast.NodeVisitor):
                    def __init__(self):
                        self.classes = []
                        self.functions = []
                        self.in_class = False
                    
                    def visit_ClassDef(self, node):
                        self.classes.append(node.name)
                        old_in_class = self.in_class
                        self.in_class = True
                        self.generic_visit(node)
                        self.in_class = old_in_class
                    
                    def visit_FunctionDef(self, node):
                        if not self.in_class:
                            self.functions.append(node.name)
                        self.generic_visit(node)
                
                visitor = FunctionVisitor()
                visitor.visit(tree)
                classes = visitor.classes
                functions = visitor.functions
            except Exception:
                classes = []
                functions = []
            
            # Tìm imports
            imports = []
            for line in lines:
                if line.strip().startswith('import ') or line.strip().startswith('from '):
                    imports.append(line.strip())
            
            # Kiểm tra có data dictionary lớn không
            has_data_dict, data_dict_size = self._analyze_data_structure(content)
            
            # Tạo suggestions
            suggestions = self._generate_suggestions(
                file_path, len(lines), code_lines, len(classes), 
                len(functions), has_data_dict, data_dict_size
            )
            
            # Đề xuất cách tách
            split_recommendation = self._recommend_split(
                file_path, content, classes, functions, has_data_dict
            )
            
            return ModuleAnalysis(
                file_path=str(file_path.relative_to(self.root_dir)),
                lines=len(lines),
                code_lines=code_lines,
                classes=classes,
                functions=functions,
                imports=imports,
                has_data_dict=has_data_dict,
                data_dict_size=data_dict_size,
                suggestions=suggestions,
                split_recommendation=split_recommendation
            )
        except Exception as e:
            return ModuleAnalysis(
                file_path=str(file_path.relative_to(self.root_dir)),
                lines=0,
                code_lines=0,
                classes=[],
                functions=[],
                imports=[],
                has_data_dict=False,
                data_dict_size=0,
                suggestions=[f"Lỗi phân tích: {str(e)}"],
                split_recommendation=None
            )
    
    def _analyze_data_structure(self, content: str) -> Tuple[bool, int]:
        """Kiểm tra có dictionary data lớn không"""
        # Tìm các dictionary lớn (như DRUG_DATABASE, ANTIBIOTICS_DATABASE)
        # Đếm số keys bằng cách tìm pattern "Key": { ở đầu dòng
        key_matches = re.findall(r'^\s*"[^"]+":\s*\{', content, re.MULTILINE)
        max_size = len(key_matches)
        has_big_dict = max_size > 50
        
        # Cũng tìm các biến database lớn
        dict_patterns = [
            r'\w+_DATABASE\s*=\s*\{',
            r'\w+_DATA\s*=\s*\{',
            r'\w+_DDX\s*=\s*\{',
        ]
        
        for pattern in dict_patterns:
            if re.search(pattern, content):
                has_big_dict = True
                break
        
        return has_big_dict, max_size
    
    def _generate_suggestions(self, file_path: Path, lines: int, code_lines: int,
                             num_classes: int, num_functions: int,
                             has_data_dict: bool, data_dict_size: int) -> List[str]:
        """Tạo các gợi ý dựa trên phân tích"""
        suggestions = []
        
        if lines > self.MAX_LINES_CRITICAL:
            suggestions.append(f"⚠️  CRITICAL: File quá dài ({lines} dòng) - Nên tách ngay!")
        elif lines > self.MAX_LINES_RECOMMENDED:
            suggestions.append(f"⚠️  File dài ({lines} dòng) - Nên xem xét tách")
        
        if code_lines > self.MAX_LINES_RECOMMENDED * 0.8:
            suggestions.append(f"📝 Code thực tế: {code_lines} dòng (không tính comment)")
        
        if num_classes > self.MAX_CLASSES_RECOMMENDED:
            suggestions.append(f"🏗️  Nhiều classes ({num_classes}) - Có thể tách theo class")
        
        if num_functions > self.MAX_FUNCTIONS_RECOMMENDED:
            suggestions.append(f"⚙️  Nhiều functions ({num_functions}) - Có thể nhóm theo chức năng")
        
        if has_data_dict and data_dict_size > 50:
            suggestions.append(f"📊 Có data dictionary lớn (~{data_dict_size} entries) - Nên tách data ra file riêng")
        
        if lines > 1000 and has_data_dict:
            suggestions.append("💡 Đề xuất: Tách data dictionary ra file riêng (.data.py)")
        
        return suggestions
    
    def _recommend_split(self, file_path: Path, content: str, 
                        classes: List[str], functions: List[str],
                        has_data_dict: bool) -> Optional[str]:
        """Đề xuất cách tách module cụ thể"""
        file_name = file_path.stem
        parent_dir = file_path.parent
        
        # Pattern 1: File có data dictionary lớn
        if has_data_dict and 'database' in file_name.lower():
            # Tách data ra file riêng
            data_file = parent_dir / f"{file_name}_data.py"
            logic_file = file_path
            return (
                f"📦 TÁCH DATA:\n"
                f"  1. Tạo {data_file.name} - Chứa data dictionary\n"
                f"  2. Giữ {file_path.name} - Chứa logic và functions\n"
                f"  3. Import từ {data_file.name} vào {file_path.name}"
            )
        
        # Pattern 2: File có nhiều classes
        if len(classes) > 3:
            return (
                f"🏗️  TÁCH THEO CLASS:\n"
                f"  - Tạo thư mục {file_name}/\n"
                f"  - Mỗi class → file riêng: {file_name}/class_name.py\n"
                f"  - Tạo {file_name}/__init__.py để export"
            )
        
        # Pattern 3: File có nhiều functions có thể nhóm
        if len(functions) > 15:
            # Phân tích tên function để nhóm
            groups = defaultdict(list)
            for func in functions:
                prefix = func.split('_')[0] if '_' in func else func
                groups[prefix].append(func)
            
            if len(groups) > 1:
                group_names = ', '.join(groups.keys()[:3])
                return (
                    f"⚙️  TÁCH THEO CHỨC NĂNG:\n"
                    f"  - Phân tích thấy {len(groups)} nhóm functions\n"
                    f"  - Có thể tách theo prefix: {group_names}...\n"
                    f"  - Ví dụ: {file_name}_utils.py, {file_name}_calculators.py"
                )
        
        # Pattern 4: File rất dài nhưng không có cấu trúc rõ ràng
        lines_count = len(content.split('\n'))
        if lines_count > 1000:
            return (
                f"📄 TÁCH THEO SECTION:\n"
                f"  - File quá dài ({lines_count} dòng)\n"
                f"  - Tìm các comment section (# ==========)\n"
                f"  - Tách mỗi section thành file riêng\n"
                f"  - Tạo {file_name}/ và chia nhỏ"
            )
        
        return None
    
    def analyze_all(self, exclude_patterns: List[str] = None) -> List[ModuleAnalysis]:
        """Phân tích tất cả file Python trong project"""
        if exclude_patterns is None:
            exclude_patterns = ['__pycache__', '.pyc', 'venv', 'env', '.git']
        
        results = []
        
        for py_file in self.root_dir.rglob('*.py'):
            # Bỏ qua các file trong exclude_patterns
            if any(pattern in str(py_file) for pattern in exclude_patterns):
                continue
            
            analysis = self.analyze_file(py_file)
            results.append(analysis)
        
        # Sắp xếp theo số dòng giảm dần
        results.sort(key=lambda x: x.lines, reverse=True)
        self.results = results
        return results
    
    def generate_report(self, output_file: str = "module_analysis_report.md") -> str:
        """Tạo báo cáo dạng Markdown"""
        if not self.results:
            return "Không có kết quả phân tích"
        
        report = []
        report.append("# BÁO CÁO PHÂN TÍCH MODULE\n")
        report.append(f"**Ngày tạo:** {Path.cwd()}\n")
        report.append(f"**Tổng số file:** {len(self.results)}\n\n")
        
        # Tóm tắt
        report.append("## 📊 TÓM TẮT\n\n")
        critical = [r for r in self.results if r.lines > self.MAX_LINES_CRITICAL]
        recommended = [r for r in self.results 
                      if self.MAX_LINES_RECOMMENDED < r.lines <= self.MAX_LINES_CRITICAL]
        
        report.append(f"- ⚠️  **CRITICAL** (> {self.MAX_LINES_CRITICAL} dòng): {len(critical)} files\n")
        report.append(f"- ⚠️  **Recommended** (> {self.MAX_LINES_RECOMMENDED} dòng): {len(recommended)} files\n")
        report.append(f"- ✅ **OK**: {len(self.results) - len(critical) - len(recommended)} files\n\n")
        
        # Chi tiết các file cần tách
        report.append("## 🔴 CẦN TÁCH NGAY (CRITICAL)\n\n")
        if critical:
            for r in critical:
                report.append(f"### {r.file_path}\n")
                report.append(f"- **Dòng:** {r.lines} (code: {r.code_lines})\n")
                report.append(f"- **Classes:** {len(r.classes)}\n")
                report.append(f"- **Functions:** {len(r.functions)}\n")
                if r.has_data_dict:
                    report.append(f"- **Data dict:** Có (~{r.data_dict_size} entries)\n")
                report.append(f"- **Gợi ý:**\n")
                for suggestion in r.suggestions:
                    report.append(f"  - {suggestion}\n")
                if r.split_recommendation:
                    report.append(f"\n**💡 Đề xuất tách:**\n```\n{r.split_recommendation}\n```\n")
                report.append("\n")
        else:
            report.append("Không có file nào cần tách ngay.\n\n")
        
        # Các file nên xem xét
        report.append("## 🟡 NÊN XEM XÉT TÁCH\n\n")
        if recommended:
            for r in recommended:
                report.append(f"### {r.file_path} ({r.lines} dòng)\n")
                for suggestion in r.suggestions:
                    report.append(f"- {suggestion}\n")
                if r.split_recommendation:
                    report.append(f"\n**💡 Đề xuất:**\n```\n{r.split_recommendation}\n```\n")
                report.append("\n")
        else:
            report.append("Không có file nào cần xem xét.\n\n")
        
        # Bảng tổng hợp top files
        report.append("## 📋 TOP 20 FILE DÀI NHẤT\n\n")
        report.append("| File | Dòng | Code | Classes | Functions | Data Dict |\n")
        report.append("|------|------|------|---------|-----------|-----------|\n")
        
        for r in self.results[:20]:
            data_info = f"✅ (~{r.data_dict_size})" if r.has_data_dict else "❌"
            report.append(
                f"| {r.file_path} | {r.lines} | {r.code_lines} | "
                f"{len(r.classes)} | {len(r.functions)} | {data_info} |\n"
            )
        
        # Lưu file
        report_text = ''.join(report)
        output_path = self.root_dir / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        return report_text


def main():
    """Chạy phân tích"""
    analyzer = ModuleAnalyzer(".")
    print("🔍 Đang phân tích các module...")
    results = analyzer.analyze_all()
    
    print(f"\n✅ Đã phân tích {len(results)} files\n")
    
    # In top 10
    print("📊 TOP 10 FILE DÀI NHẤT:")
    print("-" * 80)
    for i, r in enumerate(results[:10], 1):
        status = "🔴 CRITICAL" if r.lines > 800 else "🟡 WARNING" if r.lines > 500 else "✅ OK"
        print(f"{i:2}. {status} | {r.lines:5} dòng | {r.file_path}")
    
    # Tạo report
    print("\n📝 Đang tạo báo cáo...")
    report = analyzer.generate_report()
    print("✅ Đã tạo file: module_analysis_report.md")
    
    return analyzer


if __name__ == "__main__":
    main()

