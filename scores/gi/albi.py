"""
ALBI Score
==========

Albumin-Bilirubin (ALBI) Score for assessing liver function and prognosis in hepatocellular carcinoma.

Reference:
- Johnson PJ, et al. Assessment of liver function in patients with hepatocellular carcinoma: 
  a new evidence-based approach - the ALBI grade. J Clin Oncol. 2015;33(6):550-8.

Clinical Utility:
- Assesses liver function in HCC patients
- Predicts survival in HCC
- Simpler than Child-Pugh score
- Used for treatment decisions in HCC

ALBI Score = 0.66 × log10(bilirubin μmol/L) - 0.085 × albumin (g/L)

Grades:
- Grade 1: ≤-2.60 (Best liver function)
- Grade 2: >-2.60 to ≤-1.39 (Moderate)
- Grade 3: >-1.39 (Poor liver function)
"""

import streamlit as st
import math
from config.theme import COLORS
from scores.utils.validation import validate_lab_value
from components.ui.scoring import render_score_result, render_score_breakdown
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


def calculate_albi_score(bilirubin_umol: float, albumin_gL: float) -> dict:
    """
    Calculate ALBI Score
    
    Args:
        bilirubin_umol: Total bilirubin (μmol/L)
        albumin_gL: Albumin (g/L)
    
    Returns:
        dict with ALBI score, grade, and interpretation
    """
    # Ensure minimum values
    bilirubin_umol = max(bilirubin_umol, 1.0)
    albumin_gL = max(albumin_gL, 10.0)
    
    # ALBI Score = 0.66 × log10(bilirubin μmol/L) - 0.085 × albumin (g/L)
    albi_score = 0.66 * math.log10(bilirubin_umol) - 0.085 * albumin_gL
    
    # Grade classification
    if albi_score <= -2.60:
        grade = 1
        grade_text = "Grade 1"
        risk_level = "low"
        interpretation = "Chức năng gan tốt"
        survival = "Tốt"
        recommendation = "Có thể điều trị tích cực"
    elif albi_score <= -1.39:
        grade = 2
        grade_text = "Grade 2"
        risk_level = "moderate"
        interpretation = "Chức năng gan trung bình"
        survival = "Trung bình"
        recommendation = "Cân nhắc điều trị, theo dõi sát"
    else:
        grade = 3
        grade_text = "Grade 3"
        risk_level = "high"
        interpretation = "Chức năng gan kém"
        survival = "Kém"
        recommendation = "Chức năng gan kém, cân nhắc điều trị bảo tồn"
    
    return {
        "score": round(albi_score, 2),
        "grade": grade,
        "grade_text": grade_text,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "survival": survival,
        "recommendation": recommendation,
        "bilirubin_umol": bilirubin_umol,
        "albumin_gL": albumin_gL
    }


def render():
    """ALBI Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 ALBI Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Đánh giá chức năng gan và tiên lượng ở bệnh nhân ung thư biểu mô tế bào gan (HCC)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'albi':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông số Xét nghiệm")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        st.info("""
        **Lưu ý:** ALBI Score sử dụng đơn vị:
        - Bilirubin: μmol/L (micromol/L)
        - Albumin: g/L (gram/L)
        """)
        
        bilirubin_umol = st.number_input(
            "Total Bilirubin (μmol/L)",
            min_value=1.0,
            max_value=500.0,
            value=float(shared_inputs.get('bilirubin_umol', 20.0)) if shared_inputs else 20.0,
            step=0.1,
            format="%.1f",
            help="Bilirubin toàn phần (μmol/L). Bình thường: <17 μmol/L"
        )
        
        albumin_gL = st.number_input(
            "Albumin (g/L)",
            min_value=10.0,
            max_value=60.0,
            value=float(shared_inputs.get('albumin_gL', 40.0)) if shared_inputs else 40.0,
            step=0.1,
            format="%.1f",
            help="Albumin (g/L). Bình thường: 35-50 g/L"
        )
        
        # Conversion helper
        st.markdown("---")
        st.markdown("#### 🔄 Chuyển đổi đơn vị")
        col_conv1, col_conv2 = st.columns(2)
        
        with col_conv1:
            if st.button("Chuyển Bilirubin từ mg/dL → μmol/L"):
                bilirubin_mgdl = st.session_state.get('bilirubin_mgdl_input', 1.0)
                bilirubin_umol_converted = bilirubin_mgdl * 17.1
                st.info(f"{bilirubin_mgdl} mg/dL = {bilirubin_umol_converted:.1f} μmol/L")
                bilirubin_umol = bilirubin_umol_converted
        
        with col_conv2:
            if st.button("Chuyển Albumin từ g/dL → g/L"):
                albumin_gdl = st.session_state.get('albumin_gdl_input', 4.0)
                albumin_gL_converted = albumin_gdl * 10.0
                st.info(f"{albumin_gdl} g/dL = {albumin_gL_converted:.1f} g/L")
                albumin_gL = albumin_gL_converted
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="albi",
            calculator_name="ALBI Score",
            category="Tiêu hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("albi")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về ALBI Score",
                content="""
                **ALBI Score** đánh giá chức năng gan:
                
                **Công thức:**
                ALBI = 0.66 × log₁₀(bilirubin μmol/L) - 0.085 × albumin (g/L)
                
                **Phân loại:**
                - **Grade 1:** ≤-2.60 (Chức năng gan tốt)
                - **Grade 2:** >-2.60 to ≤-1.39 (Trung bình)
                - **Grade 3:** >-1.39 (Chức năng gan kém)
                
                **Ưu điểm:**
                - Đơn giản hơn Child-Pugh
                - Chỉ cần 2 xét nghiệm
                - Dự đoán tiên lượng tốt
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân HCC
                - Đánh giá chức năng gan
                - Quyết định điều trị
                - Dự đoán tiên lượng
                """,
                limitations="""
                **Hạn chế:**
                - Chủ yếu cho HCC
                - Cần đánh giá toàn diện
                - Không thay thế Child-Pugh hoàn toàn
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Grade 1: Có thể điều trị tích cực
                - Grade 2: Cân nhắc điều trị
                - Grade 3: Điều trị bảo tồn
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính ALBI Score", type="primary", use_container_width=True):
        result = calculate_albi_score(bilirubin_umol, albumin_gL)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="albi",
            calculator_name="ALBI Score",
            inputs={
                "bilirubin_umol": bilirubin_umol,
                "albumin_gL": albumin_gL
            },
            result=result
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Main result card
        col_result1, col_result2 = st.columns([2, 1])
        
        with col_result1:
            risk_color = {
                "low": COLORS['success'],
                "moderate": "#FFA500",
                "high": COLORS['warning']
            }.get(result['risk_level'], COLORS['info'])
            
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">ALBI Score: <strong>{result['score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Grade:</strong> {result['grade_text']}</p>
                <p style="margin: 5px 0;"><strong>Mức độ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Tiên lượng:</strong> {result['survival']}</p>
                <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['grade_text'])
        
        # Breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        breakdown_data = [
            {"label": "Total Bilirubin", "value": f"{result['bilirubin_umol']} μmol/L"},
            {"label": "Albumin", "value": f"{result['albumin_gL']} g/L"},
            {"label": "**ALBI Score**", "value": f"**{result['score']}**"},
            {"label": "**ALBI Grade**", "value": f"**{result['grade_text']}**"},
        ]
        
        render_score_breakdown(breakdown_data)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['grade'] == 3:
            st.error(f"""
            **⚠️ ALBI Grade 3 (Score >-1.39):**
            - Chức năng gan kém
            - Tiên lượng kém
            - Cân nhắc điều trị bảo tồn
            - Theo dõi sát
            """)
        elif result['grade'] == 2:
            st.info(f"""
            **ℹ️ ALBI Grade 2 (Score >-2.60 to ≤-1.39):**
            - Chức năng gan trung bình
            - Tiên lượng trung bình
            - Cân nhắc điều trị, theo dõi sát
            """)
        else:
            st.success(f"""
            **✅ ALBI Grade 1 (Score ≤-2.60):**
            - Chức năng gan tốt
            - Tiên lượng tốt
            - Có thể điều trị tích cực
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="albi",
                calculator_name="ALBI Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="ALBI Score",
                result=result,
                inputs={
                    "Bilirubin": f"{bilirubin_umol} μmol/L",
                    "Albumin": f"{albumin_gL} g/L",
                    "ALBI Score": result['score'],
                    "ALBI Grade": result['grade_text']
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("albi", "ALBI Score")
    
    # References
    st.markdown("---")
    references = get_references("albi")
    if references:
        render_references_section(references)
