"""
Antibiotic Dosing Calculator - Helper Functions
Weight calculations, renal category, CrCl, eGFR helpers
"""

def calculate_ibw(height_cm, sex):
    """
    Calculate Ideal Body Weight
    
    Args:
        height_cm: Height in centimeters (must be > 0)
        sex: "Nam" or "Nữ"
    
    Returns:
        IBW in kg, or None if invalid input
    """
    # Validation
    if height_cm is None or height_cm <= 0:
        return None
    if height_cm < 50 or height_cm > 250:  # Reasonable range
        return None
    if sex not in ["Nam", "Nữ"]:
        return None
    
    height_inch = height_cm / 2.54
    if sex == "Nam":
        ibw = 50 + 2.3 * (height_inch - 60)
    else:
        ibw = 45.5 + 2.3 * (height_inch - 60)
    
    # Ensure positive value
    return max(ibw, 0)



def calculate_abw(actual_weight, ibw):
    """
    Calculate Adjusted Body Weight for obesity
    
    Args:
        actual_weight: Actual weight in kg
        ibw: Ideal body weight in kg
    
    Returns:
        ABW in kg, or None if invalid input
    """
    # Validation
    if actual_weight is None or ibw is None:
        return None
    if actual_weight <= 0 or ibw <= 0:
        return None
    if actual_weight < ibw:
        # If actual weight is less than IBW, return actual weight
        return actual_weight
    
    return ibw + 0.4 * (actual_weight - ibw)



def calculate_bmi(weight_kg, height_cm):
    """
    Calculate BMI
    
    Args:
        weight_kg: Weight in kg
        height_cm: Height in cm
    
    Returns:
        BMI value, or None if invalid input
    """
    # Validation
    if weight_kg is None or height_cm is None:
        return None
    if weight_kg <= 0 or height_cm <= 0:
        return None
    if weight_kg > 500 or height_cm < 50 or height_cm > 250:  # Reasonable ranges
        return None
    
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)



def get_renal_category(crcl, egfr=None, is_hemodialysis=False, is_continuous_hd=False, is_peritoneal_dialysis=False):
    """
    Determine renal function category based on CrCl or eGFR
    
    Returns: 'normal', '30_60', '15_30', 'under_15', 'hemodialysis', 'continuous_hd', 'peritoneal_dialysis'
    """
    if is_continuous_hd:
        return 'continuous_hd'
    if is_hemodialysis:
        return 'hemodialysis'
    if is_peritoneal_dialysis:
        return 'peritoneal_dialysis'
    
    if crcl is None or crcl <= 0:
        return 'normal'
    
    if crcl >= 60:
        return 'normal'
    elif crcl >= 30:
        return '30_60'
    elif crcl >= 15:
        return '15_30'
    else:
        return 'under_15'



def calculate_crcl(age, weight_kg, scr_mgdl, sex, use_abw=False, abw=None):
    """
    Calculate CrCl using Cockcroft-Gault formula
    
    Args:
        age: Age in years
        weight_kg: Weight in kg (actual or ABW if use_abw=True)
        scr_mgdl: Serum creatinine in mg/dL
        sex: "Nam" or "Nữ"
        use_abw: Whether to use Adjusted Body Weight
        abw: Adjusted Body Weight if use_abw=True
    
    Returns:
        CrCl in mL/min, or None if invalid input
    """
    # Validation
    if age is None or weight_kg is None or scr_mgdl is None or sex is None:
        return None
    if age < 0 or age > 150:
        return None
    if weight_kg <= 0 or weight_kg > 500:
        return None
    if scr_mgdl <= 0 or scr_mgdl > 20:  # Reasonable range
        return None
    if sex not in ["Nam", "Nữ"]:
        return None
    
    # Handle edge case: CrCl = 0 or very low
    if scr_mgdl > 10:  # Very high creatinine, likely dialysis
        return 0
    
    dosing_weight = abw if use_abw and abw else weight_kg
    
    # Ensure positive values
    if dosing_weight <= 0:
        return None
    
    try:
        if sex == "Nam":
            crcl = ((140 - age) * dosing_weight) / (72 * scr_mgdl)
        else:
            crcl = ((140 - age) * dosing_weight) / (72 * scr_mgdl) * 0.85
        
        # Ensure non-negative
        crcl = max(0, crcl)
        
        # Cap at reasonable maximum (ARC can be high, but cap at 300)
        crcl = min(crcl, 300)
        
        return round(crcl, 1)
    except (ZeroDivisionError, ValueError):
        return None



def calculate_egfr_simplified(age, scr_mgdl, sex):
    """
    Calculate eGFR using simplified CKD-EPI formula
    
    Args:
        age: Age in years
        scr_mgdl: Serum creatinine in mg/dL
        sex: "Nam" or "Nữ"
    
    Returns:
        eGFR in mL/min/1.73m², or None if invalid input
    """
    # Validation
    if age is None or scr_mgdl is None or sex is None:
        return None
    if age < 0 or age > 150:
        return None
    if scr_mgdl <= 0 or scr_mgdl > 20:  # Reasonable range
        return None
    if sex not in ["Nam", "Nữ"]:
        return None
    
    try:
        if sex == "Nam":
            if scr_mgdl <= 0.9:
                egfr = 141 * ((scr_mgdl / 0.9) ** -0.411) * (0.993 ** age)
            else:
                egfr = 141 * ((scr_mgdl / 0.9) ** -1.209) * (0.993 ** age)
        else:
            if scr_mgdl <= 0.7:
                egfr = 144 * ((scr_mgdl / 0.7) ** -0.329) * (0.993 ** age)
            else:
                egfr = 144 * ((scr_mgdl / 0.7) ** -1.209) * (0.993 ** age)
        
        # Ensure non-negative and reasonable range
        egfr = max(0, egfr)
        egfr = min(egfr, 200)  # Cap at reasonable maximum
        
        return round(egfr, 1)
    except (ZeroDivisionError, ValueError, OverflowError):
        return None



