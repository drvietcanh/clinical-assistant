"""
ATRIA Bleeding Risk Score Calculator
=====================================

Predicts bleeding risk in patients with atrial fibrillation

Reference:
- Fang MC, et al. A new risk scheme to predict warfarin-associated hemorrhage: 
  The ATRIA (Anticoagulation and Risk Factors in Atrial Fibrillation) Study. 
  J Am Coll Cardiol. 2011;58(4):395-401.

ATRIA Score Components (5 factors):
- Anemia (hemoglobin <13 g/dL men, <12 g/dL women)
- Severe renal disease (eGFR <30 mL/min/1.73m² or dialysis)
- Age ≥75 years
- Prior bleeding
- Hypertension

Total: 0-10 points

Risk Categories:
- Low: 0-3 points
- Intermediate: 4 points
- High: 5-10 points

Clinical Utility:
- Alternative to HAS-BLED for bleeding risk assessment in AF
- Predicts major bleeding risk
- Guide anticoagulation decisions
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age, validate_lab_value
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


def calculate_atria_score(
    age: float,
    is_female: bool,
    hemoglobin: float,
    egfr: float,
    prior_bleeding: bool,
    hypertension: bool
) -> dict:
    """
    Calculate ATRIA Bleeding Risk Score
    
    Args:
        age: Age in years
        is_female: Female gender
        hemoglobin: Hemoglobin (g/dL)
        egfr: eGFR (mL/min/1.73m²)
        prior_bleeding: Prior bleeding history
        hypertension: Hypertension
    
    Returns:
        Dictionary with score, risk category, and interpretation
    """
    score = 0
    details = []
    
    # Anemia (3 points)
    # Men: <13 g/dL, Women: <12 g/dL
    anemia_threshold = 12.0 if is_female else 13.0
    if hemoglobin < anemia_threshold:
        score += 3
        details.append(f"Thiếu máu (Hb {hemoglobin:.1f} g/dL < {anemia_threshold:.0f} g/dL) → +3 điểm")
    else:
        details.append(f"Không thiếu máu (Hb {hemoglobin:.1f} g/dL ≥ {anemia_threshold:.0f} g/dL) → 0 điểm")
    
    # Severe renal disease (3 points)
    if egfr < 30:
        score += 3
        details.append(f"Suy thận nặng (eGFR {egfr:.1f} mL/min/1.73m² <30) → +3 điểm")
    else:
        details.append(f"Chức năng thận bình thường/nhẹ (eGFR {egfr:.1f} mL/min/1.73m² ≥30) → 0 điểm")
    
    # Age ≥75 years (2 points)
    if age >= 75:
        score += 2
        details.append(f"Tuổi ≥75 ({age:.0f} tuổi) → +2 điểm")
    else:
        details.append(f"Tuổi <75 ({age:.0f} tuổi) → 0 điểm")
    
    # Prior bleeding (1 point)
    if prior_bleeding:
        score += 1
        details.append("Tiền sử chảy máu → +1 điểm")
    else:
        details.append("Không có tiền sử chảy máu → 0 điểm")
    
    # Hypertension (1 point)
    if hypertension:
        score += 1
        details.append("Tăng huyết áp → +1 điểm")
    else:
        details.append("Không tăng huyết áp → 0 điểm")
    
    # Determine risk category
    if score <= 3:
        risk_category = "Thấp"
        risk_class = "LOW"
        bleeding_risk = "0.4-0.8% per year"
        color = COLORS["success"]
    elif score == 4:
        risk_category = "Trung bình"
        risk_class = "MEDIUM"
        bleeding_risk = "1.2% per year"
        color = COLORS["warning"]
    else:  # score >= 5
        risk_category = "Cao"
        risk_class = "HIGH"
        bleeding_risk = "2.1-3.2% per year"
        color = COLORS["error"]
    
    return {
        'total_score': score,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'bleeding_risk': bleeding_risk,
        'color': color,
        'details': details
    }


def render():
    """Render ATRIA Bleeding Risk Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 ATRIA Bleeding Risk Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá nguy cơ chảy máu ở bệnh nhân rung nhĩ**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'atria':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **ATRIA Bleeding Risk Score** đánh giá nguy cơ chảy máu ở bệnh nhân rung nhĩ:
        - Được phát triển từ ATRIA Study (n=9,186)
        - Alternative to HAS-BLED score
        - Dự đoán nguy cơ chảy máu nặng hàng năm
        
        ### 🎯 Yếu tố nguy cơ (5 yếu tố)
        
        1. **Thiếu máu** (3 điểm)
           - Nam: Hemoglobin <13 g/dL
           - Nữ: Hemoglobin <12 g/dL
        
        2. **Suy thận nặng** (3 điểm)
           - eGFR <30 mL/min/1.73m² hoặc chạy thận
        
        3. **Tuổi ≥75** (2 điểm)
        
        4. **Tiền sử chảy máu** (1 điểm)
        
        5. **Tăng huyết áp** (1 điểm)
        
        ### 📊 Phân loại nguy cơ
        
        | Điểm | Phân loại | Nguy cơ chảy máu/năm |
        |------|-----------|---------------------|
        | 0-3 | Thấp | 0.4-0.8% |
        | 4 | Trung bình | 1.2% |
        | 5-10 | Cao | 2.1-3.2% |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân rung nhĩ
        - Alternative to HAS-BLED
        - Kết hợp với CHA₂DS₂-VASc để đánh giá toàn diện
        - Hướng dẫn quyết định kháng đông
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="atria",
            calculator_name="ATRIA Bleeding Risk Score",
            category="Tim mạch",
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
        
        hypertension = st.checkbox(
            "Tăng huyết áp",
            help="Tăng huyết áp đã được chẩn đoán"
        )
        
        prior_bleeding = st.checkbox(
            "Tiền sử chảy máu",
            help="Tiền sử chảy máu nặng hoặc xuất huyết"
        )
    
    with col2:
        st.markdown("#### 🩺 Xét nghiệm")
        hemoglobin = st.number_input(
            "Hemoglobin (g/dL)",
            5.0, 20.0, 14.0, 0.1,
            format="%.1f",
            help=f"Hemoglobin (ngưỡng thiếu máu: {'<12' if is_female else '<13'} g/dL)"
        )
        
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²)",
            0.0, 200.0, 80.0, 1.0,
            format="%.1f",
            help="Tốc độ lọc cầu thận ước tính"
        )
        
        if egfr < 30:
            st.warning("⚠️ Suy thận nặng (eGFR <30)")
        if hemoglobin < (12.0 if is_female else 13.0):
            st.warning(f"⚠️ Thiếu máu (Hb <{12.0 if is_female else 13.0} g/dL)")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính ATRIA Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation
        is_valid_age, age_error = validate_age(age)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        # Hemoglobin validation
        is_valid_hb, hb_error = validate_lab_value(hemoglobin, "Hemoglobin", 5.0, 20.0)
        if not is_valid_hb:
            validation_errors.append(f"Hemoglobin: {hb_error}")
        
        # eGFR validation
        is_valid_egfr, egfr_error = validate_lab_value(egfr, "eGFR", 0.0, 200.0)
        if not is_valid_egfr:
            validation_errors.append(f"eGFR: {egfr_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_atria_score(
            age=age,
            is_female=is_female,
            hemoglobin=hemoglobin,
            egfr=egfr,
            prior_bleeding=prior_bleeding,
            hypertension=hypertension
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Use render_score_result for main score display
        icon_map = {
            "LOW": "✅",
            "MEDIUM": "⚠️",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🩸")
        
        render_score_result(
            title="ATRIA Bleeding Risk Score",
            score=result['total_score'],
            interpretation=f"{result['risk_category'].upper()} Risk - {result['bleeding_risk']}",
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
            
            - Nguy cơ chảy máu nặng hàng năm: **{result['bleeding_risk']}**
            - Có thể cân nhắc kháng đông nếu CHA₂DS₂-VASc ≥2
            - Theo dõi định kỳ
            """)
        elif result['risk_class'] == "MEDIUM":
            st.warning(f"""
            **Nguy cơ trung bình** - Điểm: **{result['total_score']}**
            
            - Nguy cơ chảy máu nặng hàng năm: **{result['bleeding_risk']}**
            - Cần cân nhắc kỹ lợi ích/nguy cơ khi quyết định kháng đông
            - Theo dõi sát hơn
            """)
        else:
            st.error(f"""
            **Nguy cơ cao** - Điểm: **{result['total_score']}**
            
            - Nguy cơ chảy máu nặng hàng năm: **{result['bleeding_risk']}**
            - Nguy cơ chảy máu cao, cần cân nhắc kỹ trước khi dùng kháng đông
            - Nếu CHA₂DS₂-VASc ≥2 (cần kháng đông):
              → Cân nhắc điều chỉnh các yếu tố nguy cơ trước
              → Theo dõi sát trong quá trình điều trị
              → Cân nhắc NOAC thay vì warfarin (nếu phù hợp)
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - ATRIA Score là công cụ hỗ trợ quyết định, không thay thế đánh giá lâm sàng
        - Kết hợp với CHA₂DS₂-VASc để đánh giá toàn diện nguy cơ đột quỵ vs chảy máu
        - ATRIA cao không có nghĩa là chống chỉ định tuyệt đối kháng đông
        - Cân nhắc điều chỉnh các yếu tố nguy cơ có thể thay đổi được (thiếu máu, tăng huyết áp)
        - Theo dõi sát trong quá trình điều trị kháng đông
        """)
        
        # Comparison with HAS-BLED
        st.markdown("### 🔄 So sánh với HAS-BLED")
        st.info("""
        **ATRIA vs HAS-BLED:**
        - ATRIA: Đơn giản hơn (5 yếu tố), tập trung vào các yếu tố chính
        - HAS-BLED: Chi tiết hơn (9 yếu tố), bao gồm cả thuốc và rượu
        - Cả hai đều có giá trị trong đánh giá nguy cơ chảy máu
        - Có thể sử dụng một trong hai hoặc cả hai để đánh giá toàn diện
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'atria',
            'calculator_name': 'ATRIA Bleeding Risk Score',
            'inputs': {
                'age': age,
                'is_female': is_female,
                'hemoglobin': hemoglobin,
                'egfr': egfr,
                'prior_bleeding': prior_bleeding,
                'hypertension': hypertension
            },
            'results': {
                'total_score': result['total_score'],
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class'],
                'bleeding_risk': result['bleeding_risk']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('atria')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Fang MC, et al. A new risk scheme to predict warfarin-associated hemorrhage: 
          The ATRIA (Anticoagulation and Risk Factors in Atrial Fibrillation) Study. 
          J Am Coll Cardiol. 2011;58(4):395-401.
        """)
    
    # History
    render_history_ui(calculator_id="atria", show_actions=True)
