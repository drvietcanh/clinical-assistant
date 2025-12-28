#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility script to pre-compute and cache lists of drugs missing key enhanced fields.

Mục tiêu:
- Giúp xem nhanh danh sách thuốc còn thiếu các enhanced fields quan trọng
- Tránh phải quét lại toàn bộ DRUG_DATABASE nhiều lần

Sử dụng:
    python generate_missing_lists.py

Kết quả:
- Tạo file missing_lists.json ở thư mục gốc với cấu trúc:
    {
        "contraindications_detail": ["Drug A", "Drug B", ...],
        "reversal_agents": ["Drug X", ...],
        "black_box_warnings": [...],
        "renal_adjustment": [...],
        "hepatic_adjustment": [...]
    }
"""

from __future__ import annotations

import json
from pathlib import Path

from drugs.drug_database import DRUG_DATABASE


ROOT_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT_DIR / "missing_lists.json"

# Các field quan trọng cần theo dõi thường xuyên
TARGET_FIELDS = [
    "contraindications_detail",
    "reversal_agents",
    "black_box_warnings",
    "renal_adjustment",
    "hepatic_adjustment",
]


def is_field_missing(drug_data: dict, field: str) -> bool:
    """
    Quy ước "thiếu" field:
    - Không có key
    - Hoặc value là None / rỗng / False
    """
    value = drug_data.get(field)
    if value is None:
        return True
    if value is False:
        return True
    if isinstance(value, (list, tuple, dict, str)) and not value:
        return True
    return False


def build_missing_lists() -> dict[str, list[str]]:
    """
    Quét DRUG_DATABASE và tạo danh sách thuốc thiếu cho từng field.
    """
    missing: dict[str, list[str]] = {field: [] for field in TARGET_FIELDS}

    for name, data in DRUG_DATABASE.items():
        for field in TARGET_FIELDS:
            if is_field_missing(data, field):
                missing[field].append(name)

    # Sắp xếp cho dễ đọc / dễ diff
    for field in TARGET_FIELDS:
        missing[field].sort()

    return missing


def main() -> None:
    print("=" * 80)
    print("TẠO DANH SÁCH THUỐC THIẾU ENHANCED FIELDS".center(80))
    print("=" * 80)

    missing = build_missing_lists()

    OUTPUT_PATH.write_text(
        json.dumps(missing, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"✅ Đã ghi file: {OUTPUT_PATH}")
    print()
    for field, drugs in missing.items():
        print(f"- {field}: còn thiếu {len(drugs)} thuốc")
    print()
    print("💡 Có thể mở missing_lists.json trong editor hoặc Excel để xem chi tiết.")


if __name__ == "__main__":
    main()


