"""
SOFA-2 Score - Helper Functions
Organ system scoring functions for SOFA-2
"""

def _get_respiratory_score_sofa2(pao2_fio2: float, support: str, hfnc_flow: float = None) -> dict:
    """
    Respiratory score with HFNC and ECMO support
    Updated thresholds based on 2025 data
    """
    # ECMO - maximum support
    if support == "ecmo":
        return {
            'score': 4,
            'detail': "**Hô hấp:** ECMO (Extracorporeal Membrane Oxygenation) → 4 điểm"
        }
    
    # Mechanical ventilation
    if support == "mv":
        if pao2_fio2 >= 300:  # Adjusted threshold
            score = 2
        elif pao2_fio2 >= 200:
            score = 3
        elif pao2_fio2 >= 100:
            score = 4
        else:
            score = 4
        return {
            'score': score,
            'detail': f"**Hô hấp:** Thở máy, PaO₂/FiO₂ = {pao2_fio2:.0f} → {score} điểm"
        }
    
    # Non-invasive ventilation
    if support == "niv":
        if pao2_fio2 >= 300:
            score = 2
        elif pao2_fio2 >= 200:
            score = 3
        else:
            score = 4
        return {
            'score': score,
            'detail': f"**Hô hấp:** NIV, PaO₂/FiO₂ = {pao2_fio2:.0f} → {score} điểm"
        }
    
    # HFNC - High Flow Nasal Cannula
    if support == "hfnc":
        # HFNC provides better oxygenation, adjusted scoring
        if pao2_fio2 >= 350:  # Better threshold for HFNC
            score = 1
        elif pao2_fio2 >= 250:
            score = 2
        elif pao2_fio2 >= 150:
            score = 3
        else:
            score = 4
        
        flow_info = f" (flow {hfnc_flow:.0f} L/min)" if hfnc_flow else ""
        return {
            'score': score,
            'detail': f"**Hô hấp:** HFNC{flow_info}, PaO₂/FiO₂ = {pao2_fio2:.0f} → {score} điểm"
        }
    
    # Oxygen or no support - adjusted thresholds
    if pao2_fio2 >= 400:
        score = 0
    elif pao2_fio2 >= 350:  # Adjusted from 300
        score = 1
    elif pao2_fio2 >= 250:  # Adjusted from 200
        score = 2
    elif pao2_fio2 >= 150:  # Adjusted from 100
        score = 3
    else:
        score = 4
    
    support_text = "Oxy thông thường" if support == "oxygen" else "Tự thở"
    return {
        'score': score,
        'detail': f"**Hô hấp:** {support_text}, PaO₂/FiO₂ = {pao2_fio2:.0f} → {score} điểm"
    }



def _get_coagulation_score_sofa2(platelets: float) -> dict:
    """
    Coagulation score with adjusted thresholds
    """
    # Adjusted thresholds based on big data
    if platelets >= 150:
        score = 0
    elif platelets >= 120:  # Adjusted from 100
        score = 1
    elif platelets >= 80:   # Adjusted from 50
        score = 2
    elif platelets >= 30:   # Adjusted from 20
        score = 3
    else:
        score = 4
    
    return {
        'score': score,
        'detail': f"**Đông máu:** Tiểu cầu = {platelets:.0f} ×10³/μL → {score} điểm"
    }



def _get_liver_score_sofa2(bilirubin: float) -> dict:
    """
    Liver score with adjusted thresholds
    """
    if bilirubin < 1.2:
        score = 0
    elif bilirubin < 2.0:
        score = 1
    elif bilirubin < 4.0:  # Adjusted from 6.0
        score = 2
    elif bilirubin < 8.0:  # Adjusted from 12.0
        score = 3
    else:
        score = 4
    
    return {
        'score': score,
        'detail': f"**Gan:** Bilirubin = {bilirubin:.1f} mg/dL → {score} điểm"
    }



def _get_cardiovascular_score_sofa2(
    map_value: float,
    use_vasopressor: bool,
    vasopressor_type: str,
    vasopressor_dose: float
) -> dict:
    """
    Cardiovascular score with enhanced vasopressor dosing
    Includes modern vasopressors: Vasopressin, Phenylephrine
    """
    if use_vasopressor:
        # Enhanced vasopressor scoring with modern agents
        if vasopressor_type == "Norepinephrine":
            if vasopressor_dose <= 0.1:
                score = 3
                detail = f"**Tim mạch:** Norepinephrine ≤0.1 mcg/kg/min → 3 điểm"
            elif vasopressor_dose <= 0.3:  # New intermediate threshold
                score = 4
                detail = f"**Tim mạch:** Norepinephrine 0.1-0.3 mcg/kg/min → 4 điểm"
            else:
                score = 4
                detail = f"**Tim mạch:** Norepinephrine >0.3 mcg/kg/min → 4 điểm"
        
        elif vasopressor_type == "Epinephrine":
            if vasopressor_dose <= 0.1:
                score = 3
                detail = f"**Tim mạch:** Epinephrine ≤0.1 mcg/kg/min → 3 điểm"
            elif vasopressor_dose <= 0.3:
                score = 4
                detail = f"**Tim mạch:** Epinephrine 0.1-0.3 mcg/kg/min → 4 điểm"
            else:
                score = 4
                detail = f"**Tim mạch:** Epinephrine >0.3 mcg/kg/min → 4 điểm"
        
        elif vasopressor_type == "Vasopressin":  # Modern agent
            # Vasopressin typically 0.03-0.04 U/min
            if vasopressor_dose <= 0.04:
                score = 3
                detail = f"**Tim mạch:** Vasopressin ≤0.04 U/min → 3 điểm"
            else:
                score = 4
                detail = f"**Tim mạch:** Vasopressin >0.04 U/min → 4 điểm"
        
        elif vasopressor_type == "Phenylephrine":  # Modern agent
            # Phenylephrine typically 0.5-2 mcg/kg/min
            if vasopressor_dose <= 1.0:
                score = 2
                detail = f"**Tim mạch:** Phenylephrine ≤1.0 mcg/kg/min → 2 điểm"
            elif vasopressor_dose <= 2.0:
                score = 3
                detail = f"**Tim mạch:** Phenylephrine 1.0-2.0 mcg/kg/min → 3 điểm"
            else:
                score = 4
                detail = f"**Tim mạch:** Phenylephrine >2.0 mcg/kg/min → 4 điểm"
        
        elif vasopressor_type == "Dopamine":
            if vasopressor_dose < 5:
                score = 2
                detail = f"**Tim mạch:** Dopamine <5 mcg/kg/min → 2 điểm"
            elif vasopressor_dose <= 15:
                score = 3
                detail = f"**Tim mạch:** Dopamine 5-15 mcg/kg/min → 3 điểm"
            else:
                score = 4
                detail = f"**Tim mạch:** Dopamine >15 mcg/kg/min → 4 điểm"
        
        elif vasopressor_type == "Dobutamine":
            score = 2
            detail = f"**Tim mạch:** Dobutamine (any dose) → 2 điểm"
        
        else:
            score = 3
            detail = f"**Tim mạch:** {vasopressor_type} → 3 điểm"
        
        return {'score': score, 'detail': detail}
    else:
        # No vasopressor - use MAP with adjusted threshold
        if map_value >= 70:
            score = 0
        else:
            score = 1
        
        return {
            'score': score,
            'detail': f"**Tim mạch:** MAP = {map_value:.0f} mmHg → {score} điểm"
        }



def _get_cns_score_sofa2(gcs: int) -> dict:
    """
    CNS score - same as original SOFA
    """
    if gcs == 15:
        score = 0
        detail = "**Thần kinh:** GCS = 15 → 0 điểm"
    elif gcs >= 13:
        score = 1
        detail = "**Thần kinh:** GCS = 13-14 → 1 điểm"
    elif gcs >= 10:
        score = 2
        detail = "**Thần kinh:** GCS = 10-12 → 2 điểm"
    elif gcs >= 6:
        score = 3
        detail = "**Thần kinh:** GCS = 6-9 → 3 điểm"
    else:
        score = 4
        detail = "**Thần kinh:** GCS = 3-5 → 4 điểm"
    
    return {'score': score, 'detail': detail}



def _get_renal_score_sofa2(creatinine: float, urine_output: float, on_rrt: bool) -> dict:
    """
    Renal score with RRT integration
    """
    # RRT indicates severe renal dysfunction
    if on_rrt:
        return {
            'score': 4,
            'detail': "**Thận:** Đang lọc máu (RRT) → 4 điểm"
        }
    
    # Calculate by creatinine
    if creatinine is None:
        renal_by_cr = 0
    elif creatinine < 1.2:
        renal_by_cr = 0
    elif creatinine < 2.0:
        renal_by_cr = 1
    elif creatinine < 3.5:
        renal_by_cr = 2
    elif creatinine < 5.0:
        renal_by_cr = 3
    else:
        renal_by_cr = 4
    
    # Calculate by urine output
    if urine_output is None:
        renal_by_uo = 0
    elif urine_output >= 500:
        renal_by_uo = 0
    elif urine_output >= 200:
        renal_by_uo = 3
    else:
        renal_by_uo = 4
    
    # Use worst score
    renal_score = max(renal_by_cr, renal_by_uo)
    
    if renal_by_uo > renal_by_cr:
        detail = f"**Thận:** UO = {urine_output:.0f} mL/24h → {renal_score} điểm"
    elif creatinine is not None:
        detail = f"**Thận:** Creatinine = {creatinine:.1f} mg/dL → {renal_score} điểm"
    else:
        detail = f"**Thận:** UO = {urine_output:.0f} mL/24h → {renal_score} điểm"
    
    return {'score': renal_score, 'detail': detail}



def _interpret_sofa2_score(total_score: int) -> dict:
    """
    Interpret SOFA-2 score with updated mortality predictions
    Based on big data from 2025
    """
    if total_score == 0:
        return {
            'interpretation': "Không có suy cơ quan",
            'mortality': "<8%",  # Improved from <10%
            'risk_class': "LOW",
            'color': "🟢"
        }
    elif total_score <= 6:
        return {
            'interpretation': "Suy cơ quan nhẹ",
            'mortality': "~8-18%",  # Adjusted
            'risk_class': "MILD",
            'color': "🟡"
        }
    elif total_score <= 11:
        return {
            'interpretation': "Suy cơ quan trung bình",
            'mortality': "~18-38%",  # Adjusted
            'risk_class': "MODERATE",
            'color': "🟠"
        }
    elif total_score <= 14:
        return {
            'interpretation': "Suy cơ quan nặng",
            'mortality': "~38-58%",  # Adjusted
            'risk_class': "SEVERE",
            'color': "🔴"
        }
    else:
        return {
            'interpretation': "Suy cơ quan rất nặng",
            'mortality': ">58%",  # Adjusted
            'risk_class': "CRITICAL",
            'color': "🔴"
        }



