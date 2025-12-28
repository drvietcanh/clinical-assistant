"""
Script tự động kiểm tra và cập nhật guideline trong các bài viết y khoa

Chức năng:
1. Quét tất cả các file markdown trong content/articles
2. Trích xuất thông tin guideline từ metadata và nội dung
3. Kiểm tra năm guideline và tạo báo cáo
4. Tự động cập nhật ngày "last_reviewed" hoặc "Cập nhật"
5. Tạo báo cáo về các file cần kiểm tra guideline mới

Sử dụng:
    python scripts/check_guideline_updates.py [--update-dates] [--report-only]
"""

import re
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json

# Đường dẫn tới thư mục bài viết
ARTICLES_DIR = Path("content/articles")
REPORT_DIR = Path("reports")

# Mapping các guideline chính và chu kỳ cập nhật thông thường (năm)
GUIDELINE_CYCLE = {
    "ESC": 3,  # ESC thường cập nhật mỗi 3-5 năm
    "ACC/AHA": 3,
    "ADA": 1,  # ADA cập nhật hàng năm
    "EASD": 1,
    "KDIGO": 3,
    "GOLD": 1,  # GOLD cập nhật hàng năm
    "GINA": 1,  # GINA cập nhật hàng năm
    "ATS": 5,
    "IDSA": 5,
    "AHA/ASA": 3,
    "ESO": 3,
    "ACR": 3,
    "EULAR": 3,
    "SSC": 3,
    "EASL": 3,
    "AASLD": 3,
}

# Năm hiện tại để so sánh
CURRENT_YEAR = datetime.now().year


class GuidelineChecker:
    """Class để kiểm tra và cập nhật guideline"""
    
    def __init__(self, articles_dir: Path):
        self.articles_dir = articles_dir
        self.results = []
        
    def extract_guideline_info(self, file_path: Path) -> Dict:
        """Trích xuất thông tin guideline từ file markdown"""
        content = file_path.read_text(encoding='utf-8')
        
        info = {
            "file": str(file_path.name),
            "path": str(file_path),
            "guidelines": [],
            "last_reviewed": None,
            "update_date": None,
            "needs_check": False,
        }
        
        # Trích xuất năm từ metadata (nếu có frontmatter)
        frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # Tìm last_reviewed
            last_reviewed_match = re.search(r'last_reviewed:\s*(\d{4}-\d{2})', frontmatter)
            if last_reviewed_match:
                info["last_reviewed"] = last_reviewed_match.group(1)
            
            # Tìm guideline_version
            guideline_match = re.search(r'guideline_version:\s*\n((?:\s*-.*?\n)+)', frontmatter)
            if guideline_match:
                guidelines_text = guideline_match.group(1)
                info["guidelines"] = self._parse_guideline_list(guidelines_text)
        
        # Trích xuất từ header (format: > **Cập nhật:** ...)
        update_match = re.search(r'\*\*Cập nhật:\*\*\s*Tháng\s+(\d{1,2})/(\d{4})', content)
        if update_match:
            month, year = update_match.groups()
            info["update_date"] = f"{year}-{month.zfill(2)}"
        
        # Trích xuất guideline từ tài liệu tham khảo
        ref_match = re.search(r'\*\*Tài liệu tham khảo chính:\*\*\s*(.*?)(?:---|$)', content, re.DOTALL)
        if ref_match:
            ref_text = ref_match.group(1)
            guidelines_from_ref = self._extract_guidelines_from_text(ref_text)
            if guidelines_from_ref:
                # Merge với guidelines từ metadata (tránh trùng)
                existing_names = {g["name"] for g in info["guidelines"]}
                for g in guidelines_from_ref:
                    if g["name"] not in existing_names:
                        info["guidelines"].append(g)
        
        # Nếu không có guideline từ metadata, trích xuất từ nội dung
        if not info["guidelines"]:
            guidelines_from_content = self._extract_guidelines_from_text(content[:2000])  # Chỉ check 2000 ký tự đầu
            info["guidelines"] = guidelines_from_content
        
        return info
    
    def _parse_guideline_list(self, text: str) -> List[Dict]:
        """Parse danh sách guideline từ metadata"""
        guidelines = []
        lines = text.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('-'):
                guideline_text = line[1:].strip()
                guideline_info = self._parse_single_guideline(guideline_text)
                if guideline_info:
                    guidelines.append(guideline_info)
        return guidelines
    
    def _parse_single_guideline(self, text: str) -> Optional[Dict]:
        """Parse một guideline từ text"""
        # Pattern: "ESC HF Guidelines 2021" hoặc "KDIGO 2024"
        pattern = r'([A-Z/]+(?: [A-Z]+)?)\s+.*?(\d{4})'
        match = re.search(pattern, text)
        if match:
            name = match.group(1).strip()
            year = int(match.group(2))
            return {
                "name": name,
                "year": year,
                "full_text": text
            }
        return None
    
    def _extract_guidelines_from_text(self, text: str) -> List[Dict]:
        """Trích xuất guideline từ text tự do"""
        guidelines = []
        # Pattern để tìm guideline và năm
        patterns = [
            r'([A-Z/]+(?: [A-Z]+)?)\s+.*?Guideline.*?(\d{4})',
            r'([A-Z/]+(?: [A-Z]+)?)\s+.*?(\d{4})',
            r'([A-Z]+)\s+Report\s+(\d{4})',
        ]
        
        found_names = set()
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                name = match.group(1).strip().upper()
                year = int(match.group(2))
                
                # Lọc các guideline chính
                if any(key in name for key in GUIDELINE_CYCLE.keys()):
                    if name not in found_names:
                        found_names.add(name)
                        guidelines.append({
                            "name": name,
                            "year": year,
                            "full_text": match.group(0)
                        })
        
        return guidelines
    
    def check_guideline_updates(self, file_path: Path) -> Dict:
        """Kiểm tra xem guideline có cần cập nhật không"""
        info = self.extract_guideline_info(file_path)
        
        # Đánh giá guideline có cần kiểm tra không
        needs_check = False
        reasons = []
        
        for guideline in info["guidelines"]:
            name = guideline["name"]
            year = guideline["year"]
            
            # Tính toán năm guideline mới nhất có thể có
            # Dựa trên chu kỳ cập nhật
            for key, cycle in GUIDELINE_CYCLE.items():
                if key in name:
                    expected_new_year = year + cycle
                    if CURRENT_YEAR >= expected_new_year:
                        needs_check = True
                        reasons.append(
                            f"{name} {year} có thể đã có bản mới "
                            f"(chu kỳ ~{cycle} năm, hiện tại {CURRENT_YEAR})"
                        )
                    break
        
        # Kiểm tra ngày cập nhật
        if info["last_reviewed"]:
            last_year = int(info["last_reviewed"].split('-')[0])
            if CURRENT_YEAR - last_year >= 1:
                needs_check = True
                reasons.append(f"Chưa kiểm tra từ {last_year} (đã {CURRENT_YEAR - last_year} năm)")
        elif info["update_date"]:
            update_year = int(info["update_date"].split('-')[0])
            if CURRENT_YEAR - update_year >= 1:
                needs_check = True
                reasons.append(f"Ngày cập nhật {update_year} (đã {CURRENT_YEAR - update_year} năm)")
        else:
            needs_check = True
            reasons.append("Không có thông tin ngày cập nhật")
        
        info["needs_check"] = needs_check
        info["reasons"] = reasons
        
        return info
    
    def scan_all_articles(self) -> List[Dict]:
        """Quét tất cả các bài viết"""
        results = []
        
        if not self.articles_dir.exists():
            print(f"Thư mục {self.articles_dir} không tồn tại")
            return results
        
        md_files = list(self.articles_dir.glob("*.md"))
        print(f"Tìm thấy {len(md_files)} file markdown")
        
        for file_path in sorted(md_files):
            try:
                result = self.check_guideline_updates(file_path)
                results.append(result)
            except Exception as e:
                print(f"Lỗi khi xử lý {file_path.name}: {e}")
                results.append({
                    "file": file_path.name,
                    "path": str(file_path),
                    "error": str(e)
                })
        
        return results
    
    def generate_report(self, results: List[Dict], output_file: Optional[Path] = None):
        """Tạo báo cáo về guideline cần kiểm tra"""
        needs_check = [r for r in results if r.get("needs_check", False)]
        no_check_needed = [r for r in results if not r.get("needs_check", False) and "error" not in r]
        errors = [r for r in results if "error" in r]
        
        report_lines = [
            "# Báo cáo kiểm tra Guideline",
            f"**Ngày tạo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Năm hiện tại:** {CURRENT_YEAR}",
            "",
            f"## Tổng quan",
            f"- Tổng số file: {len(results)}",
            f"- Cần kiểm tra: {len(needs_check)}",
            f"- Không cần kiểm tra: {len(no_check_needed)}",
            f"- Lỗi: {len(errors)}",
            "",
        ]
        
        if needs_check:
            report_lines.extend([
                "## Các file cần kiểm tra guideline",
                "",
            ])
            
            for item in needs_check:
                report_lines.append(f"### {item['file']}")
                report_lines.append(f"**Đường dẫn:** `{item['path']}`")
                
                if item.get("guidelines"):
                    report_lines.append("**Guideline hiện tại:**")
                    for g in item["guidelines"]:
                        report_lines.append(f"- {g['name']} {g['year']}")
                
                if item.get("reasons"):
                    report_lines.append("**Lý do cần kiểm tra:**")
                    for reason in item["reasons"]:
                        report_lines.append(f"- {reason}")
                
                if item.get("last_reviewed"):
                    report_lines.append(f"**Last reviewed:** {item['last_reviewed']}")
                elif item.get("update_date"):
                    report_lines.append(f"**Ngày cập nhật:** {item['update_date']}")
                
                report_lines.append("")
        
        if no_check_needed:
            report_lines.extend([
                "## Các file không cần kiểm tra",
                "",
                "Các file này đã có guideline tương đối mới hoặc vừa được kiểm tra gần đây.",
                "",
            ])
            for item in no_check_needed[:20]:  # Chỉ hiển thị 20 đầu tiên
                guidelines_str = ", ".join([f"{g['name']} {g['year']}" for g in item.get("guidelines", [])])
                report_lines.append(f"- `{item['file']}`: {guidelines_str or 'N/A'}")
            
            if len(no_check_needed) > 20:
                report_lines.append(f"\n... và {len(no_check_needed) - 20} file khác")
            report_lines.append("")
        
        if errors:
            report_lines.extend([
                "## Lỗi",
                "",
            ])
            for item in errors:
                report_lines.append(f"- `{item['file']}`: {item['error']}")
            report_lines.append("")
        
        report_text = "\n".join(report_lines)
        
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(report_text, encoding='utf-8')
            print(f"Đã tạo báo cáo: {output_file}")
        else:
            print(report_text)
        
        return report_text
    
    def update_review_dates(self, results: List[Dict], dry_run: bool = True):
        """Tự động cập nhật ngày review cho các file"""
        current_date_str = datetime.now().strftime("%Y-%m")
        
        updated_files = []
        
        for result in results:
            if "error" in result:
                continue
            
            file_path = Path(result["path"])
            if not file_path.exists():
                continue
            
            content = file_path.read_text(encoding='utf-8')
            original_content = content
            
            # Cập nhật last_reviewed trong frontmatter
            if re.search(r'last_reviewed:\s*\d{4}-\d{2}', content):
                content = re.sub(
                    r'last_reviewed:\s*\d{4}-\d{2}',
                    f'last_reviewed: {current_date_str}',
                    content
                )
            
            # Cập nhật "Cập nhật:" trong header
            if re.search(r'\*\*Cập nhật:\*\*\s*Tháng\s+\d{1,2}/\d{4}', content):
                current_month = datetime.now().month
                current_year = datetime.now().year
                content = re.sub(
                    r'\*\*Cập nhật:\*\*\s*Tháng\s+\d{1,2}/\d{4}',
                    f'**Cập nhật:** Tháng {current_month}/{current_year}',
                    content
                )
            
            if content != original_content:
                if not dry_run:
                    file_path.write_text(content, encoding='utf-8')
                    print(f"✅ Đã cập nhật: {file_path.name}")
                else:
                    print(f"📝 Sẽ cập nhật: {file_path.name} (dry-run)")
                updated_files.append(str(file_path))
        
        return updated_files


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Kiểm tra và cập nhật guideline trong các bài viết y khoa"
    )
    parser.add_argument(
        "--update-dates",
        action="store_true",
        help="Tự động cập nhật ngày review (mặc định: dry-run, dùng --force để thực sự cập nhật)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Thực sự cập nhật file (chỉ dùng với --update-dates)"
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Chỉ tạo báo cáo, không cập nhật"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="File output cho báo cáo (mặc định: reports/guideline_check_YYYY-MM-DD.md)"
    )
    
    args = parser.parse_args()
    
    # Tạo checker
    checker = GuidelineChecker(ARTICLES_DIR)
    
    # Quét tất cả bài viết
    print("Đang quét các bài viết...")
    results = checker.scan_all_articles()
    
    # Tạo báo cáo
    if args.output:
        output_file = Path(args.output)
    else:
        REPORT_DIR.mkdir(exist_ok=True)
        output_file = REPORT_DIR / f"guideline_check_{datetime.now().strftime('%Y-%m-%d')}.md"
    
    print("\nĐang tạo báo cáo...")
    checker.generate_report(results, output_file)
    
    # Cập nhật ngày nếu được yêu cầu
    if args.update_dates and not args.report_only:
        print("\nĐang cập nhật ngày review...")
        dry_run = not args.force
        updated = checker.update_review_dates(results, dry_run=dry_run)
        
        if dry_run:
            print(f"\n⚠️  Dry-run mode: {len(updated)} file sẽ được cập nhật")
            print("   Dùng --force để thực sự cập nhật")
        else:
            print(f"\n✅ Đã cập nhật {len(updated)} file")
    
    # Tổng kết
    needs_check = len([r for r in results if r.get("needs_check", False)])
    print(f"\n📊 Tổng kết:")
    print(f"   - Tổng số file: {len(results)}")
    print(f"   - Cần kiểm tra: {needs_check}")
    print(f"   - Báo cáo: {output_file}")


if __name__ == "__main__":
    main()

