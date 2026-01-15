"""
Advanced Analytics for Critical Care
Trend prediction, risk scoring, outcome prediction
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from components.ui.results import render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def calculate_trend_prediction(data: pd.DataFrame, parameter: str, hours_ahead: int = 6) -> Dict:
    """
    Predict future trend of a parameter using linear regression
    
    Args:
        data: DataFrame with timestamp and parameter columns
        parameter: Parameter name to predict
        hours_ahead: Hours to predict ahead
    
    Returns:
        Dictionary with prediction and confidence
    """
    if len(data) < 3:
        return {
            "predicted_value": None,
            "trend": "insufficient_data",
            "confidence": 0,
            "message": "Không đủ dữ liệu để dự đoán"
        }
    
    # Simple linear regression
    x = np.arange(len(data))
    y = data[parameter].values
    
    # Remove NaN values
    mask = ~np.isnan(y)
    x_clean = x[mask]
    y_clean = y[mask]
    
    if len(x_clean) < 2:
        return {
            "predicted_value": None,
            "trend": "insufficient_data",
            "confidence": 0,
            "message": "Không đủ dữ liệu hợp lệ"
        }
    
    # Linear regression
    coeffs = np.polyfit(x_clean, y_clean, 1)
    slope = coeffs[0]
    intercept = coeffs[1]
    
    # Predict future value
    future_x = len(data) + (hours_ahead * 2)  # Assuming 2 data points per hour
    predicted_value = slope * future_x + intercept
    
    # Calculate trend
    if abs(slope) < 0.1:
        trend = "stable"
        trend_text = "Ổn định"
    elif slope > 0:
        trend = "increasing"
        trend_text = "Tăng"
    else:
        trend = "decreasing"
        trend_text = "Giảm"
    
    # Calculate confidence (simplified - based on R²)
    y_pred = slope * x_clean + intercept
    ss_res = np.sum((y_clean - y_pred) ** 2)
    ss_tot = np.sum((y_clean - np.mean(y_clean)) ** 2)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    confidence = max(0, min(100, int(r_squared * 100)))
    
    return {
        "predicted_value": predicted_value,
        "trend": trend,
        "trend_text": trend_text,
        "confidence": confidence,
        "slope": slope,
        "message": f"Dự đoán {hours_ahead}h: {predicted_value:.1f} ({trend_text}, độ tin cậy: {confidence}%)"
    }


def calculate_risk_score(patient_data: Dict) -> Dict:
    """
    Calculate overall risk score for a patient
    
    Args:
        patient_data: Dictionary with patient parameters
    
    Returns:
        Dictionary with risk score and breakdown
    """
    risk_factors = []
    total_risk = 0
    
    # Ventilator risk
    vent_data = patient_data.get('ventilator', {})
    if vent_data.get('plateau', 0) > 30:
        risk_factors.append({"factor": "Plateau pressure cao", "score": 3})
        total_risk += 3
    elif vent_data.get('plateau', 0) > 28:
        risk_factors.append({"factor": "Plateau pressure tăng", "score": 1})
        total_risk += 1
    
    driving_pressure = vent_data.get('plateau', 0) - vent_data.get('peep', 0)
    if driving_pressure > 15:
        risk_factors.append({"factor": "Driving pressure cao", "score": 2})
        total_risk += 2
    
    # ABG risk
    abg_data = patient_data.get('abg', {})
    if abg_data.get('pf_ratio', 0) < 100:
        risk_factors.append({"factor": "P/F ratio rất thấp", "score": 3})
        total_risk += 3
    elif abg_data.get('pf_ratio', 0) < 200:
        risk_factors.append({"factor": "P/F ratio thấp", "score": 1})
        total_risk += 1
    
    if abg_data.get('ph', 7.4) < 7.20:
        risk_factors.append({"factor": "pH rất thấp", "score": 2})
        total_risk += 2
    
    # Fluid risk
    fluid_data = patient_data.get('fluid', {})
    if abs(fluid_data.get('balance', 0)) > 2000:
        risk_factors.append({"factor": "Mất cân bằng dịch nặng", "score": 2})
        total_risk += 2
    
    # Determine risk level
    if total_risk >= 6:
        risk_level = "high"
        risk_text = "Nguy cơ cao"
        risk_color = "error"
    elif total_risk >= 3:
        risk_level = "medium"
        risk_text = "Nguy cơ trung bình"
        risk_color = "warning"
    else:
        risk_level = "low"
        risk_text = "Nguy cơ thấp"
        risk_color = "success"
    
    return {
        "total_risk": total_risk,
        "risk_level": risk_level,
        "risk_text": risk_text,
        "risk_color": risk_color,
        "risk_factors": risk_factors
    }


def predict_outcome(patient_data: Dict, days_in_icu: int = 0) -> Dict:
    """
    Predict patient outcome (simplified model)
    
    Args:
        patient_data: Dictionary with patient parameters
        days_in_icu: Days already in ICU
    
    Returns:
        Dictionary with outcome prediction
    """
    # Simplified prediction model
    # In real implementation, would use ML models
    
    risk_score_data = calculate_risk_score(patient_data)
    total_risk = risk_score_data['total_risk']
    
    # Base mortality risk
    base_mortality = 0.15  # 15% baseline
    
    # Adjust based on risk factors
    mortality_risk = base_mortality + (total_risk * 0.05)
    mortality_risk = min(0.95, max(0.05, mortality_risk))  # Clamp between 5% and 95%
    
    # Adjust based on days in ICU (longer stay = better if stable)
    if days_in_icu > 7 and total_risk < 3:
        mortality_risk *= 0.8  # Reduce risk if stable for >7 days
    
    # Determine outcome
    if mortality_risk < 0.20:
        outcome = "favorable"
        outcome_text = "Tiên lượng tốt"
        outcome_color = "success"
    elif mortality_risk < 0.50:
        outcome = "guarded"
        outcome_text = "Tiên lượng dè dặt"
        outcome_color = "warning"
    else:
        outcome = "poor"
        outcome_text = "Tiên lượng xấu"
        outcome_color = "error"
    
    return {
        "mortality_risk": mortality_risk,
        "survival_probability": 1 - mortality_risk,
        "outcome": outcome,
        "outcome_text": outcome_text,
        "outcome_color": outcome_color,
        "days_in_icu": days_in_icu
    }


def render_analytics_dashboard():
    """Render analytics dashboard"""
    st.header("📊 Advanced Analytics")
    st.caption("Phân tích xu hướng, đánh giá nguy cơ, và dự đoán kết quả")
    
    tabs = st.tabs([
        "📈 Trend Prediction",
        "⚠️ Risk Scoring",
        "🔮 Outcome Prediction",
        "📊 Comparative Analysis"
    ])
    
    # Tab 1: Trend Prediction
    with tabs[0]:
        st.markdown("### 📈 Dự đoán xu hướng")
        
        if 'patient_data' in st.session_state:
            # Get historical data (simulated)
            st.info("💡 Tính năng này yêu cầu dữ liệu lịch sử. Hiện tại sử dụng dữ liệu mẫu.")
            
            # Generate sample data
            dates = pd.date_range(end=datetime.now(), periods=24, freq='H')
            sample_data = pd.DataFrame({
                'timestamp': dates,
                'plateau_pressure': 25 + np.random.normal(0, 2, 24),
                'pf_ratio': 200 + np.random.normal(0, 20, 24),
                'compliance': 30 + np.random.normal(0, 3, 24)
            })
            
            parameter = st.selectbox(
                "Chọn thông số:",
                ['plateau_pressure', 'pf_ratio', 'compliance'],
                format_func=lambda x: {
                    'plateau_pressure': 'Plateau Pressure',
                    'pf_ratio': 'P/F Ratio',
                    'compliance': 'Compliance'
                }[x],
                key="trend_param"
            )
            
            hours_ahead = st.slider("Dự đoán trước (giờ):", 1, 24, 6, key="trend_hours")
            
            prediction = calculate_trend_prediction(sample_data, parameter, hours_ahead)
            
            if prediction['predicted_value']:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    render_result_card(
                        title="Giá trị dự đoán",
                        value=f"{prediction['predicted_value']:.1f}",
                        unit="",
                        color=prediction.get('trend', 'stable'),
                        subtitle=f"Sau {hours_ahead} giờ"
                    )
                
                with col2:
                    trend_colors = {
                        "increasing": "warning",
                        "decreasing": "success",
                        "stable": "info"
                    }
                    render_result_card(
                        title="Xu hướng",
                        value=prediction['trend_text'],
                        unit="",
                        color=trend_colors.get(prediction['trend'], 'info'),
                        subtitle=""
                    )
                
                with col3:
                    render_result_card(
                        title="Độ tin cậy",
                        value=f"{prediction['confidence']}%",
                        unit="",
                        color="info",
                        subtitle=""
                    )
                
                st.info(prediction['message'])
                
                # Show trend chart
                st.markdown("### 📊 Biểu đồ xu hướng")
                chart_data = sample_data.set_index('timestamp')[parameter]
                st.line_chart(chart_data, height=300)
            else:
                st.warning(prediction['message'])
        else:
            st.info("Chưa có dữ liệu bệnh nhân. Vui lòng nhập thông tin ở Patient Dashboard.")
    
    # Tab 2: Risk Scoring
    with tabs[1]:
        st.markdown("### ⚠️ Đánh giá nguy cơ")
        
        if 'patient_data' in st.session_state:
            patient_data = st.session_state['patient_data']
            risk_data = calculate_risk_score(patient_data)
            
            col1, col2 = st.columns(2)
            
            with col1:
                render_result_card(
                    title="Risk Score",
                    value=str(risk_data['total_risk']),
                    unit="",
                    color=risk_data['risk_color'],
                    subtitle=risk_data['risk_text']
                )
            
            with col2:
                st.markdown("### Yếu tố nguy cơ")
                if risk_data['risk_factors']:
                    for factor in risk_data['risk_factors']:
                        st.markdown(f"- **{factor['factor']}** (Score: {factor['score']})")
                else:
                    st.success("✅ Không có yếu tố nguy cơ đáng kể")
            
            # Risk breakdown
            if risk_data['risk_factors']:
                st.markdown("---")
                st.markdown("### 📋 Chi tiết nguy cơ")
                
                risk_df = pd.DataFrame(risk_data['risk_factors'])
                st.dataframe(risk_df, use_container_width=True, hide_index=True)
        else:
            st.info("Chưa có dữ liệu bệnh nhân.")
    
    # Tab 3: Outcome Prediction
    with tabs[2]:
        st.markdown("### 🔮 Dự đoán kết quả")
        
        if 'patient_data' in st.session_state:
            patient_data = st.session_state['patient_data']
            
            days_in_icu = st.number_input(
                "Số ngày trong ICU:",
                min_value=0,
                max_value=365,
                value=3,
                key="outcome_days"
            )
            
            outcome = predict_outcome(patient_data, days_in_icu)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                render_result_card(
                    title="Tỷ lệ tử vong",
                    value=f"{outcome['mortality_risk']*100:.1f}%",
                    unit="",
                    color=outcome['outcome_color'],
                    subtitle="Dự đoán"
                )
            
            with col2:
                render_result_card(
                    title="Tỷ lệ sống",
                    value=f"{outcome['survival_probability']*100:.1f}%",
                    unit="",
                    color="success",
                    subtitle="Dự đoán"
                )
            
            with col3:
                render_result_card(
                    title="Tiên lượng",
                    value=outcome['outcome_text'],
                    unit="",
                    color=outcome['outcome_color'],
                    subtitle=""
                )
            
            st.markdown("---")
            st.warning("""
            **Lưu ý:** Đây là mô hình dự đoán đơn giản. Trong thực tế, cần sử dụng 
            các mô hình ML phức tạp hơn với dữ liệu lớn và validation.
            """)
        else:
            st.info("Chưa có dữ liệu bệnh nhân.")
    
    # Tab 4: Comparative Analysis
    with tabs[3]:
        st.markdown("### 📊 Phân tích so sánh")
        
        st.info("""
        **Tính năng đang phát triển:**
        - So sánh giữa các bệnh nhân
        - So sánh với dữ liệu lịch sử
        - Benchmark với guidelines
        - Population analysis
        """)
        
        if 'multi_patients' in st.session_state and st.session_state['multi_patients']:
            patients = st.session_state['multi_patients']
            
            st.markdown("#### So sánh giữa các bệnh nhân")
            
            # Create comparison table
            comparison_data = []
            for patient in patients:
                comparison_data.append({
                    "Mã BN": patient.get('id', 'N/A'),
                    "MAP": patient.get('map', 0),
                    "RR": patient.get('rr', 0),
                    "SpO2": patient.get('spO2', 0)
                })
            
            if comparison_data:
                df = pd.DataFrame(comparison_data)
                st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Chưa có dữ liệu nhiều bệnh nhân để so sánh.")
