"""
Script xuất báo cáo guideline ra định dạng JSON hoặc CSV

Sử dụng:
    python scripts/export_guideline_report.py --format json
    python scripts/export_guideline_report.py --format csv
"""

import json
import csv
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent))
from check_guideline_updates import GuidelineChecker, ARTICLES_DIR

def export_json(results, output_file):
    """Xuất ra JSON"""
    output_data = {
        "generated_at": datetime.now().isoformat(),
        "total_files": len(results),
        "needs_check": len([r for r in results if r.get("needs_check", False)]),
        "files": results
    }
    
    output_file.write_text(json.dumps(output_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"✅ Đã xuất JSON: {output_file}")

def export_csv(results, output_file):
    """Xuất ra CSV"""
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'File', 'Needs Check', 'Last Reviewed', 'Update Date',
            'Guideline Names', 'Guideline Years', 'Reasons Count'
        ])
        
        # Data
        for result in results:
            if "error" in result:
                continue
            
            guidelines = result.get("guidelines", [])
            guideline_names = ", ".join([g["name"] for g in guidelines])
            guideline_years = ", ".join([str(g["year"]) for g in guidelines])
            
            writer.writerow([
                result["file"],
                "Yes" if result.get("needs_check", False) else "No",
                result.get("last_reviewed", ""),
                result.get("update_date", ""),
                guideline_names,
                guideline_years,
                len(result.get("reasons", []))
            ])
    
    print(f"✅ Đã xuất CSV: {output_file}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Xuất báo cáo guideline ra JSON hoặc CSV")
    parser.add_argument(
        "--format",
        choices=["json", "csv"],
        default="json",
        help="Định dạng xuất (json hoặc csv)"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="File output (mặc định: reports/guideline_report_YYYY-MM-DD.[json|csv])"
    )
    
    args = parser.parse_args()
    
    # Quét file
    print("Đang quét các bài viết...")
    checker = GuidelineChecker(ARTICLES_DIR)
    results = checker.scan_all_articles()
    
    # Xác định file output
    if args.output:
        output_file = Path(args.output)
    else:
        REPORT_DIR = Path("reports")
        REPORT_DIR.mkdir(exist_ok=True)
        ext = args.format
        output_file = REPORT_DIR / f"guideline_report_{datetime.now().strftime('%Y-%m-%d')}.{ext}"
    
    # Xuất
    if args.format == "json":
        export_json(results, output_file)
    else:
        export_csv(results, output_file)
    
    print(f"\n📊 Tổng kết:")
    print(f"   - Tổng số file: {len(results)}")
    print(f"   - Cần kiểm tra: {len([r for r in results if r.get('needs_check', False)])}")

if __name__ == "__main__":
    main()

