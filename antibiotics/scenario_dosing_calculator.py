"""
Scenario Dosing Calculator - Phase 3: Visual Charts & Export
Tính liều cho nhiều scenarios (CrCl khác nhau) với biểu đồ trực quan và export
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from .dosing_calculator import (
    calculate_adjusted_dose,
    calculate_detailed_dose,
    calculate_ibw,
    calculate_abw,
    calculate_bmi,
    calculate_crcl,
    calculate_egfr_simplified
)
from .antibiotics_data import ANTIBIOTICS_DATABASE


def calculate_scenarios(antibiotic_name, weight, height, age, sex, scenarios_list, indications_list):
    """
    Tính liều cho nhiều scenarios (CrCl categories và indications)
    
    Args:
        antibiotic_name: Tên kháng sinh
        weight: Cân nặng (kg)
        height: Chiều cao (cm)
        age: Tuổi
        sex: Giới tính ("Nam" hoặc "Nữ")
        scenarios_list: List các CrCl values hoặc categories
        indications_list: List các indications ("standard", "severe", "meningitis")
    
    Returns:
        List of dicts với kết quả cho mỗi scenario
    """
    results = []
    
    # Calculate IBW, ABW, BMI
    ibw = calculate_ibw(height, sex)
    bmi = calculate_bmi(weight, height)
    is_obese = bmi > 30 or weight > ibw * 1.25
    abw = calculate_abw(weight, ibw) if is_obese else weight
    
    # Process scenarios
    for scenario in scenarios_list:
        if isinstance(scenario, dict):
            # Scenario is a dict with crcl and category
            crcl = scenario.get('crcl', 60)
            category = scenario.get('category', 'Normal')
        elif isinstance(scenario, (int, float)):
            # Scenario is a CrCl value
            crcl = float(scenario)
            # Determine category
            if crcl >= 60:
                category = "Normal"
            elif crcl >= 30:
                category = "Mild"
            elif crcl >= 15:
                category = "Moderate"
            else:
                category = "Severe"
        else:
            continue
        
        # Calculate eGFR (simplified)
        egfr = calculate_egfr_simplified(age, 1.0, sex)  # Using default SCr for estimation
        
        # For each indication
        for indication in indications_list:
            # Calculate adjusted dose
            adjusted_result = calculate_adjusted_dose(
                antibiotic_name,
                crcl,
                egfr=egfr,
                indication=indication
            )
            
            if "error" in adjusted_result:
                continue
            
            # Calculate detailed dose
            detailed = calculate_detailed_dose(
                antibiotic_name,
                weight,
                ibw,
                abw,
                crcl,
                indication=indication,
                is_pediatric=False,
                height_cm=height
            )
            
            if not detailed or not detailed.get('calculated_dose_mg'):
                continue
            
            # Map indication to Vietnamese
            indication_map = {
                "standard": "Chuẩn",
                "severe": "Nhiễm khuẩn nặng",
                "meningitis": "Viêm màng não"
            }
            
            results.append({
                "scenario": category,
                "crcl": crcl,
                "indication": indication_map.get(indication, indication),
                "indication_code": indication,
                "dose_mg": detailed['calculated_dose_mg'],
                "interval_hours": detailed.get('interval_hours', 0),
                "frequency": detailed.get('frequency', ''),
                "renal_adjustment": adjusted_result.get('adjustment', ''),
                "renal_category": adjusted_result.get('renal_category', 'normal')
            })
    
    return results


def create_dosing_chart(results_df, antibiotic_name):
    """
    Tạo bar chart cho dosing scenarios
    """
    if results_df.empty:
        return None
    
    # Group by scenario and indication
    fig = go.Figure()
    
    # Get unique indications
    indications = results_df['indication'].unique()
    scenarios = results_df['scenario'].unique()
    
    # Color map for scenarios
    color_map = {
        "Normal": "#4CAF50",
        "Mild": "#FFC107",
        "Moderate": "#FF9800",
        "Severe": "#F44336"
    }
    
    # Create bars for each indication
    for i, indication in enumerate(indications):
        indication_data = results_df[results_df['indication'] == indication]
        
        x_positions = []
        doses = []
        colors = []
        labels = []
        
        for scenario in scenarios:
            scenario_data = indication_data[indication_data['scenario'] == scenario]
            if not scenario_data.empty:
                x_positions.append(f"{scenario}\n(CrCl {scenario_data.iloc[0]['crcl']:.0f})")
                doses.append(scenario_data.iloc[0]['dose_mg'])
                colors.append(color_map.get(scenario, "#666"))
                labels.append(f"{scenario_data.iloc[0]['dose_mg']:.0f} mg")
        
        fig.add_trace(go.Bar(
            name=indication,
            x=x_positions,
            y=doses,
            marker_color=colors,
            text=labels,
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Liều: %{y:.0f} mg<br>Chỉ định: %{fullData.name}<extra></extra>'
        ))
    
    fig.update_layout(
        title=f"📊 So sánh Liều {antibiotic_name} Theo Scenarios",
        xaxis_title="Scenario (CrCl)",
        yaxis_title="Liều (mg)",
        barmode='group',
        height=500,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode='closest',
        template='plotly_white'
    )
    
    return fig


def create_interval_chart(results_df, antibiotic_name):
    """
    Tạo line chart cho dosing intervals
    """
    if results_df.empty:
        return None
    
    fig = go.Figure()
    
    # Get unique indications
    indications = results_df['indication'].unique()
    
    # Color map for indications
    color_map = {
        "Chuẩn": "#2196F3",
        "Nhiễm khuẩn nặng": "#F44336",
        "Viêm màng não": "#9C27B0"
    }
    
    # Order scenarios
    scenario_order = ["Normal", "Mild", "Moderate", "Severe"]
    
    for indication in indications:
        indication_data = results_df[results_df['indication'] == indication]
        
        x_values = []
        y_values = []
        
        for scenario in scenario_order:
            scenario_data = indication_data[indication_data['scenario'] == scenario]
            if not scenario_data.empty:
                x_values.append(scenario)
                y_values.append(scenario_data.iloc[0]['interval_hours'])
        
        if x_values:
            fig.add_trace(go.Scatter(
                name=indication,
                x=x_values,
                y=y_values,
                mode='lines+markers',
                line=dict(color=color_map.get(indication, "#666"), width=3),
                marker=dict(size=10),
                hovertemplate='<b>%{x}</b><br>Khoảng cách: %{y:.0f} giờ<br>Chỉ định: %{fullData.name}<extra></extra>'
            ))
    
    fig.update_layout(
        title=f"⏱️ Khoảng Cách Giữa Các Liều {antibiotic_name}",
        xaxis_title="Scenario",
        yaxis_title="Khoảng cách (giờ)",
        height=400,
        showlegend=True,
        hovermode='closest',
        template='plotly_white'
    )
    
    return fig


def export_to_csv(results_df, patient_info, antibiotic_name):
    """
    Tạo CSV string từ results và patient info
    """
    # Create export DataFrame
    export_data = results_df.copy()
    
    # Add patient info columns
    export_data.insert(0, 'Kháng sinh', antibiotic_name)
    export_data.insert(1, 'Cân nặng (kg)', patient_info.get('weight', ''))
    export_data.insert(2, 'Chiều cao (cm)', patient_info.get('height', ''))
    export_data.insert(3, 'Tuổi', patient_info.get('age', ''))
    export_data.insert(4, 'Giới tính', patient_info.get('sex', ''))
    export_data.insert(5, 'Ngày tính', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Rename columns for better readability
    export_data = export_data.rename(columns={
        'scenario': 'Scenario',
        'crcl': 'CrCl (mL/min)',
        'indication': 'Chỉ định',
        'dose_mg': 'Liều (mg)',
        'interval_hours': 'Khoảng cách (giờ)',
        'frequency': 'Tần suất',
        'renal_adjustment': 'Điều chỉnh thận',
        'renal_category': 'Phân loại thận'
    })
    
    return export_data.to_csv(index=False, encoding='utf-8-sig')


def render_scenario_dosing_calculator(antibiotic_name):
    """
    Render UI cho scenario dosing calculator với visual charts và export
    """
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        st.error(f"Không tìm thấy kháng sinh: {antibiotic_name}")
        return
    
    st.markdown("---")
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        margin: 15px 0;
    '>
        <h3 style='margin: 0; color: white;'>🧮 Tính liều cho nhiều trường hợp</h3>
        <p style='margin: 5px 0 0 0; color: rgba(255,255,255,0.9); font-size: 0.95em;'>
            Tính liều cho nhiều scenarios (CrCl khác nhau) và chỉ định trong một lần
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Patient input form
    st.markdown("### 📋 Thông tin bệnh nhân")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=10.0,
            max_value=200.0,
            value=70.0,
            step=1.0,
            key=f"scenario_weight_{antibiotic_name}"
        )
    
    with col2:
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=1.0,
            key=f"scenario_height_{antibiotic_name}"
        )
    
    with col3:
        age = st.number_input(
            "Tuổi",
            min_value=18,
            max_value=120,
            value=50,
            step=1,
            key=f"scenario_age_{antibiotic_name}"
        )
    
    with col4:
        sex = st.selectbox(
            "Giới tính",
            ["Nam", "Nữ"],
            key=f"scenario_sex_{antibiotic_name}"
        )
    
    # Check for imported CrCl/eGFR
    imported_crcl = st.session_state.get('patient_crcl', None)
    imported_egfr = st.session_state.get('patient_egfr', None)
    
    if imported_crcl:
        st.info(f"📥 CrCl đã import: {imported_crcl:.1f} mL/min (có thể thêm vào scenarios)")
    
    st.markdown("---")
    
    # Scenario selection
    st.markdown("### 🎯 Chọn scenarios (CrCl - Độ thanh thải creatinine)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Phân loại CrCl:**")
        scenario_normal = st.checkbox("CrCl ≥ 60 (Bình thường)", value=True, key=f"scenario_normal_{antibiotic_name}")
        scenario_mild = st.checkbox("CrCl 30-59 (Suy thận nhẹ)", value=True, key=f"scenario_mild_{antibiotic_name}")
        scenario_moderate = st.checkbox("CrCl 15-29 (Suy thận vừa)", value=True, key=f"scenario_moderate_{antibiotic_name}")
        scenario_severe = st.checkbox("CrCl < 15 (Suy thận nặng)", value=True, key=f"scenario_severe_{antibiotic_name}")
    
    with col2:
        st.markdown("**Chỉ định:**")
        indication_standard = st.checkbox("Chuẩn", value=True, key=f"indication_standard_{antibiotic_name}")
        indication_severe = st.checkbox("Nhiễm khuẩn nặng", value=False, key=f"indication_severe_{antibiotic_name}")
        indication_meningitis = st.checkbox("Viêm màng não", value=False, key=f"indication_meningitis_{antibiotic_name}")
    
    # Build scenarios list
    scenarios_list = []
    if scenario_normal:
        scenarios_list.append({"crcl": 90, "category": "Normal"})
    if scenario_mild:
        scenarios_list.append({"crcl": 45, "category": "Mild"})
    if scenario_moderate:
        scenarios_list.append({"crcl": 22, "category": "Moderate"})
    if scenario_severe:
        scenarios_list.append({"crcl": 10, "category": "Severe"})
    
    # Add imported CrCl if available
    if imported_crcl and st.checkbox("Thêm CrCl đã import vào scenarios", key=f"add_imported_{antibiotic_name}"):
        # Determine category
        if imported_crcl >= 60:
            cat = "Normal"
        elif imported_crcl >= 30:
            cat = "Mild"
        elif imported_crcl >= 15:
            cat = "Moderate"
        else:
            cat = "Severe"
        scenarios_list.append({"crcl": imported_crcl, "category": f"{cat} (Import)"})
    
    # Build indications list
    indications_list = []
    if indication_standard:
        indications_list.append("standard")
    if indication_severe:
        indications_list.append("severe")
    if indication_meningitis:
        indications_list.append("meningitis")
    
    if not scenarios_list or not indications_list:
        st.warning("⚠️ Vui lòng chọn ít nhất 1 scenario và 1 chỉ định")
        return
    
    # Calculate button
    if st.button("🧮 Tính liều cho tất cả scenarios", type="primary", use_container_width=True, key=f"calc_scenarios_{antibiotic_name}"):
        with st.spinner("Đang tính liều cho tất cả scenarios..."):
            results = calculate_scenarios(
                antibiotic_name,
                weight,
                height,
                age,
                sex,
                scenarios_list,
                indications_list
            )
            
            if results:
                from .database_display import _make_safe_session_key
                safe_ab_name = _make_safe_session_key("scenario_results", antibiotic_name)
                st.session_state[safe_ab_name] = results
                safe_patient_key = _make_safe_session_key("scenario_patient_info", antibiotic_name)
                st.session_state[safe_patient_key] = {
                    'weight': weight,
                    'height': height,
                    'age': age,
                    'sex': sex
                }
                st.rerun()
            else:
                st.error("Không thể tính liều. Vui lòng kiểm tra lại thông tin.")
    
    # Display results
    from .database_display import _make_safe_session_key
    safe_results_key = _make_safe_session_key("scenario_results", antibiotic_name)
    safe_patient_key = _make_safe_session_key("scenario_patient_info", antibiotic_name)
    
    if safe_results_key in st.session_state:
        results = st.session_state.get(safe_results_key, None)
        if not results:
            return
        patient_info = st.session_state.get(safe_patient_key, {})
        
        if not results:
            st.warning("Không có kết quả để hiển thị")
            return
        
        # Convert to DataFrame
        results_df = pd.DataFrame(results)
        
        st.markdown("---")
        st.markdown("### 📊 Kết quả")
        
        # Display table
        display_df = results_df[['scenario', 'crcl', 'indication', 'dose_mg', 'interval_hours', 'renal_adjustment']].copy()
        display_df = display_df.rename(columns={
            'scenario': 'Scenario',
            'crcl': 'CrCl (mL/min)',
            'indication': 'Chỉ định',
            'dose_mg': 'Liều (mg)',
            'interval_hours': 'Khoảng cách (giờ)',
            'renal_adjustment': 'Điều chỉnh thận'
        })
        
        # Format for display
        display_df['CrCl (mL/min)'] = display_df['CrCl (mL/min)'].apply(lambda x: f"{x:.1f}")
        display_df['Liều (mg)'] = display_df['Liều (mg)'].apply(lambda x: f"{x:.0f}")
        display_df['Khoảng cách (giờ)'] = display_df['Khoảng cách (giờ)'].apply(lambda x: f"{x:.0f}" if x > 0 else "N/A")
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # Visual Charts
        st.markdown("---")
        st.markdown("### 📈 Biểu Đồ Trực Quan")
        
        # Dosing Chart
        dosing_chart = create_dosing_chart(results_df, antibiotic_name)
        if dosing_chart:
            st.plotly_chart(dosing_chart, use_container_width=True)
        
        # Interval Chart
        interval_chart = create_interval_chart(results_df, antibiotic_name)
        if interval_chart:
            st.plotly_chart(interval_chart, use_container_width=True)
        
        # Export to CSV
        st.markdown("---")
        st.markdown("### 📥 Export")
        
        csv_data = export_to_csv(results_df, patient_info, antibiotic_name)
        st.download_button(
            label="📥 Tải Xuống CSV",
            data=csv_data,
            file_name=f"dosing_scenarios_{antibiotic_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            key=f"export_csv_{antibiotic_name}"
        )
        
        # Print-friendly view
        st.markdown("---")
        st.markdown("### 🖨️ Bản In")
        
        with st.expander("📄 Xem Bản In", expanded=False):
            st.markdown("""
            <style>
            @media print {
                .stApp { visibility: hidden; }
                .print-content { visibility: visible; position: absolute; left: 0; top: 0; width: 100%; }
            }
            </style>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="print-content">
            <h2>Báo Cáo Tính Liều: {antibiotic_name}</h2>
            <p><strong>Ngày:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            <p><strong>Bệnh nhân:</strong> {patient_info.get('sex', '')}, {patient_info.get('age', '')} tuổi, 
            {patient_info.get('weight', '')} kg, {patient_info.get('height', '')} cm</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.dataframe(display_df, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            st.markdown("**Ghi chú:** In trang này để lưu trữ hoặc chia sẻ với đồng nghiệp.")
        
        # Clear button
        if st.button("🗑️ Xóa Kết quả", key=f"clear_scenario_{antibiotic_name}"):
            keys_to_remove = [
                f"scenario_results_{antibiotic_name}",
                f"scenario_patient_info_{antibiotic_name}"
            ]
            for key in keys_to_remove:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

