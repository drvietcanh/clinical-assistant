#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script export danh sách các vấn đề cần sửa từ báo cáo validation
"""

import json
from typing import Dict, List
from collections import defaultdict

def load_validation_report():
    """Đọc báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy file drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return None

def export_errors_by_priority(report: Dict):
    """Export lỗi theo mức độ ưu tiên"""
    errors_by_type = defaultdict(list)
    
    for drug, errors in report["errors_by_drug"].items():
        for error in errors:
            if "Thiếu field bắt buộc" in error:
                errors_by_type["CRITICAL - Thiếu field bắt buộc"].append((drug, error))
            elif "Kiểu dữ liệu sai" in error:
                errors_by_type["HIGH - Sai kiểu dữ liệu"].append((drug, error))
            elif "phải là dictionary" in error or "phải là list" in error:
                errors_by_type["HIGH - Cấu trúc sai"].append((drug, error))
            elif "Field rỗng" in error:
                errors_by_type["MEDIUM - Field rỗng"].append((drug, error))
            else:
                errors_by_type["OTHER"].append((drug, error))
    
    output = []
    output.append("=" * 100)
    output.append("DANH SÁCH LỖI CẦN SỬA THEO MỨC ĐỘ ƯU TIÊN")
    output.append("=" * 100)
    output.append("")
    
    priority_order = [
        "CRITICAL - Thiếu field bắt buộc",
        "HIGH - Sai kiểu dữ liệu",
        "HIGH - Cấu trúc sai",
        "MEDIUM - Field rỗng",
        "OTHER"
    ]
    
    for priority in priority_order:
        if priority in errors_by_type:
            output.append(f"\n{priority} ({len(errors_by_type[priority])} lỗi):")
            output.append("-" * 100)
            for drug, error in errors_by_type[priority]:
                output.append(f"  • {drug}: {error}")
    
    return "\n".join(output)

def export_missing_fields_summary(report: Dict):
    """Export tóm tắt các field thiếu"""
    missing_by_field = defaultdict(list)
    
    # Lấy danh sách thuốc thiếu từng enhanced field
    for field, data in report["field_completion"].items():
        if data["missing"] > 0:
            # Tìm các thuốc thiếu field này
            for drug, warnings in report["warnings_by_drug"].items():
                for warning in warnings:
                    if f"Thiếu enhanced field: {field}" in warning or f"Enhanced field rỗng: {field}" in warning:
                        missing_by_field[field].append(drug)
    
    output = []
    output.append("=" * 100)
    output.append("DANH SÁCH THUỐC THIẾU ENHANCED FIELDS")
    output.append("=" * 100)
    output.append("")
    
    # Sắp xếp theo số lượng thiếu (nhiều nhất trước)
    sorted_fields = sorted(
        report["field_completion"].items(),
        key=lambda x: x[1]["missing"],
        reverse=True
    )
    
    for field, data in sorted_fields:
        if data["missing"] > 0:
            output.append(f"\n{field} - Thiếu {data['missing']} thuốc ({100-data['percentage']:.1f}%):")
            output.append("-" * 100)
            # Chỉ hiển thị 20 thuốc đầu tiên
            missing_drugs = missing_by_field.get(field, [])[:20]
            for drug in sorted(missing_drugs):
                output.append(f"  • {drug}")
            if len(missing_by_field.get(field, [])) > 20:
                output.append(f"  ... và {len(missing_by_field.get(field, [])) - 20} thuốc khác")
    
    return "\n".join(output)

def export_drugs_needing_fixes(report: Dict):
    """Export danh sách thuốc cần sửa với chi tiết"""
    output = []
    output.append("=" * 100)
    output.append("DANH SÁCH CHI TIẾT CÁC THUỐC CẦN SỬA")
    output.append("=" * 100)
    output.append("")
    
    # Thuốc có lỗi
    if report["drugs_with_errors"]:
        output.append(f"\n❌ THUỐC CÓ LỖI ({len(report['drugs_with_errors'])}):")
        output.append("=" * 100)
        for drug in sorted(report["drugs_with_errors"]):
            output.append(f"\n{drug}:")
            for error in report["errors_by_drug"][drug]:
                output.append(f"  {error}")
    
    # Thuốc có cảnh báo (top 50)
    if report["drugs_with_warnings"]:
        output.append(f"\n\n⚠️  THUỐC CÓ CẢNH BÁO (hiển thị 50 đầu tiên trong {len(report['drugs_with_warnings'])}):")
        output.append("=" * 100)
        for drug in sorted(report["drugs_with_warnings"])[:50]:
            output.append(f"\n{drug}:")
            warnings = report["warnings_by_drug"][drug]
            # Nhóm cảnh báo theo loại
            missing_fields = [w for w in warnings if "Thiếu enhanced field" in w]
            empty_fields = [w for w in warnings if "Enhanced field rỗng" in w]
            other_warnings = [w for w in warnings if w not in missing_fields + empty_fields]
            
            if missing_fields:
                output.append("  Thiếu field:")
                for w in missing_fields[:5]:  # 5 đầu tiên
                    output.append(f"    {w}")
                if len(missing_fields) > 5:
                    output.append(f"    ... và {len(missing_fields) - 5} field khác")
            
            if empty_fields:
                output.append("  Field rỗng:")
                for w in empty_fields[:5]:
                    output.append(f"    {w}")
                if len(empty_fields) > 5:
                    output.append(f"    ... và {len(empty_fields) - 5} field khác")
            
            if other_warnings:
                output.append("  Cảnh báo khác:")
                for w in other_warnings[:3]:
                    output.append(f"    {w}")
    
    return "\n".join(output)

def main():
    """Hàm chính"""
    report = load_validation_report()
    if not report:
        return
    
    print("Đang tạo các file export...")
    
    # 1. Lỗi theo mức độ ưu tiên
    errors_priority = export_errors_by_priority(report)
    with open('validation_errors_by_priority.txt', 'w', encoding='utf-8') as f:
        f.write(errors_priority)
    print("✅ Đã tạo: validation_errors_by_priority.txt")
    
    # 2. Tóm tắt field thiếu
    missing_fields = export_missing_fields_summary(report)
    with open('validation_missing_fields_summary.txt', 'w', encoding='utf-8') as f:
        f.write(missing_fields)
    print("✅ Đã tạo: validation_missing_fields_summary.txt")
    
    # 3. Chi tiết thuốc cần sửa
    drugs_fixes = export_drugs_needing_fixes(report)
    with open('validation_drugs_needing_fixes.txt', 'w', encoding='utf-8') as f:
        f.write(drugs_fixes)
    print("✅ Đã tạo: validation_drugs_needing_fixes.txt")
    
    # 4. Tạo file CSV cho dễ import vào Excel
    import csv
    with open('validation_errors.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['Thuốc', 'Loại Lỗi', 'Mô Tả'])
        
        for drug in sorted(report["drugs_with_errors"]):
            for error in report["errors_by_drug"][drug]:
                error_type = "LỖI"
                writer.writerow([drug, error_type, error])
        
        for drug in sorted(report["drugs_with_warnings"])[:100]:  # 100 đầu tiên
            for warning in report["warnings_by_drug"][drug][:3]:  # 3 cảnh báo đầu
                warning_type = "CẢNH BÁO"
                writer.writerow([drug, warning_type, warning])
    
    print("✅ Đã tạo: validation_errors.csv")
    
    print("\n" + "=" * 100)
    print("HOÀN THÀNH EXPORT")
    print("=" * 100)
    print("\nCác file đã tạo:")
    print("  1. validation_errors_by_priority.txt - Lỗi theo mức độ ưu tiên")
    print("  2. validation_missing_fields_summary.txt - Tóm tắt field thiếu")
    print("  3. validation_drugs_needing_fixes.txt - Chi tiết thuốc cần sửa")
    print("  4. validation_errors.csv - File CSV để import vào Excel")

if __name__ == '__main__':
    main()

