#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo báo cáo tiến độ theo thời gian
"""

import json
import os
from datetime import datetime
from typing import List, Dict

def load_all_snapshots() -> List[Dict]:
    """Đọc tất cả snapshots"""
    snapshot_dir = "validation_snapshots"
    if not os.path.exists(snapshot_dir):
        return []
    
    snapshots = []
    for file in sorted(os.listdir(snapshot_dir)):
        if file.endswith('.json'):
            file_path = os.path.join(snapshot_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    snapshots.append({
                        "file": file,
                        "timestamp": data.get("timestamp", ""),
                        "report": data.get("report", data)
                    })
            except Exception as e:
                print(f"⚠️  Lỗi khi đọc {file}: {e}")
    
    return snapshots

def generate_timeline_report(snapshots: List[Dict]) -> str:
    """Tạo báo cáo timeline"""
    if len(snapshots) < 2:
        return "⚠️  Chưa có đủ snapshot để tạo báo cáo timeline (cần ít nhất 2)"
    
    output = []
    output.append("=" * 100)
    output.append("BÁO CÁO TIẾN ĐỘ THEO THỜI GIAN")
    output.append("=" * 100)
    output.append(f"\nTổng số snapshot: {len(snapshots)}")
    output.append(f"Thời gian: {snapshots[0]['timestamp']} → {snapshots[-1]['timestamp']}")
    output.append("")
    
    # So sánh snapshot đầu và cuối
    first = snapshots[0]["report"]
    last = snapshots[-1]["report"]
    
    first_stats = first["summary"]
    last_stats = last["summary"]
    
    output.append("📊 SO SÁNH TỔNG QUAN (Đầu vs Cuối):")
    output.append("-" * 100)
    
    total_drugs = last_stats["total_drugs"]
    
    # Thuốc hoàn chỉnh
    complete_change = last_stats["complete_drugs"] - first_stats["complete_drugs"]
    complete_change_pct = (complete_change / total_drugs * 100) if total_drugs > 0 else 0
    output.append(f"Thuốc hoàn chỉnh:")
    output.append(f"  Đầu: {first_stats['complete_drugs']} ({first_stats['complete_drugs']/total_drugs*100:.1f}%)")
    output.append(f"  Cuối: {last_stats['complete_drugs']} ({last_stats['complete_drugs']/total_drugs*100:.1f}%)")
    output.append(f"  Thay đổi: {complete_change:+d} ({complete_change_pct:+.1f}%)")
    output.append("")
    
    # Lỗi
    error_change = last_stats["error_count"] - first_stats["error_count"]
    output.append(f"Lỗi nghiêm trọng:")
    output.append(f"  Đầu: {first_stats['error_count']}")
    output.append(f"  Cuối: {last_stats['error_count']}")
    output.append(f"  Thay đổi: {error_change:+d}")
    output.append("")
    
    # Cảnh báo
    warning_change = last_stats["warning_count"] - first_stats["warning_count"]
    output.append(f"Cảnh báo:")
    output.append(f"  Đầu: {first_stats['warning_count']}")
    output.append(f"  Cuối: {last_stats['warning_count']}")
    output.append(f"  Thay đổi: {warning_change:+d}")
    output.append("")
    
    # Enhanced fields
    output.append("📋 ENHANCED FIELDS (Đầu vs Cuối):")
    output.append("-" * 100)
    
    for field in first["field_completion"].keys():
        first_data = first["field_completion"][field]
        last_data = last["field_completion"][field]
        
        change = last_data["count"] - first_data["count"]
        change_pct = last_data["percentage"] - first_data["percentage"]
        
        if change != 0 or change_pct != 0:
            output.append(f"{field}:")
            output.append(f"  Đầu: {first_data['count']}/{total_drugs} ({first_data['percentage']:.1f}%)")
            output.append(f"  Cuối: {last_data['count']}/{total_drugs} ({last_data['percentage']:.1f}%)")
            output.append(f"  Thay đổi: {change:+d} ({change_pct:+.1f}%)")
            output.append("")
    
    # Timeline chi tiết
    if len(snapshots) > 2:
        output.append("📅 TIMELINE CHI TIẾT:")
        output.append("-" * 100)
        
        for i in range(1, len(snapshots)):
            prev = snapshots[i-1]["report"]
            curr = snapshots[i]["report"]
            
            prev_stats = prev["summary"]
            curr_stats = curr["summary"]
            
            output.append(f"\n{snapshots[i]['timestamp']}:")
            output.append(f"  Thuốc hoàn chỉnh: {prev_stats['complete_drugs']} → {curr_stats['complete_drugs']} ({curr_stats['complete_drugs'] - prev_stats['complete_drugs']:+d})")
            output.append(f"  Lỗi: {prev_stats['error_count']} → {curr_stats['error_count']} ({curr_stats['error_count'] - prev_stats['error_count']:+d})")
            output.append(f"  Cảnh báo: {prev_stats['warning_count']} → {curr_stats['warning_count']} ({curr_stats['warning_count'] - prev_stats['warning_count']:+d})")
    
    return "\n".join(output)

def main():
    """Hàm chính"""
    print("Đang tạo báo cáo tiến độ...")
    
    snapshots = load_all_snapshots()
    
    if len(snapshots) == 0:
        print("⚠️  Chưa có snapshot nào")
        print("   Chạy compare_validation_results.py để tạo snapshot")
        return
    
    report = generate_timeline_report(snapshots)
    print("\n" + report)
    
    # Lưu báo cáo
    output_file = f"progress_timeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Đã lưu báo cáo: {output_file}")

if __name__ == '__main__':
    main()

