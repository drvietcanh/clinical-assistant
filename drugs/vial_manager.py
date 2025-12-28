"""
Vial Management System
Calculate number of vials needed, waste, and preparation instructions
"""

import json
import math
from pathlib import Path
from typing import Dict, Optional, List


def _load_vial_database() -> Dict:
    """Load vial database from cardiovascular drugs JSON."""
    db_path = Path(__file__).parent / "cardiovascular_drugs.json"
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


VIAL_DATABASE = _load_vial_database()


def get_drug_vials(drug_name: str) -> List[Dict]:
    """
    Get list of available vials for a drug.
    
    Args:
        drug_name: Name of drug
    
    Returns:
        List of vial dictionaries
    """
    drug_info = VIAL_DATABASE.get(drug_name)
    if not drug_info:
        return []
    
    return drug_info.get("vials", [])


def calculate_vials_needed(
    drug_name: str,
    total_dose_mg: float,
    selected_vial: Optional[str] = None
) -> Optional[Dict]:
    """
    Calculate number of vials needed.
    
    Args:
        drug_name: Name of drug
        total_dose_mg: Total dose needed in mg
        selected_vial: Optional vial size (e.g., "1mg/1ml"). If None, uses first common vial.
    
    Returns:
        Dictionary with:
        {
            "vials_needed": int,
            "total_available_mg": float,
            "waste_mg": float,
            "waste_percent": float,
            "selected_vial": str,
            "vial_info": dict
        }
    """
    if total_dose_mg <= 0:
        raise ValueError("Total dose must be > 0")
    
    drug_info = VIAL_DATABASE.get(drug_name)
    if not drug_info:
        raise ValueError(f"Drug '{drug_name}' not found in database")
    
    vials = drug_info.get("vials", [])
    if not vials:
        raise ValueError(f"No vials available for '{drug_name}'")
    
    # Select vial
    selected_vial_info = None
    if selected_vial:
        # Find vial by size
        for vial in vials:
            if vial.get("size") == selected_vial:
                selected_vial_info = vial
                break
        if not selected_vial_info:
            raise ValueError(f"Vial '{selected_vial}' not found for '{drug_name}'")
    else:
        # Use first common vial, or first vial if no common
        for vial in vials:
            if vial.get("common", False):
                selected_vial_info = vial
                break
        if not selected_vial_info:
            selected_vial_info = vials[0]
    
    # Get vial size in mg
    vial_size_mg = selected_vial_info.get("total_mg", 0)
    if vial_size_mg <= 0:
        raise ValueError(f"Invalid vial size for '{drug_name}'")
    
    # Calculate number of vials needed (always round up)
    vials_needed = math.ceil(total_dose_mg / vial_size_mg)
    
    # Calculate waste
    total_available_mg = vials_needed * vial_size_mg
    waste_mg = total_available_mg - total_dose_mg
    waste_percent = (waste_mg / total_available_mg * 100) if total_available_mg > 0 else 0
    
    return {
        "vials_needed": vials_needed,
        "total_available_mg": round(total_available_mg, 2),
        "waste_mg": round(waste_mg, 2),
        "waste_percent": round(waste_percent, 2),
        "selected_vial": selected_vial_info.get("size"),
        "vial_info": selected_vial_info
    }


def calculate_preparation(
    drug_name: str,
    total_dose_mg: float,
    selected_vial: Optional[str] = None,
    final_volume_ml: Optional[float] = None
) -> Dict:
    """
    Calculate preparation details.
    
    Args:
        drug_name: Name of drug
        total_dose_mg: Total dose needed in mg
        selected_vial: Optional vial size
        final_volume_ml: Optional final volume. If None, uses standard from infusion_methods.
    
    Returns:
        Dictionary with preparation details:
        {
            "vials_needed": int,
            "total_available_mg": float,
            "final_concentration_mg_ml": float,
            "final_concentration_mcg_ml": float,
            "waste_mg": float,
            "preparation_instructions": str,
            "vial_info": dict
        }
    """
    # Get vial calculation
    vial_result = calculate_vials_needed(drug_name, total_dose_mg, selected_vial)
    if not vial_result:
        raise ValueError(f"Cannot calculate vials for '{drug_name}'")
    
    drug_info = VIAL_DATABASE.get(drug_name)
    if not drug_info:
        raise ValueError(f"Drug '{drug_name}' not found")
    
    # Get final volume
    if final_volume_ml is None:
        # Try to get from infusion_methods (use syringe_pump_50ml as default)
        infusion_methods = drug_info.get("infusion_methods", {})
        method_info = infusion_methods.get("syringe_pump_50ml", {})
        final_volume_ml = method_info.get("standard_volume", 50)
    
    if final_volume_ml <= 0:
        raise ValueError("Final volume must be > 0")
    
    # Calculate final concentration
    # Use total_available_mg (from vials) for preparation
    total_available_mg = vial_result["total_available_mg"]
    final_concentration_mg_ml = total_available_mg / final_volume_ml
    final_concentration_mcg_ml = final_concentration_mg_ml * 1000
    
    # Generate preparation instructions
    vial_size = vial_result["selected_vial"]
    vials_needed = vial_result["vials_needed"]
    solvent = drug_info.get("solvent", "NaCl 0.9%")
    
    if vials_needed == 1:
        preparation_instructions = f"Lấy {vials_needed} ống {vial_size}, pha trong {final_volume_ml}ml {solvent}"
    else:
        preparation_instructions = f"Lấy {vials_needed} ống {vial_size}, pha trong {final_volume_ml}ml {solvent}"
    
    preparation_instructions += f"\nNồng độ cuối: {final_concentration_mcg_ml:.2f} mcg/ml ({final_concentration_mg_ml:.4f} mg/ml)"
    
    if vial_result["waste_mg"] > 0:
        preparation_instructions += f"\nLưu ý: Sẽ thừa {vial_result['waste_mg']:.2f} mg ({vial_result['waste_percent']:.1f}%)"
    
    return {
        "vials_needed": vials_needed,
        "total_available_mg": total_available_mg,
        "final_concentration_mg_ml": round(final_concentration_mg_ml, 4),
        "final_concentration_mcg_ml": round(final_concentration_mcg_ml, 2),
        "waste_mg": vial_result["waste_mg"],
        "waste_percent": vial_result["waste_percent"],
        "preparation_instructions": preparation_instructions,
        "vial_info": vial_result["vial_info"]
    }


def get_vial_labels(drug_name: str) -> List[str]:
    """Get list of vial labels for a drug."""
    vials = get_drug_vials(drug_name)
    return [vial.get("size", "") for vial in vials if vial.get("size")]


def calculate_vials_from_dose(
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    duration_hours: float = 24.0
) -> Dict:
    """
    Calculate vials needed from dose and duration.
    
    Args:
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        duration_hours: Duration in hours (default 24)
    
    Returns:
        Dictionary with vial calculation and dose details
    """
    if dose_mcg_kg_min <= 0:
        raise ValueError("Dose must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    if duration_hours <= 0:
        raise ValueError("Duration must be > 0")
    
    # Calculate total dose needed
    total_dose_mcg_min = dose_mcg_kg_min * weight_kg
    total_dose_mcg = total_dose_mcg_min * 60 * duration_hours
    total_dose_mg = total_dose_mcg / 1000
    
    # Calculate vials
    vial_result = calculate_vials_needed(drug_name, total_dose_mg)
    
    return {
        "total_dose_mg": round(total_dose_mg, 2),
        "total_dose_mcg": round(total_dose_mcg, 2),
        "duration_hours": duration_hours,
        **vial_result
    }

