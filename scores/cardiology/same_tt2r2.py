"""
SAMe-TT₂R₂ Score Calculator
============================

Predicts ability to achieve target INR with warfarin

Reference:
- Apostolakis S, et al. The SAMe-TT2R2 score: a predictor of poor response to 
  warfarin anticoagulation in patients with atrial fibrillation. 
  Am J Med. 2013;126(5):423.e9-423.e15.

SAMe-TT₂R₂ Score Components (6 factors):
- Sex (female)
- Age (<60 years)
- Medical history (HTN, DM, CAD, PAD, CHF, stroke, pulmonary disease, hepatic/renal disease)
- Treatment (interacting drugs: amiodarone)
- Tobacco use (within 2 years)
- Race (non-Caucasian)

Total: 0-8 points

Risk Categories:
- Low (0-2): Good INR control expected
- High (≥3): Poor INR control expected, consider NOAC

Clinical Utility:
- Predicts time in therapeutic range (TTR) with warfarin
- Guides choice between warfarin and NOAC
- Helps identify patients who may benefit from NOAC
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age
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


def calculate_same_tt2r2_score(
    is_female: bool,
    age: float,
    medical_history: bool,
    amiodarone: bool,
    tobacco: bool,
    non_caucasian: bool
) -> dict:
    """
    Calculate SAMe-TT₂R₂ Score
    
    Args:
        is_female: Female gender
        age: Age in years
        medical_history: Medical history (HTN, DM, CAD, PAD, CHF, stroke, pulmonary disease, hepatic/renal disease)
        amiodarone: Treatment with amiodarone (interacting drug)
        tobacco: Tobacco use within 2 years
        non_caucasian: Non-Caucasian race
    
    Returns:
        Dictionary with score, risk category, and interpretation
    """
    score = 0
    details = []
    
    # Sex (female) - 1 point
    if is_female:
        score += 1
        details.append("Giới tính nữ → +1 điểm")
    else:
        details.append("Giới tính nam → 0 điểm")
    
    # Age (<60 years) - 1 point
    if age < 60:
        score += 1
        details.append(f"Tuổi <60 ({age:.0f} tuổi) → +1 điểm")
    else:
        details.append(f"Tuổi ≥60 ({age:.0f} tuổi) → 0 điểm")
    
    # Medical history - 1 point
    if medical_history:
        score += 1
        details.append("Có bệnh lý mạn tính (HTN, DM, CAD, PAD, CHF, stroke, phổi, gan/thận) → +1 điểm")
    else:
        details.append("Không có bệnh lý mạn tính → 0 điểm")
    
    # Treatment (amiodarone) - 1 point
    if amiodarone:
        score += 1
        details.append("Đang dùng amiodarone → +1 điểm")
    else:
        details.append("Không dùng amiodarone → 0 điểm")
    
    # Tobacco use - 2 points
    if tobacco:
        score += 2
        details.append("Hút thuốc trong vòng 2 năm → +2 điểm")
    else:
        details.append("Không hút thuốc hoặc đã bỏ >2 năm → 0 điểm")
    
    # Race (non-Caucasian) - 2 points
    if non_caucasian:
        score += 2
        details.append("Chủng tộc không phải da trắng → +2 điểm")
    else:
        details.append("Chủng tộc da trắng → 0 điểm")
    
    # Determine risk category
    if score <= 2:
        risk_category = "Thấp"
        risk_class = "LOW"
        ttr_prediction = "TTR dự kiến: ≥65-70%"
        recommendation = "Có thể dùng warfarin với kiểm soát INR tốt"
        color = COLORS["success"]
    else:  # score >= 3
        risk_category = "Cao"
        risk_class = "HIGH"
        ttr_prediction = "TTR dự kiến: <65%"
        recommendation = "Cân nhắc NOAC thay vì warfarin"
        color = COLORS["error"]
    
    return {
        'total_score': score,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'ttr_prediction': ttr_prediction,
        'recommendation': recommendation,
        'color': color,
        'details': details
    }


def render():
    """Render SAMe-TT₂R₂ Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>💊 SAMe-TT₂R₂ Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Dự đoán khả năng đạt INR mục tiêu với warfarin**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'same_tt2r2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **SAMe-TT₂R₂ Score** dự đoán khả năng đạt INR mục tiêu với warfarin:
        - Dự đoán Time in Therapeutic Range (TTR)
        - Hướng dẫn lựa chọn giữa warfarin và NOAC
        - Giúp xác định bệnh nhân có thể hưởng lợi từ NOAC
        
        ### 🎯 Yếu tố nguy cơ (6 yếu tố)
        
        1. **Sex** - Giới tính nữ (1 điểm)
        
        2. **Age** - Tuổi <60 (1 điểm)
        
        3. **Medical history** - Bệnh lý mạn tính (1 điểm)
           - HTN, DM, CAD, PAD, CHF, stroke, phổi, gan/thận
        
        4. **Treatment** - Đang dùng amiodarone (1 điểm)
        
        5. **Tobacco** - Hút thuốc trong vòng 2 năm (2 điểm)
        
        6. **Race** - Chủng tộc không phải da trắng (2 điểm)
        
        ### 📊 Phân loại nguy cơ
        
        | Điểm | Phân loại | TTR dự kiến | Khuyến nghị |
        |------|-----------|-------------|-------------|
        | 0-2 | Thấp | ≥65-70% | Có thể dùng warfarin |
        | ≥3 | Cao | <65% | Cân nhắc NOAC |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân cần kháng đông (rung nhĩ)
        - SAMe-TT₂R₂ ≥3: Cân nhắc NOAC thay vì warfarin
        - TTR <65%: Liên quan đến kết quả kém hơn với warfarin
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="same_tt2r2",
            calculator_name="SAMe-TT₂R₂ Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Bệnh nhân")
        age = st.number_input(
            "Tuổi (năm)",
            18, 120, 70, 1,
            format="%d",
            help="Tuổi bệnh nhân"
        )
        
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True)
        is_female = (sex == "Nữ")
        
        non_caucasian = st.checkbox(
            "Chủng tộc không phải da trắng",
            help="Châu Á, Châu Phi, Hispanic, hoặc các chủng tộc khác"
        )
        
        tobacco = st.checkbox(
            "Hút thuốc trong vòng 2 năm",
            help="Đang hút hoặc đã bỏ <2 năm"
        )
    
    with col2:
        st.markdown("#### 🏥 Bệnh lý & Điều trị")
        medical_history = st.checkbox(
            "Có bệnh lý mạn tính",
            help="HTN, DM, CAD, PAD, CHF, stroke, bệnh phổi, bệnh gan/thận"
        )
        
        amiodarone = st.checkbox(
            "Đang dùng amiodarone",
            help="Amiodarone là thuốc tương tác với warfarin"
        )
        
        if amiodarone:
            st.warning("⚠️ Amiodarone tương tác với warfarin, cần theo dõi INR sát")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính SAMe-TT₂R₂ Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation
        is_valid_age, age_error = validate_age(age)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_same_tt2r2_score(
            is_female=is_female,
            age=age,
            medical_history=medical_history,
            amiodarone=amiodarone,
            tobacco=tobacco,
            non_caucasian=non_caucasian
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Use render_score_result for main score display
        icon_map = {
            "LOW": "✅",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "💊")
        
        render_score_result(
            title="SAMe-TT₂R₂ Score",
            score=result['total_score'],
            interpretation=f"{result['risk_category'].upper()} Risk - {result['ttr_prediction']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Details
        with st.expander("📋 Chi tiết tính toán", expanded=False):
            st.markdown("### Các yếu tố đóng góp:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **Nguy cơ thấp** - Điểm: **{result['total_score']}**
            
            - **{result['ttr_prediction']}**
            - **Khuyến nghị:** {result['recommendation']}
            - Kiểm soát INR với warfarin dự kiến tốt
            - Có thể tiếp tục dùng warfarin với theo dõi định kỳ
            """)
        else:
            st.error(f"""
            **Nguy cơ cao** - Điểm: **{result['total_score']}**
            
            - **{result['ttr_prediction']}**
            - **Khuyến nghị:** {result['recommendation']}
            - Kiểm soát INR với warfarin dự kiến kém
            - **Cân nhắc chuyển sang NOAC** (apixaban, rivaroxaban, dabigatran, edoxaban)
            - NOAC không cần theo dõi INR và có thể đạt TTR tốt hơn
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - SAMe-TT₂R₂ Score giúp dự đoán khả năng kiểm soát INR với warfarin
        - **SAMe-TT₂R₂ ≥3:** Cân nhắc NOAC thay vì warfarin
        - **TTR <65%:** Liên quan đến kết quả kém hơn (tăng nguy cơ đột quỵ và chảy máu)
        - NOAC có thể là lựa chọn tốt hơn cho bệnh nhân SAMe-TT₂R₂ cao
        - Quyết định cuối cùng cần dựa trên đánh giá lâm sàng toàn diện
        """)
        
        # Comparison with warfarin vs NOAC
        st.markdown("### 💊 Warfarin vs NOAC")
        st.info("""
        **Ưu điểm của NOAC khi SAMe-TT₂R₂ ≥3:**
        - Không cần theo dõi INR định kỳ
        - TTR tốt hơn (không phụ thuộc vào kiểm soát INR)
        - Tương tác thuốc ít hơn
        - Liều cố định, dễ sử dụng
        
        **Lưu ý:**
        - NOAC có thể đắt hơn warfarin
        - Không có thuốc giải độc cho một số NOAC
        - Cần điều chỉnh liều theo chức năng thận
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'same_tt2r2',
            'calculator_name': 'SAMe-TT₂R₂ Score',
            'inputs': {
                'is_female': is_female,
                'age': age,
                'medical_history': medical_history,
                'amiodarone': amiodarone,
                'tobacco': tobacco,
                'non_caucasian': non_caucasian
            },
            'results': {
                'total_score': result['total_score'],
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class'],
                'ttr_prediction': result['ttr_prediction'],
                'recommendation': result['recommendation']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('same_tt2r2')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Apostolakis S, et al. The SAMe-TT2R2 score: a predictor of poor response to 
          warfarin anticoagulation in patients with atrial fibrillation. 
          Am J Med. 2013;126(5):423.e9-423.e15.
        """)
    
    # History
    render_history_ui(calculator_id="same_tt2r2", show_actions=True)
