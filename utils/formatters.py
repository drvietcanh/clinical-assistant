"""
Standardized Formatters for Clinical Values
Chuẩn hóa format các giá trị lâm sàng: tuổi, cân nặng, chiều cao, lab values, etc.
"""

from typing import Optional, Union
import streamlit as st


# ============================================================================
# FORMAT FUNCTIONS - Format giá trị khi hiển thị
# ============================================================================

def format_age(age: Union[int, float]) -> str:
    """
    Format tuổi - số nguyên (không có số thập phân)
    
    Args:
        age: Tuổi (int hoặc float)
    
    Returns:
        String đã format (ví dụ: "65" không phải "65.0")
    
    Example:
        >>> format_age(65.5)
        '65'
        >>> format_age(65)
        '65'
    """
    return str(int(round(age)))


def format_weight(weight: float, decimals: int = 1) -> str:
    """
    Format cân nặng - mặc định 1 số thập phân, nhưng nếu là số nguyên thì không hiển thị .0
    
    Args:
        weight: Cân nặng (kg)
        decimals: Số chữ số thập phân (mặc định 1)
    
    Returns:
        String đã format (ví dụ: "70" hoặc "70.5")
    
    Example:
        >>> format_weight(70.0)
        '70'
        >>> format_weight(70.5)
        '70.5'
        >>> format_weight(70.25, decimals=2)
        '70.25'
    """
    if decimals == 0:
        return str(int(round(weight)))
    
    # Làm tròn đến số thập phân cần thiết
    rounded = round(weight, decimals)
    
    # Nếu sau khi làm tròn là số nguyên, không hiển thị .0
    if rounded == int(rounded):
        return str(int(rounded))
    
    # Format với số thập phân
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def format_height(height: Union[int, float]) -> str:
    """
    Format chiều cao - số nguyên (không có số thập phân)
    
    Args:
        height: Chiều cao (cm)
    
    Returns:
        String đã format (ví dụ: "170" không phải "170.0")
    
    Example:
        >>> format_height(170.5)
        '170'
        >>> format_height(170)
        '170'
    """
    return str(int(round(height)))


def format_lab_value(value: float, decimals: int = 1) -> str:
    """
    Format giá trị lab - mặc định 1 số thập phân, **luôn hiển thị đúng số chữ số thập phân yêu cầu**.
    
    Args:
        value: Giá trị lab
        decimals: Số chữ số thập phân (mặc định 1, có thể 2 cho một số lab)
    
    Returns:
        String đã format với đúng số chữ số thập phân
    
    Example:
        >>> format_lab_value(100.5)
        '100.5'
        >>> format_lab_value(100.0)
        '100.0'
        >>> format_lab_value(100.25, decimals=2)
        '100.25'
        >>> format_lab_value(100.0, decimals=2)
        '100.00'
    """
    return format_number(value, decimals=decimals, remove_trailing_zeros=False)


def format_percentage(value: float, decimals: int = 1) -> str:
    """
    Format phần trăm
    
    Args:
        value: Giá trị phần trăm (0-100)
        decimals: Số chữ số thập phân
    
    Returns:
        String đã format với dấu %
    
    Example:
        >>> format_percentage(95.5)
        '95.5%'
    """
    return f"{value:.{decimals}f}%"


def format_volume(value: float, decimals: int = 0) -> str:
    """
    Format thể tích (mL, L)
    
    Args:
        value: Thể tích
        decimals: Số chữ số thập phân
    
    Returns:
        String đã format
    
    Example:
        >>> format_volume(100.5)
        '101'
        >>> format_volume(100.5, decimals=1)
        '100.5'
    """
    if decimals == 0:
        return str(int(round(value)))
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def format_dose(value: float, decimals: int = 1) -> str:
    """
    Format liều thuốc (mg, g, units)
    
    Args:
        value: Liều thuốc
        decimals: Số chữ số thập phân
    
    Returns:
        String đã format
    
    Example:
        >>> format_dose(1000.0)
        '1000'
        >>> format_dose(1000.5)
        '1000.5'
    """
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def format_rate(value: float, decimals: int = 1) -> str:
    """
    Format tốc độ (mL/h, mg/h, etc.)
    
    Args:
        value: Tốc độ
        decimals: Số chữ số thập phân
    
    Returns:
        String đã format
    
    Example:
        >>> format_rate(100.0)
        '100'
        >>> format_rate(100.5)
        '100.5'
    """
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


# ============================================================================
# STREAMLIT INPUT FUNCTIONS - Render input với format chuẩn
# ============================================================================

def render_age_input(
    label: str = "Tuổi (năm)",
    min_value: int = 0,
    max_value: int = 120,
    value: Optional[int] = None,
    step: int = 1,
    key: Optional[str] = None,
    help_text: Optional[str] = None,
    **kwargs
) -> int:
    """
    Render number input cho tuổi - tự động format số nguyên
    
    Args:
        label: Label hiển thị
        min_value: Giá trị tối thiểu
        max_value: Giá trị tối đa
        value: Giá trị mặc định
        step: Bước nhảy (mặc định 1)
        key: Streamlit key
        help_text: Text hướng dẫn
        **kwargs: Các tham số khác cho st.number_input
    
    Returns:
        Tuổi (int)
    
    Example:
        >>> age = render_age_input("Tuổi", min_value=18, max_value=120, value=50)
    """
    if value is None:
        value = 50
    
    return int(st.number_input(
        label,
        min_value=min_value,
        max_value=max_value,
        value=int(value),
        step=step,
        format="%d",  # Format số nguyên
        help=help_text,
        key=key,
        **kwargs
    ))


def render_weight_input(
    label: str = "Cân nặng (kg)",
    min_value: float = 10.0,
    max_value: float = 300.0,
    value: Optional[float] = None,
    step: float = 1.0,
    decimals: int = 1,
    key: Optional[str] = None,
    help_text: Optional[str] = None,
    **kwargs
) -> float:
    """
    Render number input cho cân nặng - format 1 số thập phân
    
    Args:
        label: Label hiển thị
        min_value: Giá trị tối thiểu
        max_value: Giá trị tối đa
        value: Giá trị mặc định
        step: Bước nhảy (mặc định 1.0)
        decimals: Số chữ số thập phân (mặc định 1)
        key: Streamlit key
        help_text: Text hướng dẫn
        **kwargs: Các tham số khác cho st.number_input
    
    Returns:
        Cân nặng (float)
    
    Example:
        >>> weight = render_weight_input("Cân nặng", min_value=10.0, max_value=200.0, value=70.0)
    """
    if value is None:
        value = 70.0
    
    format_str = f"%.{decimals}f" if decimals > 0 else "%d"
    
    return float(st.number_input(
        label,
        min_value=min_value,
        max_value=max_value,
        value=value,
        step=step,
        format=format_str,
        help=help_text,
        key=key,
        **kwargs
    ))


def render_height_input(
    label: str = "Chiều cao (cm)",
    min_value: int = 50,
    max_value: int = 250,
    value: Optional[int] = None,
    step: int = 1,
    key: Optional[str] = None,
    help_text: Optional[str] = None,
    **kwargs
) -> int:
    """
    Render number input cho chiều cao - format số nguyên
    
    Args:
        label: Label hiển thị
        min_value: Giá trị tối thiểu
        max_value: Giá trị tối đa
        value: Giá trị mặc định
        step: Bước nhảy (mặc định 1)
        key: Streamlit key
        help_text: Text hướng dẫn
        **kwargs: Các tham số khác cho st.number_input
    
    Returns:
        Chiều cao (int)
    
    Example:
        >>> height = render_height_input("Chiều cao", min_value=100, max_value=220, value=170)
    """
    if value is None:
        value = 170
    
    return int(st.number_input(
        label,
        min_value=min_value,
        max_value=max_value,
        value=int(value),
        step=step,
        format="%d",  # Format số nguyên
        help=help_text,
        key=key,
        **kwargs
    ))


def render_lab_value_input(
    label: str,
    min_value: float = 0.0,
    max_value: float = 10000.0,
    value: Optional[float] = None,
    step: Optional[float] = None,
    decimals: int = 1,
    key: Optional[str] = None,
    help_text: Optional[str] = None,
    **kwargs
) -> float:
    """
    Render number input cho giá trị lab - format với số thập phân
    
    Args:
        label: Label hiển thị
        min_value: Giá trị tối thiểu
        max_value: Giá trị tối đa
        value: Giá trị mặc định
        step: Bước nhảy (tự động tính nếu None)
        decimals: Số chữ số thập phân (mặc định 1)
        key: Streamlit key
        help_text: Text hướng dẫn
        **kwargs: Các tham số khác cho st.number_input
    
    Returns:
        Giá trị lab (float)
    
    Example:
        >>> creatinine = render_lab_value_input(
        ...     "Creatinine (µmol/L)",
        ...     min_value=10.0,
        ...     max_value=2000.0,
        ...     value=100.0,
        ...     decimals=1
        ... )
    """
    if value is None:
        value = 0.0
    
    if step is None:
        step = 10.0 ** (-decimals)  # Tự động tính step dựa trên decimals
    
    format_str = f"%.{decimals}f"
    
    return float(st.number_input(
        label,
        min_value=min_value,
        max_value=max_value,
        value=value,
        step=step,
        format=format_str,
        help=help_text,
        key=key,
        **kwargs
    ))


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_format_string(decimals: int = 1) -> str:
    """
    Lấy format string cho số thập phân
    
    Args:
        decimals: Số chữ số thập phân
    
    Returns:
        Format string (ví dụ: "%.1f", "%.2f")
    
    Example:
        >>> get_format_string(1)
        '%.1f'
        >>> get_format_string(0)
        '%d'
    """
    if decimals == 0:
        return "%d"
    return f"%.{decimals}f"


def format_number(value: float, decimals: int = 1, remove_trailing_zeros: bool = True) -> str:
    """
    Format số tổng quát
    
    Args:
        value: Giá trị số
        decimals: Số chữ số thập phân
        remove_trailing_zeros: Có loại bỏ số 0 thừa không (ví dụ: 70.0 -> 70)
    
    Returns:
        String đã format
    
    Example:
        >>> format_number(70.0, decimals=1)
        '70'
        >>> format_number(70.5, decimals=1)
        '70.5'
        >>> format_number(70.0, decimals=1, remove_trailing_zeros=False)
        '70.0'
    """
    if decimals == 0:
        return str(int(round(value)))
    
    rounded = round(value, decimals)
    
    if remove_trailing_zeros and rounded == int(rounded):
        return str(int(rounded))
    
    formatted = f"{rounded:.{decimals}f}"
    
    if remove_trailing_zeros:
        formatted = formatted.rstrip('0').rstrip('.')
    
    return formatted

