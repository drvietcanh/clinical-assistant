"""
Pediatric Dosing Calculator
Calculate drug doses for pediatric patients based on age and weight
"""

import json
from pathlib import Path
from typing import Dict, Optional, Tuple


def _load_pediatric_database() -> Dict:
    """Load pediatric dosing database from JSON file."""
    db_path = Path(__file__).parent / "pediatric_dosing_database.json"
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


PEDIATRIC_DB = _load_pediatric_database()


def get_age_group(age_days: float) -> str:
    """
    Determine age group from age in days.
    
    Args:
        age_days: Age in days
    
    Returns:
        Age group: "neonatal", "infant", "child", or "adolescent"
    """
    if age_days <= 28:
        return "neonatal"
    elif age_days <= 365:
        return "infant"
    elif age_days <= 365 * 12:
        return "child"
    else:
        return "adolescent"


def get_pediatric_dose_range(
    drug_name: str,
    age_group: str
) -> Optional[Dict]:
    """
    Get pediatric dose range for a drug and age group.
    
    Args:
        drug_name: Name of drug
        age_group: "neonatal", "infant", "child", or "adolescent"
    
    Returns:
        Dictionary with dose range information
    """
    pediatric_dosing = PEDIATRIC_DB.get("pediatric_dosing", {})
    drug_info = pediatric_dosing.get(drug_name)
    
    if not drug_info:
        return None
    
    return drug_info.get(age_group)


def validate_pediatric_dose(
    drug_name: str,
    dose_mcg_kg_min: float,
    age_days: float
) -> Dict:
    """
    Validate pediatric dose against recommended ranges.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        age_days: Age in days
    
    Returns:
        Dictionary with validation result:
        {
            "is_valid": bool,
            "age_group": str,
            "dose_range": str,
            "initial_dose": str,
            "max_dose": str,
            "warning": Optional[str],
            "error": Optional[str]
        }
    """
    age_group = get_age_group(age_days)
    dose_info = get_pediatric_dose_range(drug_name, age_group)
    
    if not dose_info:
        return {
            "is_valid": None,
            "age_group": age_group,
            "dose_range": "Unknown",
            "initial_dose": "Unknown",
            "max_dose": "Unknown",
            "warning": f"Không có thông tin liều cho {age_group}",
            "error": None
        }
    
    dose_range_str = dose_info.get("dose_range", "")
    initial_dose_str = dose_info.get("initial_dose", "")
    max_dose_str = dose_info.get("max_dose", "")
    
    # Parse max dose
    try:
        # Extract max dose value (e.g., "1–2 mcg/kg/min" -> 2)
        max_dose_parts = max_dose_str.split("–")
        if len(max_dose_parts) > 1:
            max_dose = float(max_dose_parts[-1].split()[0])
        else:
            max_dose = float(max_dose_str.split()[0])
    except (ValueError, IndexError):
        max_dose = None
    
    # Validate
    is_valid = True
    warning = None
    error = None
    
    if max_dose and dose_mcg_kg_min > max_dose:
        is_valid = False
        error = f"Liều {dose_mcg_kg_min:.2f} mcg/kg/min vượt quá liều tối đa {max_dose} mcg/kg/min cho {age_group}"
    elif max_dose and dose_mcg_kg_min > max_dose * 0.8:
        warning = f"Liều {dose_mcg_kg_min:.2f} mcg/kg/min gần đạt liều tối đa {max_dose} mcg/kg/min"
    
    return {
        "is_valid": is_valid,
        "age_group": age_group,
        "dose_range": dose_range_str,
        "initial_dose": initial_dose_str,
        "max_dose": max_dose_str,
        "warning": warning,
        "error": error
    }


def calculate_pediatric_infusion(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    age_days: float,
    infusion_method: str = "syringe_pump_50ml"
) -> Dict:
    """
    Calculate pediatric infusion details.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        age_days: Age in days
        infusion_method: "syringe_pump_50ml" or "syringe_pump_20ml" (for small children)
    
    Returns:
        Dictionary with infusion details (similar to adult calculator)
    """
    # Validate dose
    validation = validate_pediatric_dose(drug_name, dose_mcg_kg_min, age_days)
    
    # Get pediatric preparation info
    pediatric_dosing = PEDIATRIC_DB.get("pediatric_dosing", {})
    drug_info = pediatric_dosing.get(drug_name, {})
    prep_info = drug_info.get("preparation_pediatric", {})
    method_info = prep_info.get(infusion_method)
    
    if not method_info:
        # Fallback to adult preparation
        from drugs.cardiovascular_calculator import calculate_complete_infusion
        result = calculate_complete_infusion(
            drug_name, dose_mcg_kg_min, weight_kg, infusion_method
        )
        result["pediatric_mode"] = True
        result["age_group"] = validation["age_group"]
        result["validation"] = validation
        return result
    
    # Use pediatric preparation
    concentration_mcg_ml = method_info.get("standard_concentration_mcg_ml", 0)
    if concentration_mcg_ml <= 0:
        raise ValueError(f"Invalid pediatric concentration for {drug_name}")
    
    concentration_mg_ml = concentration_mcg_ml / 1000
    preparation = method_info.get("preparation", "")
    
    # Calculate using DIRC formula
    from critical_care.dirc.conversions import mcg_kg_min_to_ml_hr
    
    total_dose_mcg_min = dose_mcg_kg_min * weight_kg
    total_dose_mcg_hour = total_dose_mcg_min * 60
    
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
        "preparation_instructions": preparation,
        "infusion_method": infusion_method,
        "pediatric_mode": True,
        "age_group": validation["age_group"],
        "validation": validation
    }


def get_age_group_info(age_group: str) -> Optional[Dict]:
    """Get information about an age group."""
    age_groups = PEDIATRIC_DB.get("age_groups", {})
    return age_groups.get(age_group)

