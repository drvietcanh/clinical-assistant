"""
Wells Score for Deep Vein Thrombosis (DVT)
===========================================

Clinical prediction rule to estimate the probability of DVT

Reference:
- Wells PS, et al. Value of assessment of pretest probability of deep-vein thrombosis 
  in clinical management. Lancet. 1997;350(9094):1795-1798.
- Wells PS, et al. Evaluation of D-dimer in the diagnosis of suspected deep-vein thrombosis. 
  N Engl J Med. 2003;349(13):1227-1235.

Original Criteria (9 items):
1. Active cancer (treatment ongoing, within 6 months, or palliative) = +1
2. Paralysis, paresis, or recent plaster immobilization of lower extremity = +1
3. Recently bedridden >3 days or major surgery within 12 weeks = +1
4. Localized tenderness along distribution of deep venous system = +1
5. Entire leg swollen = +1
6. Calf swelling >3 cm compared to asymptomatic leg (measured 10 cm below tibial tuberosity) = +1
7. Pitting edema (confined to symptomatic leg) = +1
8. Collateral superficial veins (non-varicose) = +1
9. Alternative diagnosis as likely or more likely than DVT = -2

Interpretation:
- Score ≥2: DVT likely (high probability) → Consider imaging
- Score <2: DVT unlikely (low probability) → Consider D-dimer

Clinical Utility:
- High sensitivity when combined with D-dimer
- Helps reduce unnecessary imaging
- Widely validated across multiple populations
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
from components.ui.scoring import render_score_result, render_score_breakdown

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
# ========== PHASE 1: CALCULATOR ENHANCEMENTS ==========
try:
    from components.calculator_enhancements import (
        render_calculator_explanation,
        render_evidence_citation,
        render_result_interpretation
    )
    CALCULATOR_ENHANCEMENTS_AVAILABLE = True
except ImportError:
    CALCULATOR_ENHANCEMENTS_AVAILABLE = False

# ========== PHASE 1: CALCULATOR METADATA ==========
try:
    from components.phase1_calculator_metadata import (
        render_calculator_education,
        render_calculator_result_with_interpretation,
        get_calculator_metadata
    )
    CALCULATOR_METADATA_AVAILABLE = True
except ImportError:
    CALCULATOR_METADATA_AVAILABLE = False
# ===================================================


def calculate_wells_dvt(
    active_cancer: bool,
    paralysis_immobilization: bool,
    bedridden_surgery: bool,
    localized_tenderness: bool,
    entire_leg_swollen: bool,
    calf_swelling: bool,
    pitting_edema: bool,
    collateral_veins: bool,
    alternative_diagnosis: bool
) -> dict:
    """
    Calculate Wells DVT Score
    
    Args:
        active_cancer: Active cancer (treatment ongoing, within 6 months, or palliative)
        paralysis_immobilization: Paralysis, paresis, or recent plaster immobilization
        bedridden_surgery: Recently bedridden >3 days or major surgery within 12 weeks
        localized_tenderness: Localized tenderness along deep venous system
        entire_leg_swollen: Entire leg swollen
        calf_swelling: Calf swelling >3 cm compared to asymptomatic leg
        pitting_edema: Pitting edema (confined to symptomatic leg)
        collateral_veins: Collateral superficial veins (non-varicose)
        alternative_diagnosis: Alternative diagnosis as likely or more likely than DVT
    
    Returns:
        Dictionary containing score, probability, recommendations, and details
    """
    score = 0
    details = []
    
    # Calculate score
    if active_cancer:
        score += 1
        details.append("✓ Ung thư đang hoạt động (+1 điểm)")
    
    if paralysis_immobilization:
        score += 1
        details.append("✓ Liệt/bất động chân gần đây (+1 điểm)")
    
    if bedridden_surgery:
        score += 1
        details.append("✓ Nằm liệt giường >3 ngày hoặc phẫu thuật lớn trong 12 tuần (+1 điểm)")
    
    if localized_tenderness:
        score += 1
        details.append("✓ Đau chạm khu trú dọc hệ tĩnh mạch sâu (+1 điểm)")
    
    if entire_leg_swollen:
        score += 1
        details.append("✓ Toàn bộ chân phù (+1 điểm)")
    
    if calf_swelling:
        score += 1
        details.append("✓ Bắp chân phù >3 cm so với chân bên kia (+1 điểm)")
    
    if pitting_edema:
        score += 1
        details.append("✓ Phù lõm (chỉ ở chân triệu chứng) (+1 điểm)")
    
    if collateral_veins:
        score += 1
        details.append("✓ Tĩnh mạch nông nối bên (+1 điểm)")
    
    if alternative_diagnosis:
        score -= 2
        details.append("✓ Chẩn đoán khác có khả năng tương đương/cao hơn DVT (-2 điểm)")
    
    # Determine probability and recommendations
    if score >= 2:
        probability = "CÓ KHẢ NĂNG CAO (DVT Likely)"
        probability_percent = "Nguy cơ DVT: ~28-34% (trước xét nghiệm)"
        risk_class = "HIGH"
        recommendation = """
        **🔴 Xử trí khuyến cáo:**
        
        1. **Cận Lâm sàng:**
           - Siêu âm tĩnh mạch chân (Duplex ultrasound) - NGAY
           - Nếu siêu âm âm tính nhưng nghi ngờ cao → xem xét chụp CT/MRI tĩnh mạch
        
        2. **D-dimer:**
           - Không khuyến cáo khi xác suất cao (âm tính vẫn cần hình ảnh)
           - Chỉ xem xét nếu không thể làm siêu âm ngay
        
        3. **Xử trí**
           - Cân nhắc bắt đầu kháng đông nếu siêu âm chậm trễ và không có chống chỉ định
           - Theo dõi triệu chứng suy tĩnh mạch, thuyên tắc phổi
        
        4. **Lưu ý:**
           - Wells ≥2: Sensitivity ~86%, Specificity ~47%
           - PPV ~28-34%, NPV ~93-96%
        """
        education = """
        **💡 Diễn giải:**
        - Điểm Wells ≥2 → DVT có khả năng cao
        - Siêu âm tĩnh mạch là tiêu chuẩn vàng
        - Nếu siêu âm âm tính + D-dimer âm tính → loại trừ DVT
        - Nếu siêu âm dương tính → bắt đầu điều trị kháng đông
        """
        color = "🔴"
    else:  # score < 2
        probability = "KHẢ NĂNG THẤP (DVT Unlikely)"
        probability_percent = "Nguy cơ DVT: ~3-6% (trước xét nghiệm)"
        risk_class = "LOW"
        recommendation = """
        **🟢 Xử trí khuyến cáo:**
        
        1. **D-dimer:**
           - Xét nghiệm D-dimer trước tiên
           - D-dimer âm tính (age-adjusted) → loại trừ DVT (NPV ~99%)
           - D-dimer dương tính → tiến hành siêu âm tĩnh mạch
        
        2. **Chiến lược 2 bước:**
           ```
           Wells <2 → D-dimer
                ├─ Âm tính → Loại trừ DVT, tìm chẩn đoán khác
                └─ Dương tính → Siêu âm tĩnh mạch chân
           ```
        
        3. **Theo dõi:**
           - Nếu D-dimer âm: giải thích, tư vấn
           - Nếu D-dimer dương: siêu âm trong 24-48h
           - Tái khám nếu triệu chứng tiến triển
        
        4. **Lưu ý:**
           - Wells <2 + D-dimer âm: NPV ~99% → an toàn loại trừ DVT
           - D-dimer dương tính không đồng nghĩa với DVT (nhiều nguyên nhân khác)
        """
        education = """
        **💡 Diễn giải:**
        - Điểm Wells <2 → DVT ít có khả năng
        - Nên dùng D-dimer để loại trừ (tránh siêu âm không cần thiết)
        - D-dimer âm tính + Wells <2 → NPV cực cao (~99%)
        - Nếu D-dimer dương → vẫn cần siêu âm để xác định
        """
        color = "🟢"
    
    return {
        'score': score,
        'probability': probability,
        'probability_percent': probability_percent,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'education': education,
        'details': details,
        'color': color
    }


def render():
    """Render Wells DVT Score calculator in Streamlit"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'wells_dvt':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Wells DVT Score')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🩸 Wells Score - Deep Vein Thrombosis (DVT)")
    st.markdown("**Đánh giá xác suất tiền test của huyết khối tĩnh mạch sâu**")
    
    # Educational information - Enhanced with Phase 1 Metadata
    if CALCULATOR_METADATA_AVAILABLE:
        render_calculator_education("wells_dvt")
    elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
        render_calculator_explanation(
            title="Về Wells DVT Score",
            content="""
            **Wells DVT Score** là thang điểm lâm sàng được sử dụng rộng rãi để:
            
            - Đánh giá xác suất tiền test của DVT
            - Hướng dẫn chiến lược xét nghiệm (D-dimer vs siêu âm)
            - Giảm thiểu các xét nghiệm không cần thiết
            
            **9 tiêu chí lâm sàng:**
            - 8 tiêu chí dương tính (+1 điểm mỗi tiêu chí)
            - 1 tiêu chí âm tính: Chẩn đoán thay thế có khả năng cao hơn (-2 điểm)
            
            **Tổng điểm: -2 đến +8**
            """,
            when_to_use="""
            **Sử dụng Wells DVT Score khi:**
            - Bệnh nhân có triệu chứng nghi ngờ DVT (đau chân, phù, đỏ)
            - Cần quyết định chiến lược xét nghiệm
            - Giảm thiểu xét nghiệm không cần thiết
            - Kết hợp với D-dimer để tối ưu hóa chẩn đoán
            """,
            limitations="""
            **Hạn chế:**
            - Cần đánh giá lâm sàng chính xác
            - Không thay thế xét nghiệm chẩn đoán
            - Cần kết hợp với D-dimer hoặc siêu âm
            - Độ nhạy và độ đặc hiệu phụ thuộc vào kinh nghiệm người đánh giá
            """,
            clinical_context="""
            **Bối cảnh lâm sàng:**
            - Wells Score ≥2: DVT likely → Siêu âm ngay (bỏ qua D-dimer)
            - Wells Score <2: DVT unlikely → D-dimer trước, nếu dương tính mới siêu âm
            - Kết hợp Wells Score + D-dimer giúp giảm 30-50% số lượng siêu âm không cần thiết
            """
        )
        
        # Evidence citation
        render_evidence_citation(
            citation_text="Wells PS, et al. Value of assessment of pretest probability of deep-vein thrombosis in clinical management. Lancet. 1997;350(9094):1795-1798.",
            doi="10.1016/s0140-6736(97)08140-3",
            pmid="9428249"
        )
    else:
        # Fallback to original expander
        with st.expander("ℹ️ Thông tin & cách sử dụng"):
            st.markdown("""
            ### 📋 Giới Thiệu
            
            **Wells DVT Score** là thang điểm lâm sàng được sử dụng rộng rãi để:
            - Đánh giá xác suất tiền test của DVT
            - Hướng dẫn chiến lược xét nghiệm (D-dimer vs siêu âm)
            - Giảm thiểu các xét nghiệm không cần thiết
            
            ### 🎯 Cách Sử dụng
            
            1. **Thời Điểm:** Khi bệnh nhân có triệu chứng nghi ngờ DVT (đau chân, phù, đỏ)
            2. **Đánh giá:** Trả lời 9 câu hỏi lâm sàng
            3. **Kết quả:**
               - **≥2 điểm:** DVT likely → Siêu âm ngay
               - **<2 điểm:** DVT unlikely → D-dimer trước
        
        ### 📊 Độ chính xác        
        | Điểm Wells | Tỷ lệ DVT | Chiến Lược |
        |------------|-----------|------------|
        | ≥2 (likely) | 28-34% | Siêu âm trực tiếp |
        | <2 (unlikely) | 3-6% | D-dimer + siêu âm nếu (+) |
        
        **Wells <2 + D-dimer âm tính:** NPV ~99% → An toàn loại trừ DVT
        
        ### ⚠️ Lưu ý
        
        - **Không thay thế** đánh giá lâm sàng toàn diện
        - Kết hợp với D-dimer age-adjusted (tuổi >50)
        - Cân nhắc yếu tố nguy cơ khác (thrombophilia, tiền sử gia đình)
        - Nếu nghi ngờ cao bất thường → xem xét hình ảnh dù điểm thấp
        
        ### 📚 Tài liệu tham khảo
        
        - Wells PS, et al. *Lancet* 1997;350:1795-1798
        - Wells PS, et al. *N Engl J Med* 2003;349:1227-1235
        - ACCP Evidence-Based Clinical Practice Guidelines (9th Edition)
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập Thông tin lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🏥 Tiền sử & yếu tố nguy cơ")
        active_cancer = st.checkbox(
            "**Ung thư đang hoạt động**",
            help="Đang điều trị, trong 6 tháng qua, hoặc điều trị giảm nhẹ"
        )
        
        paralysis_immobilization = st.checkbox(
            "**Liệt/Bất động chân gần đây**",
            help="Liệt, giảm vận động, hoặc bó bột chi dưới"
        )
        
        bedridden_surgery = st.checkbox(
            "**Nằm liệt giường >3 ngày HOẶC phẫu thuật lớn trong 12 tuần**",
            help="Phẫu thuật cần gây mê >30 phút"
        )
    
    with col2:
        st.markdown("##### 🔍 Triệu chứng lâm sàng")
        localized_tenderness = st.checkbox(
            "**Đau chạm khu trú dọc hệ tĩnh mạch sâu**",
            help="Đau dọc theo đường đi của tĩnh mạch đùi hoặc tĩnh mạch khoeo"
        )
        
        entire_leg_swollen = st.checkbox(
            "**Toàn bộ chân phù**",
            help="Phù lan rộng toàn bộ chi dưới"
        )
        
        calf_swelling = st.checkbox(
            "**Bắp chân phù >3 cm so với chân bên kia**",
            help="Đo chu vi bắp chân cách mỏm chày 10 cm"
        )
    
    st.markdown("##### 🩺 Khám Lâm sàng")
    col3, col4 = st.columns(2)
    
    with col3:
        pitting_edema = st.checkbox(
            "**Phù lõm (chỉ ở chân triệu chứng)**",
            help="Ấn tạo lõm, không phải phù toàn thân"
        )
        
        collateral_veins = st.checkbox(
            "**Tĩnh mạch nông nối bên (không giãn tĩnh mạch)**",
            help="Tĩnh mạch nông nối bên rõ, không phải giãn tĩnh mạch mạn tính"
        )
    
    with col4:
        alternative_diagnosis = st.checkbox(
            "**Chẩn đoán khác có khả năng ≥ DVT**",
            help="Ví dụ: Cellulitis, tổn thương cơ, vỡ nang Baker, phù lympho"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính toán Wells DVT Score", type="primary", use_container_width=True):
        result = calculate_wells_dvt(
            active_cancer=active_cancer,
            paralysis_immobilization=paralysis_immobilization,
            bedridden_surgery=bedridden_surgery,
            localized_tenderness=localized_tenderness,
            entire_leg_swollen=entire_leg_swollen,
            calf_swelling=calf_swelling,
            pitting_edema=pitting_edema,
            collateral_veins=collateral_veins,
            alternative_diagnosis=alternative_diagnosis
        )
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Determine risk level for color coding
        if result['score'] >= 2:
            risk_level_code = 'high'  # DVT likely
        else:
            risk_level_code = 'low'  # DVT unlikely
        
        # Display score with color coding badge
        st.markdown(f"## Wells DVT Score = {result['score']}")
        render_risk_badge(
            risk_level=risk_level_code,
            label=result['probability'],
            value=result['score']
        )
        
        # Map color emoji to hex
        color_map_hex = {
            "🔴": "#dc3545",
            "🟢": "#28a745"
        }
        score_color = color_map_hex.get(result['color'], "#6c757d")
        
        # Use render_score_result for main score display
        render_score_result(
            title="Wells DVT Score",
            score=result['score'],
            interpretation=result['probability'],
            mortality=result['probability_percent'],
            color=score_color,
            icon=result['color'],
            size="large"
        )
        
        # Enhanced result interpretation with Phase 1 metadata
        if CALCULATOR_METADATA_AVAILABLE:
            render_calculator_result_with_interpretation(
                calculator_id="wells_dvt",
                result=f"Wells DVT Score: {result['score']}",
                result_value=float(result['score'])
        )
        
        # Visual Charts
        st.markdown("---")
        st.markdown("### 📊 Biểu Đồ Nguy Cơ")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            render_risk_gauge_chart(
                value=result['score'],
                min_value=-2,  # Wells can be negative
                max_value=9,
                thresholds={
                    'Low': 0,
                    'Moderate': 1,
                    'High': 2
                },
                title="Wells DVT Score"
            )
        
        with col_chart2:
            render_risk_bar_chart(
                value=result['score'],
                thresholds={
                    'Low': 0,
                    'Moderate': 1,
                    'High': 2
                },
                max_value=9,
                title="Risk Level",
                show_value=True
            )
        
        # Details
        if result['details']:
            with st.expander("📋 Chi tiết tính điểm", expanded=True):
                for detail in result['details']:
                    st.markdown(f"- {detail}")
        
        # Recommendations
        st.markdown("---")
        st.markdown(result['recommendation'])
        
        # Education
        with st.expander("💡 Diễn giải kết quả"):
            st.markdown(result['education'])
        
        # Additional clinical context
        st.info("""
        **🔍 Chiến Lược Chẩn đoán Theo Wells DVT:**
        
        ```
        Nghi ngờ DVT
            ↓
        Tính Wells DVT Score
            ├─ ≥2 điểm (DVT likely)
            │   └─ Siêu âm tĩnh mạch chân NGAY
            │       ├─ Dương tính → Điều trị kháng đông
            │       └─ Âm tính → Xem xét CT/MR tĩnh mạch nếu nghi ngờ cao
            │
            └─ <2 điểm (DVT unlikely)
                └─ Xét nghiệm D-dimer
                    ├─ Âm tính → Loại trừ DVT (NPV ~99%)
                    └─ Dương tính → Siêu âm tĩnh mạch chân
        ```
        
        **💊 Lưu ý điều trị:**
        - Nếu siêu âm trì hoãn + Wells ≥2 + không chống chỉ định → cân nhắc kháng đông ngay
        - Theo dõi triệu chứng thuyên tắc phổi (chest pain, SOB, hemoptysis)
        """)
        
        # Save to session state
        st.session_state['wells_dvt_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Cảnh báo Y Khoa:**
        - Thang điểm Wells DVT là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
        - Kết hợp với D-dimer và hình ảnh học để chẩn đoán chính xác
        - Nếu nghi ngờ thuyên tắc phổi → đánh giá thêm Wells PE hoặc PERC
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Active Cancer": "Yes" if active_cancer else "No",
            "Paralysis/Immobilization": "Yes" if paralysis_immobilization else "No",
            "Bedridden/Surgery": "Yes" if bedridden_surgery else "No",
            "Localized Tenderness": "Yes" if localized_tenderness else "No",
            "Entire Leg Swollen": "Yes" if entire_leg_swollen else "No",
            "Calf Swelling": "Yes" if calf_swelling else "No",
            "Pitting Edema": "Yes" if pitting_edema else "No",
            "Collateral Veins": "Yes" if collateral_veins else "No",
            "Alternative Diagnosis": "Yes" if alternative_diagnosis else "No"
        }
        
        results_dict = {
            "Wells DVT Score": f"{result['score']}",
            "Probability": result['probability'],
            "Risk Class": result['risk_class']
        }
        
        # Export section (new component)
        render_scores_export(
            calculator_name="Wells DVT Score",
            inputs=inputs_dict,
            results=results_dict,
            specialty="Huyết học & Đông máu"
        )
        
        # Keep old export for compatibility
        st.markdown("---")
        from components.export import render_export_section
        render_export_section(
            title="Wells DVT Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Wells DVT Score"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="wells_dvt",
            calculator_name="Wells DVT Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="wells_dvt",
            calculator_name="Wells DVT Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="wells_dvt", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="wells_dvt",
            calculator_name="Wells DVT Score",
            category="Huyết học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Quick reference
    with st.expander("📖 Bảng tham khảo Nhanh"):
        st.markdown("""
        ### Wells DVT Score - Tiêu chí
        
        | Tiêu chí | Điểm |
        |----------|------|
        | Ung thư đang hoạt động | +1 |
        | Liệt/bất động chân | +1 |
        | Nằm liệt giường >3 ngày/phẫu thuật lớn <12 tuần | +1 |
        | Đau chạm dọc tĩnh mạch sâu | +1 |
        | Toàn bộ chân phù | +1 |
        | Bắp chân phù >3 cm so với bên kia | +1 |
        | Phù lõm (chân triệu chứng) | +1 |
        | Tĩnh mạch nông nối bên | +1 |
        | Chẩn đoán khác có khả năng ≥ DVT | -2 |
        
        ### Phân tầng Nguy cơ
        
        | Điểm Wells | Phân loại | Tỷ lệ DVT | Xử trí|
        |------------|-----------|-----------|--------|
        | ≥2 | DVT likely | 28-34% | Siêu âm trực tiếp |
        | <2 | DVT unlikely | 3-6% | D-dimer → Siêu âm nếu (+) |
        
        ### D-dimer Age-Adjusted Cutoff
        
        - **<50 tuổi:** 500 ng/mL
        - **≥50 tuổi:** Tuổi × 10 ng/mL
        - Ví dụ: 65 tuổi → cutoff = 650 ng/mL
        
        ### Chẩn đoán Phân biệt (Alternative Diagnosis)
        
        - Cellulitis / Nhiễm trùng da mô mềm
        - Tổn thương cơ / Rách cơ
        - Vỡ nang Baker
        - Phù lympho / Suy tĩnh mạch mạn
        - Hội chứng sau huyết khối
        - Bệnh lý khớp (viêm khớp, viêm bao hoạt dịch)
        """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Wells DVT Score")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

