"""
Pregnancy & Lactation Safety Display Component
Render pregnancy and lactation safety information in drug detail view
"""

import streamlit as st
from typing import Dict, Optional
from drugs.pregnancy_lactation_safety import (
    get_pregnancy_safety,
    get_lactation_safety,
    get_safety_summary,
    FDAPregnancyCategory,
    BriggsLactationCategory,
    PregnancyRiskLevel,
    LactationRiskLevel
)


def get_risk_color(risk_level: str) -> str:
    """Get color for risk level"""
    color_map = {
        PregnancyRiskLevel.SAFE.value: "#28a745",  # Green
        PregnancyRiskLevel.PROBABLY_SAFE.value: "#17a2b8",  # Blue
        PregnancyRiskLevel.USE_CAUTION.value: "#ffc107",  # Yellow
        PregnancyRiskLevel.AVOID.value: "#fd7e14",  # Orange
        PregnancyRiskLevel.CONTRAINDICATED.value: "#dc3545",  # Red
        LactationRiskLevel.SAFE.value: "#28a745",
        LactationRiskLevel.PROBABLY_SAFE.value: "#17a2b8",
        LactationRiskLevel.USE_CAUTION.value: "#ffc107",
        LactationRiskLevel.AVOID.value: "#fd7e14",
        LactationRiskLevel.CONTRAINDICATED.value: "#dc3545",
    }
    return color_map.get(risk_level, "#6c757d")


def render_pregnancy_safety(drug_name: str) -> None:
    """
    Render pregnancy safety information
    
    Args:
        drug_name: Name of the drug
    """
    safety = get_pregnancy_safety(drug_name)
    
    if not safety:
        st.info("⚠️ Chưa có thông tin an toàn thai kỳ cho thuốc này.")
        return
    
    st.markdown("### 🤰 An toàn thai kỳ")
    
    # FDA Category
    fda_cat = safety.get("fda_category")
    if fda_cat:
        fda_value = fda_cat.value if isinstance(fda_cat, FDAPregnancyCategory) else fda_cat
        fda_colors = {
            "A": "#28a745",
            "B": "#17a2b8",
            "C": "#ffc107",
            "D": "#fd7e14",
            "X": "#dc3545"
        }
        fda_color = fda_colors.get(fda_value, "#6c757d")
        
        st.markdown(f"""
        <div style="
            padding: 1rem;
            background: {fda_color}15;
            border-left: 4px solid {fda_color};
            border-radius: 4px;
            margin-bottom: 1rem;
        ">
            <strong>FDA Pregnancy Category: {fda_value}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk Level
    risk_level = safety.get("risk_level")
    if risk_level:
        risk_value = risk_level.value if isinstance(risk_level, PregnancyRiskLevel) else risk_level
        risk_color = get_risk_color(risk_value)
        
        st.markdown(f"""
        <div style="
            padding: 0.75rem;
            background: {risk_color}15;
            border: 2px solid {risk_color};
            border-radius: 4px;
            margin-bottom: 1rem;
            text-align: center;
        ">
            <strong style="font-size: 1.1rem; color: {risk_color};">{risk_value}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Trimester-specific information
    trimester_info = safety.get("trimester_specific", {})
    if trimester_info:
        st.markdown("#### 📅 Theo từng tam cá nguyệt:")
        
        trimesters = ["first", "second", "third"]
        trimester_labels = {
            "first": "Tam cá nguyệt 1 (0-12 tuần)",
            "second": "Tam cá nguyệt 2 (13-27 tuần)",
            "third": "Tam cá nguyệt 3 (28-40 tuần)"
        }
        
        for trimester in trimesters:
            if trimester in trimester_info:
                info = trimester_info[trimester]
                st.markdown(f"**{trimester_labels[trimester]}:** {info}")
    
    # Notes
    notes = safety.get("notes")
    if notes:
        st.markdown("#### 💡 Lưu ý:")
        st.info(notes)
    
    # References
    references = safety.get("references", [])
    if references:
        with st.expander("📚 Tài liệu tham khảo"):
            for ref in references:
                st.markdown(f"- {ref}")


def render_lactation_safety(drug_name: str) -> None:
    """
    Render lactation safety information
    
    Args:
        drug_name: Name of the drug
    """
    safety = get_lactation_safety(drug_name)
    
    if not safety:
        st.info("⚠️ Chưa có thông tin an toàn cho con bú cho thuốc này.")
        return
    
    st.markdown("### 🍼 An toàn cho con bú")
    
    # Briggs Category
    briggs_cat = safety.get("briggs_category")
    if briggs_cat:
        briggs_value = briggs_cat.value if isinstance(briggs_cat, BriggsLactationCategory) else briggs_cat
        briggs_colors = {
            "L1": "#28a745",
            "L2": "#17a2b8",
            "L3": "#ffc107",
            "L4": "#fd7e14",
            "L5": "#dc3545"
        }
        briggs_color = briggs_colors.get(briggs_value, "#6c757d")
        
        briggs_labels = {
            "L1": "Safest",
            "L2": "Safer",
            "L3": "Moderately Safe",
            "L4": "Possibly Hazardous",
            "L5": "Contraindicated"
        }
        
        st.markdown(f"""
        <div style="
            padding: 1rem;
            background: {briggs_color}15;
            border-left: 4px solid {briggs_color};
            border-radius: 4px;
            margin-bottom: 1rem;
        ">
            <strong>Briggs Lactation Category: {briggs_value} ({briggs_labels.get(briggs_value, '')})</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk Level
    risk_level = safety.get("risk_level")
    if risk_level:
        risk_value = risk_level.value if isinstance(risk_level, LactationRiskLevel) else risk_level
        risk_color = get_risk_color(risk_value)
        
        st.markdown(f"""
        <div style="
            padding: 0.75rem;
            background: {risk_color}15;
            border: 2px solid {risk_color};
            border-radius: 4px;
            margin-bottom: 1rem;
            text-align: center;
        ">
            <strong style="font-size: 1.1rem; color: {risk_color};">{risk_value}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Notes
    notes = safety.get("notes")
    if notes:
        st.markdown("#### 💡 Lưu ý:")
        st.info(notes)
    
    # References
    references = safety.get("references", [])
    if references:
        with st.expander("📚 Tài liệu tham khảo"):
            for ref in references:
                st.markdown(f"- {ref}")


def render_pregnancy_lactation_section(drug_name: str) -> None:
    """
    Render complete pregnancy and lactation safety section
    
    Args:
        drug_name: Name of the drug
    """
    st.markdown("---")
    st.subheader("🤰 An toàn thai kỳ & cho con bú")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_pregnancy_safety(drug_name)
    
    with col2:
        render_lactation_safety(drug_name)
    
    # Warning
    st.warning("""
    ⚠️ **Lưu ý quan trọng:**
    - Thông tin này chỉ mang tính tham khảo
    - Luôn tham khảo ý kiến bác sĩ trước khi dùng thuốc trong thai kỳ hoặc khi cho con bú
    - Cân nhắc lợi ích/nguy cơ cho từng trường hợp cụ thể
    - Một số thuốc có thể cần điều chỉnh liều trong thai kỳ
    """)

