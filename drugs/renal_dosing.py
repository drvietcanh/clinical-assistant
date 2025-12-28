"""
Renal Dose Adjustment Calculator
Adjust drug doses based on renal function (eGFR/CrCl)
"""

import json
from pathlib import Path
from typing import Dict, Optional


def _load_renal_database() -> Dict:
    """Load renal dosing database from JSON file."""
    db_path = Path(__file__).parent / "renal_dosing_database.json"
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


RENAL_DB = _load_renal_database()


def get_egfr_category(egfr: float, on_dialysis: bool = False) -> str:
    """
    Determine eGFR category.
    
    Args:
        egfr: eGFR in ml/min/1.73m²
        on_dialysis: Whether patient is on dialysis
    
    Returns:
        Category: "normal", "mild", "moderate", "severe", "kidney_failure", or "dialysis"
    """
    if on_dialysis:
        return "dialysis"
    elif egfr >= 90:
        return "normal"
    elif egfr >= 60:
        return "mild"
    elif egfr >= 30:
        return "moderate"
    elif egfr >= 15:
        return "severe"
    else:
        return "kidney_failure"


def get_renal_adjustment_info(drug_name: str) -> Optional[Dict]:
    """
    Get renal adjustment information for a drug.
    
    Args:
        drug_name: Name of drug
    
    Returns:
        Dictionary with adjustment information
    """
    renal_dosing = RENAL_DB.get("renal_dosing", {})
    return renal_dosing.get(drug_name)


def calculate_renal_adjusted_dose(
    drug_name: str,
    original_dose_mcg_kg_min: float,
    egfr: float,
    on_dialysis: bool = False
) -> Dict:
    """
    Calculate renal-adjusted dose.
    
    Args:
        drug_name: Name of drug
        original_dose_mcg_kg_min: Original dose in mcg/kg/min
        egfr: eGFR in ml/min/1.73m²
        on_dialysis: Whether patient is on dialysis
    
    Returns:
        Dictionary with adjusted dose information:
        {
            "adjustment_needed": bool,
            "original_dose": float,
            "adjusted_dose": float,
            "multiplier": float,
            "egfr_category": str,
            "adjustment_info": Dict,
            "notes": str,
            "warning": Optional[str]
        }
    """
    adjustment_info = get_renal_adjustment_info(drug_name)
    
    if not adjustment_info:
        return {
            "adjustment_needed": None,
            "original_dose": original_dose_mcg_kg_min,
            "adjusted_dose": original_dose_mcg_kg_min,
            "multiplier": 1.0,
            "egfr_category": get_egfr_category(egfr, on_dialysis),
            "adjustment_info": None,
            "notes": "Không có thông tin điều chỉnh liều cho thuốc này",
            "warning": None
        }
    
    adjustment_needed = adjustment_info.get("adjustment_needed", False)
    
    if not adjustment_needed:
        return {
            "adjustment_needed": False,
            "original_dose": original_dose_mcg_kg_min,
            "adjusted_dose": original_dose_mcg_kg_min,
            "multiplier": 1.0,
            "egfr_category": get_egfr_category(egfr, on_dialysis),
            "adjustment_info": adjustment_info,
            "notes": adjustment_info.get("notes", "Không cần điều chỉnh liều"),
            "warning": None
        }
    
    # Determine adjustment multiplier
    egfr_category = get_egfr_category(egfr, on_dialysis)
    adjustment_rules = adjustment_info.get("adjustment", {})
    
    multiplier = 1.0
    adjustment_note = ""
    
    if on_dialysis or egfr < 15:
        rule = adjustment_rules.get("egfr_below_15")
        if rule:
            multiplier = rule.get("multiplier", 1.0)
            adjustment_note = rule.get("notes", "")
    elif egfr < 30:
        rule = adjustment_rules.get("egfr_15_30")
        if rule:
            multiplier = rule.get("multiplier", 1.0)
            adjustment_note = rule.get("notes", "")
    elif egfr < 50:
        rule = adjustment_rules.get("egfr_30_50")
        if rule:
            multiplier = rule.get("multiplier", 1.0)
            adjustment_note = rule.get("notes", "")
    
    adjusted_dose = original_dose_mcg_kg_min * multiplier
    
    # Generate warning if significant reduction
    warning = None
    if multiplier < 0.5:
        warning = f"Cần giảm liều đáng kể ({multiplier*100:.0f}% liều ban đầu) do suy thận nặng"
    elif multiplier < 0.75:
        warning = f"Cần giảm liều ({multiplier*100:.0f}% liều ban đầu) do suy thận"
    
    return {
        "adjustment_needed": True,
        "original_dose": original_dose_mcg_kg_min,
        "adjusted_dose": round(adjusted_dose, 3),
        "multiplier": multiplier,
        "egfr_category": egfr_category,
        "adjustment_info": adjustment_info,
        "notes": adjustment_note or adjustment_info.get("notes", ""),
        "warning": warning,
        "reduction_percent": round((1 - multiplier) * 100, 1)
    }


def get_egfr_category_info(category: str) -> Optional[Dict]:
    """Get information about an eGFR category."""
    categories = RENAL_DB.get("egfr_categories", {})
    return categories.get(category)


def validate_renal_dose(
    drug_name: str,
    dose_mcg_kg_min: float,
    egfr: float,
    on_dialysis: bool = False
) -> Dict:
    """
    Validate dose considering renal function.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        egfr: eGFR in ml/min/1.73m²
        on_dialysis: Whether patient is on dialysis
    
    Returns:
        Dictionary with validation result
    """
    adjustment_result = calculate_renal_adjusted_dose(
        drug_name, dose_mcg_kg_min, egfr, on_dialysis
    )
    
    # Check if dose exceeds recommended adjusted dose
    if adjustment_result["adjustment_needed"]:
        recommended_dose = adjustment_result["adjusted_dose"]
        if dose_mcg_kg_min > recommended_dose * 1.1:  # Allow 10% tolerance
            return {
                "is_valid": False,
                "error": f"Liều {dose_mcg_kg_min:.2f} mcg/kg/min vượt quá liều khuyến nghị {recommended_dose:.2f} mcg/kg/min cho eGFR {egfr:.1f}",
                "recommended_dose": recommended_dose,
                **adjustment_result
            }
    
    return {
        "is_valid": True,
        "error": None,
        **adjustment_result
    }

