#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kiểm tra nhanh - chỉ hiển thị tóm tắt

Tùy chọn:
- --fields a,b,c : chỉ kiểm tra các enhanced fields được chọn (mặc định kiểm tra cả 14)
- --top N        : hiển thị N field thiếu nhiều nhất (0 để bỏ qua, mặc định 5)
"""

import argparse

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    print("❌ Lỗi: Không thể import DRUG_DATABASE")
    exit(1)

# 14 enhanced fields
ENHANCED_FIELDS = [
    "mechanism_of_action",
    "monitoring",
    "precautions",
    "pharmacokinetics",
    "storage",
    "black_box_warnings",
    "drug_interactions",
    "contraindications_detail",
    "pregnancy_lactation",
    "hepatic_adjustment",
    "renal_adjustment",
    "overdose_management",
    "reversal_agents",
    "administration_instructions"
]

def parse_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Kiểm tra nhanh dữ liệu thuốc")
    parser.add_argument(
        "--fields",
        help="Danh sách enhanced fields, phân tách bằng dấu phẩy. Mặc định kiểm tra cả 14 field.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Số field thiếu nhiều nhất cần hiển thị (0 để bỏ qua). Mặc định 5.",
    )
    return parser.parse_args()


def quick_check(fields: str | None = None, top: int = 5):
    """Kiểm tra nhanh và hiển thị tóm tắt - Tối ưu tốc độ"""
    # Xác định danh sách field cần kiểm tra
    if fields:
        selected_fields = [f.strip() for f in fields.split(",") if f.strip()]
    else:
        selected_fields = ENHANCED_FIELDS

    # Loại bỏ trùng lặp, giữ nguyên thứ tự
    selected_fields = list(dict.fromkeys(selected_fields))

    invalid_fields = [f for f in selected_fields if f not in ENHANCED_FIELDS]
    if invalid_fields:
        print(f"❌ Field không hợp lệ: {', '.join(invalid_fields)}")
        print(f"✅ Fields hợp lệ: {', '.join(ENHANCED_FIELDS)}")
        return

    total = len(DRUG_DATABASE)
    checking_all_fields = len(selected_fields) == len(ENHANCED_FIELDS)

    # Đếm enhanced fields
    field_counts = {field: 0 for field in selected_fields}
    complete_drugs = 0
    error_count = 0
    
    # Single pass iteration với tối ưu
    for drug_data in DRUG_DATABASE.values():  # Chỉ cần values, không cần keys
        drug_complete = True

        # Kiểm tra enhanced fields - tối ưu với single pass
        for field in selected_fields:
            value = drug_data.get(field)  # get() nhanh hơn 'in' + access
            if value is not None:
                # Tối ưu type checking
                if isinstance(value, str):
                    if value.strip():  # Chỉ check strip nếu là string
                        field_counts[field] += 1
                    else:
                        drug_complete = False
                elif isinstance(value, (list, dict)):
                    if len(value) > 0:  # Fast length check
                        field_counts[field] += 1
                    else:
                        drug_complete = False
                else:
                    drug_complete = False
            else:
                drug_complete = False
        
        # Kiểm tra lỗi cơ bản - tối ưu với get()
        if not drug_data.get("dosage"):
            error_count += 1
        if not drug_data.get("indications"):
            error_count += 1
        
        if drug_complete:
            complete_drugs += 1
    
    # Hiển thị kết quả
    print("=" * 80)
    print("KIỂM TRA NHANH DỮ LIỆU THUỐC")
    print("=" * 80)
    print(f"\n📊 Tổng số thuốc: {total}")
    print(f"🔎 Đang kiểm tra fields: {', '.join(selected_fields)}")
    if checking_all_fields:
        print(f"✅ Thuốc hoàn chỉnh (14 enhanced fields): {complete_drugs} ({complete_drugs/total*100:.1f}%)")
        print(f"⚠️  Thuốc chưa hoàn chỉnh: {total - complete_drugs} ({(total-complete_drugs)/total*100:.1f}%)")
    else:
        print(f"✅ Thuốc đầy đủ các field đã chọn: {complete_drugs} ({complete_drugs/total*100:.1f}%)")
        print(f"⚠️  Thuốc thiếu ít nhất một field đã chọn: {total - complete_drugs} ({(total-complete_drugs)/total*100:.1f}%)")
    print(f"❌ Lỗi cơ bản: {error_count}")
    
    print("\n📋 Tỷ lệ hoàn thành Enhanced Fields:")
    print("-" * 80)
    for field in selected_fields:
        count = field_counts[field]
        percentage = count / total * 100
        status = "✅" if percentage == 100 else "⚠️ " if percentage >= 80 else "❌"
        print(f"{status} {field:<35} {count:3d}/{total:3d} ({percentage:5.1f}%)")
    
    # Top field thiếu nhiều nhất
    if top and top > 0:
        missing_fields = sorted(
            [(field, total - count) for field, count in field_counts.items()],
            key=lambda x: x[1],
            reverse=True
        )[:top]
        
        if any(count > 0 for _, count in missing_fields):
            print(f"\n🔴 Top {top} field thiếu nhiều nhất:")
            for field, missing_count in missing_fields:
                if missing_count > 0:
                    print(f"   • {field}: thiếu {missing_count} thuốc")
    
    print("\n" + "=" * 80)
    print("💡 Chạy 'python comprehensive_drug_validation.py' để xem báo cáo chi tiết")
    print("=" * 80)

if __name__ == '__main__':
    args = parse_args()
    quick_check(fields=args.fields, top=args.top)

