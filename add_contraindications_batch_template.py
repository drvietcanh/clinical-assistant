#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template script bổ sung contraindications_detail cho nhiều thuốc trong một batch.

Mục tiêu:
- Giảm thời gian viết tay code cho từng thuốc
- Chuẩn hóa format contraindications_detail theo template chung

Cách sử dụng (gợi ý workflow nhanh):
1. Chạy: python generate_missing_lists.py
2. Mở:  missing_lists.json  → lấy danh sách thuốc thiếu "contraindications_detail"
3. Chọn 10–20 thuốc cho batch này, điền vào CONTRAINDICATIONS_DATA ở dưới
4. Chạy: python add_contraindications_batch_template.py  → copy block code output
5. Dán block code đó vào cuối file drugs/enhanced_fields_overrides.py
6. Chạy quick check:
       python quick_validation_check.py --fields contraindications_detail --top 5
"""

from __future__ import annotations

from typing import Dict, List

from drugs.drug_database import DRUG_DATABASE


# TODO: Điền dữ liệu cho từng thuốc theo format bên dưới.
# GỢI Ý AN TOÀN:
# - Chỉ nhập nội dung sau khi đã tham khảo tài liệu chuyên môn
# - Nếu chưa chắc, có thể để placeholder "CẦN XÁC MINH" và review sau
CONTRAINDICATIONS_DATA: Dict[str, Dict[str, Dict[str, List[str]]]] = {
    # Ví dụ cấu trúc (hãy sửa/ghi đè nội dung này cho phù hợp từng thuốc thực tế):
    #
    # "5-Fluorouracil": {
    #     "contraindications_detail": {
    #         "tuyệt_đối": [
    #             "Dị ứng với 5-fluorouracil hoặc bất kỳ thành phần nào của thuốc",
    #             "CẦN XÁC MINH: chống chỉ định tuyệt đối cụ thể từ guideline",
    #         ],
    #         "tương_đối": [
    #             "CẦN XÁC MINH: suy gan/suy thận mức nào thì cần thận trọng",
    #             "CẦN XÁC MINH: các bệnh lý cần giảm liều hoặc theo dõi sát",
    #         ],
    #     },
    # },
}


def generate_code() -> str:
    """Tạo block code EXTRA_ENHANCED_FIELDS.update(...) để dán vào overrides."""
    code_lines: List[str] = []
    code_lines.append(
        "\n# ======================== BATCH: CONTRAINDICATIONS DETAIL ========================\n"
    )
    code_lines.append("# Bổ sung contraindications_detail cho một số thuốc ưu tiên\n\n")
    code_lines.append("EXTRA_ENHANCED_FIELDS.update({\n")

    for drug_name, data in CONTRAINDICATIONS_DATA.items():
        detail = data.get("contraindications_detail", {})
        abs_list = detail.get("tuyệt_đối", [])
        rel_list = detail.get("tương_đối", [])

        code_lines.append(f'    "{drug_name}": {{\n')
        code_lines.append('        "contraindications_detail": {\n')

        # tuyệt_đối
        code_lines.append('            "tuyệt_đối": [\n')
        for item in abs_list:
            code_lines.append(f'                "{item}",\n')
        code_lines.append("            ],\n")

        # tương_đối
        code_lines.append('            "tương_đối": [\n')
        for item in rel_list:
            code_lines.append(f'                "{item}",\n')
        code_lines.append("            ],\n")

        code_lines.append("        },\n")
        code_lines.append("    },\n")

    code_lines.append("})\n")
    code_lines.append(
        "# ======================== END BATCH: CONTRAINDICATIONS DETAIL ===================\n"
    )

    return "".join(code_lines)


def main() -> None:
    print("Kiểm tra các thuốc trong CONTRAINDICATIONS_DATA có nằm trong DRUG_DATABASE không:")
    for drug_name in CONTRAINDICATIONS_DATA.keys():
        if drug_name in DRUG_DATABASE:
            has_field = "contraindications_detail" in DRUG_DATABASE[drug_name]
            status = "ĐÃ CÓ" if has_field else "THIẾU"
            print(f"  ✅ {drug_name}: {status} trong DRUG_DATABASE gốc")
        else:
            print(f"  ❌ {drug_name}: KHÔNG TÌM THẤY trong DRUG_DATABASE")

    print("\n" + "=" * 80)
    print("Code để thêm vào drugs/enhanced_fields_overrides.py:")
    print("=" * 80)
    print(generate_code())


if __name__ == "__main__":
    main()


