"""
TIMI Risk Score Calculator
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
from components.ui.scoring import render_score_result
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


def render():
    """TIMI Risk Score Calculator"""
    # st.subheader("💔 TIMI Risk Score")
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>💔 TIMI Risk Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Đánh giá nguy cơ trong UA/NSTEMI")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'timi':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information - Enhanced with Phase 1 Metadata
    if CALCULATOR_METADATA_AVAILABLE:
        render_calculator_education("timi")
    elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
        render_calculator_explanation(
            title="Về TIMI Risk Score",
            content="""
            **TIMI Risk Score** dự đoán tử vong, nhồi máu cơ tim mới hoặc cần tái can thiệp trong 14 ngày:
            
            - Sử dụng cho bệnh nhân UA/NSTEMI
            - Hướng dẫn chiến lược điều trị (invasive vs conservative)
            - Dự đoán kết quả lâm sàng
            
            **7 tiêu chí:**
            1. Tuổi ≥65
            2. ≥3 yếu tố nguy cơ mạch vành
            3. Bệnh mạch vành đã biết (hẹp ≥50%)
            4. ST chênh xuống ≥0.5mm
            5. ≥2 cơn đau ngực trong 24h
            6. Aspirin trong 7 ngày qua
            7. Tăng troponin/CK-MB
            
            **Tổng điểm: 0-7**
            """,
            when_to_use="""
            **Sử dụng TIMI Risk Score khi:**
            - Bệnh nhân có UA/NSTEMI
            - Cần quyết định chiến lược điều trị (invasive vs conservative)
            - Đánh giá tiên lượng và kết quả lâm sàng
            - Hướng dẫn thời điểm can thiệp mạch vành
            """,
            limitations="""
            **Hạn chế:**
            - Chỉ áp dụng cho UA/NSTEMI, không áp dụng cho STEMI
            - Cần có đầy đủ thông tin lâm sàng và xét nghiệm
            - Không thay thế đánh giá lâm sàng cá thể hóa
            - Một số yếu tố có thể không có sẵn ngay
            """,
            clinical_context="""
            **Bối cảnh lâm sàng:**
            - **TIMI 0-2:** Nguy cơ thấp → Cân nhắc điều trị bảo tồn
            - **TIMI 3-4:** Nguy cơ trung bình → Cân nhắc can thiệp sớm
            - **TIMI 5-7:** Nguy cơ cao → Khuyến cáo can thiệp sớm (<48h)
            - TIMI cao liên quan đến tử vong và biến cố tim mạch cao hơn
            """
        )
        
        # Evidence citation
        render_evidence_citation(
            citation_text="Antman EM, et al. The TIMI risk score for unstable angina/non-ST elevation MI: A method for prognostication and therapeutic decision making. JAMA. 2000;284(7):835-42.",
            doi="10.1001/jama.284.7.835",
            pmid="10938172"
        )
    else:
        # Fallback to original
        st.info("""
        **TIMI Risk Score** dự đoán tử vong, nhồi máu cơ tim mới hoặc cần tái can thiệp trong 14 ngày.
        """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí (7 Tiêu chuẩn)")
        
        score = 0
        details = []
        
        # Age >= 65
        age_65 = st.checkbox(
            "**Tuổi ≥ 65**",
            help="1 điểm nếu tuổi ≥65",
            key="timi_age"
        )
        if age_65:
            score += 1
            details.append("✓ Tuổi ≥65 (+1)")
        
        # >= 3 CAD risk factors
        st.markdown("**≥ 3 Yếu tố nguy cơ mạch vành**")
        st.caption("THA, ĐTĐ, hút thuốc, cholesterol cao, TSGĐ CHD")
        
        rf_count = 0
        col_rf1, col_rf2 = st.columns(2)
        with col_rf1:
            if st.checkbox("Tăng huyết áp", key="timi_htn"):
                rf_count += 1
            if st.checkbox("Đái tháo đường", key="timi_dm"):
                rf_count += 1
            if st.checkbox("Hút thuốc (hiện tại)", key="timi_smoke"):
                rf_count += 1
        with col_rf2:
            if st.checkbox("Cholesterol cao", key="timi_chol"):
                rf_count += 1
            if st.checkbox("TSGĐ bệnh mạch vành", key="timi_fhx"):
                rf_count += 1
        
        if rf_count >= 3:
            score += 1
            details.append(f"✓ ≥3 yếu tố nguy cơ ({rf_count}) (+1)")
        
        # Known CAD (stenosis >= 50%)
        known_cad = st.checkbox(
            "**Bệnh mạch vành đã biết** (hẹp ≥50%)",
            help="1 điểm nếu có tiền sử can thiệp hoặc hẹp mạch vành đã biết",
            key="timi_cad"
        )
        if known_cad:
            score += 1
            details.append("✓ Bệnh mạch vành đã biết (+1)")
        
        # Aspirin use in past 7 days
        aspirin = st.checkbox(
            "**Dùng Aspirin trong 7 ngày qua**",
            help="1 điểm - nghịch lý cho thấy nguy cơ cao hơn",
            key="timi_aspirin"
        )
        if aspirin:
            score += 1
            details.append("✓ Dùng aspirin 7 ngày qua (+1)")
        
        # Severe angina (>= 2 episodes in 24h)
        severe_angina = st.checkbox(
            "**Đau thắt ngực nặng** (≥2 đợt trong 24h)",
            help="1 điểm nếu có ≥2 đợt đau trong 24h",
            key="timi_angina"
        )
        if severe_angina:
            score += 1
            details.append("✓ Đau thắt ngực nặng (+1)")
        
        # ST changes >= 0.5mm
        st_changes = st.checkbox(
            "**ST chênh ≥ 0.5mm trên ECG**",
            help="ST chênh lên hoặc xuống ≥0.5mm",
            key="timi_st"
        )
        if st_changes:
            score += 1
            details.append("✓ ST chênh ≥0.5mm (+1)")
        
        # Elevated cardiac markers
        elevated_markers = st.checkbox(
            "**Marker tim tăng** (Troponin/CK-MB)",
            help="1 điểm nếu troponin hoặc CK-MB tăng",
            key="timi_markers"
        )
        if elevated_markers:
            score += 1
            details.append("✓ Marker tim tăng (+1)")
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="timi",
            calculator_name="TIMI Risk Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🧮 Tính TIMI Risk Score", type="primary", key="timi_calc", use_container_width=True):
            # Determine risk level for color coding
            if score <= 2:
                risk_level = "thấp"
                risk_level_code = "low"
            elif score <= 4:
                risk_level = "trung bình"
                risk_level_code = "moderate"
            else:
                risk_level = "cao"
                risk_level_code = "high"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result
                color_map = {
                    "low": COLORS["success"],
                    "moderate": COLORS["warning"],
                    "high": COLORS["error"]
                }
                color = color_map.get(risk_level_code, COLORS["primary"])
                
                render_score_result(
                    title="TIMI Risk Score",
                    score=f"{score}/7",
                    interpretation=f"Nguy cơ {risk_level.upper()}",
                    mortality=f"Nguy cơ sự kiện (14 ngày): {risk_data.get(score, '>65%')}",
                    color=color,
                    icon="💔",
                    size="large"
                )
                
                # Enhanced result interpretation with Phase 1 metadata
                if CALCULATOR_METADATA_AVAILABLE:
                    render_calculator_result_with_interpretation(
                        calculator_id="timi",
                        result=f"TIMI Risk Score: {score}/7",
                        result_value=float(score)
                    )
            
            # Risk percentages based on score
            risk_data = {
                0: "4.7%",
                1: "8.3%",
                2: "13.2%",
                3: "19.9%",
                4: "26.2%",
                5: "40.9%",
                6: "52.2%",
                7: "65.0%"
            }
            
            st.markdown("### 💡 Chi tiết điểm")
            if details:
                for d in details:
                    st.write(f"- {d}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            # Visual Charts
            st.markdown("---")
            st.markdown("### 📊 Biểu Đồ Nguy Cơ")
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                render_risk_gauge_chart(
                    value=score,
                    min_value=0,
                    max_value=7,
                    thresholds={
                        'Low': 2,
                        'Moderate': 4,
                        'High': 5
                    },
                    title="TIMI Risk Score"
                )
            
            with col_chart2:
                render_risk_bar_chart(
                    value=score,
                    thresholds={
                        'Low': 2,
                        'Moderate': 4,
                        'High': 5
                    },
                    max_value=7,
                    title="Risk Level",
                    show_value=True
                )
            
            st.markdown("---")
            st.markdown("### 📈 Nguy cơ tử vong/MI/Tái can thiệp (14 Ngày)")
            st.metric(
                label="Nguy cơ sự kiện bất lợi",
                value=risk_data.get(score, ">65%"),
                delta=f"TIMI Score = {score}"
            )
            
            st.markdown("### 💊 Khuyến cáo điều trị")
            
            if score <= 2:
                st.success(f"""
                **Nguy cơ {risk_level} ({risk_data.get(score)})**
                
                **Chiến lược bảo tồn (Conservative):**
                - ✅ Có thể xuất viện sớm nếu ổn định
                - Aspirin + P2Y12 inhibitor (DAPT)
                - Statin liều cao
                - Beta-blocker, ACE-I
                - Theo dõi ngoại trú
                - Stress test ngoại trú
                """)
            
            elif score <= 4:
                st.warning(f"""
                **Nguy cơ {risk_level} ({risk_data.get(score)})**
                
                **Chiến lược xâm lấn sớm (Early Invasive):**
                - ⚠️ Nhập viện theo dõi
                - DAPT (Aspirin + Ticagrelor/Prasugrel)
                - Anticoagulation (Enoxaparin/Fondaparinux)
                - Statin liều cao
                - Cân nhắc coronary angiography trong 24-72h
                - Hội chẩn tim mạch
                """)
            
            else:
                st.error(f"""
                **Nguy cơ {risk_level} ({risk_data.get(score)})**
                
                **Chiến lược xâm lấn khẩn cấp (Urgent Invasive):**
                - 🚨 Nhập viện ICU/CCU
                - DAPT ngay (Aspirin + Ticagrelor/Prasugrel)
                - Anticoagulation (Enoxaparin hoặc UFH)
                - GPI (GP IIb/IIIa inhibitor) nếu cần
                - Statin liều cao, Beta-blocker, ACE-I
                - **Coronary angiography KHẨN CẤP (< 24h)**
                - Chuẩn bị PCI/CABG
                """)
            
            # Prepare inputs for export
            inputs_dict = {
                "Age ≥65": "Có" if age_65 else "Không",
                "≥3 CAD Risk Factors": "Có" if rf_count >= 3 else "Không",
                "Known CAD": "Có" if known_cad else "Không",
                "Aspirin in Past 7 Days": "Có" if aspirin else "Không",
                "Severe Angina": "Có" if severe_angina else "Không",
                "ST Deviation": "Có" if st_changes else "Không",
                "Positive Cardiac Marker": "Có" if elevated_markers else "Không"
            }
            
            # Prepare results for export
            results_dict = {
                "TIMI Score": f"{score}/7",
                "Risk Level": risk_level.upper(),
                "Risk Level Code": risk_level_code,
                "14-Day Event Risk": risk_data.get(score, ">65%"),
                "Details": "\n".join(details) if details else "Không có yếu tố nguy cơ"
            }
            
            # Export section (new component)
            st.markdown("---")
            render_scores_export(
                calculator_name="TIMI Risk Score",
                inputs=inputs_dict,
                results=results_dict,
                specialty="Tim mạch"
            )
            
            # Keep old export for compatibility
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"TIMI = {score} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="TIMI Risk Score",
                filename="timi_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="timi",
                calculator_name="TIMI Risk Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="timi",
                calculator_name="TIMI Risk Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="timi", show_actions=True)
            
            # References section
            references = get_references("TIMI")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            else:
                # Fallback to manual references if not in config
                with st.expander("📚 Tài liệu tham khảo"):
                    st.markdown("""
                **TIMI Risk Score for UA/NSTEMI**
                
                **7 Tiêu chuẩn (mỗi mục 1 điểm):**
                1. Age ≥65 years
                2. ≥3 CAD risk factors (HTN, DM, smoking, high cholesterol, family Hx)
                3. Known CAD (stenosis ≥50%)
                4. Aspirin use in past 7 days
                5. Severe angina (≥2 episodes in 24h)
                6. ST deviation ≥0.5mm
                7. Elevated cardiac markers (troponin/CK-MB)
                
                **Score: 0-7**
                
                **Risk of Death/MI/Urgent Revascularization at 14 days:**
                - 0-1: 4.7-8.3% (Low)
                - 2: 13.2% (Low-Intermediate)
                - 3-4: 19.9-26.2% (Intermediate)
                - 5-7: 40.9-65% (High)
                
                **Original Study:**
                - Antman EM et al. JAMA. 2000;284(7):835-842.
                
                **Guidelines:**
                - AHA/ACC 2014 NSTE-ACS Guidelines
                - ESC 2020 ACS Guidelines
                
                **Link:**
                - https://www.mdcalc.com/timi-risk-score-ua-nstemi
                """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("TIMI")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
