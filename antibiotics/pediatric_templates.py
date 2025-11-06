"""
Pediatric Dosing Templates - Phase 5
Template sẵn cho pediatric với age-based adjustments
"""

from typing import Dict, Optional, Tuple, List

# Age-based pediatric dosing templates
# Format: {age_range: {weight_range: dosing_info}}
PEDIATRIC_TEMPLATES = {
    "neonate": {
        "age_range": (0, 28),  # days
        "weight_range": (0.5, 4.0),  # kg
        "notes": "Trẻ sơ sinh - Cần điều chỉnh đặc biệt, thận trọng với độc tính"
    },
    "infant": {
        "age_range": (29, 365),  # days (1-12 months)
        "weight_range": (4.0, 10.0),  # kg
        "notes": "Trẻ nhũ nhi - Chức năng thận chưa hoàn thiện"
    },
    "toddler": {
        "age_range": (365, 1095),  # days (1-3 years)
        "weight_range": (10.0, 15.0),  # kg
        "notes": "Trẻ mới biết đi - Tăng liều theo cân nặng"
    },
    "preschool": {
        "age_range": (1095, 2190),  # days (3-6 years)
        "weight_range": (15.0, 20.0),  # kg
        "notes": "Trẻ mẫu giáo - Liều dựa trên cân nặng"
    },
    "school_age": {
        "age_range": (2190, 4380),  # days (6-12 years)
        "weight_range": (20.0, 40.0),  # kg
        "notes": "Trẻ tuổi học đường - Gần với liều người lớn"
    },
    "adolescent": {
        "age_range": (4380, 6570),  # days (12-18 years)
        "weight_range": (40.0, 70.0),  # kg
        "notes": "Thanh thiếu niên - Có thể dùng liều người lớn nếu đủ cân nặng"
    }
}


def get_pediatric_age_category(age_days: int) -> Optional[str]:
    """
    Xác định nhóm tuổi pediatric
    
    Args:
        age_days: Tuổi tính bằng ngày
    
    Returns:
        Category name hoặc None nếu không phải pediatric
    """
    for category, info in PEDIATRIC_TEMPLATES.items():
        age_min, age_max = info["age_range"]
        if age_min <= age_days <= age_max:
            return category
    
    return None


def get_pediatric_age_category_from_years(age_years: float) -> Optional[str]:
    """
    Xác định nhóm tuổi pediatric từ số năm
    
    Args:
        age_years: Tuổi tính bằng năm
    
    Returns:
        Category name hoặc None nếu không phải pediatric
    """
    age_days = int(age_years * 365.25)
    return get_pediatric_age_category(age_days)


def get_pediatric_dosing_adjustment(age_years: float, weight_kg: float) -> Dict:
    """
    Tính toán điều chỉnh liều cho pediatric
    
    Args:
        age_years: Tuổi (năm)
        weight_kg: Cân nặng (kg)
    
    Returns:
        Dict với adjustment info
    """
    age_days = int(age_years * 365.25)
    category = get_pediatric_age_category(age_days)
    
    if not category:
        return {
            "is_pediatric": False,
            "category": None,
            "adjustment_factor": 1.0,
            "notes": "Người lớn"
        }
    
    template = PEDIATRIC_TEMPLATES[category]
    
    # Age-based adjustment factors (simplified)
    # Trẻ càng nhỏ, cần điều chỉnh nhiều hơn
    adjustment_factors = {
        "neonate": 0.5,  # Giảm 50% so với liều chuẩn
        "infant": 0.7,   # Giảm 30%
        "toddler": 0.85, # Giảm 15%
        "preschool": 0.9, # Giảm 10%
        "school_age": 0.95, # Giảm 5%
        "adolescent": 1.0  # Không điều chỉnh
    }
    
    adjustment_factor = adjustment_factors.get(category, 1.0)
    
    return {
        "is_pediatric": True,
        "category": category,
        "age_days": age_days,
        "adjustment_factor": adjustment_factor,
        "notes": template["notes"],
        "weight_range": template["weight_range"]
    }


def format_pediatric_category(category: str) -> str:
    """
    Format category name thành tiếng Việt
    """
    category_map = {
        "neonate": "Trẻ sơ sinh (0-28 ngày)",
        "infant": "Trẻ nhũ nhi (1-12 tháng)",
        "toddler": "Trẻ mới biết đi (1-3 tuổi)",
        "preschool": "Trẻ mẫu giáo (3-6 tuổi)",
        "school_age": "Trẻ tuổi học đường (6-12 tuổi)",
        "adolescent": "Thanh thiếu niên (12-18 tuổi)"
    }
    
    return category_map.get(category, category)


def get_pediatric_warnings(age_years: float, antibiotic_name: str) -> List[str]:
    """
    Lấy cảnh báo đặc biệt cho pediatric
    
    Args:
        age_years: Tuổi (năm)
        antibiotic_name: Tên kháng sinh
    
    Returns:
        List of warning messages
    """
    warnings = []
    age_days = int(age_years * 365.25)
    category = get_pediatric_age_category(age_days)
    
    if not category:
        return warnings
    
    # Age-specific warnings
    if category == "neonate":
        warnings.append("⚠️ Trẻ sơ sinh: Chức năng thận và gan chưa hoàn thiện. Cần điều chỉnh liều đặc biệt.")
        warnings.append("⚠️ Theo dõi sát nồng độ thuốc và chức năng thận/gan.")
    
    if category in ["neonate", "infant"]:
        warnings.append("⚠️ Trẻ nhỏ: Nguy cơ độc tính cao hơn. Cần theo dõi chặt chẽ.")
    
    # Drug-specific warnings
    if "Tetracycline" in antibiotic_name or "Doxycycline" in antibiotic_name:
        if age_years < 8:
            warnings.append("🚨 CHỐNG CHỈ ĐỊNH: Tetracycline/Doxycycline không dùng cho trẻ <8 tuổi (ố vàng răng)")
    
    if "Fluoroquinolone" in antibiotic_name or "Ciprofloxacin" in antibiotic_name:
        if age_years < 18:
            warnings.append("⚠️ Cảnh báo: Fluoroquinolone không khuyến cáo cho trẻ <18 tuổi (nguy cơ tổn thương sụn)")
    
    if "Sulfonamide" in antibiotic_name and category == "neonate":
        warnings.append("⚠️ Cảnh báo: Sulfonamide không khuyến cáo cho trẻ sơ sinh (nguy cơ vàng da nhân)")
    
    return warnings

