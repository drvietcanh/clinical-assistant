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
from .vietnamese_terms import get_vietnamese_label, COMMON_TERMS_VI


def render_antibiotic_wizard():
    """Render the Antibiotic Wizard form and recommendations"""
    
    st.markdown("### 🧙 Trợ lý Chọn Kháng Sinh")
    st.caption("Nhập thông tin lâm sàng để nhận đề xuất phác đồ kháng sinh")
    
    protocols_collection = get_antibiotic_protocols()
    
    # Form inputs
    col1, col2 = st.columns(2)
    
    with col1:
        # Site of infection with Vietnamese labels
        infection_sites = {
            InfectionSite.CAP.get_vietnamese_label(): InfectionSite.CAP,
            InfectionSite.HAP.get_vietnamese_label(): InfectionSite.HAP,
            InfectionSite.VAP.get_vietnamese_label(): InfectionSite.VAP,
            InfectionSite.UTI.get_vietnamese_label(): InfectionSite.UTI,
            InfectionSite.SSTI.get_vietnamese_label(): InfectionSite.SSTI,
            InfectionSite.CNS.get_vietnamese_label(): InfectionSite.CNS,
            InfectionSite.IAI.get_vietnamese_label(): InfectionSite.IAI,
            InfectionSite.BACTEREMIA.get_vietnamese_label(): InfectionSite.BACTEREMIA,
            InfectionSite.SEPSIS.get_vietnamese_label(): InfectionSite.SEPSIS
        }
        
        site_display = st.selectbox(
            f"🦠 {COMMON_TERMS_VI.get('Infection Site', 'Vị trí nhiễm trùng')}",
            list(infection_sites.keys()),
            key="wizard_site"
        )
        selected_site = infection_sites[site_display]
        
        # Severity with Vietnamese labels
        severities = {
            Severity.MILD.get_vietnamese_label(): Severity.MILD,
            Severity.MODERATE.get_vietnamese_label(): Severity.MODERATE,
            Severity.SEVERE.get_vietnamese_label(): Severity.SEVERE,
            Severity.ICU.get_vietnamese_label(): Severity.ICU
        }
        
        severity_display = st.selectbox(
            f"⚡ {COMMON_TERMS_VI.get('Severity', 'Mức độ nặng')}",
            list(severities.keys()),
            key="wizard_severity"
        )
        selected_severity = severities[severity_display]
    
    with col2:
        # Setting with Vietnamese labels
        settings = {
            Setting.OPD.get_vietnamese_label(): Setting.OPD,
            Setting.WARD.get_vietnamese_label(): Setting.WARD,
            Setting.ICU.get_vietnamese_label(): Setting.ICU
        }
        
        setting_display = st.selectbox(
            f"🏥 {COMMON_TERMS_VI.get('Setting', 'Môi trường điều trị')}",
            list(settings.keys()),
            key="wizard_setting"
        )
        selected_setting = settings[setting_display]
        
        # Comorbidities
        st.markdown(f"**{COMMON_TERMS_VI.get('Comorbidities', 'Bệnh kèm theo')}:**")
        has_ckd = st.checkbox(COMMON_TERMS_VI.get("CKD", "Bệnh thận mạn"), key="wizard_ckd")
        is_immunocompromised = st.checkbox(COMMON_TERMS_VI.get("Immunocompromised", "Suy giảm miễn dịch"), key="wizard_immuno")
        is_pregnant = st.checkbox(COMMON_TERMS_VI.get("Pregnancy", "Mang thai"), key="wizard_pregnant")
    
    # Risk factors
    st.markdown(f"**⚠️ {COMMON_TERMS_VI.get('Risk Factors', 'Yếu tố nguy cơ')}:**")
    col3, col4, col5 = st.columns(3)
    with col3:
        risk_mrsa = st.checkbox("Nguy cơ MRSA", key="wizard_mrsa")
        risk_pseudomonas = st.checkbox("Nguy cơ Pseudomonas", key="wizard_pseudomonas")
    with col4:
        risk_esbl = st.checkbox("Nguy cơ ESBL", key="wizard_esbl")
        recent_hospitalization = st.checkbox("Nhập viện gần đây", key="wizard_hosp")
    with col5:
        beta_lactam_allergy = st.checkbox("Dị ứng beta-lactam", key="wizard_allergy")
    
    st.markdown("---")
    
    # Generate recommendations
    if st.button(COMMON_TERMS_VI.get("Get Recommendations", "🔍 Nhận Đề xuất"), type="primary", use_container_width=True):
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
            st.success(f"✅ {COMMON_TERMS_VI.get('Found', 'Tìm thấy')} {len(recommendations)} {COMMON_TERMS_VI.get('recommendation(s)', 'đề xuất')}")
            st.markdown("---")
            
            for idx, (protocol, regimen) in enumerate(recommendations[:3], 1):  # Show top 3
                st.markdown(f"### {COMMON_TERMS_VI.get('Recommendation', 'Đề xuất')} {idx}")
                
                # Show protocol info
                st.info(f"**{protocol.title}** - {protocol.guideline_source or 'Phác đồ chuẩn'}")
                
                # Show regimen
                from .ui_antibiotics_view import render_regimen_card
                render_regimen_card(regimen, key_prefix=f"wizard_rec_{idx}")
                
                # Special considerations
                considerations = []
                if has_ckd:
                    considerations.append(f"⚠️ {COMMON_TERMS_VI.get('Adjust dose for renal function', 'Điều chỉnh liều theo chức năng thận')}")
                if is_pregnant:
                    considerations.append(f"⚠️ {COMMON_TERMS_VI.get('Consider pregnancy safety', 'Cân nhắc an toàn khi mang thai')}")
                if beta_lactam_allergy:
                    considerations.append(f"⚠️ {COMMON_TERMS_VI.get('Beta-lactam allergy - alternative regimen', 'Dị ứng beta-lactam - phác đồ thay thế')}")
                
                if considerations:
                    st.warning(" | ".join(considerations))
                
                st.markdown("---")
        else:
            st.warning(COMMON_TERMS_VI.get("No matching protocols found. Try adjusting your criteria.", "Không tìm thấy phác đồ phù hợp. Vui lòng điều chỉnh tiêu chí."))


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
