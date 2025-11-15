"""
Shock Management
Shock classification, fluid responsiveness assessment, vasopressor selection
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def classify_shock_type(sbp: float, map_value: float, hr: float, lactate: float = None, 
                       cvp: float = None, scvo2: float = None, cardiac_output: float = None) -> dict:
    """
    Classify shock type based on hemodynamic parameters
    
    Args:
        sbp: Systolic blood pressure (mmHg)
        map_value: Mean arterial pressure (mmHg)
        hr: Heart rate (bpm)
        lactate: Lactate level (mmol/L, optional)
        cvp: Central venous pressure (mmHg, optional)
        scvo2: Central venous oxygen saturation (%, optional)
        cardiac_output: Cardiac output (L/min, optional)
    
    Returns:
        Dictionary with shock classification
    """
    # Basic classification
    if map_value < 65:
        if hr > 100:
            if cvp and cvp < 5:
                shock_type = "Hypovolemic Shock"
                color = "error"
                icon = "💧"
            elif cvp and cvp > 12:
                shock_type = "Cardiogenic Shock"
                color = "error"
                icon = "❤️"
            else:
                shock_type = "Distributive Shock (Sepsis/Anaphylaxis)"
                color = "error"
                icon = "🦠"
        else:
            shock_type = "Neurogenic Shock"
            color = "error"
            icon = "🧠"
    else:
        shock_type = "No Shock"
        color = "success"
        icon = "✅"
    
    # Refine with additional parameters
    if lactate and lactate > 2:
        if shock_type == "Distributive Shock (Sepsis/Anaphylaxis)":
            shock_type = "Septic Shock"
    
    if cardiac_output and cardiac_output < 4:
        if shock_type == "Cardiogenic Shock":
            shock_type = "Cardiogenic Shock (Low CO)"
    
    return {
        "shock_type": shock_type,
        "color": color,
        "icon": icon,
        "sbp": sbp,
        "map": map_value,
        "hr": hr,
        "lactate": lactate
    }


def assess_fluid_responsiveness(cvp: float = None, pulse_pressure_variation: float = None,
                                stroke_volume_variation: float = None, passive_leg_raise: bool = None) -> dict:
    """
    Assess fluid responsiveness
    
    Args:
        cvp: Central venous pressure (mmHg)
        pulse_pressure_variation: PPV (%) - requires mechanical ventilation
        stroke_volume_variation: SVV (%) - requires mechanical ventilation
        passive_leg_raise: Response to PLR (True/False/None)
    
    Returns:
        Dictionary with fluid responsiveness assessment
    """
    responsive = False
    evidence = []
    
    # CVP (low specificity)
    if cvp is not None:
        if cvp < 5:
            evidence.append("CVP <5 mmHg (có thể đáp ứng dịch)")
        elif cvp > 12:
            evidence.append("CVP >12 mmHg (không đáp ứng dịch)")
        else:
            evidence.append("CVP 5-12 mmHg (không rõ)")
    
    # PPV/SVV (high specificity if on mechanical ventilation)
    if pulse_pressure_variation is not None:
        if pulse_pressure_variation > 13:
            responsive = True
            evidence.append(f"PPV >13% (đáp ứng dịch)")
        else:
            evidence.append(f"PPV ≤13% (không đáp ứng dịch)")
    
    if stroke_volume_variation is not None:
        if stroke_volume_variation > 12:
            responsive = True
            evidence.append(f"SVV >12% (đáp ứng dịch)")
        else:
            evidence.append(f"SVV ≤12% (không đáp ứng dịch)")
    
    # Passive leg raise (best test)
    if passive_leg_raise is not None:
        if passive_leg_raise:
            responsive = True
            evidence.append("PLR dương tính (đáp ứng dịch)")
        else:
            evidence.append("PLR âm tính (không đáp ứng dịch)")
    
    if responsive:
        interpretation = "Đáp ứng dịch"
        color = "success"
    elif len(evidence) == 0:
        interpretation = "Chưa đánh giá"
        color = "info"
    else:
        interpretation = "Không đáp ứng dịch"
        color = "warning"
    
    return {
        "responsive": responsive,
        "interpretation": interpretation,
        "color": color,
        "evidence": evidence
    }


def render_shock_classification():
    """Render shock classification calculator"""
    st.subheader("🔍 Shock Classification")
    st.caption("Phân loại sốc dựa trên huyết động")
    
    st.markdown("""
    **Các loại sốc:**
    - **Hypovolemic:** Giảm thể tích tuần hoàn
    - **Cardiogenic:** Suy tim
    - **Distributive:** Giãn mạch (sepsis, anaphylaxis, neurogenic)
    - **Obstructive:** Tắc nghẽn (PE, tamponade, tension pneumothorax)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sbp = st.number_input(
            "Systolic BP (mmHg):",
            min_value=50,
            max_value=200,
            value=90,
            step=1,
            format="%d",
            key="shock_sbp"
        )
        
        map_value = st.number_input(
            "Mean Arterial Pressure (mmHg):",
            min_value=40,
            max_value=150,
            value=60,
            step=1,
            format="%d",
            key="shock_map"
        )
        
        hr = st.number_input(
            "Heart Rate (bpm):",
            min_value=40,
            max_value=200,
            value=120,
            step=1,
            format="%d",
            key="shock_hr"
        )
    
    with col2:
        lactate = st.number_input(
            "Lactate (mmol/L):",
            min_value=0.5,
            max_value=20.0,
            value=None,
            step=0.1,
            format="%.1f",
            key="shock_lactate",
            help="Optional"
        )
        
        cvp = st.number_input(
            "CVP (mmHg):",
            min_value=0.0,
            max_value=30.0,
            value=None,
            step=0.5,
            format="%.1f",
            key="shock_cvp",
            help="Optional"
        )
        
        scvo2 = st.number_input(
            "ScvO2 (%):",
            min_value=30,
            max_value=100,
            value=None,
            step=1,
            format="%d",
            key="shock_scvo2",
            help="Optional"
        )
    
    if st.button("Phân loại", type="primary", key="classify_shock"):
        result = classify_shock_type(sbp, map_value, hr, lactate, cvp, scvo2)
        
        st.markdown("### 📊 Kết Quả")
        
        render_result_box(
            "Loại Sốc",
            result["shock_type"],
            subtitle=f"MAP: {map_value:.0f} mmHg, HR: {hr:.0f} bpm",
            color=result["color"],
            icon=result["icon"]
        )
        
        st.markdown("---")
        
        # Management recommendations
        st.markdown("### 💡 Khuyến Nghị Xử Trí")
        
        if "Hypovolemic" in result["shock_type"]:
            st.error("""
            **💧 Hypovolemic Shock:**
            1. Truyền dịch nhanh (crystalloid hoặc colloid)
            2. Tìm nguyên nhân mất máu/dịch
            3. Xử trí nguyên nhân (cầm máu, bù dịch)
            4. Theo dõi đáp ứng
            """)
        elif "Cardiogenic" in result["shock_type"]:
            st.error("""
            **❤️ Cardiogenic Shock:**
            1. Đánh giá chức năng tim (echo, ECG)
            2. Điều trị nguyên nhân (ACS, arrhythmia, etc.)
            3. Inotrope (dobutamine, milrinone)
            4. Vasopressor nếu cần (norepinephrine)
            5. Cân nhắc IABP, ECMO nếu nặng
            """)
        elif "Septic" in result["shock_type"]:
            st.error("""
            **🦠 Septic Shock:**
            1. Sepsis bundle (kháng sinh, dịch, vasopressor)
            2. Truyền dịch 30 mL/kg
            3. Norepinephrine (1st line)
            4. Tìm và điều trị ổ nhiễm trùng
            5. Theo dõi lactate
            """)
        elif "Distributive" in result["shock_type"]:
            st.error("""
            **🦠 Distributive Shock:**
            1. Truyền dịch
            2. Vasopressor (norepinephrine)
            3. Tìm nguyên nhân (sepsis, anaphylaxis, neurogenic)
            4. Điều trị nguyên nhân
            """)
        elif "Neurogenic" in result["shock_type"]:
            st.error("""
            **🧠 Neurogenic Shock:**
            1. Vasopressor (norepinephrine hoặc phenylephrine)
            2. Điều trị nguyên nhân (chấn thương cột sống)
            3. Thận trọng với truyền dịch (có thể gây phù phổi)
            """)
        else:
            st.success("""
            **✅ Không có sốc:**
            - MAP ≥65 mmHg
            - Theo dõi tiếp
            """)


def render_fluid_responsiveness():
    """Render fluid responsiveness assessment"""
    st.subheader("💧 Fluid Responsiveness Assessment")
    st.caption("Đánh giá đáp ứng dịch")
    
    st.markdown("""
    **Đánh giá đáp ứng dịch:**
    - **PLR (Passive Leg Raise):** Test tốt nhất, không cần máy thở
    - **PPV/SVV:** Chỉ dùng khi thở máy, không có rối loạn nhịp
    - **CVP:** Độ nhạy thấp, không đáng tin cậy
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        cvp = st.number_input(
            "CVP (mmHg):",
            min_value=0.0,
            max_value=30.0,
            value=None,
            step=0.5,
            format="%.1f",
            key="fr_cvp",
            help="Optional"
        )
        
        ppv = st.number_input(
            "Pulse Pressure Variation (%):",
            min_value=0.0,
            max_value=50.0,
            value=None,
            step=0.5,
            format="%.1f",
            key="fr_ppv",
            help="Chỉ dùng khi thở máy, không có rối loạn nhịp"
        )
    
    with col2:
        svv = st.number_input(
            "Stroke Volume Variation (%):",
            min_value=0.0,
            max_value=50.0,
            value=None,
            step=0.5,
            format="%.1f",
            key="fr_svv",
            help="Chỉ dùng khi thở máy"
        )
        
        plr_response = st.selectbox(
            "Passive Leg Raise (PLR):",
            ["Chưa test", "Đáp ứng (CO tăng ≥10%)", "Không đáp ứng"],
            key="fr_plr"
        )
    
    plr_bool = None
    if plr_response == "Đáp ứng (CO tăng ≥10%)":
        plr_bool = True
    elif plr_response == "Không đáp ứng":
        plr_bool = False
    
    if st.button("Đánh giá", type="primary", key="assess_fr"):
        result = assess_fluid_responsiveness(cvp, ppv, svv, plr_bool)
        
        st.markdown("### 📊 Kết Quả")
        
        render_result_box(
            "Đáp Ứng Dịch",
            result["interpretation"],
            color=result["color"],
            icon="💧"
        )
        
        st.markdown("---")
        
        if result["evidence"]:
            st.markdown("### 📋 Bằng Chứng")
            for evidence in result["evidence"]:
                st.markdown(f"- {evidence}")
        
        st.markdown("---")
        
        # Recommendations
        if result["responsive"]:
            st.success("""
            **✅ Đáp ứng dịch:**
            - Có thể truyền dịch
            - Theo dõi đáp ứng sau mỗi bolus
            - Mục tiêu: MAP ≥65 mmHg, giảm lactate
            """)
        else:
            st.warning("""
            **⚠️ Không đáp ứng dịch:**
            - Tránh truyền dịch quá mức (nguy cơ quá tải)
            - Ưu tiên vasopressor
            - Xem xét inotrope nếu cần
            - Tìm nguyên nhân khác
            """)


def render_vasopressor_selection():
    """Render vasopressor selection guide"""
    st.subheader("💉 Vasopressor Selection Guide")
    st.caption("Hướng dẫn chọn vasopressor cho sốc")
    
    st.markdown("""
    **Nguyên tắc:**
    - **1st line:** Norepinephrine (hầu hết các loại sốc)
    - **2nd line:** Vasopressin (thêm vào norepinephrine)
    - **3rd line:** Epinephrine (nếu cần thêm)
    - **Inotrope:** Dobutamine (nếu cardiac output thấp)
    """)
    
    st.markdown("---")
    
    shock_type = st.selectbox(
        "Loại sốc:",
        [
            "Septic Shock",
            "Cardiogenic Shock",
            "Hypovolemic Shock",
            "Distributive Shock",
            "Neurogenic Shock",
            "Obstructive Shock"
        ],
        key="vasopressor_shock_type"
    )
    
    if st.button("Khuyến nghị", type="primary", key="recommend_vasopressor"):
        st.markdown("### 💡 Khuyến Nghị")
        
        if shock_type == "Septic Shock":
            st.error("""
            **🦠 Septic Shock:**
            
            **1st line: Norepinephrine**
            - Liều: 0.05-2 mcg/kg/min
            - Mục tiêu: MAP ≥65 mmHg
            - Titrate mỗi 5-10 phút
            
            **2nd line: Vasopressin**
            - Liều: 0.03-0.04 units/min (không titrate)
            - Thêm vào nếu norepinephrine không đủ
            - Giảm liều norepinephrine khi thêm vasopressin
            
            **3rd line: Epinephrine**
            - Liều: 0.05-2 mcg/kg/min
            - Nếu cần thêm vasopressor
            """)
        elif shock_type == "Cardiogenic Shock":
            st.error("""
            **❤️ Cardiogenic Shock:**
            
            **1st line: Norepinephrine**
            - Liều: 0.05-2 mcg/kg/min
            - Mục tiêu: MAP ≥65 mmHg
            
            **Inotrope: Dobutamine**
            - Liều: 2.5-20 mcg/kg/min
            - Nếu cardiac output thấp
            - Có thể kết hợp với norepinephrine
            
            **Alternative: Milrinone**
            - Liều: 0.25-0.75 mcg/kg/min
            - Nếu suy tim nặng
            """)
        elif shock_type == "Hypovolemic Shock":
            st.error("""
            **💧 Hypovolemic Shock:**
            
            **Ưu tiên: Truyền dịch**
            - Crystalloid hoặc colloid
            - Tìm nguyên nhân mất máu/dịch
            
            **Vasopressor (nếu cần):**
            - Norepinephrine: 0.05-2 mcg/kg/min
            - Chỉ dùng khi đã bù dịch đầy đủ
            """)
        elif shock_type == "Neurogenic Shock":
            st.error("""
            **🧠 Neurogenic Shock:**
            
            **1st line: Norepinephrine**
            - Liều: 0.05-2 mcg/kg/min
            - Mục tiêu: MAP ≥65 mmHg
            
            **Alternative: Phenylephrine**
            - Liều: 0.5-5 mcg/kg/min
            - Nếu cần vasopressor thuần túy (không tăng CO)
            """)
        else:
            st.error("""
            **💉 Vasopressor Selection:**
            
            **1st line: Norepinephrine**
            - Liều: 0.05-2 mcg/kg/min
            - Mục tiêu: MAP ≥65 mmHg
            
            **2nd line: Vasopressin**
            - Liều: 0.03-0.04 units/min
            - Thêm vào nếu cần
            
            **3rd line: Epinephrine**
            - Liều: 0.05-2 mcg/kg/min
            - Nếu cần thêm vasopressor
            """)


def render_shock_management():
    """Main function to render shock management tools"""
    
    st.markdown("## 💉 Shock Management")
    st.markdown("""
    Hướng dẫn quản lý sốc:
    - Phân loại sốc
    - Đánh giá đáp ứng dịch
    - Hướng dẫn chọn vasopressor
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs([
        "🔍 Classification",
        "💧 Fluid Responsiveness",
        "💉 Vasopressor Selection"
    ])
    
    with tab1:
        render_shock_classification()
    
    with tab2:
        render_fluid_responsiveness()
    
    with tab3:
        render_vasopressor_selection()
    
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các tính toán này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Tuân thủ hướng dẫn địa phương và quy định bệnh viện
    """)

