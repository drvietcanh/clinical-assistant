"""
CHA₂DS₂-VASc Score Calculator
Stroke risk assessment in atrial fibrillation
"""

import streamlit as st
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
# ===================================================


def render():
    """CHA₂DS₂-VASc Score Calculator"""
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Đánh giá nguy cơ đột quỵ Trong Rung Nhĩ")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'cha2ds2vasc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        # Pre-fill inputs from shared result (optional)
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        # Pre-fill from shared result if available
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        chf = st.checkbox(
            "**C** - Suy tim sung huyết / Rối loạn chức năng thất trái",
            help="Tiền sử suy tim hoặc EF <40%",
            value=shared_inputs.get('CHF') == 'Có' if shared_inputs else False
        )
        
        htn = st.checkbox(
            "**H** - Tăng huyết áp",
            help="Đang điều trị tăng huyết áp hoặc BP >140/90 mmHg",
            value=shared_inputs.get('Hypertension') == 'Có' if shared_inputs else False
        )
        
        age_group = st.radio(
            "**A** - Tuổi",
            ["< 65 tuổi", "65-74 tuổi", "≥ 75 tuổi"],
            horizontal=True,
            index=0 if not shared_inputs else ["< 65 tuổi", "65-74 tuổi", "≥ 75 tuổi"].index(shared_inputs.get('Age Group', "< 65 tuổi")) if shared_inputs.get('Age Group') in ["< 65 tuổi", "65-74 tuổi", "≥ 75 tuổi"] else 0
        )
        
        dm = st.checkbox(
            "**D** - Đái tháo đường",
            help="Đang điều trị hoặc HbA1c ≥6.5%",
            value=shared_inputs.get('Diabetes') == 'Có' if shared_inputs else False
        )
        
        stroke = st.checkbox(
            "**S** - Tiền sử Đột quỵ / TIA / Huyết khối",
            help="Đột quỵ, TIA hoặc tắc mạch hệ thống trước đây",
            value=shared_inputs.get('Stroke/TIA') == 'Có' if shared_inputs else False
        )
        
        vasc = st.checkbox(
            "**V** - Bệnh mạch máu",
            help="Nhồi máu cơ tim, bệnh động mạch ngoại biên, plaque động mạch chủ",
            value=shared_inputs.get('Vascular Disease') == 'Có' if shared_inputs else False
        )
        
        sex = st.radio(
            "**Sc** - Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            index=0 if not shared_inputs else (1 if shared_inputs.get('Sex') == 'Nữ' else 0)
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="cha2ds2vasc",
            calculator_name="CHA₂DS₂-VASc Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information - Enhanced with Phase 1
        if CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về CHA₂DS₂-VASc Score",
                content="""
                **CHA₂DS₂-VASc Score** đánh giá nguy cơ đột quỵ ở bệnh nhân rung nhĩ (AF):
                
                - Sử dụng để quyết định có cần kháng đông hay không
                - Kết hợp với HAS-BLED để cân nhắc lợi ích/nguy cơ
                - CHA₂DS₂-VASc ≥2 (nam) hoặc ≥3 (nữ): Khuyến cáo kháng đông
                
                **9 yếu tố nguy cơ:**
                - **C:** Congestive heart failure / LV dysfunction
                - **H:** Hypertension
                - **A:** Age (≥75 = 2 điểm, 65-74 = 1 điểm)
                - **D:** Diabetes
                - **S:** Stroke/TIA/thromboembolism (2 điểm)
                - **V:** Vascular disease
                - **A:** Age 65-74 (1 điểm)
                - **Sc:** Sex category (nữ = 1 điểm)
                
                **Tổng điểm: 0-9**
                """,
                when_to_use="""
                **Sử dụng CHA₂DS₂-VASc Score khi:**
                - Bệnh nhân có rung nhĩ (AF) cần đánh giá nguy cơ đột quỵ
                - Quyết định có cần kháng đông hay không
                - Kết hợp với HAS-BLED để cân nhắc lợi ích/nguy cơ
                - Theo dõi nguy cơ đột quỵ trong quá trình điều trị
                """,
                limitations="""
                **Hạn chế:**
                - Không áp dụng cho rung nhĩ do bệnh van tim (cần kháng đông bắt buộc)
                - Cần kết hợp với HAS-BLED để đánh giá toàn diện
                - Một số yếu tố có thể thay đổi theo thời gian
                - Không thay thế đánh giá lâm sàng cá thể hóa
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - **Nam giới:**
                  - CHA₂DS₂-VASc = 0: Không cần kháng đông
                  - CHA₂DS₂-VASc = 1: Cân nhắc kháng đông
                  - CHA₂DS₂-VASc ≥2: Khuyến cáo kháng đông
                - **Nữ giới:**
                  - CHA₂DS₂-VASc = 0-1: Cân nhắc kháng đông
                  - CHA₂DS₂-VASc ≥2: Khuyến cáo kháng đông
                - Luôn kết hợp với HAS-BLED để đánh giá nguy cơ chảy máu
                """
            )
            
            # Evidence citation
            render_evidence_citation(
                citation_text="Lip GY, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the euro heart survey on atrial fibrillation. Chest. 2010;137(2):263-72.",
                doi="10.1378/chest.09-1584",
                pmid="19762550"
            )
        
        if st.button("🧮 Tính Điểm", type="primary", key="cha2ds2vasc_calc"):
            score = 0
            details = []
            
            if chf:
                score += 1
                details.append("✓ Suy tim (+1)")
            if htn:
                score += 1
                details.append("✓ Tăng huyết áp (+1)")
            if age_group == "65-74 tuổi":
                score += 1
                details.append("✓ Tuổi 65-74 (+1)")
            elif age_group == "≥ 75 tuổi":
                score += 2
                details.append("✓ Tuổi ≥75 (+2)")
            if dm:
                score += 1
                details.append("✓ Đái tháo đường (+1)")
            if stroke:
                score += 2
                details.append("✓ Tiền sử đột quỵ/TIA (+2)")
            if vasc:
                score += 1
                details.append("✓ Bệnh mạch máu (+1)")
            if sex == "Nữ":
                score += 1
                details.append("✓ Giới tính nữ (+1)")
            
            # Determine risk level for color coding
            if score == 0:
                risk_level = 'very_low'
                risk_text = "THẤP"
                risk = "0-0.2%/năm"
            elif score == 1:
                risk_level = 'low'
                risk_text = "TRUNG BÌNH"
                risk = "0.6-2.0%/năm"
            elif score == 2:
                risk_level = 'moderate'
                risk_text = "TRUNG BÌNH-CAO"
                risk = "2.2%/năm"
            elif score <= 4:
                risk_level = 'high'
                risk_text = "CAO"
                if score <= 5:
                    risk = f"{2.2 + (score-2)*1.5:.1f}%/năm"
                else:
                    risk = ">10%/năm"
            else:
                risk_level = 'very_high'
                risk_text = "RẤT CAO"
                risk = ">10%/năm"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Display score with color coding
                st.markdown(f"## CHA₂DS₂-VASc = {score}")
                render_risk_badge(
                    risk_level=risk_level,
                    label=f"Nguy cơ: {risk_text}",
                    value=score
                )
            
            st.markdown("### 💡 Giải thích & Khuyến cáo")
            st.markdown(f"**Nguy cơ đột quỵ hàng năm:** {risk}")
            
            # Visual Charts
            st.markdown("---")
            st.markdown("### 📊 Biểu Đồ Nguy Cơ")
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                render_risk_gauge_chart(
                    value=score,
                    min_value=0,
                    max_value=9,
                    thresholds={
                        'Low': 1,
                        'Moderate': 2,
                        'High': 4
                    },
                    title="CHA₂DS₂-VASc Score"
                )
            
            with col_chart2:
                render_risk_bar_chart(
                    value=score,
                    thresholds={
                        'Low': 1,
                        'Moderate': 2,
                        'High': 4
                    },
                    max_value=9,
                    title="Risk Level",
                    show_value=True
                )
            
            st.markdown("**Chi tiết điểm:**")
            if details:
                for detail in details:
                    st.write(f"- {detail}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo điều trị")
            
            if score == 0 and sex == "Nam":
                st.info("""
                **Không cần kháng đông** (hoặc có thể dùng Aspirin)
                - Nguy cơ đột quỵ rất thấp
                - Cân nhắc lại định kỳ
                """)
            elif score == 1 and sex == "Nam":
                st.warning("""
                **Cân nhắc kháng đông** (ưu tiên NOAC/Warfarin)
                - Thảo luận với bệnh nhân về lợi ích/nguy cơ
                - Đánh giá nguy cơ chảy máu (HAS-BLED)
                """)
            elif score >= 1:
                st.error("""
                **KHUYẾN CÁO KHÁNG ĐÔNG** (NOAC hoặc Warfarin)
                
                **Lựa chọn ưu tiên:**
                - **NOAC (Kháng đông trực tiếp):**
                  - Apixaban 5mg x 2 lần/ngày
                  - Rivaroxaban 20mg x 1 lần/ngày
                  - Edoxaban 60mg x 1 lần/ngày
                  - Dabigatran 150mg x 2 lần/ngày
                
                - **Warfarin:**
                  - Mục tiêu INR 2.0-3.0
                  - Khi không dùng được NOAC
                
                **Chống chỉ định NOAC:**
                - Suy thận nặng (CrCl <15-30)
                - Bệnh van tim nặng
                - Thai kỳ
                """)
            
            # Prepare inputs for export
            inputs_dict = {
                "CHF": "Có" if chf else "Không",
                "Hypertension": "Có" if htn else "Không",
                "Age Group": age_group,
                "Diabetes": "Có" if dm else "Không",
                "Stroke/TIA": "Có" if stroke else "Không",
                "Vascular Disease": "Có" if vasc else "Không",
                "Sex": sex
            }
            
            # Prepare results for export
            results_dict = {
                "CHA₂DS₂-VASc Score": f"{score} điểm",
                "Stroke Risk": risk,
                "Risk Level": risk_text,
                "Details": "\n".join(details) if details else "Không có yếu tố nguy cơ"
            }
            
            # Export section (new component)
            render_scores_export(
                calculator_name="CHA₂DS₂-VASc Score",
                inputs=inputs_dict,
                results=results_dict,
                specialty="Tim mạch"
            )
            
            # Keep old export for compatibility
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"CHA₂DS₂-VASc = {score} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="CHA₂DS₂-VASc Score",
                filename="cha2ds2vasc_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="cha2ds2vasc",
                calculator_name="CHA₂DS₂-VASc Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="cha2ds2vasc",
                calculator_name="CHA₂DS₂-VASc Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="cha2ds2vasc", show_actions=True)
            
            # References section
            references = get_references("CHA2DS2-VASc")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
    
    # Always show references at the bottom (even before calculation)
    references = get_references("CHA2DS2-VASc")
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

