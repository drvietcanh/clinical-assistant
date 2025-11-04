"""
eGFR Calculator - BSA (Body Surface Area) Functions
Các công thức tính diện tích da cơ thể
"""

import math

def calculate_bsa_mosteller(weight_kg, height_cm):
    """
    BSA using Mosteller formula - Recommended by KDIGO, FDA, NCCN, NIH
    
    Formula: BSA = √[(height_cm × weight_kg) / 3600]
    
    Mosteller is the optimal standard for clinical practice:
    - Simple, easy to remember
    - Low error (< 5%)
    - Recommended by major organizations
    """
    bsa = math.sqrt((weight_kg * height_cm) / 3600)
    return bsa



def calculate_bsa_dubois(weight_kg, height_cm):
    """
    BSA using Du Bois formula (1916) - Classic formula
    
    Formula: BSA = 0.007184 × W^0.425 × H^0.725
    
    Used as the basis for eGFR standardization to 1.73 m²
    """
    bsa = 0.007184 * (weight_kg ** 0.425) * (height_cm ** 0.725)
    return bsa



def calculate_bsa_haycock(weight_kg, height_cm):
    """
    BSA using Haycock formula (1978)
    
    Formula: BSA = 0.024265 × W^0.5378 × H^0.3964
    
    Validated from newborns to adults, good for all ages
    """
    bsa = 0.024265 * (weight_kg ** 0.5378) * (height_cm ** 0.3964)
    return bsa



def calculate_bsa_boyd(weight_kg, height_cm):
    """
    BSA using Boyd formula (1935)
    
    Formula: BSA = 0.0003207 × H^0.3 × [1000×W]^(0.7285 - 0.0188×log10(1000×W))
    
    Takes body density into account, good for obesity/extreme weight
    """
    log_factor = math.log10(1000 * weight_kg)
    bsa = 0.0003207 * (height_cm ** 0.3) * ((1000 * weight_kg) ** (0.7285 - 0.0188 * log_factor))
    return bsa



def calculate_bsa_shuter_aslani(weight_kg, height_cm):
    """
    BSA using Shuter & Aslani formula (2000)
    
    Formula: BSA = 0.00949 × W^0.441 × H^0.655
    
    Modern dataset, high accuracy for obesity and tall stature
    """
    bsa = 0.00949 * (weight_kg ** 0.441) * (height_cm ** 0.655)
    return bsa



