"""
Maintenance Fluids Calculator
Tính nhu cầu dịch duy trì hàng ngày
"""

import streamlit as st
from scores.utils.validation import validate_range, validate_age
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def calculate_maintenance_fluids(weight_kg, method="Holliday-Segar"):
    """
    Calculate maintenance fluid requirements
    
    Methods:
    - Holliday-Segar (4-2-1 rule): Most common
    - Body Surface Area: Alternative method
    
    Args:
        weight_kg: Weight in kg
        method: Calculation method
    
    Returns:
        dict with hourly and daily fluid requirements
    """
    if method == "Holliday-Segar":
        # 4-2-1 rule
        if weight_kg <= 10:
            hourly_ml = weight_kg * 4
        elif weight_kg <= 20:
            hourly_ml = 40 + (weight_kg - 10) * 2
        else:
            hourly_ml = 60 + (weight_kg - 20) * 1
        
        daily_ml = hourly_ml * 24
        daily_l = daily_ml / 1000
    
    elif method == "Body Surface Area":
        # 1500-2000 mL/m²/day
        # Approximate BSA = sqrt((height_cm × weight_kg) / 3600)
        # Using average: 1500 mL/m²/day
        # For average adult (BSA ~1.7 m²): ~2500 mL/day
        # Simplified: ~30-35 mL/kg/day
        daily_ml = weight_kg * 32.5  # Average of 30-35
        hourly_ml = daily_ml / 24
        daily_l = daily_ml / 1000
    
    return {
        "hourly_ml": hourly_ml,
        "daily_ml": daily_ml,
        "daily_l": daily_l,
        "method": method
    }


def render():
    """Render Maintenance Fluids calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💧 Maintenance Fluids Calculator</h2>
    <p style='text-align: center;'><em>Tính nhu cầu dịch duy trì hàng ngày</em></p>
    """, unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "maintenance_fluids":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Maintenance Fluids')}")
    
    with st.expander("ℹ️ Giới thiệu về Maintenance Fluids"):
        st.markdown("""
        **Maintenance Fluids** là lượng dịch cần thiết để duy trì cân bằng nước hàng ngày.
        
        **Công thức Holliday-Segar (4-2-1 rule):**
        - **0-10 kg:** 4 mL/kg/giờ
        - **11-20 kg:** 40 mL/giờ + 2 mL/kg cho mỗi kg > 10 kg
        - **> 20 kg:** 60 mL/giờ + 1 mL/kg cho mỗi kg > 20 kg
        
        **Ví dụ:**
        - 5 kg: 5 × 4 = 20 mL/giờ = 480 mL/ngày
        - 15 kg: 40 + (15-10)×2 = 50 mL/giờ = 1200 mL/ngày
        - 70 kg: 60 + (70-20)×1 = 110 mL/giờ = 2640 mL/ngày
        
        **Lưu ý:**
        - Đây là nhu cầu cơ bản, cần điều chỉnh theo:
          - Mất dịch bất thường (sốt, tiêu chảy, nôn)
          - Suy tim, suy thận
          - Tình trạng phù, cổ trướng
        - Thường dùng dung dịch đẳng trương (NaCl 0.9% hoặc Ringer lactate)
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    weight_kg = st.number_input(
        "Cân nặng (kg)",
        min_value=1.0,
        max_value=300.0,
        value=70.0,
        step=0.1,
        format="%.1f",
        help="Cân nặng bệnh nhân"
    )
    
    method = st.radio(
        "Phương pháp tính",
        options=["Holliday-Segar", "Body Surface Area"],
        index=0,
        help="Holliday-Segar (4-2-1) là phương pháp phổ biến nhất"
    )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🧮 Tính nhu cầu dịch", type="primary", use_container_width=True):
        result = calculate_maintenance_fluids(weight_kg, method)
        
        st.subheader("📊 Kết quả")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            render_result_box(
                title="Nhu cầu dịch/giờ",
                value=f"{result['hourly_ml']:.0f}",
                unit="mL/giờ",
                status="🟢"
            )
        
        with col2:
            render_result_box(
                title="Nhu cầu dịch/ngày",
                value=f"{result['daily_ml']:.0f}",
                unit="mL/ngày",
                status="🟢"
            )
        
        with col3:
            render_result_box(
                title="Nhu cầu dịch/ngày",
                value=f"{result['daily_l']:.2f}",
                unit="L/ngày",
                status="🟢"
            )
        
        # Formula explanation
        with st.expander("📐 Công thức tính"):
            if method == "Holliday-Segar":
                if weight_kg <= 10:
                    formula_text = f"""
                    **Công thức (4-2-1 rule):**
                    ```
                    Nhu cầu/giờ = Cân nặng × 4
                    Nhu cầu/giờ = {weight_kg} × 4 = {result['hourly_ml']:.0f} mL/giờ
                    Nhu cầu/ngày = {result['hourly_ml']:.0f} × 24 = {result['daily_ml']:.0f} mL/ngày
                    ```
                    """
                elif weight_kg <= 20:
                    formula_text = f"""
                    **Công thức (4-2-1 rule):**
                    ```
                    Nhu cầu/giờ = 40 + (Cân nặng - 10) × 2
                    Nhu cầu/giờ = 40 + ({weight_kg} - 10) × 2 = {result['hourly_ml']:.0f} mL/giờ
                    Nhu cầu/ngày = {result['hourly_ml']:.0f} × 24 = {result['daily_ml']:.0f} mL/ngày
                    ```
                    """
                else:
                    formula_text = f"""
                    **Công thức (4-2-1 rule):**
                    ```
                    Nhu cầu/giờ = 60 + (Cân nặng - 20) × 1
                    Nhu cầu/giờ = 60 + ({weight_kg} - 20) × 1 = {result['hourly_ml']:.0f} mL/giờ
                    Nhu cầu/ngày = {result['hourly_ml']:.0f} × 24 = {result['daily_ml']:.0f} mL/ngày
                    ```
                    """
            else:
                formula_text = f"""
                **Công thức (Body Surface Area):**
                ```
                Nhu cầu/ngày ≈ Cân nặng × 32.5 mL/kg/ngày
                Nhu cầu/ngày = {weight_kg} × 32.5 = {result['daily_ml']:.0f} mL/ngày
                Nhu cầu/giờ = {result['daily_ml']:.0f} / 24 = {result['hourly_ml']:.0f} mL/giờ
                ```
                """
            st.markdown(formula_text)
        
        # Recommendations
        st.subheader("💡 Khuyến cáo lâm sàng")
        st.markdown("""
        - ✅ **Dung dịch thường dùng:** NaCl 0.9% hoặc Ringer lactate
        - ✅ **Điều chỉnh theo:**
          - Sốt: +10-15% cho mỗi 1°C > 37°C
          - Tiêu chảy, nôn: Bù thêm dịch mất
          - Suy tim, suy thận: Giảm lượng dịch
        - ⚠️ **Theo dõi:** Cân nặng, dấu hiệu phù, điện giải
        """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "maintenance_fluids",
            "calculator_name": "Maintenance Fluids Calculator",
            "inputs": {
                "Cân nặng": f"{weight_kg} kg",
                "Phương pháp": method
            },
            "results": {
                "Nhu cầu/giờ": f"{result['hourly_ml']:.0f} mL/giờ",
                "Nhu cầu/ngày": f"{result['daily_ml']:.0f} mL/ngày ({result['daily_l']:.2f} L/ngày)"
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
        
        # Suggestions
        render_suggestions("maintenance_fluids", result['daily_ml'])
    
    # History
    render_history_ui("maintenance_fluids", "Maintenance Fluids Calculator")
    
    # References
    references = get_references("maintenance_fluids")
    if references:
        render_references_section(references)

