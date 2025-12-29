"""
Validator script: detect any HTML tags in drug data modules.

Mục tiêu:
- Cảnh báo (và trả về exit code != 0) nếu còn string chứa HTML tags trong
  `drugs/drug_modules`.

Cách dùng:
- Chỉ kiểm tra, KHÔNG tự động sửa.
- Có thể tích hợp vào pipeline kiểm tra hệ thống:

    python check_drug_html.py
"""

import ast
import re
from pathlib import Path
from typing import List, Tuple


HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")


class HtmlDetector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.issues: List[Tuple[int, str]] = []

    def visit_Constant(self, node: ast.Constant) -> None:
        if isinstance(node.value, str):
            s = node.value
            if "<" in s and ">" in s and HTML_TAG_RE.search(s):
                snippet = s.strip().replace("\n", " ")
                if len(snippet) > 80:
                    snippet = snippet[:77] + "..."
                self.issues.append((node.lineno or 0, snippet))
        self.generic_visit(node)


def check_file(path: Path) -> List[Tuple[int, str]]:
    try:
        source = path.read_text(encoding="utf-8")
    except Exception:
        return []

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    detector = HtmlDetector()
    detector.visit(tree)
    return detector.issues


def main() -> int:
    base = Path("drugs") / "drug_modules"
    if not base.exists():
        print("❌ Không tìm thấy thư mục drugs/drug_modules")
        return 1

    print("=== CHECK DRUG MODULES FOR EMBEDDED HTML ===\n")

    total_files = 0
    files_with_issues = 0

    for py_file in sorted(base.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        total_files += 1
        issues = check_file(py_file)
        if issues:
            files_with_issues += 1
            rel = py_file
            print(f"⚠️  {rel}:")
            for lineno, snippet in issues:
                print(f"   - Line {lineno}: {snippet}")
            print()

    print("=== SUMMARY ===")
    print(f"Total files scanned    : {total_files}")
    print(f"Files with HTML issues : {files_with_issues}")

    if files_with_issues > 0:
        print("\n❌ HTML tags detected in drug data. Vui lòng chạy sanitize_drug_html.py hoặc sửa tay.")
        return 1

    print("\n✅ No HTML tags detected in drug data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


