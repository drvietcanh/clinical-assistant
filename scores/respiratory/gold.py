"""
GOLD Criteria Calculator
=========================

Classifies COPD severity

Reference:
- Global Initiative for Chronic Obstructive Lung Disease (GOLD) 2024

GOLD Classification:
Based on:
- FEV1/FVC ratio
- FEV1 % predicted
- Symptoms (mMRC or CAT score)
- Exacerbation history

GOLD Groups (A-D):
- Group A: Low symptoms, Low risk
- Group B: High symptoms, Low risk
- Group C: Low symptoms, High risk
- Group D: High symptoms, High risk

Clinical Utility:
- Guide COPD treatment
- Predict prognosis
- Monitor disease progression
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


def calculate_gold_classification(
    fev1_fvc: float,
    fev1_predicted: float,
    mmrc_score: int,
    exacerbations: int
) -> dict:
    """
    Calculate GOLD Classification
    
    Args:
        fev1_fvc: FEV1/FVC ratio
        fev1_predicted: FEV1 % predicted
        mmrc_score: mMRC dyspnea score (0-4)
        exacerbations: Number of exacerbations in past year
    
    Returns:
        Dictionary with GOLD classification and recommendations
    """
    # Determine spirometry grade
    if fev1_fvc < 0.7:
        if fev1_predicted >= 80:
            spirometry = "GOLD 1 (Nhẹ)"
        elif fev1_predicted >= 50:
            spirometry = "GOLD 2 (Trung bình)"
        elif fev1_predicted >= 30:
            spirometry = "GOLD 3 (Nặng)"
        else:
            spirometry = "GOLD 4 (Rất nặng)"
    else:
        spirometry = "Không COPD (FEV1/FVC ≥0.7)"
    
    # Determine symptom level (high if mMRC ≥2)
    high_symptoms = mmrc_score >= 2
    
    # Determine risk level (high if ≥2 exacerbations or GOLD 3-4)
    high_risk = (exacerbations >= 2) or (fev1_predicted < 50)
    
    # Determine GOLD group
    if not high_symptoms and not high_risk:
        gold_group = "A"
        group_description = "Triệu chứng thấp, Nguy cơ thấp"
        color = COLORS["success"]
    elif high_symptoms and not high_risk:
        gold_group = "B"
        group_description = "Triệu chứng cao, Nguy cơ thấp"
        color = COLORS["warning"]
    elif not high_symptoms and high_risk:
        gold_group = "C"
        group_description = "Triệu chứng thấp, Nguy cơ cao"
        color = COLORS["warning"]
    else:  # high_symptoms and high_risk
        gold_group = "D"
        group_description = "Triệu chứng cao, Nguy cơ cao"
        color = COLORS["error"]
    
    return {
        'spirometry': spirometry,
        'gold_group': gold_group,
        'group_description': group_description,
        'color': color,
        'high_symptoms': high_symptoms,
        'high_risk': high_risk
    }


def render():
    """Render GOLD Criteria calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 GOLD Criteria</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Phân loại mức độ nặng COPD**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'gold':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **GOLD Criteria** phân loại mức độ nặng COPD:
        - Dựa trên spirometry, triệu chứng, và tiền sử đợt cấp
        - Hướng dẫn điều trị COPD
        - Theo dõi diễn biến bệnh
        
        ### 🎯 Phân loại
        
        **Spirometry (GOLD 1-4):**
        - GOLD 1: FEV1 ≥80% predicted
        - GOLD 2: FEV1 50-79% predicted
        - GOLD 3: FEV1 30-49% predicted
        - GOLD 4: FEV1 <30% predicted
        
        **GOLD Groups (A-D):**
        - **Group A:** Triệu chứng thấp (mMRC 0-1), Nguy cơ thấp (<2 đợt cấp/năm, GOLD 1-2)
        - **Group B:** Triệu chứng cao (mMRC ≥2), Nguy cơ thấp
        - **Group C:** Triệu chứng thấp, Nguy cơ cao (≥2 đợt cấp/năm hoặc GOLD 3-4)
        - **Group D:** Triệu chứng cao, Nguy cơ cao
        
        ### ⚠️ Lưu ý
        
        - FEV1/FVC <0.7 để chẩn đoán COPD
        - Kết hợp với đánh giá lâm sàng
        - Hướng dẫn điều trị theo GOLD guidelines
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="gold",
            calculator_name="GOLD Criteria",
            category="Hô Hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🫁 Spirometry")
        fev1_fvc = st.number_input(
            "FEV1/FVC ratio",
            0.0, 1.0, 0.6, 0.01,
            format="%.2f",
            help="Tỷ số FEV1/FVC (COPD nếu <0.7)"
        )
        
        fev1_predicted = st.number_input(
            "FEV1 % predicted",
            0.0, 150.0, 60.0, 1.0,
            format="%.0f",
            help="FEV1 % so với giá trị dự đoán"
        )
    
    with col2:
        st.markdown("#### 📊 Triệu chứng & Đợt cấp")
        mmrc_score = st.selectbox(
            "mMRC Score",
            [0, 1, 2, 3, 4],
            index=2,
            help="mMRC dyspnea score (0-4)"
        )
        
        exacerbations = st.number_input(
            "Số đợt cấp trong năm qua",
            0, 10, 0, 1,
            format="%d",
            help="Số đợt cấp COPD trong 12 tháng qua"
        )
        
        if fev1_fvc >= 0.7:
            st.warning("⚠️ FEV1/FVC ≥0.7 - Không đáp ứng tiêu chuẩn COPD")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Phân loại GOLD", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        if fev1_fvc < 0 or fev1_fvc > 1:
            validation_errors.append("FEV1/FVC phải trong khoảng 0-1")
        
        if fev1_predicted < 0 or fev1_predicted > 150:
            validation_errors.append("FEV1 % predicted phải trong khoảng 0-150%")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_gold_classification(
            fev1_fvc=fev1_fvc,
            fev1_predicted=fev1_predicted,
            mmrc_score=mmrc_score,
            exacerbations=exacerbations
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "A": "✅",
            "B": "⚠️",
            "C": "⚠️",
            "D": "🚨"
        }
        icon = icon_map.get(result['gold_group'], "🫁")
        
        render_score_result(
            title=f"GOLD Group {result['gold_group']}",
            score=f"Group {result['gold_group']}",
            interpretation=f"{result['group_description']} - {result['spirometry']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Details
        st.markdown("### 📋 Chi tiết phân loại")
        st.markdown(f"""
        - **Spirometry:** {result['spirometry']}
        - **FEV1/FVC:** {fev1_fvc:.2f}
        - **FEV1 % predicted:** {fev1_predicted:.0f}%
        - **mMRC Score:** {mmrc_score}
        - **Đợt cấp trong năm:** {exacerbations}
        - **Triệu chứng:** {'Cao' if result['high_symptoms'] else 'Thấp'} (mMRC {'≥2' if result['high_symptoms'] else '0-1'})
        - **Nguy cơ:** {'Cao' if result['high_risk'] else 'Thấp'} ({'≥2 đợt cấp/năm hoặc GOLD 3-4' if result['high_risk'] else '<2 đợt cấp/năm và GOLD 1-2'})
        """)
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['gold_group'] == "A":
            st.success(f"""
            **GOLD Group A** - Triệu chứng thấp, Nguy cơ thấp ✅
            
            - **Spirometry:** {result['spirometry']}
            - Điều trị ban đầu: SABA/SAMA khi cần
            - Theo dõi định kỳ
            """)
        elif result['gold_group'] == "B":
            st.warning(f"""
            **GOLD Group B** - Triệu chứng cao, Nguy cơ thấp ⚠️
            
            - **Spirometry:** {result['spirometry']}
            - Điều trị: LABA hoặc LAMA (ưu tiên LAMA)
            - Có thể kết hợp LABA/LAMA nếu triệu chứng không kiểm soát
            """)
        elif result['gold_group'] == "C":
            st.warning(f"""
            **GOLD Group C** - Triệu chứng thấp, Nguy cơ cao ⚠️
            
            - **Spirometry:** {result['spirometry']}
            - Điều trị: LABA/LAMA (ưu tiên LAMA)
            - Có thể thêm ICS nếu eosinophil cao
            """)
        else:
            st.error(f"""
            **GOLD Group D** - Triệu chứng cao, Nguy cơ cao 🚨
            
            - **Spirometry:** {result['spirometry']}
            - Điều trị: LABA/LAMA/ICS (triple therapy)
            - Cân nhắc roflumilast hoặc azithromycin nếu phù hợp
            - Điều trị tích cực và theo dõi sát
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị điều trị")
        st.info("""
        - GOLD Criteria hướng dẫn điều trị COPD theo guidelines
        - **Group A:** Điều trị khi cần (SABA/SAMA)
        - **Group B:** LABA hoặc LAMA (ưu tiên LAMA)
        - **Group C:** LABA/LAMA (ưu tiên LAMA), có thể thêm ICS
        - **Group D:** Triple therapy (LABA/LAMA/ICS)
        - Kết hợp với đánh giá lâm sàng và đáp ứng điều trị
        - Điều chỉnh điều trị dựa trên đáp ứng và tác dụng phụ
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'gold',
            'calculator_name': 'GOLD Criteria',
            'inputs': {
                'fev1_fvc': fev1_fvc,
                'fev1_predicted': fev1_predicted,
                'mmrc_score': mmrc_score,
                'exacerbations': exacerbations
            },
            'results': {
                'spirometry': result['spirometry'],
                'gold_group': result['gold_group'],
                'group_description': result['group_description']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('gold')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Global Initiative for Chronic Obstructive Lung Disease (GOLD) 2024
        - GOLD Guidelines: https://goldcopd.org/
        """)
    
    # History
    render_history_ui(calculator_id="gold", show_actions=True)
