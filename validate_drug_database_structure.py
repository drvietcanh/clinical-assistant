#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schema-level validator for DRUG_DATABASE

Mục tiêu:
- Kiểm tra cấu trúc 14 enhanced fields cho mọi thuốc trong DRUG_DATABASE.
- Bắt lỗi kiểu dữ liệu sai, thiếu key con trong dict, cấu trúc list/dict bất thường.
- Bổ sung lớp kiểm tra khác với các script đếm field trống/thiếu.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from drugs.drug_database import DRUG_DATABASE


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
    "administration_instructions",
]


class ValidationError:
    def __init__(self, drug: str, field: str, message: str) -> None:
        self.drug = drug
        self.field = field
        self.message = message

    def to_dict(self) -> Dict[str, Any]:
        return {"drug": self.drug, "field": self.field, "message": self.message}

    def __str__(self) -> str:
        return f"[{self.drug}] {self.field}: {self.message}"


def _ensure_dict(value: Any) -> Tuple[Dict[str, Any], bool]:
    """Return dict value and flag whether it is a valid dict."""
    if isinstance(value, dict):
        return value, True
    return {}, False


def _ensure_list(value: Any) -> Tuple[List[Any], bool]:
    """Return list value and flag whether it is a valid list."""
    if isinstance(value, list):
        return value, True
    # Cho phép giá trị đơn lẻ (str) nhưng đánh dấu là không chuẩn list
    if isinstance(value, str):
        return [value], False
    return [], False


def validate_mechanism_of_action(drug: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    if not isinstance(value, str):
        errors.append(
            ValidationError(
                drug,
                "mechanism_of_action",
                f"expected str, got {type(value).__name__}",
            )
        )
    elif not value.strip():
        errors.append(
            ValidationError(
                drug,
                "mechanism_of_action",
                "string is empty or whitespace",
            )
        )
    return errors


def validate_string_field(drug: str, field: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    if not isinstance(value, str):
        errors.append(
            ValidationError(
                drug,
                field,
                f"expected str, got {type(value).__name__}",
            )
        )
    return errors


def validate_string_list_field(drug: str, field: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    lst, is_list = _ensure_list(value)
    if not is_list:
        errors.append(
            ValidationError(
                drug,
                field,
                f"expected list[str], got {type(value).__name__}",
            )
        )
    for idx, item in enumerate(lst):
        if not isinstance(item, str):
            errors.append(
                ValidationError(
                    drug,
                    field,
                    f"element {idx} expected str, got {type(item).__name__}",
                )
            )
    return errors


def validate_pharmacokinetics(drug: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    dct, ok = _ensure_dict(value)
    if not ok:
        errors.append(
            ValidationError(
                drug,
                "pharmacokinetics",
                f"expected dict, got {type(value).__name__}",
            )
        )
        return errors

    required_keys = [
        "absorption",
        "distribution",
        "metabolism",
        "excretion",
        "half_life",
        "notes",
    ]
    for key in required_keys:
        if key not in dct:
            errors.append(
                ValidationError(
                    drug,
                    "pharmacokinetics",
                    f"missing key '{key}'",
                )
            )
        elif not isinstance(dct[key], str):
            errors.append(
                ValidationError(
                    drug,
                    "pharmacokinetics",
                    f"key '{key}' expected str, got {type(dct[key]).__name__}",
                )
            )
    return errors


def validate_drug_interactions(drug: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    dct, ok = _ensure_dict(value)
    if not ok:
        errors.append(
            ValidationError(
                drug,
                "drug_interactions",
                f"expected dict, got {type(value).__name__}",
            )
        )
        return errors

    required_keys = ["major", "moderate", "minor"]
    for key in required_keys:
        if key not in dct:
            errors.append(
                ValidationError(
                    drug,
                    "drug_interactions",
                    f"missing key '{key}'",
                )
            )
            continue
        lst, is_list = _ensure_list(dct[key])
        if not is_list and not isinstance(dct[key], list):
            errors.append(
                ValidationError(
                    drug,
                    "drug_interactions",
                    f"key '{key}' expected list, got {type(dct[key]).__name__}",
                )
            )
        for idx, item in enumerate(lst):
            if not isinstance(item, str):
                errors.append(
                    ValidationError(
                        drug,
                        "drug_interactions",
                        f"key '{key}' element {idx} expected str, got {type(item).__name__}",
                    )
                )
    return errors


def validate_contraindications_detail(drug: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    dct, ok = _ensure_dict(value)
    if not ok:
        errors.append(
            ValidationError(
                drug,
                "contraindications_detail",
                f"expected dict, got {type(value).__name__}",
            )
        )
        return errors

    required_keys = ["tuyệt_đối", "tương_đối"]
    for key in required_keys:
        if key not in dct:
            errors.append(
                ValidationError(
                    drug,
                    "contraindications_detail",
                    f"missing key '{key}'",
                )
            )
            continue
        lst, is_list = _ensure_list(dct[key])
        if not is_list and not isinstance(dct[key], list):
            errors.append(
                ValidationError(
                    drug,
                    "contraindications_detail",
                    f"key '{key}' expected list, got {type(dct[key]).__name__}",
                )
            )
        for idx, item in enumerate(lst):
            if not isinstance(item, str):
                errors.append(
                    ValidationError(
                        drug,
                        "contraindications_detail",
                        f"key '{key}' element {idx} expected str, got {type(item).__name__}",
                    )
                )
    return errors


def validate_renal_adjustment(drug: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    dct, ok = _ensure_dict(value)
    if not ok:
        errors.append(
            ValidationError(
                drug,
                "renal_adjustment",
                f"expected dict, got {type(value).__name__}",
            )
        )
        return errors

    required_keys = ["normal", "30_60", "under_30", "dialysis", "notes"]
    for key in required_keys:
        if key not in dct:
            errors.append(
                ValidationError(
                    drug,
                    "renal_adjustment",
                    f"missing key '{key}'",
                )
            )
            continue
        if not isinstance(dct[key], str):
            errors.append(
                ValidationError(
                    drug,
                    "renal_adjustment",
                    f"key '{key}' expected str, got {type(dct[key]).__name__}",
                )
            )
    return errors


def validate_reversal_agents(drug: str, value: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []
    dct, ok = _ensure_dict(value)
    if not ok:
        errors.append(
            ValidationError(
                drug,
                "reversal_agents",
                f"expected dict, got {type(value).__name__}",
            )
        )
        return errors

    required_keys = ["available", "agents", "notes"]
    for key in required_keys:
        if key not in dct:
            errors.append(
                ValidationError(
                    drug,
                    "reversal_agents",
                    f"missing key '{key}'",
                )
            )
            continue
        if key == "available":
            if not isinstance(dct[key], bool):
                errors.append(
                    ValidationError(
                        drug,
                        "reversal_agents",
                        f"key 'available' expected bool, got {type(dct[key]).__name__}",
                    )
                )
        elif key == "agents":
            lst, is_list = _ensure_list(dct[key])
            if not is_list and not isinstance(dct[key], list):
                errors.append(
                    ValidationError(
                        drug,
                        "reversal_agents",
                        f"key 'agents' expected list, got {type(dct[key]).__name__}",
                    )
                )
            for idx, item in enumerate(lst):
                if not isinstance(item, str):
                    errors.append(
                        ValidationError(
                            drug,
                            "reversal_agents",
                            f"key 'agents' element {idx} expected str, got {type(item).__name__}",
                        )
                    )
        elif key == "notes":
            if not isinstance(dct[key], str):
                errors.append(
                    ValidationError(
                        drug,
                        "reversal_agents",
                        f"key 'notes' expected str, got {type(dct[key]).__name__}",
                    )
                )
    return errors


def validate_drug(drug_name: str, data: Any) -> List[ValidationError]:
    errors: List[ValidationError] = []

    if not isinstance(data, dict):
        errors.append(
            ValidationError(
                drug_name,
                "<root>",
                f"expected dict drug data, got {type(data).__name__}",
            )
        )
        return errors

    for field in ENHANCED_FIELDS:
        if field not in data:
            errors.append(
                ValidationError(
                    drug_name,
                    field,
                    "missing enhanced field key",
                )
            )
            # Nếu thiếu key thì không kiểm tiếp cấu trúc field đó
            continue

        value = data[field]

        if field == "mechanism_of_action":
            errors.extend(validate_mechanism_of_action(drug_name, value))
        elif field in ("pregnancy_lactation", "hepatic_adjustment", "storage", "overdose_management", "administration_instructions", "black_box_warnings"):
            errors.extend(validate_string_field(drug_name, field, value))
        elif field in ("monitoring", "precautions"):
            errors.extend(validate_string_list_field(drug_name, field, value))
        elif field == "pharmacokinetics":
            errors.extend(validate_pharmacokinetics(drug_name, value))
        elif field == "drug_interactions":
            errors.extend(validate_drug_interactions(drug_name, value))
        elif field == "contraindications_detail":
            errors.extend(validate_contraindications_detail(drug_name, value))
        elif field == "renal_adjustment":
            errors.extend(validate_renal_adjustment(drug_name, value))
        elif field == "reversal_agents":
            errors.extend(validate_reversal_agents(drug_name, value))

    return errors


def validate_database() -> List[ValidationError]:
    all_errors: List[ValidationError] = []

    for drug_name, data in DRUG_DATABASE.items():
        drug_errors = validate_drug(drug_name, data)
        all_errors.extend(drug_errors)

    return all_errors


def main() -> None:
    errors = validate_database()

    total_drugs = len(DRUG_DATABASE)
    total_errors = len(errors)

    print("=" * 80)
    print("DRUG_DATABASE STRUCTURAL VALIDATION")
    print("=" * 80)
    print(f"Tổng số thuốc: {total_drugs}")
    print(f"Tổng số lỗi cấu trúc enhanced fields: {total_errors}")

    if total_errors == 0:
        print("\n✓ Tất cả thuốc đều đạt chuẩn schema enhanced fields (cấu trúc).")
        return

    # Gom lỗi theo field để dễ xem tổng quan
    by_field: Dict[str, int] = {}
    for err in errors:
        by_field[err.field] = by_field.get(err.field, 0) + 1

    print("\nTổng quan lỗi theo field:")
    for field, count in sorted(by_field.items(), key=lambda x: x[0]):
        print(f"  - {field}: {count} lỗi")

    print("\nMột số lỗi ví dụ (tối đa 50 dòng):")
    for err in errors[:50]:
        print(f"  - {err}")


if __name__ == "__main__":
    main()

