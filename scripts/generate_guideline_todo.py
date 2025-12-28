"""
Script tạo TODO list Markdown từ báo cáo guideline (JSON)

Sử dụng:
    python scripts/generate_guideline_todo.py
    python scripts/generate_guideline_todo.py --input reports/guideline_report_latest.json
"""

from pathlib import Path
from datetime import datetime
import json
from typing import Dict, List

DEFAULT_REPORT = Path("reports/guideline_report_latest.json")
OUTPUT_TODO = Path("reports/GUIDELINE_TODO.md")


def load_report(path: Path) -> Dict:
    """Đọc JSON report từ export_guideline_report.py"""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data


def classify_area(file_name: str, guidelines: List[Dict]) -> str:
    """Tạm phân loại chuyên khû theo guideline / tên file (thô nhưng đủ dùng cho TODO)."""
    name_lower = file_name.lower()
    gl_text = " ".join(g.get("name", "") for g in guidelines).upper()

    if any(k in gl_text for k in ["ESC", "ACC", "AHA", "HFSA", "EAS", "VAN TIM", "CORONARY"]):
        return "Tim mạch"
    if any(k in gl_text for k in ["GOLD", "GINA", "ARDS", "COPD", "ASTHMA"]):
        return "Hô hấp"
    if any(k in gl_text for k in ["KDIGO", "CKD", "AKI", "THẬN"]):
        return "Thận - Tiết niệu"
    if any(k in gl_text for k in ["ADA", "EASD", "ĐÁI THÁO ĐƯỜNG"]):
        return "Nội tiết - ĐTĐ"
    if any(k in gl_text for k in ["AHA/ASA", "ESO", "STROKE"]):
        return "Thần kinh"
    if any(k in gl_text for k in ["SSC", "SEPSIS", "IDSA", "ATS"]):
        return "Nhiễm khuẩn - Hồi sức"
    return "Khác"


def generate_todo(report: Dict) -> str:
    """Sinh nội dung Markdown TODO."""
    files = report.get("files", [])
    needs = [f for f in files if f.get("needs_check")]

    # Gom theo chuyên khoa thô
    groups: Dict[str, List[Dict]] = {}
    for item in needs:
        area = classify_area(item.get("file", ""), item.get("guidelines", []))
        groups.setdefault(area, []).append(item)

    lines: List[str] = []
    lines.append("# TODO cập nhật guideline\n")
    lines.append(f"**Ngày tạo:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}  ")
    lines.append(f"**Tổng số bài:** {report.get('total_files', 0)}  ")
    lines.append(f"**Cần kiểm tra:** {len(needs)}\n")

    for area in sorted(groups.keys()):
        items = groups[area]
        lines.append(f"## {area} ({len(items)} bài cần kiểm tra)\n")
        for item in sorted(items, key=lambda x: x.get("file", "")):
            file_name = item.get("file", "")
            path = item.get("path", "")
            gls = item.get("guidelines", [])
            reasons = item.get("reasons", [])

            # Hàng checklist
            lines.append(f"- [ ] **{file_name}**  ")
            lines.append(f"  - File: `{path}`")

            if gls:
                gl_text = ", ".join(f"{g.get('name', '').strip()} {g.get('year', '')}" for g in gls)
                lines.append(f"  - Guideline hiện tại: {gl_text}")
            if reasons:
                lines.append("  - Lý do cần kiểm tra:")
                for r in reasons:
                    lines.append(f"    - {r}")
            lines.append("")  # dòng trống

    if not needs:
        lines.append("✅ Hiện không có bài nào cần kiểm tra guideline.")

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Tạo TODO list Markdown từ báo cáo guideline (JSON)")
    parser.add_argument(
        "--input",
        type=str,
        help="Đường dẫn tới JSON report (mặc định: reports/guideline_report_latest.json)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="File TODO output (mặc định: reports/GUIDELINE_TODO.md)",
    )

    args = parser.parse_args()

    input_path = Path(args.input) if args.input else DEFAULT_REPORT
    if not input_path.exists():
        print(f"❌ Không tìm thấy report JSON: {input_path}")
        print("Trước tiên hãy chạy:")
        print("  python scripts/export_guideline_report.py --format json --output reports/guideline_report_latest.json")
        return

    report = load_report(input_path)
    todo_md = generate_todo(report)

    output_path = Path(args.output) if args.output else OUTPUT_TODO
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(todo_md, encoding="utf-8")

    print(f"✅ Đã tạo TODO: {output_path}")


if __name__ == "__main__":
    main()


