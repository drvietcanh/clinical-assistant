"""
Renal Replacement Therapy (RRT) Calculator
CRRT, IHD, SLED dosing and anticoagulation
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def calculate_crrt_dosing(weight_kg: float, target_clearance: float = 25.0) -> dict:
    """
    Calculate CRRT (Continuous Renal Replacement Therapy) dosing
    
    Args:
        weight_kg: Patient weight in kg
        target_clearance: Target clearance rate (ml/kg/h, default 25)
    
    Returns:
        Dictionary with CRRT dosing recommendations
    """
    # CRRT clearance = Dialysate flow + Replacement flow (pre/post)
    # Target: 25-35 ml/kg/h for adequate clearance
    
    target_flow_ml_h = weight_kg * target_clearance
    target_flow_l_h = target_flow_ml_h / 1000
    
    # Typical CRRT settings
    dialysate_flow = target_flow_ml_h * 0.5  # 50% dialysate
    replacement_flow = target_flow_ml_h * 0.5  # 50% replacement
    
    return {
        "target_clearance": target_clearance,
        "total_flow_ml_h": target_flow_ml_h,
        "total_flow_l_h": target_flow_l_h,
        "dialysate_flow_ml_h": dialysate_flow,
        "replacement_flow_ml_h": replacement_flow,
        "weight_kg": weight_kg
    }


def calculate_ihd_dosing(weight_kg: float, target_kt_v: float = 1.2) -> dict:
    """
    Calculate IHD (Intermittent Hemodialysis) dosing
    
    Args:
        weight_kg: Patient weight in kg
        target_kt_v: Target Kt/V (default 1.2 for adequate dialysis)
    
    Returns:
        Dictionary with IHD dosing recommendations
    """
    # Kt/V = (Dialysate flow × Time) / (Volume of distribution)
    # V ≈ 0.58 × weight (for urea distribution)
    
    v_urea = weight_kg * 0.58  # Volume of distribution for urea (L)
    
    # Typical IHD: 3-4 hours, dialysate flow 500-800 ml/min
    # Kt = Kt/V × V
    kt = target_kt_v * v_urea
    
    # Typical dialysate flow: 500 ml/min = 30 L/h
    dialysate_flow_ml_min = 500
    dialysate_flow_l_h = dialysate_flow_ml_min * 60 / 1000
    
    # Time needed: t = Kt / (K = dialysate flow)
    time_hours = kt / dialysate_flow_l_h
    
    return {
        "target_kt_v": target_kt_v,
        "v_urea_liters": v_urea,
        "kt": kt,
        "dialysate_flow_ml_min": dialysate_flow_ml_min,
        "dialysate_flow_l_h": dialysate_flow_l_h,
        "time_hours": time_hours,
        "weight_kg": weight_kg
    }


def calculate_sled_dosing(weight_kg: float, duration_hours: float = 8.0) -> dict:
    """
    Calculate SLED (Sustained Low-Efficiency Dialysis) dosing
    
    Args:
        weight_kg: Patient weight in kg
        duration_hours: Duration of SLED session (hours, default 8)
    
    Returns:
        Dictionary with SLED dosing recommendations
    """
    # SLED: Lower dialysate flow, longer duration
    # Typical: 200-300 ml/min dialysate flow, 6-12 hours
    
    dialysate_flow_ml_min = 250  # Typical SLED flow
    dialysate_flow_l_h = dialysate_flow_ml_min * 60 / 1000
    
    total_flow_l = dialysate_flow_l_h * duration_hours
    
    # Calculate Kt/V
    v_urea = weight_kg * 0.58
    kt = dialysate_flow_l_h * duration_hours
    kt_v = kt / v_urea if v_urea > 0 else 0
    
    return {
        "duration_hours": duration_hours,
        "dialysate_flow_ml_min": dialysate_flow_ml_min,
        "dialysate_flow_l_h": dialysate_flow_l_h,
        "total_flow_l": total_flow_l,
        "kt_v": kt_v,
        "weight_kg": weight_kg
    }


def calculate_anticoagulation_rrt(weight_kg: float, rrt_type: str, 
                                  has_bleeding_risk: bool = False) -> dict:
    """
    Calculate anticoagulation for RRT
    
    Args:
        weight_kg: Patient weight in kg
        rrt_type: Type of RRT ("CRRT", "IHD", "SLED")
        has_bleeding_risk: Whether patient has bleeding risk
    
    Returns:
        Dictionary with anticoagulation recommendations
    """
    if has_bleeding_risk:
        return {
            "anticoagulation": "No anticoagulation (bleeding risk)",
            "heparin_dose": None,
            "citrate_dose": None,
            "color": "warning",
            "recommendations": [
                "No anticoagulation",
                "Regional citrate (if available)",
                "Frequent circuit flushing",
                "Monitor circuit patency"
            ]
        }
    
    if rrt_type == "CRRT":
        # Heparin: 5-10 U/kg/h (typical)
        heparin_dose_u_h = weight_kg * 7.5  # Average
        heparin_dose_u_kg_h = 7.5
        
        # Citrate: 2-4 mmol/L blood flow (regional anticoagulation)
        citrate_dose_mmol_l = 3.0
        
        return {
            "anticoagulation": "Heparin or Citrate",
            "heparin_dose_u_h": heparin_dose_u_h,
            "heparin_dose_u_kg_h": heparin_dose_u_kg_h,
            "citrate_dose_mmol_l": citrate_dose_mmol_l,
            "color": "info",
            "recommendations": [
                "Heparin: 5-10 U/kg/h (target aPTT 1.5-2x normal)",
                "Citrate: 2-4 mmol/L blood flow (regional, preferred if available)",
                "Monitor aPTT (heparin) or ionized Ca (citrate)",
                "Adjust based on circuit patency"
            ]
        }
    else:  # IHD or SLED
        # Heparin: Bolus + maintenance
        heparin_bolus_u = weight_kg * 50  # 50 U/kg bolus
        heparin_maintenance_u_h = weight_kg * 10  # 10 U/kg/h
        
        return {
            "anticoagulation": "Heparin",
            "heparin_bolus_u": heparin_bolus_u,
            "heparin_maintenance_u_h": heparin_maintenance_u_h,
            "color": "info",
            "recommendations": [
                "Bolus: 50 U/kg at start",
                "Maintenance: 10 U/kg/h",
                "Target aPTT: 1.5-2x normal",
                "Stop 30-60 min before end of session"
            ]
        }


def render_crrt_calculator():
    """Render CRRT dosing calculator"""
    st.subheader("💧 CRRT (Continuous Renal Replacement Therapy)")
    st.caption("Tính toán liều CRRT")
    
    st.markdown("""
    **CRRT:** Continuous dialysis, ưu tiên cho bệnh nhân hemodynamic không ổn định.
    - Target clearance: **25-35 ml/kg/h**
    - Dialysate + Replacement flow
    - 24/7 continuous
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="crrt_weight"
        )
    
    with col2:
        target_clearance = st.number_input(
            "Target clearance (ml/kg/h):",
            min_value=20,
            max_value=40,
            value=25,
            step=1,
            format="%d",
            key="crrt_clearance",
            help="Typical: 25-35 ml/kg/h"
        )
    
    if st.button("Tính toán", type="primary", key="calc_crrt"):
        results = calculate_crrt_dosing(weight_kg, target_clearance)
        
        st.markdown("### 📊 Kết Quả")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            render_result_box(
                "Total Flow",
                f"{results['total_flow_ml_h']:.0f} ml/h",
                subtitle=f"{results['total_flow_l_h']:.2f} L/h",
                color="primary",
                icon="💧"
            )
        
        with col2:
            render_result_box(
                "Dialysate Flow",
                f"{results['dialysate_flow_ml_h']:.0f} ml/h",
                subtitle="50% of total",
                color="info"
            )
        
        with col3:
            render_result_box(
                "Replacement Flow",
                f"{results['replacement_flow_ml_h']:.0f} ml/h",
                subtitle="50% of total",
                color="info"
            )
        
        st.markdown("---")
        st.info(f"""
        **💡 Khuyến nghị:**
        - **Total flow:** {results['total_flow_ml_h']:.0f} ml/h ({results['total_flow_l_h']:.2f} L/h)
        - **Dialysate:** {results['dialysate_flow_ml_h']:.0f} ml/h
        - **Replacement:** {results['replacement_flow_ml_h']:.0f} ml/h (pre- or post-dilution)
        - **Target clearance:** {target_clearance:.0f} ml/kg/h
        - **Duration:** Continuous (24/7)
        """)


def render_ihd_calculator():
    """Render IHD dosing calculator"""
    st.subheader("💉 IHD (Intermittent Hemodialysis)")
    st.caption("Tính toán liều IHD")
    
    st.markdown("""
    **IHD:** Intermittent dialysis, ưu tiên cho bệnh nhân hemodynamic ổn định.
    - Target Kt/V: **≥1.2** (adequate dialysis)
    - Typical: 3-4 hours, 3-4 times/week
    - Dialysate flow: 500-800 ml/min
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="ihd_weight"
        )
    
    with col2:
        target_kt_v = st.number_input(
            "Target Kt/V:",
            min_value=1.0,
            max_value=2.0,
            value=1.2,
            step=0.1,
            key="ihd_ktv",
            help="Adequate: ≥1.2"
        )
    
    if st.button("Tính toán", type="primary", key="calc_ihd"):
        results = calculate_ihd_dosing(weight_kg, target_kt_v)
        
        st.markdown("### 📊 Kết Quả")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            render_result_box(
                "Kt/V",
                f"{target_kt_v:.2f}",
                subtitle="Target achieved",
                color="success",
                icon="📊"
            )
        
        with col2:
            render_result_box(
                "Dialysate Flow",
                f"{results['dialysate_flow_ml_min']:.0f} ml/min",
                subtitle=f"{results['dialysate_flow_l_h']:.1f} L/h",
                color="info"
            )
        
        with col3:
            render_result_box(
                "Time Needed",
                f"{results['time_hours']:.1f} hours",
                subtitle="To achieve Kt/V",
                color="info"
            )
        
        st.markdown("---")
        st.info(f"""
        **💡 Khuyến nghị:**
        - **Dialysate flow:** {results['dialysate_flow_ml_min']:.0f} ml/min ({results['dialysate_flow_l_h']:.1f} L/h)
        - **Duration:** {results['time_hours']:.1f} hours (typical: 3-4 hours)
        - **Frequency:** 3-4 times/week
        - **Target Kt/V:** {target_kt_v:.2f} (adequate: ≥1.2)
        - **V (urea):** {results['v_urea_liters']:.1f} L
        """)


def render_sled_calculator():
    """Render SLED dosing calculator"""
    st.subheader("🔄 SLED (Sustained Low-Efficiency Dialysis)")
    st.caption("Tính toán liều SLED")
    
    st.markdown("""
    **SLED:** Sustained low-efficiency dialysis, thỏa hiệp giữa CRRT và IHD.
    - Lower dialysate flow (200-300 ml/min)
    - Longer duration (6-12 hours)
    - Better hemodynamic tolerance than IHD
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="sled_weight"
        )
    
    with col2:
        duration_hours = st.number_input(
            "Duration (hours):",
            min_value=6.0,
            max_value=12.0,
            value=8.0,
            step=0.5,
            format="%.1f",
            key="sled_duration",
            help="Typical: 6-12 hours"
        )
    
    if st.button("Tính toán", type="primary", key="calc_sled"):
        results = calculate_sled_dosing(weight_kg, duration_hours)
        
        st.markdown("### 📊 Kết Quả")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            render_result_box(
                "Kt/V",
                f"{results['kt_v']:.2f}",
                subtitle="Achieved",
                color="success",
                icon="📊"
            )
        
        with col2:
            render_result_box(
                "Dialysate Flow",
                f"{results['dialysate_flow_ml_min']:.0f} ml/min",
                subtitle=f"{results['dialysate_flow_l_h']:.1f} L/h",
                color="info"
            )
        
        with col3:
            render_result_box(
                "Duration",
                f"{duration_hours:.1f} hours",
                subtitle="Per session",
                color="info"
            )
        
        st.markdown("---")
        st.info(f"""
        **💡 Khuyến nghị:**
        - **Dialysate flow:** {results['dialysate_flow_ml_min']:.0f} ml/min ({results['dialysate_flow_l_h']:.1f} L/h)
        - **Duration:** {duration_hours:.1f} hours per session
        - **Total flow:** {results['total_flow_l']:.1f} L per session
        - **Kt/V:** {results['kt_v']:.2f}
        - **Frequency:** Daily or every other day
        """)


def render_anticoagulation_calculator():
    """Render anticoagulation calculator"""
    st.subheader("💉 Anticoagulation for RRT")
    st.caption("Tính toán liều chống đông cho RRT")
    
    st.markdown("""
    **Anticoagulation:** Cần thiết để duy trì patency của circuit RRT.
    - **Heparin:** Standard, cần monitor aPTT
    - **Citrate:** Regional anticoagulation, ưu tiên nếu có
    - **No anticoagulation:** Nếu có nguy cơ chảy máu
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="anticoag_weight"
        )
    
    with col2:
        rrt_type = st.selectbox(
            "Loại RRT:",
            ["CRRT", "IHD", "SLED"],
            key="anticoag_rrt_type"
        )
    
    has_bleeding_risk = st.checkbox(
        "Có nguy cơ chảy máu",
        key="anticoag_bleeding",
        help="Active bleeding, recent surgery, coagulopathy"
    )
    
    if st.button("Tính toán", type="primary", key="calc_anticoag"):
        results = calculate_anticoagulation_rrt(weight_kg, rrt_type, has_bleeding_risk)
        
        st.markdown("### 📊 Kết Quả")
        
        render_result_box(
            "Anticoagulation",
            results["anticoagulation"],
            color=results["color"],
            icon="💉"
        )
        
        st.markdown("---")
        
        if results["heparin_dose_u_h"]:
            st.markdown("### 💊 Liều Heparin")
            
            if rrt_type == "CRRT":
                col1, col2 = st.columns(2)
                
                with col1:
                    render_result_box(
                        "Heparin",
                        f"{results['heparin_dose_u_h']:.0f} U/h",
                        subtitle=f"{results['heparin_dose_u_kg_h']:.1f} U/kg/h",
                        color="info"
                    )
                
                with col2:
                    if results.get("citrate_dose_mmol_l"):
                        render_result_box(
                            "Citrate",
                            f"{results['citrate_dose_mmol_l']:.1f} mmol/L",
                            subtitle="Blood flow",
                            color="info"
                        )
            else:
                render_result_box(
                    "Heparin Bolus",
                    f"{results['heparin_bolus_u']:.0f} U",
                    subtitle=f"At start + {results['heparin_maintenance_u_h']:.0f} U/h",
                    color="info"
                )
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến Nghị")
        
        for rec in results["recommendations"]:
            st.markdown(f"- {rec}")


def render_rrt_calculator():
    """Main function to render RRT calculator"""
    
    st.markdown("## 🩺 Renal Replacement Therapy (RRT)")
    st.markdown("""
    Tính toán liều RRT cho bệnh nhân suy thận cấp:
    - CRRT (Continuous RRT) - Cho bệnh nhân hemodynamic không ổn định
    - IHD (Intermittent Hemodialysis) - Cho bệnh nhân hemodynamic ổn định
    - SLED (Sustained Low-Efficiency Dialysis) - Thỏa hiệp giữa CRRT và IHD
    - Anticoagulation - Chống đông cho RRT circuit
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3, tab4 = st.tabs([
        "💧 CRRT",
        "💉 IHD",
        "🔄 SLED",
        "💉 Anticoagulation"
    ])
    
    with tab1:
        render_crrt_calculator()
    
    with tab2:
        render_ihd_calculator()
    
    with tab3:
        render_sled_calculator()
    
    with tab4:
        render_anticoagulation_calculator()
    
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các tính toán này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Tuân thủ hướng dẫn địa phương và quy định bệnh viện
    - Tư vấn thận học khi cần
    """)

