"""
NAFLD Fibrosis Score
====================

Predicts advanced fibrosis in patients with non-alcoholic fatty liver disease (NAFLD).

Reference:
- Angulo P, et al. The NAFLD fibrosis score: a noninvasive system that identifies liver fibrosis 
  in patients with NAFLD. Hepatology. 2007;45(4):846-54.

Clinical Utility:
- Predicts advanced fibrosis in NAFLD
- Non-invasive assessment
- Helps avoid liver biopsy
- Used in primary care and hepatology

NAFLD Fibrosis Score = -1.675 + 0.037 × age (years) + 0.094 × BMI (kg/m²) + 1.13 × IFG/diabetes (yes=1, no=0) + 0.99 × AST/ALT ratio - 0.013 × platelet count (×10⁹/L) - 0.66 × albumin (g/dL)

Cutoffs:
- <-1.455: Low probability of advanced fibrosis
- -1.455 to 0.676: Indeterminate
- >0.676: High probability of advanced fibrosis
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


def calculate_nafld_fibrosis_score(
    age: int,
    bmi: float,
    has_diabetes: bool,
    ast: float,
    alt: float,
    platelet_count: int,
    albumin_gdl: float
) -> dict:
    """
    Calculate NAFLD Fibrosis Score
    
    Args:
        age: Patient age (years)
        bmi: Body mass index (kg/m²)
        has_diabetes: History of diabetes or IFG
        ast: AST (U/L)
        alt: ALT (U/L)
        platelet_count: Platelet count (×10⁹/L)
        albumin_gdl: Albumin (g/dL)
    
    Returns:
        dict with score, risk level, and fibrosis prediction
    """
    # Calculate AST/ALT ratio
    if alt > 0:
        ast_alt_ratio = ast / alt
    else:
        ast_alt_ratio = 1.0
    
    # NAFLD Fibrosis Score
    nafld_score = (-1.675 + 
                   0.037 * age + 
                   0.094 * bmi + 
                   1.13 * (1 if has_diabetes else 0) + 
                   0.99 * ast_alt_ratio - 
                   0.013 * platelet_count - 
                   0.66 * albumin_gdl)
    
    # Risk stratification
    if nafld_score < -1.455:
        risk_level = "low"
        interpretation = "Nguy cơ thấp xơ hóa tiến triển"
        fibrosis_probability = "Thấp (<10%)"
        recommendation = "Không cần sinh thiết gan, theo dõi định kỳ"
    elif nafld_score <= 0.676:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình xơ hóa tiến triển"
        fibrosis_probability = "Trung bình (10-30%)"
        recommendation = "Cân nhắc sinh thiết gan hoặc đánh giá thêm"
    else:
        risk_level = "high"
        interpretation = "Nguy cơ cao xơ hóa tiến triển"
        fibrosis_probability = "Cao (>30%)"
        recommendation = "Cân nhắc sinh thiết gan, điều trị tích cực"
    
    return {
        "score": round(nafld_score, 2),
        "risk_level": risk_level,
        "interpretation": interpretation,
        "fibrosis_probability": fibrosis_probability,
        "recommendation": recommendation,
        "age": age,
        "bmi": bmi,
        "has_diabetes": has_diabetes,
        "ast_alt_ratio": round(ast_alt_ratio, 2),
        "platelet_count": platelet_count,
        "albumin_gdl": albumin_gdl
    }


def render():
    """NAFLD Fibrosis Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 NAFLD Fibrosis Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán xơ hóa tiến triển ở bệnh nhân bệnh gan nhiễm mỡ không do rượu (NAFLD)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'nafld_fibrosis':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin Bệnh nhân")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        age = st.number_input(
            "Tuổi (năm)",
            min_value=0,
            max_value=120,
            value=int(shared_inputs.get('age', 50)) if shared_inputs else 50,
            step=1,
            help="Tuổi bệnh nhân (năm)"
        )
        
        bmi = st.number_input(
            "BMI (kg/m²)",
            min_value=10.0,
            max_value=60.0,
            value=float(shared_inputs.get('bmi', 28.0)) if shared_inputs else 28.0,
            step=0.1,
            format="%.1f",
            help="Body Mass Index (kg/m²)"
        )
        
        has_diabetes = st.checkbox(
            "Đái tháo đường hoặc IFG (Impaired Fasting Glucose)",
            help="Có tiền sử đái tháo đường hoặc rối loạn đường huyết lúc đói",
            value=shared_inputs.get('has_diabetes') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        st.markdown("### 📋 Xét nghiệm")
        
        ast = st.number_input(
            "AST (U/L)",
            min_value=1.0,
            max_value=1000.0,
            value=float(shared_inputs.get('ast', 40.0)) if shared_inputs else 40.0,
            step=1.0,
            format="%.0f",
            help="AST (U/L). Bình thường: <40 U/L"
        )
        
        alt = st.number_input(
            "ALT (U/L)",
            min_value=1.0,
            max_value=1000.0,
            value=float(shared_inputs.get('alt', 40.0)) if shared_inputs else 40.0,
            step=1.0,
            format="%.0f",
            help="ALT (U/L). Bình thường: <40 U/L"
        )
        
        platelet_count = st.number_input(
            "Platelet count (×10⁹/L)",
            min_value=10,
            max_value=1000,
            value=int(shared_inputs.get('platelet_count', 250)) if shared_inputs else 250,
            step=1,
            help="Số lượng tiểu cầu (×10⁹/L). Bình thường: 150-400 ×10⁹/L"
        )
        
        albumin_gdl = st.number_input(
            "Albumin (g/dL)",
            min_value=1.0,
            max_value=6.0,
            value=float(shared_inputs.get('albumin_gdl', 4.0)) if shared_inputs else 4.0,
            step=0.1,
            format="%.1f",
            help="Albumin (g/dL). Bình thường: 3.5-5.0 g/dL"
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="nafld_fibrosis",
            calculator_name="NAFLD Fibrosis Score",
            category="Tiêu hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("nafld_fibrosis")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về NAFLD Fibrosis Score",
                content="""
                **NAFLD Fibrosis Score** dự đoán xơ hóa tiến triển:
                
                **Công thức:**
                NFS = -1.675 + 0.037×age + 0.094×BMI + 1.13×diabetes + 0.99×AST/ALT - 0.013×platelet - 0.66×albumin
                
                **Phân tầng:**
                - **<-1.455:** Nguy cơ thấp (<10%)
                - **-1.455 to 0.676:** Trung bình (10-30%)
                - **>0.676:** Nguy cơ cao (>30%)
                
                **Ưu điểm:**
                - Không xâm lấn
                - Tránh sinh thiết gan
                - Dễ sử dụng
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân NAFLD
                - Cần đánh giá xơ hóa
                - Tránh sinh thiết gan
                - Theo dõi tiến triển
                """,
                limitations="""
                **Hạn chế:**
                - Dự đoán, không chẩn đoán
                - Có thể cần sinh thiết nếu nghi ngờ
                - Không áp dụng cho bệnh gan khác
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score <-1.455: Theo dõi định kỳ
                - Score -1.455 to 0.676: Cân nhắc sinh thiết
                - Score >0.676: Cân nhắc sinh thiết, điều trị tích cực
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính NAFLD Fibrosis Score", type="primary", use_container_width=True):
        result = calculate_nafld_fibrosis_score(
            age,
            bmi,
            has_diabetes,
            ast,
            alt,
            platelet_count,
            albumin_gdl
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="nafld_fibrosis",
            calculator_name="NAFLD Fibrosis Score",
            inputs={
                "age": age,
                "bmi": bmi,
                "has_diabetes": "Có" if has_diabetes else "Không",
                "ast": ast,
                "alt": alt,
                "platelet_count": platelet_count,
                "albumin_gdl": albumin_gdl
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
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">NAFLD Fibrosis Score: <strong>{result['score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Xác suất xơ hóa tiến triển:</strong> {result['fibrosis_probability']}</p>
                <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['interpretation'])
        
        # Breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        breakdown_data = [
            {"label": "Age", "value": f"{result['age']} tuổi"},
            {"label": "BMI", "value": f"{result['bmi']} kg/m²"},
            {"label": "Diabetes/IFG", "value": "Có" if result['has_diabetes'] else "Không"},
            {"label": "AST/ALT ratio", "value": f"{result['ast_alt_ratio']}"},
            {"label": "Platelet count", "value": f"{result['platelet_count']} ×10⁹/L"},
            {"label": "Albumin", "value": f"{result['albumin_gdl']} g/dL"},
            {"label": "**NAFLD Fibrosis Score**", "value": f"**{result['score']}**"},
        ]
        
        render_score_breakdown(breakdown_data)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score >0.676):**
            - Xác suất xơ hóa tiến triển >30%
            - Cân nhắc sinh thiết gan
            - Điều trị tích cực
            - Theo dõi sát
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score -1.455 to 0.676):**
            - Xác suất xơ hóa tiến triển 10-30%
            - Cân nhắc sinh thiết gan hoặc đánh giá thêm
            - Theo dõi định kỳ
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score <-1.455):**
            - Xác suất xơ hóa tiến triển <10%
            - Không cần sinh thiết gan
            - Theo dõi định kỳ
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="nafld_fibrosis",
                calculator_name="NAFLD Fibrosis Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="NAFLD Fibrosis Score",
                result=result,
                inputs={
                    "Age": f"{age} tuổi",
                    "BMI": f"{bmi} kg/m²",
                    "Diabetes": "Có" if has_diabetes else "Không",
                    "AST/ALT": f"{result['ast_alt_ratio']}",
                    "NAFLD Score": result['score']
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("nafld_fibrosis", "NAFLD Fibrosis Score")
    
    # References
    st.markdown("---")
    references = get_references("nafld_fibrosis")
    if references:
        render_references_section(references)
