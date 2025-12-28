"""
Enhanced Infusion Calculator
Comprehensive calculator for infusion rates, drop rates, time, and volume
Extends Phase 2 cardiovascular calculator and DIRC calculator
"""

from typing import Dict, Optional
from critical_care.dirc.conversions import mcg_kg_min_to_ml_hr, ml_hr_to_mcg_kg_min


def calculate_infusion_rate(
    dose_mcg_kg_min: float,
    weight_kg: float,
    concentration_mcg_ml: float,
    drop_factor: Optional[int] = None
) -> Dict:
    """
    Calculate infusion rate with optional drop rate.
    
    Args:
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        concentration_mcg_ml: Concentration in mcg/ml
        drop_factor: Optional drop factor for gtt/min calculation
    
    Returns:
        Dictionary with infusion details:
        {
            "total_dose_mcg_min": float,
            "total_dose_mcg_hour": float,
            "infusion_rate_ml_hour": float,
            "drop_rate_gtt_min": Optional[float],
            "concentration_mcg_ml": float
        }
    """
    if dose_mcg_kg_min <= 0:
        raise ValueError("Dose must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    if concentration_mcg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    
    # Calculate total doses
    total_dose_mcg_min = dose_mcg_kg_min * weight_kg
    total_dose_mcg_hour = total_dose_mcg_min * 60
    
    # Convert concentration to mg/ml for DIRC function
    concentration_mg_ml = concentration_mcg_ml / 1000
    
    # Calculate infusion rate
    infusion_rate_ml_hour = mcg_kg_min_to_ml_hr(
        dose_mcg_kg_min,
        weight_kg,
        concentration_mg_ml
    )
    
    # Calculate drop rate if drop factor provided
    drop_rate_gtt_min = None
    if drop_factor and drop_factor > 0:
        drop_rate_gtt_min = (infusion_rate_ml_hour * drop_factor) / 60
    
    return {
        "total_dose_mcg_min": round(total_dose_mcg_min, 2),
        "total_dose_mcg_hour": round(total_dose_mcg_hour, 2),
        "infusion_rate_ml_hour": round(infusion_rate_ml_hour, 2),
        "drop_rate_gtt_min": round(drop_rate_gtt_min, 1) if drop_rate_gtt_min else None,
        "concentration_mcg_ml": round(concentration_mcg_ml, 2)
    }


def calculate_volume_needed(
    dose_mcg_kg_min: float,
    weight_kg: float,
    duration_hours: float,
    concentration_mcg_ml: float
) -> Dict:
    """
    Calculate volume needed for given duration.
    
    Args:
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        duration_hours: Duration in hours
        concentration_mcg_ml: Concentration in mcg/ml
    
    Returns:
        Dictionary with volume details:
        {
            "total_dose_mcg": float,
            "volume_ml": float,
            "infusion_rate_ml_hour": float
        }
    """
    if dose_mcg_kg_min <= 0:
        raise ValueError("Dose must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    if duration_hours <= 0:
        raise ValueError("Duration must be > 0")
    if concentration_mcg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    
    # Calculate total dose needed
    total_dose_mcg_min = dose_mcg_kg_min * weight_kg
    total_dose_mcg = total_dose_mcg_min * 60 * duration_hours
    
    # Calculate volume
    volume_ml = total_dose_mcg / concentration_mcg_ml
    
    # Calculate infusion rate
    concentration_mg_ml = concentration_mcg_ml / 1000
    infusion_rate_ml_hour = mcg_kg_min_to_ml_hr(
        dose_mcg_kg_min,
        weight_kg,
        concentration_mg_ml
    )
    
    return {
        "total_dose_mcg": round(total_dose_mcg, 2),
        "volume_ml": round(volume_ml, 2),
        "infusion_rate_ml_hour": round(infusion_rate_ml_hour, 2)
    }


def calculate_dose_from_rate(
    infusion_rate_ml_hour: float,
    weight_kg: float,
    concentration_mcg_ml: float
) -> Dict:
    """
    Calculate dose from infusion rate (reverse calculation).
    
    Args:
        infusion_rate_ml_hour: Infusion rate in ml/hour
        weight_kg: Weight in kg
        concentration_mcg_ml: Concentration in mcg/ml
    
    Returns:
        Dictionary with dose details:
        {
            "dose_mcg_kg_min": float,
            "total_dose_mcg_min": float,
            "total_dose_mcg_hour": float
        }
    """
    if infusion_rate_ml_hour <= 0:
        raise ValueError("Infusion rate must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    if concentration_mcg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    
    # Convert concentration to mg/ml for DIRC function
    concentration_mg_ml = concentration_mcg_ml / 1000
    
    # Calculate dose using reverse DIRC formula
    dose_mcg_kg_min = ml_hr_to_mcg_kg_min(
        infusion_rate_ml_hour,
        weight_kg,
        concentration_mg_ml
    )
    
    # Calculate total doses
    total_dose_mcg_min = dose_mcg_kg_min * weight_kg
    total_dose_mcg_hour = total_dose_mcg_min * 60
    
    return {
        "dose_mcg_kg_min": round(dose_mcg_kg_min, 3),
        "total_dose_mcg_min": round(total_dose_mcg_min, 2),
        "total_dose_mcg_hour": round(total_dose_mcg_hour, 2)
    }


def calculate_infusion_time(
    volume_ml: float,
    infusion_rate_ml_hour: float
) -> Dict:
    """
    Calculate infusion time from volume and rate.
    
    Args:
        volume_ml: Volume in ml
        infusion_rate_ml_hour: Infusion rate in ml/hour
    
    Returns:
        Dictionary with time details:
        {
            "time_hours": float,
            "time_minutes": float,
            "time_formatted": str
        }
    """
    if volume_ml <= 0:
        raise ValueError("Volume must be > 0")
    if infusion_rate_ml_hour <= 0:
        raise ValueError("Infusion rate must be > 0")
    
    # Calculate time
    time_hours = volume_ml / infusion_rate_ml_hour
    time_minutes = time_hours * 60
    
    # Format time
    hours = int(time_hours)
    minutes = int(time_minutes % 60)
    
    if hours > 0:
        time_formatted = f"{hours} giờ {minutes} phút"
    else:
        time_formatted = f"{minutes} phút"
    
    return {
        "time_hours": round(time_hours, 2),
        "time_minutes": round(time_minutes, 1),
        "time_formatted": time_formatted
    }


def calculate_drop_rate(
    infusion_rate_ml_hour: float,
    drop_factor: int
) -> float:
    """
    Calculate drop rate in gtt/min.
    
    Args:
        infusion_rate_ml_hour: Infusion rate in ml/hour
        drop_factor: Drop factor (10, 15, 20, or 60 gtt/ml)
    
    Returns:
        Drop rate in gtt/min
    """
    if infusion_rate_ml_hour <= 0:
        raise ValueError("Infusion rate must be > 0")
    if drop_factor <= 0:
        raise ValueError("Drop factor must be > 0")
    
    drop_rate = (infusion_rate_ml_hour * drop_factor) / 60
    return round(drop_rate, 1)

