"""
Hestia Score Calculator
========================

Assesses eligibility for outpatient treatment of pulmonary embolism

Reference:
- Zondag W, et al. Outpatient treatment in patients with acute pulmonary embolism: 
  the Hestia Study. J Thromb Haemost. 2011;9(8):1500-1507.

Hestia Criteria (11 criteria):
Any positive = Not eligible for outpatient treatment

Criteria:
1. Hemodynamically unstable
2. Thrombolysis or embolectomy needed
3. Active bleeding or high bleeding risk
4. Oxygen needed for >24h
5. PE diagnosed while on anticoagulation
6. Severe pain needing IV analgesia >24h
7. Medical/social reason for admission >24h
8. Creatinine clearance <30 mL/min
9. Severe liver impairment
10. Pregnant
11. Documented history of heparin-induced thrombocytopenia

Clinical Utility:
- Identify low-risk PE patients safe for outpatient treatment
- Reduce unnecessary hospitalizations
- Guide ED disposition decisions
"""

import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_hestia_score(criteria: dict) -> dict:
    """
    Calculate Hestia Score assessment
    
    Args:
        criteria: Dictionary of Hestia criteria (all boolean)
    
    Returns:
        Dictionary with eligibility assessment
    """
    positive_criteria = []
    details = []
    
    criteria_list = [
        ("hemodynamically_unstable", "Không ổn định huyết động"),
        ("thrombolysis_needed", "Cần điều trị tiêu sợi huyết hoặc lấy huyết khối"),
        ("active_bleeding", "Chảy máu đang hoạt động hoặc nguy cơ chảy máu cao"),
        ("oxygen_needed", "Cần oxy >24 giờ"),
        ("pe_on_anticoagulation", "PE được chẩn đoán khi đang dùng kháng đông"),
        ("severe_pain", "Đau nặng cần giảm đau IV >24 giờ"),
        ("medical_social_reason", "Lý do y tế/xã hội cần nhập viện >24 giờ"),
        ("crcl_low", "Creatinine clearance <30 mL/min"),
        ("liver_impairment", "Suy gan nặng"),
        ("pregnant", "Có thai"),
        ("hit_history", "Tiền sử HIT (heparin-induced thrombocytopenia)")
    ]
    
    for key, description in criteria_list:
        if criteria.get(key, False):
            positive_criteria.append(description)
            details.append(f"✅ {description} → Chống chỉ định điều trị ngoại trú")
        else:
            details.append(f"❌ {description} → Không có")
    
    # Eligibility assessment
    if len(positive_criteria) > 0:
        eligible = False
        interpretation = "Không đủ điều kiện điều trị ngoại trú"
        recommendation = "Cần nhập viện để điều trị và theo dõi"
        color = COLORS["error"]
        risk_class = "HIGH"
    else:
        eligible = True
        interpretation = "Đủ điều kiện điều trị ngoại trú"
        recommendation = "Có thể cân nhắc điều trị ngoại trú với thuốc kháng đông"
        color = COLORS["success"]
        risk_class = "LOW"
    
    return {
        'eligible': eligible,
        'positive_criteria': positive_criteria,
        'interpretation': interpretation,
        'recommendation': recommendation,
        'color': color,
        'risk_class': risk_class,
        'details': details
    }


def render():
    """Render Hestia Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 Hestia Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá khả năng điều trị thuyên tắc phổi ngoại trú**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'hestia':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Hestia Score** đánh giá khả năng điều trị PE ngoại trú:
        - Xác định bệnh nhân PE nguy cơ thấp có thể điều trị ngoại trú
        - Giảm nhập viện không cần thiết
        - Hướng dẫn quyết định xuất viện từ ED
        
        ### 🎯 Tiêu chí Hestia (11 tiêu chí)
        
        **Bất kỳ tiêu chí nào dương tính = Không đủ điều kiện điều trị ngoại trú**
        
        1. Không ổn định huyết động
        2. Cần điều trị tiêu sợi huyết hoặc lấy huyết khối
        3. Chảy máu đang hoạt động hoặc nguy cơ chảy máu cao
        4. Cần oxy >24 giờ
        5. PE được chẩn đoán khi đang dùng kháng đông
        6. Đau nặng cần giảm đau IV >24 giờ
        7. Lý do y tế/xã hội cần nhập viện >24 giờ
        8. Creatinine clearance <30 mL/min
        9. Suy gan nặng
        10. Có thai
        11. Tiền sử HIT
        
        ### 📊 Phân loại
        
        | Kết quả | Điều trị ngoại trú | Khuyến nghị |
        |---------|-------------------|-------------|
        | Có ≥1 tiêu chí | Không đủ điều kiện | Nhập viện |
        | Không có tiêu chí | Đủ điều kiện | Có thể ngoại trú |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân đã chẩn đoán PE
        - Kết hợp với đánh giá lâm sàng
        - Đảm bảo bệnh nhân có thể tuân thủ điều trị ngoại trú
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="hestia",
            calculator_name="Hestia Score",
            category="Hô Hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Đánh giá các tiêu chí Hestia")
    
    st.markdown("**Chọn các tiêu chí áp dụng (bất kỳ tiêu chí nào dương tính = không đủ điều kiện điều trị ngoại trú):**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        hemodynamically_unstable = st.checkbox(
            "1. Không ổn định huyết động",
            help="Sốc, hạ huyết áp, cần vận mạch"
        )
        
        thrombolysis_needed = st.checkbox(
            "2. Cần điều trị tiêu sợi huyết hoặc lấy huyết khối",
            help="Chỉ định điều trị tiêu sợi huyết hoặc embolectomy"
        )
        
        active_bleeding = st.checkbox(
            "3. Chảy máu đang hoạt động hoặc nguy cơ chảy máu cao",
            help="Chảy máu đang hoạt động hoặc HAS-BLED ≥3"
        )
        
        oxygen_needed = st.checkbox(
            "4. Cần oxy >24 giờ",
            help="Cần oxy hỗ trợ >24 giờ"
        )
        
        pe_on_anticoagulation = st.checkbox(
            "5. PE được chẩn đoán khi đang dùng kháng đông",
            help="PE xảy ra khi đang điều trị kháng đông"
        )
        
        severe_pain = st.checkbox(
            "6. Đau nặng cần giảm đau IV >24 giờ",
            help="Đau nặng cần giảm đau đường tĩnh mạch >24 giờ"
        )
    
    with col2:
        medical_social_reason = st.checkbox(
            "7. Lý do y tế/xã hội cần nhập viện >24 giờ",
            help="Lý do y tế hoặc xã hội cần nhập viện >24 giờ"
        )
        
        crcl_low = st.checkbox(
            "8. Creatinine clearance <30 mL/min",
            help="Suy thận nặng (CrCl <30 mL/min)"
        )
        
        liver_impairment = st.checkbox(
            "9. Suy gan nặng",
            help="Suy gan nặng (Child-Pugh C hoặc tương đương)"
        )
        
        pregnant = st.checkbox(
            "10. Có thai",
            help="Bệnh nhân đang có thai"
        )
        
        hit_history = st.checkbox(
            "11. Tiền sử HIT",
            help="Tiền sử heparin-induced thrombocytopenia"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Đánh giá Hestia Score", type="primary", use_container_width=True):
        criteria = {
            'hemodynamically_unstable': hemodynamically_unstable,
            'thrombolysis_needed': thrombolysis_needed,
            'active_bleeding': active_bleeding,
            'oxygen_needed': oxygen_needed,
            'pe_on_anticoagulation': pe_on_anticoagulation,
            'severe_pain': severe_pain,
            'medical_social_reason': medical_social_reason,
            'crcl_low': crcl_low,
            'liver_impairment': liver_impairment,
            'pregnant': pregnant,
            'hit_history': hit_history
        }
        
        result = calculate_hestia_score(criteria)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "HIGH": "🚨",
            "LOW": "✅"
        }
        icon = icon_map.get(result['risk_class'], "🫁")
        
        render_score_result(
            title="Hestia Score",
            score=f"{len(result['positive_criteria'])}/11",
            interpretation=f"{result['interpretation']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Details
        with st.expander("📋 Chi tiết đánh giá", expanded=False):
            st.markdown("### Các tiêu chí:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            if result['positive_criteria']:
                st.markdown("### ⚠️ Tiêu chí chống chỉ định phát hiện:")
                for criterion in result['positive_criteria']:
                    st.markdown(f"- **{criterion}**")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['eligible']:
            st.success(f"""
            **Đủ điều kiện điều trị ngoại trú** ✅
            
            - **Khuyến nghị:** {result['recommendation']}
            - Không có tiêu chí chống chỉ định
            - Có thể cân nhắc điều trị ngoại trú với thuốc kháng đông
            - Đảm bảo bệnh nhân có thể tuân thủ điều trị và theo dõi
            - Hướng dẫn quay lại nếu triệu chứng xấu đi
            """)
        else:
            st.error(f"""
            **Không đủ điều kiện điều trị ngoại trú** 🚨
            
            - Phát hiện **{len(result['positive_criteria'])}** tiêu chí chống chỉ định
            - **Khuyến nghị:** {result['recommendation']}
            - Cần nhập viện để điều trị và theo dõi
            - Điều trị kháng đông và hỗ trợ phù hợp
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - Hestia Score giúp xác định bệnh nhân PE có thể điều trị ngoại trú
        - **Đủ điều kiện:** Có thể cân nhắc điều trị ngoại trú với thuốc kháng đông
        - **Không đủ điều kiện:** Cần nhập viện để điều trị và theo dõi
        - Kết hợp với đánh giá lâm sàng và khả năng tuân thủ điều trị
        - Đảm bảo bệnh nhân có thể tiếp cận chăm sóc y tế nếu cần
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'hestia',
            'calculator_name': 'Hestia Score',
            'inputs': criteria,
            'results': {
                'eligible': result['eligible'],
                'positive_criteria_count': len(result['positive_criteria']),
                'interpretation': result['interpretation'],
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
    references = get_references('hestia')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Zondag W, et al. Outpatient treatment in patients with acute pulmonary embolism: 
          the Hestia Study. J Thromb Haemost. 2011;9(8):1500-1507.
        """)
    
    # History
    render_history_ui(calculator_id="hestia", show_actions=True)
