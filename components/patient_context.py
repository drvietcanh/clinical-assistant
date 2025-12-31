import streamlit as st

def render_patient_context():
    """
    Renders the Patient Context sidebar input for persistent data.
    Stores data in st.session_state for use across all calculators.
    """
    st.sidebar.markdown("---")
    with st.sidebar.expander("👤 Thông tin bệnh nhân", expanded=True):
        st.caption("Nhập liệu 1 lần - Sử dụng mọi nơi")
        
        # Initialize session state for patient context
        if 'patient_weight' not in st.session_state:
            st.session_state.patient_weight = 0.0
        if 'patient_height' not in st.session_state:
            st.session_state.patient_height = 0.0
        if 'patient_age' not in st.session_state:
            st.session_state.patient_age = 0
            
        # Inputs with callback to update state immediately
        col1, col2 = st.columns(2)
        with col1:
             weight = st.number_input("Cân nặng (kg)", min_value=0.0, max_value=200.0, step=0.1, key="input_weight", 
                                     value=st.session_state.get('patient_weight', 0.0))
        with col2:
             height = st.number_input("Chiều cao (cm)", min_value=0.0, max_value=250.0, step=1.0, key="input_height",
                                     value=st.session_state.get('patient_height', 0.0))
             
        age = st.number_input("Tuổi (năm)", min_value=0, max_value=120, step=1, key="input_age",
                            value=int(st.session_state.get('patient_age', 0)))
                            
        # Creatinine (Critical for renal dosing)
        scr = st.number_input("Creatinine (micromol/L)", min_value=0.0, max_value=1000.0, step=1.0, key="input_scr",
                            value=st.session_state.get('patient_scr', 0.0))
                            
        # Update session state
        st.session_state.patient_weight = weight
        st.session_state.patient_height = height
        st.session_state.patient_age = int(age)
        st.session_state.patient_scr = scr
        
        # Display derived metrics (simple Calc)
        if weight > 0 and height > 0:
            bmi = weight / ((height/100)**2)
            st.caption(f"📊 BMI: **{bmi:.1f}**")
            
        if scr > 0 and age > 0 and weight > 0:
            # Cockcroft-Gault (Simple Estimate)
            crcl = ((140 - age) * weight) / (0.814 * scr)
            st.caption(f"🧪 Est. CrCl: **{crcl:.1f}** ml/min")
