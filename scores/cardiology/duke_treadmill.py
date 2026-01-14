"""
Duke Treadmill Score Calculator
=================================

Assesses risk of coronary artery disease based on exercise stress test

Reference:
- Mark DB, et al. Prognostic value of a treadmill exercise score in outpatients 
  with suspected coronary artery disease. N Engl J Med. 1991;325(12):849-853.

Duke Treadmill Score Components:
- Exercise duration (minutes)
- ST segment depression (mm)
- Angina during exercise

Formula:
Score = Exercise time (minutes) - (5 × ST depression mm) - (4 × Angina index)

Angina index:
- 0 = No angina
- 1 = Non-limiting angina
- 2 = Exercise-limiting angina

Risk Categories:
- Low risk: ≥+5
- Moderate risk: -10 to +4
- High risk: ≤-11

Clinical Utility:
- Risk stratification after exercise stress test
- Guide further testing (coronary angiography)
- Predict prognosis
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_lab_value
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_duke_treadmill_score(
    exercise_time: float,
    st_depression: float,
    angina_index: int
) -> dict:
    """
    Calculate Duke Treadmill Score
    
    Args:
        exercise_time: Exercise duration in minutes
        st_depression: ST segment depression in mm
        angina_index: Angina index (0=no angina, 1=non-limiting, 2=exercise-limiting)
    
    Returns:
        Dictionary with score, risk category, and interpretation
    """
    # Calculate score
    score = exercise_time - (5 * st_depression) - (4 * angina_index)
    
    # Build details
    details = []
    details.append(f"Thời gian gắng sức: {exercise_time:.1f} phút → +{exercise_time:.1f} điểm")
    if st_depression > 0:
        details.append(f"ST chênh xuống: {st_depression:.1f} mm → -{5 * st_depression:.1f} điểm")
    else:
        details.append(f"ST chênh xuống: {st_depression:.1f} mm → 0 điểm")
    
    angina_labels = {
        0: "Không đau ngực",
        1: "Đau ngực không giới hạn gắng sức",
        2: "Đau ngực giới hạn gắng sức"
    }
    details.append(f"Đau ngực: {angina_labels.get(angina_index, 'N/A')} → -{4 * angina_index} điểm")
    
    # Determine risk category
    if score >= 5:
        risk_category = "Thấp"
        risk_class = "LOW"
        annual_mortality = "0.25% per year"
        color = COLORS["success"]
    elif score >= -10:
        risk_category = "Trung bình"
        risk_class = "MEDIUM"
        annual_mortality = "1.25% per year"
        color = COLORS["warning"]
    else:  # score <= -11
        risk_category = "Cao"
        risk_class = "HIGH"
        annual_mortality = "5.0% per year"
        color = COLORS["error"]
    
    return {
        'total_score': score,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'annual_mortality': annual_mortality,
        'color': color,
        'details': details
    }


def render():
    """Render Duke Treadmill Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🏃 Duke Treadmill Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá nguy cơ bệnh động mạch vành dựa trên nghiệm pháp gắng sức**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'duke_treadmill':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Duke Treadmill Score** đánh giá nguy cơ bệnh động mạch vành dựa trên nghiệm pháp gắng sức:
        - Được phát triển từ Duke University
        - Dự đoán tiên lượng bệnh nhân nghi ngờ bệnh động mạch vành
        - Hướng dẫn quyết định chụp mạch vành
        
        ### 🎯 Yếu tố tính điểm
        
        1. **Thời gian gắng sức** (phút)
           - Càng lâu càng tốt
        
        2. **ST chênh xuống** (mm)
           - Mỗi mm chênh xuống trừ 5 điểm
        
        3. **Đau ngực khi gắng sức**
           - Không đau: 0 điểm
           - Đau không giới hạn gắng sức: -4 điểm
           - Đau giới hạn gắng sức: -8 điểm
        
        ### 📊 Công thức
        
        **Score = Thời gian (phút) - (5 × ST chênh xuống mm) - (4 × Chỉ số đau ngực)**
        
        ### 📊 Phân loại nguy cơ
        
        | Điểm | Phân loại | Tử vong/năm |
        |------|-----------|-------------|
        | ≥+5 | Thấp | 0.25% |
        | -10 đến +4 | Trung bình | 1.25% |
        | ≤-11 | Cao | 5.0% |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân đã làm nghiệm pháp gắng sức
        - Hướng dẫn quyết định chụp mạch vành
        - Kết hợp với đánh giá lâm sàng
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="duke_treadmill",
            calculator_name="Duke Treadmill Score",
            category="Tim mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin từ nghiệm pháp gắng sức")
    
    col1, col2 = st.columns(2)
    
    with col1:
        exercise_time = st.number_input(
            "Thời gian gắng sức (phút)",
            0.0, 30.0, 10.0, 0.1,
            format="%.1f",
            help="Thời gian gắng sức đạt được trong nghiệm pháp"
        )
        
        st_depression = st.number_input(
            "ST chênh xuống (mm)",
            0.0, 10.0, 0.0, 0.1,
            format="%.1f",
            help="Độ chênh xuống của đoạn ST (mm)"
        )
    
    with col2:
        angina_index = st.selectbox(
            "Đau ngực khi gắng sức",
            [
                (0, "Không đau ngực"),
                (1, "Đau ngực không giới hạn gắng sức"),
                (2, "Đau ngực giới hạn gắng sức")
            ],
            index=0,
            format_func=lambda x: x[1],
            help="Mức độ đau ngực trong nghiệm pháp gắng sức"
        )
        angina_index = angina_index[0]
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Duke Treadmill Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Exercise time validation
        if exercise_time < 0 or exercise_time > 30:
            validation_errors.append("Thời gian gắng sức phải trong khoảng 0-30 phút")
        
        # ST depression validation
        if st_depression < 0 or st_depression > 10:
            validation_errors.append("ST chênh xuống phải trong khoảng 0-10 mm")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_duke_treadmill_score(
            exercise_time=exercise_time,
            st_depression=st_depression,
            angina_index=angina_index
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Use render_score_result for main score display
        icon_map = {
            "LOW": "✅",
            "MEDIUM": "⚠️",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🏃")
        
        render_score_result(
            title="Duke Treadmill Score",
            score=f"{result['total_score']:.1f}",
            interpretation=f"{result['risk_category'].upper()} Risk - Tử vong/năm: {result['annual_mortality']}",
            mortality=result['annual_mortality'],
            color=result['color'],
            icon=icon,
            show_mortality=True
        )
        
        # Details
        with st.expander("📋 Chi tiết tính toán", expanded=False):
            st.markdown("### Các yếu tố đóng góp:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            st.markdown(f"**Tổng điểm: {result['total_score']:.1f}**")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **Nguy cơ thấp** - Điểm: **{result['total_score']:.1f}**
            
            - Tử vong hàng năm: **{result['annual_mortality']}**
            - Nguy cơ bệnh động mạch vành thấp
            - Có thể tiếp tục theo dõi, không cần chụp mạch vành ngay
            - Tiên lượng tốt
            """)
        elif result['risk_class'] == "MEDIUM":
            st.warning(f"""
            **Nguy cơ trung bình** - Điểm: **{result['total_score']:.1f}**
            
            - Tử vong hàng năm: **{result['annual_mortality']}**
            - Nguy cơ bệnh động mạch vành trung bình
            - Cân nhắc chụp mạch vành hoặc các xét nghiệm khác
            - Theo dõi sát và điều trị yếu tố nguy cơ
            """)
        else:
            st.error(f"""
            **Nguy cơ cao** - Điểm: **{result['total_score']:.1f}**
            
            - Tử vong hàng năm: **{result['annual_mortality']}**
            - Nguy cơ bệnh động mạch vành cao
            - **Khuyến cáo chụp mạch vành** để đánh giá chi tiết
            - Cần điều trị tích cực và theo dõi sát
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - Duke Treadmill Score giúp phân tầng nguy cơ sau nghiệm pháp gắng sức
        - **Nguy cơ thấp (≥+5):** Có thể tiếp tục theo dõi, điều trị yếu tố nguy cơ
        - **Nguy cơ trung bình (-10 đến +4):** Cân nhắc chụp mạch vành hoặc xét nghiệm khác
        - **Nguy cơ cao (≤-11):** Khuyến cáo chụp mạch vành để đánh giá chi tiết
        - Kết hợp với đánh giá lâm sàng và các yếu tố nguy cơ khác
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'duke_treadmill',
            'calculator_name': 'Duke Treadmill Score',
            'inputs': {
                'exercise_time': exercise_time,
                'st_depression': st_depression,
                'angina_index': angina_index
            },
            'results': {
                'total_score': result['total_score'],
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class'],
                'annual_mortality': result['annual_mortality']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('duke_treadmill')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Mark DB, et al. Prognostic value of a treadmill exercise score in outpatients 
          with suspected coronary artery disease. N Engl J Med. 1991;325(12):849-853.
        """)
    
    # History
    render_history_ui(calculator_id="duke_treadmill", show_actions=True)
