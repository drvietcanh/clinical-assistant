"""
NEWS2 Score (National Early Warning Score 2)
==============================================

A tool for assessing the severity of illness and prompting 
clinical response. Used daily in wards for early detection 
of clinical deterioration.

Reference:
- Royal College of Physicians (RCP) 2017 NEWS2 guideline
- Category-based response thresholds
- Enhanced SpO2 scale for Type 2 respiratory failure

NEWS2 Components (7 parameters):
1. Respiration Rate
2. Độ bão hòa oxy (SpO2)
3. Huyết áp tâm thu
4. Pulse Rate
5. Level of Consciousness (Alert/Verbal/Pain/Unresponsive)
6. Temperature
7. Supplemental Oxygen (yes/no)

Score: Variable points per parameter → Total: 0-20 points

Clinical Utility:
- Early warning system for ward patients
- Triggers appropriate clinical response
- Category-based action plan
- Used daily in clinical practice
"""

import streamlit as st
from scores.utils.validation import (
    validate_blood_pressure,
    validate_heart_rate,
    validate_respiratory_rate,
    validate_temperature,
    validate_lab_value
)
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def get_respiration_score(resp_rate: float) -> int:
    """Respiratory rate scoring"""
    if resp_rate <= 8:
        return 3
    elif resp_rate <= 11:
        return 1
    elif resp_rate <= 20:
        return 0
    elif resp_rate <= 24:
        return 2
    else:
        return 3


def get_oxygen_saturation_score(spo2: float, use_supplemental_oxygen: bool, 
                                 has_type2_respiratory_failure: bool = False) -> int:
    """
    Oxygen saturation scoring with Type 2 respiratory failure scale
    
    Type 2 respiratory failure: Use different SpO2 scale
    Normal: Use standard scale
    
    Note: +2 points if supplemental oxygen required (capped at 3)
    """
    base_score = 0
    
    if has_type2_respiratory_failure:
        # Type 2 respiratory failure scale
        if spo2 <= 83:
            base_score = 3
        elif spo2 <= 85:
            base_score = 2
        elif spo2 <= 87:
            base_score = 1
        elif spo2 <= 91:
            base_score = 0
        elif spo2 <= 93:
            base_score = 1
        elif spo2 <= 95:
            base_score = 2
        else:
            base_score = 3
    else:
        # Standard scale
        if spo2 <= 91:
            base_score = 3
        elif spo2 <= 93:
            base_score = 2
        elif spo2 <= 95:
            base_score = 1
        else:
            base_score = 0
    
    # Add 2 points if supplemental oxygen required (capped at 3)
    if use_supplemental_oxygen:
        return min(base_score + 2, 3)
    
    return base_score


def get_blood_pressure_score(systolic_bp: float) -> int:
    """Systolic blood pressure scoring"""
    if systolic_bp <= 90:
        return 3
    elif systolic_bp <= 100:
        return 2
    elif systolic_bp <= 110:
        return 1
    elif systolic_bp <= 219:
        return 0
    else:
        return 3


def get_pulse_rate_score(pulse_rate: float) -> int:
    """Pulse rate scoring"""
    if pulse_rate <= 40:
        return 3
    elif pulse_rate <= 50:
        return 1
    elif pulse_rate <= 90:
        return 0
    elif pulse_rate <= 110:
        return 1
    elif pulse_rate <= 130:
        return 2
    else:
        return 3


def get_consciousness_score(consciousness: str) -> int:
    """Level of consciousness scoring"""
    if consciousness in ["Alert", "alert"]:
        return 0
    elif consciousness in ["Verbal", "verbal", "V"]:
        return 3
    elif consciousness in ["Pain", "pain", "P"]:
        return 3
    elif consciousness in ["Unresponsive", "unresponsive", "U"]:
        return 3
    else:
        return 0


def get_temperature_score(temperature: float, unit: str = "C") -> int:
    """Temperature scoring (Celsius or Fahrenheit)"""
    if unit.upper() == "F":
        # Convert Fahrenheit to Celsius
        temperature = (temperature - 32) * 5 / 9
    
    if temperature <= 35.0:
        return 3
    elif temperature <= 36.0:
        return 1
    elif temperature <= 38.0:
        return 0
    elif temperature <= 39.0:
        return 1
    else:
        return 2


def get_supplemental_oxygen_score(use_supplemental_oxygen: bool) -> int:
    """Supplemental oxygen scoring"""
    return 2 if use_supplemental_oxygen else 0


def calculate_news2(
    resp_rate: float,
    spo2: float,
    systolic_bp: float,
    pulse_rate: float,
    consciousness: str,
    temperature: float,
    use_supplemental_oxygen: bool,
    has_type2_respiratory_failure: bool = False,
    temp_unit: str = "C"
) -> dict:
    """
    Calculate NEWS2 Score
    
    Args:
        resp_rate: Respiratory rate (/min)
        spo2: Oxygen saturation (%)
        systolic_bp: Systolic blood pressure (mmHg)
        pulse_rate: Pulse/heart rate (/min)
        consciousness: Level of consciousness (Alert/Verbal/Pain/Unresponsive)
        temperature: Body temperature (°C or °F)
        use_supplemental_oxygen: Whether patient requires supplemental oxygen
        has_type2_respiratory_failure: Whether patient has Type 2 respiratory failure
        temp_unit: Temperature unit ("C" or "F")
    
    Returns:
        Dictionary containing NEWS2 score, subscores, category, and action plan
    """
    
    subscores = {}
    details = []
    
    # 1. Respiration Rate
    resp_score = get_respiration_score(resp_rate)
    subscores['respiration'] = resp_score
    details.append(f"**Nhịp thở:** {resp_rate:.0f} /min → {resp_score} điểm")
    
    # 2. Độ bão hòa oxy
    spo2_score = get_oxygen_saturation_score(spo2, use_supplemental_oxygen, has_type2_respiratory_failure)
    subscores['oxygen_saturation'] = spo2_score
    scale_note = " (thang Type 2 RF)" if has_type2_respiratory_failure else ""
    if use_supplemental_oxygen:
        # Calculate base score without oxygen
        base_spo2 = get_oxygen_saturation_score(spo2, False, has_type2_respiratory_failure)
        details.append(f"**SpO₂:** {spo2:.0f}%{scale_note} → {base_spo2} điểm")
        details.append(f"  → +2 điểm vì cần oxy hỗ trợ → **Tổng: {spo2_score} điểm**")
    else:
        details.append(f"**SpO₂:** {spo2:.0f}%{scale_note} → {spo2_score} điểm")
    
    # 3. Blood Pressure
    bp_score = get_blood_pressure_score(systolic_bp)
    subscores['blood_pressure'] = bp_score
    details.append(f"**Huyết áp tâm thu:** {systolic_bp:.0f} mmHg → {bp_score} điểm")
    
    # 4. Pulse Rate
    pulse_score = get_pulse_rate_score(pulse_rate)
    subscores['pulse_rate'] = pulse_score
    details.append(f"**Nhịp tim:** {pulse_rate:.0f} /min → {pulse_score} điểm")
    
    # 5. Consciousness
    consciousness_score = get_consciousness_score(consciousness)
    subscores['consciousness'] = consciousness_score
    details.append(f"**Mức độ tỉnh táo:** {consciousness} → {consciousness_score} điểm")
    
    # 6. Temperature
    temp_score = get_temperature_score(temperature, temp_unit)
    subscores['temperature'] = temp_score
    temp_symbol = "°C" if temp_unit.upper() == "C" else "°F"
    details.append(f"**Nhiệt độ:** {temperature:.1f} {temp_symbol} → {temp_score} điểm")
    
    # 7. Supplemental Oxygen
    oxygen_score = get_supplemental_oxygen_score(use_supplemental_oxygen)
    subscores['supplemental_oxygen'] = oxygen_score
    oxygen_text = "Có" if use_supplemental_oxygen else "Không"
    details.append(f"**Oxy hỗ trợ:** {oxygen_text} → {oxygen_score} điểm")
    
    # Total score
    total_score = sum(subscores.values())
    
    # Determine category and action plan
    if total_score <= 4:
        category = "Low"
        risk_level = "Thấp"
        action_plan = """
        **Kế hoạch hành động (Category Low - 0-4 điểm):**
        - Đo lại các chỉ số theo protocol của khoa
        - Ghi nhận điểm NEWS2 trên bảng theo dõi
        - Tiếp tục theo dõi thường quy
        """
    elif total_score == 5:
        category = "Low-Medium"
        risk_level = "Thấp-Trung bình"
        action_plan = """
        **Kế hoạch hành động (Category Low-Medium - 5 điểm):**
        - Đánh giá lại trong 1 giờ
        - Thông báo cho điều dưỡng trưởng/điều dưỡng phụ trách
        - Xem xét tăng tần suất theo dõi
        - Đánh giá phản ứng điều trị
        """
    elif total_score == 6:
        category = "Medium"
        risk_level = "Trung bình"
        action_plan = """
        **Kế hoạch hành động (Category Medium - 6 điểm):**
        - Thông báo ngay cho bác sĩ điều trị
        - Đánh giá lại trong 1 giờ
        - Xem xét tăng cường chăm sóc
        - Có thể cần chuyển lên cấp cao hơn
        """
    elif 7 <= total_score <= 9:
        category = "High"
        risk_level = "Cao"
        action_plan = """
        **Kế hoạch hành động (Category High - 7-9 điểm):**
        - **Thông báo ngay lập tức** cho bác sĩ điều trị
        - Đánh giá lại trong 30 phút
        - Xem xét chuyển đến đơn vị chăm sóc tích cực
        - Chuẩn bị nhân lực và trang thiết bị
        - Có thể cần hội chẩn với chuyên khoa
        """
    else:  # total_score >= 10
        category = "Very High"
        risk_level = "Rất cao"
        action_plan = """
        **Kế hoạch hành động (Category Very High - ≥10 điểm):**
        - **Báo động khẩn cấp** - Thông báo ngay cho bác sĩ và điều dưỡng trưởng
        - Đánh giá lại trong 15-30 phút
        - **Chuyển ngay** đến đơn vị chăm sóc tích cực (ICU/CCU)
        - Hội chẩn với chuyên khoa hồi sức
        - Chuẩn bị các biện pháp hồi sức tích cực
        - Xem xét các can thiệp khẩn cấp
        """
    
    return {
        'total_score': total_score,
        'subscores': subscores,
        'category': category,
        'risk_level': risk_level,
        'action_plan': action_plan,
        'details': details
    }


def render():
    """NEWS2 Score Calculator"""
    st.subheader("📊 NEWS2 Score")
    st.caption("National Early Warning Score 2 - Hệ thống cảnh báo sớm cho bệnh nhân nội trú")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'news2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Thông số bệnh nhân")
        
        # Respiration Rate
        resp_rate = st.number_input(
            "Nhịp thở (/phút)",
            min_value=0,
            max_value=60,
            value=20,
            step=1,
            help="Bình thường: 12-20 /phút"
        )
        
        # Độ bão hòa oxy
        col_spo2_1, col_spo2_2 = st.columns([3, 1])
        with col_spo2_1:
            spo2 = st.number_input(
                "SpO₂ (%)",
                min_value=0,
                max_value=100,
                value=98,
                step=1,
                help="Bão hòa oxy máu (pulse oximetry)"
            )
        
        with col_spo2_2:
            has_type2_rf = st.checkbox(
                "Type 2 RF",
                help="Type 2 Respiratory Failure - dùng thang đánh giá đặc biệt"
            )
        
        # Blood Pressure
        systolic_bp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=1,
            help="Bình thường: 90-140 mmHg"
        )
        
        # Pulse Rate
        pulse_rate = st.number_input(
            "Nhịp tim (/phút)",
            min_value=0,
            max_value=250,
            value=80,
            step=1,
            help="Bình thường: 60-100 /phút"
        )
        
        # Consciousness
        consciousness = st.selectbox(
            "Mức độ tỉnh táo",
            ["Alert", "Verbal", "Pain", "Unresponsive"],
            index=0,
            help="Alert = Tỉnh táo; Verbal = Đáp ứng lời nói; Pain = Đáp ứng đau; Unresponsive = Không đáp ứng"
        )
        
        # Temperature
        temp_unit = st.radio(
            "Đơn vị nhiệt độ",
            ["C", "F"],
            index=0,
            horizontal=True
        )
        temp_label = "Nhiệt độ (°C)" if temp_unit == "C" else "Nhiệt độ (°F)"
        temp_default = 37.0 if temp_unit == "C" else 98.6
        temperature = st.number_input(
            temp_label,
            min_value=30.0 if temp_unit == "C" else 86.0,
            max_value=45.0 if temp_unit == "C" else 113.0,
            value=temp_default,
            step=0.1,
            format="%.1f",
            help="Bình thường: 36.5-37.5°C (97.7-99.5°F)"
        )
        
        # Supplemental Oxygen
        use_supplemental_oxygen = st.checkbox(
            "Cần oxy hỗ trợ",
            help="Bệnh nhân đang dùng oxy hỗ trợ qua mask, nasal cannula, v.v."
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="news2",
            calculator_name="NEWS2 Score",
            category="Cấp Cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🔢 Tính NEWS2", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_rr, rr_error = validate_respiratory_rate(resp_rate)
            if not is_valid_rr:
                validation_errors.append(rr_error)
            
            is_valid_sbp, sbp_error = validate_blood_pressure(systolic_bp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
            
            is_valid_hr, hr_error = validate_heart_rate(pulse_rate)
            if not is_valid_hr:
                validation_errors.append(hr_error)
            
            is_valid_spo2, spo2_error = validate_lab_value(spo2, "SpO2", 0, 100)
            if not is_valid_spo2:
                validation_errors.append(spo2_error)
            
            is_valid_temp, temp_error = validate_temperature(temperature, "celsius" if temp_unit == "C" else "fahrenheit")
            if not is_valid_temp:
                validation_errors.append(temp_error)
            
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
            
            result = calculate_news2(
                resp_rate=resp_rate,
                spo2=spo2,
                systolic_bp=systolic_bp,
                pulse_rate=pulse_rate,
                consciousness=consciousness,
                temperature=temperature,
                use_supplemental_oxygen=use_supplemental_oxygen,
                has_type2_respiratory_failure=has_type2_rf,
                temp_unit=temp_unit
            )
            
            # Determine color and icon based on category
            if result['category'] == "Very High":
                color = "#6c757d"  # dark gray
                icon = "🚨"
            elif result['category'] == "High":
                color = "#dc3545"  # red
                icon = "⚠️"
            elif result['category'] == "Medium":
                color = "#fd7e14"  # orange
                icon = "⚡"
            elif result['category'] == "Low-Medium":
                color = "#ffc107"  # yellow
                icon = "⚡"
            else:
                color = "#28a745"  # green
                icon = "✅"
            
            with col2:
                st.markdown("### Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="NEWS2 Score",
                    score=result['total_score'],
                    interpretation=result['risk_level'],
                    mortality=None,
                    color=color,
                    icon=icon,
                    size="large"
                )
                
                st.markdown(result['action_plan'])
            
            # Use render_score_breakdown for component scores
            render_score_breakdown(
                title="Điểm Từng Thông Số",
                subscores={
                    "Nhịp thở": result['subscores']['respiration'],
                    "SpO₂": result['subscores']['oxygen_saturation'],
                    "Huyết áp tâm thu": result['subscores']['blood_pressure'],
                    "Nhịp tim": result['subscores']['pulse_rate'],
                    "Mức độ tỉnh táo": result['subscores']['consciousness'],
                    "Nhiệt độ": result['subscores']['temperature'],
                    "Oxy hỗ trợ": result['subscores']['supplemental_oxygen']
                },
                total_score=result['total_score']
            )
            
            st.markdown("---")
            st.markdown("### Chi tiết điểm số")
            for detail in result['details']:
                st.markdown(detail)
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            
            # Prepare inputs for export
            inputs_dict = {
                "Nhịp thở": f"{resp_rate} /phút",
                "SpO₂": f"{spo2}%",
                "Systolic BP": f"{systolic_bp} mmHg",
                "Pulse Rate": f"{pulse_rate} /phút",
                "Consciousness": consciousness,
                "Temperature": f"{temperature:.1f} {temp_unit}",
                "Supplemental Oxygen": "Có" if use_supplemental_oxygen else "Không",
                "Type 2 RF": "Có" if has_type2_rf else "Không"
            }
            
            # Prepare results for export
            results_dict = {
                "NEWS2 Score": f"{result['total_score']} điểm",
                "Risk Level": result['risk_level'],
                "Category": result['category'],
                "Action Plan": result['action_plan'],
                "Subscores": {
                    "Respiration": result['subscores']['respiration'],
                    "Độ bão hòa oxy": result['subscores']['oxygen_saturation'],
                    "Blood Pressure": result['subscores']['blood_pressure'],
                    "Pulse Rate": result['subscores']['pulse_rate'],
                    "Consciousness": result['subscores']['consciousness'],
                    "Temperature": result['subscores']['temperature'],
                    "Supplemental Oxygen": result['subscores']['supplemental_oxygen']
                }
            }
            
            render_export_section(
                title=f"NEWS2 = {result['total_score']} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="NEWS2 Score",
                filename="news2_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="news2",
                calculator_name="NEWS2 Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="news2",
                calculator_name="NEWS2 Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="news2", show_actions=True)
            
            # References section
            references = get_references("NEWS2")
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
                with st.expander("📚 Tham khảo lâm sàng"):
                    st.markdown("""
                **NEWS2 (National Early Warning Score 2)**
                
                **Mục đích:** Hệ thống cảnh báo sớm để phát hiện suy giảm lâm sàng ở bệnh nhân nội trú
                
                **Tham số:**
                1. **Nhịp thở** (/phút): ≤8 (3), 9-11 (1), 12-20 (0), 21-24 (2), ≥25 (3)
                2. **SpO₂** (%): 
                   - Thang chuẩn: ≤91 (3), 92-93 (2), 94-95 (1), >95 (0)
                   - Thang Type 2 RF: ≤83 (3), 84-85 (2), 86-87 (1), 88-91 (0), 92-93 (1), 94-95 (2), >95 (3)
                   - +2 điểm nếu cần oxy hỗ trợ
                3. **Huyết áp tâm thu** (mmHg): ≤90 (3), 91-100 (2), 101-110 (1), 111-219 (0), ≥220 (3)
                4. **Nhịp tim** (/phút): ≤40 (3), 41-50 (1), 51-90 (0), 91-110 (1), 111-130 (2), ≥131 (3)
                5. **Mức độ tỉnh táo**: Alert (0), Verbal/Pain/Unresponsive (3)
                6. **Nhiệt độ** (°C): ≤35.0 (3), 35.1-36.0 (1), 36.1-38.0 (0), 38.1-39.0 (1), >39.0 (2)
                7. **Oxy hỗ trợ**: Có (2), Không (0)
                
                **Phân loại và kế hoạch hành động:**
                - **Low (0-4 điểm):** Theo dõi thường quy
                - **Low-Medium (5 điểm):** Đánh giá lại trong 1 giờ, thông báo điều dưỡng
                - **Medium (6 điểm):** Thông báo bác sĩ, đánh giá lại trong 1 giờ
                - **High (7-9 điểm):** Thông báo ngay, đánh giá lại trong 30 phút, xem xét chuyển ICU
                - **Very High (≥10 điểm):** Báo động khẩn cấp, đánh giá lại trong 15-30 phút, chuyển ngay ICU
                
                **Lưu ý:**
                - NEWS2 chỉ là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
                - Type 2 Respiratory Failure cần dùng thang đánh giá đặc biệt cho SpO₂
                - Cần đánh giá lại thường xuyên, đặc biệt khi điểm số thay đổi
                - Kết hợp với đánh giá lâm sàng tổng thể
                
                **Tham khảo:**
                - Royal College of Physicians (RCP) 2017 NEWS2 guideline
                - National Early Warning Score (NEWS) 2: Standardising the assessment of acute-illness severity in the NHS
                
                **Ứng dụng:**
                - Theo dõi hàng ngày ở các khoa nội trú
                - Phát hiện sớm suy giảm lâm sàng
                - Hỗ trợ quyết định chuyển lên cấp chăm sóc cao hơn
                - Cải thiện an toàn bệnh nhân
                """)
    
    st.markdown("---")
    st.info("""
    **Bước tiếp theo:**
    - Ghi nhận điểm NEWS2 trên bảng theo dõi
    - Thực hiện kế hoạch hành động theo category
    - Đánh giá lại theo lịch trình phù hợp
    - Nếu điểm cao → Xem xét tính toán **SOFA** hoặc **APACHE II**
    """)

