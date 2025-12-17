"""Conversion functions for Drug Infusion Rate Conversion (DIRC)."""


def mcg_kg_min_to_ml_hr(dose_mcg_kg_min: float, weight_kg: float, concentration_mg_ml: float) -> float:
    """Convert mcg/kg/min to mL/hr.

    Formula:
        mL/hr = (mcg/kg/min × kg × 60) / (mg/mL × 1000)
    """
    if concentration_mg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    return (dose_mcg_kg_min * weight_kg * 60) / (concentration_mg_ml * 1000)


def ml_hr_to_mcg_kg_min(ml_per_hr: float, weight_kg: float, concentration_mg_ml: float) -> float:
    """Convert mL/hr to mcg/kg/min.

    Formula:
        mcg/kg/min = (mL/hr × mg/mL × 1000) / (kg × 60)
    """
    if concentration_mg_ml <= 0:
        raise ValueError("Concentration must be > 0")
    if weight_kg <= 0:
        raise ValueError("Weight must be > 0")
    return (ml_per_hr * concentration_mg_ml * 1000) / (weight_kg * 60)


