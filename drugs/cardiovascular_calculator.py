"""
Cardiovascular Drugs Calculator
Calculate vasopressor/inotrope infusion rates, drop rates, and infusion times
"""

import json
import math
from pathlib import Path
from typing import Dict, Optional, List

# Import DIRC conversion functions
try:
    from critical_care.dirc.conversions import mcg_kg_min_to_ml_hr, ml_hr_to_mcg_kg_min
    DIRC_AVAILABLE = True
except ImportError:
    DIRC_AVAILABLE = False
    # Fallback functions
    def mcg_kg_min_to_ml_hr(dose_mcg_kg_min: float, weight_kg: float, concentration_mg_ml: float) -> float:
        """Convert mcg/kg/min to mL/hr."""
        if concentration_mg_ml <= 0 or weight_kg <= 0:
            raise ValueError("Concentration and weight must be > 0")
        return (dose_mcg_kg_min * weight_kg * 60) / (concentration_mg_ml * 1000)
    
    def ml_hr_to_mcg_kg_min(ml_per_hr: float, weight_kg: float, concentration_mg_ml: float) -> float:
        """Convert mL/hr to mcg/kg/min."""
        if concentration_mg_ml <= 0 or weight_kg <= 0:
            raise ValueError("Concentration and weight must be > 0")
        return (ml_per_hr * concentration_mg_ml * 1000) / (weight_kg * 60)


# Load cardiovascular drugs database
def _load_cardiovascular_database() -> Dict:
    """Load cardiovascular drugs database from JSON file."""
    db_path = Path(__file__).parent / "cardiovascular_drugs.json"
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


CARDIOVASCULAR_DRUGS = _load_cardiovascular_database()


def get_drug_names() -> List[str]:
    """Get list of available drug names."""
    return list(CARDIOVASCULAR_DRUGS.keys())


def get_drug_info(drug_name: str) -> Optional[Dict]:
    """Get drug information from database."""
    return CARDIOVASCULAR_DRUGS.get(drug_name)


def calculate_vasopressor_infusion(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    custom_concentration_mcg_ml: Optional[float] = None
) -> Dict:
    """
    Calculate vasopressor infusion details.
    
    Args:
        drug_name: Name of drug (e.g., "Adrenaline", "Noradrenaline")
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: "syringe_pump_50ml" or "iv_bag_500ml"
        custom_concentration_mcg_ml: Optional custom concentration (overrides standard)
    
    Returns:
        Dictionary with infusion details:
        {
            "total_dose_mcg_min": float,
            "total_dose_mcg_hour": float,
            "infusion_rate_ml_hour": float,
            "concentration_mcg_ml": float,
            "preparation_instructions": str,
            "infusion_method": str
        }
    """
    # Validate inputs
    if dose_mcg_kg_min <= 0:
        raise ValueError("Dose must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    
    # Get drug info
    drug_info = get_drug_info(drug_name)
    if not drug_info:
        raise ValueError(f"Drug '{drug_name}' not found in database")
    
    # Get concentration
    if custom_concentration_mcg_ml:
        concentration_mcg_ml = custom_concentration_mcg_ml
        concentration_mg_ml = concentration_mcg_ml / 1000
        preparation_instructions = f"Custom concentration: {concentration_mcg_ml} mcg/ml"
    else:
        infusion_methods = drug_info.get("infusion_methods", {})
        method_info = infusion_methods.get(infusion_method)
        if not method_info:
            raise ValueError(f"Infusion method '{infusion_method}' not available for {drug_name}")
        
        concentration_mcg_ml = method_info.get("standard_concentration_mcg_ml", 0)
        concentration_mg_ml = concentration_mcg_ml / 1000
        preparation_instructions = method_info.get("preparation", "")
    
    if concentration_mcg_ml <= 0:
        raise ValueError(f"Invalid concentration for {drug_name}")
    
    # Calculate total doses
    total_dose_mcg_min = dose_mcg_kg_min * weight_kg
    total_dose_mcg_hour = total_dose_mcg_min * 60
    
    # Calculate infusion rate using DIRC formula
    infusion_rate_ml_hour = mcg_kg_min_to_ml_hr(
        dose_mcg_kg_min, 
        weight_kg, 
        concentration_mg_ml
    )
    
    return {
        "total_dose_mcg_min": round(total_dose_mcg_min, 2),
        "total_dose_mcg_hour": round(total_dose_mcg_hour, 2),
        "infusion_rate_ml_hour": round(infusion_rate_ml_hour, 2),
        "concentration_mcg_ml": round(concentration_mcg_ml, 2),
        "preparation_instructions": preparation_instructions,
        "infusion_method": infusion_method
    }


def calculate_drop_rate(
    infusion_rate_ml_hour: float,
    drop_factor: int = 20
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
    
    # Formula: gtt/min = (ml/hr × drop_factor) / 60
    drop_rate = (infusion_rate_ml_hour * drop_factor) / 60
    return round(drop_rate, 1)


def calculate_infusion_time(
    volume_ml: float,
    infusion_rate_ml_hour: float
) -> Dict:
    """
    Calculate infusion time.
    
    Args:
        volume_ml: Volume in ml
        infusion_rate_ml_hour: Infusion rate in ml/hour
    
    Returns:
        Dictionary with time in hours, minutes, and formatted string:
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


def calculate_complete_infusion(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    drop_factor: Optional[int] = None,
    custom_concentration_mcg_ml: Optional[float] = None
) -> Dict:
    """
    Calculate complete infusion details including drop rate and time.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: "syringe_pump_50ml" or "iv_bag_500ml"
        drop_factor: Optional drop factor for gtt/min calculation (None for syringe pump)
        custom_concentration_mcg_ml: Optional custom concentration
    
    Returns:
        Complete infusion details dictionary
    """
    # Calculate basic infusion
    infusion_details = calculate_vasopressor_infusion(
        drug_name, dose_mcg_kg_min, weight_kg, infusion_method, custom_concentration_mcg_ml
    )
    
    # Get volume based on method
    drug_info = get_drug_info(drug_name)
    if not drug_info:
        raise ValueError(f"Drug '{drug_name}' not found")
    
    method_info = drug_info.get("infusion_methods", {}).get(infusion_method, {})
    volume_ml = method_info.get("standard_volume", 50 if infusion_method == "syringe_pump_50ml" else 500)
    
    # Calculate drop rate if applicable
    drop_rate = None
    if drop_factor and infusion_method == "iv_bag_500ml":
        drop_rate = calculate_drop_rate(infusion_details["infusion_rate_ml_hour"], drop_factor)
    
    # Calculate infusion time
    time_details = calculate_infusion_time(volume_ml, infusion_details["infusion_rate_ml_hour"])
    
    # Merge results
    result = {
        **infusion_details,
        "volume_ml": volume_ml,
        "drop_rate_gtt_min": drop_rate,
        **time_details
    }
    
    return result


def validate_dose_range(
    drug_name: str,
    dose_mcg_kg_min: float
) -> Dict:
    """
    Validate if dose is within recommended range.
    
    Returns:
        Dictionary with validation result:
        {
            "is_valid": bool,
            "warning": Optional[str],
            "recommended_range": str
        }
    """
    drug_info = get_drug_info(drug_name)
    if not drug_info:
        return {
            "is_valid": False,
            "warning": f"Drug '{drug_name}' not found",
            "recommended_range": ""
        }
    
    dose_range = drug_info.get("dose_range", "")
    max_dose_str = drug_info.get("max_dose", "")
    
    # Parse max dose (simple parsing, assumes format like "1-2 mcg/kg/min")
    try:
        max_dose = float(max_dose_str.split()[0].split("-")[-1])
    except (ValueError, IndexError):
        max_dose = None
    
    warning = None
    is_valid = True
    
    if max_dose and dose_mcg_kg_min > max_dose:
        is_valid = False
        warning = f"Liều {dose_mcg_kg_min} mcg/kg/min vượt quá liều tối đa khuyến nghị ({max_dose} mcg/kg/min)"
    elif dose_mcg_kg_min <= 0:
        is_valid = False
        warning = "Liều phải > 0"
    
    return {
        "is_valid": is_valid,
        "warning": warning,
        "recommended_range": dose_range,
        "max_dose": max_dose_str
    }

