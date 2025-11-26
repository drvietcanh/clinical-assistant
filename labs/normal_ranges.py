"""
Normal Laboratory Ranges
Reference ranges for common lab values
Loads from JSON file for easier maintenance
"""

import json
from pathlib import Path

# Load lab ranges from JSON file
_lab_ranges_file = Path(__file__).parent.parent / "data" / "lab_ranges.json"

try:
    with open(_lab_ranges_file, "r", encoding="utf-8") as f:
        _lab_data = json.load(f)
    
    CBC_RANGES = _lab_data.get("CBC_RANGES", {})
    BMP_RANGES = _lab_data.get("BMP_RANGES", {})
    LFT_RANGES = _lab_data.get("LFT_RANGES", {})
    LIPID_RANGES = _lab_data.get("LIPID_RANGES", {})
    CARDIAC_RANGES = _lab_data.get("CARDIAC_RANGES", {})
    COAG_RANGES = _lab_data.get("COAG_RANGES", {})
    THYROID_RANGES = _lab_data.get("THYROID_RANGES", {})
    ADDITIONAL_RANGES = _lab_data.get("ADDITIONAL_RANGES", {})
    # CMP (Comprehensive Metabolic Panel) = BMP + LFT
    CMP_RANGES = {**BMP_RANGES, **LFT_RANGES}
except FileNotFoundError:
    # Fallback to empty dicts if JSON not found
    CBC_RANGES = {}
    BMP_RANGES = {}
    LFT_RANGES = {}
    LIPID_RANGES = {}
    CARDIAC_RANGES = {}
    COAG_RANGES = {}
    THYROID_RANGES = {}
    ADDITIONAL_RANGES = {}
    # CMP (Comprehensive Metabolic Panel) = BMP + LFT
    CMP_RANGES = {}

# Combine all ranges
# Note: CMP_RANGES is BMP + LFT combined, so we don't need to add it separately here
ALL_RANGES = {
    **CBC_RANGES,
    **BMP_RANGES,
    **LFT_RANGES,
    **LIPID_RANGES,
    **CARDIAC_RANGES,
    **COAG_RANGES,
    **THYROID_RANGES,
    **ADDITIONAL_RANGES
}


def get_normal_range(test_name, gender="male", age=None):
    """Get normal range for a lab test"""
    if test_name not in ALL_RANGES:
        return None
    
    test = ALL_RANGES[test_name]
    
    # Handle gender-specific ranges
    if gender == "female" and "normal_female" in test:
        return test["normal_female"]
    
    return test.get("normal", {})


def is_critical(test_name, value):
    """Check if value is critically abnormal"""
    if test_name not in ALL_RANGES:
        return False
    
    test = ALL_RANGES[test_name]
    
    if "critical_low" in test and value < test["critical_low"]:
        return True
    
    if "critical_high" in test and value > test["critical_high"]:
        return True
    
    return False


def interpret_value(test_name, value, gender="male", age=None):
    """Interpret lab value"""
    if test_name not in ALL_RANGES:
        return "Unknown test"
    
    test = ALL_RANGES[test_name]
    normal = get_normal_range(test_name, gender, age)
    
    # Check critical
    if is_critical(test_name, value):
        if value < test.get("critical_low", float('-inf')):
            return "CRITICALLY LOW ⚠️"
        else:
            return "CRITICALLY HIGH ⚠️"
    
    # Check normal range
    if "min" in normal and "max" in normal:
        if value < normal["min"]:
            return "Low ⬇️"
        elif value > normal["max"]:
            return "High ⬆️"
        else:
            return "Normal ✓"
    
    # Check max only (like HbA1c, Cholesterol)
    if "max" in normal and "min" not in normal:
        if value <= normal["max"]:
            return "Normal ✓"
        else:
            return "High ⬆️"
    
    return "See reference ranges"
