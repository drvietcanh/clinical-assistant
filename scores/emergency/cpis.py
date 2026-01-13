"""
CPIS (Clinical Pulmonary Infection Score) Calculator
=====================================================

Assesses likelihood of ventilator-associated pneumonia (VAP)

Reference:
- Pugin J, et al. Clinical pulmonary infection score for ventilator-associated pneumonia. 
  Am J Respir Crit Care Med. 1991;143(5 Pt 1):1121-1129.

CPIS Components (6 factors):
- Temperature (°C)
- White blood cell count (×10³/μL)
- Tracheal secretions
- Oxygenation (PaO2/FiO2 ratio)
- Chest X-ray
- Culture of tracheal aspirate

Total: 0-12 points

Interpretation:
- ≥6 points: High likelihood of VAP
- <6 points: Low likelihood of VAP

Clinical Utility:
- Early identification of VAP
- Guide antibiotic therapy
- Monitor response to treatment
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


def calculate_cpis_score(
    temperature: float,
    wbc: float,
    tracheal_secretions: int,
    pao2_fio2: float,
    chest_xray: int,
    culture: bool
) -> dict:
    """
    Calculate CPIS Score
    
    Args:
        temperature: Temperature (°C)
        wbc: White blood cell count (×10³/μL)
        tracheal_secretions: Tracheal secretions score (0-2)
        pao2_fio2: PaO2/FiO2 ratio
        chest_xray: Chest X-ray score (0-2)
        culture: Positive culture of tracheal aspirate
    
    Returns:
        Dictionary with score, interpretation, and details
    """
    score = 0
    details = []
    
    # Temperature (0-2 points)
    if temperature >= 36.5 and temperature <= 38.4:
        temp_score = 0
        details.append(f"Nhiệt độ {temperature:.1f}°C (36.5-38.4) → 0 điểm")
    elif (temperature >= 38.5 and temperature <= 38.9) or (temperature >= 36.0 and temperature < 36.5):
        temp_score = 1
        score += 1
        details.append(f"Nhiệt độ {temperature:.1f}°C (38.5-38.9 hoặc 36.0-36.4) → 1 điểm")
    else:  # ≥39.0 or <36.0
        temp_score = 2
        score += 2
        details.append(f"Nhiệt độ {temperature:.1f}°C (≥39.0 hoặc <36.0) → 2 điểm")
    
    # White blood cell count (0-2 points)
    if wbc >= 4.0 and wbc <= 11.0:
        wbc_score = 0
        details.append(f"WBC {wbc:.1f} ×10³/μL (4.0-11.0) → 0 điểm")
    elif (wbc >= 11.1 and wbc <= 17.0) or (wbc >= 3.0 and wbc < 4.0):
        wbc_score = 1
        score += 1
        details.append(f"WBC {wbc:.1f} ×10³/μL (11.1-17.0 hoặc 3.0-3.9) → 1 điểm")
    else:  # >17.0 or <3.0
        wbc_score = 2
        score += 2
        details.append(f"WBC {wbc:.1f} ×10³/μL (>17.0 hoặc <3.0) → 2 điểm")
    
    # Tracheal secretions (0-2 points)
    secretion_labels = {
        0: "Ít hoặc không có",
        1: "Vừa phải",
        2: "Nhiều và mủ"
    }
    score += tracheal_secretions
    details.append(f"Dịch khí quản: {secretion_labels.get(tracheal_secretions, 'N/A')} → {tracheal_secretions} điểm")
    
    # Oxygenation (PaO2/FiO2) (0-2 points)
    if pao2_fio2 > 240 or (pao2_fio2 <= 240 and pao2_fio2 > 0):
        if pao2_fio2 > 240:
            oxy_score = 0
            details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (>240) → 0 điểm")
        elif pao2_fio2 <= 240 and pao2_fio2 >= 200:
            oxy_score = 1
            score += 1
            details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (200-240) → 1 điểm")
        else:  # <200
            oxy_score = 2
            score += 2
            details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (<200) → 2 điểm")
    else:
        details.append(f"PaO2/FiO2 {pao2_fio2:.0f} → 0 điểm")
    
    # Chest X-ray (0-2 points)
    xray_labels = {
        0: "Không có thâm nhiễm",
        1: "Thâm nhiễm khu trú",
        2: "Thâm nhiễm lan tỏa hoặc mới xuất hiện"
    }
    score += chest_xray
    details.append(f"X-quang ngực: {xray_labels.get(chest_xray, 'N/A')} → {chest_xray} điểm")
    
    # Culture (0-2 points)
    if culture:
        culture_score = 2
        score += 2
        details.append("Cấy dịch khí quản dương tính → 2 điểm")
    else:
        culture_score = 0
        details.append("Cấy dịch khí quản âm tính → 0 điểm")
    
    # Interpretation
    if score >= 6:
        interpretation = "Khả năng cao VAP"
        risk_class = "HIGH"
        color = COLORS["error"]
        recommendation = "Khuyến cáo điều trị kháng sinh cho VAP"
    else:
        interpretation = "Khả năng thấp VAP"
        risk_class = "LOW"
        color = COLORS["success"]
        recommendation = "Có thể không cần điều trị kháng sinh, tiếp tục theo dõi"
    
    return {
        'total_score': score,
        'interpretation': interpretation,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'color': color,
        'details': details
    }


def render():
    """Render CPIS calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 CPIS - Clinical Pulmonary Infection Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá khả năng viêm phổi liên quan thở máy (VAP)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'cpis':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **CPIS (Clinical Pulmonary Infection Score)** đánh giá khả năng VAP:
        - Dùng cho bệnh nhân thở máy
        - Hỗ trợ quyết định điều trị kháng sinh
        - Theo dõi đáp ứng điều trị
        
        ### 🎯 Yếu tố tính điểm (6 yếu tố)
        
        1. **Nhiệt độ** (0-2 điểm)
           - 36.5-38.4°C: 0 điểm
           - 38.5-38.9°C hoặc 36.0-36.4°C: 1 điểm
           - ≥39.0°C hoặc <36.0°C: 2 điểm
        
        2. **WBC** (0-2 điểm)
           - 4.0-11.0 ×10³/μL: 0 điểm
           - 11.1-17.0 hoặc 3.0-3.9 ×10³/μL: 1 điểm
           - >17.0 hoặc <3.0 ×10³/μL: 2 điểm
        
        3. **Dịch khí quản** (0-2 điểm)
           - Ít hoặc không có: 0 điểm
           - Vừa phải: 1 điểm
           - Nhiều và mủ: 2 điểm
        
        4. **PaO2/FiO2** (0-2 điểm)
           - >240: 0 điểm
           - 200-240: 1 điểm
           - <200: 2 điểm
        
        5. **X-quang ngực** (0-2 điểm)
           - Không có thâm nhiễm: 0 điểm
           - Thâm nhiễm khu trú: 1 điểm
           - Thâm nhiễm lan tỏa hoặc mới xuất hiện: 2 điểm
        
        6. **Cấy dịch khí quản** (0-2 điểm)
           - Âm tính: 0 điểm
           - Dương tính: 2 điểm
        
        ### 📊 Phân loại
        
        | Điểm | Khả năng VAP | Khuyến nghị |
        |------|--------------|-------------|
        | ≥6 | Cao | Điều trị kháng sinh |
        | <6 | Thấp | Theo dõi, có thể không cần kháng sinh |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân thở máy
        - Kết hợp với đánh giá lâm sàng
        - Theo dõi diễn biến theo thời gian
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="cpis",
            calculator_name="CPIS",
            category="Hồi Sức Cấp Cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🩺 Sinh hiệu & Xét nghiệm")
        temperature = st.number_input(
            "Nhiệt độ (°C)",
            30.0, 45.0, 37.0, 0.1,
            format="%.1f",
            help="Nhiệt độ cơ thể"
        )
        
        wbc = st.number_input(
            "WBC (×10³/μL)",
            0.0, 50.0, 10.0, 0.1,
            format="%.1f",
            help="Số lượng bạch cầu"
        )
        
        pao2_fio2 = st.number_input(
            "PaO2/FiO2 ratio",
            0.0, 600.0, 300.0, 1.0,
            format="%.0f",
            help="Tỷ số PaO2/FiO2"
        )
    
    with col2:
        st.markdown("#### 🫁 Hô hấp & Hình ảnh")
        tracheal_secretions = st.selectbox(
            "Dịch khí quản",
            [
                (0, "Ít hoặc không có"),
                (1, "Vừa phải"),
                (2, "Nhiều và mủ")
            ],
            index=0,
            format_func=lambda x: x[1],
            help="Số lượng và đặc điểm dịch khí quản"
        )
        tracheal_secretions = tracheal_secretions[0]
        
        chest_xray = st.selectbox(
            "X-quang ngực",
            [
                (0, "Không có thâm nhiễm"),
                (1, "Thâm nhiễm khu trú"),
                (2, "Thâm nhiễm lan tỏa hoặc mới xuất hiện")
            ],
            index=0,
            format_func=lambda x: x[1],
            help="Kết quả X-quang ngực"
        )
        chest_xray = chest_xray[0]
        
        culture = st.checkbox(
            "Cấy dịch khí quản dương tính",
            help="Kết quả cấy dịch khí quản"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính CPIS", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Temperature validation
        if temperature < 30 or temperature > 45:
            validation_errors.append("Nhiệt độ phải trong khoảng 30-45°C")
        
        # WBC validation
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "WBC", 0.0, 50.0)
        if not is_valid_wbc:
            validation_errors.append(f"WBC: {wbc_error}")
        
        # PaO2/FiO2 validation
        if pao2_fio2 < 0 or pao2_fio2 > 600:
            validation_errors.append("PaO2/FiO2 phải trong khoảng 0-600")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_cpis_score(
            temperature=temperature,
            wbc=wbc,
            tracheal_secretions=tracheal_secretions,
            pao2_fio2=pao2_fio2,
            chest_xray=chest_xray,
            culture=culture
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "HIGH": "🚨",
            "LOW": "✅"
        }
        icon = icon_map.get(result['risk_class'], "🫁")
        
        render_score_result(
            title="CPIS Score",
            score=result['total_score'],
            interpretation=f"{result['interpretation']} - {result['recommendation']}",
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
            st.markdown(f"**Tổng điểm: {result['total_score']}/12**")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "HIGH":
            st.error(f"""
            **Khả năng cao VAP** - Điểm: **{result['total_score']}/12**
            
            - **Khuyến nghị:** {result['recommendation']}
            - Cân nhắc bắt đầu điều trị kháng sinh cho VAP
            - Theo dõi đáp ứng điều trị
            - Có thể cần điều chỉnh kháng sinh dựa trên kết quả cấy và kháng sinh đồ
            """)
        else:
            st.success(f"""
            **Khả năng thấp VAP** - Điểm: **{result['total_score']}/12**
            
            - **Khuyến nghị:** {result['recommendation']}
            - Có thể không cần điều trị kháng sinh ngay
            - Tiếp tục theo dõi và đánh giá lại
            - Nếu triệu chứng xấu đi, đánh giá lại CPIS
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - CPIS là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
        - **CPIS ≥6:** Khuyến cáo điều trị kháng sinh cho VAP
        - **CPIS <6:** Có thể trì hoãn kháng sinh, tiếp tục theo dõi
        - Đánh giá lại CPIS sau 48-72 giờ để theo dõi đáp ứng
        - Kết hợp với kết quả cấy và kháng sinh đồ để điều chỉnh kháng sinh
        - Cân nhắc ngừng kháng sinh nếu CPIS giảm và bệnh nhân cải thiện
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'cpis',
            'calculator_name': 'CPIS - Clinical Pulmonary Infection Score',
            'inputs': {
                'temperature': temperature,
                'wbc': wbc,
                'tracheal_secretions': tracheal_secretions,
                'pao2_fio2': pao2_fio2,
                'chest_xray': chest_xray,
                'culture': culture
            },
            'results': {
                'total_score': result['total_score'],
                'interpretation': result['interpretation'],
                'risk_class': result['risk_class'],
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
    references = get_references('cpis')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Pugin J, et al. Clinical pulmonary infection score for ventilator-associated pneumonia. 
          Am J Respir Crit Care Med. 1991;143(5 Pt 1):1121-1129.
        """)
    
    # History
    render_history_ui(calculator_id="cpis", show_actions=True)
