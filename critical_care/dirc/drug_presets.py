"""Preset data for emergency drugs used in DIRC.

These presets are intentionally simple and focus on common ICU vasopressors
and inotropes with typical ampoule strengths and recommended dose ranges.
"""

from __future__ import annotations

from typing import Dict, List, TypedDict, Optional


class VialInfo(TypedDict):
    label: str          # e.g. "4 mg/4 mL"
    amount_mg: float    # total drug in mg
    volume_ml: float    # ampoule volume in mL


class DoseRange(TypedDict, total=False):
    min_mcg_kg_min: float
    max_mcg_kg_min: float
    note: str


class DrugPreset(TypedDict):
    name: str
    category: str
    vials: List[VialInfo]
    dose_range: DoseRange


EMERGENCY_DRUG_PRESETS: Dict[str, DrugPreset] = {
    "Norepinephrine": {
        "name": "Norepinephrine (Noradrenalin)",
        "category": "Vasopressor",
        "vials": [
            {"label": "4 mg/4 mL", "amount_mg": 4.0, "volume_ml": 4.0},
            {"label": "8 mg/4 mL", "amount_mg": 8.0, "volume_ml": 4.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.02,
            "max_mcg_kg_min": 1.0,
            "note": "Thường khởi đầu 0.02–0.05 mcg/kg/phút, tối đa ~1 mcg/kg/phút.",
        },
    },
    "Dopamine": {
        "name": "Dopamine",
        "category": "Inotrope/Vasopressor",
        "vials": [
            {"label": "200 mg/5 mL", "amount_mg": 200.0, "volume_ml": 5.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 2.0,
            "max_mcg_kg_min": 20.0,
            "note": "2–5: inotrope nhẹ; 5–10: beta; 10–20: alpha chiếm ưu thế.",
        },
    },
    "Dobutamine": {
        "name": "Dobutamine",
        "category": "Inotrope",
        "vials": [
            {"label": "250 mg/5 mL", "amount_mg": 250.0, "volume_ml": 5.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 2.0,
            "max_mcg_kg_min": 20.0,
            "note": "Thường 2–20 mcg/kg/phút, titrate theo đáp ứng.",
        },
    },
    "Epinephrine": {
        "name": "Epinephrine (Adrenalin)",
        "category": "Vasopressor/Inotrope",
        "vials": [
            {"label": "1 mg/1 mL (1:1000)", "amount_mg": 1.0, "volume_ml": 1.0},
            {"label": "1 mg/10 mL (1:10000)", "amount_mg": 1.0, "volume_ml": 10.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.01,
            "max_mcg_kg_min": 1.0,
            "note": "Thường 0.01–0.5 mcg/kg/phút; có thể cao hơn trong sốc nặng.",
        },
    },
    "Phenylephrine": {
        "name": "Phenylephrine",
        "category": "Vasopressor",
        "vials": [
            {"label": "10 mg/1 mL", "amount_mg": 10.0, "volume_ml": 1.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.2,
            "max_mcg_kg_min": 5.0,
            "note": "Thường 0.2–3 mcg/kg/phút, chỉnh liều theo huyết áp và mạch.",
        },
    },
    "Milrinone": {
        "name": "Milrinone",
        "category": "Inotrope/Vasodilator",
        "vials": [
            {"label": "10 mg/10 mL", "amount_mg": 10.0, "volume_ml": 10.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.25,
            "max_mcg_kg_min": 0.75,
            "note": "Thường 0.25–0.75 mcg/kg/phút sau liều tấn công (nếu dùng).",
        },
    },
    "Nitroprusside": {
        "name": "Sodium Nitroprusside",
        "category": "Vasodilator",
        "vials": [
            {"label": "50 mg/2 mL", "amount_mg": 50.0, "volume_ml": 2.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.3,
            "max_mcg_kg_min": 10.0,
            "note": "Thường 0.3–10 mcg/kg/phút; tránh liều cao kéo dài do nguy cơ ngộ độc cyanid.",
        },
    },
    "Nitroglycerin": {
        "name": "Nitroglycerin (Glyceryl trinitrate)",
        "category": "Vasodilator",
        "vials": [
            {"label": "50 mg/10 mL", "amount_mg": 50.0, "volume_ml": 10.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.5,
            "max_mcg_kg_min": 10.0,
            "note": "Thường 0.5–10 mcg/kg/phút; bắt đầu thấp và tăng dần theo huyết áp / triệu chứng.",
        },
    },
    "Vasopressin": {
        "name": "Vasopressin",
        "category": "Vasopressor",
        "vials": [
            {"label": "20 units/1 mL", "amount_mg": 20.0, "volume_ml": 1.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.0,
            "max_mcg_kg_min": 0.0,
            "note": "Thường tính theo đơn vị/phút (0.01–0.04 units/phút); dùng preset chủ yếu để tính nồng độ trong bơm.",
        },
    },
    "Amiodarone": {
        "name": "Amiodarone",
        "category": "Antiarrhythmic",
        "vials": [
            {"label": "150 mg/3 mL", "amount_mg": 150.0, "volume_ml": 3.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.0,
            "max_mcg_kg_min": 0.0,
            "note": "Truyền duy trì thường 0.5–1 mg/phút sau liều tấn công; không chuẩn hóa theo mcg/kg/phút.",
        },
    },
    "Lidocaine": {
        "name": "Lidocaine",
        "category": "Antiarrhythmic/Local anesthetic",
        "vials": [
            {"label": "100 mg/5 mL (2%)", "amount_mg": 100.0, "volume_ml": 5.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.0,
            "max_mcg_kg_min": 0.0,
            "note": "Truyền duy trì thường 1–4 mg/phút sau bolus; dùng preset chủ yếu để tính nồng độ.",
        },
    },
    "MagnesiumSulfate": {
        "name": "Magnesium sulfate",
        "category": "Electrolyte/Emergency",
        "vials": [
            {"label": "10 g/100 mL (10%)", "amount_mg": 10000.0, "volume_ml": 100.0},
        ],
        "dose_range": {
            "min_mcg_kg_min": 0.0,
            "max_mcg_kg_min": 0.0,
            "note": "Thường truyền theo mg/kg trong thời gian nhất định (Torsades, sản giật); không chuẩn hóa mcg/kg/phút.",
        },
    },
}


def get_drug_names() -> List[str]:
    """Return list of human‑readable drug names for UI."""
    return [preset["name"] for preset in EMERGENCY_DRUG_PRESETS.values()]


def find_drug_key_by_name(name: str) -> Optional[str]:
    """Map display name back to internal key."""
    for key, preset in EMERGENCY_DRUG_PRESETS.items():
        if preset["name"] == name:
            return key
    return None


def get_vial_labels_for_drug(drug_key: str) -> List[str]:
    """Return list of vial labels for a given drug key."""
    drug = EMERGENCY_DRUG_PRESETS.get(drug_key)
    if not drug:
        return []
    return [v["label"] for v in drug["vials"]]


def get_vial_info(drug_key: str, vial_label: str) -> Optional[VialInfo]:
    """Return vial info for a specific drug and vial label."""
    drug = EMERGENCY_DRUG_PRESETS.get(drug_key)
    if not drug:
        return None
    for vial in drug["vials"]:
        if vial["label"] == vial_label:
            return vial
    return None



