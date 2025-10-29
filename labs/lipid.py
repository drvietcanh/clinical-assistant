"""
Lipid Panel
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Lipid Panel"""
    st.subheader("💊 Lipid Panel")
    st.caption("Mỡ Máu - Chuyển đổi đơn vị mmol/L ↔ mg/dL")
    
    # Unit selection
    st.markdown("#### 🔄 Chọn Đơn Vị")
    unit_system = st.radio(
        "Hệ đơn vị:",
        ["mmol/L (SI Units - Mặc định)", "mg/dL (Conventional)"],
        horizontal=True,
        key="lipid_unit_system"
    )
    
    use_si = "mmol/L" in unit_system
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Nhập Giá Trị")
        
        # Total Cholesterol
        st.markdown("**Total Cholesterol**")
        if use_si:
            chol_input = st.number_input(
                "Total Cholesterol (mmol/L)",
                0.0, 15.0, 4.65, 0.1,
                help="Bình thường: <5.2 mmol/L",
                key="chol_mmol"
            )
            chol = chol_input * 38.67  # Convert to mg/dL for calculations
            st.caption(f"≈ {chol:.1f} mg/dL")
        else:
            chol = st.number_input(
                "Total Cholesterol (mg/dL)",
                0.0, 500.0, 180.0, 1.0,
                help="Bình thường: <200 mg/dL",
                key="chol_mgdl"
            )
            st.caption(f"≈ {chol/38.67:.2f} mmol/L")
        
        # LDL
        st.markdown("**LDL Cholesterol**")
        if use_si:
            ldl_input = st.number_input(
                "LDL Cholesterol (mmol/L)",
                0.0, 10.0, 2.59, 0.1,
                help="Mục tiêu: <2.6 mmol/L",
                key="ldl_mmol"
            )
            ldl = ldl_input * 38.67
            st.caption(f"≈ {ldl:.1f} mg/dL")
        else:
            ldl = st.number_input(
                "LDL Cholesterol (mg/dL)",
                0.0, 300.0, 100.0, 1.0,
                help="Mục tiêu: <100 mg/dL",
                key="ldl_mgdl"
            )
            st.caption(f"≈ {ldl/38.67:.2f} mmol/L")
        
        # HDL
        st.markdown("**HDL Cholesterol**")
        if use_si:
            hdl_input = st.number_input(
                "HDL Cholesterol (mmol/L)",
                0.0, 5.0, 1.29, 0.1,
                help="Nam >1.0, Nữ >1.3 mmol/L",
                key="hdl_mmol"
            )
            hdl = hdl_input * 38.67
            st.caption(f"≈ {hdl:.1f} mg/dL")
        else:
            hdl = st.number_input(
                "HDL Cholesterol (mg/dL)",
                0.0, 150.0, 50.0, 1.0,
                help="Nam >40, Nữ >50 mg/dL",
                key="hdl_mgdl"
            )
            st.caption(f"≈ {hdl/38.67:.2f} mmol/L")
        
        # Triglycerides
        st.markdown("**Triglycerides**")
        if use_si:
            tg_input = st.number_input(
                "Triglycerides (mmol/L)",
                0.0, 15.0, 1.35, 0.1,
                help="Bình thường: <1.7 mmol/L",
                key="tg_mmol"
            )
            tg = tg_input * 88.57  # Convert to mg/dL for calculations
            st.caption(f"≈ {tg:.1f} mg/dL")
        else:
            tg = st.number_input(
                "Triglycerides (mg/dL)",
                0.0, 1000.0, 120.0, 1.0,
                help="Bình thường: <150 mg/dL",
                key="tg_mgdl"
            )
            st.caption(f"≈ {tg/88.57:.2f} mmol/L")
        
        # Calculate ratios
        if hdl > 0:
            chol_hdl = chol / hdl
            st.info(f"**Total Chol/HDL ratio:** {chol_hdl:.1f}")
            if chol_hdl > 5:
                st.caption("⬆️ High risk (>5)")
            elif chol_hdl < 3.5:
                st.caption("✓ Low risk (<3.5)")
            else:
                st.caption("⚠️ Average risk (3.5-5)")
    
    with col2:
        st.markdown("#### Interpretation")
        
        # Total Cholesterol
        if chol < 200:
            st.success(f"**Total Cholesterol:** {chol} - Desirable ✓")
        elif chol < 240:
            st.warning(f"**Total Cholesterol:** {chol} - Borderline high ⚠️")
        else:
            st.error(f"**Total Cholesterol:** {chol} - High ⬆️")
        
        # LDL
        if ldl < 100:
            st.success(f"**LDL:** {ldl} - Optimal ✓")
        elif ldl < 130:
            st.info(f"**LDL:** {ldl} - Near optimal")
        elif ldl < 160:
            st.warning(f"**LDL:** {ldl} - Borderline high ⚠️")
        elif ldl < 190:
            st.error(f"**LDL:** {ldl} - High ⬆️")
        else:
            st.error(f"**LDL:** {ldl} - Very high ⬆️⬆️")
        
        # HDL
        if hdl < 40:
            st.error(f"**HDL:** {hdl} - Low (⬇️ risk factor)")
        elif hdl < 60:
            st.success(f"**HDL:** {hdl} - Normal ✓")
        else:
            st.success(f"**HDL:** {hdl} - High (✓ protective)")
        
        # Triglycerides
        if tg < 150:
            st.success(f"**Triglycerides:** {tg} - Normal ✓")
        elif tg < 200:
            st.warning(f"**Triglycerides:** {tg} - Borderline high ⚠️")
        elif tg < 500:
            st.error(f"**Triglycerides:** {tg} - High ⬆️")
        else:
            st.error(f"**Triglycerides:** {tg} - Very high ⬆️⬆️")
    
    st.markdown("---")
    st.info("""
    **LDL Goals by Risk:**
    - Very high risk (CAD, DM): <70 mg/dL
    - High risk (2+ risk factors): <100 mg/dL
    - Moderate risk: <130 mg/dL
    - Low risk: <160 mg/dL
    """)
