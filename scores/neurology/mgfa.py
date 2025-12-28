"""
MGFA Clinical Classification (Myasthenia Gravis Foundation of America)
========================================================================

Classifies severity of myasthenia gravis.

Reference:
- Jaretzki A 3rd, et al. Myasthenia gravis: recommendations for clinical 
  research standards. Task Force of the Medical Scientific Advisory Board 
  of the Myasthenia Gravis Foundation of America. 
  Neurology. 2000;55(1):16-23.

MGFA Clinical Classification:
- Class I: Ocular only
- Class II: Mild weakness affecting other than ocular muscles
  - IIa: Predominantly affecting limb, axial muscles, or both
  - IIb: Predominantly affecting oropharyngeal, respiratory muscles, or both
- Class III: Moderate weakness affecting other than ocular muscles
  - IIIa: Predominantly affecting limb, axial muscles, or both
  - IIIb: Predominantly affecting oropharyngeal, respiratory muscles, or both
- Class IV: Severe weakness affecting other than ocular muscles
  - IVa: Predominantly affecting limb, axial muscles, or both
  - IVb: Predominantly affecting oropharyngeal, respiratory muscles, or both
- Class V: Intubation required (with or without mechanical ventilation)

Clinical Utility:
- Standardized classification of MG severity
- Guides treatment decisions
- Monitors disease progression
- Used in neurology
"""

import streamlit as st
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def classify_mgfa(
    ocular_only: bool,
    mild_weakness: bool,
    moderate_weakness: bool,
    severe_weakness: bool,
    intubation_required: bool,
    predominantly_limb_axial: bool,
    predominantly_oropharyngeal_respiratory: bool
) -> dict:
    """
    Classify MGFA Clinical Classification
    
    Args:
        ocular_only: Ocular symptoms only
        mild_weakness: Mild weakness (other than ocular)
        moderate_weakness: Moderate weakness (other than ocular)
        severe_weakness: Severe weakness (other than ocular)
        intubation_required: Intubation required
        predominantly_limb_axial: Predominantly limb/axial muscles
        predominantly_oropharyngeal_respiratory: Predominantly oropharyngeal/respiratory muscles
    
    Returns:
        Dictionary with MGFA class and interpretation
    """
    if intubation_required:
        mgfa_class = "Class V"
        class_description = "Cần đặt nội khí quản (có hoặc không thở máy)"
        severity = "Rất nặng"
        treatment = "Điều trị tại ICU, thở máy, điều trị tích cực"
    elif ocular_only:
        mgfa_class = "Class I"
        class_description = "Chỉ có triệu chứng mắt"
        severity = "Nhẹ"
        treatment = "Điều trị tại chỗ (pyridostigmine), theo dõi"
    elif severe_weakness:
        if predominantly_limb_axial:
            mgfa_class = "Class IVa"
            class_description = "Yếu nặng, chủ yếu ảnh hưởng chi/trục"
            severity = "Nặng"
            treatment = "Điều trị tích cực, có thể cần IVIG/plasma exchange, cân nhắc thymectomy"
        else:
            mgfa_class = "Class IVb"
            class_description = "Yếu nặng, chủ yếu ảnh hưởng hầu họng/hô hấp"
            severity = "Rất nặng"
            treatment = "Điều trị tích cực tại bệnh viện, IVIG/plasma exchange, cân nhắc ICU"
    elif moderate_weakness:
        if predominantly_limb_axial:
            mgfa_class = "Class IIIa"
            class_description = "Yếu trung bình, chủ yếu ảnh hưởng chi/trục"
            severity = "Trung bình"
            treatment = "Điều trị tích cực, pyridostigmine, có thể cần immunosuppression"
        else:
            mgfa_class = "Class IIIb"
            class_description = "Yếu trung bình, chủ yếu ảnh hưởng hầu họng/hô hấp"
            severity = "Trung bình-Nặng"
            treatment = "Điều trị tích cực, theo dõi sát, có thể cần IVIG"
    else:  # mild_weakness
        if predominantly_limb_axial:
            mgfa_class = "Class IIa"
            class_description = "Yếu nhẹ, chủ yếu ảnh hưởng chi/trục"
            severity = "Nhẹ"
            treatment = "Pyridostigmine, theo dõi, có thể cần immunosuppression"
        else:
            mgfa_class = "Class IIb"
            class_description = "Yếu nhẹ, chủ yếu ảnh hưởng hầu họng/hô hấp"
            severity = "Nhẹ-Trung bình"
            treatment = "Pyridostigmine, theo dõi sát, cân nhắc immunosuppression"
    
    return {
        "mgfa_class": mgfa_class,
        "class_description": class_description,
        "severity": severity,
        "treatment": treatment
    }


def render():
    """Render MGFA Clinical Classification interface"""
    import streamlit as st
    
    st.set_page_config(page_title="MGFA Classification", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🧠 MGFA Clinical Classification</h2>
    <p style='text-align: center; color: #6B7280;'>
    Myasthenia Gravis Foundation of America Clinical Classification<br>
    Phân loại mức độ nặng của bệnh nhược cơ
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về MGFA Clinical Classification"):
        st.markdown("""
        **MGFA Clinical Classification** là hệ thống phân loại chuẩn hóa mức độ nặng 
        của bệnh nhược cơ (Myasthenia Gravis).
        
        ### Phân loại:
        - **Class I:** Chỉ có triệu chứng mắt
        - **Class II:** Yếu nhẹ (ngoài mắt)
          - IIa: Chủ yếu chi/trục
          - IIb: Chủ yếu hầu họng/hô hấp
        - **Class III:** Yếu trung bình (ngoài mắt)
          - IIIa: Chủ yếu chi/trục
          - IIIb: Chủ yếu hầu họng/hô hấp
        - **Class IV:** Yếu nặng (ngoài mắt)
          - IVa: Chủ yếu chi/trục
          - IVb: Chủ yếu hầu họng/hô hấp
        - **Class V:** Cần đặt nội khí quản
        
        ### Ứng dụng lâm sàng:
        - Phân loại chuẩn hóa mức độ nặng MG
        - Hướng dẫn quyết định điều trị
        - Theo dõi tiến triển bệnh
        - Dùng trong thần kinh
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá lâm sàng")
    
    st.markdown("#### Mức độ yếu")
    
    ocular_only = st.checkbox(
        "Chỉ có triệu chứng mắt (sụp mi, nhìn đôi)",
        key="mgfa_ocular"
    )
    
    if not ocular_only:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            mild_weakness = st.checkbox(
                "Yếu nhẹ (ngoài mắt)",
                key="mgfa_mild"
            )
        
        with col2:
            moderate_weakness = st.checkbox(
                "Yếu trung bình (ngoài mắt)",
                key="mgfa_moderate"
            )
        
        with col3:
            severe_weakness = st.checkbox(
                "Yếu nặng (ngoài mắt)",
                key="mgfa_severe"
            )
        
        intubation_required = st.checkbox(
            "Cần đặt nội khí quản",
            key="mgfa_intubation"
        )
        
        if mild_weakness or moderate_weakness or severe_weakness:
            st.markdown("#### Vị trí yếu chủ yếu")
            
            col1, col2 = st.columns(2)
            
            with col1:
                predominantly_limb_axial = st.checkbox(
                    "Chủ yếu ảnh hưởng chi/trục",
                    key="mgfa_limb"
                )
            
            with col2:
                predominantly_oropharyngeal_respiratory = st.checkbox(
                    "Chủ yếu ảnh hưởng hầu họng/hô hấp",
                    key="mgfa_oropharyngeal"
                )
    else:
        mild_weakness = False
        moderate_weakness = False
        severe_weakness = False
        intubation_required = False
        predominantly_limb_axial = False
        predominantly_oropharyngeal_respiratory = False
    
    if st.button("🔬 Phân loại MGFA", type="primary", use_container_width=True):
        result = classify_mgfa(
            ocular_only=ocular_only,
            mild_weakness=mild_weakness if not ocular_only else False,
            moderate_weakness=moderate_weakness if not ocular_only else False,
            severe_weakness=severe_weakness if not ocular_only else False,
            intubation_required=intubation_required if not ocular_only else False,
            predominantly_limb_axial=predominantly_limb_axial if not ocular_only else False,
            predominantly_oropharyngeal_respiratory=predominantly_oropharyngeal_respiratory if not ocular_only else False
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả MGFA Classification")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("MGFA Class", result['mgfa_class'])
        
        with col2:
            st.metric("Mức độ", result['severity'])
        
        st.info(f"**{result['class_description']}**")
        
        # Clinical recommendations
        st.markdown("### 💡 Khuyến nghị điều trị")
        
        if result['mgfa_class'] == "Class I":
            st.success(f"**{result['mgfa_class']}** - {result['severity']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
        elif result['mgfa_class'].startswith("Class II"):
            st.info(f"**{result['mgfa_class']}** - {result['severity']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
        elif result['mgfa_class'].startswith("Class III"):
            st.warning(f"**{result['mgfa_class']}** - {result['severity']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
        elif result['mgfa_class'].startswith("Class IV"):
            st.error(f"**{result['mgfa_class']}** - {result['severity']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
        else:  # Class V
            st.error(f"**{result['mgfa_class']}** - {result['severity']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mgfa",
            calculator_name="MGFA Clinical Classification",
            inputs={
                "Chỉ mắt": "Có" if ocular_only else "Không",
                "Yếu nhẹ": "Có" if mild_weakness else "Không",
                "Yếu trung bình": "Có" if moderate_weakness else "Không",
                "Yếu nặng": "Có" if severe_weakness else "Không",
                "Cần đặt NKQ": "Có" if intubation_required else "Không"
            },
            result={
                "MGFA Class": result['mgfa_class'],
                "Mức độ": result['severity']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="mgfa",
            calculator_name="MGFA Clinical Classification"
        )
        
        render_export_section(
            calculator_id="mgfa",
            calculator_name="MGFA Clinical Classification",
            data={
                "inputs": {
                    "ocular_only": ocular_only,
                    "mild_weakness": mild_weakness,
                    "moderate_weakness": moderate_weakness,
                    "severe_weakness": severe_weakness,
                    "intubation_required": intubation_required,
                    "predominantly_limb_axial": predominantly_limb_axial,
                    "predominantly_oropharyngeal_respiratory": predominantly_oropharyngeal_respiratory
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="mgfa", show_actions=True)
    
    # References
    references = get_references("MGFA Clinical Classification")
    if references:
        render_references_section(references)

