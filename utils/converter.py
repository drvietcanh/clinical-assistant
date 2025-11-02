"""
Unit Conversion Utilities
Common unit conversions for clinical values
"""


def convert_creatinine(value, from_unit, to_unit):
    """
    Convert Creatinine between mg/dL and µmol/L
    
    Args:
        value: Numeric value to convert
        from_unit: "mg/dL" or "µmol/L"
        to_unit: "mg/dL" or "µmol/L"
    
    Returns:
        Converted value
    """
    if from_unit == to_unit:
        return value
    
    if from_unit == "mg/dL" and to_unit == "µmol/L":
        return value * 88.4
    elif from_unit == "µmol/L" and to_unit == "mg/dL":
        return value / 88.4
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


def convert_glucose(value, from_unit, to_unit):
    """
    Convert Glucose between mg/dL and mmol/L
    
    Args:
        value: Numeric value to convert
        from_unit: "mg/dL" or "mmol/L"
        to_unit: "mg/dL" or "mmol/L"
    
    Returns:
        Converted value
    """
    if from_unit == to_unit:
        return value
    
    if from_unit == "mg/dL" and to_unit == "mmol/L":
        return value * 0.0555
    elif from_unit == "mmol/L" and to_unit == "mg/dL":
        return value / 0.0555
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


def convert_cholesterol(value, from_unit, to_unit):
    """
    Convert Cholesterol between mg/dL and mmol/L
    
    Args:
        value: Numeric value to convert
        from_unit: "mg/dL" or "mmol/L"
        to_unit: "mg/dL" or "mmol/L"
    
    Returns:
        Converted value (rounded to 2 decimals)
    """
    if from_unit == to_unit:
        return round(value, 2)
    
    if from_unit == "mg/dL" and to_unit == "mmol/L":
        return round(value * 0.0259, 2)
    elif from_unit == "mmol/L" and to_unit == "mg/dL":
        return round(value / 0.0259, 2)
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


def convert_bilirubin(value, from_unit, to_unit):
    """
    Convert Bilirubin between mg/dL and µmol/L
    
    Args:
        value: Numeric value to convert
        from_unit: "mg/dL" or "µmol/L"
        to_unit: "mg/dL" or "µmol/L"
    
    Returns:
        Converted value
    """
    if from_unit == to_unit:
        return value
    
    if from_unit == "mg/dL" and to_unit == "µmol/L":
        return value * 17.1
    elif from_unit == "µmol/L" and to_unit == "mg/dL":
        return value / 17.1
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


def convert_bun(value, from_unit, to_unit):
    """
    Convert BUN (Blood Urea Nitrogen) between mg/dL and mmol/L
    
    Args:
        value: Numeric value to convert
        from_unit: "mg/dL" or "mmol/L"
        to_unit: "mg/dL" or "mmol/L"
    
    Returns:
        Converted value
    """
    if from_unit == to_unit:
        return value
    
    if from_unit == "mg/dL" and to_unit == "mmol/L":
        return value * 0.357
    elif from_unit == "mmol/L" and to_unit == "mg/dL":
        return value / 0.357
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


def convert_triglycerides(value, from_unit, to_unit):
    """
    Convert Triglycerides between mg/dL and mmol/L
    
    Args:
        value: Numeric value to convert
        from_unit: "mg/dL" or "mmol/L"
        to_unit: "mg/dL" or "mmol/L"
    
    Returns:
        Converted value (rounded to 2 decimals)
    """
    if from_unit == to_unit:
        return round(value, 2)
    
    if from_unit == "mg/dL" and to_unit == "mmol/L":
        return round(value * 0.0113, 2)
    elif from_unit == "mmol/L" and to_unit == "mg/dL":
        return round(value / 0.0113, 2)
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


def convert_pao2(value, from_unit, to_unit):
    """
    Convert PaO2 between mmHg and kPa
    
    Args:
        value: Numeric value to convert
        from_unit: "mmHg" or "kPa"
        to_unit: "mmHg" or "kPa"
    
    Returns:
        Converted value (rounded to 1 decimal)
    """
    if from_unit == to_unit:
        return round(value, 1)
    
    if from_unit == "mmHg" and to_unit == "kPa":
        return round(value / 7.5, 1)
    elif from_unit == "kPa" and to_unit == "mmHg":
        return round(value * 7.5, 1)
    else:
        raise ValueError(f"Invalid conversion: {from_unit} → {to_unit}")


# Conversion lookup table
CONVERSION_FACTORS = {
    "creatinine": {"mg/dL_to_µmol/L": 88.4, "µmol/L_to_mg/dL": 1/88.4},
    "glucose": {"mg/dL_to_mmol/L": 0.0555, "mmol/L_to_mg/dL": 1/0.0555},
    "cholesterol": {"mg/dL_to_mmol/L": 0.0259, "mmol/L_to_mg/dL": 1/0.0259},
    "bilirubin": {"mg/dL_to_µmol/L": 17.1, "µmol/L_to_mg/dL": 1/17.1},
    "bun": {"mg/dL_to_mmol/L": 0.357, "mmol/L_to_mg/dL": 1/0.357},
    "triglycerides": {"mg/dL_to_mmol/L": 0.0113, "mmol/L_to_mg/dL": 1/0.0113},
    "pao2": {"mmHg_to_kPa": 1/7.5, "kPa_to_mmHg": 7.5},
}

