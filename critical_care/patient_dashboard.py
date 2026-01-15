"""
Integrated Patient Dashboard for Critical Care
Displays comprehensive patient information with real-time alerts and quick actions
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert
from datetime import datetime


def init_patient_state():
    """Initialize patient state in session_state"""
    if 'patient_data' not in st.session_state:
        st.session_state['patient_data'] = {
            'ventilator': {},
            'abg': {},
            'sedation': {},
            'fluid': {},
            'vasopressor': {},
            'scoring': {}
        }


def get_patient_summary():
    """Get summary of current patient data"""
    init_patient_state()
    data = st.session_state['patient_data']
    
    summary = {
        'has_ventilator': bool(data.get('ventilator')),
        'has_abg': bool(data.get('abg')),
        'has_sedation': bool(data.get('sedation')),
        'has_fluid': bool(data.get('fluid')),
        'has_vasopressor': bool(data.get('vasopressor')),
        'has_scoring': bool(data.get('scoring'))
    }
    
    return summary


def calculate_pf_ratio(pao2: float, fio2: float) -> float:
    """Calculate P/F ratio"""
    if fio2 > 0:
        return pao2 / fio2
    return None


def classify_ards_severity(pf_ratio: float) -> dict:
    """Classify ARDS severity based on P/F ratio"""
    if pf_ratio is None:
        return {'severity': None, 'color': None, 'message': None}
    
    if pf_ratio > 300:
        return {'severity': 'None', 'color': 'success', 'message': 'Không ARDS'}
    elif pf_ratio > 200:
        return {'severity': 'Mild', 'color': 'info', 'message': 'ARDS nhẹ (200-300)'}
    elif pf_ratio > 100:
        return {'severity': 'Moderate', 'color': 'warning', 'message': 'ARDS trung bình (100-200)'}
    else:
        return {'severity': 'Severe', 'color': 'error', 'message': 'ARDS nặng (<100)'}


def render_patient_dashboard():
    """Render integrated patient dashboard"""
    st.header("🏥 Bảng điều khiển bệnh nhân")
    st.caption("Tổng hợp thông tin bệnh nhân và hỗ trợ quyết định lâm sàng")
    
    init_patient_state()
    
    # Patient information section
    st.markdown("### 📋 Thông tin bệnh nhân")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        patient_id = st.text_input("Mã bệnh nhân:", key="patient_id", placeholder="BN-001")
        age = st.number_input("Tuổi:", min_value=0, max_value=150, value=0, key="patient_age")
    
    with col2:
        sex = st.selectbox("Giới tính:", ["Nam", "Nữ"], key="patient_sex")
        height = st.number_input("Chiều cao (cm):", min_value=0.0, value=170.0, key="patient_height")
    
    with col3:
        weight = st.number_input("Cân nặng (kg):", min_value=0.0, value=70.0, key="patient_weight")
        diagnosis = st.text_input("Chẩn đoán:", key="patient_diagnosis", placeholder="ARDS, Sepsis, etc.")
    
    st.markdown("---")
    
    # Main dashboard tabs
    tabs = st.tabs([
        "🫁 Hô hấp & Máy thở",
        "💧 Dịch & Huyết động",
        "💤 An thần & Giảm đau",
        "📊 Đánh giá tổng hợp"
    ])
    
    # Tab 1: Respiratory & Ventilator
    with tabs[0]:
        st.markdown("### 🫁 Thông số máy thở")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Cài đặt máy thở:**")
            mode = st.selectbox("Mode:", ["AC", "VC", "SIMV", "PSV", "CPAP"], key="vent_mode")
            vt_ml = st.number_input("Tidal Volume (mL):", min_value=0.0, value=420.0, key="vent_vt")
            rr = st.number_input("Respiratory Rate (/min):", min_value=0.0, value=20.0, key="vent_rr")
            peep = st.number_input("PEEP (cmH2O):", min_value=0.0, value=10.0, key="vent_peep")
            fio2 = st.slider("FiO2:", 0.21, 1.0, 0.6, 0.01, key="vent_fio2")
        
        with col2:
            st.markdown("**Thông số đo được:**")
            plateau = st.number_input("Plateau Pressure (cmH2O):", min_value=0.0, value=25.0, key="vent_plateau")
            peak = st.number_input("Peak Pressure (cmH2O):", min_value=0.0, value=30.0, key="vent_peak")
            compliance = st.number_input("Compliance (mL/cmH2O):", min_value=0.0, value=30.0, key="vent_compliance")
            
            st.markdown("**ABG:**")
            ph = st.number_input("pH:", min_value=6.5, max_value=7.8, value=7.35, step=0.01, key="abg_ph")
            paco2 = st.number_input("PaCO2 (mmHg):", min_value=0.0, value=45.0, key="abg_paco2")
            pao2 = st.number_input("PaO2 (mmHg):", min_value=0.0, value=60.0, key="abg_pao2")
            hco3 = st.number_input("HCO3- (mEq/L):", min_value=0.0, value=24.0, key="abg_hco3")
        
        # Calculate and display P/F ratio
        pf_ratio = calculate_pf_ratio(pao2, fio2)
        ards_class = classify_ards_severity(pf_ratio)
        
        # Save to session state
        st.session_state['patient_data']['ventilator'] = {
            'mode': mode,
            'vt_ml': vt_ml,
            'rr': rr,
            'peep': peep,
            'fio2': fio2,
            'plateau': plateau,
            'peak': peak,
            'compliance': compliance
        }
        
        st.session_state['patient_data']['abg'] = {
            'ph': ph,
            'paco2': paco2,
            'pao2': pao2,
            'hco3': hco3,
            'pf_ratio': pf_ratio
        }
        
        # Display results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if pf_ratio:
                render_result_card(
                    title="P/F Ratio",
                    value=f"{pf_ratio:.0f}",
                    unit="",
                    color=ards_class['color'],
                    subtitle=ards_class['message']
                )
        
        with col2:
            driving_pressure = plateau - peep if plateau and peep else None
            if driving_pressure:
                dp_color = 'error' if driving_pressure > 15 else ('warning' if driving_pressure > 12 else 'success')
                render_result_card(
                    title="Driving Pressure",
                    value=f"{driving_pressure:.1f}",
                    unit="cmH2O",
                    color=dp_color,
                    subtitle="Target: ≤15 cmH2O"
                )
        
        with col3:
            if plateau:
                plat_color = 'error' if plateau > 30 else ('warning' if plateau > 28 else 'success')
                render_result_card(
                    title="Plateau Pressure",
                    value=f"{plateau:.1f}",
                    unit="cmH2O",
                    color=plat_color,
                    subtitle="Target: ≤30 cmH2O"
                )
        
        # Quick actions
        st.markdown("---")
        st.markdown("### ⚡ Hành động nhanh")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🫁 Mở Ventilator Calculator", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
                st.rerun()
        
        with col2:
            if st.button("📊 Mở ARDS Protocol", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "🫁 ARDS Protocols"
                st.rerun()
        
        with col3:
            if st.button("🔄 Đánh giá cai máy thở", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
                st.session_state['ventilator_tool_to_open'] = 'weaning'
                st.rerun()
    
    # Tab 2: Fluid & Hemodynamics
    with tabs[1]:
        st.markdown("### 💧 Dịch & Huyết động")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Huyết động:**")
            map = st.number_input("MAP (mmHg):", min_value=0.0, value=70.0, key="hemo_map")
            cvp = st.number_input("CVP (mmHg):", min_value=0.0, value=8.0, key="hemo_cvp")
            urine_output = st.number_input("Lượng nước tiểu (mL/h):", min_value=0.0, value=50.0, key="hemo_urine")
        
        with col2:
            st.markdown("**Dịch:**")
            fluid_in = st.number_input("Dịch vào (mL/24h):", min_value=0.0, value=2000.0, key="fluid_in")
            fluid_out = st.number_input("Dịch ra (mL/24h):", min_value=0.0, value=1500.0, key="fluid_out")
            fluid_balance = fluid_in - fluid_out
            
            render_result_card(
                title="Cân bằng dịch",
                value=f"{fluid_balance:+.0f}",
                unit="mL/24h",
                color='warning' if abs(fluid_balance) > 1000 else 'success',
                subtitle="Target: ±500 mL"
            )
        
        # Save to session state
        st.session_state['patient_data']['fluid'] = {
            'in': fluid_in,
            'out': fluid_out,
            'balance': fluid_balance,
            'urine_output': urine_output
        }
        
        st.session_state['patient_data']['vasopressor'] = {
            'map': map,
            'cvp': cvp
        }
        
        # Quick actions
        st.markdown("---")
        st.markdown("### ⚡ Hành động nhanh")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("💧 Mở Fluid Calculator", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "💧 Fluid Therapy"
                st.rerun()
        
        with col2:
            if st.button("💉 Mở Vasopressor Guide", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "💉 Vasopressors"
                st.rerun()
        
        with col3:
            if st.button("💉 Mở Shock Management", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "💉 Shock Management"
                st.rerun()
    
    # Tab 3: Sedation & Analgesia
    with tabs[2]:
        st.markdown("### 💤 An thần & Giảm đau")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Thuốc an thần:**")
            sedation_drug = st.selectbox("Thuốc:", ["Propofol", "Midazolam", "Dexmedetomidine"], key="sed_drug")
            sedation_rate = st.number_input("Tốc độ (mcg/kg/min hoặc mg/h):", min_value=0.0, value=50.0, key="sed_rate")
        
        with col2:
            st.markdown("**Đánh giá:**")
            rass = st.slider("RASS Score:", -5, 4, -2, key="sed_rass")
            cam_icu = st.selectbox("CAM-ICU:", ["Âm tính", "Dương tính"], key="sed_cam")
        
        # Save to session state
        st.session_state['patient_data']['sedation'] = {
            'drug': sedation_drug,
            'rate': sedation_rate,
            'rass': rass,
            'cam_icu': cam_icu
        }
        
        # RASS interpretation
        rass_target = "Mục tiêu: -1 đến -2"
        rass_color = 'success' if -2 <= rass <= -1 else ('warning' if -3 <= rass <= 0 else 'error')
        
        render_result_card(
            title="RASS Score",
            value=f"{rass}",
            unit="",
            color=rass_color,
            subtitle=rass_target
        )
        
        # Quick actions
        st.markdown("---")
        st.markdown("### ⚡ Hành động nhanh")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💤 Mở Sedation Calculator", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "💤 Sedation & Analgesia"
                st.rerun()
        
        with col2:
            if st.button("📊 Mở RASS Calculator", use_container_width=True):
                st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
                st.session_state['scoring_calc_to_open'] = 'rass'
                st.rerun()
    
    # Tab 4: Comprehensive Assessment
    with tabs[3]:
        st.markdown("### 📊 Đánh giá tổng hợp")
        
        # Get all data
        vent_data = st.session_state['patient_data'].get('ventilator', {})
        abg_data = st.session_state['patient_data'].get('abg', {})
        fluid_data = st.session_state['patient_data'].get('fluid', {})
        sed_data = st.session_state['patient_data'].get('sedation', {})
        
        # Display summary
        st.markdown("**Tóm tắt:**")
        
        summary_items = []
        
        if abg_data.get('pf_ratio'):
            pf = abg_data['pf_ratio']
            ards_class = classify_ards_severity(pf)
            summary_items.append(f"**P/F Ratio:** {pf:.0f} ({ards_class['message']})")
        
        if vent_data.get('plateau'):
            plat = vent_data['plateau']
            summary_items.append(f"**Plateau Pressure:** {plat:.1f} cmH2O")
        
        if sed_data.get('rass') is not None:
            rass = sed_data['rass']
            summary_items.append(f"**RASS:** {rass}")
        
        if fluid_data.get('balance') is not None:
            balance = fluid_data['balance']
            summary_items.append(f"**Fluid Balance:** {balance:+.0f} mL/24h")
        
        if summary_items:
            for item in summary_items:
                st.markdown(f"- {item}")
        else:
            st.info("Chưa có dữ liệu. Vui lòng nhập thông tin ở các tab trên.")
        
        # Quick links to all tools
        st.markdown("---")
        st.markdown("### 🔗 Liên kết nhanh")
        
        tools = [
            ("🫁 Ventilator Management", "🫁 Ventilator Management"),
            ("🫁 ARDS Protocols", "🫁 ARDS Protocols"),
            ("💧 Fluid Therapy", "💧 Fluid Therapy"),
            ("💉 Vasopressors", "💉 Vasopressors"),
            ("💤 Sedation & Analgesia", "💤 Sedation & Analgesia"),
            ("📊 Scoring Systems", "📊 Scoring Systems"),
            ("🦠 Sepsis Protocols", "🦠 Sepsis Protocols"),
            ("💉 Shock Management", "💉 Shock Management")
        ]
        
        cols = st.columns(4)
        for idx, (label, tool_value) in enumerate(tools):
            with cols[idx % 4]:
                if st.button(label, key=f"quick_link_{idx}", use_container_width=True):
                    st.session_state['critical_care_tool_selection'] = tool_value
                    st.rerun()
