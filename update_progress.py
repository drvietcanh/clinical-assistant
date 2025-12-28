#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động cập nhật tiến trình vào file TIEN_TRINH_VALIDATION_CHI_TIET.md
"""

import json
import re
from datetime import datetime
from typing import Dict

def load_validation_report():
    """Đọc báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return None

def get_current_stats(report: Dict) -> Dict:
    """Lấy thống kê hiện tại"""
    stats = report["summary"]
    field_completion = report["field_completion"]
    
    return {
        "total_drugs": stats["total_drugs"],
        "complete_drugs": stats["complete_drugs"],
        "incomplete_drugs": stats["incomplete_drugs"],
        "error_count": stats["error_count"],
        "warning_count": stats["warning_count"],
        "field_completion": field_completion
    }

def update_progress_file(stats: Dict):
    """Cập nhật file tiến trình"""
    progress_file = "TIEN_TRINH_VALIDATION_CHI_TIET.md"
    
    try:
        with open(progress_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Không tìm thấy {progress_file}")
        return
    
    # Cập nhật ngày
    content = re.sub(
        r'\*\*Ngày cập nhật cuối:\*\* \d{4}-\d{2}-\d{2}',
        f'**Ngày cập nhật cuối:** {datetime.now().strftime("%Y-%m-%d")}',
        content
    )
    
    # Cập nhật thống kê database
    stats_section = f"""### Database ({stats['total_drugs']} thuốc)

| Chỉ Số | Giá Trị | Tỷ Lệ | Trạng Thái |
|--------|---------|-------|------------|
| Thuốc hoàn chỉnh | {stats['complete_drugs']} | {stats['complete_drugs']/stats['total_drugs']*100:.1f}% | {'✅ Tốt' if stats['complete_drugs']/stats['total_drugs'] > 0.8 else '⚠️ Cần cải thiện'} |
| Thuốc chưa hoàn chỉnh | {stats['incomplete_drugs']} | {stats['incomplete_drugs']/stats['total_drugs']*100:.1f}% | {'✅ Tốt' if stats['incomplete_drugs']/stats['total_drugs'] < 0.2 else '⚠️ Cần cải thiện'} |
| Lỗi nghiêm trọng | {stats['error_count']} | {stats['error_count']/stats['total_drugs']*100:.1f}% | {'✅ Tốt' if stats['error_count'] == 0 else '❌ Cần sửa'} |
| Cảnh báo | {stats['warning_count']} | - | {'✅ Tốt' if stats['warning_count'] < 500 else '⚠️ Cần xử lý'} |"""
    
    content = re.sub(
        r'### Database \(\d+ thuốc\).*?\| Cảnh báo.*?\|',
        stats_section,
        content,
        flags=re.DOTALL
    )
    
    # Cập nhật enhanced fields
    fields_section = "### Enhanced Fields\n\n| Field | Hoàn Thành | Thiếu | Trạng Thái | Ưu Tiên |\n|-------|-----------|-------|------------|---------|"
    
    priority_order = {
        "contraindications_detail": "HIGH",
        "reversal_agents": "HIGH",
        "black_box_warnings": "MEDIUM",
        "drug_interactions": "MEDIUM",
        "renal_adjustment": "MEDIUM",
        "hepatic_adjustment": "MEDIUM",
        "pregnancy_lactation": "MEDIUM",
        "overdose_management": "MEDIUM",
        "administration_instructions": "MEDIUM",
    }
    
    for field, data in sorted(stats['field_completion'].items(), 
                             key=lambda x: x[1]['percentage']):
        percentage = data['percentage']
        missing = data['missing']
        total = stats['total_drugs']
        
        if percentage == 100:
            status = "✅ 100%"
            priority = "-"
        elif percentage >= 95:
            status = "⚠️ 95%+"
            priority = priority_order.get(field, "LOW")
        elif percentage >= 80:
            status = "⚠️ 80%+"
            priority = priority_order.get(field, "MEDIUM")
        else:
            status = "❌ <80%"
            priority = priority_order.get(field, "HIGH")
        
        fields_section += f"\n| {field} | {data['count']}/{total} | {missing} | {status} | {priority} |"
    
    content = re.sub(
        r'### Enhanced Fields.*?\| administration_instructions.*?\|',
        fields_section,
        content,
        flags=re.DOTALL
    )
    
    # Lưu file
    with open(progress_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Đã cập nhật {progress_file}")

def generate_progress_summary(stats: Dict):
    """Tạo tóm tắt tiến độ"""
    summary = []
    summary.append("=" * 100)
    summary.append("TÓM TẮT TIẾN ĐỘ")
    summary.append("=" * 100)
    summary.append(f"\nNgày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    summary.append(f"\n📊 THỐNG KÊ:")
    summary.append(f"   Tổng số thuốc: {stats['total_drugs']}")
    summary.append(f"   Thuốc hoàn chỉnh: {stats['complete_drugs']} ({stats['complete_drugs']/stats['total_drugs']*100:.1f}%)")
    summary.append(f"   Lỗi: {stats['error_count']}")
    summary.append(f"   Cảnh báo: {stats['warning_count']}")
    
    summary.append(f"\n📋 ENHANCED FIELDS:")
    for field, data in sorted(stats['field_completion'].items(), 
                             key=lambda x: x[1]['missing'], reverse=True):
        if data['missing'] > 0:
            summary.append(f"   {field}: {data['count']}/{stats['total_drugs']} ({data['percentage']:.1f}%) - Thiếu {data['missing']}")
    
    return "\n".join(summary)

def main():
    """Hàm chính"""
    print("Đang cập nhật tiến trình...")
    
    report = load_validation_report()
    if not report:
        return
    
    stats = get_current_stats(report)
    update_progress_file(stats)
    
    # Tạo tóm tắt
    summary = generate_progress_summary(stats)
    print("\n" + summary)
    
    # Lưu tóm tắt
    with open('progress_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"\n✅ Đã lưu tóm tắt vào progress_summary.txt")

if __name__ == '__main__':
    main()

