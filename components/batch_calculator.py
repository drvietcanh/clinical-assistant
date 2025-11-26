"""
Batch Calculator Component
Calculate for multiple patients at once
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Callable, Any, Optional
from datetime import datetime


def render_batch_calculator(
    calculator_function: Callable,
    input_fields: List[Dict[str, Any]],
    calculator_name: str,
    max_patients: int = 10
):
    """
    Render batch calculator UI
    
    Args:
        calculator_function: Function that takes inputs and returns results
        input_fields: List of input field definitions
            Example: [
                {'name': 'age', 'label': 'Age', 'type': 'number', 'min': 0, 'max': 120},
                {'name': 'weight', 'label': 'Weight (kg)', 'type': 'number', 'min': 0}
            ]
        calculator_name: Name of the calculator
        max_patients: Maximum number of patients
    """
    st.subheader(f"📊 Batch Calculator: {calculator_name}")
    st.caption(f"Tính toán cho tối đa {max_patients} bệnh nhân cùng lúc")
    
    # Initialize batch data
    if 'batch_data' not in st.session_state:
        st.session_state.batch_data = []
    
    # Add patient button
    if st.button("➕ Thêm bệnh nhân", key="add_patient_batch"):
        if len(st.session_state.batch_data) < max_patients:
            patient_data = {
                'id': f"patient_{len(st.session_state.batch_data)}_{datetime.now().timestamp()}",
                'name': f"Bệnh nhân {len(st.session_state.batch_data) + 1}",
                'inputs': {}
            }
            st.session_state.batch_data.append(patient_data)
            st.rerun()
        else:
            st.warning(f"Tối đa {max_patients} bệnh nhân")
    
    if not st.session_state.batch_data:
        st.info("👆 Click 'Thêm bệnh nhân' để bắt đầu")
        return
    
    # Display batch input form
    results = []
    
    for idx, patient in enumerate(st.session_state.batch_data):
        with st.expander(f"👤 {patient['name']}", expanded=True):
            # Patient name
            patient_name = st.text_input(
                "Tên bệnh nhân",
                value=patient['name'],
                key=f"patient_name_{patient['id']}"
            )
            patient['name'] = patient_name
            
            # Input fields
            cols = st.columns(min(3, len(input_fields)))
            patient_inputs = {}
            
            for field_idx, field in enumerate(input_fields):
                col = cols[field_idx % len(cols)]
                with col:
                    if field['type'] == 'number':
                        value = st.number_input(
                            field['label'],
                            min_value=field.get('min'),
                            max_value=field.get('max'),
                            value=patient['inputs'].get(field['name'], field.get('default', 0)),
                            step=field.get('step', 1),
                            key=f"{field['name']}_{patient['id']}"
                        )
                    elif field['type'] == 'select':
                        value = st.selectbox(
                            field['label'],
                            options=field.get('options', []),
                            index=field.get('options', []).index(patient['inputs'].get(field['name'], field.get('default'))) if patient['inputs'].get(field['name']) in field.get('options', []) else 0,
                            key=f"{field['name']}_{patient['id']}"
                        )
                    else:
                        value = st.text_input(
                            field['label'],
                            value=patient['inputs'].get(field['name'], field.get('default', '')),
                            key=f"{field['name']}_{patient['id']}"
                        )
                    
                    patient_inputs[field['name']] = value
            
            patient['inputs'] = patient_inputs
            
            # Calculate button
            if st.button("🧮 Tính toán", key=f"calc_{patient['id']}"):
                try:
                    result = calculator_function(**patient_inputs)
                    patient['result'] = result
                    patient['calculated_at'] = datetime.now().isoformat()
                    st.success("✅ Tính toán thành công")
                except Exception as e:
                    st.error(f"❌ Lỗi: {str(e)}")
            
            # Show result if available
            if 'result' in patient:
                st.markdown("**Kết quả:**")
                if isinstance(patient['result'], dict):
                    st.json(patient['result'])
                else:
                    st.write(patient['result'])
            
            # Delete patient
            if st.button("🗑️ Xóa", key=f"delete_{patient['id']}"):
                st.session_state.batch_data = [
                    p for p in st.session_state.batch_data if p['id'] != patient['id']
                ]
                st.rerun()
            
            results.append({
                'patient': patient_name,
                'inputs': patient_inputs,
                'result': patient.get('result'),
                'calculated_at': patient.get('calculated_at')
            })
    
    # Batch actions
    if st.session_state.batch_data:
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🧮 Tính toán tất cả", key="calc_all_batch"):
                for patient in st.session_state.batch_data:
                    try:
                        result = calculator_function(**patient['inputs'])
                        patient['result'] = result
                        patient['calculated_at'] = datetime.now().isoformat()
                    except Exception as e:
                        st.error(f"Lỗi với {patient['name']}: {str(e)}")
                st.rerun()
        
        with col2:
            if st.button("📊 Xem bảng kết quả", key="view_table_batch"):
                st.session_state['show_batch_table'] = True
        
        with col3:
            if st.button("🗑️ Xóa tất cả", key="clear_all_batch"):
                st.session_state.batch_data = []
                st.rerun()
        
        # Show results table
        if st.session_state.get('show_batch_table', False):
            st.markdown("### 📊 Bảng Kết quả")
            
            # Prepare table data
            table_data = []
            for patient in st.session_state.batch_data:
                row = {'Bệnh nhân': patient['name']}
                row.update(patient['inputs'])
                if 'result' in patient:
                    if isinstance(patient['result'], dict):
                        for key, value in patient['result'].items():
                            row[f"Kết quả: {key}"] = value
                    else:
                        row['Kết quả'] = patient['result']
                table_data.append(row)
            
            if table_data:
                df = pd.DataFrame(table_data)
                st.dataframe(df, use_container_width=True)
                
                # Export
                csv = df.to_csv(index=False)
                st.download_button(
                    "📥 Tải xuống CSV",
                    csv,
                    file_name=f"batch_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            if st.button("❌ Đóng bảng", key="close_table_batch"):
                st.session_state['show_batch_table'] = False
                st.rerun()

