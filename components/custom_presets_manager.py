"""
Custom Drug Presets Manager UI Component
Create and manage custom drug presets
"""

import streamlit as st
from drugs.custom_presets import (
    get_custom_presets,
    add_custom_preset,
    delete_custom_preset,
    get_custom_preset,
    export_presets,
    import_presets
)
from drugs.cardiovascular_calculator import get_drug_names
from components.ui.results import render_result_box
from components.ui.alerts import render_info_alert


def render_custom_presets_manager():
    """Render custom presets manager interface."""
    
    st.markdown("## ⚙️ Custom Drug Presets Manager")
    st.markdown("""
    Tạo và quản lý preset thuốc tùy chỉnh.
    
    **Tính năng:**
    - Tạo preset mới
    - Lưu preset thường dùng
    - Sử dụng preset trong calculator
    - Import/Export preset
    """)
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "➕ Tạo preset mới",
        "📋 Quản lý preset",
        "📥 Import/Export"
    ])
    
    # Tab 1: Create new preset
    with tab1:
        st.markdown("### ➕ Tạo preset mới")
        
        preset_name = st.text_input(
            "**Tên preset:**",
            value="",
            key="preset_name",
            placeholder="Ví dụ: Noradrenaline 70kg 0.1",
            help="Tên để dễ nhớ, ví dụ: 'Noradrenaline 70kg 0.1'"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            selected_drug = st.selectbox(
                "**Thuốc:**",
                get_drug_names(),
                key="preset_drug"
            )
        
        with col2:
            weight_kg = st.number_input(
                "**Cân nặng (kg):**",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                format="%.1f",
                key="preset_weight"
            )
        
        col3, col4 = st.columns(2)
        
        with col3:
            dose_mcg_kg_min = st.number_input(
                "**Liều (µg/kg/phút):**",
                min_value=0.01,
                max_value=100.0,
                value=0.1,
                step=0.01,
                format="%.2f",
                key="preset_dose"
            )
        
        with col4:
            infusion_method = st.radio(
                "**Phương pháp:**",
                ["syringe_pump_50ml", "iv_bag_500ml"],
                format_func=lambda x: "Bơm 50ml" if x == "syringe_pump_50ml" else "Chai 500ml",
                key="preset_method"
            )
        
        drop_factor = None
        if infusion_method == "iv_bag_500ml":
            drop_factor = st.selectbox(
                "**Drop factor:**",
                [10, 15, 20, 60],
                index=2,
                key="preset_drop_factor"
            )
        
        notes = st.text_area(
            "**Ghi chú (tùy chọn):**",
            value="",
            key="preset_notes",
            placeholder="Ví dụ: Dùng cho bệnh nhân sốc nhiễm khuẩn"
        )
        
        if st.button("💾 Lưu preset", key="preset_save", type="primary"):
            if not preset_name:
                st.error("Vui lòng nhập tên preset")
            else:
                try:
                    success = add_custom_preset(
                        preset_name,
                        selected_drug,
                        dose_mcg_kg_min,
                        weight_kg,
                        infusion_method,
                        drop_factor,
                        notes if notes else None
                    )
                    if success:
                        st.success(f"Đã lưu preset '{preset_name}'!")
                        st.rerun()
                except Exception as e:
                    st.error(f"Lỗi: {str(e)}")
    
    # Tab 2: Manage presets
    with tab2:
        st.markdown("### 📋 Quản lý preset")
        
        presets = get_custom_presets()
        
        if not presets:
            st.info("Chưa có preset nào. Hãy tạo preset mới ở tab 'Tạo preset mới'.")
        else:
            st.markdown(f"**Tổng số preset:** {len(presets)}")
            st.markdown("---")
            
            for preset_name, preset_data in presets.items():
                with st.expander(f"💊 {preset_name}", expanded=False):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"**Thuốc:** {preset_data.get('drug_name', 'N/A')}")
                        st.markdown(f"**Liều:** {preset_data.get('dose_mcg_kg_min', 0):.2f} µg/kg/phút")
                        st.markdown(f"**Cân nặng:** {preset_data.get('weight_kg', 0):.1f} kg")
                        st.markdown(f"**Phương pháp:** {preset_data.get('infusion_method', 'N/A')}")
                        if preset_data.get('drop_factor'):
                            st.markdown(f"**Drop factor:** {preset_data.get('drop_factor')} gtt/ml")
                        if preset_data.get('notes'):
                            st.markdown(f"**Ghi chú:** {preset_data.get('notes')}")
                    
                    with col2:
                        if st.button("🗑️ Xóa", key=f"delete_{preset_name}", type="secondary"):
                            delete_custom_preset(preset_name)
                            st.success(f"Đã xóa preset '{preset_name}'")
                            st.rerun()
                        
                        if st.button("📋 Dùng", key=f"use_{preset_name}", type="primary"):
                            st.session_state['use_preset'] = preset_data
                            st.success(f"Đã chọn preset '{preset_name}'. Quay lại calculator để sử dụng.")
    
    # Tab 3: Import/Export
    with tab3:
        st.markdown("### 📥 Import/Export Presets")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📤 Export")
            st.caption("Xuất preset ra file JSON")
            
            presets_json = export_presets()
            st.code(presets_json, language="json")
            
            st.download_button(
                "💾 Tải xuống file JSON",
                presets_json,
                file_name="custom_presets.json",
                mime="application/json",
                key="export_presets"
            )
        
        with col2:
            st.markdown("#### 📥 Import")
            st.caption("Nhập preset từ file JSON")
            
            uploaded_file = st.file_uploader(
                "Chọn file JSON",
                type=["json"],
                key="import_file"
            )
            
            if uploaded_file:
                try:
                    content = uploaded_file.read().decode("utf-8")
                    if import_presets(content):
                        st.success("Đã import preset thành công!")
                        st.rerun()
                    else:
                        st.error("Lỗi: File JSON không hợp lệ")
                except Exception as e:
                    st.error(f"Lỗi import: {str(e)}")
            
            # Or paste JSON
            st.markdown("**Hoặc dán JSON:**")
            pasted_json = st.text_area(
                "Dán JSON ở đây:",
                value="",
                key="import_json",
                height=100
            )
            
            if st.button("📥 Import từ JSON", key="import_button"):
                if pasted_json:
                    if import_presets(pasted_json):
                        st.success("Đã import preset thành công!")
                        st.rerun()
                    else:
                        st.error("Lỗi: JSON không hợp lệ")
                else:
                    st.warning("Vui lòng dán JSON")

