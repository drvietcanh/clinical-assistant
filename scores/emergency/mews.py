"""
MEWS - Modified Early Warning Score
====================================
Early warning system for detecting clinical deterioration in ward patients

Reference:
- Subbe CP, et al. Validation of a modified Early Warning Score in medical admissions.
  QJM. 2001;94(10):521-526.
- Morgan RJ, et al. An early warning scoring system for detecting developing critical illness.
  Clin Intensive Care. 1997;8(2):100.

MEWS Components (5 parameters):
1. Huyết áp tâm thu
2. Nhịp tim
3. Nhịp thở
4. Temperature
5. AVPU (Alert/Verbal/Pain/Unresponsive)

Score: 0-14 points
- 0-4: Low risk
- 5-6: Medium risk
- ≥7: High risk

Clinical Utility:
- Early detection of clinical deterioration
- Triggers appropriate clinical response
- Used in general wards
"""

import streamlit as st
from utils.formatters import format_number
from scores.utils.validation import (
    validate_blood_pressure,
    validate_heart_rate,
    validate_respiratory_rate,
    validate_temperature
)


def get_sbp_score(sbp: float) -> int:
    """Systolic BP scoring"""
    if sbp < 70:
        return 3
    elif sbp < 80:
        return 2
    elif sbp <= 100:
        return 1
    elif sbp <= 199:
        return 0
    else:
        return 2


def get_heart_rate_score(hr: float) -> int:
    """Heart rate scoring"""
    if hr < 40:
        return 2
    elif hr <= 50:
        return 1
    elif hr <= 100:
        return 0
    elif hr <= 110:
        return 1
    elif hr <= 130:
        return 2
    else:
        return 3


def get_resp_rate_score(resp_rate: float) -> int:
    """Respiratory rate scoring"""
    if resp_rate < 9:
        return 2
    elif resp_rate <= 14:
        return 0
    elif resp_rate <= 20:
        return 1
    elif resp_rate <= 29:
        return 2
    else:
        return 3


def get_temperature_score(temp: float) -> int:
    """Temperature scoring (Celsius)"""
    if temp < 35:
        return 2
    elif temp <= 38.4:
        return 0
    else:
        return 2


def get_avpu_score(avpu: str) -> int:
    """AVPU scoring"""
    avpu_map = {
        "Alert": 0,
        "Verbal": 1,
        "Pain": 2,
        "Unresponsive": 3
    }
    return avpu_map.get(avpu, 0)


def calculate_mews(sbp: float, hr: float, resp_rate: float, temp: float, avpu: str) -> dict:
    """
    Calculate MEWS Score
    
    Args:
        sbp: Systolic blood pressure (mmHg)
        hr: Heart rate (bpm)
        resp_rate: Respiratory rate (per minute)
        temp: Temperature (°C)
        avpu: AVPU status (Alert/Verbal/Pain/Unresponsive)
    
    Returns:
        dict with total score, risk category, and recommendations
    """
    sbp_score = get_sbp_score(sbp)
    hr_score = get_heart_rate_score(hr)
    resp_score = get_resp_rate_score(resp_rate)
    temp_score = get_temperature_score(temp)
    avpu_score = get_avpu_score(avpu)
    
    total_score = sbp_score + hr_score + resp_score + temp_score + avpu_score
    
    # Risk category
    if total_score <= 4:
        risk = "Thấp"
        color = "success"
        action = "Theo dõi định kỳ (mỗi 12h)"
    elif total_score <= 6:
        risk = "Trung bình"
        color = "warning"
        action = "Theo dõi sát (mỗi 4-6h), cân nhắc chuyển HDU"
    else:
        risk = "Cao"
        color = "error"
        action = "Khẩn cấp: Đánh giá ngay, cân nhắc chuyển ICU/HDU"
    
    return {
        "total_score": total_score,
        "sbp_score": sbp_score,
        "hr_score": hr_score,
        "resp_score": resp_score,
        "temp_score": temp_score,
        "avpu_score": avpu_score,
        "risk_category": risk,
        "color": color,
        "action": action
    }


def render():
    """MEWS Score Calculator"""
    st.subheader("🚨 MEWS - Modified Early Warning Score")
    st.caption("Early Warning System for Clinical Deterioration Detection")
    
    st.info("""
    **MEWS** là hệ thống cảnh báo sớm để phát hiện tình trạng xấu đi của bệnh nhân trong khoa.
    Sử dụng 5 thông số sinh tồn để tính điểm và phân loại nguy cơ.
    """)
    
    st.markdown("---")
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        sbp = st.number_input(
            "**Huyết áp tâm thu (mmHg):**",
            min_value=0.0,
            max_value=300.0,
            value=120.0,
            step=1.0,
            key="mews_sbp"
        )
        
        hr = st.number_input(
            "**Nhịp tim (bpm):**",
            min_value=0.0,
            max_value=300.0,
            value=80.0,
            step=1.0,
            key="mews_hr"
        )
        
        resp_rate = st.number_input(
            "**Nhịp thở (lần/phút):**",
            min_value=0.0,
            max_value=60.0,
            value=16.0,
            step=1.0,
            key="mews_resp"
        )
    
    with col2:
        temp = st.number_input(
            "**Nhiệt độ (°C):**",
            min_value=30.0,
            max_value=45.0,
            value=37.0,
            step=0.1,
            key="mews_temp"
        )
        
        avpu = st.selectbox(
            "**Mức độ ý thức (AVPU):**",
            ["Alert", "Verbal", "Pain", "Unresponsive"],
            key="mews_avpu",
            help="Alert: Tỉnh táo, Verbal: Đáp ứng với lời nói, Pain: Đáp ứng với đau, Unresponsive: Không đáp ứng"
        )
    
    st.markdown("---")
    
    # Calculate
    if st.button("**Tính MEWS Score**", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(sbp_error)
        
        is_valid_hr, hr_error = validate_heart_rate(hr)
        if not is_valid_hr:
            validation_errors.append(hr_error)
        
        is_valid_rr, rr_error = validate_respiratory_rate(resp_rate)
        if not is_valid_rr:
            validation_errors.append(rr_error)
        
        is_valid_temp, temp_error = validate_temperature(temp)
        if not is_valid_temp:
            validation_errors.append(temp_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        result = calculate_mews(sbp, hr, resp_rate, temp, avpu)
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Total score with color
        if result["color"] == "success":
            st.success(f"## MEWS Score: {result['total_score']} điểm")
        elif result["color"] == "warning":
            st.warning(f"## MEWS Score: {result['total_score']} điểm")
        else:
            st.error(f"## MEWS Score: {result['total_score']} điểm")
        
        st.markdown(f"**Nguy cơ:** {result['risk_category']}")
        st.markdown(f"**Hành động:** {result['action']}")
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết Điểm số")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Huyết áp", f"{result['sbp_score']}", help=f"SBP: {format_number(sbp)} mmHg")
        
        with col2:
            st.metric("Nhịp tim", f"{result['hr_score']}", help=f"HR: {format_number(hr)} bpm")
        
        with col3:
            st.metric("Nhịp thở", f"{result['resp_score']}", help=f"RR: {format_number(resp_rate)} /phút")
        
        with col4:
            st.metric("Nhiệt độ", f"{result['temp_score']}", help=f"Temp: {format_number(temp)} °C")
        
        with col5:
            st.metric("AVPU", f"{result['avpu_score']}", help=f"AVPU: {avpu}")
        
        st.markdown("---")
        st.markdown("### 📖 Bảng Điểm MEWS")
        
        # Scoring table
        import pandas as pd
        
        scoring_data = {
            "Thông số": [
                "Huyết áp tâm thu (mmHg)",
                "Nhịp tim (bpm)",
                "Nhịp thở (/phút)",
                "Nhiệt độ (°C)",
                "AVPU"
            ],
            "0 điểm": [
                "101-199",
                "51-100",
                "9-14",
                "35.0-38.4",
                "Alert"
            ],
            "1 điểm": [
                "81-100",
                "41-50 hoặc 101-110",
                "15-20",
                "-",
                "Verbal"
            ],
            "2 điểm": [
                "71-80",
                "-",
                "<9 hoặc 21-29",
                "<35.0 hoặc ≥38.5",
                "Pain"
            ],
            "3 điểm": [
                "<70",
                "<40 hoặc >130",
                "≥30",
                "-",
                "Unresponsive"
            ]
        }
        
        st.dataframe(pd.DataFrame(scoring_data), use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("### 🎯 Phân Loại Nguy cơ")
        
        risk_data = {
            "Điểm": ["0-4", "5-6", "≥7"],
            "Nguy cơ": ["Thấp", "Trung bình", "Cao"],
            "Hành động": [
                "Theo dõi định kỳ (mỗi 12h)",
                "Theo dõi sát (mỗi 4-6h), cân nhắc chuyển HDU",
                "Khẩn cấp: Đánh giá ngay, cân nhắc chuyển ICU/HDU"
            ]
        }
        
        st.dataframe(pd.DataFrame(risk_data), use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("### 📚 Tài Liệu Tham Khảo")
        
        st.markdown("""
        1. **Subbe CP, et al.** Validation of a modified Early Warning Score in medical admissions.
           QJM. 2001;94(10):521-526.
        
        2. **Morgan RJ, et al.** An early warning scoring system for detecting developing critical illness.
           Clin Intensive Care. 1997;8(2):100.
        
        3. **Royal College of Physicians.** National Early Warning Score (NEWS) 2.
           RCP, 2017.
        """)
        
        st.caption("⚠️ MEWS chỉ là công cụ hỗ trợ. Đánh giá lâm sàng toàn diện vẫn là quan trọng nhất.")


















