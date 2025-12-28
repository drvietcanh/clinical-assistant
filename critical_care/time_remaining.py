"""
Time Remaining Calculator
Calculate remaining time for infusion
"""

from typing import Dict, Optional
from critical_care.enhanced_infusion import calculate_infusion_time


def calculate_remaining_time(
    initial_volume_ml: float,
    infused_volume_ml: float,
    current_rate_ml_hour: float
) -> Dict:
    """
    Calculate remaining time for infusion.
    
    Args:
        initial_volume_ml: Initial volume in bag/syringe
        infused_volume_ml: Volume already infused
        current_rate_ml_hour: Current infusion rate in ml/hour
    
    Returns:
        Dictionary with remaining time details:
        {
            "remaining_volume_ml": float,
            "remaining_time_hours": float,
            "remaining_time_minutes": float,
            "remaining_time_formatted": str,
            "percent_infused": float,
            "percent_remaining": float,
            "warning": Optional[str]
        }
    """
    if initial_volume_ml <= 0:
        raise ValueError("Initial volume must be > 0")
    if infused_volume_ml < 0:
        raise ValueError("Infused volume must be >= 0")
    if infused_volume_ml > initial_volume_ml:
        raise ValueError("Infused volume cannot exceed initial volume")
    if current_rate_ml_hour <= 0:
        raise ValueError("Infusion rate must be > 0")
    
    # Calculate remaining volume
    remaining_volume_ml = initial_volume_ml - infused_volume_ml
    
    # Calculate remaining time
    remaining_time_hours = remaining_volume_ml / current_rate_ml_hour
    remaining_time_minutes = remaining_time_hours * 60
    
    # Format time
    hours = int(remaining_time_hours)
    minutes = int(remaining_time_minutes % 60)
    
    if hours > 0:
        time_formatted = f"{hours} giờ {minutes} phút"
    else:
        time_formatted = f"{minutes} phút"
    
    # Calculate percentages
    percent_infused = (infused_volume_ml / initial_volume_ml * 100) if initial_volume_ml > 0 else 0
    percent_remaining = (remaining_volume_ml / initial_volume_ml * 100) if initial_volume_ml > 0 else 0
    
    # Generate warning
    warning = None
    if remaining_time_hours < 0.5:  # Less than 30 minutes
        warning = "⚠️ Sắp hết dịch (< 30 phút) - Chuẩn bị thay dịch mới"
    elif remaining_time_hours < 1:  # Less than 1 hour
        warning = "⚠️ Sắp hết dịch (< 1 giờ) - Kiểm tra lại"
    
    return {
        "remaining_volume_ml": round(remaining_volume_ml, 1),
        "remaining_time_hours": round(remaining_time_hours, 2),
        "remaining_time_minutes": round(remaining_time_minutes, 1),
        "remaining_time_formatted": time_formatted,
        "percent_infused": round(percent_infused, 1),
        "percent_remaining": round(percent_remaining, 1),
        "warning": warning
    }


def calculate_time_from_rate_and_volume(
    volume_ml: float,
    rate_ml_hour: float
) -> Dict:
    """
    Calculate time needed to infuse a volume at a given rate.
    
    Args:
        volume_ml: Volume to infuse
        rate_ml_hour: Infusion rate in ml/hour
    
    Returns:
        Dictionary with time details
    """
    return calculate_infusion_time(volume_ml, rate_ml_hour)

