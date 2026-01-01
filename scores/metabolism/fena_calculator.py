"""
FENa Calculator - Calculation Functions
Handles FENa calculation and interpretation logic
"""

from config.theme import COLORS


def calculate_fena(u_na, p_na, u_cr_mgdl, p_cr_mgdl):
    """
    Calculate FENa (Fractional Excretion of Sodium)
    
    Formula: FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100
    
    Args:
        u_na: Urine Sodium (mEq/L)
        p_na: Plasma Sodium (mEq/L)
        u_cr_mgdl: Urine Creatinine (mg/dL)
        p_cr_mgdl: Plasma Creatinine (mg/dL)
    
    Returns:
        float: FENa percentage
    """
    if p_na == 0 or u_cr_mgdl == 0:
        return 0.0
    
    fena = ((u_na * p_cr_mgdl) / (p_na * u_cr_mgdl)) * 100
    return fena


def interpret_fena(fena):
    """
    Interpret FENa result
    
    Args:
        fena: FENa percentage
    
    Returns:
        dict: Interpretation with keys: interpretation, color, cause
    """
    if fena < 1.0:
        return {
            "interpretation": "PRERENAL AKI",
            "color": COLORS["info"],
            "cause": "Thiếu tưới máu thận"
        }
    elif fena <= 2.0:
        return {
            "interpretation": "KHÔNG RÕ RÀNG",
            "color": COLORS["warning"],
            "cause": "Cần thêm thông tin lâm sàng"
        }
    else:
        return {
            "interpretation": "INTRINSIC RENAL AKI",
            "color": COLORS["error"],
            "cause": "Tổn thương nhu mô thận"
        }

