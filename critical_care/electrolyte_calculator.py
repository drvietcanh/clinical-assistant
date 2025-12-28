"""
Electrolyte Concentration Calculator
Calculate and adjust electrolyte concentrations in IV fluids
"""

from typing import Dict, Optional


def calculate_electrolyte_addition(
    current_volume_ml: float,
    current_na_mmol_l: float,
    target_na_mmol_l: float
) -> Dict:
    """
    Calculate Na+ addition needed to reach target concentration.
    
    Args:
        current_volume_ml: Current volume of fluid in ml
        current_na_mmol_l: Current Na+ concentration in mmol/L
        target_na_mmol_l: Target Na+ concentration in mmol/L
    
    Returns:
        Dictionary with calculation results:
        {
            "current_na_mmol": float,
            "target_na_mmol": float,
            "na_deficit_mmol": float,
            "nacl_3_percent_ml": float,  # 3% NaCl (513 mmol/L)
            "nacl_0_9_percent_ml": float,  # 0.9% NaCl (154 mmol/L)
            "nacl_10_percent_ml": float,  # 10% NaCl (1713 mmol/L)
            "recommendations": List[str]
        }
    """
    if current_volume_ml <= 0:
        raise ValueError("Volume must be > 0")
    if current_na_mmol_l < 0 or target_na_mmol_l < 0:
        raise ValueError("Na+ concentration must be >= 0")
    
    # Convert volume to liters
    current_volume_l = current_volume_ml / 1000
    
    # Calculate current and target Na+ in mmol
    current_na_mmol = current_volume_l * current_na_mmol_l
    target_na_mmol = current_volume_l * target_na_mmol_l
    
    # Calculate deficit
    na_deficit_mmol = target_na_mmol - current_na_mmol
    
    # If no deficit, return early
    if na_deficit_mmol <= 0:
        return {
            "current_na_mmol": round(current_na_mmol, 2),
            "target_na_mmol": round(target_na_mmol, 2),
            "na_deficit_mmol": 0,
            "nacl_3_percent_ml": 0,
            "nacl_0_9_percent_ml": 0,
            "nacl_10_percent_ml": 0,
            "recommendations": ["Không cần thêm Na+"]
        }
    
    # Calculate volume of different NaCl solutions needed
    # 3% NaCl = 513 mmol/L
    nacl_3_percent_ml = (na_deficit_mmol / 513) * 1000
    
    # 0.9% NaCl = 154 mmol/L
    nacl_0_9_percent_ml = (na_deficit_mmol / 154) * 1000
    
    # 10% NaCl = 1713 mmol/L (hypertonic)
    nacl_10_percent_ml = (na_deficit_mmol / 1713) * 1000
    
    # Generate recommendations
    recommendations = []
    if na_deficit_mmol < 10:
        recommendations.append("Thiếu Na+ nhỏ, có thể dùng 0.9% NaCl")
    elif na_deficit_mmol < 50:
        recommendations.append("Thiếu Na+ trung bình, cân nhắc 3% NaCl")
    else:
        recommendations.append("Thiếu Na+ lớn, cần 3% hoặc 10% NaCl")
        recommendations.append("⚠️ Cần theo dõi sát Na+ máu")
    
    recommendations.append("Kiểm tra Na+ máu sau khi điều chỉnh")
    
    return {
        "current_na_mmol": round(current_na_mmol, 2),
        "target_na_mmol": round(target_na_mmol, 2),
        "na_deficit_mmol": round(na_deficit_mmol, 2),
        "nacl_3_percent_ml": round(nacl_3_percent_ml, 1),
        "nacl_0_9_percent_ml": round(nacl_0_9_percent_ml, 1),
        "nacl_10_percent_ml": round(nacl_10_percent_ml, 1),
        "recommendations": recommendations
    }


def calculate_potassium_addition(
    current_volume_ml: float,
    current_k_mmol_l: float,
    target_k_mmol_l: float
) -> Dict:
    """
    Calculate K+ addition needed to reach target concentration.
    
    Args:
        current_volume_ml: Current volume of fluid in ml
        current_k_mmol_l: Current K+ concentration in mmol/L
        target_k_mmol_l: Target K+ concentration in mmol/L
    
    Returns:
        Dictionary with calculation results:
        {
            "current_k_mmol": float,
            "target_k_mmol": float,
            "k_deficit_mmol": float,
            "kcl_10_percent_ml": float,  # 10% KCl (1342 mmol/L)
            "kcl_15_percent_ml": float,  # 15% KCl (2013 mmol/L)
            "recommendations": List[str]
        }
    """
    if current_volume_ml <= 0:
        raise ValueError("Volume must be > 0")
    if current_k_mmol_l < 0 or target_k_mmol_l < 0:
        raise ValueError("K+ concentration must be >= 0")
    
    # Convert volume to liters
    current_volume_l = current_volume_ml / 1000
    
    # Calculate current and target K+ in mmol
    current_k_mmol = current_volume_l * current_k_mmol_l
    target_k_mmol = current_volume_l * target_k_mmol_l
    
    # Calculate deficit
    k_deficit_mmol = target_k_mmol - current_k_mmol
    
    # If no deficit, return early
    if k_deficit_mmol <= 0:
        return {
            "current_k_mmol": round(current_k_mmol, 2),
            "target_k_mmol": round(target_k_mmol, 2),
            "k_deficit_mmol": 0,
            "kcl_10_percent_ml": 0,
            "kcl_15_percent_ml": 0,
            "recommendations": ["Không cần thêm K+"]
        }
    
    # Calculate volume of KCl solutions needed
    # 10% KCl = 1342 mmol/L
    kcl_10_percent_ml = (k_deficit_mmol / 1342) * 1000
    
    # 15% KCl = 2013 mmol/L
    kcl_15_percent_ml = (k_deficit_mmol / 2013) * 1000
    
    # Generate recommendations
    recommendations = []
    if k_deficit_mmol < 10:
        recommendations.append("Thiếu K+ nhỏ, có thể dùng 10% KCl")
    elif k_deficit_mmol < 40:
        recommendations.append("Thiếu K+ trung bình, cân nhắc 10% hoặc 15% KCl")
    else:
        recommendations.append("Thiếu K+ lớn, cần 15% KCl")
        recommendations.append("⚠️ Cần theo dõi sát K+ máu")
        recommendations.append("⚠️ Không truyền quá 20 mEq/h (trừ trường hợp đặc biệt)")
    
    recommendations.append("Kiểm tra K+ máu sau khi điều chỉnh")
    
    return {
        "current_k_mmol": round(current_k_mmol, 2),
        "target_k_mmol": round(target_k_mmol, 2),
        "k_deficit_mmol": round(k_deficit_mmol, 2),
        "kcl_10_percent_ml": round(kcl_10_percent_ml, 1),
        "kcl_15_percent_ml": round(kcl_15_percent_ml, 1),
        "recommendations": recommendations
    }


def calculate_calcium_addition(
    current_volume_ml: float,
    current_ca_mmol_l: float,
    target_ca_mmol_l: float
) -> Dict:
    """
    Calculate Ca++ addition needed to reach target concentration.
    
    Args:
        current_volume_ml: Current volume of fluid in ml
        current_ca_mmol_l: Current Ca++ concentration in mmol/L
        target_ca_mmol_l: Target Ca++ concentration in mmol/L
    
    Returns:
        Dictionary with calculation results:
        {
            "current_ca_mmol": float,
            "target_ca_mmol": float,
            "ca_deficit_mmol": float,
            "cacl2_10_percent_ml": float,  # 10% CaCl2 (680 mmol/L)
            "cagluconate_10_percent_ml": float,  # 10% Ca gluconate (225 mmol/L)
            "recommendations": List[str]
        }
    """
    if current_volume_ml <= 0:
        raise ValueError("Volume must be > 0")
    if current_ca_mmol_l < 0 or target_ca_mmol_l < 0:
        raise ValueError("Ca++ concentration must be >= 0")
    
    # Convert volume to liters
    current_volume_l = current_volume_ml / 1000
    
    # Calculate current and target Ca++ in mmol
    current_ca_mmol = current_volume_l * current_ca_mmol_l
    target_ca_mmol = current_volume_l * target_ca_mmol_l
    
    # Calculate deficit
    ca_deficit_mmol = target_ca_mmol - current_ca_mmol
    
    # If no deficit, return early
    if ca_deficit_mmol <= 0:
        return {
            "current_ca_mmol": round(current_ca_mmol, 2),
            "target_ca_mmol": round(target_ca_mmol, 2),
            "ca_deficit_mmol": 0,
            "cacl2_10_percent_ml": 0,
            "cagluconate_10_percent_ml": 0,
            "recommendations": ["Không cần thêm Ca++"]
        }
    
    # Calculate volume of Ca++ solutions needed
    # 10% CaCl2 = 680 mmol/L
    cacl2_10_percent_ml = (ca_deficit_mmol / 680) * 1000
    
    # 10% Ca gluconate = 225 mmol/L
    cagluconate_10_percent_ml = (ca_deficit_mmol / 225) * 1000
    
    # Generate recommendations
    recommendations = []
    if ca_deficit_mmol < 5:
        recommendations.append("Thiếu Ca++ nhỏ, có thể dùng Ca gluconate")
    elif ca_deficit_mmol < 20:
        recommendations.append("Thiếu Ca++ trung bình, cân nhắc CaCl2 hoặc Ca gluconate")
    else:
        recommendations.append("Thiếu Ca++ lớn, cần CaCl2")
        recommendations.append("⚠️ Cần theo dõi sát Ca++ máu")
    
    recommendations.append("⚠️ Không trộn với sodium bicarbonate")
    recommendations.append("Kiểm tra Ca++ máu sau khi điều chỉnh")
    
    return {
        "current_ca_mmol": round(current_ca_mmol, 2),
        "target_ca_mmol": round(target_ca_mmol, 2),
        "ca_deficit_mmol": round(ca_deficit_mmol, 2),
        "cacl2_10_percent_ml": round(cacl2_10_percent_ml, 1),
        "cagluconate_10_percent_ml": round(cagluconate_10_percent_ml, 1),
        "recommendations": recommendations
    }


def calculate_osmolarity(
    na_mmol_l: float,
    glucose_mmol_l: float = 0,
    bun_mmol_l: float = 0,
    k_mmol_l: float = 0,
    ca_mmol_l: float = 0
) -> Dict:
    """
    Calculate osmolarity of a solution.
    
    Formula: Osmolarity = 2×Na + Glucose + BUN + 2×K + 3×Ca (mOsm/L)
    
    Args:
        na_mmol_l: Na+ concentration in mmol/L
        glucose_mmol_l: Glucose concentration in mmol/L
        bun_mmol_l: BUN concentration in mmol/L
        k_mmol_l: K+ concentration in mmol/L
        ca_mmol_l: Ca++ concentration in mmol/L
    
    Returns:
        Dictionary with osmolarity:
        {
            "osmolarity_mosm_l": float,
            "is_isotonic": bool,
            "classification": str,
            "notes": str
        }
    """
    # Calculate osmolarity
    osmolarity = (2 * na_mmol_l) + glucose_mmol_l + bun_mmol_l + (2 * k_mmol_l) + (3 * ca_mmol_l)
    
    # Classify
    is_isotonic = 280 <= osmolarity <= 310
    if osmolarity < 280:
        classification = "Hypotonic"
        notes = "Dung dịch nhược trương. Cẩn thận khi truyền."
    elif osmolarity <= 310:
        classification = "Isotonic"
        notes = "Dung dịch đẳng trương. An toàn để truyền."
    else:
        classification = "Hypertonic"
        notes = "Dung dịch ưu trương. Cần theo dõi sát."
    
    return {
        "osmolarity_mosm_l": round(osmolarity, 1),
        "is_isotonic": is_isotonic,
        "classification": classification,
        "notes": notes
    }


def calculate_final_concentration(
    volume1_ml: float,
    concentration1_mmol_l: float,
    volume2_ml: float,
    concentration2_mmol_l: float
) -> float:
    """
    Calculate final concentration when mixing two solutions.
    
    Args:
        volume1_ml: Volume of first solution in ml
        concentration1_mmol_l: Concentration of first solution in mmol/L
        volume2_ml: Volume of second solution in ml
        concentration2_mmol_l: Concentration of second solution in mmol/L
    
    Returns:
        Final concentration in mmol/L
    """
    if volume1_ml <= 0 or volume2_ml <= 0:
        raise ValueError("Volumes must be > 0")
    
    total_volume_l = (volume1_ml + volume2_ml) / 1000
    total_mmol = (volume1_ml / 1000 * concentration1_mmol_l) + (volume2_ml / 1000 * concentration2_mmol_l)
    
    if total_volume_l == 0:
        return 0
    
    final_concentration = total_mmol / total_volume_l
    return round(final_concentration, 2)

