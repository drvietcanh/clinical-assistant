"""
ORBIT Bleeding Risk Score Calculator
=====================================

Predicts bleeding risk in patients with atrial fibrillation

Reference:
- O'Brien EC, et al. The ORBIT bleeding score: a simple bedside score to assess 
  bleeding risk in atrial fibrillation. Eur Heart J. 2015;36(46):3258-3264.

ORBIT Score Components (5 factors):
- Older age (≥75 years)
- Reduced hemoglobin/hematocrit/Anemia
- Bleeding history
- Insufficient kidney function (eGFR <60 mL/min/1.73m²)
- Treatment with antiplatelet

Total: 0-7 points

Risk Categories:
- Low: 0-2 points
- High: 3-7 points

Clinical Utility:
- Alternative to HAS-BLED for bleeding risk assessment in AF
- Simpler than HAS-BLED (5 factors vs 9)
- Predicts major bleeding risk
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


def calculate_orbit_score(
    age: float,
    anemia: bool,
    bleeding_history: bool,
    egfr: float,
    antiplatelet: bool
) -> dict:
    """
    Calculate ORBIT Bleeding Risk Score
    
    Args:
        age: Age in years
        anemia: Anemia (reduced hemoglobin/hematocrit)
        bleeding_history: Prior bleeding history
        egfr: eGFR (mL/min/1.73m²)
        antiplatelet: Treatment with antiplatelet
    
    Returns:
        Dictionary with score, risk category, and interpretation
    """
    score = 0
    details = []
    
    # Older age ≥75 (1 point)
    if age >= 75:
        score += 1
        details.append(f"Tuổi ≥75 ({age:.0f} tuổi) → +1 điểm")
    else:
        details.append(f"Tuổi <75 ({age:.0f} tuổi) → 0 điểm")
    
    # Reduced hemoglobin/Anemia (2 points)
    if anemia:
        score += 2
        details.append("Thiếu máu/Giảm hemoglobin → +2 điểm")
    else:
        details.append("Không thiếu máu → 0 điểm")
    
    # Bleeding history (2 points)
    if bleeding_history:
        score += 2
        details.append("Tiền sử chảy máu → +2 điểm")
    else:
        details.append("Không có tiền sử chảy máu → 0 điểm")
    
    # Insufficient kidney function (1 point)
    if egfr < 60:
        score += 1
        details.append(f"Suy thận (eGFR {egfr:.1f} mL/min/1.73m² <60) → +1 điểm")
    else:
        details.append(f"Chức năng thận đủ (eGFR {egfr:.1f} mL/min/1.73m² ≥60) → 0 điểm")
    
    # Treatment with antiplatelet (1 point)
    if antiplatelet:
        score += 1
        details.append("Đang dùng thuốc chống tiểu cầu → +1 điểm")
    else:
        details.append("Không dùng thuốc chống tiểu cầu → 0 điểm")
    
    # Determine risk category
    if score <= 2:
        risk_category = "Thấp"
        risk_class = "LOW"
        bleeding_risk = "~1% per year"
        color = COLORS["success"]
    else:  # score >= 3
        risk_category = "Cao"
        risk_class = "HIGH"
        bleeding_risk = "~3-5% per year"
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
    """Render ORBIT Bleeding Risk Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 ORBIT Bleeding Risk Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá nguy cơ chảy máu ở bệnh nhân rung nhĩ**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'orbit':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **ORBIT Bleeding Risk Score** đánh giá nguy cơ chảy máu ở bệnh nhân rung nhĩ:
        - Được phát triển từ ORBIT-AF registry (n=7,411)
        - Đơn giản hơn HAS-BLED (5 yếu tố vs 9 yếu tố)
        - Alternative to HAS-BLED và ATRIA
        - Dự đoán nguy cơ chảy máu nặng hàng năm
        
        ### 🎯 Yếu tố nguy cơ (5 yếu tố)
        
        1. **Tuổi ≥75** (1 điểm)
        
        2. **Thiếu máu** (2 điểm)
           - Giảm hemoglobin/hematocrit
        
        3. **Tiền sử chảy máu** (2 điểm)
        
        4. **Suy thận** (1 điểm)
           - eGFR <60 mL/min/1.73m²
        
        5. **Đang dùng thuốc chống tiểu cầu** (1 điểm)
        
        ### 📊 Phân loại nguy cơ
        
        | Điểm | Phân loại | Nguy cơ chảy máu/năm |
        |------|-----------|---------------------|
        | 0-2 | Thấp | ~1% |
        | 3-7 | Cao | ~3-5% |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân rung nhĩ
        - Đơn giản hơn HAS-BLED
        - Kết hợp với CHA₂DS₂-VASc để đánh giá toàn diện
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="orbit",
            calculator_name="ORBIT Bleeding Risk Score",
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
        
        anemia = st.checkbox(
            "Thiếu máu",
            help="Giảm hemoglobin/hematocrit"
        )
        
        bleeding_history = st.checkbox(
            "Tiền sử chảy máu",
            help="Tiền sử chảy máu nặng hoặc xuất huyết"
        )
        
        antiplatelet = st.checkbox(
            "Đang dùng thuốc chống tiểu cầu",
            help="Aspirin, clopidogrel, hoặc thuốc chống tiểu cầu khác"
        )
    
    with col2:
        st.markdown("#### 🩺 Xét nghiệm")
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²)",
            0.0, 200.0, 80.0, 1.0,
            format="%.1f",
            help="Tốc độ lọc cầu thận ước tính"
        )
        
        if egfr < 60:
            st.warning("⚠️ Suy thận (eGFR <60)")
        if age >= 75:
            st.info("ℹ️ Tuổi ≥75")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính ORBIT Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation
        is_valid_age, age_error = validate_age(age)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        # eGFR validation
        is_valid_egfr, egfr_error = validate_lab_value(egfr, "eGFR", 0.0, 200.0)
        if not is_valid_egfr:
            validation_errors.append(f"eGFR: {egfr_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_orbit_score(
            age=age,
            anemia=anemia,
            bleeding_history=bleeding_history,
            egfr=egfr,
            antiplatelet=antiplatelet
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Use render_score_result for main score display
        icon_map = {
            "LOW": "✅",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🩸")
        
        render_score_result(
            title="ORBIT Bleeding Risk Score",
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
        - ORBIT Score là công cụ hỗ trợ quyết định, không thay thế đánh giá lâm sàng
        - Kết hợp với CHA₂DS₂-VASc để đánh giá toàn diện nguy cơ đột quỵ vs chảy máu
        - ORBIT cao không có nghĩa là chống chỉ định tuyệt đối kháng đông
        - Cân nhắc điều chỉnh các yếu tố nguy cơ có thể thay đổi được
        - Theo dõi sát trong quá trình điều trị kháng đông
        """)
        
        # Comparison with other scores
        st.markdown("### 🔄 So sánh với các thang điểm khác")
        st.info("""
        **ORBIT vs HAS-BLED vs ATRIA:**
        - **ORBIT:** Đơn giản nhất (5 yếu tố), dễ sử dụng
        - **HAS-BLED:** Chi tiết nhất (9 yếu tố), bao gồm cả thuốc và rượu
        - **ATRIA:** Trung bình (5 yếu tố), tập trung vào các yếu tố chính
        - Cả ba đều có giá trị trong đánh giá nguy cơ chảy máu
        - Có thể sử dụng một trong ba hoặc kết hợp để đánh giá toàn diện
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'orbit',
            'calculator_name': 'ORBIT Bleeding Risk Score',
            'inputs': {
                'age': age,
                'anemia': anemia,
                'bleeding_history': bleeding_history,
                'egfr': egfr,
                'antiplatelet': antiplatelet
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
    references = get_references('orbit')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - O'Brien EC, et al. The ORBIT bleeding score: a simple bedside score to assess 
          bleeding risk in atrial fibrillation. Eur Heart J. 2015;36(46):3258-3264.
        """)
    
    # History
    render_history_ui(calculator_id="orbit", show_actions=True)
