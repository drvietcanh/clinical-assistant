"""
Multiple Simultaneous Infusions Calculator
Calculate multiple drugs infusing simultaneously
"""

from typing import List, Dict, Optional
from drugs.cardiovascular_calculator import calculate_complete_infusion


class InfusionItem:
    """Represents a single infusion item."""
    
    def __init__(
        self,
        drug_name: str,
        dose_mcg_kg_min: float,
        weight_kg: float,
        infusion_method: str = "syringe_pump_50ml",
        drop_factor: Optional[int] = None
    ):
        self.drug_name = drug_name
        self.dose_mcg_kg_min = dose_mcg_kg_min
        self.weight_kg = weight_kg
        self.infusion_method = infusion_method
        self.drop_factor = drop_factor
        self._result = None
    
    def calculate(self) -> Dict:
        """Calculate infusion details for this item."""
        if self._result is None:
            self._result = calculate_complete_infusion(
                self.drug_name,
                self.dose_mcg_kg_min,
                self.weight_kg,
                self.infusion_method,
                self.drop_factor
            )
        return self._result
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        result = self.calculate()
        # Get bag volume from result or calculate from method
        bag_volume = result.get("volume_ml", 50 if self.infusion_method == "syringe_pump_50ml" else 500)
        return {
            "drug_name": self.drug_name,
            "dose_mcg_kg_min": self.dose_mcg_kg_min,
            "weight_kg": self.weight_kg,
            "infusion_method": self.infusion_method,
            "drop_factor": self.drop_factor,
            "infusion_rate_ml_hour": result.get("infusion_rate_ml_hour", 0),
            "drop_rate_gtt_min": result.get("drop_rate_gtt_min"),
            "total_dose_mcg_hour": result.get("total_dose_mcg_hour", 0),
            "concentration_mcg_ml": result.get("concentration_mcg_ml", 0),
            "preparation": result.get("preparation_instructions", ""),
            "bag_volume_ml": bag_volume
        }


def add_infusion(
    infusions: List[InfusionItem],
    drug_name: str,
    dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    drop_factor: Optional[int] = None
) -> InfusionItem:
    """
    Add an infusion to the list.
    
    Args:
        infusions: List of existing infusions
        drug_name: Name of drug
        dose_mcg_kg_min: Dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: Infusion method
        drop_factor: Optional drop factor
    
    Returns:
        New InfusionItem
    """
    new_infusion = InfusionItem(
        drug_name,
        dose_mcg_kg_min,
        weight_kg,
        infusion_method,
        drop_factor
    )
    infusions.append(new_infusion)
    return new_infusion


def remove_infusion(infusions: List[InfusionItem], index: int) -> bool:
    """
    Remove an infusion from the list.
    
    Args:
        infusions: List of infusions
        index: Index to remove
    
    Returns:
        True if removed successfully
    """
    if 0 <= index < len(infusions):
        infusions.pop(index)
        return True
    return False


def calculate_total_volume(infusions: List[InfusionItem], same_bag: bool = False) -> Dict:
    """
    Calculate total volume if using same bag.
    
    Args:
        infusions: List of infusions
        same_bag: Whether all drugs are in the same bag
    
    Returns:
        Dictionary with total volume details
    """
    if not infusions:
        return {
            "total_volume_ml": 0,
            "bag_volume_ml": 0,
            "can_fit": True
        }
    
    # Get standard volume from first infusion
    first_result = infusions[0].calculate()
    bag_volume = first_result.get("volume_ml", 50 if infusions[0].infusion_method == "syringe_pump_50ml" else 500)
    
    if same_bag:
        # If same bag, total volume is the bag volume
        total_volume = bag_volume
    else:
        # If separate bags, sum all volumes
        total_volume = sum(
            item.calculate().get("bag_volume_ml", 50) for item in infusions
        )
    
    # Check if can fit (assuming max 500ml per bag)
    max_volume_per_bag = 500
    can_fit = total_volume <= max_volume_per_bag if same_bag else True
    
    return {
        "total_volume_ml": round(total_volume, 2),
        "bag_volume_ml": bag_volume,
        "can_fit": can_fit,
        "same_bag": same_bag
    }


def calculate_total_rate(infusions: List[InfusionItem]) -> Dict:
    """
    Calculate total infusion rate.
    
    Args:
        infusions: List of infusions
    
    Returns:
        Dictionary with total rate details
    """
    if not infusions:
        return {
            "total_rate_ml_hour": 0,
            "total_drop_rate_gtt_min": None,
            "total_dose_mcg_hour": 0
        }
    
    total_rate_ml_hour = sum(
        item.calculate().get("infusion_rate_ml_hour", 0) for item in infusions
    )
    
    total_dose_mcg_hour = sum(
        item.calculate().get("total_dose_mcg_hour", 0) for item in infusions
    )
    
    # Calculate total drop rate if all have same drop factor
    drop_factors = [item.drop_factor for item in infusions if item.drop_factor]
    if drop_factors and len(set(drop_factors)) == 1:
        drop_factor = drop_factors[0]
        total_drop_rate = (total_rate_ml_hour * drop_factor) / 60
    else:
        total_drop_rate = None
    
    return {
        "total_rate_ml_hour": round(total_rate_ml_hour, 2),
        "total_drop_rate_gtt_min": round(total_drop_rate, 1) if total_drop_rate else None,
        "total_dose_mcg_hour": round(total_dose_mcg_hour, 2)
    }


def validate_limits(
    total_volume_ml: float,
    total_rate_ml_hour: float,
    same_bag: bool = False
) -> Dict:
    """
    Validate against safety limits.
    
    Args:
        total_volume_ml: Total volume in ml
        total_rate_ml_hour: Total rate in ml/hour
        same_bag: Whether using same bag
    
    Returns:
        Dictionary with validation results and warnings
    """
    warnings = []
    errors = []
    
    # Volume limits
    max_volume_per_bag = 500
    if same_bag and total_volume_ml > max_volume_per_bag:
        errors.append(f"Tổng thể tích ({total_volume_ml:.1f}ml) vượt quá giới hạn ({max_volume_per_bag}ml/bag)")
    elif same_bag and total_volume_ml > max_volume_per_bag * 0.8:
        warnings.append(f"Tổng thể tích ({total_volume_ml:.1f}ml) gần đạt giới hạn ({max_volume_per_bag}ml/bag)")
    
    # Rate limits
    max_rate_ml_hour = 1000  # Reasonable limit
    if total_rate_ml_hour > max_rate_ml_hour:
        errors.append(f"Tổng tốc độ ({total_rate_ml_hour:.1f}ml/h) vượt quá giới hạn ({max_rate_ml_hour}ml/h)")
    elif total_rate_ml_hour > max_rate_ml_hour * 0.8:
        warnings.append(f"Tổng tốc độ ({total_rate_ml_hour:.1f}ml/h) gần đạt giới hạn ({max_rate_ml_hour}ml/h)")
    
    return {
        "is_valid": len(errors) == 0,
        "warnings": warnings,
        "errors": errors
    }


def calculate_multiple_infusions_summary(infusions: List[InfusionItem], same_bag: bool = False) -> Dict:
    """
    Calculate complete summary for multiple infusions.
    
    Args:
        infusions: List of infusions
        same_bag: Whether using same bag
    
    Returns:
        Complete summary dictionary
    """
    if not infusions:
        return {
            "infusions": [],
            "total_volume": {"total_volume_ml": 0},
            "total_rate": {"total_rate_ml_hour": 0},
            "validation": {"is_valid": True, "warnings": [], "errors": []}
        }
    
    # Calculate totals
    total_volume = calculate_total_volume(infusions, same_bag)
    total_rate = calculate_total_rate(infusions)
    
    # Validate
    validation = validate_limits(
        total_volume["total_volume_ml"],
        total_rate["total_rate_ml_hour"],
        same_bag
    )
    
    # Get individual infusion details
    infusion_details = [item.to_dict() for item in infusions]
    
    return {
        "infusions": infusion_details,
        "total_volume": total_volume,
        "total_rate": total_rate,
        "validation": validation,
        "same_bag": same_bag
    }

