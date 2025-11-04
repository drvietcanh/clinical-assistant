"""
Antibiotic Dosing Calculator - Helper Functions
Weight calculations, renal category, CrCl, eGFR helpers
"""

def calculate_ibw(height_cm, sex):
    """Calculate Ideal Body Weight"""
    height_inch = height_cm / 2.54
    if sex == "Nam":
        ibw = 50 + 2.3 * (height_inch - 60)
    else:
        ibw = 45.5 + 2.3 * (height_inch - 60)
    return ibw



def calculate_abw(actual_weight, ibw):
    """Calculate Adjusted Body Weight for obesity"""
    return ibw + 0.4 * (actual_weight - ibw)



def calculate_bmi(weight_kg, height_cm):
    """Calculate BMI"""
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)



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
        CrCl in mL/min
    """
    dosing_weight = abw if use_abw and abw else weight_kg
    
    if sex == "Nam":
        crcl = ((140 - age) * dosing_weight) / (72 * scr_mgdl)
    else:
        crcl = ((140 - age) * dosing_weight) / (72 * scr_mgdl) * 0.85
    
    return round(crcl, 1)



def calculate_egfr_simplified(age, scr_mgdl, sex):
    """
    Calculate eGFR using simplified CKD-EPI formula
    
    Args:
        age: Age in years
        scr_mgdl: Serum creatinine in mg/dL
        sex: "Nam" or "Nữ"
    
    Returns:
        eGFR in mL/min/1.73m²
    """
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
    
    return round(egfr, 1)



