"""
Cardiovascular Drugs Calculator UI Component
Streamlit component for calculating vasopressor/inotrope infusions
"""

import streamlit as st
from drugs.cardiovascular_calculator import (
    get_drug_names,
    get_drug_info,
    calculate_complete_infusion,
    validate_dose_range
)
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert

# Import vial management
try:
    from components.vial_selector import render_vial_selector, render_preparation_calculator
    VIAL_MANAGEMENT_AVAILABLE = True
except ImportError:
    VIAL_MANAGEMENT_AVAILABLE = False


def render_cardiovascular_calculator():
    """Render cardiovascular drugs calculator interface."""
    
    # Mode selection
    mode = st.radio(
        "**Chế độ:**",
        ["Người lớn", "Trẻ em (Pediatric)", "Điều chỉnh liều (Renal)", "📋 Quick Reference"],
        horizontal=True,
        key="cv_mode_selector"
    )
    
    if mode == "Trẻ em (Pediatric)":
        try:
            from components.pediatric_dosing_calculator import render_pediatric_dosing_calculator
            render_pediatric_dosing_calculator()
            return
        except ImportError:
            st.warning("Pediatric calculator chưa sẵn sàng. Sử dụng chế độ người lớn.")
    
    if mode == "Điều chỉnh liều (Renal)":
        try:
            from components.renal_dosing_calculator import render_renal_dosing_calculator
            render_renal_dosing_calculator()
            return
        except ImportError:
            st.warning("Renal dosing calculator chưa sẵn sàng. Sử dụng chế độ người lớn.")
    
    if mode == "📋 Quick Reference":
        try:
            from components.quick_reference import render_quick_reference
            render_quick_reference()
            return
        except ImportError:
            st.warning("Quick Reference chưa sẵn sàng. Sử dụng chế độ người lớn.")
    
    st.markdown("## 💉 Tính liều thuốc tim mạch cấp cứu")
    st.markdown("""
    Tính toán liều dùng, tốc độ truyền, giọt/phút và thời gian truyền cho các thuốc tim mạch cấp cứu.
    
    **Dựa trên:** Surviving Sepsis Campaign 2021, ACCM Guidelines
    """)
    
    st.markdown("---")
    
    # Get available drugs
    drug_names = get_drug_names()
    if not drug_names:
        st.error("Không tìm thấy database thuốc tim mạch. Vui lòng kiểm tra file cardiovascular_drugs.json")
        return
    
    # Drug selection
    col1, col2 = st.columns(2)
    
    with col1:
        selected_drug = st.selectbox(
            "**Chọn thuốc:**",
            drug_names,
            key="cv_drug_select",
            help="Chọn thuốc tim mạch cần tính liều"
        )
    
    # Get drug info
    drug_info = get_drug_info(selected_drug)
    if not drug_info:
        st.error(f"Không tìm thấy thông tin thuốc: {selected_drug}")
        return
    
    # Display drug info
    with col2:
        st.markdown(f"**Nhóm:** {drug_info.get('group', 'N/A')}")
        if drug_info.get('name_vn'):
            st.markdown(f"**Tên khác:** {drug_info.get('name_vn')}")
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📊 Nhập thông tin")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="cv_weight"
        )
    
    with col2:
        dose_mcg_kg_min = st.number_input(
            "**Liều (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=0.1,
            step=0.01,
            format="%.2f",
            key="cv_dose",
            help=f"Liều khuyến nghị: {drug_info.get('dose_range', 'N/A')}"
        )
    
    with col3:
        infusion_method = st.radio(
            "**Phương pháp truyền:**",
            ["syringe_pump_50ml", "iv_bag_500ml"],
            format_func=lambda x: "Bơm tiêm điện (50ml)" if x == "syringe_pump_50ml" else "Chai truyền (500ml)",
            key="cv_method"
        )
    
    # Drop factor (only for IV bag)
    drop_factor = None
    if infusion_method == "iv_bag_500ml":
        st.markdown("---")
        drop_factor = st.selectbox(
            "**Drop factor (gtt/ml):**",
            [10, 15, 20, 60],
            index=2,  # Default 20
            key="cv_drop_factor",
            help="10-15: Macro drip, 20: Standard, 60: Micro drip"
        )
    
    st.markdown("---")
    
    # Validate dose
    validation = validate_dose_range(selected_drug, dose_mcg_kg_min)
    if not validation["is_valid"]:
        render_warning_alert(validation["warning"], title="Cảnh báo liều dùng")
    
    # Calculate button
    if st.button("🧮 Tính toán", key="cv_calculate", type="primary", use_container_width=True):
        try:
            # Calculate infusion
            results = calculate_complete_infusion(
                selected_drug,
                dose_mcg_kg_min,
                weight_kg,
                infusion_method,
                drop_factor
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả tính toán")
            
            # Main results
            metrics = [
                {
                    "label": "Tổng liều/phút",
                    "value": f"{results['total_dose_mcg_min']:.2f} µg/min",
                    "icon": "⏱️"
                },
                {
                    "label": "Tổng liều/giờ",
                    "value": f"{results['total_dose_mcg_hour']:.2f} µg/h",
                    "icon": "💉"
                },
                {
                    "label": "Tốc độ truyền",
                    "value": f"{results['infusion_rate_ml_hour']:.2f} ml/h",
                    "icon": "💧"
                }
            ]
            
            # Add drop rate if applicable
            if results.get('drop_rate_gtt_min'):
                metrics.append({
                    "label": "Giọt/phút",
                    "value": f"{results['drop_rate_gtt_min']:.1f} gtt/min",
                    "icon": "💧"
                })
            
            render_result_card("Kết quả tính toán", metrics, color="primary")
            
            # Infusion time
            st.markdown("---")
            st.markdown("### ⏰ Thời gian truyền")
            col1, col2 = st.columns(2)
            
            with col1:
                render_result_box(
                    "Thời gian",
                    results['time_formatted'],
                    color="info",
                    icon="⏱️"
                )
            
            with col2:
                render_result_box(
                    "Thể tích",
                    f"{results['volume_ml']} ml",
                    color="info"
                )
            
            # Preparation instructions
            st.markdown("---")
            st.markdown("### 📋 Hướng dẫn pha thuốc")
            render_info_alert(
                results.get('preparation_instructions', 'Không có hướng dẫn'),
                title="Cách pha"
            )
            
            # Drug information
            st.markdown("---")
            st.markdown("### 💊 Thông tin thuốc")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Chỉ định:**")
                st.info(drug_info.get('indication', 'N/A'))
                
                st.markdown("**Theo dõi:**")
                monitoring = drug_info.get('monitoring', '')
                if monitoring:
                    for item in monitoring.split(', '):
                        st.markdown(f"- ✅ {item}")
            
            with col2:
                st.markdown("**Liều khuyến nghị:**")
                st.markdown(f"- **Khởi đầu:** {drug_info.get('initial_dose', 'N/A')}")
                st.markdown(f"- **Thông thường:** {drug_info.get('dose_range', 'N/A')}")
                st.markdown(f"- **Tối đa:** {drug_info.get('max_dose', 'N/A')}")
                
                if drug_info.get('side_effects'):
                    st.markdown("**Tác dụng phụ:**")
                    st.warning(drug_info.get('side_effects'))
            
            # Notes
            if drug_info.get('notes'):
                st.markdown("---")
                st.markdown("### 💡 Lưu ý")
                render_info_alert(drug_info.get('notes'), title="Thông tin quan trọng")
            
            # Vial Management (if available)
            if VIAL_MANAGEMENT_AVAILABLE:
                st.markdown("---")
                st.markdown("### 📦 Quản lý ống thuốc")
                
                # Calculate total dose needed for 24 hours
                total_dose_mcg = results['total_dose_mcg_hour'] * 24
                total_dose_mg = total_dose_mcg / 1000
                
                # Render vial selector
                vial_result = render_vial_selector(selected_drug, total_dose_mg)
                
                # Preparation calculator
                if vial_result:
                    st.markdown("---")
                    render_preparation_calculator(
                        selected_drug,
                        vial_result['total_available_mg'],
                        vial_result.get('selected_vial')
                    )
            
        except ValueError as e:
            st.error(f"Lỗi tính toán: {str(e)}")
        except Exception as e:
            st.error(f"Lỗi không xác định: {str(e)}")
            st.exception(e)
    
    # Quick reference
    with st.expander("📋 Thông tin nhanh về thuốc"):
        st.markdown(f"**{selected_drug}** ({drug_info.get('name_vn', '')})")
        st.markdown(f"- **Nhóm:** {drug_info.get('group', 'N/A')}")
        st.markdown(f"- **Liều khởi đầu:** {drug_info.get('initial_dose', 'N/A')}")
        st.markdown(f"- **Liều thông thường:** {drug_info.get('dose_range', 'N/A')}")
        st.markdown(f"- **Liều tối đa:** {drug_info.get('max_dose', 'N/A')}")
        st.markdown(f"- **Chỉ định:** {drug_info.get('indication', 'N/A')}")
    
    # Disclaimer
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Kết quả tính toán chỉ mục đích tham khảo
    - Luôn điều chỉnh liều theo đáp ứng lâm sàng của bệnh nhân
    - Theo dõi sát các dấu hiệu sống và tác dụng phụ
    - Tuân thủ hướng dẫn của Bộ Y tế, Bệnh viện
    - Dùng đường truyền tĩnh mạch trung tâm khi có thể
    - Kiểm tra lại tính toán trước khi sử dụng
    """)

