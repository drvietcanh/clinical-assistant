"""
Universal Antibiotic Dosing Calculator
Tính liều kháng sinh tự động dựa trên eGFR/CrCl cho bất kỳ kháng sinh nào
Enhanced with: Special populations, detailed dosing, warnings, pediatric support
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE


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


def parse_dosage_text(dosage_text):
    """
    Parse dosage text to extract mg/kg, interval, etc.
    Returns dict with parsed components
    Enhanced parsing with more patterns
    """
    import re
    result = {
        'dose_per_kg': None,
        'total_dose': None,
        'dose_min': None,
        'dose_max': None,
        'interval_hours': None,
        'frequency': None,
        'route': None
    }
    
    # Look for mg/kg pattern (can be range: "15-20mg/kg")
    mg_kg_match = re.search(r'(\d+(?:\.\d+)?)(?:\s*-\s*(\d+(?:\.\d+)?))?\s*mg/kg', dosage_text, re.IGNORECASE)
    if mg_kg_match:
        result['dose_per_kg'] = float(mg_kg_match.group(1))
        if mg_kg_match.group(2):  # Has range
            result['dose_max'] = float(mg_kg_match.group(2))
    
    # Look for total dose (g or mg) - can be range
    # Pattern: "1-2g", "500mg-1g", "1g"
    total_range_match = re.search(r'(\d+(?:\.\d+)?)\s*(g|mg)\s*(?:-|đến|to)\s*(\d+(?:\.\d+)?)\s*(g|mg)', dosage_text, re.IGNORECASE)
    if total_range_match:
        val1 = float(total_range_match.group(1))
        unit1 = total_range_match.group(2).lower()
        val2 = float(total_range_match.group(3))
        unit2 = total_range_match.group(4).lower()
        
        val1_mg = val1 * 1000 if unit1 == 'g' else val1
        val2_mg = val2 * 1000 if unit2 == 'g' else val2
        
        result['dose_min'] = min(val1_mg, val2_mg)
        result['total_dose'] = max(val1_mg, val2_mg)
        result['dose_max'] = max(val1_mg, val2_mg)
    else:
        total_match = re.search(r'(\d+(?:\.\d+)?)\s*(g|mg)', dosage_text, re.IGNORECASE)
        if total_match:
            value = float(total_match.group(1))
            unit = total_match.group(2).lower()
            result['total_dose'] = value * 1000 if unit == 'g' else value
    
    # Look for interval (multiple patterns)
    # "mỗi 8 giờ", "mỗi 8h", "q8h", "mỗi 8-12 giờ"
    interval_match = re.search(r'(?:mỗi|q)\s*(\d+)(?:\s*-\s*(\d+))?\s*(?:giờ|h|hours)', dosage_text, re.IGNORECASE)
    if interval_match:
        interval = int(interval_match.group(1))
        if interval_match.group(2):  # Has range
            interval_max = int(interval_match.group(2))
            result['interval_hours'] = (interval + interval_max) / 2  # Average
        else:
            result['interval_hours'] = interval
    
    # Look for frequency
    # "2 lần/ngày", "x 2 lần/ngày", "bid", "tid", "qid"
    freq_match = re.search(r'(?:x\s*)?(\d+)\s*lần/ngày', dosage_text, re.IGNORECASE)
    if freq_match:
        result['frequency'] = int(freq_match.group(1))
        result['interval_hours'] = 24 / result['frequency']
    else:
        # Check for bid/tid/qid
        if re.search(r'\bbid\b', dosage_text, re.IGNORECASE):
            result['frequency'] = 2
            result['interval_hours'] = 12
        elif re.search(r'\btid\b', dosage_text, re.IGNORECASE):
            result['frequency'] = 3
            result['interval_hours'] = 8
        elif re.search(r'\bqid\b', dosage_text, re.IGNORECASE):
            result['frequency'] = 4
            result['interval_hours'] = 6
    
    # Detect route
    if re.search(r'\bIV\b', dosage_text, re.IGNORECASE):
        result['route'] = 'IV'
    elif re.search(r'\bIM\b', dosage_text, re.IGNORECASE):
        result['route'] = 'IM'
    elif re.search(r'\bPO\b', dosage_text, re.IGNORECASE):
        result['route'] = 'PO'
    
    return result


def calculate_infusion_details(calculated_dose_mg, antibiotic_name, route="IV"):
    """
    Calculate infusion time and concentration
    Returns: dict with infusion_time_minutes, volume_ml, concentration_mg_ml
    """
    # Default infusion parameters by antibiotic
    infusion_params = {
        "Vancomycin": {"time_min": 60, "max_conc_mg_ml": 5, "max_rate_mg_min": 10},
        "Gentamicin": {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 20},
        "Tobramycin": {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 20},
        "Amikacin": {"time_min": 30, "max_conc_mg_ml": 5, "max_rate_mg_min": 20},
        "Piperacillin-Tazobactam": {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 30},
        "Meropenem": {"time_min": 30, "max_conc_mg_ml": 20, "max_rate_mg_min": 50},
        "Imipenem-Cilastatin": {"time_min": 30, "max_conc_mg_ml": 5, "max_rate_mg_min": 25},
        "Ceftriaxone": {"time_min": 30, "max_conc_mg_ml": 40, "max_rate_mg_min": 50},
        "Cefepime": {"time_min": 30, "max_conc_mg_ml": 40, "max_rate_mg_min": 50},
    }
    
    # Get parameters for this antibiotic (or defaults)
    params = infusion_params.get(antibiotic_name, {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 20})
    
    # Calculate concentration (try to use reasonable volume)
    volume_ml = max(50, calculated_dose_mg / params["max_conc_mg_ml"] * 2)  # Use 2x max to be safe
    volume_ml = round(volume_ml / 50) * 50  # Round to nearest 50ml
    concentration_mg_ml = calculated_dose_mg / volume_ml
    
    # Ensure concentration doesn't exceed max
    if concentration_mg_ml > params["max_conc_mg_ml"]:
        volume_ml = round(calculated_dose_mg / params["max_conc_mg_ml"] / 10) * 10  # Round to nearest 10ml
        concentration_mg_ml = calculated_dose_mg / volume_ml
    
    # Calculate infusion time based on rate
    infusion_time_minutes = max(params["time_min"], (calculated_dose_mg / params["max_rate_mg_min"]))
    infusion_time_minutes = round(infusion_time_minutes / 5) * 5  # Round to nearest 5 minutes
    
    return {
        "infusion_time_minutes": infusion_time_minutes,
        "volume_ml": volume_ml,
        "concentration_mg_ml": concentration_mg_ml,
        "infusion_time_hours": infusion_time_minutes / 60
    }


def calculate_detailed_dose(antibiotic_name, weight_kg, ibw, abw, crcl, indication="standard", is_pediatric=False, height_cm=None):
    """
    Calculate detailed dose (mg, interval, infusion time, concentration)
    """
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        return None
    
    ab_data = ANTIBIOTICS_DATABASE[antibiotic_name]
    dosage = ab_data.get('dosage', {})
    
    # Select appropriate base dose
    if is_pediatric:
        if 'pediatric_iv' in dosage:
            base_text = dosage['pediatric_iv']
        elif 'pediatric_po' in dosage:
            base_text = dosage['pediatric_po']
        else:
            return None
    else:
        if indication == "severe" and 'adult_iv_severe' in dosage:
            base_text = dosage['adult_iv_severe']
        elif indication == "meningitis" and 'meningitis_iv' in dosage:
            base_text = dosage['meningitis_iv']
        elif 'adult_iv' in dosage:
            base_text = dosage['adult_iv']
        elif 'adult_standard' in dosage:
            base_text = dosage['adult_standard']
        else:
            return None
    
    parsed = parse_dosage_text(base_text)
    
    # Calculate actual dose
    # Need height for BMI calculation - using a default for now if not provided
    # In actual use, height should be passed as parameter
    try:
        # Try to calculate BMI if height available (would need to pass height parameter)
        # For now, use simplified logic
        is_obese_simple = weight_kg > ibw * 1.25
        dosing_weight = abw if is_obese_simple else weight_kg
    except:
        dosing_weight = weight_kg
    
    if parsed['dose_per_kg']:
        calculated_dose_mg = parsed['dose_per_kg'] * dosing_weight
        # If there's a max dose, use the average or max depending on indication
        if parsed.get('dose_max'):
            max_dose = parsed['dose_max'] * dosing_weight
            if indication == "severe" or indication == "meningitis":
                # Use higher dose for severe infections
                calculated_dose_mg = max_dose
            else:
                # Use average for standard
                calculated_dose_mg = (calculated_dose_mg + max_dose) / 2
    elif parsed['total_dose']:
        calculated_dose_mg = parsed['total_dose']
        # If there's a range, choose based on indication
        if parsed.get('dose_min'):
            if indication == "severe" or indication == "meningitis":
                calculated_dose_mg = parsed.get('dose_max', parsed['total_dose'])
            else:
                calculated_dose_mg = (parsed['dose_min'] + parsed['total_dose']) / 2
    else:
        calculated_dose_mg = None
    
    # Calculate infusion details if IV
    infusion_details = None
    if parsed.get('route') == 'IV' and calculated_dose_mg:
        infusion_details = calculate_infusion_details(calculated_dose_mg, antibiotic_name, route='IV')
    
    return {
        'calculated_dose_mg': calculated_dose_mg,
        'dosing_weight_kg': dosing_weight,
        'interval_hours': parsed['interval_hours'],
        'frequency': parsed['frequency'],
        'infusion_details': infusion_details,
        'parsed': parsed
    }


def check_warnings(antibiotic_name, crcl, age, is_pregnant=False, is_breastfeeding=False, other_drugs=None):
    """
    Check for warnings: accumulation, toxicity, contraindications
    Returns list of warnings
    """
    warnings = []
    
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        return warnings
    
    ab_data = ANTIBIOTICS_DATABASE[antibiotic_name]
    
    # Check renal accumulation
    renal_clearance = ab_data.get('renal_clearance_percent', 50)  # Default assume 50% renal clearance
    if crcl < 30 and renal_clearance > 50:
        warnings.append({
            'level': 'high',
            'message': f'⚠️ Nguy cơ tích lũy thuốc cao: CrCl < 30 mL/min và thuốc thải chủ yếu qua thận ({renal_clearance}%). Cần giảm liều và monitor.',
            'icon': '🚨'
        })
    
    # Check for nephrotoxic combinations
    if antibiotic_name == "Vancomycin" and other_drugs:
        nephrotoxic_drugs = ["Aminoglycoside", "Gentamicin", "Amikacin", "Tobramycin"]
        if any(drug in other_drugs for drug in nephrotoxic_drugs):
            warnings.append({
                'level': 'high',
                'message': '🚨 PHỐI HỢP ĐỘC THẬN: Vancomycin + Aminoglycoside → Tăng nguy cơ độc thận. Monitor creatinine thường xuyên.',
                'icon': '🚨'
            })
    
    # Enhanced pregnancy/breastfeeding checks with category display
    pregnancy_category = ab_data.get('pregnancy', '')
    pregnancy_info = {
        'A': {'level': 'low', 'message': 'An toàn cho thai kỳ'},
        'B': {'level': 'low', 'message': 'An toàn, dùng được trong thai kỳ'},
        'C': {'level': 'medium', 'message': 'Thận trọng: Cân nhắc lợi ích/nguy cơ'},
        'D': {'level': 'high', 'message': 'Có bằng chứng nguy cơ, chỉ dùng nếu lợi ích > nguy cơ'},
        'X': {'level': 'high', 'message': 'CHỐNG CHỈ ĐỊNH trong thai kỳ'}
    }
    
    if is_pregnant:
        if pregnancy_category in ['D', 'X']:
            warnings.append({
                'level': 'high',
                'message': f'🚨 KHÔNG AN TOÀN CHO THAI: Pregnancy category {pregnancy_category} - {pregnancy_info.get(pregnancy_category, {}).get("message", "")}. Tìm kháng sinh thay thế.',
                'icon': '🚨'
            })
        elif pregnancy_category == 'C':
            warnings.append({
                'level': 'medium',
                'message': f'⚠️ Thận trọng khi có thai: Pregnancy category C - {pregnancy_info.get("C", {}).get("message", "")}. Cân nhắc lợi ích/nguy cơ.',
                'icon': '⚠️'
            })
        elif pregnancy_category in ['A', 'B']:
            warnings.append({
                'level': 'low',
                'message': f'✅ Pregnancy category {pregnancy_category}: {pregnancy_info.get(pregnancy_category, {}).get("message", "")}',
                'icon': '✅'
            })
    
    # Breastfeeding check
    if is_breastfeeding:
        # Most antibiotics are compatible with breastfeeding, but some need caution
        if antibiotic_name in ["Tetracycline", "Doxycycline"]:
            warnings.append({
                'level': 'medium',
                'message': '⚠️ Doxycycline/Tetracycline: Có thể ảnh hưởng răng xương trẻ nhỏ. Thận trọng khi cho con bú.',
                'icon': '⚠️'
            })
        elif antibiotic_name in ["Chloramphenicol"]:
            warnings.append({
                'level': 'high',
                'message': '🚨 Chloramphenicol: Tránh dùng khi cho con bú (nguy cơ gray baby syndrome).',
                'icon': '🚨'
            })
        else:
            # Most antibiotics are safe
            warnings.append({
                'level': 'low',
                'message': '✅ Hầu hết kháng sinh an toàn khi cho con bú. Tra cứu thông tin cụ thể.',
                'icon': 'ℹ️'
            })
    
    # Enhanced age restrictions (pediatric with specific ages)
    if age < 18:
        if antibiotic_name == "Doxycycline" and age < 8:
            warnings.append({
                'level': 'high',
                'message': '🚨 CHỐNG CHỈ ĐỊNH: Doxycycline không dùng cho trẻ < 8 tuổi (ảnh hưởng răng và xương).',
                'icon': '🚨'
            })
        
        if antibiotic_name == "Tetracycline" and age < 8:
            warnings.append({
                'level': 'high',
                'message': '🚨 CHỐNG CHỈ ĐỊNH: Tetracycline không dùng cho trẻ < 8 tuổi.',
                'icon': '🚨'
            })
        
        if antibiotic_name == "Ciprofloxacin" and age < 18:
            warnings.append({
                'level': 'medium',
                'message': '⚠️ Ciprofloxacin: Tránh dùng cho trẻ < 18 tuổi (trừ trường hợp đặc biệt). Ảnh hưởng xương và sụn.',
                'icon': '⚠️'
            })
        
        if antibiotic_name == "Levofloxacin" and age < 18:
            warnings.append({
                'level': 'medium',
                'message': '⚠️ Levofloxacin: Tránh dùng cho trẻ < 18 tuổi (trừ trường hợp đặc biệt).',
                'icon': '⚠️'
            })
    
    # Check for ototoxicity in elderly
    if age >= 65 and antibiotic_name in ["Gentamicin", "Amikacin", "Tobramycin"]:
        warnings.append({
            'level': 'medium',
            'message': '⚠️ Thận trọng độc tai ở người già. Monitor thính lực.',
            'icon': '⚠️'
        })
    
    # Check for nephrotoxicity risk
    if age >= 65 and antibiotic_name in ["Vancomycin", "Colistin"]:
        warnings.append({
            'level': 'medium',
            'message': '⚠️ Thận trọng độc thận ở người già. Monitor creatinine thường xuyên.',
            'icon': '⚠️'
        })
    
    return warnings


def calculate_icu_adjustment(antibiotic_name, albumin_gdl=None, shock_type=None, is_icu=False, crcl=None):
    """
    Calculate ICU-specific dose adjustments based on:
    - Albumin level (protein binding)
    - Shock state (Vd changes, ARC)
    
    Args:
        antibiotic_name: Name of antibiotic
        albumin_gdl: Albumin level in g/dL (normal: 3.5-5.0)
        shock_type: Type of shock ("septic", "cardiogenic", "distributive", "hypovolemic", None)
        is_icu: Boolean if patient is in ICU
        crcl: Creatinine clearance (for ARC detection)
    
    Returns:
        dict with adjustment factors and recommendations
    """
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        return {'adjustment_factor': 1.0, 'recommendations': []}
    
    ab_data = ANTIBIOTICS_DATABASE[antibiotic_name]
    
    # Get protein binding info (default values based on antibiotic class)
    protein_binding_percent = ab_data.get('protein_binding_percent', 0)
    
    # Known protein binding values for common antibiotics
    protein_binding_db = {
        "Ceftriaxone": 90,  # 85-95 average
        "Cefazolin": 85,  # 80-90 average
        "Ertapenem": 95,
        "Teicoplanin": 90,
        "Piperacillin-Tazobactam": 30,
        "Meropenem": 2,
        "Imipenem-Cilastatin": 20,
        "Vancomycin": 40,  # 30-50 average
        "Gentamicin": 5,  # 0-10 average
        "Amikacin": 5,  # 0-10 average
        "Tobramycin": 5,
        "Ciprofloxacin": 30,  # 20-40 average
        "Levofloxacin": 31,  # 24-38 average
        "Linezolid": 31,
        "Daptomycin": 92,  # 90-93 average
        "Cefepime": 20,
        "Ceftazidime": 10,
        "Cefotaxime": 35,
        "Aztreonam": 56,
        "Colistin": 50,
    }
    
    if antibiotic_name in protein_binding_db:
        protein_binding_percent = protein_binding_db[antibiotic_name]
        if isinstance(protein_binding_percent, (list, tuple)):
            protein_binding_percent = sum(protein_binding_percent) / len(protein_binding_percent)
    
    adjustment_factor = 1.0
    recommendations = []
    
    # Albumin adjustment (hypoalbuminemia)
    if albumin_gdl is not None:
        if albumin_gdl < 3.0:
            # Significant hypoalbuminemia
            if protein_binding_percent > 80:
                # High protein binding - significant impact
                # Increase dose by 25-50% due to increased free fraction and Vd
                adjustment_factor *= 1.5
                recommendations.append(f"🚨 Albumin rất thấp ({albumin_gdl:.1f} g/dL) + liên kết protein cao ({protein_binding_percent}%) → Tăng liều 50%")
            elif protein_binding_percent > 50:
                # Moderate binding
                adjustment_factor *= 1.25
                recommendations.append(f"⚠️ Albumin thấp ({albumin_gdl:.1f} g/dL) + liên kết protein trung bình ({protein_binding_percent}%) → Tăng liều 25%")
            else:
                # Low binding - minimal impact
                recommendations.append(f"ℹ️ Albumin thấp nhưng liên kết protein thấp ({protein_binding_percent}%) → Ảnh hưởng tối thiểu")
        elif albumin_gdl < 3.5:
            # Mild hypoalbuminemia
            if protein_binding_percent > 80:
                adjustment_factor *= 1.25
                recommendations.append(f"⚠️ Albumin giảm nhẹ ({albumin_gdl:.1f} g/dL) + liên kết protein cao → Tăng liều 25%")
    
    # Shock adjustment
    if shock_type:
        if shock_type == "septic":
            # Septic shock: increased Vd, ARC, capillary leak
            adjustment_factor *= 1.5  # Increase dose by 50%
            recommendations.append("🚨 Sốc nhiễm khuẩn: Tăng Vd, ARC, rò rỉ mao mạch → Tăng liều 50%, cân nhắc loading dose")
        elif shock_type == "distributive":
            # Similar to septic
            adjustment_factor *= 1.5
            recommendations.append("🚨 Sốc phân bố: Tăng Vd → Tăng liều 50%")
        elif shock_type == "cardiogenic":
            # Cardiogenic shock: reduced perfusion but may still need higher dose
            adjustment_factor *= 1.25
            recommendations.append("⚠️ Sốc tim: Giảm tưới máu nhưng vẫn có thể cần tăng liều 25%")
        elif shock_type == "hypovolemic":
            # Hypovolemic: less dramatic Vd changes
            adjustment_factor *= 1.15
            recommendations.append("⚠️ Sốc giảm thể tích: Tăng liều nhẹ 15%")
    
    # ARC (Augmented Renal Clearance) - common in ICU
    if is_icu and crcl is not None:
        if crcl > 130:  # Very high CrCl suggests ARC
            adjustment_factor *= 1.25
            recommendations.append(f"⚠️ ARC (CrCl = {crcl:.0f} mL/min) → Tăng liều 25% hoặc rút ngắn interval")
    
    return {
        'adjustment_factor': adjustment_factor,
        'recommendations': recommendations,
        'protein_binding': protein_binding_percent,
        'albumin': albumin_gdl
    }


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


def calculate_adjusted_dose(antibiotic_name, crcl, egfr=None, base_dose=None, indication="standard",
                            albumin_gdl=None, shock_type=None, is_icu=False):
    """
    Calculate adjusted antibiotic dose based on renal function AND ICU factors
    
    Args:
        antibiotic_name: Name of antibiotic from database
        crcl: Creatinine clearance (mL/min)
        egfr: eGFR (optional, for reference)
        base_dose: Base dose if not in database (e.g., custom dosing)
        indication: Type of infection (standard, severe, meningitis, etc.)
        albumin_gdl: Albumin level in g/dL (for ICU adjustment)
        shock_type: Type of shock ("septic", "cardiogenic", "distributive", "hypovolemic", None)
        is_icu: Boolean if patient is in ICU
    
    Returns:
        dict with adjusted dose information
    """
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        return {
            "error": f"Kháng sinh '{antibiotic_name}' không có trong database",
            "recommendation": "Vui lòng tra cứu hướng dẫn riêng"
        }
    
    ab_data = ANTIBIOTICS_DATABASE[antibiotic_name]
    renal_category = get_renal_category(crcl, egfr)
    
    # Get base dosage information
    dosage = ab_data.get('dosage', {})
    renal_adj = ab_data.get('renal_adjustment', {})
    
    # Determine base dose based on indication
    if indication == "severe" and 'adult_iv_severe' in dosage:
        base_info = dosage['adult_iv_severe']
    elif indication == "meningitis" and 'meningitis_iv' in dosage:
        base_info = dosage['meningitis_iv']
    elif 'adult_iv' in dosage:
        base_info = dosage['adult_iv']
    elif 'adult_standard' in dosage:
        base_info = dosage['adult_standard']
    elif 'adult_im' in dosage:
        base_info = dosage['adult_im']
    else:
        base_info = "Liều chuẩn theo hướng dẫn"
    
    # Get renal adjustment recommendation
    if renal_category in renal_adj:
        adjustment_text = renal_adj[renal_category]
    elif renal_category == 'normal':
        adjustment_text = renal_adj.get('normal', 'Không đổi')
    else:
        adjustment_text = "Tham khảo hướng dẫn cụ thể"
    
    # ICU-specific adjustments
    icu_adjustment = calculate_icu_adjustment(antibiotic_name, albumin_gdl, shock_type, is_icu, crcl)
    icu_factor = icu_adjustment['adjustment_factor']
    icu_recommendations = icu_adjustment['recommendations']
    
    # Combine adjustments
    if icu_factor > 1.0:
        if "Tăng liều" in adjustment_text or "Giảm liều" in adjustment_text:
            # Modify existing adjustment
            adjustment_text = f"{adjustment_text} + Điều chỉnh ICU (x{icu_factor:.2f})"
        else:
            adjustment_text = f"{adjustment_text} + ICU: Tăng liều (x{icu_factor:.2f})"
    
    # Additional notes
    notes = dosage.get('notes', '')
    monitoring = ab_data.get('monitoring', '')
    
    # Add ICU-specific monitoring if applicable
    if is_icu:
        monitoring = f"{monitoring}\n📊 ICU: Monitor nồng độ thuốc, cân nhắc TDM" if monitoring else "📊 ICU: Monitor nồng độ thuốc, cân nhắc TDM"
    
    return {
        "antibiotic": antibiotic_name,
        "base_dose": base_info,
        "renal_category": renal_category,
        "crcl": crcl,
        "egfr": egfr,
        "adjustment": adjustment_text,
        "recommended_dose": adjustment_text,
        "icu_factor": icu_factor,
        "icu_recommendations": icu_recommendations,
        "protein_binding": icu_adjustment.get('protein_binding', 0),
        "notes": notes,
        "monitoring": monitoring,
        "full_renal_guide": renal_adj
    }


def render_dosing_calculator():
    """Universal antibiotic dosing calculator interface - REFACTORED to use UI components"""
    
    # Import UI components
    from .dosing_ui import (
        render_header,
        render_patient_inputs,
        render_weight_metrics,
        render_renal_metrics,
        render_antibiotic_selection,
        check_imported_values,
        render_dosage_results,
        render_warnings_section
    )
    
    # Render header
    render_header()
    
    # Check for imported values
    use_imported, imported_crcl, imported_egfr, imported_gfr_absolute = check_imported_values()
    
    # Get patient inputs
    patient_data = render_patient_inputs()
    
    st.markdown("---")
    
    # Calculate IBW, ABW, BMI
    ibw = patient_data['ibw']
    bmi = patient_data['bmi']
    is_obese = patient_data['is_obese']
    abw = patient_data['abw']
    weight = patient_data['weight']
    
    # Display weight metrics
    render_weight_metrics(weight, ibw, bmi, is_obese, abw)
    
    st.markdown("---")
    
    # Calculate CrCl (use imported if available)
    if use_imported and imported_crcl:
        crcl = imported_crcl
        st.info(f"📥 Sử dụng CrCl đã import: {crcl:.1f} mL/min")
    else:
        # Calculate with appropriate weight
        crcl = calculate_crcl(
            patient_data['age'],
            abw if is_obese else weight,
            patient_data['scr_mgdl'],
            patient_data['sex'],
            use_abw=is_obese,
            abw=abw
        )
    
    # Calculate eGFR (use imported if available)
    if use_imported and imported_egfr:
        egfr = imported_egfr
        st.info(f"📥 Sử dụng eGFR đã import: {egfr:.1f} mL/min/1.73m²")
    else:
        egfr = calculate_egfr_simplified(
            patient_data['age'],
            patient_data['scr_mgdl'],
            patient_data['sex']
        )
    
    # Get renal category
    renal_category = get_renal_category(
        crcl, egfr,
        patient_data['is_hemodialysis'],
        patient_data['is_continuous_hd'],
        patient_data['is_peritoneal_dialysis']
    )
    
    # Display renal metrics
    render_renal_metrics(crcl, egfr, renal_category)
    
    st.markdown("---")
    
    # Antibiotic selection
    selected_ab, indication_code, other_drugs = render_antibiotic_selection()
    
    st.markdown("---")
    
    # Calculate dose button
    if st.button("🧮 Tính Liều", type="primary", use_container_width=True):
        # Calculate adjusted dose
        result = calculate_adjusted_dose(
            selected_ab,
            crcl,
            egfr,
            indication=indication_code,
            albumin_gdl=patient_data['albumin_gdl'] if patient_data['is_icu'] else None,
            shock_type=patient_data['shock_type'] if patient_data['is_icu'] else None,
            is_icu=patient_data['is_icu']
        )
        
        if "error" in result:
            st.error(result["error"])
            st.info(result["recommendation"])
        else:
            ab_data = ANTIBIOTICS_DATABASE[selected_ab]
            
            # Render dosage results
            render_dosage_results(
                result,
                selected_ab,
                ab_data,
                crcl,
                renal_category,
                patient_data,
                indication_code
            )
            
            # Render warnings
            render_warnings_section(
                selected_ab,
                crcl,
                patient_data['age'],
                patient_data['is_pregnant'],
                patient_data['is_breastfeeding'],
                other_drugs
            )
    
    # Integration with eGFR calculator
    st.markdown("---")
    
    # Link to database view
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **🔗 Tích hợp với eGFR Calculator:**
        - Tính eGFR/GFR đầy đủ với nhiều công thức tại trang **Calculators** → **eGFR/GFR Calculator**
        - Tự động chuyển đổi giữa eGFR chuẩn hóa và GFR tuyệt đối
        - Hỗ trợ tính BSA và điều chỉnh cho bệnh nhân béo phì/gầy
        """)
    
    with col2:
        st.info("""
        **📖 Tra Cứu Kháng Sinh:**
        - Xem thông tin đầy đủ về kháng sinh đã chọn
        - Tính liều nhanh ngay trong trang tra cứu
        - Dùng **"🔍 Tra Cứu & Dữ Liệu Kháng Sinh"** ở menu
        """)
    st.markdown("---")
    
    # Link to database view
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **🔗 Tích hợp với eGFR Calculator:**
        - Tính eGFR/GFR đầy đủ với nhiều công thức tại trang **Calculators** → **eGFR/GFR Calculator**
        - Tự động chuyển đổi giữa eGFR chuẩn hóa và GFR tuyệt đối
        - Hỗ trợ tính BSA và điều chỉnh cho bệnh nhân béo phì/gầy
        """)
    
    with col2:
        st.info("""
        **📖 Tra Cứu Kháng Sinh:**
        - Xem thông tin đầy đủ về kháng sinh đã chọn
        - Tính liều nhanh ngay trong trang tra cứu
        - Dùng **"🔍 Tra Cứu & Dữ Liệu Kháng Sinh"** ở menu
        """)

