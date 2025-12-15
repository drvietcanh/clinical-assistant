"""
Validation utilities specifically for anesthesiology scoring systems
"""

from typing import Optional, Tuple


def validate_ponv_risk_factors(
    female: bool,
    non_smoker: bool,
    history_ponv: bool,
    opioids: bool
) -> Tuple[bool, Optional[str]]:
    """
    Validate PONV risk factors (basic check)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    # All are boolean, so always valid
    return True, None


def validate_wilson_score(
    weight: int,
    head_neck_movement: int,
    jaw_movement: int,
    receding_mandible: int,
    buck_teeth: int
) -> Tuple[bool, Optional[str]]:
    """
    Validate Wilson Risk Score components
    
    Args:
        weight: 0-2
        head_neck_movement: 0-2
        jaw_movement: 0-2
        receding_mandible: 0-2
        buck_teeth: 0-2
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    components = [
        ("Cân nặng", weight, 0, 2),
        ("Cử động đầu cổ", head_neck_movement, 0, 2),
        ("Cử động hàm", jaw_movement, 0, 2),
        ("Hàm lùi", receding_mandible, 0, 2),
        ("Răng hô", buck_teeth, 0, 2)
    ]
    
    for name, value, min_val, max_val in components:
        if not (min_val <= value <= max_val):
            return False, f"{name} phải từ {min_val}-{max_val}"
    
    return True, None


def validate_el_ganzouri_score(
    mouth_opening: int,
    thyromental_distance: int,
    mallampati: int,
    neck_movement: int,
    jaw_protrusion: int,
    weight: int,
    history_difficult_intubation: int
) -> Tuple[bool, Optional[str]]:
    """
    Validate El-Ganzouri Risk Index components
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    components = [
        ("Mở miệng", mouth_opening, 0, 2),
        ("Khoảng cách thyromental", thyromental_distance, 0, 2),
        ("Mallampati", mallampati, 0, 2),
        ("Cử động cổ", neck_movement, 0, 2),
        ("Đưa hàm ra", jaw_protrusion, 0, 2),
        ("Cân nặng", weight, 0, 1),
        ("Tiền sử đặt NKQ khó", history_difficult_intubation, 0, 1)
    ]
    
    for name, value, min_val, max_val in components:
        if not (min_val <= value <= max_val):
            return False, f"{name} phải từ {min_val}-{max_val}"
    
    return True, None


def validate_surgery_duration(duration: float) -> Tuple[bool, Optional[str]]:
    """
    Validate surgery duration in minutes
    
    Args:
        duration: Duration in minutes
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if duration < 0:
        return False, "Thời gian phẫu thuật phải ≥ 0 phút"
    if duration > 600:  # 10 hours max
        return False, "Thời gian phẫu thuật phải ≤ 600 phút (10 giờ)"
    return True, None


def validate_ramsay_score(score: int) -> Tuple[bool, Optional[str]]:
    """
    Validate Ramsay Sedation Scale score
    
    Args:
        score: Ramsay score (1-6)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not (1 <= score <= 6):
        return False, "Ramsay Score phải từ 1-6"
    return True, None


def validate_rass_score(score: int) -> Tuple[bool, Optional[str]]:
    """
    Validate RASS score
    
    Args:
        score: RASS score (-5 to +4)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not (-5 <= score <= 4):
        return False, "RASS Score phải từ -5 đến +4"
    return True, None


def validate_riker_sas_score(score: int) -> Tuple[bool, Optional[str]]:
    """
    Validate Riker SAS score
    
    Args:
        score: Riker SAS score (1-7)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not (1 <= score <= 7):
        return False, "Riker SAS Score phải từ 1-7"
    return True, None


def validate_padss_components(
    vitals: int,
    ambulation: int,
    nausea_vomiting: int,
    pain: int,
    bleeding: int
) -> Tuple[bool, Optional[str]]:
    """
    Validate PADSS components
    
    Args:
        All components should be 0-2
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    components = [
        ("Dấu hiệu sinh tồn", vitals, 0, 2),
        ("Đi lại", ambulation, 0, 2),
        ("Buồn nôn nôn", nausea_vomiting, 0, 2),
        ("Đau", pain, 0, 2),
        ("Chảy máu", bleeding, 0, 2)
    ]
    
    for name, value, min_val, max_val in components:
        if not (min_val <= value <= max_val):
            return False, f"{name} phải từ {min_val}-{max_val}"
    
    return True, None


def validate_ariscat_components(
    age: int,
    spo2: int,
    respiratory_infection: int,
    anemia: int,
    surgical_incision: int,
    duration_surgery: int,
    emergency: int
) -> Tuple[bool, Optional[str]]:
    """
    Validate ARISCAT components
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    components = [
        ("Tuổi", age, 0, 2),
        ("SpO₂", spo2, 0, 2),
        ("Nhiễm trùng hô hấp", respiratory_infection, 0, 1),
        ("Thiếu máu", anemia, 0, 1),
        ("Vị trí đường mổ", surgical_incision, 0, 1),
        ("Thời gian phẫu thuật", duration_surgery, 0, 2),
        ("Phẫu thuật cấp cứu", emergency, 0, 1)
    ]
    
    for name, value, min_val, max_val in components:
        if not (min_val <= value <= max_val):
            return False, f"{name} phải từ {min_val}-{max_val}"
    
    return True, None


def validate_cormack_lehane_grade(grade: int) -> Tuple[bool, Optional[str]]:
    """
    Validate Cormack-Lehane grade
    
    Args:
        grade: Grade (1-4)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not (1 <= grade <= 4):
        return False, "Cormack-Lehane Grade phải từ 1-4"
    return True, None


def validate_4at_components(
    alertness: int,
    amt4: int,
    attention: int,
    acute_change: int
) -> Tuple[bool, Optional[str]]:
    """
    Validate 4AT components
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    components = [
        ("Alertness", alertness, 0, 2),
        ("AMT4", amt4, 0, 1),
        ("Attention", attention, 0, 1),
        ("Acute Change", acute_change, 0, 1)
    ]
    
    for name, value, min_val, max_val in components:
        if not (min_val <= value <= max_val):
            return False, f"{name} phải từ {min_val}-{max_val}"
    
    return True, None


def validate_spo2(spo2: float) -> Tuple[bool, Optional[str]]:
    """
    Validate SpO2 value
    
    Args:
        spo2: SpO2 percentage (0-100)
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not (0 <= spo2 <= 100):
        return False, "SpO₂ phải từ 0-100%"
    return True, None

