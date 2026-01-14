"""
Vietnam Drug Formulary (starter)

Lightweight mapping for a few common drugs to demonstrate VN coverage
and formulary status (BHYT, generic substitution, approximate cost).
Extend this file incrementally with real data.
"""

from typing import Optional, Dict, Any

# Simple static dataset keyed by generic name (lowercase)
FORMULARY_VN: Dict[str, Dict[str, Any]] = {
    "metformin": {
        "bhyt": True,
        "generic_substitution": True,
        "cost_vnd": 500,  # per 500mg tab (approx)
        "cost_range_vnd": "400-800 VND/viên 500mg",
        "note": "Sẵn trong danh mục BHYT; ưu tiên generic đạt GMP-WHO.",
        "generic_examples": ["Metformin STADA", "Metformin Domesco"],
        "brand_examples": ["Glucophage"],
        "hospital_formulary": ["Bạch Mai", "Chợ Rẫy", "108", "Nhi Đồng", "YTDT HCM"],
    },
    "losartan": {
        "bhyt": True,
        "generic_substitution": True,
        "cost_vnd": 1200,  # per 50mg tab (approx)
        "cost_range_vnd": "1,000-2,000 VND/viên 50mg",
        "note": "Thuốc nhóm ARB phổ biến; có nhiều biệt dược/generic.",
        "generic_examples": ["Losartan DHG", "Losartan Domesco"],
        "brand_examples": ["Cozaar"],
        "hospital_formulary": ["Bạch Mai", "Chợ Rẫy", "YTDT HCM", "Đa khoa tỉnh"],
    },
    "atorvastatin": {
        "bhyt": True,
        "generic_substitution": True,
        "cost_vnd": 1500,  # per 20mg tab (approx)
        "cost_range_vnd": "1,200-2,500 VND/viên 20mg",
        "note": "Có trong BHYT theo mức trần; giá thay đổi theo hàm lượng.",
        "generic_examples": ["Atorvastatin STADA", "Atorvastatin DHG"],
        "brand_examples": ["Lipitor"],
        "hospital_formulary": ["Bạch Mai", "Chợ Rẫy", "108", "Đa khoa tỉnh"],
    },
    "insulin glargine": {
        "bhyt": False,
        "generic_substitution": False,
        "cost_vnd": 120000,  # per 100IU pen (approx, out-of-pocket)
        "cost_range_vnd": "90,000-140,000 VND/bút 100IU",
        "note": "Thường phải đồng chi trả / tự chi; kiểm tra tồn kho trước.",
        "generic_examples": [],
        "brand_examples": ["Lantus", "Basaglar"],
        "hospital_formulary": ["Chợ Rẫy", "108", "YTDT HCM"],
    },
}


def get_formulary_info(drug_name: str) -> Optional[Dict[str, Any]]:
    """Return formulary info by generic name (case-insensitive)."""
    if not drug_name:
        return None
    key = drug_name.strip().lower()
    return FORMULARY_VN.get(key)

