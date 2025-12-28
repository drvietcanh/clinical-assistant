#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script so sánh kết quả validation giữa các lần chạy
"""

import json
import os
from datetime import datetime
from typing import Dict, Optional

def load_validation_report(file_path: str = 'drug_validation_report.json') -> Optional[Dict]:
    """Đọc báo cáo validation"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_validation_report_snapshot(report: Dict, snapshot_name: str = None):
    """Lưu snapshot của báo cáo"""
    if snapshot_name is None:
        snapshot_name = f"validation_snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    snapshot_dir = "validation_snapshots"
    if not os.path.exists(snapshot_dir):
        os.makedirs(snapshot_dir)
    
    snapshot_path = os.path.join(snapshot_dir, snapshot_name)
    
    # Thêm metadata
    snapshot_data = {
        "timestamp": datetime.now().isoformat(),
        "report": report
    }
    
    with open(snapshot_path, 'w', encoding='utf-8') as f:
        json.dump(snapshot_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Đã lưu snapshot: {snapshot_path}")
    return snapshot_path

def compare_reports(report1: Dict, report2: Dict) -> Dict:
    """So sánh 2 báo cáo"""
    stats1 = report1["summary"]
    stats2 = report2["summary"]
    
    comparison = {
        "total_drugs": {
            "before": stats1["total_drugs"],
            "after": stats2["total_drugs"],
            "change": stats2["total_drugs"] - stats1["total_drugs"]
        },
        "complete_drugs": {
            "before": stats1["complete_drugs"],
            "after": stats2["complete_drugs"],
            "change": stats2["complete_drugs"] - stats1["complete_drugs"],
            "change_percent": ((stats2["complete_drugs"] - stats1["complete_drugs"]) / stats1["total_drugs"] * 100) if stats1["total_drugs"] > 0 else 0
        },
        "error_count": {
            "before": stats1["error_count"],
            "after": stats2["error_count"],
            "change": stats2["error_count"] - stats1["error_count"]
        },
        "warning_count": {
            "before": stats1["warning_count"],
            "after": stats2["warning_count"],
            "change": stats2["warning_count"] - stats1["warning_count"]
        },
        "field_completion": {}
    }
    
    # So sánh enhanced fields
    for field in report1["field_completion"].keys():
        before = report1["field_completion"][field]
        after = report2["field_completion"][field]
        
        comparison["field_completion"][field] = {
            "before_count": before["count"],
            "after_count": after["count"],
            "change": after["count"] - before["count"],
            "before_percent": before["percentage"],
            "after_percent": after["percentage"],
            "change_percent": after["percentage"] - before["percentage"]
        }
    
    return comparison

def generate_comparison_report(comparison: Dict, report1_name: str, report2_name: str) -> str:
    """Tạo báo cáo so sánh"""
    output = []
    output.append("=" * 100)
    output.append("BÁO CÁO SO SÁNH VALIDATION")
    output.append("=" * 100)
    output.append(f"\nSo sánh: {report1_name} vs {report2_name}")
    output.append(f"Ngày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("")
    
    # Thống kê tổng quan
    output.append("📊 THỐNG KÊ TỔNG QUAN:")
    output.append("-" * 100)
    
    for key, data in comparison.items():
        if key == "field_completion":
            continue
        
        before = data["before"]
        after = data["after"]
        change = data["change"]
        
        if change > 0:
            change_str = f"+{change} ✅"
        elif change < 0:
            change_str = f"{change} ⚠️"
        else:
            change_str = "0 ➡️"
        
        output.append(f"  {key}:")
        output.append(f"    Trước: {before}")
        output.append(f"    Sau:   {after}")
        output.append(f"    Thay đổi: {change_str}")
        
        if "change_percent" in data:
            output.append(f"    Thay đổi %: {data['change_percent']:+.1f}%")
        output.append("")
    
    # Enhanced fields
    output.append("📋 ENHANCED FIELDS:")
    output.append("-" * 100)
    
    for field, data in sorted(comparison["field_completion"].items(),
                             key=lambda x: abs(x[1]["change"]), reverse=True):
        if data["change"] != 0 or data["change_percent"] != 0:
            before_pct = data["before_percent"]
            after_pct = data["after_percent"]
            change_pct = data["change_percent"]
            
            if change_pct > 0:
                status = "✅ Cải thiện"
            elif change_pct < 0:
                status = "⚠️ Giảm"
            else:
                status = "➡️ Không đổi"
            
            output.append(f"  {field}:")
            output.append(f"    Trước: {data['before_count']} ({before_pct:.1f}%)")
            output.append(f"    Sau:   {data['after_count']} ({after_pct:.1f}%)")
            output.append(f"    Thay đổi: {data['change']:+d} ({change_pct:+.1f}%) {status}")
            output.append("")
    
    return "\n".join(output)

def list_snapshots():
    """Liệt kê các snapshot có sẵn"""
    snapshot_dir = "validation_snapshots"
    if not os.path.exists(snapshot_dir):
        return []
    
    snapshots = []
    for file in os.listdir(snapshot_dir):
        if file.endswith('.json'):
            snapshots.append(file)
    
    return sorted(snapshots)

def main():
    """Hàm chính"""
    import sys
    
    # Lưu snapshot hiện tại
    current_report = load_validation_report()
    if not current_report:
        print("❌ Không tìm thấy drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return
    
    print("Đang lưu snapshot hiện tại...")
    snapshot_path = save_validation_report_snapshot(current_report)
    
    # Kiểm tra có snapshot trước đó không
    snapshots = list_snapshots()
    if len(snapshots) < 2:
        print("\n⚠️  Chưa có đủ snapshot để so sánh")
        print(f"   Hiện có {len(snapshots)} snapshot(s)")
        print("   Chạy lại script sau khi có thay đổi để so sánh")
        return
    
    # So sánh với snapshot gần nhất
    previous_snapshot = snapshots[-2]  # Snapshot trước snapshot vừa tạo
    previous_path = os.path.join("validation_snapshots", previous_snapshot)
    
    print(f"\nĐang so sánh với snapshot trước: {previous_snapshot}")
    previous_report_data = load_validation_report(previous_path)
    
    if previous_report_data:
        previous_report = previous_report_data.get("report", previous_report_data)
        comparison = compare_reports(previous_report, current_report)
        
        report_text = generate_comparison_report(
            comparison,
            previous_snapshot,
            os.path.basename(snapshot_path)
        )
        
        print("\n" + report_text)
        
        # Lưu báo cáo so sánh
        comparison_file = f"comparison_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(comparison_file, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print(f"\n✅ Đã lưu báo cáo so sánh: {comparison_file}")

if __name__ == '__main__':
    main()

