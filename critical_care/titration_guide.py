"""
Infusion Rate Titration Guide
Guide for adjusting infusion rates and tracking titration history
"""

from typing import Dict, List, Optional
from drugs.cardiovascular_calculator import calculate_complete_infusion


class TitrationStep:
    """Represents a single titration step."""
    
    def __init__(
        self,
        drug_name: str,
        old_dose_mcg_kg_min: float,
        new_dose_mcg_kg_min: float,
        weight_kg: float,
        infusion_method: str = "syringe_pump_50ml",
        drop_factor: Optional[int] = None,
        reason: Optional[str] = None
    ):
        self.drug_name = drug_name
        self.old_dose = old_dose_mcg_kg_min
        self.new_dose = new_dose_mcg_kg_min
        self.weight_kg = weight_kg
        self.infusion_method = infusion_method
        self.drop_factor = drop_factor
        self.reason = reason
        self._old_result = None
        self._new_result = None
    
    def calculate_changes(self) -> Dict:
        """Calculate changes between old and new doses."""
        # Calculate old infusion
        self._old_result = calculate_complete_infusion(
            self.drug_name,
            self.old_dose,
            self.weight_kg,
            self.infusion_method,
            self.drop_factor
        )
        
        # Calculate new infusion
        self._new_result = calculate_complete_infusion(
            self.drug_name,
            self.new_dose,
            self.weight_kg,
            self.infusion_method,
            self.drop_factor
        )
        
        # Calculate changes
        old_rate = self._old_result.get("infusion_rate_ml_hour", 0)
        new_rate = self._new_result.get("infusion_rate_ml_hour", 0)
        rate_change = new_rate - old_rate
        rate_change_percent = (rate_change / old_rate * 100) if old_rate > 0 else 0
        
        dose_change = self.new_dose - self.old_dose
        dose_change_percent = (dose_change / self.old_dose * 100) if self.old_dose > 0 else 0
        
        return {
            "old_dose": self.old_dose,
            "new_dose": self.new_dose,
            "dose_change": round(dose_change, 3),
            "dose_change_percent": round(dose_change_percent, 1),
            "old_rate_ml_hour": round(old_rate, 2),
            "new_rate_ml_hour": round(new_rate, 2),
            "rate_change_ml_hour": round(rate_change, 2),
            "rate_change_percent": round(rate_change_percent, 1),
            "old_drop_rate": self._old_result.get("drop_rate_gtt_min"),
            "new_drop_rate": self._new_result.get("drop_rate_gtt_min"),
            "old_total_dose_mcg_hour": self._old_result.get("total_dose_mcg_hour", 0),
            "new_total_dose_mcg_hour": self._new_result.get("total_dose_mcg_hour", 0)
        }
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        changes = self.calculate_changes()
        return {
            "drug_name": self.drug_name,
            "old_dose_mcg_kg_min": self.old_dose,
            "new_dose_mcg_kg_min": self.new_dose,
            "weight_kg": self.weight_kg,
            "reason": self.reason,
            **changes
        }


def calculate_titration(
    drug_name: str,
    old_dose_mcg_kg_min: float,
    new_dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    drop_factor: Optional[int] = None,
    reason: Optional[str] = None
) -> Dict:
    """
    Calculate titration from old dose to new dose.
    
    Args:
        drug_name: Name of drug
        old_dose_mcg_kg_min: Current dose in mcg/kg/min
        new_dose_mcg_kg_min: New dose in mcg/kg/min
        weight_kg: Weight in kg
        infusion_method: Infusion method
        drop_factor: Optional drop factor
        reason: Optional reason for titration
    
    Returns:
        Dictionary with titration details
    """
    step = TitrationStep(
        drug_name, old_dose_mcg_kg_min, new_dose_mcg_kg_min,
        weight_kg, infusion_method, drop_factor, reason
    )
    
    changes = step.calculate_changes()
    
    # Generate recommendations
    recommendations = []
    
    if changes["dose_change"] > 0:
        recommendations.append("Tăng liều - Theo dõi sát huyết áp và nhịp tim")
        if changes["dose_change_percent"] > 50:
            recommendations.append("⚠️ Tăng liều đáng kể (>50%) - Tăng từ từ và theo dõi sát")
    elif changes["dose_change"] < 0:
        recommendations.append("Giảm liều - Theo dõi đáp ứng")
        if abs(changes["dose_change_percent"]) > 50:
            recommendations.append("⚠️ Giảm liều đáng kể (>50%) - Theo dõi sát")
    else:
        recommendations.append("Không thay đổi liều")
    
    # Check rate change
    if abs(changes["rate_change_percent"]) > 20:
        recommendations.append(f"⚠️ Thay đổi tốc độ truyền đáng kể ({changes['rate_change_percent']:.1f}%)")
    
    return {
        **changes,
        "recommendations": recommendations,
        "reason": reason
    }


def add_titration_step(
    titration_history: List[Dict],
    drug_name: str,
    old_dose_mcg_kg_min: float,
    new_dose_mcg_kg_min: float,
    weight_kg: float,
    infusion_method: str = "syringe_pump_50ml",
    drop_factor: Optional[int] = None,
    reason: Optional[str] = None
) -> Dict:
    """
    Add a titration step to history.
    
    Args:
        titration_history: List of previous titration steps
        drug_name: Name of drug
        old_dose_mcg_kg_min: Current dose
        new_dose_mcg_kg_min: New dose
        weight_kg: Weight in kg
        infusion_method: Infusion method
        drop_factor: Optional drop factor
        reason: Optional reason
    
    Returns:
        Titration step dictionary
    """
    step = TitrationStep(
        drug_name, old_dose_mcg_kg_min, new_dose_mcg_kg_min,
        weight_kg, infusion_method, drop_factor, reason
    )
    
    step_dict = step.to_dict()
    titration_history.append(step_dict)
    
    return step_dict


def get_titration_summary(titration_history: List[Dict]) -> Dict:
    """
    Get summary of titration history.
    
    Args:
        titration_history: List of titration steps
    
    Returns:
        Summary dictionary
    """
    if not titration_history:
        return {
            "total_steps": 0,
            "current_dose": None,
            "initial_dose": None,
            "total_increase": 0,
            "total_decrease": 0,
            "net_change": 0
        }
    
    initial_dose = titration_history[0].get("old_dose_mcg_kg_min", 0)
    current_dose = titration_history[-1].get("new_dose_mcg_kg_min", 0)
    
    total_increase = sum(
        step.get("dose_change", 0) for step in titration_history
        if step.get("dose_change", 0) > 0
    )
    
    total_decrease = abs(sum(
        step.get("dose_change", 0) for step in titration_history
        if step.get("dose_change", 0) < 0
    ))
    
    net_change = current_dose - initial_dose
    
    return {
        "total_steps": len(titration_history),
        "current_dose": round(current_dose, 3),
        "initial_dose": round(initial_dose, 3),
        "total_increase": round(total_increase, 3),
        "total_decrease": round(total_decrease, 3),
        "net_change": round(net_change, 3),
        "net_change_percent": round((net_change / initial_dose * 100) if initial_dose > 0 else 0, 1)
    }

