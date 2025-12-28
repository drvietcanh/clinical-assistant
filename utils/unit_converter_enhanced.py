"""
Enhanced Unit Converter
Auto-detection, context-aware conversion, and extended unit support
"""

from typing import Dict, Optional, List, Tuple
import re

# Import existing converters
from utils.converter import (
    convert_creatinine,
    convert_glucose,
    convert_cholesterol,
    convert_bilirubin,
    convert_bun,
    convert_triglycerides
)


# Unit patterns for auto-detection
UNIT_PATTERNS = {
    "creatinine": {
        "mg/dL": [r"mg/dl", r"mg/dL", r"mg/100ml"],
        "µmol/L": [r"µmol/l", r"µmol/L", r"umol/l", r"umol/L", r"micromol/l"],
        "mmol/L": [r"mmol/l", r"mmol/L"]
    },
    "glucose": {
        "mg/dL": [r"mg/dl", r"mg/dL", r"mg/100ml"],
        "mmol/L": [r"mmol/l", r"mmol/L"]
    },
    "cholesterol": {
        "mg/dL": [r"mg/dl", r"mg/dL", r"mg/100ml"],
        "mmol/L": [r"mmol/l", r"mmol/L"]
    },
    "bilirubin": {
        "mg/dL": [r"mg/dl", r"mg/dL", r"mg/100ml"],
        "µmol/L": [r"µmol/l", r"µmol/L", r"umol/l", r"umol/L"]
    },
    "hemoglobin": {
        "g/dL": [r"g/dl", r"g/dL", r"g/100ml", r"g%"],
        "g/L": [r"g/l", r"g/L"]
    },
    "albumin": {
        "g/dL": [r"g/dl", r"g/dL", r"g/100ml"],
        "g/L": [r"g/l", r"g/L"]
    }
}


def detect_unit(value_str: str, context: Optional[str] = None) -> Optional[Tuple[str, str]]:
    """
    Auto-detect unit from input string.
    
    Args:
        value_str: Input string (e.g., "5.2 mg/dL", "120")
        context: Optional context hint (e.g., "creatinine", "glucose")
    
    Returns:
        Tuple of (value, unit) or None if cannot detect
    """
    if not value_str:
        return None
    
    # Try to extract number and unit
    # Pattern: number followed by unit
    pattern = r'([\d.]+)\s*([a-zA-Zµ/]+)'
    match = re.search(pattern, value_str, re.IGNORECASE)
    
    if match:
        value = float(match.group(1))
        unit_str = match.group(2).strip()
        
        # If context provided, check against context patterns
        if context and context in UNIT_PATTERNS:
            for unit, patterns in UNIT_PATTERNS[context].items():
                for pattern in patterns:
                    if re.match(pattern, unit_str, re.IGNORECASE):
                        return (value, unit)
        
        # Try to match against all patterns
        for param_type, units in UNIT_PATTERNS.items():
            for unit, patterns in units.items():
                for pattern in patterns:
                    if re.match(pattern, unit_str, re.IGNORECASE):
                        return (value, unit)
    
    # If no unit found, try to extract just number
    try:
        value = float(value_str.strip())
        return (value, None)  # Unit unknown
    except ValueError:
        return None


def convert_with_auto_detect(
    value_str: str,
    target_unit: str,
    context: Optional[str] = None
) -> Optional[Dict]:
    """
    Convert with auto-detection of input unit.
    
    Args:
        value_str: Input string (e.g., "5.2 mg/dL")
        target_unit: Target unit (e.g., "µmol/L")
        context: Optional context hint
    
    Returns:
        Dictionary with conversion result:
        {
            "value": float,
            "from_unit": str,
            "to_unit": str,
            "converted_value": float
        }
    """
    # Detect unit
    detected = detect_unit(value_str, context)
    if not detected:
        return None
    
    value, from_unit = detected
    
    if from_unit is None:
        return None
    
    if from_unit == target_unit:
        return {
            "value": value,
            "from_unit": from_unit,
            "to_unit": target_unit,
            "converted_value": value
        }
    
    # Perform conversion based on context
    if context == "creatinine":
        converted = convert_creatinine(value, from_unit, target_unit)
    elif context == "glucose":
        converted = convert_glucose(value, from_unit, target_unit)
    elif context == "cholesterol":
        converted = convert_cholesterol(value, from_unit, target_unit)
    elif context == "bilirubin":
        converted = convert_bilirubin(value, from_unit, target_unit)
    elif context == "bun":
        converted = convert_bun(value, from_unit, target_unit)
    elif context == "triglycerides":
        converted = convert_triglycerides(value, from_unit, target_unit)
    else:
        # Try generic conversion
        converted = _generic_convert(value, from_unit, target_unit, context)
    
    return {
        "value": value,
        "from_unit": from_unit,
        "to_unit": target_unit,
        "converted_value": converted
    }


def _generic_convert(
    value: float,
    from_unit: str,
    to_unit: str,
    context: Optional[str] = None
) -> float:
    """
    Generic conversion function.
    Handles common conversions not covered by specific functions.
    """
    # Hemoglobin: g/dL ↔ g/L
    if "hemoglobin" in (context or "").lower() or "hgb" in (context or "").lower():
        if from_unit == "g/dL" and to_unit == "g/L":
            return value * 10
        elif from_unit == "g/L" and to_unit == "g/dL":
            return value / 10
    
    # Albumin: g/dL ↔ g/L
    if "albumin" in (context or "").lower():
        if from_unit == "g/dL" and to_unit == "g/L":
            return value * 10
        elif from_unit == "g/L" and to_unit == "g/dL":
            return value / 10
    
    # If no conversion found, return original value
    return value


def get_available_units(context: str) -> List[str]:
    """
    Get list of available units for a given context.
    
    Args:
        context: Context (e.g., "creatinine", "glucose")
    
    Returns:
        List of available units
    """
    if context in UNIT_PATTERNS:
        return list(UNIT_PATTERNS[context].keys())
    return []


def convert_value(
    value: float,
    from_unit: str,
    to_unit: str,
    context: Optional[str] = None
) -> float:
    """
    Convert value between units with context awareness.
    
    Args:
        value: Value to convert
        from_unit: Source unit
        to_unit: Target unit
        context: Optional context hint
    
    Returns:
        Converted value
    """
    if from_unit == to_unit:
        return value
    
    # Use context-specific converter if available
    if context == "creatinine":
        return convert_creatinine(value, from_unit, to_unit)
    elif context == "glucose":
        return convert_glucose(value, from_unit, to_unit)
    elif context == "cholesterol":
        return convert_cholesterol(value, from_unit, to_unit)
    elif context == "bilirubin":
        return convert_bilirubin(value, from_unit, to_unit)
    elif context == "bun":
        return convert_bun(value, from_unit, to_unit)
    elif context == "triglycerides":
        return convert_triglycerides(value, from_unit, to_unit)
    else:
        # Try generic conversion
        return _generic_convert(value, from_unit, to_unit, context)


def format_unit_conversion_result(
    value: float,
    from_unit: str,
    to_unit: str,
    converted_value: float
) -> str:
    """
    Format unit conversion result as string.
    
    Returns:
        Formatted string (e.g., "5.2 mg/dL = 460 µmol/L")
    """
    return f"{value:.2f} {from_unit} = {converted_value:.2f} {to_unit}"

