"""
Protocol Related Component
Suggest related protocols based on specialty, keywords, or clinical relationships
"""

import streamlit as st
from typing import List, Dict, Optional
from config.protocol_lists import get_protocol_list, SPECIALTY_LIST


# Related protocols mapping
RELATED_PROTOCOLS = {
    "Sepsis": [
        "Sepsis 3-Hour Bundle",
        "Septic Shock",
        "ARDS Management",
        "AKI Management",
        "Ventilator Weaning"
    ],
    "Sepsis 1-Hour Bundle": [
        "Sepsis 3-Hour Bundle",
        "Septic Shock",
        "ARDS Management"
    ],
    "Stroke": [
        "TIA Management",
        "Intracranial Hypertension",
        "Status Epilepticus"
    ],
    "DKA": [
        "HHS (Hyperglycemic Hyperosmolar State)",
        "Hypoglycemia",
        "Diabetic Nephropathy"
    ],
    "Heart Failure": [
        "Acute Decompensated HF",
        "ACS",
        "Atrial Fibrillation",
        "Hypertensive Emergency"
    ],
    "ACS": [
        "STEMI",
        "NSTEMI",
        "Heart Failure",
        "Cardiac Arrest"
    ],
    "STEMI": [
        "NSTEMI",
        "ACS",
        "Cardiac Arrest",
        "Cardiac Tamponade"
    ],
    "ARDS": [
        "Sepsis",
        "Ventilator Weaning",
        "Acute Respiratory Failure",
        "Pneumonia"
    ],
    "AKI": [
        "CKD",
        "Hepatorenal Syndrome",
        "Emergency Dialysis",
        "Electrolyte Emergency"
    ],
    "COPD": [
        "Asthma",
        "Acute Respiratory Failure",
        "Pneumonia"
    ],
    "Asthma": [
        "COPD",
        "Anaphylaxis",
        "Acute Respiratory Failure"
    ],
    "Pneumonia": [
        "CAP Management",
        "HAP/VAP Guidelines",
        "Sepsis",
        "ARDS"
    ],
    "GI Bleeding": [
        "Lower GI Bleeding",
        "Shock",
        "Transfusion",
        "Anticoagulation Reversal"
    ],
    "Anaphylaxis": [
        "Asthma",
        "Upper Airway Obstruction",
        "Shock"
    ],
    "Cardiac Arrest": [
        "ACLS",
        "STEMI",
        "Shock",
        "Malignant Arrhythmias"
    ],
    "Shock": [
        "Sepsis",
        "Cardiac Arrest",
        "GI Bleeding",
        "Anaphylaxis"
    ]
}


def get_related_protocols(protocol_name: str, specialty: str = None) -> List[str]:
    """
    Get list of related protocols for a given protocol.
    
    Args:
        protocol_name: Name of the protocol
        specialty: Optional specialty name for filtering
        
    Returns:
        List of related protocol names
    """
    related = []
    
    # Remove emoji and get clean name
    clean_name = protocol_name.split(' ', 1)[-1] if ' ' in protocol_name else protocol_name
    
    # Check exact match
    if clean_name in RELATED_PROTOCOLS:
        related.extend(RELATED_PROTOCOLS[clean_name])
    
    # Check partial matches
    for key, protocols in RELATED_PROTOCOLS.items():
        if key.lower() in clean_name.lower() or clean_name.lower() in key.lower():
            for p in protocols:
                if p not in related:
                    related.append(p)
    
    # Add protocols from same specialty if available
    if specialty:
        specialty_protocols = get_protocol_list(specialty)
        if specialty_protocols:
            # Add 2-3 protocols from same specialty (excluding current)
            same_specialty = [
                p for p in specialty_protocols 
                if p != protocol_name and p not in related
            ][:3]
            related.extend(same_specialty)
    
    # Remove duplicates and limit to 5-6
    seen = set()
    unique_related = []
    for p in related:
        if p not in seen and p != protocol_name:
            seen.add(p)
            unique_related.append(p)
            if len(unique_related) >= 6:
                break
    
    return unique_related


def render_related_protocols(protocol_name: str, specialty: str = None):
    """
    Render related protocols section.
    
    Args:
        protocol_name: Name of current protocol
        specialty: Current specialty
    """
    related = get_related_protocols(protocol_name, specialty)
    
    if not related:
        return
    
    st.markdown("---")
    st.subheader("🔗 Protocols Liên Quan")
    
    st.markdown("Các protocols có thể hữu ích cho bệnh cảnh này:")
    
    # Display as buttons or links
    cols = st.columns(min(3, len(related)))
    
    for idx, related_protocol in enumerate(related):
        with cols[idx % 3]:
            # Create button to switch to related protocol
            if st.button(
                f"📄 {related_protocol}",
                key=f"related_{related_protocol}_{protocol_name}".replace(" ", "_"),
                use_container_width=True
            ):
                # Set session state to open related protocol
                st.session_state['protocol_to_open'] = related_protocol
                if specialty:
                    st.session_state['protocol_specialty'] = specialty
                st.rerun()
    
    st.caption("💡 Chọn protocol để chuyển nhanh")


def render_related_by_keywords(keywords: List[str], specialty: str = None):
    """
    Render related protocols based on keywords.
    
    Args:
        keywords: List of keywords to search
        specialty: Optional specialty filter
    """
    if not keywords:
        return
        
    keyword_str = ", ".join(keywords)
    
    # Simple keyword matching
    all_protocols = []
    if specialty:
        all_protocols = get_protocol_list(specialty)
    else:
        # Get from all specialties
        for spec in SPECIALTY_LIST:
            all_protocols.extend(get_protocol_list(spec))
    
    # Filter by keywords
    matched = []
    for protocol in all_protocols:
        protocol_lower = protocol.lower()
        if any(kw.lower() in protocol_lower for kw in keywords):
            matched.append(protocol)
    
    if matched:
        st.markdown(f"**Tìm thấy từ khóa:** *{keyword_str}*")
        st.markdown("---")
        st.subheader("🔍 Gợi ý liên quan")
        
        cols = st.columns(min(3, len(matched[:6])))
        for idx, protocol in enumerate(matched[:6]):  # Limit to 6
            with cols[idx % 3]:
                if st.button(
                    f"📄 {protocol}",
                    key=f"keyword_{protocol}".replace(" ", "_"),
                    use_container_width=True
                ):
                    st.session_state['protocol_to_open'] = protocol
                    st.rerun()
    else:
        pass # Don't show anything if no matches found

