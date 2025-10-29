"""
Normal Laboratory Ranges
Reference ranges for common lab values
"""

# CBC - Complete Blood Count
CBC_RANGES = {
    "WBC": {
        "name": "White Blood Cells",
        "unit": "x10³/µL",
        "normal": {"min": 4.0, "max": 11.0},
        "critical_low": 2.0,
        "critical_high": 30.0,
        "vn_name": "Bạch cầu"
    },
    "RBC": {
        "name": "Red Blood Cells",
        "unit": "x10⁶/µL",
        "normal": {"min": 4.5, "max": 6.0, "male": True},
        "normal_female": {"min": 4.0, "max": 5.5},
        "vn_name": "Hồng cầu"
    },
    "Hemoglobin": {
        "name": "Hemoglobin",
        "unit": "g/dL",
        "normal": {"min": 13.5, "max": 17.5, "male": True},
        "normal_female": {"min": 12.0, "max": 16.0},
        "critical_low": 7.0,
        "critical_high": 20.0,
        "vn_name": "Hemoglobin",
        "si_unit": "g/L",
        "si_conversion": 10
    },
    "Hematocrit": {
        "name": "Hematocrit",
        "unit": "%",
        "normal": {"min": 40, "max": 52, "male": True},
        "normal_female": {"min": 36, "max": 48},
        "critical_low": 20,
        "critical_high": 60,
        "vn_name": "Hematocrit"
    },
    "MCV": {
        "name": "Mean Corpuscular Volume",
        "unit": "fL",
        "normal": {"min": 80, "max": 100},
        "vn_name": "MCV"
    },
    "MCH": {
        "name": "Mean Corpuscular Hemoglobin",
        "unit": "pg",
        "normal": {"min": 27, "max": 33},
        "vn_name": "MCH"
    },
    "MCHC": {
        "name": "Mean Corpuscular Hemoglobin Concentration",
        "unit": "g/dL",
        "normal": {"min": 32, "max": 36},
        "vn_name": "MCHC"
    },
    "Platelets": {
        "name": "Platelets",
        "unit": "x10³/µL",
        "normal": {"min": 150, "max": 400},
        "critical_low": 50,
        "critical_high": 1000,
        "vn_name": "Tiểu cầu"
    }
}

# Chemistry - Basic Metabolic Panel (BMP)
BMP_RANGES = {
    "Sodium": {
        "name": "Sodium",
        "unit": "mEq/L",
        "normal": {"min": 136, "max": 145},
        "critical_low": 120,
        "critical_high": 160,
        "vn_name": "Natri",
        "si_unit": "mmol/L"
    },
    "Potassium": {
        "name": "Potassium",
        "unit": "mEq/L",
        "normal": {"min": 3.5, "max": 5.0},
        "critical_low": 2.5,
        "critical_high": 6.5,
        "vn_name": "Kali",
        "si_unit": "mmol/L"
    },
    "Chloride": {
        "name": "Chloride",
        "unit": "mEq/L",
        "normal": {"min": 96, "max": 106},
        "vn_name": "Clo",
        "si_unit": "mmol/L"
    },
    "CO2": {
        "name": "Bicarbonate (CO2)",
        "unit": "mEq/L",
        "normal": {"min": 22, "max": 29},
        "critical_low": 10,
        "critical_high": 40,
        "vn_name": "Bicarbonate",
        "si_unit": "mmol/L"
    },
    "BUN": {
        "name": "Blood Urea Nitrogen",
        "unit": "mg/dL",
        "normal": {"min": 7, "max": 20},
        "critical_high": 100,
        "vn_name": "Ure máu",
        "si_unit": "mmol/L",
        "si_conversion": 0.357
    },
    "Creatinine": {
        "name": "Creatinine",
        "unit": "mg/dL",
        "normal": {"min": 0.7, "max": 1.3, "male": True},
        "normal_female": {"min": 0.6, "max": 1.1},
        "critical_high": 10,
        "vn_name": "Creatinine",
        "si_unit": "µmol/L",
        "si_conversion": 88.4
    },
    "Glucose": {
        "name": "Glucose (Fasting)",
        "unit": "mg/dL",
        "normal": {"min": 70, "max": 100},
        "critical_low": 40,
        "critical_high": 400,
        "vn_name": "Glucose",
        "si_unit": "mmol/L",
        "si_conversion": 0.0555
    },
    "Calcium": {
        "name": "Calcium",
        "unit": "mg/dL",
        "normal": {"min": 8.5, "max": 10.5},
        "critical_low": 6.0,
        "critical_high": 13.0,
        "vn_name": "Canxi",
        "si_unit": "mmol/L",
        "si_conversion": 0.25
    }
}

# Liver Function Tests (LFT)
LFT_RANGES = {
    "ALT": {
        "name": "Alanine Aminotransferase",
        "unit": "U/L",
        "normal": {"min": 7, "max": 56},
        "vn_name": "ALT (SGPT)",
        "si_unit": "U/L"
    },
    "AST": {
        "name": "Aspartate Aminotransferase",
        "unit": "U/L",
        "normal": {"min": 10, "max": 40},
        "vn_name": "AST (SGOT)",
        "si_unit": "U/L"
    },
    "ALP": {
        "name": "Alkaline Phosphatase",
        "unit": "U/L",
        "normal": {"min": 45, "max": 115},
        "vn_name": "Alkaline Phosphatase",
        "si_unit": "U/L"
    },
    "Bilirubin_Total": {
        "name": "Total Bilirubin",
        "unit": "mg/dL",
        "normal": {"min": 0.1, "max": 1.2},
        "critical_high": 12,
        "vn_name": "Bilirubin toàn phần",
        "si_unit": "µmol/L",
        "si_conversion": 17.1
    },
    "Bilirubin_Direct": {
        "name": "Direct Bilirubin",
        "unit": "mg/dL",
        "normal": {"min": 0, "max": 0.3},
        "vn_name": "Bilirubin trực tiếp",
        "si_unit": "µmol/L",
        "si_conversion": 17.1
    },
    "Albumin": {
        "name": "Albumin",
        "unit": "g/dL",
        "normal": {"min": 3.5, "max": 5.5},
        "critical_low": 2.0,
        "vn_name": "Albumin",
        "si_unit": "g/L",
        "si_conversion": 10
    },
    "Total_Protein": {
        "name": "Total Protein",
        "unit": "g/dL",
        "normal": {"min": 6.0, "max": 8.3},
        "vn_name": "Protein toàn phần",
        "si_unit": "g/L",
        "si_conversion": 10
    }
}

# Lipid Panel
LIPID_RANGES = {
    "Cholesterol": {
        "name": "Total Cholesterol",
        "unit": "mg/dL",
        "desirable": {"max": 200},
        "borderline": {"min": 200, "max": 239},
        "high": {"min": 240},
        "vn_name": "Cholesterol toàn phần",
        "si_unit": "mmol/L",
        "si_conversion": 0.0259
    },
    "LDL": {
        "name": "LDL Cholesterol",
        "unit": "mg/dL",
        "optimal": {"max": 100},
        "near_optimal": {"min": 100, "max": 129},
        "borderline": {"min": 130, "max": 159},
        "high": {"min": 160, "max": 189},
        "very_high": {"min": 190},
        "vn_name": "LDL-C",
        "si_unit": "mmol/L",
        "si_conversion": 0.0259
    },
    "HDL": {
        "name": "HDL Cholesterol",
        "unit": "mg/dL",
        "low": {"max": 40, "male": True},
        "low_female": {"max": 50},
        "normal": {"min": 40, "max": 60, "male": True},
        "normal_female": {"min": 50, "max": 60},
        "high": {"min": 60},
        "vn_name": "HDL-C",
        "si_unit": "mmol/L",
        "si_conversion": 0.0259
    },
    "Triglycerides": {
        "name": "Triglycerides",
        "unit": "mg/dL",
        "normal": {"max": 150},
        "borderline": {"min": 150, "max": 199},
        "high": {"min": 200, "max": 499},
        "very_high": {"min": 500},
        "vn_name": "Triglyceride",
        "si_unit": "mmol/L",
        "si_conversion": 0.0113
    }
}

# Cardiac Markers
CARDIAC_RANGES = {
    "Troponin_I": {
        "name": "Troponin I",
        "unit": "ng/mL",
        "normal": {"max": 0.04},
        "elevated": {"min": 0.04},
        "vn_name": "Troponin I"
    },
    "Troponin_T": {
        "name": "Troponin T",
        "unit": "ng/mL",
        "normal": {"max": 0.01},
        "elevated": {"min": 0.01},
        "vn_name": "Troponin T"
    },
    "BNP": {
        "name": "B-type Natriuretic Peptide",
        "unit": "pg/mL",
        "normal": {"max": 100},
        "vn_name": "BNP"
    },
    "NT_proBNP": {
        "name": "NT-proBNP",
        "unit": "pg/mL",
        "normal_under_50": {"max": 125},
        "normal_50_75": {"max": 450},
        "normal_over_75": {"max": 900},
        "vn_name": "NT-proBNP"
    },
    "CK_MB": {
        "name": "Creatine Kinase-MB",
        "unit": "ng/mL",
        "normal": {"max": 5.0},
        "vn_name": "CK-MB"
    }
}

# Coagulation
COAG_RANGES = {
    "PT": {
        "name": "Prothrombin Time",
        "unit": "seconds",
        "normal": {"min": 11, "max": 13.5},
        "vn_name": "PT"
    },
    "INR": {
        "name": "International Normalized Ratio",
        "unit": "",
        "normal": {"min": 0.8, "max": 1.2},
        "therapeutic_afib": {"min": 2.0, "max": 3.0},
        "therapeutic_mechanical": {"min": 2.5, "max": 3.5},
        "critical_high": 5.0,
        "vn_name": "INR"
    },
    "aPTT": {
        "name": "Activated Partial Thromboplastin Time",
        "unit": "seconds",
        "normal": {"min": 25, "max": 35},
        "therapeutic": {"min": 60, "max": 80},
        "vn_name": "aPTT"
    },
    "Fibrinogen": {
        "name": "Fibrinogen",
        "unit": "mg/dL",
        "normal": {"min": 200, "max": 400},
        "vn_name": "Fibrinogen"
    },
    "D_dimer": {
        "name": "D-dimer",
        "unit": "µg/mL",
        "normal": {"max": 0.5},
        "vn_name": "D-dimer"
    }
}

# Thyroid
THYROID_RANGES = {
    "TSH": {
        "name": "Thyroid Stimulating Hormone",
        "unit": "mIU/L",
        "normal": {"min": 0.4, "max": 4.0},
        "vn_name": "TSH"
    },
    "Free_T4": {
        "name": "Free T4",
        "unit": "ng/dL",
        "normal": {"min": 0.8, "max": 1.8},
        "vn_name": "FT4",
        "si_unit": "pmol/L",
        "si_conversion": 12.87
    },
    "Free_T3": {
        "name": "Free T3",
        "unit": "pg/mL",
        "normal": {"min": 2.3, "max": 4.2},
        "vn_name": "FT3",
        "si_unit": "pmol/L",
        "si_conversion": 1.54
    }
}

# Additional chemistry
ADDITIONAL_RANGES = {
    "HbA1c": {
        "name": "Hemoglobin A1c",
        "unit": "%",
        "normal": {"max": 5.7},
        "prediabetes": {"min": 5.7, "max": 6.4},
        "diabetes": {"min": 6.5},
        "vn_name": "HbA1c"
    },
    "Magnesium": {
        "name": "Magnesium",
        "unit": "mg/dL",
        "normal": {"min": 1.7, "max": 2.2},
        "critical_low": 1.0,
        "vn_name": "Magiê",
        "si_unit": "mmol/L",
        "si_conversion": 0.411
    },
    "Phosphate": {
        "name": "Phosphate",
        "unit": "mg/dL",
        "normal": {"min": 2.5, "max": 4.5},
        "vn_name": "Phosphate",
        "si_unit": "mmol/L",
        "si_conversion": 0.323
    },
    "Uric_Acid": {
        "name": "Uric Acid",
        "unit": "mg/dL",
        "normal": {"min": 3.5, "max": 7.2, "male": True},
        "normal_female": {"min": 2.6, "max": 6.0},
        "vn_name": "Acid uric",
        "si_unit": "µmol/L",
        "si_conversion": 59.48
    }
}

# Combine all ranges
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

