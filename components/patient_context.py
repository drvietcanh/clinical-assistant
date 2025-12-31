"""
Patient Context Component
Phase 2 Enhancement - Auto-fill functionality for calculators
"""

import streamlit as st

def render_patient_context():
    """
    Renders the Patient Context sidebar with enhanced UI (Phase 2)
    Stores data in st.session_state for auto-fill across all calculators
    """
    st.sidebar.markdown("---")
    with st.sidebar.expander("👤 Thông tin bệnh nhân", expanded=True):
        st.caption("💡 Nhập 1 lần - Tự động điền mọi nơi")
        
        # Initialize session state for patient context
        if 'patient_weight' not in st.session_state:
            st.session_state.patient_weight = 0.0
        if 'patient_height' not in st.session_state:
            st.session_state.patient_height = 0.0
        if 'patient_age' not in st.session_state:
            st.session_state.patient_age = 0
        if 'patient_scr' not in st.session_state:
            st.session_state.patient_scr = 0.0
        if 'patient_gender' not in st.session_state:
            st.session_state.patient_gender = "Nam"
            
        # Inputs with improved layout
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)", 
                min_value=0.0, 
                max_value=200.0, 
                step=0.1, 
                key="input_weight", 
                value=st.session_state.get('patient_weight', 0.0),
                help="Cân nặng hiện tại của bệnh nhân"
            )
        with col2:
            height = st.number_input(
                "Chiều cao (cm)", 
                min_value=0.0, 
                max_value=250.0, 
                step=1.0, 
                key="input_height",
                value=st.session_state.get('patient_height', 0.0),
                help="Chiều cao của bệnh nhân"
            )
        
        col3, col4 = st.columns(2)
        with col3:
            age = st.number_input(
                "Tuổi (năm)", 
                min_value=0, 
                max_value=120, 
                step=1, 
                key="input_age",
                value=int(st.session_state.get('patient_age', 0)),
                help="Tuổi của bệnh nhân"
            )
        with col4:
            gender = st.selectbox(
                "Giới tính",
                options=["Nam", "Nữ"],
                index=0 if st.session_state.get('patient_gender', 'Nam') == 'Nam' else 1,
                key="input_gender",
                help="Giới tính (quan trọng cho CrCl)"
            )
                            
        # Creatinine (Critical for renal dosing)
        scr = st.number_input(
            "Creatinine (micromol/L)", 
            min_value=0.0, 
            max_value=1000.0, 
            step=1.0, 
            key="input_scr",
            value=st.session_state.get('patient_scr', 0.0),
            help="Creatinine huyết thanh (quan trọng cho điều chỉnh liều)"
        )
                            
        # Update session state
        st.session_state.patient_weight = weight
        st.session_state.patient_height = height
        st.session_state.patient_age = int(age)
        st.session_state.patient_scr = scr
        st.session_state.patient_gender = gender
        
        # Display derived metrics with better styling
        if weight > 0 and height > 0:
            bmi = weight / ((height/100)**2)
            bmi_category = "Thiếu cân" if bmi < 18.5 else "Bình thường" if bmi < 25 else "Thừa cân" if bmi < 30 else "Béo phì"
            st.markdown(f"📊 **BMI:** {bmi:.1f} kg/m² ({bmi_category})")
            
        if scr > 0 and age > 0 and weight > 0:
            # Cockcroft-Gault (adjusted for gender)
            crcl = ((140 - age) * weight) / (0.814 * scr)
            if gender == "Nữ":
                crcl *= 0.85
            
            # Color code based on CrCl
            if crcl >= 90:
                color = "🟢"
                status = "Bình thường"
            elif crcl >= 60:
                color = "🟡"
                status = "Giảm nhẹ"
            elif crcl >= 30:
                color = "🟠"
                status = "Giảm vừa"
            else:
                color = "🔴"
                status = "Giảm nặng"
            
            st.markdown(f"{color} **CrCl:** {crcl:.1f} ml/min ({status})")
        
        # Clear button
        if st.button("🗑️ Xóa dữ liệu", use_container_width=True, help="Xóa tất cả thông tin bệnh nhân"):
            st.session_state.patient_weight = 0.0
            st.session_state.patient_height = 0.0
            st.session_state.patient_age = 0
            st.session_state.patient_scr = 0.0
            st.session_state.patient_gender = "Nam"
            st.rerun()
