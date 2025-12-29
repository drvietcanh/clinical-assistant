"""
Utility script to scan all drug modules and strip any embedded HTML tags
from text fields.

Mục tiêu:
- Loại bỏ các tag HTML (ví dụ: <div>, <span>, <strong> ...) khỏi dữ liệu thuốc
  trong thư mục `drugs/drug_modules`.
- Giữ nguyên nội dung chữ, chỉ bỏ phần markup.

Cách hoạt động:
- Duyệt toàn bộ file .py trong `drugs/drug_modules`.
- Parse AST và tìm tất cả hằng số dạng string.
- Nếu string có chứa dấu `<` và `>`, script sẽ strip tag bằng regex
  r"<[^>]+>" và giữ lại phần text.
- Ghi đè lại source bằng AST unparse, đồng thời lưu file backup `.backup`.

⚠️ Lưu ý:
- Script cố gắng an toàn, nhưng vẫn nên commit code hiện tại trước khi chạy
  để có thể rollback dễ dàng.
- Chỉ nên chạy khi bạn chắc chắn `drugs/drug_modules` chỉ chứa data (dict)
  chứ không chứa code UI HTML đặc biệt cần giữ nguyên.
"""

import ast
import re
from pathlib import Path
from typing import Tuple


HTML_TAG_RE = re.compile(r"<[^>]+>")


class HtmlStripper(ast.NodeTransformer):
    """AST transformer: strip HTML tags from all string constants."""

    def __init__(self) -> None:
        super().__init__()
        self.changed = False

    def _strip_html(self, s: str) -> Tuple[str, bool]:
        if "<" not in s or ">" not in s:
            return s, False
        # Only treat as HTML if it looks like a tag, not e.g. math comparison
        if not re.search(r"</?[a-zA-Z][^>]*>", s):
            return s, False
        clean = HTML_TAG_RE.sub("", s)
        clean_stripped = clean.strip()
        if clean_stripped != s:
            return clean_stripped, True
        return s, False

    def visit_Constant(self, node: ast.Constant) -> ast.AST:
        if isinstance(node.value, str):
            new_val, changed = self._strip_html(node.value)
            if changed:
                self.changed = True
                return ast.copy_location(ast.Constant(value=new_val), node)
        return node


def process_file(path: Path) -> bool:
    """Strip HTML from one file. Returns True if file was modified."""
    try:
        source = path.read_text(encoding="utf-8")
    except Exception:
        return False

    try:
        tree = ast.parse(source)
    except SyntaxError:
        # Skip files with syntax errors
        return False

    stripper = HtmlStripper()
    new_tree = stripper.visit(tree)
    if not stripper.changed:
        return False

    ast.fix_missing_locations(new_tree)

    try:
        new_source = ast.unparse(new_tree)  # type: ignore[attr-defined]
    except Exception:
        # Fallback: không sửa nếu unparse thất bại
        return False

    # Tạo backup
    backup_path = path.with_suffix(path.suffix + ".backup")
    backup_path.write_text(source, encoding="utf-8")

    # Ghi file mới
    path.write_text(new_source + "\n", encoding="utf-8")
    return True


def main() -> None:
    base = Path("drugs") / "drug_modules"
    if not base.exists():
        print("❌ Không tìm thấy thư mục drugs/drug_modules")
        return

    total_files = 0
    changed_files = 0

    print("=== STRIP HTML TAGS FROM DRUG MODULES ===\n")
    for py_file in sorted(base.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        total_files += 1
        modified = process_file(py_file)
        status = "CLEAN" if not modified else "FIXED"
        if modified:
            changed_files += 1
        print(f"[{status}] {py_file}")

    print("\n=== SUMMARY ===")
    print(f"Total files scanned : {total_files}")
    print(f"Files modified      : {changed_files}")
    print("Backup of modified files saved with '.backup' extension.")


if __name__ == "__main__":
    main()


