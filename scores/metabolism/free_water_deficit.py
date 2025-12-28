"""
Free Water Deficit in Hypernatremia
Tính thiếu nước tự do trong tăng natri máu
"""

import streamlit as st
from scores.utils.validation import validate_range
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def calculate_free_water_deficit(weight_kg, current_na, target_na=140):
    """
    Calculate free water deficit in hypernatremia
    
    Formula: FWD (L) = Weight (kg) × 0.6 × [(Current Na - Target Na) / Target Na]
    Alternative: FWD (L) = Weight (kg) × 0.5 (female) or 0.6 (male) × [(Current Na - 140) / 140]
    
    Args:
        weight_kg: Current weight (kg)
        current_na: Current sodium (mmol/L)
        target_na: Target sodium (mmol/L), default 140
    
    Returns:
        Free water deficit in liters
    """
    # Using 0.6 as average TBW fraction (can be adjusted for gender/age)
    tbw_fraction = 0.6
    fwd_liters = weight_kg * tbw_fraction * ((current_na - target_na) / target_na)
    return max(fwd_liters, 0)  # Ensure non-negative


def calculate_correction_rate(fwd_liters, correction_speed="moderate"):
    """
    Calculate correction rate
    
    Args:
        fwd_liters: Free water deficit (L)
        correction_speed: "slow" (0.5 mmol/L/hour), "moderate" (0.7 mmol/L/hour), "fast" (1.0 mmol/L/hour)
    
    Returns:
        dict with correction time and hourly rate
    """
    # Safe correction rates (mmol/L per hour)
    rates = {
        "slow": 0.5,
        "moderate": 0.7,
        "fast": 1.0
    }
    
    rate = rates.get(correction_speed, 0.7)
    
    # Estimate time (simplified - actual depends on many factors)
    # Assuming 1L D5W decreases Na by ~2-3 mmol/L
    na_decrease_per_liter = 2.5
    estimated_hours = (fwd_liters * na_decrease_per_liter) / rate
    
    hourly_rate_ml = (fwd_liters * 1000) / estimated_hours if estimated_hours > 0 else 0
    
    return {
        "estimated_hours": estimated_hours,
        "hourly_rate_ml": hourly_rate_ml,
        "correction_speed": correction_speed,
        "rate_mmol_per_hour": rate
    }


def render():
    """Render Free Water Deficit calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💧 Free Water Deficit in Hypernatremia</h2>
    <p style='text-align: center;'><em>Tính thiếu nước tự do trong tăng natri máu</em></p>
    """, unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "free_water_deficit":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Free Water Deficit')}")
    
    with st.expander("ℹ️ Giới thiệu về Free Water Deficit"):
        st.markdown("""
        **Free Water Deficit (FWD)** là lượng nước tự do cần bù để điều chỉnh tăng natri máu.
        
        **Công thức:**
        ```
        FWD (L) = Weight (kg) × TBW fraction × [(Current Na - Target Na) / Target Na]
        ```
        
        **TBW (Total Body Water) fraction:**
        - Nam trẻ: 0.6
        - Nữ trẻ: 0.5
        - Người cao tuổi: 0.5-0.55
        
        **Mục tiêu điều chỉnh:**
        - **Tốc độ an toàn:** 0.5-0.7 mmol/L/giờ
        - **Tối đa:** 1.0 mmol/L/giờ (tránh phù não)
        - **Mục tiêu Na:** 140 mmol/L
        
        **Dung dịch điều chỉnh:**
        - D5W (Dextrose 5% in Water)
        - 0.45% NaCl (half-normal saline)
        - Nước uống (nếu bệnh nhân tỉnh)
        
        **Lưu ý:**
        - ⚠️ Điều chỉnh quá nhanh → phù não nguy hiểm
        - Theo dõi Na mỗi 2-4 giờ
        - Điều chỉnh nguyên nhân gây tăng natri máu
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f"
        )
    
    with col2:
        current_na = st.number_input(
            "Na hiện tại (mmol/L)",
            min_value=135.0,
            max_value=180.0,
            value=150.0,
            step=0.1,
            format="%.1f",
            help="Na đo được trong máu"
        )
    
    target_na = st.number_input(
        "Na mục tiêu (mmol/L)",
        min_value=135.0,
        max_value=145.0,
        value=140.0,
        step=0.1,
        format="%.1f",
        help="Na mục tiêu cần đạt"
    )
    
    tbw_fraction = st.slider(
        "TBW Fraction (Total Body Water)",
        min_value=0.40,
        max_value=0.70,
        value=0.60,
        step=0.05,
        help="0.6 cho nam trẻ, 0.5 cho nữ trẻ, 0.5-0.55 cho người cao tuổi"
    )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🧮 Tính Free Water Deficit", type="primary", use_container_width=True):
        if current_na <= target_na:
            st.error("⚠️ Na hiện tại phải lớn hơn Na mục tiêu (tăng natri máu)")
            st.stop()
        
        fwd_liters = weight_kg * tbw_fraction * ((current_na - target_na) / target_na)
        correction = calculate_correction_rate(fwd_liters, "moderate")
        
        st.subheader("📊 Kết quả")
        
        col1, col2 = st.columns(2)
        
        with col1:
            render_result_box(
                title="Free Water Deficit",
                value=f"{fwd_liters:.2f}",
                unit="L",
                status="🔴" if fwd_liters > 3 else "🟡" if fwd_liters > 1.5 else "🟢"
            )
        
        with col2:
            render_result_box(
                title="Free Water Deficit",
                value=f"{fwd_liters * 1000:.0f}",
                unit="mL",
                status="🔴" if fwd_liters > 3 else "🟡" if fwd_liters > 1.5 else "🟢"
            )
        
        # Formula
        with st.expander("📐 Công thức"):
            st.markdown(f"""
            **Công thức:**
            ```
            FWD (L) = Weight × TBW fraction × [(Current Na - Target Na) / Target Na]
            FWD (L) = {weight_kg} × {tbw_fraction} × [({current_na} - {target_na}) / {target_na}]
            FWD (L) = {weight_kg} × {tbw_fraction} × {((current_na - target_na) / target_na):.3f}
            FWD (L) = {fwd_liters:.2f} L
            ```
            """)
        
        # Correction plan
        st.subheader("💧 Kế hoạch điều chỉnh")
        
        st.info(f"""
        **Ước tính thời gian điều chỉnh:** {correction['estimated_hours']:.1f} giờ
        **Tốc độ điều chỉnh:** {correction['rate_mmol_per_hour']} mmol/L/giờ
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Tốc độ truyền ước tính", f"{correction['hourly_rate_ml']:.0f} mL/giờ")
        
        with col2:
            st.metric("Dung dịch khuyến nghị", "D5W hoặc 0.45% NaCl")
        
        # Recommendations
        st.subheader("💡 Khuyến cáo lâm sàng")
        st.markdown(f"""
        - ✅ **Bù nước tự do:** {fwd_liters:.2f} L ({fwd_liters * 1000:.0f} mL)
        - ✅ **Dung dịch:** D5W hoặc 0.45% NaCl
        - ✅ **Tốc độ an toàn:** 0.5-0.7 mmol/L/giờ (tối đa 1.0 mmol/L/giờ)
        - ⚠️ **Theo dõi Na mỗi 2-4 giờ** để tránh điều chỉnh quá nhanh
        - ⚠️ **Điều chỉnh nguyên nhân** gây tăng natri máu
        - ⚠️ **Tránh điều chỉnh quá nhanh** → nguy cơ phù não
        """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "free_water_deficit",
            "calculator_name": "Free Water Deficit in Hypernatremia",
            "inputs": {
                "Cân nặng": f"{weight_kg} kg",
                "Na hiện tại": f"{current_na} mmol/L",
                "Na mục tiêu": f"{target_na} mmol/L",
                "TBW fraction": f"{tbw_fraction}"
            },
            "results": {
                "Free Water Deficit": f"{fwd_liters:.2f} L ({fwd_liters * 1000:.0f} mL)",
                "Thời gian điều chỉnh ước tính": f"{correction['estimated_hours']:.1f} giờ"
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
        
        # Suggestions
        render_suggestions("free_water_deficit", fwd_liters)
    
    # History
    render_history_ui("free_water_deficit", "Free Water Deficit in Hypernatremia")
    
    # References
    references = get_references("free_water_deficit")
    if references:
        render_references_section(references)

