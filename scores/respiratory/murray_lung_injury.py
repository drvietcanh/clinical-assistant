"""
Murray Lung Injury Score Calculator
====================================

Assesses severity of acute lung injury/ARDS

Reference:
- Murray JF, et al. An expanded definition of the adult respiratory distress syndrome. 
  Am Rev Respir Dis. 1988;138(3):720-723.

Murray Score Components (4 factors):
- Chest X-ray (0-4 points)
- PaO2/FiO2 ratio (0-4 points)
- PEEP (0-4 points)
- Compliance (0-4 points)

Total: 0-16 points (divided by 4 for final score)

Final Score: 0-4
- 0: No lung injury
- 0.1-2.5: Mild to moderate lung injury
- >2.5: Severe lung injury (ARDS)

Clinical Utility:
- Quantify severity of ARDS
- Monitor progression
- Guide treatment decisions
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


def calculate_murray_score(
    chest_xray: int,
    pao2_fio2: float,
    peep: float,
    compliance: float
) -> dict:
    """
    Calculate Murray Lung Injury Score
    
    Args:
        chest_xray: Chest X-ray score (0-4)
        pao2_fio2: PaO2/FiO2 ratio
        peep: PEEP (cmH2O)
        compliance: Static compliance (mL/cmH2O)
    
    Returns:
        Dictionary with score, interpretation, and details
    """
    total_score = 0
    details = []
    
    # Chest X-ray (0-4 points)
    xray_labels = {
        0: "Không có thâm nhiễm",
        1: "Thâm nhiễm 1/4 phổi",
        2: "Thâm nhiễm 2/4 phổi",
        3: "Thâm nhiễm 3/4 phổi",
        4: "Thâm nhiễm 4/4 phổi (toàn bộ)"
    }
    total_score += chest_xray
    details.append(f"X-quang ngực: {xray_labels.get(chest_xray, 'N/A')} → {chest_xray} điểm")
    
    # PaO2/FiO2 ratio (0-4 points)
    if pao2_fio2 >= 300:
        pao2_score = 0
        details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (≥300) → 0 điểm")
    elif pao2_fio2 >= 225:
        pao2_score = 1
        total_score += 1
        details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (225-299) → 1 điểm")
    elif pao2_fio2 >= 175:
        pao2_score = 2
        total_score += 2
        details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (175-224) → 2 điểm")
    elif pao2_fio2 >= 100:
        pao2_score = 3
        total_score += 3
        details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (100-174) → 3 điểm")
    else:
        pao2_score = 4
        total_score += 4
        details.append(f"PaO2/FiO2 {pao2_fio2:.0f} (<100) → 4 điểm")
    
    # PEEP (0-4 points)
    if peep <= 5:
        peep_score = 0
        details.append(f"PEEP {peep:.0f} cmH2O (≤5) → 0 điểm")
    elif peep <= 8:
        peep_score = 1
        total_score += 1
        details.append(f"PEEP {peep:.0f} cmH2O (6-8) → 1 điểm")
    elif peep <= 11:
        peep_score = 2
        total_score += 2
        details.append(f"PEEP {peep:.0f} cmH2O (9-11) → 2 điểm")
    elif peep <= 14:
        peep_score = 3
        total_score += 3
        details.append(f"PEEP {peep:.0f} cmH2O (12-14) → 3 điểm")
    else:
        peep_score = 4
        total_score += 4
        details.append(f"PEEP {peep:.0f} cmH2O (≥15) → 4 điểm")
    
    # Compliance (0-4 points)
    if compliance >= 80:
        comp_score = 0
        details.append(f"Compliance {compliance:.0f} mL/cmH2O (≥80) → 0 điểm")
    elif compliance >= 60:
        comp_score = 1
        total_score += 1
        details.append(f"Compliance {compliance:.0f} mL/cmH2O (60-79) → 1 điểm")
    elif compliance >= 40:
        comp_score = 2
        total_score += 2
        details.append(f"Compliance {compliance:.0f} mL/cmH2O (40-59) → 2 điểm")
    elif compliance >= 20:
        comp_score = 3
        total_score += 3
        details.append(f"Compliance {compliance:.0f} mL/cmH2O (20-39) → 3 điểm")
    else:
        comp_score = 4
        total_score += 4
        details.append(f"Compliance {compliance:.0f} mL/cmH2O (<20) → 4 điểm")
    
    # Calculate final score (divide by 4)
    final_score = total_score / 4.0
    
    # Interpretation
    if final_score == 0:
        interpretation = "Không có tổn thương phổi"
        severity = "None"
        color = COLORS["success"]
    elif final_score <= 2.5:
        interpretation = "Tổn thương phổi nhẹ đến trung bình"
        severity = "Mild-Moderate"
        color = COLORS["warning"]
    else:  # >2.5
        interpretation = "Tổn thương phổi nặng (ARDS)"
        severity = "Severe"
        color = COLORS["error"]
    
    return {
        'total_score': total_score,
        'final_score': final_score,
        'interpretation': interpretation,
        'severity': severity,
        'color': color,
        'details': details
    }


def render():
    """Render Murray Lung Injury Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 Murray Lung Injury Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá mức độ nặng của tổn thương phổi cấp/ARDS**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'murray_lung_injury':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Murray Lung Injury Score** đánh giá mức độ nặng của tổn thương phổi cấp/ARDS:
        - Được phát triển để lượng hóa mức độ ARDS
        - Theo dõi diễn biến bệnh
        - Hướng dẫn quyết định điều trị
        
        ### 🎯 Yếu tố tính điểm (4 yếu tố)
        
        1. **X-quang ngực** (0-4 điểm)
           - 0: Không có thâm nhiễm
           - 1-4: Thâm nhiễm 1/4, 2/4, 3/4, 4/4 phổi
        
        2. **PaO2/FiO2** (0-4 điểm)
           - 0: ≥300
           - 1: 225-299
           - 2: 175-224
           - 3: 100-174
           - 4: <100
        
        3. **PEEP** (0-4 điểm)
           - 0: ≤5 cmH2O
           - 1: 6-8 cmH2O
           - 2: 9-11 cmH2O
           - 3: 12-14 cmH2O
           - 4: ≥15 cmH2O
        
        4. **Compliance** (0-4 điểm)
           - 0: ≥80 mL/cmH2O
           - 1: 60-79 mL/cmH2O
           - 2: 40-59 mL/cmH2O
           - 3: 20-39 mL/cmH2O
           - 4: <20 mL/cmH2O
        
        ### 📊 Phân loại
        
        **Điểm cuối = Tổng điểm / 4**
        
        | Điểm cuối | Phân loại |
        |-----------|-----------|
        | 0 | Không có tổn thương phổi |
        | 0.1-2.5 | Tổn thương phổi nhẹ đến trung bình |
        | >2.5 | Tổn thương phổi nặng (ARDS) |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân thở máy
        - Kết hợp với tiêu chuẩn ARDS Berlin 2012
        - Theo dõi diễn biến theo thời gian
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="murray_lung_injury",
            calculator_name="Murray Lung Injury Score",
            category="Hô Hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🫁 Hô hấp")
        pao2_fio2 = st.number_input(
            "PaO2/FiO2 ratio",
            0.0, 600.0, 300.0, 1.0,
            format="%.0f",
            help="Tỷ số PaO2/FiO2"
        )
        
        peep = st.number_input(
            "PEEP (cmH2O)",
            0.0, 30.0, 5.0, 1.0,
            format="%.0f",
            help="Positive end-expiratory pressure"
        )
        
        compliance = st.number_input(
            "Static Compliance (mL/cmH2O)",
            0.0, 200.0, 80.0, 1.0,
            format="%.0f",
            help="Độ giãn nở tĩnh của phổi"
        )
    
    with col2:
        st.markdown("#### 📷 Hình ảnh")
        chest_xray = st.selectbox(
            "X-quang ngực - Mức độ thâm nhiễm",
            [
                (0, "Không có thâm nhiễm"),
                (1, "Thâm nhiễm 1/4 phổi"),
                (2, "Thâm nhiễm 2/4 phổi"),
                (3, "Thâm nhiễm 3/4 phổi"),
                (4, "Thâm nhiễm 4/4 phổi (toàn bộ)")
            ],
            index=0,
            format_func=lambda x: x[1],
            help="Mức độ thâm nhiễm trên X-quang ngực"
        )
        chest_xray = chest_xray[0]
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Murray Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        if pao2_fio2 < 0 or pao2_fio2 > 600:
            validation_errors.append("PaO2/FiO2 phải trong khoảng 0-600")
        
        if peep < 0 or peep > 30:
            validation_errors.append("PEEP phải trong khoảng 0-30 cmH2O")
        
        if compliance < 0 or compliance > 200:
            validation_errors.append("Compliance phải trong khoảng 0-200 mL/cmH2O")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_murray_score(
            chest_xray=chest_xray,
            pao2_fio2=pao2_fio2,
            peep=peep,
            compliance=compliance
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "None": "✅",
            "Mild-Moderate": "⚠️",
            "Severe": "🚨"
        }
        icon = icon_map.get(result['severity'], "🫁")
        
        render_score_result(
            title="Murray Lung Injury Score",
            score=f"{result['final_score']:.2f}",
            interpretation=f"{result['interpretation']} (Tổng điểm: {result['total_score']}/16)",
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
            st.markdown(f"**Tổng điểm: {result['total_score']}/16**")
            st.markdown(f"**Điểm cuối: {result['final_score']:.2f}** (Tổng điểm / 4)")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['severity'] == "None":
            st.success(f"""
            **Không có tổn thương phổi** - Điểm cuối: **{result['final_score']:.2f}**
            
            - Không có bằng chứng tổn thương phổi cấp
            - Tiên lượng tốt
            """)
        elif result['severity'] == "Mild-Moderate":
            st.warning(f"""
            **Tổn thương phổi nhẹ đến trung bình** - Điểm cuối: **{result['final_score']:.2f}**
            
            - Có tổn thương phổi cấp mức độ nhẹ đến trung bình
            - Cần theo dõi sát và điều trị hỗ trợ
            - Có thể tiến triển thành ARDS
            """)
        else:
            st.error(f"""
            **Tổn thương phổi nặng (ARDS)** - Điểm cuối: **{result['final_score']:.2f}**
            
            - Tổn thương phổi cấp nặng, đáp ứng tiêu chuẩn ARDS
            - Cần điều trị tích cực: thở máy, PEEP cao, có thể cần ECMO
            - Tiên lượng nghiêm trọng, tỷ lệ tử vong cao
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - Murray Score giúp lượng hóa mức độ tổn thương phổi
        - **Điểm >2.5:** Đáp ứng tiêu chuẩn ARDS, cần điều trị tích cực
        - Kết hợp với tiêu chuẩn ARDS Berlin 2012 để chẩn đoán ARDS
        - Theo dõi diễn biến theo thời gian để đánh giá đáp ứng điều trị
        - Điều trị ARDS: thở máy bảo vệ phổi, PEEP tối ưu, có thể cần ECMO
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'murray_lung_injury',
            'calculator_name': 'Murray Lung Injury Score',
            'inputs': {
                'chest_xray': chest_xray,
                'pao2_fio2': pao2_fio2,
                'peep': peep,
                'compliance': compliance
            },
            'results': {
                'total_score': result['total_score'],
                'final_score': result['final_score'],
                'interpretation': result['interpretation'],
                'severity': result['severity']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('murray_lung_injury')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Murray JF, et al. An expanded definition of the adult respiratory distress syndrome. 
          Am Rev Respir Dis. 1988;138(3):720-723.
        """)
    
    # History
    render_history_ui(calculator_id="murray_lung_injury", show_actions=True)
