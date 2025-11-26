"""
Vancomycin TDM Calculator
Therapeutic Drug Monitoring cho Vancomycin
AUC-based dosing (preferred) hoặc Trough-based dosing
"""

import streamlit as st
import math
from drugs.tdm.base_template import TDMCalculator


def calculate_vancomycin_auc(peak_mg_l, trough_mg_l, infusion_time_hours=1.0):
    """
    Calculate Vancomycin AUC using trapezoidal method
    
    Args:
        peak_mg_l: Peak level (mg/L)
        trough_mg_l: Trough level (mg/L)
        infusion_time_hours: Infusion time in hours
    
    Returns:
        AUC in mg·h/L
    """
    # Simplified AUC calculation
    # AUC = (peak + trough) / 2 * tau
    # Where tau is dosing interval
    
    # For continuous infusion or steady state
    # More accurate: AUC = (peak - trough) / k + trough * tau
    # Where k = elimination rate constant
    
    # Simplified version for quick calculation
    # Assuming linear decline between peak and trough
    avg_level = (peak_mg_l + trough_mg_l) / 2
    tau = 12  # Default dosing interval (can be adjusted)
    auc = avg_level * tau
    
    return auc


def calculate_vancomycin_dose_auc_based(
    weight_kg,
    crcl,
    target_auc=400,
    current_auc=None,
    current_dose_mg=None
):
    """
    Calculate Vancomycin dose based on AUC target (400-600 mg·h/L)
    
    Args:
        weight_kg: Body weight
        crcl: Creatinine clearance
        target_auc: Target AUC (default 400-600)
        current_auc: Current AUC if available
        current_dose_mg: Current dose if available
    
    Returns:
        dict with dosing information
    """
    # AUC-based dosing formula
    # Maintenance dose (mg) = (target AUC × CrCl) / F
    # Where F is bioavailability (1.0 for IV)
    
    # Simplified: Dose (mg) = target_AUC × CrCl × 0.5
    # More accurate formulas exist but this is a reasonable approximation
    
    if current_auc and current_dose_mg:
        # Dose adjustment based on current AUC
        dose_ratio = target_auc / current_auc
        new_dose = current_dose_mg * dose_ratio
    else:
        # Initial dose calculation
        # Formula: Dose (mg) = target_AUC × CrCl × 0.5
        new_dose = target_auc * crcl * 0.5
    
    # Round to practical dosing (usually 250mg, 500mg, 750mg, 1000mg, 1250mg, 1500mg)
    practical_doses = [250, 500, 750, 1000, 1250, 1500, 1750, 2000]
    closest_dose = min(practical_doses, key=lambda x: abs(x - new_dose))
    
    # Determine frequency based on CrCl
    if crcl >= 80:
        frequency = 8  # Q8h
    elif crcl >= 50:
        frequency = 12  # Q12h
    elif crcl >= 30:
        frequency = 24  # Q24h
    else:
        frequency = 48  # Q48h
    
    return {
        "dose_mg": closest_dose,
        "dose_mg_calculated": new_dose,
        "frequency_hours": frequency,
        "target_auc": target_auc,
        "dosing_interval": f"Q{frequency}h"
    }


def calculate_vancomycin_dose_trough_based(
    weight_kg,
    crcl,
    target_trough=15,
    current_trough=None,
    current_dose_mg=None
):
    """
    Calculate Vancomycin dose based on trough target (10-20 mg/L)
    
    Args:
        weight_kg: Body weight
        crcl: Creatinine clearance
        target_trough: Target trough (10-20 mg/L)
        current_trough: Current trough if available
        current_dose_mg: Current dose if available
    
    Returns:
        dict with dosing information
    """
    if current_trough and current_dose_mg:
        # Dose adjustment based on current trough
        dose_ratio = target_trough / current_trough
        new_dose = current_dose_mg * dose_ratio
    else:
        # Initial dose calculation
        # Loading dose: 20-25 mg/kg
        loading_dose = weight_kg * 20
        
        # Maintenance dose: 15-20 mg/kg/day, adjusted for renal function
        base_dose_per_kg = 15
        if crcl < 30:
            base_dose_per_kg = 10
        elif crcl < 50:
            base_dose_per_kg = 12
        
        daily_dose = base_dose_per_kg * weight_kg
        new_dose = daily_dose
    
    # Round to practical dosing
    practical_doses = [250, 500, 750, 1000, 1250, 1500, 1750, 2000]
    closest_dose = min(practical_doses, key=lambda x: abs(x - new_dose))
    
    # Determine frequency
    if crcl >= 80:
        frequency = 8
    elif crcl >= 50:
        frequency = 12
    elif crcl >= 30:
        frequency = 24
    else:
        frequency = 48
    
    return {
        "loading_dose_mg": loading_dose if not current_trough else None,
        "dose_mg": closest_dose,
        "dose_mg_calculated": new_dose,
        "frequency_hours": frequency,
        "target_trough": target_trough,
        "dosing_interval": f"Q{frequency}h"
    }


def interpret_vancomycin_level(trough_mg_l=None, peak_mg_l=None, auc=None):
    """
    Interpret Vancomycin levels
    
    Args:
        trough_mg_l: Trough level (mg/L)
        peak_mg_l: Peak level (mg/L) - optional
        auc: AUC (mg·h/L) - optional
    
    Returns:
        dict with interpretation
    """
    results = []
    
    # Trough interpretation
    if trough_mg_l is not None:
        if trough_mg_l < 10:
            status = "subtherapeutic"
            level_text = "⬇️ Trough thấp (< 10 mg/L)"
            recommendation = "Trough thấp. Cân nhắc tăng liều hoặc rút ngắn khoảng cách liều."
            color = "info"
        elif trough_mg_l <= 20:
            status = "therapeutic"
            level_text = "✅ Trough trong mục tiêu (10-20 mg/L)"
            recommendation = "Trough trong khoảng điều trị. Tiếp tục liều hiện tại."
            color = "success"
        elif trough_mg_l <= 25:
            status = "supratherapeutic"
            level_text = "⚠️ Trough hơi cao (20-25 mg/L)"
            recommendation = "Trough hơi cao. Theo dõi độc tính thận. Cân nhắc giảm liều."
            color = "warning"
        else:
            status = "toxic"
            level_text = "🚨 Trough quá cao (> 25 mg/L) - Nguy cơ độc thận"
            recommendation = "Trough quá cao! Nguy cơ độc tính thận và ốc tai. Giảm liều ngay, theo dõi creatinine."
            color = "error"
        
        results.append({
            "type": "trough",
            "value": trough_mg_l,
            "status": status,
            "level_text": level_text,
            "recommendation": recommendation,
            "color": color
        })
    
    # AUC interpretation (preferred method)
    if auc is not None:
        if auc < 400:
            status = "subtherapeutic"
            level_text = "⬇️ AUC thấp (< 400 mg·h/L)"
            recommendation = "AUC thấp. Cân nhắc tăng liều để đạt AUC 400-600 mg·h/L."
            color = "info"
        elif auc <= 600:
            status = "therapeutic"
            level_text = "✅ AUC trong mục tiêu (400-600 mg·h/L)"
            recommendation = "AUC trong khoảng điều trị tối ưu. Tiếp tục liều hiện tại."
            color = "success"
        elif auc <= 800:
            status = "supratherapeutic"
            level_text = "⚠️ AUC hơi cao (600-800 mg·h/L)"
            recommendation = "AUC hơi cao. Theo dõi độc tính. Cân nhắc giảm liều."
            color = "warning"
        else:
            status = "toxic"
            level_text = "🚨 AUC quá cao (> 800 mg·h/L) - Nguy cơ độc thận"
            recommendation = "AUC quá cao! Nguy cơ độc tính thận. Giảm liều ngay."
            color = "error"
        
        results.append({
            "type": "auc",
            "value": auc,
            "status": status,
            "level_text": level_text,
            "recommendation": recommendation,
            "color": color
        })
    
    return results


def render_vancomycin_tdm():
    """Render Vancomycin TDM Calculator Interface"""
    
    # Initialize calculator
    calc = TDMCalculator(
        drug_name="Vancomycin",
        drug_icon="💊",
        therapeutic_range="Trough: 10-20 mg/L (AUC: 400-600 mg·h/L)",
        target_min=10.0,
        target_max=20.0,
        toxic_threshold=25.0,
        unit="mg/L",
        sampling_time="Trough (pre-dose) hoặc AUC",
        half_life_hours=6.0
    )
    
    calc.render_header()
    
    calc.render_info_box("""
    **Phương pháp ưu tiên:** AUC-based dosing (400-600 mg·h/L)
    **Phương pháp thay thế:** Trough-based dosing (10-20 mg/L)
    **Thời điểm lấy mẫu:** Trough: trước liều tiếp theo (≥ 1 giờ sau khi truyền xong)
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs(["🧮 Tính Liều (AUC-based)", "🧮 Tính Liều (Trough-based)", "📊 Giải Thích Nồng Độ"])
    
    with tab1:
        st.markdown("### 📋 AUC-Based Dosing (Ưu tiên)")
        st.info("""
        **AUC-based dosing là phương pháp ưu tiên:**
        - Mục tiêu: AUC 400-600 mg·h/L
        - Giảm nguy cơ độc tính thận
        - Hiệu quả điều trị tốt hơn
        """)
        
        st.markdown("---")
        st.markdown("#### 📋 Thông số bệnh nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="vanc_auc_weight"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=5.0,
                max_value=150.0,
                value=60.0,
                step=5.0,
                format="%.1f",
                key="vanc_auc_crcl",
                help="Creatinine clearance"
            )
        
        with col2:
            target_auc = st.number_input(
                "Mục tiêu AUC (mg·h/L)",
                min_value=300.0,
                max_value=700.0,
                value=500.0,
                step=50.0,
                key="vanc_target_auc",
                help="Thường 400-600 mg·h/L"
            )
            
            has_current_levels = st.checkbox(
                "Có nồng độ hiện tại?",
                key="vanc_auc_has_levels"
            )
        
        if has_current_levels:
            st.markdown("---")
            st.markdown("#### 📊 Nồng Độ Hiện Tại")
            
            col1, col2 = st.columns(2)
            
            with col1:
                current_peak = st.number_input(
                    "Peak (mg/L)",
                    min_value=0.0,
                    max_value=50.0,
                    value=25.0,
                    step=0.5,
                    key="vanc_current_peak"
                )
            
            with col2:
                current_trough = st.number_input(
                    "Trough (mg/L)",
                    min_value=0.0,
                    max_value=30.0,
                    value=12.0,
                    step=0.5,
                    key="vanc_current_trough_auc"
                )
            
            # Calculate current AUC
            current_auc = calculate_vancomycin_auc(current_peak, current_trough)
            st.info(f"**AUC hiện tại:** {current_auc:.0f} mg·h/L")
            
            current_dose = st.number_input(
                "Liều hiện tại (mg)",
                min_value=250.0,
                max_value=2000.0,
                value=1000.0,
                step=250.0,
                key="vanc_current_dose_auc"
            )
        else:
            current_auc = None
            current_dose = None
        
        st.markdown("---")
        
        if st.button("🧮 Tính Liều Vancomycin (AUC-based)", type="primary", use_container_width=True):
            result = calculate_vancomycin_dose_auc_based(
                weight, crcl, target_auc, current_auc, current_dose
            )
            
            st.markdown("### 💊 Kết quả Tính Liều")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều đề xuất",
                    f"{result['dose_mg']:.0f} mg"
                )
            
            with col2:
                st.metric(
                    "Tần suất",
                    result['dosing_interval']
                )
            
            with col3:
                st.metric(
                    "Mục tiêu AUC",
                    f"{result['target_auc']:.0f} mg·h/L"
                )
            
            st.markdown("---")
            
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Liều:** {result['dose_mg']:.0f} mg **{result['dosing_interval']}**
            
            **Lưu ý:**
            - Mục tiêu AUC: {result['target_auc']:.0f} mg·h/L
            - Theo dõi nồng độ sau 3-5 liều (steady state)
            - Lấy cả peak và trough để tính AUC chính xác
            - CrCl {crcl:.0f} mL/min: Dùng liều điều chỉnh cho suy thận
            """)
    
    with tab2:
        st.markdown("### 📋 Trough-Based Dosing (Thay Thế)")
        st.warning("""
        **Lưu ý:** AUC-based dosing được ưu tiên hơn.
        Trough-based chỉ dùng khi không thể tính AUC.
        """)
        
        st.markdown("---")
        st.markdown("#### 📋 Thông số bệnh nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="vanc_trough_weight"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=5.0,
                max_value=150.0,
                value=60.0,
                step=5.0,
                format="%.1f",
                key="vanc_trough_crcl"
            )
        
        with col2:
            target_trough = st.number_input(
                "Mục tiêu Trough (mg/L)",
                min_value=10.0,
                max_value=20.0,
                value=15.0,
                step=1.0,
                key="vanc_target_trough",
                help="Thường 10-20 mg/L"
            )
            
            has_current_trough = st.checkbox(
                "Có trough hiện tại?",
                key="vanc_trough_has_level"
            )
        
        if has_current_trough:
            st.markdown("---")
            st.markdown("#### 📊 Nồng Độ Hiện Tại")
            
            current_trough = st.number_input(
                "Trough hiện tại (mg/L)",
                min_value=0.0,
                max_value=30.0,
                value=12.0,
                step=0.5,
                key="vanc_current_trough"
            )
            
            current_dose = st.number_input(
                "Liều hiện tại (mg)",
                min_value=250.0,
                max_value=2000.0,
                value=1000.0,
                step=250.0,
                key="vanc_current_dose_trough"
            )
        else:
            current_trough = None
            current_dose = None
        
        st.markdown("---")
        
        if st.button("🧮 Tính Liều Vancomycin (Trough-based)", type="primary", use_container_width=True):
            result = calculate_vancomycin_dose_trough_based(
                weight, crcl, target_trough, current_trough, current_dose
            )
            
            st.markdown("### 💊 Kết quả Tính Liều")
            
            if result.get('loading_dose_mg'):
                st.markdown("#### 🔴 Loading Dose:")
                st.info(f"**Loading dose:** {result['loading_dose_mg']:.0f} mg (một lần)")
                st.markdown("---")
            
            st.markdown("#### 📅 Maintenance Dose:")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều đề xuất",
                    f"{result['dose_mg']:.0f} mg"
                )
            
            with col2:
                st.metric(
                    "Tần suất",
                    result['dosing_interval']
                )
            
            with col3:
                st.metric(
                    "Mục tiêu Trough",
                    f"{result['target_trough']:.0f} mg/L"
                )
            
            st.markdown("---")
            
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Liều:** {result['dose_mg']:.0f} mg **{result['dosing_interval']}**
            
            **Lưu ý:**
            - Mục tiêu Trough: {result['target_trough']:.0f} mg/L
            - Theo dõi nồng độ sau 3-5 liều (steady state)
            - Lấy mẫu trước liều tiếp theo (trough)
            - CrCl {crcl:.0f} mL/min: Dùng liều điều chỉnh cho suy thận
            """)
    
    with tab3:
        st.markdown("### 📊 Giải Thích Nồng Độ Vancomycin")
        
        method = st.radio(
            "Phương pháp:",
            ["AUC (Ưu tiên)", "Trough"],
            key="vanc_interp_method"
        )
        
        st.markdown("---")
        
        if method == "AUC (Ưu tiên)":
            col1, col2 = st.columns(2)
            
            with col1:
                peak = st.number_input(
                    "Peak (mg/L)",
                    min_value=0.0,
                    max_value=50.0,
                    value=25.0,
                    step=0.5,
                    key="vanc_interp_peak"
                )
            
            with col2:
                trough = st.number_input(
                    "Trough (mg/L)",
                    min_value=0.0,
                    max_value=30.0,
                    value=12.0,
                    step=0.5,
                    key="vanc_interp_trough"
                )
            
            # Calculate AUC
            auc = calculate_vancomycin_auc(peak, trough)
            st.info(f"**AUC tính được:** {auc:.0f} mg·h/L")
        else:
            trough = st.number_input(
                "Trough (mg/L)",
                min_value=0.0,
                max_value=30.0,
                value=15.0,
                step=0.5,
                key="vanc_interp_trough_only"
            )
            peak = None
            auc = None
        
        st.markdown("---")
        
        if st.button("📊 Giải Thích Nồng Độ", type="primary", use_container_width=True):
            interpretations = interpret_vancomycin_level(
                trough_mg_l=trough if method == "Trough" else (trough if peak else None),
                peak_mg_l=peak if method == "AUC (Ưu tiên)" else None,
                auc=auc if method == "AUC (Ưu tiên)" else None
            )
            
            st.markdown("### 📈 Kết quả Giải Thích")
            
            for interp in interpretations:
                if interp['color'] == 'success':
                    st.success(f"**{interp['level_text']}**")
                elif interp['color'] == 'info':
                    st.info(f"**{interp['level_text']}**")
                elif interp['color'] == 'warning':
                    st.warning(f"**{interp['level_text']}**")
                else:
                    st.error(f"**{interp['level_text']}**")
                
                st.markdown(f"**💡 Khuyến nghị:** {interp['recommendation']}")
                st.markdown("---")
    
    # References
    calc.render_references("""
    - **ASHP/IDSA Vancomycin Guidelines 2020** - AUC-based dosing preferred
    - **Target AUC:** 400-600 mg·h/L for most infections
    - **Target Trough:** 10-20 mg/L (if AUC not available)
    - **Half-life:** ~6 hours (normal renal function), 7-9 days (ESRD)
    - **Protein binding:** ~50%
    - **Volume of distribution:** 0.4-1.0 L/kg
    """)

