"""
Script kiểm tra format của các file markdown article

Kiểm tra:
- Có frontmatter đúng format không
- Có header với thông tin cập nhật không
- Có tài liệu tham khảo không
- Có guideline được ghi rõ không

Sử dụng:
    python scripts/validate_article_format.py
    python scripts/validate_article_format.py --fix  # Tự động sửa một số lỗi
"""

import re
from pathlib import Path
from typing import Dict, List
from datetime import datetime

ARTICLES_DIR = Path("content/articles")

def validate_file(file_path: Path) -> Dict:
    """Kiểm tra format của một file"""
    content = file_path.read_text(encoding='utf-8')
    
    issues = []
    warnings = []
    
    # Kiểm tra frontmatter
    if not content.startswith('---'):
        warnings.append("Không có frontmatter (bắt đầu bằng ---)")
    else:
        frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            if 'last_reviewed:' not in frontmatter:
                warnings.append("Thiếu 'last_reviewed' trong frontmatter")
        else:
            issues.append("Frontmatter không đúng format")
    
    # Kiểm tra header với thông tin cập nhật
    if '**Cập nhật:**' not in content and 'last_reviewed:' not in content:
        warnings.append("Không có thông tin ngày cập nhật")
    
    # Kiểm tra có tài liệu tham khảo
    if '**Tài liệu tham khảo' not in content and 'tài liệu tham khảo' not in content:
        warnings.append("Không có section tài liệu tham khảo")
    
    # Kiểm tra có guideline
    guideline_patterns = [
        r'\b(ESC|ACC/AHA|ADA|KDIGO|GOLD|GINA|ATS|IDSA|AHA/ASA|ACR|EULAR|SSC|EASL|AASLD)\b',
    ]
    has_guideline = any(re.search(pattern, content, re.IGNORECASE) for pattern in guideline_patterns)
    if not has_guideline:
        warnings.append("Không tìm thấy guideline nào được đề cập")
    
    # Kiểm tra có năm trong guideline
    if has_guideline:
        year_pattern = r'\b(20\d{2})\b'
        years = re.findall(year_pattern, content[:2000])  # Chỉ check 2000 ký tự đầu
        if not years:
            warnings.append("Có guideline nhưng không thấy năm")
    
    return {
        "file": file_path.name,
        "path": str(file_path),
        "issues": issues,
        "warnings": warnings,
        "is_valid": len(issues) == 0,
        "has_warnings": len(warnings) > 0
    }

def validate_all():
    """Kiểm tra tất cả file"""
    results = []
    
    md_files = list(ARTICLES_DIR.glob("*.md"))
    print(f"Đang kiểm tra {len(md_files)} file...\n")
    
    for file_path in sorted(md_files):
        try:
            result = validate_file(file_path)
            results.append(result)
        except Exception as e:
            results.append({
                "file": file_path.name,
                "path": str(file_path),
                "error": str(e),
                "is_valid": False
            })
    
    return results

def print_report(results: List[Dict]):
    """In báo cáo"""
    valid = [r for r in results if r.get("is_valid") and not r.get("error")]
    invalid = [r for r in results if not r.get("is_valid") and not r.get("error")]
    errors = [r for r in results if "error" in r]
    with_warnings = [r for r in results if r.get("has_warnings") and r.get("is_valid")]
    
    print("=" * 60)
    print("BÁO CÁO KIỂM TRA FORMAT")
    print("=" * 60)
    print()
    print(f"📊 Tổng quan:")
    print(f"   - Tổng số file: {len(results)}")
    print(f"   - File hợp lệ: {len(valid)} ({len(valid)/len(results)*100:.1f}%)")
    print(f"   - File có vấn đề: {len(invalid)} ({len(invalid)/len(results)*100:.1f}%)")
    print(f"   - File có cảnh báo: {len(with_warnings)} ({len(with_warnings)/len(results)*100:.1f}%)")
    print(f"   - Lỗi khi đọc: {len(errors)}")
    print()
    
    if invalid:
        print("❌ Files có vấn đề:")
        for result in invalid[:20]:  # Limit 20
            print(f"\n  📄 {result['file']}")
            for issue in result.get("issues", []):
                print(f"     - {issue}")
        if len(invalid) > 20:
            print(f"\n  ... và {len(invalid) - 20} file khác")
        print()
    
    if with_warnings:
        print("⚠️  Files có cảnh báo (top 20):")
        for result in with_warnings[:20]:
            print(f"\n  📄 {result['file']}")
            for warning in result.get("warnings", [])[:3]:  # Limit 3 warnings
                print(f"     - {warning}")
        if len(with_warnings) > 20:
            print(f"\n  ... và {len(with_warnings) - 20} file khác")
        print()
    
    if errors:
        print("❌ Lỗi khi đọc file:")
        for result in errors:
            print(f"  - {result['file']}: {result['error']}")
        print()

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Kiểm tra format các file markdown article")
    parser.add_argument(
        "--output",
        type=str,
        help="Xuất báo cáo ra file JSON"
    )
    
    args = parser.parse_args()
    
    results = validate_all()
    print_report(results)
    
    if args.output:
        import json
        output_path = Path(args.output)
        output_path.write_text(
            json.dumps(results, indent=2, ensure_ascii=False),
            encoding='utf-8'
        )
        print(f"✅ Đã xuất báo cáo: {output_path}")

if __name__ == "__main__":
    main()

