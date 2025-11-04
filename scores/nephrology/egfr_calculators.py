"""
eGFR Calculator - eGFR Calculation Functions
Các công thức tính eGFR (CKD-EPI, MDRD, Cockcroft-Gault)
"""

def calculate_ckd_epi(creatinine_mg, age, gender, race="non-black"):
    """
    CKD-EPI 2009 formula
    
    Returns eGFR in mL/min/1.73m²
    """
    # Gender-specific parameters
    kappa = 0.7 if gender == "female" else 0.9
    alpha = -0.329 if gender == "female" else -0.411
    gender_factor = 1.018 if gender == "female" else 1.0
    
    # Race factor
    race_factor = 1.159 if race == "black" else 1.0
    
    # Calculate
    min_val = min(creatinine_mg / kappa, 1)
    max_val = max(creatinine_mg / kappa, 1)
    
    egfr = 141 * (min_val ** alpha) * (max_val ** -1.209) * (0.993 ** age) * gender_factor * race_factor
    
    return egfr



def calculate_mdrd(creatinine_mg, age, gender, race="non-black"):
    """
    MDRD formula
    
    Returns eGFR in mL/min/1.73m²
    """
    # Gender factor
    gender_factor = 0.742 if gender == "female" else 1.0
    
    # Race factor
    race_factor = 1.212 if race == "black" else 1.0
    
    # Calculate
    egfr = 175 * (creatinine_mg ** -1.154) * (age ** -0.203) * gender_factor * race_factor
    
    return egfr



def calculate_cockcroft_gault(age, weight_kg, creatinine_mg, gender, use_abw=False, abw=None):
    """
    Cockcroft-Gault formula for Creatinine Clearance
    
    Returns CrCl in mL/min
    """
    # Use ABW if specified
    weight_to_use = abw if (use_abw and abw) else weight_kg
    
    # Cockcroft-Gault formula
    crcl = ((140 - age) * weight_to_use) / (72 * creatinine_mg)
    
    if gender == "female":
        crcl = crcl * 0.85
    
    return crcl



def calculate_abw(actual_weight, ibw):
    """Calculate Adjusted Body Weight for obesity"""
    abw = ibw + 0.4 * (actual_weight - ibw)
    return abw



def calculate_ibw(height_cm, gender):
    """Calculate Ideal Body Weight using Devine formula"""
    if gender == "male":
        ibw = 50 + 0.91 * (height_cm - 152.4)
    else:  # female
        ibw = 45.5 + 0.91 * (height_cm - 152.4)
    
    return max(ibw, 0)



