"""
FAST-ED (Field Assessment Stroke Triage for Emergency Destination)
===================================================================

Identifies large vessel occlusion stroke (LVOS) in the pre-hospital setting.

Reference:
- Lima FO, et al. Field Assessment Stroke Triage for Emergency Destination: 
  A Simple and Accurate Prehospital Scale to Detect Large Vessel Occlusion Strokes. 
  Stroke. 2016;47(8):1997-2002.

FAST-ED Components (6 factors):
- F: Facial droop (present = 1 point)
- A: Arm weakness (present = 1 point)
- S: Speech disturbance (present = 1 point)
- T: Time (symptom onset <6 hours = 1 point)
- E: Eye deviation (present = 1 point)
- D: Denial/neglect (present = 1 point)

Total: 0-6 points

Interpretation:
- ≥4 points: High probability of LVOS → Transport to comprehensive stroke center
- <4 points: Lower probability of LVOS → May transport to primary stroke center

Clinical Utility:
- Pre-hospital triage tool
- Used daily in emergency medicine
- Helps determine destination (primary vs comprehensive stroke center)
- Faster than NIHSS in field
"""

import streamlit as st
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_fast_ed(
    facial_droop: bool,
    arm_weakness: bool,
    speech_disturbance: bool,
    symptom_onset_less_6h: bool,
    eye_deviation: bool,
    denial_neglect: bool
) -> dict:
    """
    Calculate FAST-ED Score
    
    Args:
        facial_droop: Facial droop present
        arm_weakness: Arm weakness present
        speech_disturbance: Speech disturbance present
        symptom_onset_less_6h: Symptom onset <6 hours
        eye_deviation: Eye deviation present
        denial_neglect: Denial/neglect present
    
    Returns:
        Dictionary with score, LVOS probability, and transport recommendation
    """
    score = 0
    details = []
    
    if facial_droop:
        score += 1
        details.append("Liệt mặt → +1 điểm")
    else:
        details.append("Không liệt mặt → 0 điểm")
    
    if arm_weakness:
        score += 1
        details.append("Yếu tay → +1 điểm")
    else:
        details.append("Không yếu tay → 0 điểm")
    
    if speech_disturbance:
        score += 1
        details.append("Rối loạn ngôn ngữ → +1 điểm")
    else:
        details.append("Không rối loạn ngôn ngữ → 0 điểm")
    
    if symptom_onset_less_6h:
        score += 1
        details.append("Khởi phát <6 giờ → +1 điểm")
    else:
        details.append("Khởi phát ≥6 giờ → 0 điểm")
    
    if eye_deviation:
        score += 1
        details.append("Lệch mắt → +1 điểm")
    else:
        details.append("Không lệch mắt → 0 điểm")
    
    if denial_neglect:
        score += 1
        details.append("Phủ nhận/bỏ qua → +1 điểm")
    else:
        details.append("Không phủ nhận/bỏ qua → 0 điểm")
    
    # Interpretation
    if score >= 4:
        lvos_probability = "Cao (≥4 điểm)"
        transport = "Vận chuyển đến trung tâm đột quỵ toàn diện (Comprehensive Stroke Center)"
        recommendation = "Có thể cần thrombectomy"
    else:
        lvos_probability = "Thấp (<4 điểm)"
        transport = "Có thể vận chuyển đến trung tâm đột quỵ cơ bản (Primary Stroke Center)"
        recommendation = "Đánh giá thêm tại bệnh viện"
    
    return {
        "score": score,
        "lvos_probability": lvos_probability,
        "transport": transport,
        "recommendation": recommendation,
        "details": details
    }


def render():
    """Render FAST-ED Score interface"""
    import streamlit as st
    
    st.set_page_config(page_title="FAST-ED Score", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🧠 FAST-ED Score</h2>
    <p style='text-align: center; color: #6B7280;'>
    Field Assessment Stroke Triage for Emergency Destination<br>
    Xác định đột quỵ tắc mạch lớn (LVOS) trong môi trường tiền viện
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về FAST-ED Score"):
        st.markdown("""
        **FAST-ED (Field Assessment Stroke Triage for Emergency Destination)** là công cụ 
        sàng lọc tiền viện để xác định đột quỵ tắc mạch lớn (LVOS).
        
        ### Các thành phần (6 yếu tố):
        1. **F - Facial droop:** Liệt mặt
        2. **A - Arm weakness:** Yếu tay
        3. **S - Speech disturbance:** Rối loạn ngôn ngữ
        4. **T - Time:** Khởi phát triệu chứng <6 giờ
        5. **E - Eye deviation:** Lệch mắt
        6. **D - Denial/neglect:** Phủ nhận/bỏ qua
        
        ### Diễn giải:
        - **≥4 điểm:** Khả năng cao LVOS → Vận chuyển đến trung tâm đột quỵ toàn diện
        - **<4 điểm:** Khả năng thấp LVOS → Có thể vận chuyển đến trung tâm đột quỵ cơ bản
        
        ### Ưu điểm:
        - Đơn giản, nhanh chóng
        - Dùng trong môi trường tiền viện
        - Giúp quyết định điểm đến (primary vs comprehensive stroke center)
        - Nhanh hơn NIHSS trong thực địa
        - Dùng hàng ngày trong cấp cứu
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        facial_droop = st.checkbox(
            "F - Liệt mặt (Facial droop)",
            key="fast_ed_facial"
        )
        
        arm_weakness = st.checkbox(
            "A - Yếu tay (Arm weakness)",
            key="fast_ed_arm"
        )
        
        speech_disturbance = st.checkbox(
            "S - Rối loạn ngôn ngữ (Speech disturbance)",
            key="fast_ed_speech"
        )
    
    with col2:
        symptom_onset_less_6h = st.checkbox(
            "T - Khởi phát <6 giờ (Time <6 hours)",
            key="fast_ed_time"
        )
        
        eye_deviation = st.checkbox(
            "E - Lệch mắt (Eye deviation)",
            key="fast_ed_eye"
        )
        
        denial_neglect = st.checkbox(
            "D - Phủ nhận/bỏ qua (Denial/neglect)",
            key="fast_ed_denial"
        )
    
    if st.button("🔬 Tính điểm FAST-ED", type="primary", use_container_width=True):
        result = calculate_fast_ed(
            facial_droop=facial_droop,
            arm_weakness=arm_weakness,
            speech_disturbance=speech_disturbance,
            symptom_onset_less_6h=symptom_onset_less_6h,
            eye_deviation=eye_deviation,
            denial_neglect=denial_neglect
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả FAST-ED")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Điểm FAST-ED", f"{result['score']}/6")
        
        with col2:
            st.metric("Khả năng LVOS", result['lvos_probability'])
        
        # Details
        st.markdown("### 📝 Chi tiết tính điểm")
        for detail in result['details']:
            st.markdown(f"- {detail}")
        
        # Transport recommendation
        st.markdown("### 💡 Khuyến nghị vận chuyển")
        
        if result['score'] >= 4:
            st.error(f"**{result['transport']}**")
            st.markdown("""
            **Lý do:**
            - Khả năng cao đột quỵ tắc mạch lớn (LVOS)
            - Có thể cần can thiệp nội mạch (thrombectomy)
            - Cần trung tâm đột quỵ toàn diện với:
              - Chụp mạch máu não
              - Can thiệp nội mạch 24/7
              - Chuyên khoa thần kinh can thiệp
            
            **Hành động:**
            - Vận chuyển ngay lập tức
            - Thông báo trước cho bệnh viện
            - Chuẩn bị cho can thiệp nội mạch
            """)
        else:
            st.warning(f"**{result['transport']}**")
            st.markdown("""
            **Lý do:**
            - Khả năng thấp đột quỵ tắc mạch lớn
            - Có thể điều trị tại trung tâm đột quỵ cơ bản
            - Đánh giá thêm tại bệnh viện
            
            **Hành động:**
            - Vận chuyển đến trung tâm đột quỵ gần nhất
            - Đánh giá lại tại bệnh viện
            - Có thể chuyển viện nếu cần
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="fast_ed",
            calculator_name="FAST-ED Score",
            inputs={
                "Liệt mặt": "Có" if facial_droop else "Không",
                "Yếu tay": "Có" if arm_weakness else "Không",
                "Rối loạn ngôn ngữ": "Có" if speech_disturbance else "Không",
                "Khởi phát <6h": "Có" if symptom_onset_less_6h else "Không",
                "Lệch mắt": "Có" if eye_deviation else "Không",
                "Phủ nhận/bỏ qua": "Có" if denial_neglect else "Không"
            },
            result={
                "Điểm": f"{result['score']}/6",
                "Khả năng LVOS": result['lvos_probability'],
                "Vận chuyển": result['transport']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="fast_ed",
            calculator_name="FAST-ED Score"
        )
        
        render_export_section(
            calculator_id="fast_ed",
            calculator_name="FAST-ED Score",
            data={
                "inputs": {
                    "facial_droop": facial_droop,
                    "arm_weakness": arm_weakness,
                    "speech_disturbance": speech_disturbance,
                    "symptom_onset_less_6h": symptom_onset_less_6h,
                    "eye_deviation": eye_deviation,
                    "denial_neglect": denial_neglect
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="fast_ed", show_actions=True)
    
    # References
    references = get_references("FAST-ED Score")
    if references:
        render_references_section(references)

