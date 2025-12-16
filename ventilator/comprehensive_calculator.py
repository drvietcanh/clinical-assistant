"""
Comprehensive Ventilator Calculator
Tính toán tổng hợp với tất cả thông số
"""

import streamlit as st
from .abg_integration import (
    render_abg_panel, 
    calculate_pf_ratio, 
    classify_ards,
    display_abg_summary
)
from .abg_advisor import (
    analyze_abg_for_ventilator,
    recommend_ventilator_adjustments,
    display_abg_recommendations,
    display_ventilator_adjustments
)
from .alerts import check_ventilator_alerts, display_alerts
from .protocols import display_protocol_recommendations
from .compliance import (
    calculate_static_compliance,
    calculate_dynamic_compliance,
    display_compliance_analysis,
    interpret_compliance as _interpret_compliance,
)
from .auto_peep import (
    estimate_auto_peep,
    display_auto_peep_analysis
)
from .history import save_ventilator_entry, render_history_panel
from .trends import render_trends_panel
from .export import render_export_panel
from .cache_utils import cached_pbw, cached_driving_pressure, cached_pf_ratio


def calculate_pbw(sex, height):
    """Tính Predicted Body Weight (PBW) - Optimized with cache"""
    return cached_pbw(sex, height)


def calculate_driving_pressure(plateau, peep):
    """Tính Driving Pressure (ΔP = Plateau - PEEP) - Optimized with cache"""
    return cached_driving_pressure(plateau, peep)


def calculate_compliance(vt, plateau, peep):
    """Tính Static Compliance (C = Vt / (Plateau - PEEP))"""
    driving_p = calculate_driving_pressure(plateau, peep)
    if driving_p and driving_p > 0 and vt > 0:
        return vt / driving_p
    return None


# Note: interpret_compliance is now imported from .compliance module
# This function is kept for backward compatibility but should use the one from compliance.py


def interpret_compliance(compliance):
    """
    Backward-compatible wrapper for tests.
    
    Returns:
        Tuple[str, str]: (interpretation, color) using static compliance thresholds.
    """
    text, color, _ = _interpret_compliance(compliance, "static")
    return text, color


def render_comprehensive_calculator():
    """Comprehensive Ventilator Calculator"""
    st.subheader("🫁 Máy Thở - Tính Toán Tổng Hợp")
    st.caption("Nhập đầy đủ thông số để có khuyến nghị chính xác")
    
    st.info("""
    **💡 Hướng dẫn:**
    - Nhập thông tin bệnh nhân và thông số máy thở
    - Nhập ABG để có phân tích đầy đủ
    - App sẽ tự động tính toán và đưa ra khuyến nghị
    """)
    
    st.markdown("---")
    
    # Layout: 3 cột
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin bệnh nhân")
        sex = st.radio(
            "Giới tính", 
            ["Nam", "Nữ"], 
            horizontal=True, 
            key="comp_sex"
        )
        height = st.number_input(
            "Chiều cao (cm)", 
            100, 220, 170, 1,
            format="%d",
            key="comp_height",
            help="Chiều cao thực tế của bệnh nhân"
        )
        
        # Calculate PBW
        pbw = calculate_pbw(sex, height)
        st.metric("PBW (Predicted Body Weight)", f"{pbw} kg")
        st.caption(f"Chiều cao: {height} cm ({sex})")
    
    with col2:
        st.markdown("### ⚙️ Thông Số Máy Thở")
        mode = st.selectbox(
            "Mode", 
            ["AC/VC", "SIMV", "PSV", "CPAP", "BiPAP", "PRVC", "APRV"],
            key="comp_mode",
            help="Chế độ thở máy"
        )
        vt = st.number_input(
            "Vt (mL)", 
            0, 1000, 0, 10,
            format="%d",
            key="comp_vt",
            help="Thể tích khí lưu thông"
        )
        rr = st.number_input(
            "RR (lần/phút)", 
            0, 50, 0, 1,
            format="%d",
            key="comp_rr",
            help="Tần số thở"
        )
        peep = st.number_input(
            "PEEP (cmH2O)", 
            0, 30, 0, 1,
            format="%d",
            key="comp_peep",
            help="Áp lực dương cuối thì thở ra"
        )
        fio2 = st.number_input(
            "FiO₂ (%)", 
            21, 100, 21, 1,
            format="%d",
            key="comp_fio2",
            help="Nồng độ O₂ trong khí thở vào"
        )
        plateau = st.number_input(
            "Plateau Pressure (cmH2O)", 
            0, 60, 0, 1,
            format="%d",
            key="comp_plateau",
            help="Áp lực cao nguyên (đo khi giữ hơi thở)"
        )
        peak = st.number_input(
            "Peak Pressure (cmH2O)", 
            0, 80, 0, 1,
            format="%d",
            key="comp_peak",
            help="Áp lực đỉnh (tùy chọn)"
        )
        ie_ratio = st.text_input(
            "I:E Ratio (ví dụ: 1:2)",
            value="1:2",
            key="comp_ie_ratio",
            help="Tỷ lệ thời gian hít vào:thở ra (ví dụ: 1:2, 1:3)"
        )
        end_expiratory_pause = st.number_input(
            "End-Expiratory Pause Pressure (cmH2O) - Tùy chọn",
            0, 50, 0, 1,
            format="%d",
            key="comp_end_exp_pause",
            help="Áp lực khi giữ hơi thở cuối thì thở ra (để tính auto-PEEP chính xác)"
        )
    
    with col3:
        st.markdown("### 💨 ABG (Khí Máu)")
        abg_data = render_abg_panel(key_prefix="comp_abg")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính Toán & Phân tích", type="primary", use_container_width=True):
        # Calculate all metrics
        pf_ratio = calculate_pf_ratio(abg_data["po2"], abg_data["fio2"])
        ards_class, ards_color, _ = classify_ards(pf_ratio)
        driving_pressure = calculate_driving_pressure(plateau, peep)
        
        # Compliance calculations
        static_compliance = calculate_static_compliance(vt, plateau, peep)
        dynamic_compliance = calculate_dynamic_compliance(vt, peak, peep) if peak > 0 else None
        compliance = static_compliance  # Use static for main display
        
        # Auto-PEEP
        end_exp_pause_value = end_expiratory_pause if end_expiratory_pause > 0 else None
        auto_peep = estimate_auto_peep(plateau, peep, end_exp_pause_value)
        
        # Get compliance interpretation
        from .compliance import interpret_compliance
        result = interpret_compliance(compliance, "static")
        if result and result[0] is not None:
            compliance_text, compliance_color, _ = result
        else:
            compliance_text, compliance_color = None, None
        vt_per_kg = (vt / pbw) if pbw > 0 and vt > 0 else None
        
        # Display ABG summary
        abg_analysis = display_abg_summary(abg_data, show_details=True)
        
        st.markdown("---")
        st.markdown("### 📊 Kết quả Tính Toán")
        
        # Metrics in 4 columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("#### 🫁 P/F Ratio & ARDS")
            if pf_ratio:
                if ards_color == "success":
                    st.success(f"**{pf_ratio:.0f}**")
                    st.caption(f"{ards_class} ✓")
                elif ards_color == "info":
                    st.info(f"**{pf_ratio:.0f}**")
                    st.caption(f"{ards_class}")
                elif ards_color == "warning":
                    st.warning(f"**{pf_ratio:.0f}** ⚠️")
                    st.caption(f"{ards_class}")
                else:
                    st.error(f"**{pf_ratio:.0f}** ⚠️")
                    st.caption(f"{ards_class}")
            else:
                st.info("Cần nhập PaO₂ & FiO₂")
        
        with col2:
            st.markdown("#### 📏 Driving Pressure")
            if driving_pressure is not None:
                if driving_pressure <= 15:
                    st.success(f"**{driving_pressure:.1f}** cmH2O ✓")
                    st.caption("Mục tiêu: ≤15 cmH2O")
                elif driving_pressure <= 18:
                    st.warning(f"**{driving_pressure:.1f}** cmH2O ⚠️")
                    st.caption("Hơi cao")
                else:
                    st.error(f"**{driving_pressure:.1f}** cmH2O ⚠️")
                    st.caption("Cao - Cần điều chỉnh")
            else:
                st.info("Cần nhập Plateau & PEEP")
        
        with col3:
            st.markdown("#### 📊 Compliance")
            if compliance:
                if compliance_color == "success":
                    st.success(f"**{compliance:.1f}** mL/cmH2O ✓")
                elif compliance_color == "error":
                    st.error(f"**{compliance:.1f}** mL/cmH2O ⚠️")
                elif compliance_color == "warning":
                    st.warning(f"**{compliance:.1f}** mL/cmH2O")
                else:
                    st.info(f"**{compliance:.1f}** mL/cmH2O")
                st.caption(f"{compliance_text}")
            else:
                st.info("Cần đủ thông số")
        
        with col4:
            st.markdown("#### 💨 Vt/kg PBW")
            if vt_per_kg:
                if vt_per_kg <= 6:
                    st.success(f"**{vt_per_kg:.1f}** mL/kg ✓")
                    st.caption("Lung-protective")
                elif vt_per_kg <= 8:
                    st.warning(f"**{vt_per_kg:.1f}** mL/kg")
                    st.caption("Có thể chấp nhận")
                else:
                    st.error(f"**{vt_per_kg:.1f}** mL/kg ⚠️")
                    st.caption("Cao - Không lung-protective")
            else:
                st.info("Cần nhập Vt")
        
        # Prepare data for advanced analysis
        vent_settings = {
            "mode": mode,
            "vt": vt,
            "rr": rr,
            "peep": peep,
            "fio2": fio2,
            "plateau": plateau,
            "peak": peak
        }
        
        calculations = {
            "pf_ratio": pf_ratio,
            "driving_pressure": driving_pressure,
            "compliance": compliance,
            "static_compliance": static_compliance,
            "dynamic_compliance": dynamic_compliance,
            "vt_per_kg": vt_per_kg,
            "auto_peep": auto_peep
        }
        
        # Advanced Alerts System
        st.markdown("---")
        alerts = check_ventilator_alerts(vent_settings, abg_data, calculations, pbw)
        display_alerts(alerts)
        
        # ABG-based Recommendations
        st.markdown("---")
        abg_recommendations = analyze_abg_for_ventilator(abg_data)
        display_abg_recommendations(abg_recommendations)
        
        # Ventilator Adjustment Recommendations
        st.markdown("---")
        vent_adjustments = recommend_ventilator_adjustments(abg_data, vent_settings, pbw)
        display_ventilator_adjustments(vent_adjustments)
        
        # Compliance Analysis
        if static_compliance or dynamic_compliance:
            st.markdown("---")
            display_compliance_analysis(
                static_compliance, 
                dynamic_compliance, 
                plateau, 
                peak, 
                peep, 
                vt, 
                pbw
            )
        
        # Auto-PEEP Analysis
        if auto_peep is not None or end_expiratory_pause > 0:
            st.markdown("---")
            display_auto_peep_analysis(
                auto_peep,
                plateau,
                peep,
                rr,
                ie_ratio,
                vt
            )
        
        # Protocol-based Recommendations
        st.markdown("---")
        display_protocol_recommendations("ARDSNet", pbw=pbw, pf_ratio=pf_ratio, has_ards=True)
        
        # Save to history (PHIÊN 5)
        patient_info = {
            "sex": sex,
            "height": height,
            "pbw": pbw
        }
        save_ventilator_entry(
            vent_settings=vent_settings,
            abg_data=abg_data,
            calculations=calculations,
            patient_info=patient_info
        )
        st.success("✅ Đã lưu vào lịch sử")
        
        # Summary table
        st.markdown("---")
        st.markdown("### 📋 Tóm Tắt Thông Số")
        
        summary_data = {
            "Thông số": ["PBW", "Vt", "Vt/kg", "RR", "PEEP", "FiO₂", "Plateau", "Driving P", "P/F", "Compliance"],
            "Giá trị": [
                f"{pbw} kg",
                f"{vt} mL" if vt > 0 else "Chưa nhập",
                f"{vt_per_kg:.1f} mL/kg" if vt_per_kg else "N/A",
                f"{rr} /phút" if rr > 0 else "Chưa nhập",
                f"{peep} cmH2O",
                f"{fio2}%",
                f"{plateau} cmH2O" if plateau > 0 else "Chưa nhập",
                f"{driving_pressure:.1f} cmH2O" if driving_pressure else "N/A",
                f"{pf_ratio:.0f}" if pf_ratio else "N/A",
                f"{compliance:.1f} mL/cmH2O" if compliance else "N/A"
            ]
        }
        
        import pandas as pd
        df = pd.DataFrame(summary_data)
        st.dataframe(df, hide_index=True, use_container_width=True)
        
        # PHIÊN 5: History, Trends, Export Tabs
        st.markdown("---")
        st.markdown("### 📊 Lịch Sử & Xu Hướng (PHIÊN 5)")
        
        tab1, tab2, tab3 = st.tabs(["📜 Lịch Sử", "📈 Xu Hướng", "📤 Export"])
        
        with tab1:
            render_history_panel()
        
        with tab2:
            render_trends_panel()
        
        with tab3:
            render_export_panel()
        
        # Expandable reference
        with st.expander("📚 Thông tin thêm"):
            st.markdown("""
            **Công thức:**
            - **PBW:** Nam = 50 + 0.91 × (Height - 152.4), Nữ = 45.5 + 0.91 × (Height - 152.4)
            - **P/F Ratio:** PaO₂ / FiO₂
            - **Driving Pressure:** Plateau - PEEP
            - **Compliance:** Vt / (Plateau - PEEP)
            - **Vt/kg:** Vt / PBW
            
            **Mục Tiêu:**
            - Vt/kg: ≤6-8 mL/kg PBW (lung-protective)
            - Plateau: ≤30 cmH2O
            - Driving P: ≤15 cmH2O
            - P/F: >200 (ARDS nhẹ), >100 (ARDS trung bình)
            - Compliance: 30-50 mL/cmH2O (bình thường)
            
            **References:**
            - ARDSNet Protocol (2000)
            - Surviving Sepsis Campaign 2021
            - ATS/ERS Guidelines
            """)

