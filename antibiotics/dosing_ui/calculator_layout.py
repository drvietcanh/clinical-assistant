"""
Calculator Layout Components
Header, metrics display, antibiotic selection
"""

import streamlit as st
from ..antibiotics_data import ANTIBIOTICS_DATABASE


def render_header():
    """Render header section"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧮 Tính liều kháng sinh theo eGFR/CrCl</h2>
    <p style='text-align: center;'><em>Công cụ tính liều tự động cho tất cả kháng sinh dựa trên chức năng thận</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Công cụ này (Enhanced):**
    - ✅ Tự động tính liều dựa trên CrCl/eGFR
    - ✅ Áp dụng cho tất cả kháng sinh trong database
    - ✅ Hỗ trợ bệnh nhân đặc biệt (HD, PD, béo phì, trẻ em)
    - ✅ Tính liều chi tiết (mg/kg, interval, infusion time)
    - ✅ Cảnh báo tự động (tích lũy, độc tính, tương tác)
    - ✅ Tích hợp với eGFR calculator
    """)
    
    st.markdown("---")


def render_weight_metrics(weight, ibw, bmi, is_obese, abw):
    """Render weight metrics display"""
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Cân nặng thực", f"{weight:.1f} kg")
    with col2:
        st.metric("IBW", f"{ibw:.1f} kg")
    with col3:
        st.metric("BMI", f"{bmi:.1f}", help="< 18.5: Gầy | 18.5-25: Bình thường | > 30: Béo phì")
    with col4:
        if is_obese:
            st.metric("ABW", f"{abw:.1f} kg", help="Adjusted Body Weight - dùng cho tính liều")
            st.caption("⚠️ Béo phì: Sẽ dùng ABW")
        else:
            st.metric("Dosing Weight", f"{weight:.1f} kg")


def render_renal_metrics(crcl, egfr, renal_category):
    """Render renal function metrics"""
    category_labels = {
        'normal': '✅ Bình thường (CrCl ≥ 60)',
        '30_60': '⚠️ Suy thận nhẹ-vừa (CrCl 30-59)',
        '15_30': '🔴 Suy thận nặng (CrCl 15-29)',
        'under_15': '🚨 Suy thận rất nặng (CrCl < 15)',
        'hemodialysis': '💉 Đang lọc máu ngắt quãng (HD)',
        'continuous_hd': '💉 Đang lọc máu liên tục (CRRT/CVVH)',
        'peritoneal_dialysis': '💉 Đang lọc màng bụng (PD)'
    }
    
    category_colors = {
        'normal': '🟢',
        '30_60': '🟡',
        '15_30': '🟠',
        'under_15': '🔴',
        'hemodialysis': '🔵',
        'continuous_hd': '🔵',
        'peritoneal_dialysis': '🔵'
    }
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CrCl (Cockcroft-Gault)", f"{crcl:.1f} mL/min", help="Ưu tiên dùng cho điều chỉnh liều thuốc")
    with col2:
        st.metric("eGFR (CKD-EPI)", f"{egfr:.1f} mL/min/1.73m²", help="Dùng cho phân loại CKD")
    
    st.info(f"{category_colors.get(renal_category, '')} **{category_labels.get(renal_category, 'Chưa xác định')}**")


def render_antibiotic_selection():
    """Render antibiotic selection section"""
    st.markdown("### 💊 Chọn kháng sinh")
    
    all_antibiotics = sorted(list(ANTIBIOTICS_DATABASE.keys()))
    
    # Check for preset antibiotic from drug detail view
    preset_antibiotic = st.session_state.get('preset_antibiotic_name', None)
    preset_index = 0
    if preset_antibiotic and preset_antibiotic in all_antibiotics:
        preset_index = all_antibiotics.index(preset_antibiotic)
        st.success(f"✅ **Đã chọn sẵn:** {preset_antibiotic} (từ tra cứu thuốc)")
        # Clear the preset after showing
        if 'preset_antibiotic_name' in st.session_state:
            del st.session_state['preset_antibiotic_name']
    
    col1, col2 = st.columns(2)
    with col1:
        selected_ab = st.selectbox(
            "Kháng sinh:",
            all_antibiotics,
            index=preset_index,
            format_func=lambda x: x,
            key="dosing_antibiotic"
        )
    
    with col2:
        indication = st.selectbox(
            "Chỉ định:",
            ["Chuẩn", "Nhiễm khuẩn nặng", "Viêm màng não", "Viêm nội tâm mạc"],
            key="dosing_indication"
        )
    
    # Other drugs (for interaction checking)
    st.markdown("#### 💊 Thuốc Đang Dùng (Để Kiểm Tra Tương Tác)")
    other_drugs_input = st.text_input(
        "Nhập tên thuốc (cách nhau bằng dấu phẩy):",
        placeholder="Ví dụ: Gentamicin, Furosemide, Warfarin",
        key="other_drugs"
    )
    other_drugs = [d.strip() for d in other_drugs_input.split(",")] if other_drugs_input else []
    
    indication_map = {
        "Chuẩn": "standard",
        "Nhiễm khuẩn nặng": "severe",
        "Viêm màng não": "meningitis",
        "Viêm nội tâm mạc": "endocarditis"
    }
    indication_code = indication_map.get(indication, "standard")
    
    return selected_ab, indication_code, other_drugs


def check_imported_values():
    """Check for imported values from eGFR calculator"""
    imported_crcl = st.session_state.get('patient_crcl', None)
    imported_egfr = st.session_state.get('patient_egfr', None)
    imported_gfr_absolute = st.session_state.get('gfr_absolute', None)
    
    use_imported = False
    if imported_crcl is not None or imported_egfr is not None:
        if imported_crcl and imported_egfr:
            st.success(f"✅ **Đã import từ eGFR Calculator:** CrCl = {imported_crcl:.1f} mL/min | eGFR = {imported_egfr:.1f} mL/min/1.73m²")
        else:
            st.success(f"✅ **Đã import:** eGFR = {imported_egfr:.1f} mL/min/1.73m²")
        use_imported = st.checkbox("Sử dụng giá trị đã import", value=True, key="use_imported")
        st.markdown("---")
    
    return use_imported, imported_crcl, imported_egfr, imported_gfr_absolute

