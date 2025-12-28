#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo checklist tự động dựa trên kết quả validation
"""

import json
from datetime import datetime
from typing import Dict, List

def load_validation_report():
    """Đọc báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy drug_validation_report.json")
        return None

def create_checklist(report: Dict) -> str:
    """Tạo checklist"""
    stats = report["summary"]
    errors_by_drug = report["errors_by_drug"]
    field_completion = report["field_completion"]
    
    output = []
    output.append("# ✅ Checklist Công Việc Validation")
    output.append("")
    output.append(f"**Ngày tạo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append(f"**Tổng số thuốc:** {stats['total_drugs']}")
    output.append("")
    output.append("---")
    output.append("")
    
    # Phase 1: Sửa lỗi
    output.append("## 🔴 Phase 1: Sửa Lỗi Nghiêm Trọng (CRITICAL)")
    output.append("")
    
    if errors_by_drug:
        output.append(f"**Tổng số lỗi:** {stats['error_count']}")
        output.append(f"**Số thuốc có lỗi:** {len(errors_by_drug)}")
        output.append("")
        
        for drug_name in sorted(errors_by_drug.keys()):
            errors = errors_by_drug[drug_name]
            output.append(f"### {drug_name}")
            output.append("")
            for error in errors:
                output.append(f"- [ ] {error}")
            output.append("")
    else:
        output.append("✅ Không có lỗi nghiêm trọng!")
        output.append("")
    
    output.append("---")
    output.append("")
    
    # Phase 2: Bổ sung enhanced fields
    output.append("## 🟠 Phase 2: Bổ Sung Enhanced Fields (HIGH)")
    output.append("")
    
    # Sắp xếp theo số lượng thiếu
    sorted_fields = sorted(
        field_completion.items(),
        key=lambda x: x[1]["missing"],
        reverse=True
    )
    
    for field, data in sorted_fields:
        if data["missing"] > 0:
            missing = data["missing"]
            percentage = data["percentage"]
            
            if percentage < 50:
                priority = "🔴 HIGH"
            elif percentage < 80:
                priority = "🟠 MEDIUM"
            else:
                priority = "🟡 LOW"
            
            output.append(f"### {field} {priority}")
            output.append("")
            output.append(f"- [ ] Bổ sung cho {missing} thuốc ({100-percentage:.1f}% thiếu)")
            output.append(f"  - Hoàn thành: {data['count']}/{stats['total_drugs']} ({percentage:.1f}%)")
            output.append(f"  - Thiếu: {missing}")
            output.append("")
            
            # Thêm sub-tasks
            if missing > 100:
                output.append(f"  - [ ] Nhóm 1: 50 thuốc đầu tiên")
                output.append(f"  - [ ] Nhóm 2: 50 thuốc tiếp theo")
                if missing > 200:
                    output.append(f"  - [ ] Nhóm 3: 50 thuốc tiếp theo")
                if missing > 300:
                    output.append(f"  - [ ] Nhóm 4: 50 thuốc tiếp theo")
                output.append(f"  - [ ] Nhóm cuối: {missing - (missing // 50) * 50} thuốc còn lại")
                output.append("")
            elif missing > 50:
                output.append(f"  - [ ] Nhóm 1: 50 thuốc đầu tiên")
                output.append(f"  - [ ] Nhóm 2: {missing - 50} thuốc còn lại")
                output.append("")
            else:
                output.append(f"  - [ ] Bổ sung cho tất cả {missing} thuốc")
                output.append("")
    
    output.append("---")
    output.append("")
    
    # Phase 3: Kiểm tra lại
    output.append("## ✅ Phase 3: Kiểm Tra Lại")
    output.append("")
    output.append("- [ ] Chạy validation lại")
    output.append("  - [ ] `python comprehensive_drug_validation.py`")
    output.append("  - [ ] Kiểm tra không còn lỗi nghiêm trọng")
    output.append("  - [ ] Kiểm tra tỷ lệ hoàn thành đã tăng")
    output.append("")
    output.append("- [ ] Cập nhật tiến trình")
    output.append("  - [ ] `python update_progress.py`")
    output.append("  - [ ] Cập nhật `TIEN_TRINH_VALIDATION_CHI_TIET.md`")
    output.append("")
    output.append("- [ ] Commit changes")
    output.append("  - [ ] Review changes")
    output.append("  - [ ] Commit với message rõ ràng")
    output.append("")
    
    return "\n".join(output)

def main():
    """Hàm chính"""
    print("Đang tạo checklist...")
    
    report = load_validation_report()
    if not report:
        return
    
    checklist = create_checklist(report)
    
    # Lưu file
    output_file = "validation_checklist.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(checklist)
    
    print(f"✅ Đã tạo checklist: {output_file}")
    print("\n" + "=" * 80)
    print("PREVIEW:")
    print("=" * 80)
    print(checklist[:1000] + "..." if len(checklist) > 1000 else checklist)

if __name__ == '__main__':
    main()

