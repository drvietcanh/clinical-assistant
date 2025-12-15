"""
FOUR Score (Full Outline of UnResponsiveness)
=============================================

Alternative to GCS for consciousness assessment
Better for intubated patients

Reference:
- Wijdicks EF, et al. Validation of a new coma scale: The FOUR score.
  Ann Neurol. 2005;58(4):585-593.

FOUR Score Components:
- Eye response (E): 0-4
- Motor response (M): 0-4
- Brainstem reflexes (B): 0-4
- Respiration (R): 0-4

Total: 0-16 points

Advantages over GCS:
- Can assess intubated patients (no verbal component)
- Includes brainstem reflexes
- Better for ICU patients
- More detailed motor assessment

Clinical Utility:
- Consciousness assessment (especially intubated patients)
- Neurological monitoring
- Prognosis in coma
- ICU monitoring
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert
from scores.utils.validation import validate_positive
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def calculate_four_score(eye: int, motor: int, brainstem: int, respiration: int) -> dict:
    """
    Calculate FOUR Score
    
    Args:
        eye: Eye response (0-4)
        motor: Motor response (0-4)
        brainstem: Brainstem reflexes (0-4)
        respiration: Respiration (0-4)
    
    Returns:
        Dictionary with score and interpretation
    """
    total_score = eye + motor + brainstem + respiration
    
    # Interpretation
    if total_score >= 13:
        interpretation = "Tỉnh táo hoặc lú lẫn nhẹ"
        severity = "Nhẹ"
        color = "success"
    elif total_score >= 9:
        interpretation = "Hôn mê nhẹ"
        severity = "Trung bình"
        color = "warning"
    elif total_score >= 5:
        interpretation = "Hôn mê trung bình"
        severity = "Nặng"
        color = "error"
    else:
        interpretation = "Hôn mê sâu"
        severity = "Rất nặng"
        color = "error"
    
    return {
        "total_score": total_score,
        "eye": eye,
        "motor": motor,
        "brainstem": brainstem,
        "respiration": respiration,
        "interpretation": interpretation,
        "severity": severity,
        "color": color
    }


def render():
    """FOUR Score Calculator"""
    st.subheader("🧠 FOUR Score - Full Outline of UnResponsiveness")
    st.caption("Đánh giá mức độ ý thức - Thay thế GCS cho bệnh nhân thở máy")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'four_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    **FOUR Score** là thang điểm đánh giá mức độ ý thức, đặc biệt hữu ích cho bệnh nhân thở máy.
    
    **Ưu điểm so với GCS:**
    - ✅ Có thể đánh giá bệnh nhân thở máy (không cần verbal response)
    - ✅ Bao gồm phản xạ thân não
    - ✅ Đánh giá vận động chi tiết hơn
    - ✅ Phù hợp hơn cho ICU
    
    **4 thành phần (mỗi thành phần 0-4 điểm):**
    1. **Eye (Mắt):** 0-4
    2. **Motor (Vận động):** 0-4
    3. **Brainstem (Phản xạ thân não):** 0-4
    4. **Respiration (Hô hấp):** 0-4
    
    **Tổng điểm:** 0-16
    """)
    
    st.markdown("---")
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="four_score",
            calculator_name="FOUR Score",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.markdown("### 📝 Đánh giá")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👁️ 1. Eye Response (Mở mắt)")
        eye_options = {
            "4 - Mở mắt tự nhiên hoặc khi gọi": 4,
            "3 - Mở mắt khi đau": 3,
            "2 - Mở mắt khi đau mạnh": 2,
            "1 - Không mở mắt": 1,
            "0 - Không mở mắt + mí mắt nhắm chặt": 0
        }
        eye_response = st.radio(
            "Phản ứng mở mắt:",
            list(eye_options.keys()),
            key="four_eye"
        )
        eye_score = eye_options[eye_response]
        
        st.markdown("#### 💪 2. Motor Response (Vận động)")
        motor_options = {
            "4 - Làm theo lệnh (thumbs-up, OK sign)": 4,
            "3 - Định vị đau (đưa tay lên đầu)": 3,
            "2 - Rút tay khi đau": 2,
            "1 - Cử động bất thường khi đau": 1,
            "0 - Không cử động hoặc duỗi cứng": 0
        }
        motor_response = st.radio(
            "Phản ứng vận động:",
            list(motor_options.keys()),
            key="four_motor"
        )
        motor_score = motor_options[motor_response]
    
    with col2:
        st.markdown("#### 🧠 3. Brainstem Reflexes (Phản xạ thân não)")
        brainstem_options = {
            "4 - Tất cả phản xạ bình thường (pupil, corneal, cough)": 4,
            "3 - Một phản xạ bất thường": 3,
            "2 - Hai phản xạ bất thường": 2,
            "1 - Một phản xạ còn lại": 1,
            "0 - Không có phản xạ": 0
        }
        brainstem_response = st.radio(
            "Phản xạ thân não:",
            list(brainstem_options.keys()),
            key="four_brainstem"
        )
        brainstem_score = brainstem_options[brainstem_response]
        
        st.markdown("#### 🫁 4. Respiration (Hô hấp)")
        respiration_options = {
            "4 - Thở đều, không thở máy": 4,
            "3 - Thở không đều, không thở máy": 3,
            "2 - Thở máy, thở tự nhiên": 2,
            "1 - Thở máy, thở không đều": 1,
            "0 - Thở máy, không thở tự nhiên": 0
        }
        respiration_response = st.radio(
            "Hô hấp:",
            list(respiration_options.keys()),
            key="four_respiration"
        )
        respiration_score = respiration_options[respiration_response]
    
    st.markdown("---")
    
    if st.button("🧮 Tính FOUR Score", type="primary", use_container_width=True):
        # Validate inputs (all should be 0-4)
        validation_errors = []
        
        if eye_score < 0 or eye_score > 4:
            validation_errors.append("Eye score phải từ 0-4")
        if motor_score < 0 or motor_score > 4:
            validation_errors.append("Motor score phải từ 0-4")
        if brainstem_score < 0 or brainstem_score > 4:
            validation_errors.append("Brainstem score phải từ 0-4")
        if respiration_score < 0 or respiration_score > 4:
            validation_errors.append("Respiration score phải từ 0-4")
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        result = calculate_four_score(eye_score, motor_score, brainstem_score, respiration_score)
        
        # Display results
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
        score_color = color_map.get(result['color'], "#17a2b8")
        score_icon = icon_map.get(result['color'], "🧠")
        
        # Use render_score_result for main score display
        render_score_result(
            title="FOUR Score",
            score=result['total_score'],
            interpretation=result['interpretation'],
            mortality=None,
            color=score_color,
            icon=score_icon,
            size="large"
        )
        
        # Use render_score_breakdown for component scores
        render_score_breakdown(
            title="Điểm Từng Thành Phần",
            subscores={
                "👁️ Eye (E)": result['eye'],
                "💪 Motor (M)": result['motor'],
                "🧠 Brainstem (B)": result['brainstem'],
                "🫁 Respiration (R)": result['respiration']
            },
            total_score=result['total_score']
        )
        
        st.markdown(f"**Chi tiết:** E{result['eye']} M{result['motor']} B{result['brainstem']} R{result['respiration']}")
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown(f"""
            **👁️ Eye (Mắt):** {result['eye']}/4
            - {eye_response}
            
            **💪 Motor (Vận động):** {result['motor']}/4
            - {motor_response}
            """)
        
        with col4:
            st.markdown(f"""
            **🧠 Brainstem (Phản xạ thân não):** {result['brainstem']}/4
            - {brainstem_response}
            
            **🫁 Respiration (Hô hấp):** {result['respiration']}/4
            - {respiration_response}
            """)
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến nghị")
        
        if result['severity'] == "Nhẹ":
            st.success("""
            **✅ Tỉnh táo hoặc lú lẫn nhẹ:**
            - Theo dõi định kỳ
            - Đánh giá lại khi có thay đổi
            """)
        elif result['severity'] == "Trung bình":
            st.warning("""
            **⚠️ Hôn mê nhẹ:**
            - Theo dõi sát
            - Đánh giá lại thường xuyên
            - Cân nhắc CT/MRI nếu chưa có
            """)
        elif result['severity'] == "Nặng":
            st.error("""
            **🚨 Hôn mê trung bình:**
            - Theo dõi rất sát
            - Đánh giá lại mỗi giờ
            - Cân nhắc ICP monitoring
            - Hội chẩn thần kinh
            """)
        else:
            st.error("""
            **🚨 Hôn mê sâu:**
            - Theo dõi liên tục
            - ICP monitoring nếu có chỉ định
            - Hội chẩn thần kinh ngay
            - Thảo luận với gia đình về tiên lượng
            """)
        
        st.markdown("---")
        
        # Comparison with GCS
        st.markdown("### 🔄 So sánh với GCS")
        st.info("""
        **FOUR Score vs GCS:**
        
        **Ưu điểm FOUR Score:**
        - Có thể đánh giá bệnh nhân thở máy (không cần verbal)
        - Bao gồm phản xạ thân não (quan trọng cho tiên lượng)
        - Đánh giá vận động chi tiết hơn (thumbs-up, OK sign)
        
        **Khi nào dùng FOUR Score:**
        - Bệnh nhân thở máy
        - ICU monitoring
        - Cần đánh giá phản xạ thân não
        
        **Khi nào dùng GCS:**
        - Bệnh nhân không thở máy
        - Đánh giá nhanh tại hiện trường
        - Tiêu chuẩn quốc tế
        """)
        
        # Prepare inputs and results for Phase 1
        inputs_dict = {
            "Eye Response": eye_response,
            "Motor Response": motor_response,
            "Brainstem Reflexes": brainstem_response,
            "Respiration": respiration_response
        }
        
        results_dict = {
            "FOUR Score": f"{result['total_score']}/16",
            "Eye (E)": f"{result['eye']}/4",
            "Motor (M)": f"{result['motor']}/4",
            "Brainstem (B)": f"{result['brainstem']}/4",
            "Respiration (R)": f"{result['respiration']}/4",
            "Severity": result['severity'],
            "Interpretation": result['interpretation']
        }
        
        # Save to history
        save_calculation_to_history(
            calculator_id="four_score",
            calculator_name="FOUR Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="four_score",
            calculator_name="FOUR Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="four_score", show_actions=True)
        
        # References section
        references = get_references("FOUR Score")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
    
    st.markdown("---")
    
    with st.expander("📖 Bảng điểm FOUR Score"):
        st.markdown("""
        ### 👁️ Eye Response (Mở mắt) - 0-4 điểm
        
        | Điểm | Mô tả |
        |------|-------|
        | 4 | Mở mắt tự nhiên hoặc khi gọi |
        | 3 | Mở mắt khi đau |
        | 2 | Mở mắt khi đau mạnh |
        | 1 | Không mở mắt |
        | 0 | Không mở mắt + mí mắt nhắm chặt |
        
        ### 💪 Motor Response (Vận động) - 0-4 điểm
        
        | Điểm | Mô tả |
        |------|-------|
        | 4 | Làm theo lệnh (thumbs-up, OK sign, nắm tay) |
        | 3 | Định vị đau (đưa tay lên đầu khi đau trán) |
        | 2 | Rút tay khi đau |
        | 1 | Cử động bất thường khi đau (flexion/extension) |
        | 0 | Không cử động hoặc duỗi cứng |
        
        ### 🧠 Brainstem Reflexes (Phản xạ thân não) - 0-4 điểm
        
        | Điểm | Mô tả |
        |------|-------|
        | 4 | Tất cả phản xạ bình thường (pupil, corneal, cough) |
        | 3 | Một phản xạ bất thường |
        | 2 | Hai phản xạ bất thường |
        | 1 | Một phản xạ còn lại |
        | 0 | Không có phản xạ |
        
        ### 🫁 Respiration (Hô hấp) - 0-4 điểm
        
        | Điểm | Mô tả |
        |------|-------|
        | 4 | Thở đều, không thở máy |
        | 3 | Thở không đều, không thở máy |
        | 2 | Thở máy, thở tự nhiên |
        | 1 | Thở máy, thở không đều |
        | 0 | Thở máy, không thở tự nhiên |
        """)
    
    # Always show references at the bottom (even before calculation)
    st.markdown("---")
    references = get_references("FOUR Score")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        # Fallback to manual references if Phase 1 references not found
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **Tài liệu tham khảo:**
            
            1. **Wijdicks EF, et al.** Validation of a new coma scale: The FOUR score.
               Ann Neurol. 2005;58(4):585-593.
            
            2. **Iyer VN, et al.** Validity and reliability of the FOUR score coma scale
               compared with the Glasgow Coma Scale in the assessment of neurosurgical patients.
               Neurocrit Care. 2009;10(1):50-54.
            
            3. **Wolf CA, et al.** Comparison of the Full Outline of UnResponsiveness score
               and the Glasgow Coma Scale in predicting mortality in intoxicated patients.
               J Emerg Med. 2013;45(5):711-716.
            """)
    
    st.markdown("---")
    st.caption("⚠️ FOUR Score chỉ là công cụ hỗ trợ. Đánh giá lâm sàng toàn diện vẫn là quan trọng nhất.")

