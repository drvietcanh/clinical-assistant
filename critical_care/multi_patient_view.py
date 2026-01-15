"""
Multi-Patient View
View and manage multiple patients simultaneously
"""

import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime
import pandas as pd


def init_multi_patient_state():
    """Initialize multi-patient state"""
    if 'multi_patients' not in st.session_state:
        st.session_state['multi_patients'] = []
    
    if 'selected_patient_id' not in st.session_state:
        st.session_state['selected_patient_id'] = None


def add_patient(patient_id: str, name: str = "", age: int = 0, diagnosis: str = ""):
    """Add a patient to the list"""
    init_multi_patient_state()
    
    patient = {
        'id': patient_id,
        'name': name,
        'age': age,
        'diagnosis': diagnosis,
        'status': 'active',
        'last_update': datetime.now(),
        'alerts': 0,
        'ventilator': False,
        'map': 70.0,
        'rr': 20.0,
        'spO2': 95.0
    }
    
    # Check if patient already exists
    existing = [p for p in st.session_state['multi_patients'] if p['id'] == patient_id]
    if not existing:
        st.session_state['multi_patients'].append(patient)
    else:
        # Update existing
        idx = next(i for i, p in enumerate(st.session_state['multi_patients']) if p['id'] == patient_id)
        st.session_state['multi_patients'][idx].update(patient)


def get_patient_status_summary(patient: Dict) -> Dict:
    """Get status summary for a patient"""
    alerts = 0
    status_color = "success"
    
    # Check for alerts
    if patient.get('map', 70) < 65:
        alerts += 1
        status_color = "error"
    elif patient.get('spO2', 95) < 90:
        alerts += 1
        status_color = "warning"
    elif patient.get('rr', 20) > 30:
        alerts += 1
        status_color = "warning"
    
    return {
        'alerts': alerts,
        'status_color': status_color,
        'status_text': "Ổn định" if alerts == 0 else ("Cảnh báo" if alerts == 1 else "Nghiêm trọng")
    }


def render_patient_card(patient: Dict, columns: int = 3):
    """Render a patient card"""
    status = get_patient_status_summary(patient)
    
    card_html = f"""
    <div style="
        background: {'#fff3cd' if status['status_color'] == 'warning' else ('#f8d7da' if status['status_color'] == 'error' else '#d4edda')};
        border: 2px solid {'#ffc107' if status['status_color'] == 'warning' else ('#dc3545' if status['status_color'] == 'error' else '#28a745')};
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
    ">
        <div style="font-weight: bold; font-size: 16px; margin-bottom: 8px;">
            {patient.get('id', 'N/A')} - {patient.get('name', 'Bệnh nhân')}
        </div>
        <div style="font-size: 14px; color: #666;">
            Tuổi: {patient.get('age', 'N/A')} | {patient.get('diagnosis', 'N/A')}
        </div>
        <div style="margin-top: 8px; display: flex; gap: 12px; font-size: 12px;">
            <span>MAP: {patient.get('map', 0):.0f}</span>
            <span>RR: {patient.get('rr', 0):.0f}</span>
            <span>SpO2: {patient.get('spO2', 0):.0f}%</span>
        </div>
        <div style="margin-top: 4px; font-weight: bold; color: {'#dc3545' if status['status_color'] == 'error' else ('#ffc107' if status['status_color'] == 'warning' else '#28a745')};">
            {status['status_text']} {('🚨' * status['alerts']) if status['alerts'] > 0 else ''}
        </div>
    </div>
    """
    
    return card_html


def render_multi_patient_view():
    """Render multi-patient view"""
    st.header("👥 Multi-Patient View")
    st.caption("Xem và quản lý nhiều bệnh nhân cùng lúc")
    
    init_multi_patient_state()
    
    st.markdown("---")
    
    # Add patient
    st.markdown("### ➕ Thêm bệnh nhân")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        patient_id = st.text_input("Mã BN:", key="mp_patient_id", placeholder="BN-001")
    with col2:
        patient_name = st.text_input("Tên:", key="mp_patient_name", placeholder="Nguyễn Văn A")
    with col3:
        patient_age = st.number_input("Tuổi:", min_value=0, max_value=150, value=50, key="mp_patient_age")
    with col4:
        patient_diagnosis = st.text_input("Chẩn đoán:", key="mp_patient_diagnosis", placeholder="ARDS")
    
    if st.button("➕ Thêm bệnh nhân", use_container_width=True):
        if patient_id:
            add_patient(patient_id, patient_name, patient_age, patient_diagnosis)
            st.success(f"✅ Đã thêm {patient_id}")
            st.rerun()
        else:
            st.error("Vui lòng nhập mã bệnh nhân")
    
    st.markdown("---")
    
    # Patient list
    patients = st.session_state.get('multi_patients', [])
    
    if patients:
        st.markdown(f"### 📋 Danh sách bệnh nhân ({len(patients)})")
        
        # Filter and sort
        col1, col2 = st.columns(2)
        
        with col1:
            filter_status = st.selectbox(
                "Lọc theo trạng thái:",
                ["Tất cả", "Ổn định", "Cảnh báo", "Nghiêm trọng"],
                key="mp_filter"
            )
        
        with col2:
            sort_by = st.selectbox(
                "Sắp xếp theo:",
                ["Mã BN", "Tên", "Tuổi", "Trạng thái"],
                key="mp_sort"
            )
        
        # Filter patients
        filtered_patients = patients
        if filter_status != "Tất cả":
            status_map = {"Ổn định": "success", "Cảnh báo": "warning", "Nghiêm trọng": "error"}
            target_status = status_map.get(filter_status, "success")
            filtered_patients = [
                p for p in patients
                if get_patient_status_summary(p)['status_color'] == target_status
            ]
        
        # Sort patients
        if sort_by == "Mã BN":
            filtered_patients.sort(key=lambda x: x.get('id', ''))
        elif sort_by == "Tên":
            filtered_patients.sort(key=lambda x: x.get('name', ''))
        elif sort_by == "Tuổi":
            filtered_patients.sort(key=lambda x: x.get('age', 0), reverse=True)
        elif sort_by == "Trạng thái":
            filtered_patients.sort(key=lambda x: get_patient_status_summary(x)['alerts'], reverse=True)
        
        # Display in grid
        st.markdown("---")
        
        # Responsive grid
        num_columns = st.slider("Số cột:", 1, 4, 3, key="mp_columns")
        
        rows = (len(filtered_patients) + num_columns - 1) // num_columns
        
        for row in range(rows):
            cols = st.columns(num_columns)
            for col_idx in range(num_columns):
                patient_idx = row * num_columns + col_idx
                if patient_idx < len(filtered_patients):
                    with cols[col_idx]:
                        patient = filtered_patients[patient_idx]
                        st.markdown(render_patient_card(patient), unsafe_allow_html=True)
                        
                        # Quick actions
                        if st.button("📊 Mở", key=f"open_{patient['id']}", use_container_width=True):
                            st.session_state['selected_patient_id'] = patient['id']
                            st.session_state['critical_care_tool_selection'] = "🏥 Patient Dashboard"
                            st.rerun()
        
        # Summary statistics
        st.markdown("---")
        st.markdown("### 📊 Thống kê")
        
        total_alerts = sum(get_patient_status_summary(p)['alerts'] for p in patients)
        stable_count = len([p for p in patients if get_patient_status_summary(p)['alerts'] == 0])
        warning_count = len([p for p in patients if get_patient_status_summary(p)['alerts'] == 1])
        critical_count = len([p for p in patients if get_patient_status_summary(p)['alerts'] > 1])
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tổng số BN", len(patients))
        with col2:
            st.metric("Ổn định", stable_count, delta=None)
        with col3:
            st.metric("Cảnh báo", warning_count, delta=None)
        with col4:
            st.metric("Nghiêm trọng", critical_count, delta=None)
    else:
        st.info("Chưa có bệnh nhân. Thêm bệnh nhân ở trên.")
    
    # Delete patient
    if patients:
        st.markdown("---")
        st.markdown("### 🗑️ Xóa bệnh nhân")
        
        patient_to_delete = st.selectbox(
            "Chọn bệnh nhân để xóa:",
            [p['id'] for p in patients],
            key="delete_patient"
        )
        
        if st.button("🗑️ Xóa", use_container_width=True):
            st.session_state['multi_patients'] = [
                p for p in patients if p['id'] != patient_to_delete
            ]
            st.success(f"✅ Đã xóa {patient_to_delete}")
            st.rerun()
