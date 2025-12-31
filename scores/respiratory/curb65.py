"""
CURB-65 Score
Community-Acquired Pneumonia severity assessment
"""

import streamlit as st
from scores.utils.validation import (
    validate_age,
    validate_respiratory_rate,
    validate_blood_pressure,
    validate_lab_value
)
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
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
    """CURB-65 Score Calculator"""
    st.subheader("🫁 CURB-65")
    st.caption("Mức độ Nặng Viêm Phổi Cộng Đồng")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'curb65':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        # Pre-fill inputs from shared result (optional)
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        # Pre-fill from shared result if available
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        confusion = st.checkbox(
            "**C** - Confusion (Lú lẫn)",
            help="Mới xuất hiện hoặc AMT ≤8",
            value=shared_inputs.get('Confusion') == 'Có' if shared_inputs else False
        )
        
        # Urea with unit conversion
        st.markdown("#### **U** - Urea")
        urea_unit = st.radio(
            "Đơn vị:",
            ["mmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="urea_unit_curb65"
        )
        
        if urea_unit == "mmol/L":
            urea_input = st.number_input(
                "Urea (mmol/L)",
                min_value=0.0,
                max_value=70.0,
                value=7.0,
                step=0.5,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L",
                key="urea_mmol"
            )
            urea_mmol = urea_input
            st.caption(f"≈ {urea_mmol * 2.8:.1f} mg/dL")
        else:
            urea_input = st.number_input(
                "Urea (mg/dL)",
                min_value=0.0,
                max_value=200.0,
                value=20.0,
                step=1.0,
                format="%.0f",
                help="BUN (Blood Urea Nitrogen)",
                key="urea_mgdl"
            )
            urea_mmol = urea_input / 2.8  # Convert to mmol/L
            st.caption(f"≈ {urea_mmol:.1f} mmol/L")
        
        urea_high = urea_mmol > 7.0  # >7 mmol/L (>20 mg/dL)
        
        # Respiratory rate
        rr = st.number_input(
            "**R** - Nhịp thở (nhịp thở/phút)",
            min_value=0,
            max_value=60,
            value=18,
            step=1,
            format="%d",
            help="Bình thường: 12-20/phút"
        )
        
        # Blood pressure
        sbp = st.number_input(
            "**B** - Systolic BP (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=5,
            format="%d"
        )
        
        dbp = st.number_input(
            "Diastolic BP (mmHg)",
            min_value=0,
            max_value=200,
            value=80,
            step=5,
            format="%d"
        )
        
        # Age
        age = st.number_input(
            "Tuổi",
            min_value=0,
            max_value=120,
            value=int(shared_inputs.get('Age', 50)) if shared_inputs and shared_inputs.get('Age') else 50,
            step=1
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="curb65",
            calculator_name="CURB-65",
            category="Hô Hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information - Enhanced with Phase 1 Metadata
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("curb65")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về CURB-65 Score",
                content="""
                **CURB-65 Score** đánh giá mức độ nặng của viêm phổi cộng đồng (CAP):
                
                - Giúp quyết định nơi điều trị (ngoại trú, nhập viện, ICU)
                - Dự đoán tử vong 30 ngày
                - Sử dụng rộng rãi trong thực hành lâm sàng
                
                **5 tiêu chí:**
                - **C:** Confusion** (Lú lẫn) - AMT ≤8
                - **U:** Urea >7 mmol/L (hoặc >19 mg/dL)
                - **R:** Respiratory rate ≥30/min
                - **B:** Blood pressure <90/60 mmHg
                - **65:** Age ≥65
                
                **Tổng điểm: 0-5**
                """,
                when_to_use="""
                **Sử dụng CURB-65 Score khi:**
                - Bệnh nhân có chẩn đoán viêm phổi cộng đồng
                - Cần quyết định nơi điều trị (ngoại trú vs nhập viện vs ICU)
                - Đánh giá mức độ nặng và tiên lượng
                - Hướng dẫn điều trị kháng sinh
                """,
                limitations="""
                **Hạn chế:**
                - Không áp dụng cho viêm phổi bệnh viện (HAP/VAP)
                - Cần có đầy đủ thông tin lâm sàng và xét nghiệm
                - Không thay thế đánh giá lâm sàng
                - Một số yếu tố có thể không có sẵn (urea)
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - **0-1 điểm:** Ngoại trú, kháng sinh uống
                - **2 điểm:** Nhập viện, kháng sinh IV
                - **3-5 điểm:** Nhập viện hoặc ICU, kháng sinh IV, theo dõi sát
                - CURB-65 ≥3: Nguy cơ tử vong cao (>15%), cần điều trị tích cực
                """
            )
            
            # Evidence citation
            render_evidence_citation(
                citation_text="Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study. Thorax. 2003;58(5):377-82.",
                doi="10.1136/thorax.58.5.377",
                pmid="12728155"
            )
        
        if st.button("🧮 Tính CURB-65", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 0, 120)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            is_valid_rr, rr_error = validate_respiratory_rate(rr)
            if not is_valid_rr:
                validation_errors.append(rr_error)
            
            is_valid_bp, bp_error = validate_blood_pressure(sbp, dbp)
            if not is_valid_bp:
                validation_errors.append(bp_error)
            
            # Validate urea
            if urea_unit == "mmol/L":
                is_valid_urea, urea_error = validate_lab_value(urea_mmol, "Urea (mmol/L)", 0, 70)
            else:
                is_valid_urea, urea_error = validate_lab_value(urea_input, "Urea (mg/dL)", 0, 200)
            if not is_valid_urea:
                validation_errors.append(urea_error)
            
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
            
            score = 0
            details = []
            
            if confusion:
                score += 1
                details.append("✓ Confusion - Lú lẫn (+1)")
            
            if urea_high:
                score += 1
                details.append(f"✓ Urea >7 mmol/L ({urea_mmol:.1f}) (+1)")
            
            if rr >= 30:
                score += 1
                details.append(f"✓ RR ≥30/phút ({rr}) (+1)")
            
            if sbp < 90 or dbp <= 60:
                score += 1
                details.append(f"✓ BP thấp (SBP<90 hoặc DBP≤60) (+1)")
            
            if age >= 65:
                score += 1
                details.append(f"✓ Tuổi ≥65 ({age}) (+1)")
            
            # Determine risk level and color
            if score == 0:
                risk_level = "Nguy cơ THẤP"
                mortality = "0.7%"
                recommendation = "Điều trị ngoại trú"
                color = "#28a745"  # green
                icon = "✅"
            elif score == 1:
                risk_level = "Nguy cơ THẤP"
                mortality = "2.1%"
                recommendation = "Điều trị ngoại trú hoặc theo dõi ngắn"
                color = "#17a2b8"  # info blue
                icon = "💡"
            elif score == 2:
                risk_level = "Nguy cơ TRUNG BÌNH"
                mortality = "9.2%"
                recommendation = "Cân nhắc nhập viện"
                color = "#fd7e14"  # orange
                icon = "⚠️"
            elif score == 3:
                risk_level = "Nguy cơ CAO"
                mortality = "14.5%"
                recommendation = "Nhập viện, ICU nếu cần"
                color = "#dc3545"  # red
                icon = "❗"
            else:
                risk_level = "Nguy cơ RẤT CAO"
                mortality = "40%"
                recommendation = "Nhập ICU ngay"
                color = "#6c757d"  # dark gray
                icon = "🚨"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="CURB-65 Score",
                    score=score,
                    interpretation=risk_level,
                    mortality=f"Tử vong 30 ngày: {mortality}",
                    color=color,
                    icon=icon,
                    size="large"
                )
            
            # Build breakdown of criteria
            criteria_scores = {}
            if confusion:
                criteria_scores["C - Confusion"] = 1
            if urea_high:
                criteria_scores["U - Urea >7 mmol/L"] = 1
            if rr >= 30:
                criteria_scores["R - RR ≥30/phút"] = 1
            if sbp < 90 or dbp <= 60:
                criteria_scores["B - BP thấp"] = 1
            if age >= 65:
                criteria_scores["65 - Tuổi ≥65"] = 1
            
            if criteria_scores:
                render_score_breakdown(
                    title="Tiêu chí Đánh giá",
                    subscores=criteria_scores,
                    total_score=score
                )
            
            st.markdown("---")
            st.markdown("### 💡 Chi tiết")
            
            if details:
                for d in details:
                    st.write(f"- {d}")
            else:
                st.write("- Không có tiêu chí nào")
            
            # Enhanced result interpretation with Phase 1 metadata
            if CALCULATOR_METADATA_AVAILABLE:
                render_calculator_result_with_interpretation(
                    calculator_id="curb65",
                    result=f"CURB-65 Score: {score}/5",
                    result_value=float(score)
                )
            else:
                st.markdown("---")
                st.markdown("### 💊 Khuyến cáo")
                
                st.info(f"""
                **Tỷ lệ tử vong 30 ngày:** {mortality}
                
                **Khuyến cáo:** {recommendation}
                """)
            
            if score <= 1:
                st.success("""
                **Điều trị ngoại trú:**
                - Amoxicillin hoặc Macrolide
                - Theo dõi tại nhà
                - Tái khám sau 2-3 ngày
                """)
            elif score == 2:
                st.warning("""
                **Cân nhắc nhập viện:**
                - Đánh giá thêm các yếu tố khác
                - Oxy saturation
                - Bệnh lý nền
                - Khả năng tuân thủ điều trị
                """)
            else:
                st.error("""
                **Nhập viện/ICU:**
                - Kháng sinh IV
                - Beta-lactam + Macrolide
                - Hỗ trợ oxy
                - Theo dõi sát
                """)
            
            # Prepare inputs for export and history
            inputs_dict = {
                "Confusion": "Có" if confusion else "Không",
                "Urea": f"{urea_mmol:.1f} mmol/L ({urea_input:.1f} {urea_unit})",
                "Urea High": "Có" if urea_high else "Không",
                "Respiratory Rate": str(rr),
                "Systolic BP": str(sbp),
                "Diastolic BP": str(dbp),
                "Age": str(age)
            }
            
            # Prepare results for export and history
            results_dict = {
                "CURB-65 Score": f"{score} điểm",
                "Risk Level": risk_level,
                "Mortality": mortality,
                "Recommendation": recommendation,
                "Details": "\n".join(details) if details else "Không có tiêu chí nào"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"CURB-65 = {score} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="CURB-65",
                filename="curb65_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="curb65",
                calculator_name="CURB-65",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="curb65",
                calculator_name="CURB-65",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="curb65", show_actions=True)
            
            # References section
            references = get_references("CURB-65")
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
                    **CURB-65 Score**
                    
                    **Tiêu chí (1 điểm mỗi mục):**
                    - **C**: Confusion (AMT ≤8)
                    - **U**: Urea >7 mmol/L (>20 mg/dL BUN)
                    - **R**: Respiratory rate ≥30/min
                    - **B**: Blood pressure (SBP <90 hoặc DBP ≤60 mmHg)
                    - **65**: Age ≥65 years
                    
                    **Tỷ lệ tử vong 30 ngày:**
                    - Score 0-1: 0.7-2.1% (điều trị ngoại trú)
                    - Score 2: 9.2% (cân nhắc nhập viện)
                    - Score 3-5: 14.5-40% (nhập viện/ICU)
                    
                    **Reference:**
                    Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study. Thorax. 2003;58(5):377-382.
                    
                    **Guidelines:**
                    - BTS Guidelines for CAP (2009)
                    - IDSA/ATS Guidelines (2019)
                    """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("CURB-65")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

