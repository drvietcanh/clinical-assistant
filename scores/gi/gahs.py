"""
GAHS (Glasgow Alcoholic Hepatitis Score) Calculator
=====================================================

Predicts mortality in alcoholic hepatitis

Reference:
- Forrest EH, et al. Analysis of factors predictive of mortality in alcoholic hepatitis 
  and derivation and validation of the Glasgow alcoholic hepatitis score. Gut. 2005;54(8):1174-1179.

GAHS Components (5 factors):
- Age (years)
- White blood cell count (×10⁹/L)
- Urea (mmol/L)
- Bilirubin (μmol/L)
- PT ratio (prothrombin time ratio)

Score calculation:
- Each factor contributes points based on thresholds
- Total score determines mortality risk

Risk Categories:
- Low risk: GAHS <9
- High risk: GAHS ≥9

Clinical Utility:
- Predict 28-day and 84-day mortality
- Guide treatment decisions (steroids)
- Assess prognosis
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


def calculate_gahs_score(
    age: float,
    wbc: float,
    urea: float,
    bilirubin: float,
    pt_ratio: float
) -> dict:
    """
    Calculate GAHS Score
    
    Args:
        age: Age (years)
        wbc: White blood cell count (×10⁹/L)
        urea: Urea (mmol/L)
        bilirubin: Bilirubin (μmol/L)
        pt_ratio: Prothrombin time ratio
    
    Returns:
        Dictionary with GAHS score and interpretation
    """
    score = 0
    details = []
    
    # Age scoring
    if age >= 50:
        score += 1
        details.append(f"Tuổi {age:.0f} (≥50) → +1 điểm")
    else:
        details.append(f"Tuổi {age:.0f} (<50) → 0 điểm")
    
    # WBC scoring
    if wbc >= 15:
        score += 1
        details.append(f"WBC {wbc:.1f} ×10⁹/L (≥15) → +1 điểm")
    else:
        details.append(f"WBC {wbc:.1f} ×10⁹/L (<15) → 0 điểm")
    
    # Urea scoring
    if urea >= 7:
        score += 1
        details.append(f"Urea {urea:.1f} mmol/L (≥7) → +1 điểm")
    else:
        details.append(f"Urea {urea:.1f} mmol/L (<7) → 0 điểm")
    
    # Bilirubin scoring
    if bilirubin >= 125:
        score += 1
        details.append(f"Bilirubin {bilirubin:.0f} μmol/L (≥125) → +1 điểm")
    else:
        details.append(f"Bilirubin {bilirubin:.0f} μmol/L (<125) → 0 điểm")
    
    # PT ratio scoring
    if pt_ratio >= 1.5:
        score += 1
        details.append(f"PT ratio {pt_ratio:.2f} (≥1.5) → +1 điểm")
    else:
        details.append(f"PT ratio {pt_ratio:.2f} (<1.5) → 0 điểm")
    
    # Determine risk category
    if score < 9:
        risk_category = "Thấp"
        risk_class = "LOW"
        mortality_28d = "~3%"
        mortality_84d = "~14%"
        color = COLORS["success"]
        recommendation = "Nguy cơ tử vong thấp, có thể không cần steroids"
    else:  # score >= 9
        risk_category = "Cao"
        risk_class = "HIGH"
        mortality_28d = "~46%"
        mortality_84d = "~52%"
        color = COLORS["error"]
        recommendation = "Nguy cơ tử vong cao, cân nhắc điều trị steroids"
    
    return {
        'total_score': score,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'mortality_28d': mortality_28d,
        'mortality_84d': mortality_84d,
        'recommendation': recommendation,
        'color': color,
        'details': details
    }


def render():
    """Render GAHS calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩺 GAHS - Glasgow Alcoholic Hepatitis Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Tiên lượng tử vong ở bệnh nhân viêm gan do rượu**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'gahs':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **GAHS (Glasgow Alcoholic Hepatitis Score)** tiên lượng tử vong ở bệnh nhân viêm gan do rượu:
        - Dự đoán tử vong 28 ngày và 84 ngày
        - Hướng dẫn quyết định điều trị steroids
        - Đánh giá tiên lượng
        
        ### 🎯 Yếu tố tính điểm (5 yếu tố)
        
        Mỗi yếu tố đóng góp 1 điểm nếu đạt ngưỡng:
        
        1. **Tuổi ≥50** (1 điểm)
        
        2. **WBC ≥15 ×10⁹/L** (1 điểm)
        
        3. **Urea ≥7 mmol/L** (1 điểm)
        
        4. **Bilirubin ≥125 μmol/L** (1 điểm)
        
        5. **PT ratio ≥1.5** (1 điểm)
        
        ### 📊 Phân loại
        
        | Điểm | Nguy cơ | Tử vong 28 ngày | Tử vong 84 ngày |
        |------|---------|-----------------|-----------------|
        | <9 | Thấp | ~3% | ~14% |
        | ≥9 | Cao | ~46% | ~52% |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân viêm gan do rượu
        - GAHS ≥9: Cân nhắc điều trị steroids
        - Kết hợp với đánh giá lâm sàng
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="gahs",
            calculator_name="GAHS",
            category="Tiêu hóa",
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
            18, 120, 50, 1,
            format="%d",
            help="Tuổi bệnh nhân"
        )
        
        st.markdown("#### 🩺 Xét nghiệm")
        wbc = st.number_input(
            "WBC (×10⁹/L)",
            0.0, 50.0, 10.0, 0.1,
            format="%.1f",
            help="Số lượng bạch cầu"
        )
        
        urea = st.number_input(
            "Urea (mmol/L)",
            0.0, 50.0, 5.0, 0.1,
            format="%.1f",
            help="Urea máu"
        )
    
    with col2:
        bilirubin = st.number_input(
            "Bilirubin (μmol/L)",
            0.0, 1000.0, 100.0, 1.0,
            format="%.0f",
            help="Bilirubin toàn phần"
        )
        
        pt_ratio = st.number_input(
            "PT ratio",
            0.5, 5.0, 1.2, 0.01,
            format="%.2f",
            help="Tỷ số prothrombin time (PT bệnh nhân / PT bình thường)"
        )
        
        if age >= 50:
            st.info("ℹ️ Tuổi ≥50")
        if wbc >= 15:
            st.warning("⚠️ WBC ≥15 ×10⁹/L")
        if urea >= 7:
            st.warning("⚠️ Urea ≥7 mmol/L")
        if bilirubin >= 125:
            st.warning("⚠️ Bilirubin ≥125 μmol/L")
        if pt_ratio >= 1.5:
            st.warning("⚠️ PT ratio ≥1.5")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính GAHS", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_age, age_error = validate_age(age)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "WBC", 0.0, 50.0)
        if not is_valid_wbc:
            validation_errors.append(f"WBC: {wbc_error}")
        
        if urea < 0 or urea > 50:
            validation_errors.append("Urea phải trong khoảng 0-50 mmol/L")
        
        if bilirubin < 0 or bilirubin > 1000:
            validation_errors.append("Bilirubin phải trong khoảng 0-1000 μmol/L")
        
        if pt_ratio < 0.5 or pt_ratio > 5.0:
            validation_errors.append("PT ratio phải trong khoảng 0.5-5.0")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_gahs_score(
            age=age,
            wbc=wbc,
            urea=urea,
            bilirubin=bilirubin,
            pt_ratio=pt_ratio
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "LOW": "✅",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🩺")
        
        render_score_result(
            title="GAHS Score",
            score=result['total_score'],
            interpretation=f"{result['risk_category'].upper()} Risk - Tử vong 28 ngày: {result['mortality_28d']}, 84 ngày: {result['mortality_84d']}",
            mortality=f"28 ngày: {result['mortality_28d']}, 84 ngày: {result['mortality_84d']}",
            color=result['color'],
            icon=icon,
            show_mortality=True
        )
        
        # Details
        with st.expander("📋 Chi tiết tính toán", expanded=False):
            st.markdown("### Các yếu tố đóng góp:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            st.markdown(f"**Tổng điểm: {result['total_score']}**")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **Nguy cơ thấp** - Điểm: **{result['total_score']}**
            
            - **Tử vong 28 ngày:** {result['mortality_28d']}
            - **Tử vong 84 ngày:** {result['mortality_84d']}
            - **Khuyến nghị:** {result['recommendation']}
            - Tiên lượng tốt hơn
            """)
        else:
            st.error(f"""
            **Nguy cơ cao** - Điểm: **{result['total_score']}**
            
            - **Tử vong 28 ngày:** {result['mortality_28d']}
            - **Tử vong 84 ngày:** {result['mortality_84d']}
            - **Khuyến nghị:** {result['recommendation']}
            - Tiên lượng nghiêm trọng, tỷ lệ tử vong cao
            - Cân nhắc điều trị steroids (prednisolone 40mg/ngày × 28 ngày)
            - Điều trị hỗ trợ tích cực
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - GAHS giúp tiên lượng tử vong ở bệnh nhân viêm gan do rượu
        - **GAHS <9:** Nguy cơ tử vong thấp, có thể không cần steroids
        - **GAHS ≥9:** Nguy cơ tử vong cao, cân nhắc điều trị steroids
        - Điều trị steroids: Prednisolone 40mg/ngày × 28 ngày (nếu không có chống chỉ định)
        - Kết hợp với điều trị hỗ trợ và cai rượu
        - Theo dõi đáp ứng điều trị và điều chỉnh khi cần
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'gahs',
            'calculator_name': 'GAHS - Glasgow Alcoholic Hepatitis Score',
            'inputs': {
                'age': age,
                'wbc': wbc,
                'urea': urea,
                'bilirubin': bilirubin,
                'pt_ratio': pt_ratio
            },
            'results': {
                'total_score': result['total_score'],
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class'],
                'mortality_28d': result['mortality_28d'],
                'mortality_84d': result['mortality_84d']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('gahs')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Forrest EH, et al. Analysis of factors predictive of mortality in alcoholic hepatitis 
          and derivation and validation of the Glasgow alcoholic hepatitis score. Gut. 2005;54(8):1174-1179.
        """)
    
    # History
    render_history_ui(calculator_id="gahs", show_actions=True)
