"""
Hemodynamic Monitoring Tools
SVV, PPV, Cardiac Output, SVR calculations and interpretations
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def calculate_svv(svv_value: float) -> dict:
    """
    Calculate and interpret Stroke Volume Variation (SVV)
    
    SVV is a dynamic parameter to assess fluid responsiveness
    Measured by pulse contour analysis or esophageal Doppler
    
    Args:
        svv_value: SVV percentage
    
    Returns:
        Dictionary with interpretation
    """
    if svv_value < 10:
        interpretation = "Không đáp ứng dịch - Không cần bù dịch"
        color = "success"
        recommendation = "Không cần bù dịch. Cân nhắc giảm dịch nếu quá tải."
    elif svv_value < 13:
        interpretation = "Có thể đáp ứng dịch - Theo dõi"
        color = "info"
        recommendation = "Theo dõi sát. Cân nhắc bù dịch nếu có dấu hiệu thiếu dịch."
    else:
        interpretation = "Đáp ứng dịch - Cần bù dịch"
        color = "warning"
        recommendation = "Bệnh nhân có thể đáp ứng với bù dịch. Cân nhắc fluid challenge."
    
    return {
        "svv": svv_value,
        "interpretation": interpretation,
        "color": color,
        "recommendation": recommendation
    }


def calculate_ppv(ppv_value: float) -> dict:
    """
    Calculate and interpret Pulse Pressure Variation (PPV)
    
    PPV is a dynamic parameter to assess fluid responsiveness
    Requires mechanical ventilation and sinus rhythm
    
    Args:
        ppv_value: PPV percentage
    
    Returns:
        Dictionary with interpretation
    """
    if ppv_value < 10:
        interpretation = "Không đáp ứng dịch - Không cần bù dịch"
        color = "success"
        recommendation = "Không cần bù dịch. Cân nhắc giảm dịch nếu quá tải."
    elif ppv_value < 13:
        interpretation = "Có thể đáp ứng dịch - Theo dõi"
        color = "info"
        recommendation = "Theo dõi sát. Cân nhắc bù dịch nếu có dấu hiệu thiếu dịch."
    else:
        interpretation = "Đáp ứng dịch - Cần bù dịch"
        color = "warning"
        recommendation = "Bệnh nhân có thể đáp ứng với bù dịch. Cân nhắc fluid challenge."
    
    return {
        "ppv": ppv_value,
        "interpretation": interpretation,
        "color": color,
        "recommendation": recommendation
    }


def calculate_cardiac_output(map: float, cvp: float, svr: float) -> dict:
    """
    Calculate Cardiac Output from MAP, CVP, and SVR
    
    CO = (MAP - CVP) / SVR × 80
    
    Args:
        map: Mean Arterial Pressure (mmHg)
        cvp: Central Venous Pressure (mmHg)
        svr: Systemic Vascular Resistance (dynes·s/cm⁵)
    
    Returns:
        Dictionary with CO and CI
    """
    if svr > 0:
        co = ((map - cvp) / svr) * 80  # Convert to L/min
    else:
        co = None
    
    return {
        "co": co,
        "map": map,
        "cvp": cvp,
        "svr": svr
    }


def calculate_cardiac_index(co: float, bsa: float) -> dict:
    """
    Calculate Cardiac Index
    
    CI = CO / BSA
    
    Args:
        co: Cardiac Output (L/min)
        bsa: Body Surface Area (m²)
    
    Returns:
        Dictionary with CI and interpretation
    """
    if bsa > 0:
        ci = co / bsa
    else:
        ci = None
    
    if ci:
        if ci < 2.0:
            interpretation = "Thấp - Suy tim nặng"
            color = "error"
        elif ci < 2.5:
            interpretation = "Giảm - Suy tim"
            color = "warning"
        elif ci <= 4.0:
            interpretation = "Bình thường"
            color = "success"
        else:
            interpretation = "Tăng - Tăng cung lượng tim"
            color = "info"
    else:
        interpretation = None
        color = None
    
    return {
        "ci": ci,
        "co": co,
        "bsa": bsa,
        "interpretation": interpretation,
        "color": color
    }


def calculate_svr(map: float, cvp: float, co: float) -> dict:
    """
    Calculate Systemic Vascular Resistance
    
    SVR = ((MAP - CVP) / CO) × 80
    
    Args:
        map: Mean Arterial Pressure (mmHg)
        cvp: Central Venous Pressure (mmHg)
        co: Cardiac Output (L/min)
    
    Returns:
        Dictionary with SVR and interpretation
    """
    if co > 0:
        svr = ((map - cvp) / co) * 80  # dynes·s/cm⁵
    else:
        svr = None
    
    if svr:
        if svr < 800:
            interpretation = "Thấp - Giãn mạch (sốc phân bố)"
            color = "warning"
        elif svr <= 1200:
            interpretation = "Bình thường"
            color = "success"
        else:
            interpretation = "Cao - Co mạch (sốc tim, sốc do thiếu dịch)"
            color = "error"
    else:
        interpretation = None
        color = None
    
    return {
        "svr": svr,
        "map": map,
        "cvp": cvp,
        "co": co,
        "interpretation": interpretation,
        "color": color
    }


def calculate_bsa(height_cm: float, weight_kg: float, formula: str = "DuBois") -> float:
    """
    Calculate Body Surface Area
    
    Args:
        height_cm: Height in cm
        weight_kg: Weight in kg
        formula: "DuBois" or "Mosteller"
    
    Returns:
        BSA in m²
    """
    if formula == "DuBois":
        # BSA = 0.007184 × height^0.725 × weight^0.425
        bsa = 0.007184 * (height_cm ** 0.725) * (weight_kg ** 0.425)
    else:  # Mosteller
        # BSA = sqrt((height × weight) / 3600)
        bsa = ((height_cm * weight_kg) / 3600) ** 0.5
    
    return bsa


def render_svv_calculator():
    """Render SVV calculator"""
    st.subheader("📊 Stroke Volume Variation (SVV)")
    st.caption("Đánh giá đáp ứng dịch bằng SVV")
    
    st.markdown("""
    **SVV** là thông số động để đánh giá đáp ứng dịch:
    - Đo bằng pulse contour analysis hoặc esophageal Doppler
    - Yêu cầu: Thở máy, nhịp xoang, không có rối loạn nhịp
    - **SVV >13%:** Đáp ứng dịch (có thể bù dịch)
    - **SVV <10%:** Không đáp ứng dịch (không cần bù dịch)
    """)
    
    st.markdown("---")
    
    svv_value = st.number_input(
        "SVV (%):",
        min_value=0.0,
        max_value=50.0,
        value=12.0,
        step=0.1,
        key="svv_value"
    )
    
    result = calculate_svv(svv_value)
    
    render_result_card(
        title="SVV",
        value=f"{result['svv']:.1f}",
        unit="%",
        color=result['color'],
        subtitle=result['interpretation']
    )
    
    st.info(f"**Khuyến nghị:** {result['recommendation']}")
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Lưu ý")
    st.warning("""
    **Hạn chế của SVV:**
    - Chỉ chính xác khi thở máy với Vt ≥8 mL/kg
    - Không chính xác khi có rối loạn nhịp
    - Không chính xác khi có tự thở
    - Cần đo liên tục (không phải một lần)
    """)


def render_ppv_calculator():
    """Render PPV calculator"""
    st.subheader("📊 Pulse Pressure Variation (PPV)")
    st.caption("Đánh giá đáp ứng dịch bằng PPV")
    
    st.markdown("""
    **PPV** là thông số động để đánh giá đáp ứng dịch:
    - Đo từ huyết áp động mạch
    - Yêu cầu: Thở máy, nhịp xoang, không có rối loạn nhịp
    - **PPV >13%:** Đáp ứng dịch (có thể bù dịch)
    - **PPV <10%:** Không đáp ứng dịch (không cần bù dịch)
    """)
    
    st.markdown("---")
    
    ppv_value = st.number_input(
        "PPV (%):",
        min_value=0.0,
        max_value=50.0,
        value=12.0,
        step=0.1,
        key="ppv_value"
    )
    
    result = calculate_ppv(ppv_value)
    
    render_result_card(
        title="PPV",
        value=f"{result['ppv']:.1f}",
        unit="%",
        color=result['color'],
        subtitle=result['interpretation']
    )
    
    st.info(f"**Khuyến nghị:** {result['recommendation']}")
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Lưu ý")
    st.warning("""
    **Hạn chế của PPV:**
    - Chỉ chính xác khi thở máy với Vt ≥8 mL/kg
    - Không chính xác khi có rối loạn nhịp
    - Không chính xác khi có tự thở
    - Không chính xác khi có ARDS nặng
    """)


def render_cardiac_output_calculator():
    """Render Cardiac Output calculator"""
    st.subheader("❤️ Cardiac Output / Cardiac Index")
    st.caption("Tính toán cung lượng tim và chỉ số tim")
    
    st.markdown("---")
    
    # Method selection
    method = st.radio(
        "Phương pháp tính:",
        ["Từ MAP, CVP, SVR", "Nhập trực tiếp CO"],
        key="co_method"
    )
    
    if method == "Từ MAP, CVP, SVR":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            map = st.number_input("MAP (mmHg):", min_value=0.0, value=70.0, key="co_map")
        
        with col2:
            cvp = st.number_input("CVP (mmHg):", min_value=0.0, value=8.0, key="co_cvp")
        
        with col3:
            svr = st.number_input("SVR (dynes·s/cm⁵):", min_value=0.0, value=1000.0, key="co_svr")
        
        result = calculate_cardiac_output(map, cvp, svr)
        co = result['co']
    else:
        co = st.number_input("Cardiac Output (L/min):", min_value=0.0, value=5.0, key="co_direct")
    
    if co:
        # Calculate CI
        st.markdown("### 📏 Thông tin bệnh nhân")
        col1, col2 = st.columns(2)
        
        with col1:
            height = st.number_input("Chiều cao (cm):", min_value=0.0, value=170.0, key="co_height")
        
        with col2:
            weight = st.number_input("Cân nặng (kg):", min_value=0.0, value=70.0, key="co_weight")
        
        bsa = calculate_bsa(height, weight)
        ci_result = calculate_cardiac_index(co, bsa)
        
        # Display results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            render_result_card(
                title="Cardiac Output",
                value=f"{co:.2f}",
                unit="L/min",
                color="info",
                subtitle="Target: 4-8 L/min"
            )
        
        with col2:
            render_result_card(
                title="Cardiac Index",
                value=f"{ci_result['ci']:.2f}",
                unit="L/min/m²",
                color=ci_result['color'],
                subtitle=ci_result['interpretation']
            )
        
        with col3:
            render_result_card(
                title="BSA",
                value=f"{bsa:.2f}",
                unit="m²",
                color="info",
                subtitle="Body Surface Area"
            )
        
        # Interpretation
        if ci_result['ci']:
            if ci_result['color'] == 'error':
                st.error(f"⚠️ {ci_result['interpretation']} - Cần can thiệp")
            elif ci_result['color'] == 'warning':
                st.warning(f"⚠️ {ci_result['interpretation']} - Theo dõi sát")
            else:
                st.success(f"✅ {ci_result['interpretation']}")


def render_svr_calculator():
    """Render SVR calculator"""
    st.subheader("💉 Systemic Vascular Resistance (SVR)")
    st.caption("Tính toán sức cản mạch hệ thống")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        map = st.number_input("MAP (mmHg):", min_value=0.0, value=70.0, key="svr_map")
    
    with col2:
        cvp = st.number_input("CVP (mmHg):", min_value=0.0, value=8.0, key="svr_cvp")
    
    with col3:
        co = st.number_input("Cardiac Output (L/min):", min_value=0.0, value=5.0, key="svr_co")
    
    result = calculate_svr(map, cvp, co)
    
    if result['svr']:
        render_result_card(
            title="SVR",
            value=f"{result['svr']:.0f}",
            unit="dynes·s/cm⁵",
            color=result['color'],
            subtitle=result['interpretation']
        )
        
        st.info(f"**Giá trị bình thường:** 800-1200 dynes·s/cm⁵")
        
        if result['color'] == 'error':
            st.error(f"⚠️ {result['interpretation']} - Cần đánh giá nguyên nhân")
        elif result['color'] == 'warning':
            st.warning(f"⚠️ {result['interpretation']} - Theo dõi sát")


def render_hemodynamics():
    """Main function to render hemodynamic monitoring tools"""
    st.header("💉 Hemodynamic Monitoring")
    st.caption("Công cụ đánh giá huyết động và đáp ứng dịch")
    
    tabs = st.tabs([
        "📊 SVV",
        "📊 PPV",
        "❤️ Cardiac Output",
        "💉 SVR"
    ])
    
    with tabs[0]:
        render_svv_calculator()
    
    with tabs[1]:
        render_ppv_calculator()
    
    with tabs[2]:
        render_cardiac_output_calculator()
    
    with tabs[3]:
        render_svr_calculator()
