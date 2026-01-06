"""
Antibiotics UI View Component
Modern UI for displaying antibiotic protocols with filters and cards
"""

import streamlit as st
from typing import List, Optional
from .protocols_schema import (
    AntibioticProtocol, ProtocolCollection,
    InfectionSite, Severity, Setting, RegimenType, RecommendationLevel
)
from .protocols_data import get_antibiotic_protocols


def render_protocol_card(protocol: AntibioticProtocol, key_prefix: str = ""):
    """Render a single protocol card with regimens"""
    
    # Color coding based on severity
    severity_colors = {
        Severity.MILD: "#e8f5e9",  # Green
        Severity.MODERATE: "#fff3e0",  # Yellow/Orange
        Severity.SEVERE: "#ffebee",  # Light red
        Severity.ICU: "#fce4ec"  # Pink
    }
    
    severity_borders = {
        Severity.MILD: "#4caf50",
        Severity.MODERATE: "#ff9800",
        Severity.SEVERE: "#f44336",
        Severity.ICU: "#e91e63"
    }
    
    bg_color = severity_colors.get(protocol.severity, "#f5f5f5")
    border_color = severity_borders.get(protocol.severity, "#757575")
    
    # Card header
    st.markdown(f"""
    <div style='
        background: {bg_color};
        border-left: 4px solid {border_color};
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    '>
        <h3 style='margin: 0 0 8px 0; color: #212121;'>{protocol.title}</h3>
        <p style='margin: 0 0 12px 0; color: #666; font-size: 0.9em;'>{protocol.description or ''}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Guideline badge
    if protocol.guideline_source:
        guideline_text = f"{protocol.guideline_source}"
        if protocol.guideline_year:
            guideline_text += f" ({protocol.guideline_year})"
        st.markdown(f"""
        <div style='margin-bottom: 12px;'>
            <span style='
                background: #e3f2fd;
                color: #1976d2;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 0.85em;
                font-weight: 600;
            '>📋 {guideline_text}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Link to Critical Care for sepsis/severe infections
    if protocol.infection_site == InfectionSite.SEPSIS or protocol.severity == Severity.ICU:
        if st.button("🫁 Open Critical Care Protocol", key=f"{key_prefix}_critical_care_link", use_container_width=True):
            st.switch_page("pages/09_🫁_Critical_Care.py")
        st.markdown("---")
    
    # Render regimens
    for idx, regimen in enumerate(protocol.regimens):
        render_regimen_card(regimen, key_prefix=f"{key_prefix}_regimen_{idx}")
    
    # Notes
    if protocol.notes:
        with st.expander("📝 Notes", expanded=False):
            for note in protocol.notes:
                st.markdown(f"• {note}")
    
    # Risk factors
    if protocol.risk_factors:
        st.markdown("**⚠️ Risk Factors:**")
        for risk in protocol.risk_factors:
            st.markdown(f"- {risk}")
    
    st.markdown("---")


def render_regimen_card(regimen, key_prefix: str = ""):
    """Render a single regimen card"""
    
    # Badge colors
    type_colors = {
        RegimenType.FIRST_LINE: ("#4caf50", "🟢 First-line"),
        RegimenType.ALTERNATIVE: ("#ff9800", "🟡 Alternative"),
        RegimenType.RESCUE: ("#f44336", "🔴 Rescue"),
        RegimenType.STEP_DOWN: ("#2196f3", "💊 Step-down")
    }
    
    badge_color, badge_text = type_colors.get(regimen.regimen_type, ("#757575", "Regimen"))
    
    # Recommendation level badge
    rec_badge = ""
    if regimen.recommendation_level:
        rec_colors = {
            RecommendationLevel.STRONG: "#4caf50",
            RecommendationLevel.WEAK: "#ff9800",
            RecommendationLevel.CONDITIONAL: "#ffc107"
        }
        rec_color = rec_colors.get(regimen.recommendation_level, "#757575")
        rec_text = regimen.recommendation_level.value.title()
        rec_badge = f"""
        <span style='
            background: {rec_color};
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75em;
            margin-left: 8px;
        '>{rec_text}</span>
        """
    
    st.markdown(f"""
    <div style='
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    '>
        <div style='margin-bottom: 12px;'>
            <span style='
                background: {badge_color};
                color: white;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 0.85em;
                font-weight: 600;
            '>{badge_text}</span>
            {rec_badge}
        </div>
        <p style='margin: 0 0 12px 0; color: #666; font-size: 0.9em;'><strong>Indication:</strong> {regimen.indication}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Drugs with links to Drug Detail
    st.markdown("**Drugs:**")
    for drug in regimen.drugs:
        drug_text = f"{drug.drug_name} {drug.dose} {drug.route} {drug.frequency}"
        if drug.duration:
            drug_text += f" × {drug.duration}"
        
        # Check if drug needs TDM
        tdm_drugs = ["vancomycin", "aminoglycoside", "gentamicin", "tobramycin", "amikacin"]
        needs_tdm = any(tdm in drug.drug_name.lower() for tdm in tdm_drugs)
        
        col_drug1, col_drug2 = st.columns([3, 1])
        with col_drug1:
            st.markdown(f"- {drug_text}")
            if drug.notes:
                st.caption(f"  ⚠️ {drug.notes}")
        with col_drug2:
            # Link to Drug Detail
            if st.button("📖 Detail", key=f"{key_prefix}_drug_{drug.drug_name}_detail", use_container_width=True):
                st.session_state.drug_search_query = drug.drug_name
                st.switch_page("pages/07_💊_Drug_Database.py")
            
            # Link to TDM if needed
            if needs_tdm:
                if st.button("📊 TDM", key=f"{key_prefix}_drug_{drug.drug_name}_tdm", use_container_width=True):
                    st.switch_page("pages/08_📊_TDM.py")
    
    # Rationale
    if regimen.rationale:
        st.markdown(f"**Rationale:** {regimen.rationale}")
    
    # Warnings
    if regimen.warnings:
        st.warning("⚠️ " + " | ".join(regimen.warnings))
    
    # Step-down options
    if regimen.step_down_options:
        with st.expander("💊 Step-down Options (IV → PO)", expanded=False):
            for step_down in regimen.step_down_options:
                step_text = f"{step_down.drug_name} {step_down.dose} {step_down.route} {step_down.frequency}"
                if step_down.duration:
                    step_text += f" × {step_down.duration}"
                st.markdown(f"- {step_text}")
    
    # Special populations
    if regimen.special_populations:
        with st.expander("👥 Special Populations", expanded=False):
            for pop, note in regimen.special_populations.items():
                st.markdown(f"**{pop.title()}:** {note}")
    
    # Integration links
    st.markdown("---")
    col_link1, col_link2, col_link3 = st.columns(3)
    with col_link1:
        if st.button("🔍 Global Search", key=f"{key_prefix}_global_search", use_container_width=True):
            st.switch_page("pages/20_🔍_Global_Search.py")
    with col_link2:
        # Link to Critical Care for sepsis/severe infections
        if st.button("🫁 Critical Care", key=f"{key_prefix}_critical_care", use_container_width=True):
            st.switch_page("pages/09_🫁_Critical_Care.py")
    with col_link3:
        if st.button("💊 Drug Database", key=f"{key_prefix}_drug_db", use_container_width=True):
            st.switch_page("pages/07_💊_Drug_Database.py")


def render_protocols_by_infection(protocols: List[AntibioticProtocol]):
    """Render protocols grouped by infection site"""
    
    # Group by infection site
    sites = {}
    for protocol in protocols:
        site = protocol.infection_site.value
        if site not in sites:
            sites[site] = []
        sites[site].append(protocol)
    
    # Render each site
    for site, site_protocols in sites.items():
        with st.expander(f"🦠 {site}", expanded=True):
            for protocol in site_protocols:
                render_protocol_card(protocol, key_prefix=f"{site}_{protocol.severity.value}")


def render_filters_sidebar(protocols: ProtocolCollection):
    """Render filter sidebar"""
    
    st.markdown("### 🔍 Filters")
    
    # Infection site filter
    sites = list(set([p.infection_site.value for p in protocols.protocols]))
    selected_sites = st.multiselect(
        "Infection Site",
        sites,
        default=sites,
        key="filter_site"
    )
    
    # Severity filter
    severities = list(set([p.severity.value for p in protocols.protocols]))
    selected_severities = st.multiselect(
        "Severity",
        severities,
        default=severities,
        key="filter_severity"
    )
    
    # Setting filter
    settings = list(set([p.setting.value for p in protocols.protocols]))
    selected_settings = st.multiselect(
        "Setting",
        settings,
        default=settings,
        key="filter_setting"
    )
    
    # Guideline source filter
    sources = list(set([p.guideline_source for p in protocols.protocols if p.guideline_source]))
    if sources:
        selected_sources = st.multiselect(
            "Guideline Source",
            sources,
            default=sources,
            key="filter_source"
        )
    else:
        selected_sources = []
    
    return {
        "sites": [InfectionSite(s) for s in selected_sites] if selected_sites else None,
        "severities": [Severity(s) for s in selected_severities] if selected_severities else None,
        "settings": [Setting(s) for s in selected_settings] if selected_settings else None,
        "sources": selected_sources if selected_sources else None
    }


def filter_protocols(protocols: ProtocolCollection, filters: dict) -> List[AntibioticProtocol]:
    """Filter protocols based on filter criteria"""
    
    results = protocols.protocols
    
    if filters.get("sites") and len(filters["sites"]) > 0:
        results = [p for p in results if p.infection_site in filters["sites"]]
    
    if filters.get("severities") and len(filters["severities"]) > 0:
        results = [p for p in results if p.severity in filters["severities"]]
    
    if filters.get("settings") and len(filters["settings"]) > 0:
        results = [p for p in results if p.setting in filters["settings"]]
    
    if filters.get("sources") and len(filters["sources"]) > 0:
        results = [p for p in results if p.guideline_source in filters["sources"]]
    
    return results


def render_antibiotics_by_infection_view():
    """Main view for 'By Infection' tab"""
    
    protocols_collection = get_antibiotic_protocols()
    
    # Wizard button (prominent on mobile)
    col_wiz1, col_wiz2, col_wiz3 = st.columns([1, 2, 1])
    with col_wiz2:
        if st.button("🧙 Start Antibiotic Wizard", type="primary", use_container_width=True):
            st.session_state.show_wizard = True
    
    # Show wizard if requested
    if st.session_state.get("show_wizard", False):
        from .wizard import render_antibiotic_wizard
        render_antibiotic_wizard()
        if st.button("← Back to Protocols", key="wizard_back"):
            st.session_state.show_wizard = False
            st.rerun()
        return
    
    # Search bar
    search_query = st.text_input(
        "🔍 Search protocols",
        placeholder="Search by infection, drug, or guideline...",
        key="ab_search_protocols"
    )
    
    # Filters in sidebar
    with st.sidebar:
        filters = render_filters_sidebar(protocols_collection)
    
    # Filter protocols
    filtered_protocols = filter_protocols(protocols_collection, filters)
    
    # Search filter
    if search_query:
        search_lower = search_query.lower()
        filtered_protocols = [
            p for p in filtered_protocols
            if (search_lower in p.title.lower() or
                (search_lower in p.description.lower() if p.description else False) or
                any(search_lower in r.indication.lower() for r in p.regimens) or
                any(search_lower in d.drug_name.lower() for r in p.regimens for d in r.drugs))
        ]
    
    # Display results
    if filtered_protocols:
        st.markdown(f"**Found {len(filtered_protocols)} protocol(s)**")
        st.markdown("---")
        
        render_protocols_by_infection(filtered_protocols)
    else:
        st.info("No protocols found. Try adjusting your filters or search query.")


def render_antibiotics_by_drug_class_view():
    """View for 'By Drug Class' tab"""
    
    st.info("💊 **By Drug Class** view - Coming soon")
    st.markdown("""
    This view will organize antibiotics by drug class:
    - Beta-lactams (Penicillins, Cephalosporins, Carbapenems)
    - Fluoroquinolones
    - Macrolides
    - Glycopeptides
    - Others
    
    Each class will show:
    - Spectrum of activity
    - Common indications
    - Dosing guidelines
    - Resistance patterns
    """)


def render_stewardship_view():
    """View for 'Stewardship & Dosing' tab"""
    
    st.info("🔄 **Stewardship & Dosing** view - Coming soon")
    st.markdown("""
    This view will include:
    - De-escalation guidelines
    - IV → PO switch criteria
    - Renal dosing summary
    - Duration of therapy recommendations
    - Antibiotic stewardship principles
    """)
