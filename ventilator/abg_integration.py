"""
ABG Integration for Ventilator Module
Tích hợp ABG vào ventilator calculator
"""

import streamlit as st


def render_abg_panel(key_prefix="vent_abg"):
    """Panel nhập ABG trong ventilator page"""
    st.markdown("### 💨 Thông Số Khí Máu (ABG)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ph = st.number_input(
            "pH", 
            6.8, 7.8, 7.40, 0.01,
            format="%.2f",
            key=f"{key_prefix}_ph",
            help="pH động mạch (bình thường: 7.35-7.45)"
        )
        pco2 = st.number_input(
            "PaCO₂ (mmHg)", 
            10.0, 100.0, 40.0, 0.1, 
            format="%.1f", 
            key=f"{key_prefix}_pco2",
            help="Áp lực riêng phần CO₂ (bình thường: 35-45 mmHg)"
        )
        po2 = st.number_input(
            "PaO₂ (mmHg)", 
            30.0, 600.0, 95.0, 1.0,
            format="%.0f",
            key=f"{key_prefix}_po2",
            help="Áp lực riêng phần O₂ (bình thường: 80-100 mmHg)"
        )
    
    with col2:
        hco3 = st.number_input(
            "HCO₃ (mEq/L)", 
            5.0, 50.0, 24.0, 0.1, 
            format="%.1f", 
            key=f"{key_prefix}_hco3",
            help="Bicarbonate (bình thường: 22-26 mEq/L)"
        )
        fio2 = st.number_input(
            "FiO₂ (%)", 
            21.0, 100.0, 21.0, 1.0,
            format="%.0f",
            key=f"{key_prefix}_fio2",
            help="Nồng độ O₂ trong khí thở vào (21-100%)"
        )
        sao2 = st.number_input(
            "SaO₂ (%)", 
            70.0, 100.0, 98.0, 0.1, 
            format="%.1f", 
            key=f"{key_prefix}_sao2",
            help="Độ bão hòa O₂ động mạch (bình thường: >95%)"
        )
    
    return {
        "ph": ph,
        "pco2": pco2,
        "po2": po2,
        "hco3": hco3,
        "fio2": fio2,
        "sao2": sao2
    }


def calculate_pf_ratio(po2, fio2):
    """Tính P/F ratio (PaO₂/FiO₂)"""
    if fio2 == 0:
        return None
    return po2 / (fio2 / 100)


def classify_ards(pf_ratio):
    """Phân loại ARDS dựa trên P/F ratio"""
    if pf_ratio is None:
        return None, None, None
    
    if pf_ratio >= 400:
        return "Bình thường", "success", "Oxy hóa bình thường"
    elif pf_ratio >= 300:
        return "Thiếu oxy nhẹ", "info", "P/F 300-400"
    elif pf_ratio >= 200:
        return "ARDS nhẹ", "warning", "P/F 200-300"
    elif pf_ratio >= 100:
        return "ARDS trung bình", "error", "P/F 100-200"
    else:
        return "ARDS nặng", "error", "P/F <100"


def analyze_acid_base(ph, pco2, hco3):
    """Phân tích rối loạn acid-base"""
    disorders = []
    
    # Acidosis
    if ph < 7.35:
        if pco2 > 45:
            disorders.append({
                "type": "Respiratory Acidosis",
                "severity": "severe" if ph < 7.20 else "moderate",
                "ph": ph,
                "pco2": pco2
            })
        if hco3 < 22:
            disorders.append({
                "type": "Metabolic Acidosis",
                "severity": "severe" if hco3 < 15 else "moderate",
                "ph": ph,
                "hco3": hco3
            })
    
    # Alkalosis
    elif ph > 7.45:
        if pco2 < 35:
            disorders.append({
                "type": "Respiratory Alkalosis",
                "severity": "moderate",
                "ph": ph,
                "pco2": pco2
            })
        if hco3 > 26:
            disorders.append({
                "type": "Metabolic Alkalosis",
                "severity": "moderate",
                "ph": ph,
                "hco3": hco3
            })
    
    return disorders


def display_abg_summary(abg_data, show_details=True):
    """Hiển thị tóm tắt ABG với màu sắc cảnh báo"""
    pf_ratio = calculate_pf_ratio(abg_data["po2"], abg_data["fio2"])
    ards_class, color, description = classify_ards(pf_ratio)
    acid_base_disorders = analyze_acid_base(abg_data["ph"], abg_data["pco2"], abg_data["hco3"])
    
    if show_details:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # pH
            if 7.35 <= abg_data["ph"] <= 7.45:
                st.success(f"**pH:** {abg_data['ph']:.2f} ✓")
            elif abg_data["ph"] < 7.35:
                st.error(f"**pH:** {abg_data['ph']:.2f} ⚠️ Toan")
            else:
                st.error(f"**pH:** {abg_data['ph']:.2f} ⚠️ Kiềm")
        
        with col2:
            # P/F Ratio
            if pf_ratio:
                if color == "success":
                    st.success(f"**P/F:** {pf_ratio:.0f} ✓")
                elif color == "info":
                    st.info(f"**P/F:** {pf_ratio:.0f}")
                elif color == "warning":
                    st.warning(f"**P/F:** {pf_ratio:.0f} ⚠️")
                else:
                    st.error(f"**P/F:** {pf_ratio:.0f} ⚠️")
                st.caption(f"{ards_class} ({description})")
        
        with col3:
            # PaCO2
            if 35 <= abg_data["pco2"] <= 45:
                st.success(f"**PaCO₂:** {abg_data['pco2']:.1f} ✓")
            elif abg_data["pco2"] < 35:
                st.warning(f"**PaCO₂:** {abg_data['pco2']:.1f} ⚠️ Thấp")
            else:
                st.warning(f"**PaCO₂:** {abg_data['pco2']:.1f} ⚠️ Cao")
    
    # Acid-base disorders
    if acid_base_disorders and show_details:
        st.markdown("---")
        st.markdown("**🔬 Phân tích Acid-Base:**")
        for disorder in acid_base_disorders:
            severity_icon = "🔴" if disorder["severity"] == "severe" else "🟡"
            st.warning(f"{severity_icon} **{disorder['type']}** ({disorder['severity']})")
    
    return {
        "pf_ratio": pf_ratio,
        "ards_class": ards_class,
        "ards_color": color,
        "acid_base_disorders": acid_base_disorders
    }

