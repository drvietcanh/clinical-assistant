"""
Vial Selector UI Component
Select vials and calculate preparation details
"""

from typing import Dict, Optional

import streamlit as st
from drugs.vial_manager import (
    get_drug_vials,
    get_vial_labels,
    calculate_vials_needed,
    calculate_preparation,
    calculate_vials_from_dose
)
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert


def render_vial_selector(drug_name: str, total_dose_mg: float = None) -> Dict:
    """
    Render vial selection UI.
    
    Args:
        drug_name: Name of drug
        total_dose_mg: Optional total dose in mg. If None, shows input field.
    
    Returns:
        Dictionary with selection results
    """
    st.markdown("### 📦 Quản lý ống thuốc (Vial Management)")
    
    # Get available vials
    vials = get_drug_vials(drug_name)
    if not vials:
        st.warning(f"Không có thông tin ống cho thuốc '{drug_name}'")
        return None
    
    # Get total dose
    if total_dose_mg is None:
        total_dose_mg = st.number_input(
            "**Tổng liều cần (mg):**",
            min_value=0.01,
            max_value=10000.0,
            value=1.0,
            step=0.1,
            format="%.2f",
            key=f"vial_dose_{drug_name}"
        )
    
    if total_dose_mg <= 0:
        st.warning("Vui lòng nhập liều > 0")
        return None
    
    # Vial selection
    vial_labels = get_vial_labels(drug_name)
    if len(vial_labels) > 1:
        selected_vial = st.selectbox(
            "**Chọn loại ống:**",
            vial_labels,
            key=f"vial_select_{drug_name}",
            help="Chọn loại ống có sẵn"
        )
    else:
        selected_vial = vial_labels[0] if vial_labels else None
        if selected_vial:
            st.info(f"Loại ống: {selected_vial}")
    
    # Calculate button
    if st.button("📊 Tính số lượng ống", key=f"vial_calc_{drug_name}", type="primary"):
        try:
            # Calculate vials needed
            result = calculate_vials_needed(drug_name, total_dose_mg, selected_vial)
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            # Display results
            metrics = [
                {
                    "label": "Số ống cần",
                    "value": f"{result['vials_needed']} ống",
                    "icon": "📦"
                },
                {
                    "label": "Tổng có",
                    "value": f"{result['total_available_mg']:.2f} mg",
                    "icon": "💊"
                },
                {
                    "label": "Cần dùng",
                    "value": f"{total_dose_mg:.2f} mg",
                    "icon": "💉"
                }
            ]
            
            render_result_card("Tính số lượng ống", metrics, color="primary")
            
            # Waste information
            if result['waste_mg'] > 0:
                st.markdown("---")
                waste_percent = result['waste_percent']
                
                if waste_percent > 20:
                    render_warning_alert(
                        f"Lượng thuốc thừa: {result['waste_mg']:.2f} mg ({waste_percent:.1f}%)",
                        title="⚠️ Cảnh báo: Lượng thừa lớn"
                    )
                else:
                    render_info_alert(
                        f"Lượng thuốc thừa: {result['waste_mg']:.2f} mg ({waste_percent:.1f}%)",
                        title="ℹ️ Thông tin"
                    )
            
            return result
            
        except ValueError as e:
            st.error(f"Lỗi: {str(e)}")
            return None
    
    return None


def render_preparation_calculator(
    drug_name: str,
    total_dose_mg: float,
    selected_vial: Optional[str] = None
):
    """Render preparation calculator."""
    
    st.markdown("### 🧪 Tính toán cách pha")
    
    # Final volume input
    final_volume_ml = st.number_input(
        "**Thể tích pha cuối (ml):**",
        min_value=1.0,
        max_value=1000.0,
        value=50.0,
        step=1.0,
        format="%.0f",
        key=f"prep_vol_{drug_name}",
        help="Thể tích cuối cùng sau khi pha (ví dụ: 50ml cho bơm, 500ml cho chai)"
    )
    
    if st.button("🧮 Tính cách pha", key=f"prep_calc_{drug_name}", type="primary"):
        try:
            result = calculate_preparation(
                drug_name, total_dose_mg, selected_vial, final_volume_ml
            )
            
            st.markdown("---")
            st.markdown("### 🧪 Hướng dẫn pha")
            
            # Display preparation instructions
            st.markdown("**Cách pha:**")
            st.info(result['preparation_instructions'])
            
            # Concentration info
            st.markdown("---")
            st.markdown("### 📊 Thông tin nồng độ")
            
            metrics = [
                {
                    "label": "Nồng độ",
                    "value": f"{result['final_concentration_mcg_ml']:.2f} mcg/ml",
                    "icon": "💧"
                },
                {
                    "label": "Nồng độ",
                    "value": f"{result['final_concentration_mg_ml']:.4f} mg/ml",
                    "icon": "💊"
                },
                {
                    "label": "Số ống",
                    "value": f"{result['vials_needed']} ống",
                    "icon": "📦"
                }
            ]
            
            render_result_card("Nồng độ pha", metrics, color="info")
            
        except ValueError as e:
            st.error(f"Lỗi: {str(e)}")


def render_vial_management_full(drug_name: str):
    """Render full vial management interface."""
    
    st.markdown("## 📦 Vial Management System")
    st.markdown(f"**Thuốc:** {drug_name}")
    st.markdown("---")
    
    # Tab 1: Calculate vials from dose
    tab1, tab2 = st.tabs([
        "📊 Tính từ liều dùng",
        "💧 Tính cách pha"
    ])
    
    with tab1:
        st.markdown("### 📊 Tính số lượng ống từ liều dùng")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            dose_mcg_kg_min = st.number_input(
                "**Liều (µg/kg/phút):**",
                min_value=0.01,
                max_value=100.0,
                value=0.1,
                step=0.01,
                format="%.2f",
                key=f"vial_mgmt_dose_{drug_name}"
            )
        
        with col2:
            weight_kg = st.number_input(
                "**Cân nặng (kg):**",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                format="%.1f",
                key=f"vial_mgmt_weight_{drug_name}"
            )
        
        with col3:
            duration_hours = st.number_input(
                "**Thời gian (giờ):**",
                min_value=0.1,
                max_value=168.0,
                value=24.0,
                step=0.1,
                format="%.1f",
                key=f"vial_mgmt_duration_{drug_name}"
            )
        
        if st.button("📊 Tính số ống", key=f"vial_mgmt_calc_{drug_name}", type="primary"):
            try:
                result = calculate_vials_from_dose(
                    drug_name, dose_mcg_kg_min, weight_kg, duration_hours
                )
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                metrics = [
                    {
                        "label": "Tổng liều cần",
                        "value": f"{result['total_dose_mg']:.2f} mg",
                        "icon": "💉"
                    },
                    {
                        "label": "Số ống cần",
                        "value": f"{result['vials_needed']} ống",
                        "icon": "📦"
                    },
                    {
                        "label": "Tổng có",
                        "value": f"{result['total_available_mg']:.2f} mg",
                        "icon": "💊"
                    }
                ]
                
                render_result_card("Kết quả", metrics, color="primary")
                
                # Waste info
                if result['waste_mg'] > 0:
                    st.markdown("---")
                    if result['waste_percent'] > 20:
                        render_warning_alert(
                            f"Lượng thừa: {result['waste_mg']:.2f} mg ({result['waste_percent']:.1f}%)",
                            title="⚠️ Cảnh báo"
                        )
                    else:
                        render_info_alert(
                            f"Lượng thừa: {result['waste_mg']:.2f} mg ({result['waste_percent']:.1f}%)",
                            title="ℹ️ Thông tin"
                        )
                
                # Store result for tab 2
                st.session_state[f'vial_result_{drug_name}'] = result
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    with tab2:
        # Get stored result or calculate from input
        if f'vial_result_{drug_name}' in st.session_state:
            result = st.session_state[f'vial_result_{drug_name}']
            total_dose_mg = result['total_dose_mg']
            selected_vial = result.get('selected_vial')
        else:
            total_dose_mg = st.number_input(
                "**Tổng liều (mg):**",
                min_value=0.01,
                max_value=10000.0,
                value=1.0,
                step=0.1,
                format="%.2f",
                key=f"prep_dose_{drug_name}"
            )
            selected_vial = None
        
        render_preparation_calculator(drug_name, total_dose_mg, selected_vial)

