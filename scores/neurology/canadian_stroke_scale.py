"""
Canadian Stroke Scale (CSS)
============================

Assess stroke severity using the Canadian Stroke Scale.

Reference:
- Côté R, et al. The Canadian Neurological Scale: a preliminary study in acute stroke. Stroke. 1986;17(4):731-7.
- Côté R, et al. The Canadian Neurological Scale: validation and reliability assessment. Neurology. 1989;39(5):638-43.

Clinical Utility:
- Assess stroke severity at presentation
- Monitor stroke progression
- Guide treatment decisions
- Predict outcomes
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================

from components.ui.scoring import render_score_result, render_score_breakdown
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.scores_export import render_export_section as render_scores_export


def calculate_canadian_stroke_scale(
    level_of_consciousness: int = 3,
    orientation: int = 2,
    speech: int = 2,
    facial_palsy: int = 2,
    motor_function_arm_left: int = 2,
    motor_function_arm_right: int = 2,
    motor_function_leg_left: int = 2,
    motor_function_leg_right: int = 2,
    gait: int = 2
) -> dict:
    """
    Calculate Canadian Stroke Scale score
    
    Args:
        level_of_consciousness: 0-3 (0=comatose, 3=alert)
        orientation: 0-2 (0=none, 2=oriented)
        speech: 0-2 (0=aphasic, 2=normal)
        facial_palsy: 0-2 (0=complete, 2=none)
        motor_function_arm_left: 0-2 (0=no movement, 2=normal)
        motor_function_arm_right: 0-2 (0=no movement, 2=normal)
        motor_function_leg_left: 0-2 (0=no movement, 2=normal)
        motor_function_leg_right: 0-2 (0=no movement, 2=normal)
        gait: 0-2 (0=unable, 2=normal)
    
    Returns:
        dict with CSS score, severity level, and recommendations
    """
    # Calculate total score (maximum 11.5)
    total_score = (
        level_of_consciousness +
        orientation +
        speech +
        facial_palsy +
        motor_function_arm_left +
        motor_function_arm_right +
        motor_function_leg_left +
        motor_function_leg_right +
        gait
    )
    
    # Determine severity level
    if total_score >= 10:
        severity_level = "Mild"
        severity_label = "Nhẹ"
        risk_level = "low"
        risk_color = "green"
        recommendations = [
            "Đột quỵ nhẹ - tiên lượng tốt",
            "Có thể điều trị ngoại trú hoặc điều trị ngắn ngày",
            "Tái khám sau 1 tuần",
            "Tiếp tục theo dõi triệu chứng",
            "Đánh giá nguy cơ tái phát và điều trị dự phòng"
        ]
    elif total_score >= 7:
        severity_level = "Moderate"
        severity_label = "Trung bình"
        risk_level = "moderate"
        risk_color = "orange"
        recommendations = [
            "Đột quỵ trung bình - cần theo dõi sát",
            "Điều trị tại bệnh viện",
            "Đánh giá chỉ định tPA nếu trong cửa sổ thời gian",
            "Theo dõi sát các dấu hiệu thần kinh",
            "Bắt đầu phục hồi chức năng sớm",
            "Tái khám sau 2-4 tuần"
        ]
    elif total_score >= 4:
        severity_level = "Moderate-Severe"
        severity_label = "Trung bình-Nặng"
        risk_level = "moderate-high"
        risk_color = "orange-red"
        recommendations = [
            "Đột quỵ trung bình-nặng - cần điều trị tích cực",
            "Nhập viện điều trị",
            "Đánh giá chỉ định tPA/thrombectomy nếu phù hợp",
            "Theo dõi sát trong ICU/đơn vị đột quỵ",
            "Đánh giá nguy cơ biến chứng",
            "Bắt đầu phục hồi chức năng khi ổn định",
            "Tái khám sau 1-2 tuần"
        ]
    else:
        severity_level = "Severe"
        severity_label = "Nặng"
        risk_level = "high"
        risk_color = "red"
        recommendations = [
            "Đột quỵ NẶNG - cần điều trị tích cực ngay",
            "Nhập ICU/đơn vị đột quỵ",
            "Đánh giá chỉ định tPA/thrombectomy khẩn cấp",
            "Theo dõi sát dấu hiệu thần kinh và sinh tồn",
            "Đánh giá nguy cơ phù não và tăng áp lực nội sọ",
            "Xem xét can thiệp phẫu thuật nếu cần",
            "Phục hồi chức năng khi bệnh nhân ổn định",
            "Tiên lượng thận trọng"
        ]
    
    # Item breakdown
    items = [
        {"item": "Ý thức", "score": level_of_consciousness, "max": 3},
        {"item": "Định hướng", "score": orientation, "max": 2},
        {"item": "Lời nói", "score": speech, "max": 2},
        {"item": "Liệt mặt", "score": facial_palsy, "max": 2},
        {"item": "Vận động tay trái", "score": motor_function_arm_left, "max": 2},
        {"item": "Vận động tay phải", "score": motor_function_arm_right, "max": 2},
        {"item": "Vận động chân trái", "score": motor_function_leg_left, "max": 2},
        {"item": "Vận động chân phải", "score": motor_function_leg_right, "max": 2},
        {"item": "Dáng đi", "score": gait, "max": 2}
    ]
    
    return {
        "total_score": total_score,
        "max_score": 19,
        "severity_level": severity_level,
        "severity_label": severity_label,
        "risk_level": risk_level,
        "risk_color": risk_color,
        "recommendations": recommendations,
        "items": items,
        "interpretation": f"Điểm số {total_score}/19 - {severity_label}"
    }


def render():
    """Render the Canadian Stroke Scale Calculator interface"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 Canadian Stroke Scale (CSS)</h3>
    """, unsafe_allow_html=True)
    st.caption("Đánh giá mức độ nặng của đột quỵ")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'canadian_stroke_scale':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Đánh giá Thần Kinh")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        # Level of consciousness
        st.markdown("#### Ý Thức")
        level_of_consciousness = st.selectbox(
            "Mức độ ý thức",
            [0, 1, 2, 3],
            format_func=lambda x: {
                0: "0 - Hôn mê",
                1: "1 - Lơ mơ, không đáp ứng lời nói",
                2: "2 - Đáp ứng lời nói nhưng không định hướng",
                3: "3 - Tỉnh táo, định hướng"
            }[x],
            index=3,
            help="Đánh giá mức độ ý thức của bệnh nhân"
        )
        
        # Orientation
        st.markdown("#### Định Hướng")
        orientation = st.selectbox(
            "Định hướng",
            [0, 1, 2],
            format_func=lambda x: {
                0: "0 - Không định hướng",
                1: "1 - Định hướng một phần",
                2: "2 - Định hướng hoàn toàn"
            }[x],
            index=2,
            help="Khả năng định hướng về thời gian, địa điểm, con người"
        )
        
        # Speech
        st.markdown("#### Lời nói")
        speech = st.selectbox(
            "Lời nói",
            [0, 1, 2],
            format_func=lambda x: {
                0: "0 - Mất ngôn ngữ hoàn toàn",
                1: "1 - Rối loạn ngôn ngữ một phần",
                2: "2 - Bình thường"
            }[x],
            index=2,
            help="Khả năng nói và hiểu lời nói"
        )
        
        # Facial palsy
        st.markdown("#### Liệt mặt")
        facial_palsy = st.selectbox(
            "Liệt mặt",
            [0, 1, 2],
            format_func=lambda x: {
                0: "0 - Liệt hoàn toàn",
                1: "1 - Liệt một phần",
                2: "2 - Bình thường"
            }[x],
            index=2,
            help="Mức độ liệt mặt"
        )
        
        # Motor function - Arms
        st.markdown("#### Vận động tay")
        col_arm_l, col_arm_r = st.columns(2)
        with col_arm_l:
            motor_function_arm_left = st.selectbox(
                "Tay trái",
                [0, 1, 2],
                format_func=lambda x: {
                    0: "0 - Không cử động",
                    1: "1 - Cử động một phần",
                    2: "2 - Bình thường"
                }[x],
                index=2,
                help="Vận động tay trái"
            )
        with col_arm_r:
            motor_function_arm_right = st.selectbox(
                "Tay phải",
                [0, 1, 2],
                format_func=lambda x: {
                    0: "0 - Không cử động",
                    1: "1 - Cử động một phần",
                    2: "2 - Bình thường"
                }[x],
                index=2,
                help="Vận động tay phải"
            )
        
        # Motor function - Legs
        st.markdown("#### Vận động chân")
        col_leg_l, col_leg_r = st.columns(2)
        with col_leg_l:
            motor_function_leg_left = st.selectbox(
                "Chân trái",
                [0, 1, 2],
                format_func=lambda x: {
                    0: "0 - Không cử động",
                    1: "1 - Cử động một phần",
                    2: "2 - Bình thường"
                }[x],
                index=2,
                help="Vận động chân trái"
            )
        with col_leg_r:
            motor_function_leg_right = st.selectbox(
                "Chân phải",
                [0, 1, 2],
                format_func=lambda x: {
                    0: "0 - Không cử động",
                    1: "1 - Cử động một phần",
                    2: "2 - Bình thường"
                }[x],
                index=2,
                help="Vận động chân phải"
            )
        
        # Gait
        st.markdown("#### Dáng Đi")
        gait = st.selectbox(
            "Dáng đi",
            [0, 1, 2],
            format_func=lambda x: {
                0: "0 - Không thể đi",
                1: "1 - Đi với hỗ trợ",
                2: "2 - Đi bình thường"
            }[x],
            index=2,
            help="Khả năng đi lại"
        )
        
        # Calculate
        if st.button("🔄 Tính Toán CSS", type="primary", use_container_width=True):
            result = calculate_canadian_stroke_scale(
                level_of_consciousness=level_of_consciousness,
                orientation=orientation,
                speech=speech,
                facial_palsy=facial_palsy,
                motor_function_arm_left=motor_function_arm_left,
                motor_function_arm_right=motor_function_arm_right,
                motor_function_leg_left=motor_function_leg_left,
                motor_function_leg_right=motor_function_leg_right,
                gait=gait
            )
            
            st.session_state['canadian_stroke_scale_result'] = result
            
            # Display results
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            # Score display
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.metric(
                    "Điểm CSS",
                    f"{result['total_score']}/19",
                    delta=result['severity_label']
                )
            
            with col_res2:
                render_risk_badge(
                    result['risk_level'],
                    result['severity_label'],
                    result['total_score'],
                    result['max_score']
                )
            
            # Score breakdown
            st.markdown("### 📋 Chi tiết điểm số")
            render_score_breakdown(result['items'])
            
            # Recommendations
            st.markdown("### 💡 Khuyến nghị")
            for i, rec in enumerate(result['recommendations'], 1):
                st.markdown(f"{i}. {rec}")
            
            # Clinical guidance
            st.markdown("### 📋 Hướng Dẫn Lâm Sàng")
            
            if result['severity_level'] == "Severe":
                st.error("""
                **Đột quỵ NẶNG:**
                - Cần đánh giá khẩn cấp chỉ định tPA/thrombectomy
                - Theo dõi sát trong ICU
                - Đánh giá nguy cơ phù não
                - Tiên lượng thận trọng
                """)
            elif result['severity_level'] in ["Moderate-Severe", "Moderate"]:
                st.warning("""
                **Đột quỵ Trung bình:**
                - Đánh giá chỉ định tPA nếu trong cửa sổ thời gian
                - Theo dõi sát dấu hiệu thần kinh
                - Bắt đầu phục hồi chức năng sớm
                """)
            else:
                st.success("""
                **Đột quỵ Nhẹ:**
                - Tiên lượng tốt
                - Có thể điều trị ngoại trú
                - Đánh giá nguy cơ tái phát
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="canadian_stroke_scale",
                calculator_name="Canadian Stroke Scale",
                inputs={
                    "Ý thức": level_of_consciousness,
                    "Định hướng": orientation,
                    "Lời nói": speech,
                    "Liệt mặt": facial_palsy,
                    "Vận động": f"Tay T:{motor_function_arm_left}, Tay P:{motor_function_arm_right}, Chân T:{motor_function_leg_left}, Chân P:{motor_function_leg_right}",
                    "Dáng đi": gait
                },
                result={
                    "Điểm CSS": f"{result['total_score']}/19",
                    "Mức độ": result['severity_label']
                }
            )
            
            render_share_section(
                calculator_id="canadian_stroke_scale",
                calculator_name="Canadian Stroke Scale"
            )
            render_scores_export(
                calculator_id="canadian_stroke_scale",
                calculator_name="Canadian Stroke Scale",
                data={"result": result}
            )
            render_suggestions(calculator_id="canadian_stroke_scale", result=result)
    
    with col2:
        st.markdown("### 📚 Thông tin")
        
        st.markdown("""
        **Canadian Stroke Scale:**
        
        - Đánh giá mức độ nặng đột quỵ
        - Thang điểm: 0-19
        - Điểm càng cao = đột quỵ càng nhẹ
        
        **Phân loại:**
        - ≥10: Nhẹ
        - 7-9: Trung bình
        - 4-6: Trung bình-Nặng
        - <4: Nặng
        
        **Lưu ý:**
        - Đánh giá tại thời điểm nhập viện
        - Theo dõi diễn biến
        - Kết hợp với các đánh giá khác
        """)
        
        if st.session_state.get('canadian_stroke_scale_result'):
            result = st.session_state['canadian_stroke_scale_result']
            render_risk_badge(
                result['risk_level'],
                result['severity_label'],
                size="large"
            )
    
    render_history_ui(calculator_id="canadian_stroke_scale", show_actions=True)
    references = get_references("Canadian Stroke Scale")
    if references:
        render_references_section(references)
