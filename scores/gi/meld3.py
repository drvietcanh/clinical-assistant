"""
MELD 3.0 Score
==============

Updated MELD score (2021) for predicting mortality in patients with end-stage liver disease.

Reference:
- Kim WR, et al. MELD 3.0: The Model for End-Stage Liver Disease Updated for the Modern Era. 
  Gastroenterology. 2021;161(6):1887-1895.e4.

Clinical Utility:
- Predicts 90-day mortality in patients with end-stage liver disease
- Updated version of MELD score (2021)
- More accurate than original MELD
- Used for liver transplant allocation

MELD 3.0 Components:
1. Total bilirubin (mg/dL)
2. Creatinine (mg/dL)
3. INR
4. Sodium (mmol/L) - included in calculation
5. Sex (female = 1.33 multiplier)
"""

import streamlit as st
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

import math


def calculate_meld3(
    bilirubin: float,
    creatinine: float,
    inr: float,
    sodium: float,
    is_female: bool = False
) -> dict:
    """
    Calculate MELD 3.0 Score
    
    Args:
        bilirubin: Total bilirubin (mg/dL)
        creatinine: Creatinine (mg/dL)
        inr: International Normalized Ratio
        sodium: Sodium (mmol/L)
        is_female: Female sex (applies 1.33 multiplier)
    
    Returns:
        dict with MELD 3.0 score and interpretation
    """
    # MELD 3.0 formula
    # MELD 3.0 = 1.33 (if female) × [1.33 × ln(bilirubin) + 4.56 × ln(creatinine) + 0.82 × ln(INR) - 0.24 × ln(sodium) + 1.85]
    
    # Ensure minimum values
    bilirubin = max(bilirubin, 1.0)
    creatinine = max(creatinine, 0.8)
    inr = max(inr, 1.0)
    sodium = max(sodium, 125.0)
    sodium = min(sodium, 137.0)  # Cap at 137
    
    # Calculate MELD 3.0
    meld3 = (1.33 * math.log(bilirubin) + 
             4.56 * math.log(creatinine) + 
             0.82 * math.log(inr) - 
             0.24 * math.log(sodium) + 
             1.85)
    
    # Apply female multiplier
    if is_female:
        meld3 *= 1.33
    
    # Round to nearest integer
    meld3_score = round(meld3)
    
    # Cap at 40 (for display purposes, actual can go higher)
    meld3_score = min(meld3_score, 40)
    
    # Risk stratification
    if meld3_score < 10:
        risk_level = "low"
        interpretation = "Nguy cơ thấp"
        mortality_90d = "<5%"
        recommendation = "Theo dõi thường quy"
    elif meld3_score < 20:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình"
        mortality_90d = "5-15%"
        recommendation = "Theo dõi sát, cân nhắc ghép gan"
    elif meld3_score < 30:
        risk_level = "high"
        interpretation = "Nguy cơ cao"
        mortality_90d = "15-30%"
        recommendation = "Cân nhắc ghép gan, điều trị tích cực"
    else:
        risk_level = "critical"
        interpretation = "Nguy cơ rất cao"
        mortality_90d = ">30%"
        recommendation = "Ưu tiên ghép gan, điều trị tích cực"
    
    return {
        "score": meld3_score,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "mortality_90d": mortality_90d,
        "recommendation": recommendation,
        "bilirubin": bilirubin,
        "creatinine": creatinine,
        "inr": inr,
        "sodium": sodium,
        "is_female": is_female
    }


def render():
    """MELD 3.0 Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 MELD 3.0 Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán tử vong 90 ngày ở bệnh nhân bệnh gan giai đoạn cuối (Phiên bản cập nhật 2021)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'meld3':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông số Xét nghiệm")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        bilirubin = st.number_input(
            "Total Bilirubin (mg/dL)",
            min_value=0.1,
            max_value=50.0,
            value=float(shared_inputs.get('bilirubin', 2.0)) if shared_inputs else 2.0,
            step=0.1,
            format="%.1f",
            help="Bilirubin toàn phần (mg/dL). Bình thường: <1.2 mg/dL"
        )
        
        creatinine = st.number_input(
            "Creatinine (mg/dL)",
            min_value=0.1,
            max_value=10.0,
            value=float(shared_inputs.get('creatinine', 1.0)) if shared_inputs else 1.0,
            step=0.1,
            format="%.1f",
            help="Creatinine (mg/dL). Bình thường: 0.6-1.2 mg/dL"
        )
        
        inr = st.number_input(
            "INR (International Normalized Ratio)",
            min_value=0.5,
            max_value=10.0,
            value=float(shared_inputs.get('inr', 1.0)) if shared_inputs else 1.0,
            step=0.1,
            format="%.2f",
            help="INR. Bình thường: 0.9-1.1"
        )
        
        sodium = st.number_input(
            "Sodium (mmol/L)",
            min_value=100.0,
            max_value=150.0,
            value=float(shared_inputs.get('sodium', 140.0)) if shared_inputs else 140.0,
            step=1.0,
            format="%.0f",
            help="Natri (mmol/L). Bình thường: 135-145 mmol/L"
        )
        
        is_female = st.checkbox(
            "Giới tính nữ",
            help="Giới tính nữ (áp dụng hệ số 1.33)",
            value=shared_inputs.get('is_female') == 'Có' if shared_inputs else False
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="meld3",
            calculator_name="MELD 3.0",
            category="Tiêu hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("meld3")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về MELD 3.0",
                content="""
                **MELD 3.0** là phiên bản cập nhật 2021 của MELD:
                
                **Công thức:**
                MELD 3.0 = 1.33 (nếu nữ) × [1.33 × ln(bilirubin) + 4.56 × ln(creatinine) + 0.82 × ln(INR) - 0.24 × ln(sodium) + 1.85]
                
                **Cải tiến so với MELD cũ:**
                - Bao gồm natri trong công thức
                - Hệ số điều chỉnh cho nữ giới
                - Chính xác hơn trong dự đoán tử vong
                
                **Phân tầng:**
                - <10: Nguy cơ thấp (<5% tử vong 90 ngày)
                - 10-19: Nguy cơ trung bình (5-15%)
                - 20-29: Nguy cơ cao (15-30%)
                - ≥30: Nguy cơ rất cao (>30%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân bệnh gan giai đoạn cuối
                - Đánh giá tiên lượng
                - Quyết định ghép gan
                - Phân bổ nguồn lực
                """,
                limitations="""
                **Hạn chế:**
                - Dự đoán tử vong 90 ngày
                - Cần xét nghiệm cập nhật
                - Không áp dụng cho một số bệnh gan đặc biệt
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score <10: Theo dõi thường quy
                - Score 10-19: Cân nhắc ghép gan
                - Score ≥20: Ưu tiên ghép gan
                - Score ≥30: Ưu tiên cao nhất
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính MELD 3.0", type="primary", use_container_width=True):
        result = calculate_meld3(
            bilirubin,
            creatinine,
            inr,
            sodium,
            is_female
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="meld3",
            calculator_name="MELD 3.0",
            inputs={
                "bilirubin": bilirubin,
                "creatinine": creatinine,
                "inr": inr,
                "sodium": sodium,
                "is_female": "Có" if is_female else "Không"
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
                "high": COLORS['warning'],
                "critical": COLORS['danger']
            }.get(result['risk_level'], COLORS['info'])
            
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">MELD 3.0 Score: <strong>{result['score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Tử vong 90 ngày:</strong> {result['mortality_90d']}</p>
                <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['interpretation'])
        
        # Breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        breakdown_data = [
            {"label": "Total Bilirubin", "value": f"{result['bilirubin']} mg/dL"},
            {"label": "Creatinine", "value": f"{result['creatinine']} mg/dL"},
            {"label": "INR", "value": f"{result['inr']:.2f}"},
            {"label": "Sodium", "value": f"{result['sodium']} mmol/L"},
            {"label": "Giới tính", "value": "Nữ (×1.33)" if result['is_female'] else "Nam"},
            {"label": "**MELD 3.0 Score**", "value": f"**{result['score']}**"},
        ]
        
        render_score_breakdown(breakdown_data)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'critical':
            st.error(f"""
            **⚠️ Nguy cơ rất cao (Score ≥30):**
            - Tử vong 90 ngày >30%
            - Ưu tiên cao nhất cho ghép gan
            - Điều trị tích cực
            - Theo dõi sát
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score 20-29):**
            - Tử vong 90 ngày 15-30%
            - Cân nhắc ghép gan
            - Điều trị tích cực
            - Theo dõi sát
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 10-19):**
            - Tử vong 90 ngày 5-15%
            - Theo dõi sát
            - Cân nhắc ghép gan
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score <10):**
            - Tử vong 90 ngày <5%
            - Theo dõi thường quy
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="meld3",
                calculator_name="MELD 3.0",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="MELD 3.0",
                result=result,
                inputs={
                    "Bilirubin": f"{bilirubin} mg/dL",
                    "Creatinine": f"{creatinine} mg/dL",
                    "INR": f"{inr:.2f}",
                    "Sodium": f"{sodium} mmol/L",
                    "Sex": "Female" if is_female else "Male"
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("meld3", "MELD 3.0")
    
    # References
    st.markdown("---")
    references = get_references("meld3")
    if references:
        render_references_section(references)
