"""
Antibiotic Wizard
Form-based tool to recommend antibiotic regimens based on clinical scenario
"""

import streamlit as st
from typing import List, Optional
from .protocols_schema import (
    AntibioticProtocol, ProtocolCollection,
    InfectionSite, Severity, Setting
)
from .protocols_data import get_antibiotic_protocols


def render_antibiotic_wizard():
    """Render the Antibiotic Wizard form and recommendations"""
    
    st.markdown("### 🧙 Antibiotic Wizard")
    st.caption("Nhập thông tin lâm sàng để nhận đề xuất phác đồ kháng sinh")
    
    protocols_collection = get_antibiotic_protocols()
    
    # Form inputs
    col1, col2 = st.columns(2)
    
    with col1:
        # Site of infection
        infection_sites = {
            "CAP": InfectionSite.CAP,
            "HAP": InfectionSite.HAP,
            "VAP": InfectionSite.VAP,
            "UTI": InfectionSite.UTI,
            "SSTI": InfectionSite.SSTI,
            "CNS": InfectionSite.CNS,
            "IAI": InfectionSite.IAI,
            "Bacteremia": InfectionSite.BACTEREMIA,
            "Sepsis": InfectionSite.SEPSIS
        }
        
        site_display = st.selectbox(
            "🦠 Site of Infection",
            list(infection_sites.keys()),
            key="wizard_site"
        )
        selected_site = infection_sites[site_display]
        
        # Severity
        severities = {
            "Mild": Severity.MILD,
            "Moderate": Severity.MODERATE,
            "Severe": Severity.SEVERE,
            "ICU": Severity.ICU
        }
        
        severity_display = st.selectbox(
            "⚡ Severity",
            list(severities.keys()),
            key="wizard_severity"
        )
        selected_severity = severities[severity_display]
    
    with col2:
        # Setting
        settings = {
            "Outpatient": Setting.OPD,
            "Ward": Setting.WARD,
            "ICU": Setting.ICU
        }
        
        setting_display = st.selectbox(
            "🏥 Setting",
            list(settings.keys()),
            key="wizard_setting"
        )
        selected_setting = settings[setting_display]
        
        # Comorbidities
        st.markdown("**Comorbidities:**")
        has_ckd = st.checkbox("CKD", key="wizard_ckd")
        is_immunocompromised = st.checkbox("Immunocompromised", key="wizard_immuno")
        is_pregnant = st.checkbox("Pregnancy", key="wizard_pregnant")
    
    # Risk factors
    st.markdown("**⚠️ Risk Factors:**")
    col3, col4, col5 = st.columns(3)
    with col3:
        risk_mrsa = st.checkbox("MRSA risk", key="wizard_mrsa")
        risk_pseudomonas = st.checkbox("Pseudomonas risk", key="wizard_pseudomonas")
    with col4:
        risk_esbl = st.checkbox("ESBL risk", key="wizard_esbl")
        recent_hospitalization = st.checkbox("Recent hospitalization", key="wizard_hosp")
    with col5:
        beta_lactam_allergy = st.checkbox("Beta-lactam allergy", key="wizard_allergy")
    
    st.markdown("---")
    
    # Generate recommendations
    if st.button("🔍 Get Recommendations", type="primary", use_container_width=True):
        recommendations = get_wizard_recommendations(
            protocols_collection,
            selected_site,
            selected_severity,
            selected_setting,
            {
                "ckd": has_ckd,
                "immunocompromised": is_immunocompromised,
                "pregnant": is_pregnant,
                "mrsa_risk": risk_mrsa,
                "pseudomonas_risk": risk_pseudomonas,
                "esbl_risk": risk_esbl,
                "beta_lactam_allergy": beta_lactam_allergy
            }
        )
        
        if recommendations:
            st.success(f"✅ Found {len(recommendations)} recommendation(s)")
            st.markdown("---")
            
            for idx, (protocol, regimen) in enumerate(recommendations[:3], 1):  # Show top 3
                st.markdown(f"### Recommendation {idx}")
                
                # Show protocol info
                st.info(f"**{protocol.title}** - {protocol.guideline_source or 'Standard protocol'}")
                
                # Show regimen
                from .ui_antibiotics_view import render_regimen_card
                render_regimen_card(regimen, key_prefix=f"wizard_rec_{idx}")
                
                # Special considerations
                considerations = []
                if has_ckd:
                    considerations.append("⚠️ Adjust dose for renal function")
                if is_pregnant:
                    considerations.append("⚠️ Consider pregnancy safety")
                if beta_lactam_allergy:
                    considerations.append("⚠️ Beta-lactam allergy - alternative regimen")
                
                if considerations:
                    st.warning(" | ".join(considerations))
                
                st.markdown("---")
        else:
            st.warning("No matching protocols found. Try adjusting your criteria.")


def get_wizard_recommendations(
    protocols: ProtocolCollection,
    site: InfectionSite,
    severity: Severity,
    setting: Setting,
    comorbidities: dict
) -> List[tuple]:
    """
    Get antibiotic recommendations based on wizard inputs
    
    Returns:
        List of tuples (protocol, regimen) sorted by priority
    """
    
    # Find matching protocols
    matching_protocols = protocols.search(
        site=site,
        severity=severity,
        setting=setting
    )
    
    if not matching_protocols:
        # Try with less specific filters
        matching_protocols = protocols.search(site=site, severity=severity)
        if not matching_protocols:
            matching_protocols = protocols.get_by_infection_site(site)
    
    # Filter regimens based on comorbidities
    recommendations = []
    
    for protocol in matching_protocols:
        for regimen in protocol.regimens:
            # Skip if beta-lactam allergy and regimen contains beta-lactam
            if comorbidities.get("beta_lactam_allergy"):
                beta_lactam_drugs = ["penicillin", "cef", "carbapenem", "piperacillin"]
                if any(beta in drug.drug_name.lower() for drug in regimen.drugs 
                       for beta in beta_lactam_drugs):
                    # Prefer alternative regimens
                    if regimen.regimen_type.value != "ALTERNATIVE":
                        continue
            
            # Prioritize regimens
            priority = 0
            if regimen.regimen_type.value == "FIRST_LINE":
                priority = 3
            elif regimen.regimen_type.value == "ALTERNATIVE":
                priority = 2
            elif regimen.regimen_type.value == "RESCUE":
                priority = 1
            
            recommendations.append((priority, protocol, regimen))
    
    # Sort by priority (highest first)
    recommendations.sort(key=lambda x: x[0], reverse=True)
    
    # Return (protocol, regimen) tuples
    return [(p, r) for _, p, r in recommendations]
