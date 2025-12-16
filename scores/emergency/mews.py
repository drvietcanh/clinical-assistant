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
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


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
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mews':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **MEWS** là hệ thống cảnh báo sớm để phát hiện tình trạng xấu đi của bệnh nhân trong khoa.
    Sử dụng 5 thông số sinh tồn để tính điểm và phân loại nguy cơ.
    """)
    
    st.markdown("---")
    
    # Input section
    col1, col2 = st.columns([2, 1])
    
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
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="mews",
            calculator_name="MEWS",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
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
        
        # Map color names to hex
        color_map = {
            "success": "#28a745",  # green
            "warning": "#fd7e14",  # orange
            "error": "#dc3545"     # red
        }
        icon_map = {
            "success": "✅",
            "warning": "⚠️",
            "error": "🚨"
        }
        score_color = color_map[result["color"]]
        score_icon = icon_map[result["color"]]
        
        # Use render_score_result for main score display
        render_score_result(
            title="MEWS Score",
            score=result['total_score'],
            interpretation=f"{result['risk_category']} - {result['action']}",
            mortality=None,
            color=score_color,
            icon=score_icon,
            size="large"
        )
        
        # Use render_score_breakdown for component scores
        render_score_breakdown(
            title="Điểm Từng Thông Số",
            subscores={
                "Huyết áp tâm thu": result['sbp_score'],
                "Nhịp tim": result['hr_score'],
                "Nhịp thở": result['resp_score'],
                "Nhiệt độ": result['temp_score'],
                "AVPU": result['avpu_score']
            },
            total_score=result['total_score']
        )
        
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
        st.markdown("### 🎯 Phân loại Nguy cơ")
        
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
        
        # Prepare inputs and results for export/history
        inputs_dict = {
            "Systolic BP": f"{sbp:.0f} mmHg",
            "Heart Rate": f"{hr:.0f} bpm",
            "Respiratory Rate": f"{resp_rate:.0f} /min",
            "Temperature": f"{temp:.1f}°C",
            "AVPU": avpu
        }
        
        results_dict = {
            "MEWS Score": f"{result['total_score']} điểm",
            "Risk Category": result['risk_category'],
            "Action": result['action'],
            "Components": f"SBP:{result['sbp_score']} HR:{result['hr_score']} RR:{result['resp_score']} Temp:{result['temp_score']} AVPU:{result['avpu_score']}"
        }
        
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        render_export_section(
            title=f"MEWS Score = {result['total_score']} điểm",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="MEWS",
            filename="mews_result"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mews",
            calculator_name="MEWS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="mews",
            calculator_name="MEWS",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="mews", show_actions=True)
        
        # References section
        references = get_references("MEWS")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        else:
            # Fallback to manual references if not in config
            st.markdown("---")
            st.markdown("### 📚 Tài liệu tham khảo")
            st.markdown("""
            1. **Subbe CP, et al.** Validation of a modified Early Warning Score in medical admissions.
               QJM. 2001;94(10):521-526.
            
            2. **Morgan RJ, et al.** An early warning scoring system for detecting developing critical illness.
               Clin Intensive Care. 1997;8(2):100.
            
            3. **Royal College of Physicians.** National Early Warning Score (NEWS) 2.
               RCP, 2017.
            """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("MEWS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.caption("⚠️ MEWS chỉ là công cụ hỗ trợ. Đánh giá lâm sàng toàn diện vẫn là quan trọng nhất.")


















