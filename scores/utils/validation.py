"""
Validation utilities for calculators
Common validation functions to ensure input safety
"""

from typing import Optional, Tuple


def validate_age(age: float, min_age: int = 0, max_age: int = 120) -> Tuple[bool, Optional[str]]:
    """
    Validate age input
    
    Args:
        age: Age value
        min_age: Minimum valid age
        max_age: Maximum valid age
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if age < min_age:
        return False, f"Tuổi phải ≥ {min_age}"
    if age > max_age:
        return False, f"Tuổi phải ≤ {max_age}"
    return True, None


def validate_positive(value: float, name: str = "Giá trị") -> Tuple[bool, Optional[str]]:
    """
    Validate that value is positive
    
    Args:
        value: Value to validate
        name: Name of the value for error message
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if value < 0:
        return False, f"{name} phải ≥ 0"
    return True, None


def validate_range(
    value: float,
    min_val: float,
    max_val: float,
    name: str = "Giá trị"
) -> Tuple[bool, Optional[str]]:
    """
    Validate that value is within range
    
    Args:
        value: Value to validate
        min_val: Minimum valid value
        max_val: Maximum valid value
        name: Name of the value for error message
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if value < min_val:
        return False, f"{name} phải ≥ {min_val}"
    if value > max_val:
        return False, f"{name} phải ≤ {max_val}"
    return True, None


def validate_gcs(gcs: int) -> Tuple[bool, Optional[str]]:
    """
    Validate GCS score
    
    Args:
        gcs: GCS value
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if gcs < 3 or gcs > 15:
        return False, "GCS phải từ 3-15"
    return True, None


def validate_blood_pressure(sbp: float, dbp: Optional[float] = None) -> Tuple[bool, Optional[str]]:
    """
    Validate blood pressure values
    
    Args:
        sbp: Systolic blood pressure
        dbp: Diastolic blood pressure (optional)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if sbp < 0 or sbp > 300:
        return False, "Huyết áp tâm thu phải từ 0-300 mmHg"
    
    if dbp is not None:
        if dbp < 0 or dbp > 200:
            return False, "Huyết áp tâm trương phải từ 0-200 mmHg"
        if dbp > sbp:
            return False, "Huyết áp tâm trương không thể lớn hơn tâm thu"
    
    return True, None


def validate_heart_rate(hr: float) -> Tuple[bool, Optional[str]]:
    """
    Validate heart rate
    
    Args:
        hr: Heart rate value
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if hr < 0 or hr > 300:
        return False, "Nhịp tim phải từ 0-300 /phút"
    return True, None


def validate_respiratory_rate(rr: float) -> Tuple[bool, Optional[str]]:
    """
    Validate respiratory rate
    
    Args:
        rr: Respiratory rate value
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if rr < 0 or rr > 100:
        return False, "Nhịp thở phải từ 0-100 /phút"
    return True, None


def validate_temperature(temp: float, unit: str = "celsius") -> Tuple[bool, Optional[str]]:
    """
    Validate temperature
    
    Args:
        temp: Temperature value
        unit: Unit of temperature ("celsius" or "fahrenheit")
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if unit == "celsius":
        if temp < 20 or temp > 50:
            return False, "Nhiệt độ phải từ 20-50°C"
    else:  # fahrenheit
        if temp < 68 or temp > 122:
            return False, "Nhiệt độ phải từ 68-122°F"
    return True, None


def validate_lab_value(
    value: float,
    name: str,
    min_val: float = 0.0,
    max_val: float = 1000.0
) -> Tuple[bool, Optional[str]]:
    """
    Validate laboratory value
    
    Args:
        value: Lab value
        name: Name of the lab value
        min_val: Minimum valid value
        max_val: Maximum valid value
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if value < min_val:
        return False, f"{name} phải ≥ {min_val}"
    if value > max_val:
        return False, f"{name} phải ≤ {max_val}"
    return True, None


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Safe division with default value if denominator is zero
    
    Args:
        numerator: Numerator
        denominator: Denominator
        default: Default value if denominator is zero
    
    Returns:
        Result of division or default value
    """
    if denominator == 0:
        return default
    return numerator / denominator


def validate_ratio(
    numerator: float,
    denominator: float,
    name: str = "Tỷ lệ"
) -> Tuple[bool, Optional[str], Optional[float]]:
    """
    Validate and calculate ratio safely
    
    Args:
        numerator: Numerator
        denominator: Denominator
        name: Name of the ratio
    
    Returns:
        Tuple of (is_valid, error_message, ratio_value)
    """
    if denominator == 0:
        return False, f"{name}: Mẫu số không thể bằng 0", None
    
    ratio = numerator / denominator
    return True, None, ratio


def validate_input_range(
    value: float,
    name: str,
    min_val: float,
    max_val: float,
    unit: str = ""
) -> Tuple[bool, Optional[str]]:
    """
    Validate input range with unit support
    
    Args:
        value: Input value
        name: Name of the input
        min_val: Minimum value
        max_val: Maximum value
        unit: Unit string (optional)
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if value < min_val:
        return False, f"{name} phải ≥ {min_val} {unit}".strip()
    if value > max_val:
        return False, f"{name} phải ≤ {max_val} {unit}".strip()
    return True, None


def validate_weight(
    weight: float,
    min_val: float = 0.0,
    max_val: float = 600.0
) -> Tuple[bool, Optional[str]]:
    """
    Validate weight
    
    Args:
        weight: Weight in kg
        min_val: Minimum weight
        max_val: Maximum weight
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if weight < min_val or weight > max_val:
        return False, f"Cân nặng phải từ {min_val}-{max_val} kg"
    return True, None


