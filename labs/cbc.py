"""
Complete Blood Count (CBC) Panel
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Complete Blood Count"""
    st.subheader("🔬 CBC - Complete Blood Count")
    st.caption("Toàn Bộ Tế Bào Máu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values / Nhập Kết Quả")
        
        gender = st.radio("Giới tính:", ["Male/Nam", "Female/Nữ"], key="cbc_gender")
        gender_key = "male" if "Male" in gender else "female"
        
        # WBC
        wbc = st.number_input(
            "WBC - Bạch cầu (x10³/µL)",
            min_value=0.0,
            max_value=100.0,
            value=7.0,
            step=0.1,
            key="wbc"
        )
        
        # RBC
        rbc = st.number_input(
            "RBC - Hồng cầu (x10⁶/µL)",
            min_value=0.0,
            max_value=10.0,
            value=5.0,
            step=0.1,
            key="rbc"
        )
        
        # Hemoglobin
        hgb = st.number_input(
            "Hemoglobin - Huyết sắc tố (g/dL)",
            min_value=0.0,
            max_value=25.0,
            value=14.0,
            step=0.1,
            key="hgb"
        )
        
        # Hematocrit
        hct = st.number_input(
            "Hematocrit (%) ",
            min_value=0.0,
            max_value=70.0,
            value=42.0,
            step=0.1,
            key="hct"
        )
        
        # MCV
        mcv = st.number_input(
            "MCV (fL)",
            min_value=0.0,
            max_value=150.0,
            value=90.0,
            step=0.1,
            key="mcv"
        )
        
        # MCH
        mch = st.number_input(
            "MCH (pg)",
            min_value=0.0,
            max_value=50.0,
            value=30.0,
            step=0.1,
            key="mch"
        )
        
        # MCHC
        mchc = st.number_input(
            "MCHC (g/dL)",
            min_value=0.0,
            max_value=40.0,
            value=34.0,
            step=0.1,
            key="mchc"
        )
        
        # Platelets
        plt = st.number_input(
            "Platelets - Tiểu cầu (x10³/µL)",
            min_value=0.0,
            max_value=2000.0,
            value=250.0,
            step=1.0,
            key="plt"
        )
    
    with col2:
        st.markdown("#### Interpretation / Giải Thích")
        
        results = {
            "WBC": wbc,
            "RBC": rbc,
            "Hemoglobin": hgb,
            "Hematocrit": hct,
            "MCV": mcv,
            "MCH": mch,
            "MCHC": mchc,
            "Platelets": plt
        }
        
        for test_name, value in results.items():
            test_data = ALL_RANGES.get(test_name, {})
            normal_range = get_normal_range(test_name, gender_key)
            interpretation = interpret_value(test_name, value, gender_key)
            
            # Display result
            if "CRITICALLY" in interpretation:
                st.error(f"**{test_data.get('vn_name', test_name)}:** {value} {test_data.get('unit', '')} - {interpretation}")
            elif "Low" in interpretation or "High" in interpretation:
                st.warning(f"**{test_data.get('vn_name', test_name)}:** {value} {test_data.get('unit', '')} - {interpretation}")
            else:
                st.success(f"**{test_data.get('vn_name', test_name)}:** {value} {test_data.get('unit', '')} - {interpretation}")
            
            # Show normal range
            if "min" in normal_range and "max" in normal_range:
                st.caption(f"   Normal: {normal_range['min']}-{normal_range['max']} {test_data.get('unit', '')}")
            elif "max" in normal_range:
                st.caption(f"   Normal: <{normal_range['max']} {test_data.get('unit', '')}")
    
    # Interpretation guide
    st.markdown("---")
    with st.expander("📚 Interpretation Guide / Hướng Dẫn Giải Thích"):
        st.markdown("""
        **WBC (White Blood Cells):**
        - ⬆️ High: Nhiễm trùng, viêm, ung thư máu
        - ⬇️ Low: Suy tủy, virus, thuốc ức chế tủy
        
        **RBC/Hgb/Hct:**
        - ⬇️ Low: Thiếu máu (anemia)
        - ⬆️ High: Mất nước, polycythemia
        
        **MCV (Mean Corpuscular Volume):**
        - <80 fL: Microcytic (thiếu sắt, thalassemia)
        - 80-100 fL: Normocytic (mất máu cấp, bệnh mạn)
        - >100 fL: Macrocytic (thiếu B12/folate, rượu)
        
        **Platelets:**
        - ⬆️ High: Nhiễm trùng, viêm, ung thư, sau cắt lách
        - ⬇️ Low: ITP, DIC, thuốc, virus, suy tủy
        """)
