"""
Infusion Safety Checker
Comprehensive safety checks for infusion calculations
"""

from typing import Dict, List, Optional
from drugs.cardiovascular_calculator import (
    get_drug_info,
    validate_dose_range,
    calculate_complete_infusion
)


class SafetyCheckResult:
    """Result of a safety check."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        self.score = 100  # Start with perfect score
    
    def add_error(self, message: str, points: int = 20):
        """Add an error (reduces score significantly)."""
        self.errors.append(message)
        self.score -= points
    
    def add_warning(self, message: str, points: int = 10):
        """Add a warning (reduces score moderately)."""
        self.warnings.append(message)
        self.score -= points
    
    def add_info(self, message: str):
        """Add informational message (no score change)."""
        self.info.append(message)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
            "score": max(0, min(100, self.score)),
            "is_safe": len(self.errors) == 0,
            "has_warnings": len(self.warnings) > 0
        }


def check_dose_safety(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float
) -> SafetyCheckResult:
    """
    Check dose safety.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
    
    Returns:
        SafetyCheckResult
    """
    result = SafetyCheckResult()
    
    # Get drug info
    drug_info = get_drug_info(drug_name)
    if not drug_info:
        result.add_error(f"Không tìm thấy thông tin thuốc '{drug_name}'")
        return result
    
    # Validate dose range
    validation = validate_dose_range(drug_name, dose_mcg_kg_min)
    if not validation.get("is_valid", True):
        result.add_error(validation.get("warning", "Liều không hợp lệ"))
    
    # Check max dose
    max_dose_str = drug_info.get("max_dose", "")
    try:
        # Parse max dose (e.g., "1–2 mcg/kg/min" -> 2)
        max_dose_parts = max_dose_str.split("–")
        if len(max_dose_parts) > 1:
            max_dose = float(max_dose_parts[-1].split()[0])
        else:
            max_dose = float(max_dose_str.split()[0])
        
        if dose_mcg_kg_min > max_dose:
            result.add_error(f"Liều {dose_mcg_kg_min:.2f} mcg/kg/phút vượt quá liều tối đa {max_dose} mcg/kg/phút")
        elif dose_mcg_kg_min > max_dose * 0.8:
            result.add_warning(f"Liều {dose_mcg_kg_min:.2f} mcg/kg/phút gần đạt liều tối đa {max_dose} mcg/kg/phút")
    except (ValueError, IndexError):
        pass
    
    # Check weight
    if weight_kg <= 0:
        result.add_error("Cân nặng phải > 0")
    elif weight_kg < 1:
        result.add_warning("Cân nặng rất thấp (< 1kg) - Kiểm tra lại")
    elif weight_kg > 200:
        result.add_warning("Cân nặng rất cao (> 200kg) - Có thể cần điều chỉnh liều")
    
    # Calculate total dose
    total_dose_mcg_hour = dose_mcg_kg_min * weight_kg * 60
    if total_dose_mcg_hour > 100000:  # 100 mg/hour
        result.add_warning(f"Tổng liều rất cao: {total_dose_mcg_hour/1000:.1f} mg/giờ")
    
    return result


def check_rate_safety(
    infusion_rate_ml_hour: float,
    infusion_method: str,
    volume_ml: float = None
) -> SafetyCheckResult:
    """
    Check infusion rate safety.
    
    Args:
        infusion_rate_ml_hour: Infusion rate in ml/hour
        infusion_method: Infusion method
        volume_ml: Optional volume in bag/syringe
    
    Returns:
        SafetyCheckResult
    """
    result = SafetyCheckResult()
    
    # Rate limits
    max_rate_syringe = 200  # ml/hour for syringe pump
    max_rate_iv_bag = 1000  # ml/hour for IV bag
    
    if infusion_method == "syringe_pump_50ml" or infusion_method == "syringe_pump_20ml":
        max_rate = max_rate_syringe
        if infusion_rate_ml_hour > max_rate:
            result.add_error(f"Tốc độ truyền {infusion_rate_ml_hour:.1f} ml/h vượt quá giới hạn {max_rate} ml/h cho bơm tiêm")
        elif infusion_rate_ml_hour > max_rate * 0.8:
            result.add_warning(f"Tốc độ truyền {infusion_rate_ml_hour:.1f} ml/h gần đạt giới hạn {max_rate} ml/h")
    else:  # IV bag
        max_rate = max_rate_iv_bag
        if infusion_rate_ml_hour > max_rate:
            result.add_error(f"Tốc độ truyền {infusion_rate_ml_hour:.1f} ml/h vượt quá giới hạn {max_rate} ml/h cho chai truyền")
        elif infusion_rate_ml_hour > max_rate * 0.8:
            result.add_warning(f"Tốc độ truyền {infusion_rate_ml_hour:.1f} ml/h gần đạt giới hạn {max_rate} ml/h")
    
    # Check if rate is too low
    if infusion_rate_ml_hour < 0.1:
        result.add_warning("Tốc độ truyền rất thấp (< 0.1 ml/h) - Khó kiểm soát chính xác")
    
    # Check volume vs rate
    if volume_ml:
        time_hours = volume_ml / infusion_rate_ml_hour if infusion_rate_ml_hour > 0 else 0
        if time_hours > 48:
            result.add_warning(f"Thời gian truyền rất dài ({time_hours:.1f} giờ) - Cần thay dịch mới")
        elif time_hours < 0.1:
            result.add_warning(f"Thời gian truyền rất ngắn ({time_hours*60:.1f} phút) - Kiểm tra lại")
    
    return result


def check_complete_infusion_safety(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    drop_factor: Optional[int] = None
) -> SafetyCheckResult:
    """
    Perform complete safety check for an infusion.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: Infusion method
        drop_factor: Optional drop factor
    
    Returns:
        SafetyCheckResult with all checks
    """
    result = SafetyCheckResult()
    
    # Check dose safety
    dose_check = check_dose_safety(drug_name, dose_mcg_kg_min, weight_kg)
    result.errors.extend(dose_check.errors)
    result.warnings.extend(dose_check.warnings)
    result.info.extend(dose_check.info)
    result.score = min(result.score, dose_check.score)
    
    # Calculate infusion to get rate
    try:
        infusion_result = calculate_complete_infusion(
            drug_name, dose_mcg_kg_min, weight_kg, infusion_method, drop_factor
        )
        
        infusion_rate = infusion_result.get("infusion_rate_ml_hour", 0)
        volume_ml = infusion_result.get("volume_ml", 0)
        
        # Check rate safety
        rate_check = check_rate_safety(infusion_rate, infusion_method, volume_ml)
        result.errors.extend(rate_check.errors)
        result.warnings.extend(rate_check.warnings)
        result.info.extend(rate_check.info)
        result.score = min(result.score, rate_check.score)
        
        # Additional checks
        if infusion_rate > 0:
            result.add_info(f"Tốc độ truyền: {infusion_rate:.2f} ml/h")
            result.add_info(f"Thể tích: {volume_ml:.0f} ml")
            
            if volume_ml > 0:
                time_hours = volume_ml / infusion_rate
                result.add_info(f"Thời gian truyền: {time_hours:.1f} giờ")
    
    except Exception as e:
        result.add_warning(f"Không thể tính toán đầy đủ: {str(e)}")
    
    return result


def get_safety_checklist() -> List[Dict]:
    """
    Get safety checklist items.
    
    Returns:
        List of checklist items
    """
    return [
        {
            "item": "Đúng thuốc",
            "description": "Kiểm tra tên thuốc trước khi pha",
            "critical": True
        },
        {
            "item": "Đúng bệnh nhân",
            "description": "Xác nhận đúng bệnh nhân trước khi truyền",
            "critical": True
        },
        {
            "item": "Đúng liều",
            "description": "Kiểm tra liều dùng đã tính toán",
            "critical": True
        },
        {
            "item": "Đúng nồng độ pha",
            "description": "Kiểm tra nồng độ pha đã đúng",
            "critical": True
        },
        {
            "item": "Đúng tốc độ",
            "description": "Kiểm tra tốc độ truyền đã đúng",
            "critical": True
        },
        {
            "item": "Kiểm tra tương thích",
            "description": "Kiểm tra tương thích nếu trộn thuốc",
            "critical": False
        },
        {
            "item": "Theo dõi sát",
            "description": "Theo dõi sát huyết áp, nhịp tim, tưới máu",
            "critical": False
        },
        {
            "item": "Ghi chép",
            "description": "Ghi chép lại liều và thời gian",
            "critical": False
        }
    ]

