"""
Unit Converter for Lab Values
Convert between conventional and SI units
"""

from .normal_ranges import ALL_RANGES


def convert_units(test_name, value, from_unit, to_unit):
    """
    Convert lab value between units
    
    Args:
        test_name: Name of the lab test
        value: Numeric value to convert
        from_unit: Current unit
        to_unit: Target unit
    
    Returns:
        Converted value or None if conversion not available
    """
    if test_name not in ALL_RANGES:
        return None
    
    test = ALL_RANGES[test_name]
    
    # Check if SI conversion available
    if "si_unit" not in test or "si_conversion" not in test:
        return None
    
    conventional_unit = test["unit"]
    si_unit = test["si_unit"]
    conversion_factor = test["si_conversion"]
    
    # Convert from conventional to SI
    if from_unit == conventional_unit and to_unit == si_unit:
        return value * conversion_factor
    
    # Convert from SI to conventional
    if from_unit == si_unit and to_unit == conventional_unit:
        return value / conversion_factor
    
    return None


def get_available_units(test_name):
    """Get list of available units for a test"""
    if test_name not in ALL_RANGES:
        return []
    
    test = ALL_RANGES[test_name]
    units = [test["unit"]]
    
    if "si_unit" in test:
        units.append(test["si_unit"])
    
    return units

