"""
BARC Classification
==================

Bleeding Academic Research Consortium (BARC) Classification for bleeding events.

Reference:
- Mehran R, et al. Standardized bleeding definitions for cardiovascular clinical trials: 
  A consensus report from the Bleeding Academic Research Consortium. Circulation. 2011;123(23):2736-47.
- Updated: BARC-2 (2018) and BARC-3 (2019)

Clinical Utility:
- Standardized classification of bleeding events
- Used in cardiovascular clinical trials
- Important for PCI and anticoagulation management
- Helps guide treatment decisions

BARC Types:
- Type 0: No bleeding
- Type 1: Bleeding that is not actionable
- Type 2: Any overt, actionable sign of hemorrhage
- Type 3: Overt bleeding plus hemoglobin drop
- Type 4: CABG-related bleeding
- Type 5: Fatal bleeding
"""

import streamlit as st
from config.theme import COLORS
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


def classify_barc_bleeding(
    has_bleeding: bool,
    actionable: bool,
    hemoglobin_drop: float = None,
    hemoglobin_drop_unit: str = "g/dL",
    transfusion: bool = False,
    cabg_related: bool = False,
    fatal: bool = False,
    intracranial: bool = False,
    retroperitoneal: bool = False,
    intraocular: bool = False,
    pericardial: bool = False
) -> dict:
    """
    Classify bleeding according to BARC criteria
    
    Args:
        has_bleeding: Any bleeding present
        actionable: Bleeding requires medical attention
        hemoglobin_drop: Hemoglobin drop (g/dL or g/L)
        hemoglobin_drop_unit: Unit for hemoglobin drop
        transfusion: Requires transfusion
        cabg_related: CABG-related bleeding
        fatal: Fatal bleeding
        intracranial: Intracranial bleeding
        retroperitoneal: Retroperitoneal bleeding
        intraocular: Intraocular bleeding
        pericardial: Pericardial bleeding
    
    Returns:
        dict with BARC classification and details
    """
    # Convert hemoglobin drop to g/dL if needed
    if hemoglobin_drop is not None:
        if hemoglobin_drop_unit == "g/L":
            hb_drop_gdl = hemoglobin_drop / 10.0
        else:
            hb_drop_gdl = hemoglobin_drop
    else:
        hb_drop_gdl = None
    
    # BARC Type 5: Fatal bleeding
    if fatal:
        return {
            "barc_type": 5,
            "classification": "BARC Type 5 - Fatal Bleeding",
            "severity": "Fatal",
            "risk_level": "critical",
            "description": "Fatal bleeding",
            "criteria": "Probable or definite fatal bleeding",
            "management": "N/A - Fatal event"
        }
    
    # BARC Type 4: CABG-related bleeding
    if cabg_related:
        return {
            "barc_type": 4,
            "classification": "BARC Type 4 - CABG-Related Bleeding",
            "severity": "Severe",
            "risk_level": "high",
            "description": "CABG-related bleeding",
            "criteria": "Perioperative intracranial bleeding within 48h, Reoperation for bleeding, Transfusion ≥5U whole blood or packed red blood cells within 48h, Chest tube output ≥2L within 24h",
            "management": "Surgical intervention, intensive monitoring"
        }
    
    # BARC Type 3: Overt bleeding plus hemoglobin drop
    if has_bleeding and actionable:
        type_3a = False
        type_3b = False
        type_3c = False
        
        # Type 3a: Hemoglobin drop 3-5 g/dL
        if hb_drop_gdl is not None and 3.0 <= hb_drop_gdl < 5.0:
            type_3a = True
        
        # Type 3b: Hemoglobin drop ≥5 g/dL or transfusion
        if (hb_drop_gdl is not None and hb_drop_gdl >= 5.0) or transfusion:
            type_3b = True
        
        # Type 3c: Intracranial, retroperitoneal, intraocular, or pericardial
        if intracranial or retroperitoneal or intraocular or pericardial:
            type_3c = True
        
        if type_3c:
            return {
                "barc_type": 3,
                "barc_subtype": "3c",
                "classification": "BARC Type 3c - Intracranial/Retroperitoneal/Intraocular/Pericardial",
                "severity": "Severe",
                "risk_level": "critical",
                "description": "Intracranial, retroperitoneal, intraocular, or pericardial bleeding",
                "criteria": "Intracranial, retroperitoneal, intraocular, or pericardial bleeding",
                "management": "Immediate intervention, intensive care, consider reversal agents"
            }
        elif type_3b:
            return {
                "barc_type": 3,
                "barc_subtype": "3b",
                "classification": "BARC Type 3b - Hemoglobin Drop ≥5 g/dL or Transfusion",
                "severity": "Moderate-Severe",
                "risk_level": "high",
                "description": "Hemoglobin drop ≥5 g/dL or requires transfusion",
                "criteria": "Hemoglobin drop ≥5 g/dL or transfusion",
                "management": "Transfusion, consider stopping anticoagulation, intensive monitoring"
            }
        elif type_3a:
            return {
                "barc_type": 3,
                "barc_subtype": "3a",
                "classification": "BARC Type 3a - Hemoglobin Drop 3-5 g/dL",
                "severity": "Moderate",
                "risk_level": "moderate",
                "description": "Hemoglobin drop 3-5 g/dL",
                "criteria": "Hemoglobin drop 3-5 g/dL",
                "management": "Close monitoring, consider transfusion, reassess anticoagulation"
            }
    
    # BARC Type 2: Any overt, actionable sign of hemorrhage
    if has_bleeding and actionable:
        return {
            "barc_type": 2,
            "classification": "BARC Type 2 - Actionable Bleeding",
            "severity": "Mild-Moderate",
            "risk_level": "moderate",
            "description": "Any overt, actionable sign of hemorrhage",
            "criteria": "Requires medical intervention, leads to hospitalization, or prompts evaluation",
            "management": "Medical intervention, monitoring, consider dose adjustment"
        }
    
    # BARC Type 1: Bleeding that is not actionable
    if has_bleeding and not actionable:
        return {
            "barc_type": 1,
            "classification": "BARC Type 1 - Non-Actionable Bleeding",
            "severity": "Minimal",
            "risk_level": "low",
            "description": "Bleeding that is not actionable",
            "criteria": "Bleeding that does not require medical intervention or hospitalization",
            "management": "Observation, no intervention needed"
        }
    
    # BARC Type 0: No bleeding
    return {
        "barc_type": 0,
        "classification": "BARC Type 0 - No Bleeding",
        "severity": "None",
        "risk_level": "low",
        "description": "No bleeding",
        "criteria": "No evidence of bleeding",
        "management": "Continue current management"
    }


def render():
    """BARC Classification Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>❤️ BARC Classification</h3>
    """, unsafe_allow_html=True)
    st.caption("Phân loại chảy máu theo Bleeding Academic Research Consortium (BARC)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'barc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Đánh giá Chảy máu")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        has_bleeding = st.checkbox(
            "Có chảy máu",
            help="Có bằng chứng chảy máu",
            value=shared_inputs.get('has_bleeding') == 'Có' if shared_inputs else False
        )
        
        if has_bleeding:
            actionable = st.checkbox(
                "Chảy máu cần can thiệp y tế",
                help="Chảy máu cần can thiệp y tế, nhập viện, hoặc đánh giá",
                value=shared_inputs.get('actionable') == 'Có' if shared_inputs else False
            )
            
            if actionable:
                st.markdown("#### Thông số chảy máu")
                
                hemoglobin_drop = st.number_input(
                    "Giảm hemoglobin (nếu có)",
                    min_value=0.0,
                    max_value=20.0,
                    value=float(shared_inputs.get('hemoglobin_drop', 0.0)) if shared_inputs else None,
                    step=0.1,
                    format="%.1f",
                    help="Giảm hemoglobin (g/dL hoặc g/L)"
                )
                
                if hemoglobin_drop > 0:
                    hb_unit = st.radio(
                        "Đơn vị hemoglobin:",
                        ["g/dL", "g/L"],
                        horizontal=True,
                        index=0
                    )
                else:
                    hb_unit = "g/dL"
                    hemoglobin_drop = None
                
                transfusion = st.checkbox(
                    "Cần truyền máu",
                    help="Cần truyền máu",
                    value=shared_inputs.get('transfusion') == 'Có' if shared_inputs else False
                )
                
                st.markdown("#### Vị trí chảy máu đặc biệt")
                intracranial = st.checkbox(
                    "Chảy máu nội sọ",
                    value=shared_inputs.get('intracranial') == 'Có' if shared_inputs else False
                )
                retroperitoneal = st.checkbox(
                    "Chảy máu sau phúc mạc",
                    value=shared_inputs.get('retroperitoneal') == 'Có' if shared_inputs else False
                )
                intraocular = st.checkbox(
                    "Chảy máu trong mắt",
                    value=shared_inputs.get('intraocular') == 'Có' if shared_inputs else False
                )
                pericardial = st.checkbox(
                    "Chảy máu màng ngoài tim",
                    value=shared_inputs.get('pericardial') == 'Có' if shared_inputs else False
                )
            else:
                hemoglobin_drop = None
                hb_unit = "g/dL"
                transfusion = False
                intracranial = False
                retroperitoneal = False
                intraocular = False
                pericardial = False
        else:
            actionable = False
            hemoglobin_drop = None
            hb_unit = "g/dL"
            transfusion = False
            intracranial = False
            retroperitoneal = False
            intraocular = False
            pericardial = False
        
        st.markdown("---")
        st.markdown("#### Tình huống đặc biệt")
        cabg_related = st.checkbox(
            "Chảy máu liên quan CABG",
            help="Chảy máu trong hoặc sau phẫu thuật CABG",
            value=shared_inputs.get('cabg_related') == 'Có' if shared_inputs else False
        )
        fatal = st.checkbox(
            "Chảy máu tử vong",
            help="Chảy máu gây tử vong",
            value=shared_inputs.get('fatal') == 'Có' if shared_inputs else False
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="barc",
            calculator_name="BARC Classification",
            category="Tim mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("barc")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về BARC Classification",
                content="""
                **BARC Classification** phân loại chảy máu chuẩn hóa:
                
                **6 loại:**
                - **Type 0:** Không chảy máu
                - **Type 1:** Chảy máu không cần can thiệp
                - **Type 2:** Chảy máu cần can thiệp
                - **Type 3:** Chảy máu + giảm hemoglobin
                  - 3a: Giảm Hb 3-5 g/dL
                  - 3b: Giảm Hb ≥5 g/dL hoặc truyền máu
                  - 3c: Nội sọ/sau phúc mạc/trong mắt/màng ngoài tim
                - **Type 4:** Chảy máu liên quan CABG
                - **Type 5:** Chảy máu tử vong
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân sau PCI
                - Đang dùng kháng đông/kháng tiểu cầu
                - Có biến cố chảy máu
                - Trong nghiên cứu lâm sàng
                """,
                limitations="""
                **Hạn chế:**
                - Phân loại chuẩn hóa, không thay thế đánh giá lâm sàng
                - Cần đánh giá toàn diện
                - Kết hợp với các yếu tố khác
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Type 0-1: Tiếp tục điều trị
                - Type 2: Điều chỉnh liều, theo dõi
                - Type 3: Cần can thiệp tích cực
                - Type 4-5: Can thiệp khẩn cấp
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Phân loại BARC", type="primary", use_container_width=True):
        result = classify_barc_bleeding(
            has_bleeding,
            actionable,
            hemoglobin_drop,
            hb_unit if hemoglobin_drop else "g/dL",
            transfusion,
            cabg_related,
            fatal,
            intracranial,
            retroperitoneal,
            intraocular,
            pericardial
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="barc",
            calculator_name="BARC Classification",
            inputs={
                "has_bleeding": "Có" if has_bleeding else "Không",
                "actionable": "Có" if actionable else "Không",
                "hemoglobin_drop": hemoglobin_drop if hemoglobin_drop else 0,
                "transfusion": "Có" if transfusion else "Không",
                "cabg_related": "Có" if cabg_related else "Không",
                "fatal": "Có" if fatal else "Không"
            },
            result=result
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Main result card
        risk_color = {
            "low": COLORS['success'],
            "moderate": "#FFA500",
            "high": COLORS['warning'],
            "critical": COLORS['danger']
        }.get(result['risk_level'], COLORS['info'])
        
        st.markdown(f"""
        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h2 style="color: {risk_color}; margin: 0 0 10px 0;">{result['classification']}</h2>
            <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ:</strong> {result['severity']}</p>
            <p style="margin: 5px 0;"><strong>Mô tả:</strong> {result['description']}</p>
            <p style="margin: 5px 0;"><strong>Tiêu chí:</strong> {result['criteria']}</p>
            <p style="margin: 5px 0;"><strong>Xử trí:</strong> {result['management']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['barc_type'] == 5:
            st.error("""
            **⚠️ BARC Type 5 - Chảy máu tử vong:**
            - Chảy máu gây tử vong
            - Cần đánh giá nguyên nhân và phòng ngừa
            """)
        elif result['barc_type'] == 4:
            st.error("""
            **⚠️ BARC Type 4 - Chảy máu liên quan CABG:**
            - Chảy máu nghiêm trọng trong/sau CABG
            - Cần can thiệp phẫu thuật
            - Theo dõi tích cực
            """)
        elif result['barc_type'] == 3:
            st.warning(f"""
            **⚠️ BARC Type 3 - Chảy máu nặng:**
            - Chảy máu kèm giảm hemoglobin
            - Cần can thiệp tích cực
            - Xem xét ngừng kháng đông
            - Truyền máu nếu cần
            - Theo dõi sát
            """)
        elif result['barc_type'] == 2:
            st.info("""
            **ℹ️ BARC Type 2 - Chảy máu cần can thiệp:**
            - Chảy máu cần can thiệp y tế
            - Điều chỉnh liều thuốc nếu cần
            - Theo dõi sát
            """)
        elif result['barc_type'] == 1:
            st.success("""
            **✅ BARC Type 1 - Chảy máu nhẹ:**
            - Chảy máu không cần can thiệp
            - Theo dõi thường quy
            - Tiếp tục điều trị
            """)
        else:
            st.success("""
            **✅ BARC Type 0 - Không chảy máu:**
            - Không có bằng chứng chảy máu
            - Tiếp tục điều trị hiện tại
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="barc",
                calculator_name="BARC Classification",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="BARC Classification",
                result=result,
                inputs={
                    "BARC Type": result['barc_type'],
                    "Classification": result['classification'],
                    "Severity": result['severity']
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("barc", "BARC Classification")
    
    # References
    st.markdown("---")
    references = get_references("barc")
    if references:
        render_references_section(references)
