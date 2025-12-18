"""
Antibiotic Dosing Calculator - Main Calculation Functions
Dose calculations, ICU adjustments, warnings
"""

import streamlit as st
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .dosing_helpers import (
    get_renal_category,
    calculate_ibw,
    calculate_abw
)
from .dosing_processing import parse_dosage_text, calculate_infusion_details

# Import eGFR dosing lookup module
try:
    from .egfr_dosing_lookup import (
        lookup_egfr_dosing,
        get_drug_warning,
        get_drug_note,
        is_drug_in_egfr_database
    )
    EGFR_LOOKUP_AVAILABLE = True
except ImportError:
    EGFR_LOOKUP_AVAILABLE = False
    lookup_egfr_dosing = None
    get_drug_warning = None
    get_drug_note = None
    is_drug_in_egfr_database = None

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
    # Ưu tiên sử dụng eGFR-based lookup nếu có
    egfr_dosing_text = None
    if EGFR_LOOKUP_AVAILABLE and egfr is not None:
        is_dialysis = (renal_category in ['hemodialysis', 'continuous_hd', 'peritoneal_dialysis'])
        egfr_dosing_text = lookup_egfr_dosing(antibiotic_name, egfr, is_dialysis)
    
    if egfr_dosing_text:
        # Sử dụng dữ liệu từ eGFR lookup (chi tiết hơn)
        adjustment_text = egfr_dosing_text
        # Thêm ghi chú nếu có
        drug_note = get_drug_note(antibiotic_name) if EGFR_LOOKUP_AVAILABLE else None
        if drug_note:
            adjustment_text = f"{adjustment_text}\n📝 Lưu ý: {drug_note}"
    elif renal_category in renal_adj:
        # Fallback về logic cũ
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
    
    # Thêm cảnh báo từ eGFR database nếu có
    if EGFR_LOOKUP_AVAILABLE:
        drug_warning = get_drug_warning(antibiotic_name)
        if drug_warning:
            if drug_warning.get('critical', False):
                notes = f"🚨 {drug_warning.get('message', '')}\n{notes}" if notes else f"🚨 {drug_warning.get('message', '')}"
            else:
                notes = f"{drug_warning.get('message', '')}\n{notes}" if notes else drug_warning.get('message', '')
            
            warning_monitoring = drug_warning.get('monitoring', '')
            if warning_monitoring:
                monitoring = f"{monitoring}\n{warning_monitoring}" if monitoring else warning_monitoring
    
    # Add ICU-specific monitoring if applicable
    if is_icu:
        monitoring = f"{monitoring}\n📊 ICU: Monitor nồng độ thuốc, cân nhắc TDM" if monitoring else "📊 ICU: Monitor nồng độ thuốc, cân nhắc TDM"
    
    # Thêm thông tin về nguồn dữ liệu
    data_source = "eGFR database" if egfr_dosing_text else "standard database"
    
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
        "full_renal_guide": renal_adj,
        "data_source": data_source,
        "egfr_based": egfr_dosing_text is not None
    }



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



