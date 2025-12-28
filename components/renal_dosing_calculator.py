"""
Renal Dose Adjustment Calculator UI Component
Adjust drug doses based on renal function
"""

import streamlit as st
from drugs.renal_dosing import (
    calculate_renal_adjusted_dose,
    validate_renal_dose,
    get_egfr_category,
    get_egfr_category_info,
    get_renal_adjustment_info
)
from drugs.cardiovascular_calculator import get_drug_names, get_drug_info
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


def render_renal_dosing_calculator():
    """Render renal dose adjustment calculator interface."""
    
    st.markdown("## 🫘 Renal Dose Adjustment Calculator")
    st.markdown("""
    Điều chỉnh liều thuốc tim mạch dựa trên chức năng thận (eGFR/CrCl).
    
    **Lưu ý:**
    - Một số thuốc không cần điều chỉnh (chuyển hóa ở gan)
    - Một số thuốc cần giảm liều khi suy thận
    - Bệnh nhân lọc máu cần điều chỉnh đặc biệt
    """)
    
    st.markdown("---")
    
    # Get available drugs
    drug_names = get_drug_names()
    
    # Patient information
    st.markdown("### 👤 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        egfr = st.number_input(
            "**eGFR (ml/min/1.73m²):**",
            min_value=0.0,
            max_value=200.0,
            value=90.0,
            step=1.0,
            format="%.1f",
            key="renal_egfr",
            help="eGFR (estimated Glomerular Filtration Rate)"
        )
    
    with col2:
        on_dialysis = st.checkbox(
            "**Đang lọc máu (Dialysis)**",
            value=False,
            key="renal_dialysis",
            help="Bệnh nhân đang lọc máu"
        )
    
    # Display eGFR category
    egfr_category = get_egfr_category(egfr, on_dialysis)
    category_info = get_egfr_category_info(egfr_category)
    
    if category_info:
        color = "success" if egfr_category == "normal" else ("warning" if egfr_category in ["mild", "moderate"] else "error")
        render_result_box(
            "Phân loại chức năng thận",
            f"{category_info.get('description', egfr_category)} ({category_info.get('range', '')})",
            color=color,
            icon="🫘"
        )
    
    st.markdown("---")
    
    # Drug selection
    st.markdown("### 💊 Chọn thuốc và liều")
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_drug = st.selectbox(
            "**Thuốc:**",
            drug_names,
            key="renal_drug"
        )
    
    with col2:
        original_dose = st.number_input(
            "**Liều ban đầu (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=0.1,
            step=0.01,
            format="%.2f",
            key="renal_original_dose"
        )
    
    # Check if adjustment needed
    adjustment_info = get_renal_adjustment_info(selected_drug)
    
    if adjustment_info:
        if not adjustment_info.get("adjustment_needed", False):
            st.info(f"✅ {selected_drug}: {adjustment_info.get('notes', 'Không cần điều chỉnh liều khi suy thận')}")
        else:
            st.warning(f"⚠️ {selected_drug}: Cần điều chỉnh liều khi suy thận")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính liều điều chỉnh", key="renal_calculate", type="primary", use_container_width=True):
        try:
            # Calculate adjusted dose
            result = calculate_renal_adjusted_dose(
                selected_drug,
                original_dose,
                egfr,
                on_dialysis
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả điều chỉnh liều")
            
            # Display results
            if result["adjustment_needed"]:
                metrics = [
                    {
                        "label": "Liều ban đầu",
                        "value": f"{result['original_dose']:.2f} µg/kg/phút",
                        "icon": "💊"
                    },
                    {
                        "label": "Liều điều chỉnh",
                        "value": f"{result['adjusted_dose']:.3f} µg/kg/phút",
                        "icon": "💉"
                    },
                    {
                        "label": "Giảm liều",
                        "value": f"{result['reduction_percent']:.1f}%",
                        "icon": "📉"
                    }
                ]
                
                render_result_card("Điều chỉnh liều", metrics, color="warning")
                
                # Warning
                if result.get("warning"):
                    render_warning_alert(result["warning"], title="⚠️ Cảnh báo")
                
                # Notes
                if result.get("notes"):
                    st.markdown("---")
                    render_info_alert(result["notes"], title="ℹ️ Thông tin")
            else:
                metrics = [
                    {
                        "label": "Liều",
                        "value": f"{result['original_dose']:.2f} µg/kg/phút",
                        "icon": "💊"
                    },
                    {
                        "label": "Điều chỉnh",
                        "value": "Không cần",
                        "icon": "✅"
                    }
                ]
                
                render_result_card("Kết quả", metrics, color="success")
                
                # Notes
                if result.get("notes"):
                    st.markdown("---")
                    render_info_alert(result["notes"], title="ℹ️ Thông tin")
            
            # Validation
            st.markdown("---")
            validation = validate_renal_dose(selected_drug, original_dose, egfr, on_dialysis)
            
            if not validation["is_valid"]:
                render_error_alert(validation["error"], title="❌ Lỗi")
                st.markdown(f"**Liều khuyến nghị:** {validation['recommended_dose']:.3f} µg/kg/phút")
            
            # Drug info
            drug_info = get_drug_info(selected_drug)
            if drug_info and adjustment_info:
                st.markdown("---")
                st.markdown("### 💡 Thông tin thuốc")
                
                if adjustment_info.get("reason"):
                    st.markdown(f"**Lý do:** {adjustment_info.get('reason')}")
                
                if adjustment_info.get("adjustment"):
                    with st.expander("📋 Chi tiết điều chỉnh liều"):
                        for key, rule in adjustment_info.get("adjustment", {}).items():
                            st.markdown(f"**{key.replace('_', ' ').title()}:**")
                            st.markdown(f"  - {rule.get('notes', '')}")
                            st.markdown(f"  - Hệ số: {rule.get('multiplier', 1.0)}")
            
        except ValueError as e:
            st.error(f"Lỗi: {str(e)}")
        except Exception as e:
            st.error(f"Lỗi không xác định: {str(e)}")
    
    # Reference
    with st.expander("📋 Bảng tham khảo eGFR"):
        import pandas as pd
        
        categories_data = []
        for cat in ["normal", "mild", "moderate", "severe", "kidney_failure", "dialysis"]:
            info = get_egfr_category_info(cat)
            if info:
                categories_data.append({
                    "Phân loại": info.get("description", cat),
                    "eGFR": info.get("range", ""),
                    "Điều chỉnh": info.get("adjustment", "")
                })
        
        if categories_data:
            df = pd.DataFrame(categories_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Drug adjustment reference
    with st.expander("📋 Thuốc cần điều chỉnh liều"):
        drugs_need_adjustment = []
        drugs_no_adjustment = []
        
        for drug in drug_names:
            info = get_renal_adjustment_info(drug)
            if info:
                if info.get("adjustment_needed", False):
                    drugs_need_adjustment.append(drug)
                else:
                    drugs_no_adjustment.append(drug)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Cần điều chỉnh:**")
            for drug in drugs_need_adjustment:
                st.markdown(f"  - {drug}")
        
        with col2:
            st.markdown("**Không cần điều chỉnh:**")
            for drug in drugs_no_adjustment:
                st.markdown(f"  - {drug}")

