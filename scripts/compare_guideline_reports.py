"""
Script so sánh 2 báo cáo guideline để xem có gì thay đổi

Sử dụng:
    python scripts/compare_guideline_reports.py report1.json report2.json
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

def load_report(file_path: Path) -> Dict:
    """Đọc báo cáo từ file JSON"""
    data = json.loads(file_path.read_text(encoding='utf-8'))
    return data

def compare_reports(old_report: Dict, new_report: Dict):
    """So sánh 2 báo cáo"""
    old_files = {f["file"]: f for f in old_report["files"]}
    new_files = {f["file"]: f for f in new_report["files"]}
    
    # Files mới
    new_file_names = set(new_files.keys()) - set(old_files.keys())
    # Files bị xóa
    deleted_file_names = set(old_files.keys()) - set(new_files.keys())
    # Files giữ nguyên
    common_file_names = set(old_files.keys()) & set(new_files.keys())
    
    # So sánh từng file
    changed_files = []
    status_changes = []
    
    for file_name in common_file_names:
        old_file = old_files[file_name]
        new_file = new_files[file_name]
        
        # Kiểm tra thay đổi needs_check
        old_needs_check = old_file.get("needs_check", False)
        new_needs_check = new_file.get("needs_check", False)
        
        if old_needs_check != new_needs_check:
            status_changes.append({
                "file": file_name,
                "old": "Cần kiểm tra" if old_needs_check else "Không cần",
                "new": "Cần kiểm tra" if new_needs_check else "Không cần"
            })
        
        # Kiểm tra thay đổi last_reviewed
        old_reviewed = old_file.get("last_reviewed", "")
        new_reviewed = new_file.get("last_reviewed", "")
        
        if old_reviewed != new_reviewed:
            changed_files.append({
                "file": file_name,
                "change": "last_reviewed",
                "old": old_reviewed,
                "new": new_reviewed
            })
        
        # Kiểm tra thay đổi guideline
        old_guidelines = {(g["name"], g["year"]) for g in old_file.get("guidelines", [])}
        new_guidelines = {(g["name"], g["year"]) for g in new_file.get("guidelines", [])}
        
        if old_guidelines != new_guidelines:
            added = new_guidelines - old_guidelines
            removed = old_guidelines - new_guidelines
            changed_files.append({
                "file": file_name,
                "change": "guidelines",
                "added": [f"{g[0]} {g[1]}" for g in added],
                "removed": [f"{g[0]} {g[1]}" for g in removed]
            })
    
    return {
        "new_files": list(new_file_names),
        "deleted_files": list(deleted_file_names),
        "status_changes": status_changes,
        "changed_files": changed_files,
        "old_date": old_report.get("generated_at", "N/A"),
        "new_date": new_report.get("generated_at", "N/A")
    }

def print_comparison(comparison: Dict):
    """In kết quả so sánh"""
    print("=" * 60)
    print("SO SÁNH BÁO CÁO GUIDELINE")
    print("=" * 60)
    print()
    print(f"Báo cáo cũ: {comparison['old_date']}")
    print(f"Báo cáo mới: {comparison['new_date']}")
    print()
    
    if comparison["new_files"]:
        print(f"📄 File mới ({len(comparison['new_files'])}):")
        for file_name in comparison["new_files"]:
            print(f"   + {file_name}")
        print()
    
    if comparison["deleted_files"]:
        print(f"🗑️  File đã xóa ({len(comparison['deleted_files'])}):")
        for file_name in comparison["deleted_files"]:
            print(f"   - {file_name}")
        print()
    
    if comparison["status_changes"]:
        print(f"🔄 Thay đổi trạng thái ({len(comparison['status_changes'])}):")
        for change in comparison["status_changes"]:
            print(f"   {change['file']}")
            print(f"      {change['old']} → {change['new']}")
        print()
    
    if comparison["changed_files"]:
        print(f"📝 File có thay đổi ({len(comparison['changed_files'])}):")
        for change in comparison["changed_files"]:
            print(f"   {change['file']}: {change['change']}")
            if "old" in change:
                print(f"      Cũ: {change['old']}")
                print(f"      Mới: {change['new']}")
            if "added" in change:
                print(f"      Thêm: {', '.join(change['added'])}")
            if "removed" in change:
                print(f"      Xóa: {', '.join(change['removed'])}")
        print()
    
    if not any([comparison["new_files"], comparison["deleted_files"], 
                comparison["status_changes"], comparison["changed_files"]]):
        print("✅ Không có thay đổi nào")
        print()

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="So sánh 2 báo cáo guideline")
    parser.add_argument("old_report", type=str, help="File báo cáo cũ (JSON)")
    parser.add_argument("new_report", type=str, help="File báo cáo mới (JSON)")
    
    args = parser.parse_args()
    
    old_path = Path(args.old_report)
    new_path = Path(args.new_report)
    
    if not old_path.exists():
        print(f"❌ File không tồn tại: {old_path}")
        return
    
    if not new_path.exists():
        print(f"❌ File không tồn tại: {new_path}")
        return
    
    print("Đang đọc báo cáo...")
    old_report = load_report(old_path)
    new_report = load_report(new_path)
    
    print("Đang so sánh...")
    comparison = compare_reports(old_report, new_report)
    
    print_comparison(comparison)

if __name__ == "__main__":
    main()

