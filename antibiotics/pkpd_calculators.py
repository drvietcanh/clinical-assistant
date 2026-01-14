"""
PK/PD Calculators
Pharmacokinetic/Pharmacodynamic calculations for antibiotics
AUC/MIC, Time above MIC, Cmax/MIC ratios
"""

import streamlit as st
import math
from typing import Dict, Optional, Tuple

# PK parameters for common antibiotics
PK_PARAMETERS = {
    "Vancomycin": {
        "vd": 0.7,  # L/kg
        "clearance": 0.05,  # L/kg/h
        "half_life": 6,  # hours
        "protein_binding": 0.4,
        "notes": "VD và clearance thay đổi theo bệnh nhân"
    },
    "Gentamicin": {
        "vd": 0.25,  # L/kg
        "clearance": 0.08,  # L/kg/h
        "half_life": 2,  # hours
        "protein_binding": 0.05,
        "notes": "Time-dependent killing, peak/MIC important"
    },
    "Amikacin": {
        "vd": 0.25,  # L/kg
        "clearance": 0.06,  # L/kg/h
        "half_life": 2.5,  # hours
        "protein_binding": 0.05,
        "notes": "Time-dependent killing"
    },
    "Ceftriaxone": {
        "vd": 0.15,  # L/kg
        "clearance": 0.02,  # L/kg/h
        "half_life": 8,  # hours
        "protein_binding": 0.9,
        "notes": "Time above MIC important"
    },
    "Piperacillin-Tazobactam": {
        "vd": 0.2,  # L/kg
        "clearance": 0.15,  # L/kg/h
        "half_life": 1,  # hours
        "protein_binding": 0.3,
        "notes": "Time above MIC critical (40-50% of dosing interval)"
    },
    "Meropenem": {
        "vd": 0.25,  # L/kg
        "clearance": 0.2,  # L/kg/h
        "half_life": 1,  # hours
        "protein_binding": 0.02,
        "notes": "Time above MIC critical (40% of dosing interval)"
    },
    "Levofloxacin": {
        "vd": 1.1,  # L/kg
        "clearance": 0.12,  # L/kg/h
        "half_life": 7,  # hours
        "protein_binding": 0.31,
        "notes": "AUC/MIC ratio important (target >100 for Gram-negative)"
    },
    "Ciprofloxacin": {
        "vd": 2.0,  # L/kg
        "clearance": 0.35,  # L/kg/h
        "half_life": 4,  # hours
        "protein_binding": 0.3,
        "notes": "AUC/MIC ratio important"
    },
}

# PK/PD targets
PKPD_TARGETS = {
    "Vancomycin": {
        "auc_mic": {"target": 400, "notes": "AUC24/MIC target for MRSA"},
        "trough": {"target": 15, "notes": "Trough target 15-20 mg/L"},
    },
    "Gentamicin": {
        "peak_mic": {"target": 8, "notes": "Peak/MIC ratio target"},
        "cmax_mic": {"target": 8, "notes": "Cmax/MIC target"},
    },
    "Amikacin": {
        "peak_mic": {"target": 8, "notes": "Peak/MIC ratio target"},
        "cmax_mic": {"target": 8, "notes": "Cmax/MIC target"},
    },
    "Ceftriaxone": {
        "time_above_mic": {"target": 0.5, "notes": "Time above MIC > 50% of dosing interval"},
    },
    "Piperacillin-Tazobactam": {
        "time_above_mic": {"target": 0.5, "notes": "Time above MIC > 50% of dosing interval"},
    },
    "Meropenem": {
        "time_above_mic": {"target": 0.4, "notes": "Time above MIC > 40% of dosing interval"},
    },
    "Levofloxacin": {
        "auc_mic": {"target": 100, "notes": "AUC24/MIC target for Gram-negative"},
    },
    "Ciprofloxacin": {
        "auc_mic": {"target": 125, "notes": "AUC24/MIC target"},
    },
}


def calculate_auc_mic(dose_mg, weight_kg, mic_mg_l, antibiotic_name: str, interval_hours: int = 24) -> Dict:
    """
    Calculate AUC/MIC ratio
    
    Args:
        dose_mg: Dose in mg
        weight_kg: Weight in kg
        mic_mg_l: MIC in mg/L
        antibiotic_name: Name of antibiotic
        interval_hours: Dosing interval in hours
    
    Returns:
        dict with AUC/MIC calculation results
    """
    if antibiotic_name not in PK_PARAMETERS:
        return {"error": "Không có dữ liệu PK cho kháng sinh này"}
    
    pk = PK_PARAMETERS[antibiotic_name]
    
    # Calculate AUC
    # AUC = Dose / Clearance
    clearance_l_h = pk["clearance"] * weight_kg  # L/h
    auc_mg_h_l = dose_mg / clearance_l_h  # mg·h/L
    
    # AUC24 = AUC per dose * (24 / interval)
    auc24_mg_h_l = auc_mg_h_l * (24 / interval_hours)
    
    # AUC/MIC ratio
    if mic_mg_l > 0:
        auc_mic_ratio = auc24_mg_h_l / mic_mg_l
    else:
        auc_mic_ratio = None
    
    # Get target
    target_info = PKPD_TARGETS.get(antibiotic_name, {}).get("auc_mic", {})
    target = target_info.get("target", None)
    
    # Assessment
    if auc_mic_ratio and target:
        if auc_mic_ratio >= target:
            assessment = "✅ Đạt mục tiêu"
            color = "#4caf50"
        elif auc_mic_ratio >= target * 0.8:
            assessment = "⚠️ Gần đạt mục tiêu"
            color = "#ffc107"
        else:
            assessment = "❌ Chưa đạt mục tiêu"
            color = "#f44336"
    else:
        assessment = "ℹ️ Không có mục tiêu cụ thể"
        color = "#757575"
    
    return {
        "auc24_mg_h_l": auc24_mg_h_l,
        "mic_mg_l": mic_mg_l,
        "auc_mic_ratio": auc_mic_ratio,
        "target": target,
        "assessment": assessment,
        "color": color,
        "notes": target_info.get("notes", "")
    }


def calculate_time_above_mic(dose_mg, weight_kg, mic_mg_l, antibiotic_name: str, 
                             interval_hours: int, infusion_time_hours: float = 0.5) -> Dict:
    """
    Calculate Time above MIC
    
    Args:
        dose_mg: Dose in mg
        weight_kg: Weight in kg
        mic_mg_l: MIC in mg/L
        antibiotic_name: Name of antibiotic
        interval_hours: Dosing interval in hours
        infusion_time_hours: Infusion time in hours
    
    Returns:
        dict with Time above MIC calculation results
    """
    if antibiotic_name not in PK_PARAMETERS:
        return {"error": "Không có dữ liệu PK cho kháng sinh này"}
    
    pk = PK_PARAMETERS[antibiotic_name]
    
    # Calculate Cmax (peak concentration)
    vd_l = pk["vd"] * weight_kg  # L
    cmax_mg_l = dose_mg / vd_l  # mg/L
    
    # Calculate elimination rate constant
    half_life_h = pk["half_life"]
    kel_h = math.log(2) / half_life_h  # 1/h
    
    # Time above MIC
    # C(t) = Cmax * e^(-kel * t) > MIC
    # Solve for t: t = (1/kel) * ln(Cmax/MIC)
    if mic_mg_l > 0 and cmax_mg_l > mic_mg_l:
        time_above_mic_h = (1 / kel_h) * math.log(cmax_mg_l / mic_mg_l)
        time_above_mic_h += infusion_time_hours  # Add infusion time
    else:
        time_above_mic_h = 0
    
    # Percentage of dosing interval
    percent_interval = (time_above_mic_h / interval_hours) * 100 if interval_hours > 0 else 0
    
    # Get target
    target_info = PKPD_TARGETS.get(antibiotic_name, {}).get("time_above_mic", {})
    target_percent = target_info.get("target", 0.5) * 100  # Convert to percentage
    
    # Assessment
    if percent_interval >= target_percent:
        assessment = "✅ Đạt mục tiêu"
        color = "#4caf50"
    elif percent_interval >= target_percent * 0.8:
        assessment = "⚠️ Gần đạt mục tiêu"
        color = "#ffc107"
    else:
        assessment = "❌ Chưa đạt mục tiêu"
        color = "#f44336"
    
    return {
        "cmax_mg_l": cmax_mg_l,
        "mic_mg_l": mic_mg_l,
        "time_above_mic_h": time_above_mic_h,
        "percent_interval": percent_interval,
        "target_percent": target_percent,
        "assessment": assessment,
        "color": color,
        "notes": target_info.get("notes", "")
    }


def calculate_cmax_mic(dose_mg, weight_kg, mic_mg_l, antibiotic_name: str) -> Dict:
    """
    Calculate Cmax/MIC ratio
    
    Args:
        dose_mg: Dose in mg
        weight_kg: Weight in kg
        mic_mg_l: MIC in mg/L
        antibiotic_name: Name of antibiotic
    
    Returns:
        dict with Cmax/MIC calculation results
    """
    if antibiotic_name not in PK_PARAMETERS:
        return {"error": "Không có dữ liệu PK cho kháng sinh này"}
    
    pk = PK_PARAMETERS[antibiotic_name]
    
    # Calculate Cmax
    vd_l = pk["vd"] * weight_kg  # L
    cmax_mg_l = dose_mg / vd_l  # mg/L
    
    # Cmax/MIC ratio
    if mic_mg_l > 0:
        cmax_mic_ratio = cmax_mg_l / mic_mg_l
    else:
        cmax_mic_ratio = None
    
    # Get target
    target_info = PKPD_TARGETS.get(antibiotic_name, {}).get("cmax_mic", {})
    target = target_info.get("target", None)
    
    # Assessment
    if cmax_mic_ratio and target:
        if cmax_mic_ratio >= target:
            assessment = "✅ Đạt mục tiêu"
            color = "#4caf50"
        elif cmax_mic_ratio >= target * 0.8:
            assessment = "⚠️ Gần đạt mục tiêu"
            color = "#ffc107"
        else:
            assessment = "❌ Chưa đạt mục tiêu"
            color = "#f44336"
    else:
        assessment = "ℹ️ Không có mục tiêu cụ thể"
        color = "#757575"
    
    return {
        "cmax_mg_l": cmax_mg_l,
        "mic_mg_l": mic_mg_l,
        "cmax_mic_ratio": cmax_mic_ratio,
        "target": target,
        "assessment": assessment,
        "color": color,
        "notes": target_info.get("notes", "")
    }


def render_pkpd_calculator():
    """Render PK/PD Calculator UI"""
    
    st.markdown("### 🧮 PK/PD Calculator")
    st.caption("Tính toán các chỉ số PK/PD: AUC/MIC, Time above MIC, Cmax/MIC")
    
    st.info("""
    **💡 Lưu ý:**
    - Các tính toán này dựa trên mô hình PK đơn giản
    - Kết quả chỉ mang tính tham khảo
    - Để tính chính xác, cần TDM và mô hình PK/PD phức tạp hơn
    """)
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        antibiotic_name = st.selectbox(
            "Chọn kháng sinh:",
            options=sorted(list(PK_PARAMETERS.keys())),
            key="pkpd_ab_select"
        )
        
        dose_mg = st.number_input(
            "Liều dùng (mg):",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            key="pkpd_dose"
        )
        
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=0.0,
            value=70.0,
            step=1.0,
            key="pkpd_weight"
        )
    
    with col2:
        mic_mg_l = st.number_input(
            "MIC (mg/L):",
            min_value=0.0,
            value=1.0,
            step=0.1,
            format="%.2f",
            key="pkpd_mic"
        )
        
        interval_hours = st.number_input(
            "Khoảng cách liều (giờ):",
            min_value=0.0,
            value=24.0,
            step=1.0,
            key="pkpd_interval"
        )
        
        infusion_time_hours = st.number_input(
            "Thời gian truyền (giờ):",
            min_value=0.0,
            value=0.5,
            step=0.1,
            format="%.1f",
            key="pkpd_infusion"
        )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính PK/PD", type="primary", use_container_width=True):
        if not antibiotic_name or dose_mg <= 0 or weight_kg <= 0 or mic_mg_l <= 0:
            st.warning("⚠️ Vui lòng nhập đầy đủ thông tin hợp lệ")
            return
        
        # Display PK parameters
        pk = PK_PARAMETERS[antibiotic_name]
        st.markdown("#### 📊 Thông Số PK")
        col_pk1, col_pk2, col_pk3, col_pk4 = st.columns(4)
        with col_pk1:
            st.metric("Vd", f"{pk['vd']} L/kg")
        with col_pk2:
            st.metric("Clearance", f"{pk['clearance']} L/kg/h")
        with col_pk3:
            st.metric("Half-life", f"{pk['half_life']} giờ")
        with col_pk4:
            st.metric("Protein binding", f"{pk['protein_binding']*100:.0f}%")
        
        if pk.get("notes"):
            st.caption(f"💡 {pk['notes']}")
        
        st.markdown("---")
        
        # Calculate different PK/PD indices based on antibiotic type
        pkpd_targets = PKPD_TARGETS.get(antibiotic_name, {})
        
        # AUC/MIC for time-dependent antibiotics
        if "auc_mic" in pkpd_targets:
            st.markdown("#### 📈 AUC/MIC Ratio")
            result = calculate_auc_mic(dose_mg, weight_kg, mic_mg_l, antibiotic_name, interval_hours)
            
            if "error" not in result:
                st.markdown(f"""
                <div style='
                    background: {result["color"]};
                    color: white;
                    padding: 20px;
                    border-radius: 12px;
                    margin-bottom: 10px;
                '>
                    <h3 style='margin: 0 0 10px 0; color: white;'>{result["assessment"]}</h3>
                    <p style='margin: 5px 0;'><strong>AUC24/MIC:</strong> {result["auc_mic_ratio"]:.1f}</p>
                    <p style='margin: 5px 0;'><strong>Mục tiêu:</strong> ≥ {result["target"]}</p>
                    {f'<p style="margin: 5px 0;"><strong>Ghi chú:</strong> {result["notes"]}</p>' if result.get("notes") else ""}
                </div>
                """, unsafe_allow_html=True)
                
                st.metric("AUC24", f"{result['auc24_mg_h_l']:.1f} mg·h/L")
        
        # Time above MIC for beta-lactams
        if "time_above_mic" in pkpd_targets:
            st.markdown("#### ⏱️ Time above MIC")
            result = calculate_time_above_mic(dose_mg, weight_kg, mic_mg_l, antibiotic_name, 
                                             interval_hours, infusion_time_hours)
            
            if "error" not in result:
                st.markdown(f"""
                <div style='
                    background: {result["color"]};
                    color: white;
                    padding: 20px;
                    border-radius: 12px;
                    margin-bottom: 10px;
                '>
                    <h3 style='margin: 0 0 10px 0; color: white;'>{result["assessment"]}</h3>
                    <p style='margin: 5px 0;'><strong>Thời gian trên MIC:</strong> {result["time_above_mic_h"]:.2f} giờ</p>
                    <p style='margin: 5px 0;'><strong>% khoảng cách liều:</strong> {result["percent_interval"]:.1f}%</p>
                    <p style='margin: 5px 0;'><strong>Mục tiêu:</strong> ≥ {result["target_percent"]:.0f}%</p>
                    {f'<p style="margin: 5px 0;"><strong>Ghi chú:</strong> {result["notes"]}</p>' if result.get("notes") else ""}
                </div>
                """, unsafe_allow_html=True)
                
                col_t1, col_t2 = st.columns(2)
                with col_t1:
                    st.metric("Cmax", f"{result['cmax_mg_l']:.2f} mg/L")
                with col_t2:
                    st.metric("MIC", f"{result['mic_mg_l']:.2f} mg/L")
        
        # Cmax/MIC for concentration-dependent antibiotics
        if "cmax_mic" in pkpd_targets or "peak_mic" in pkpd_targets:
            st.markdown("#### 📊 Cmax/MIC Ratio")
            result = calculate_cmax_mic(dose_mg, weight_kg, mic_mg_l, antibiotic_name)
            
            if "error" not in result:
                st.markdown(f"""
                <div style='
                    background: {result["color"]};
                    color: white;
                    padding: 20px;
                    border-radius: 12px;
                    margin-bottom: 10px;
                '>
                    <h3 style='margin: 0 0 10px 0; color: white;'>{result["assessment"]}</h3>
                    <p style='margin: 5px 0;'><strong>Cmax/MIC:</strong> {result["cmax_mic_ratio"]:.1f}</p>
                    {f'<p style="margin: 5px 0;"><strong>Mục tiêu:</strong> ≥ {result["target"]}</p>' if result.get("target") else ""}
                    {f'<p style="margin: 5px 0;"><strong>Ghi chú:</strong> {result["notes"]}</p>' if result.get("notes") else ""}
                </div>
                """, unsafe_allow_html=True)
                
                col_c1, col_c2 = st.columns(2)
                with col_c1:
                    st.metric("Cmax", f"{result['cmax_mg_l']:.2f} mg/L")
                with col_c2:
                    st.metric("MIC", f"{result['mic_mg_l']:.2f} mg/L")
    
    # Information section
    with st.expander("📚 Thông tin về PK/PD", expanded=False):
        st.markdown("""
        **Các chỉ số PK/PD quan trọng:**
        
        **1. AUC/MIC (Area Under Curve / Minimum Inhibitory Concentration)**
        - Quan trọng cho: Fluoroquinolones, Vancomycin
        - Mục tiêu: AUC24/MIC ≥ 100-400 (tùy thuốc và vi khuẩn)
        
        **2. Time above MIC**
        - Quan trọng cho: Beta-lactams (Penicillin, Cephalosporin, Carbapenem)
        - Mục tiêu: Thời gian trên MIC > 40-50% khoảng cách liều
        
        **3. Cmax/MIC (Peak Concentration / MIC)**
        - Quan trọng cho: Aminoglycosides
        - Mục tiêu: Cmax/MIC ≥ 8-10
        
        **Lưu ý:**
        - Các tính toán này dựa trên mô hình PK đơn giản
        - Để chính xác hơn, cần TDM và mô hình PK/PD phức tạp
        - Kết quả chỉ mang tính tham khảo
        """)
