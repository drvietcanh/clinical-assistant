"""
Protocol Calculators Integration
Quick access to calculators from protocols
"""

import streamlit as st
from typing import List, Dict, Optional


# Mapping of protocols to relevant calculators
PROTOCOL_CALCULATOR_MAP = {
    "Sepsis": [
        {"name": "qSOFA Score", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "qsofa"},
        {"name": "SOFA Score", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "sofa"},
        {"name": "SIRS Criteria", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "sirs"}
    ],
    "Stroke": [
        {"name": "NIHSS Score", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "nihss"},
        {"name": "Modified Rankin Scale", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "mrs"}
    ],
    "DKA": [
        {"name": "Anion Gap Calculator", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "anion_gap"},
        {"name": "Corrected Sodium", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "corrected_na"}
    ],
    "Heart Failure": [
        {"name": "Ejection Fraction Calculator", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "ef"},
        {"name": "BNP/NT-proBNP", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "bnp"}
    ],
    "ACS": [
        {"name": "TIMI Risk Score", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "timi"},
        {"name": "GRACE Score", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "grace"}
    ],
    "DVT/PE": [
        {"name": "Wells Score", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "wells_pe"},
        {"name": "PERC Rule", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "perc"}
    ],
    "AKI": [
        {"name": "Creatinine Clearance", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "creatinine_clearance"},
        {"name": "eGFR Calculator", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "egfr"}
    ],
    "Dosing": [
        {"name": "Weight-Based Dosing", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "weight_dosing"},
        {"name": "Renal Dosing Adjustment", "page": "pages/05_🔬_Labs_and_Calculators.py", "calc_id": "renal_dosing"}
    ]
}


def get_calculators_for_protocol(protocol_name: str) -> List[Dict]:
    """
    Get list of relevant calculators for a protocol.
    
    Args:
        protocol_name: Name of the protocol
        
    Returns:
        List of calculator dicts
    """
    calculators = []
    
    # Check for exact match
    if protocol_name in PROTOCOL_CALCULATOR_MAP:
        calculators.extend(PROTOCOL_CALCULATOR_MAP[protocol_name])
    
    # Check for partial matches
    protocol_lower = protocol_name.lower()
    for key, calcs in PROTOCOL_CALCULATOR_MAP.items():
        if key.lower() in protocol_lower or protocol_lower in key.lower():
            # Avoid duplicates
            for calc in calcs:
                if calc not in calculators:
                    calculators.append(calc)
    
    # Add general dosing calculators for most protocols
    if "Dosing" not in protocol_name and len(calculators) > 0:
        # Add weight-based dosing if not already present
        has_dosing = any("dosing" in calc.get("name", "").lower() for calc in calculators)
        if not has_dosing:
            calculators.append({
                "name": "Weight-Based Dosing",
                "page": "pages/05_🔬_Labs_and_Calculators.py",
                "calc_id": "weight_dosing"
            })
    
    return calculators


def render_calculator_links(protocol_name: str, calculators: Optional[List[Dict]] = None):
    """
    Render calculator links section.
    
    Args:
        protocol_name: Name of the protocol
        calculators: Optional pre-determined calculator list
    """
    if calculators is None:
        calculators = get_calculators_for_protocol(protocol_name)
    
    if not calculators:
        return
    
    with st.expander("🧮 Công cụ tính toán liên quan", expanded=False):
        st.markdown("**Các công cụ hữu ích cho protocol này:**")
        st.markdown("")
        
        for calc in calculators:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"📊 **{calc['name']}**")
            with col2:
                if st.button("Mở", key=f"calc_{calc['calc_id']}_{protocol_name}".replace(" ", "_"), 
                            use_container_width=True):
                    # Set calculator to open
                    st.session_state['calculator_to_open'] = calc.get('calc_id')
                    st.switch_page(calc['page'])


def render_quick_calculator_embed(calculator_name: str, calc_id: str):
    """
    Render a quick calculator embed (simplified version).
    This is a placeholder - full implementation would require
    importing actual calculator components.
    
    Args:
        calculator_name: Display name of calculator
        calc_id: Calculator ID
    """
    st.markdown(f"### 🧮 {calculator_name}")
    st.info(f"💡 Tính năng embed calculator đang được phát triển. Vui lòng sử dụng link bên trên để mở calculator đầy đủ.")


def render_dosing_calculator_quick(weight_kg: float = None):
    """
    Quick dosing calculator embedded in protocol.
    
    Args:
        weight_kg: Patient weight in kg (optional)
    """
    st.markdown("### 💉 Tính Liều Nhanh")
    
    if weight_kg is None:
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            key="protocol_weight"
        )
    
    dose_per_kg = st.number_input(
        "Liều (mg/kg):",
        min_value=0.1,
        max_value=100.0,
        value=10.0,
        step=0.1,
        key="protocol_dose_per_kg"
    )
    
    total_dose = weight_kg * dose_per_kg
    
    st.success(f"**Tổng liều:** {total_dose:.2f} mg")
    
    # Common dosing examples
    st.caption("💡 **Ví dụ:**")
    st.caption(f"- 10 mg/kg = {10 * weight_kg:.1f} mg")
    st.caption(f"- 20 mg/kg = {20 * weight_kg:.1f} mg")
    st.caption(f"- 50 mg/kg = {50 * weight_kg:.1f} mg")

