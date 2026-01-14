"""
Antibiotics UI View Component
Modern UI for displaying antibiotic protocols with filters and cards
"""

import json
import time
from typing import List, Optional

import streamlit as st

from .protocols_schema import (
    AntibioticProtocol,
    ProtocolCollection,
    InfectionSite,
    Severity,
    Setting,
    RegimenType,
    RecommendationLevel,
)
from .protocols_data import get_antibiotic_protocols
from .vietnamese_terms import get_vietnamese_label, COMMON_TERMS_VI
from .ui_helpers import (
    SEVERITY_COLORS,
    REGIMEN_BADGE_COLORS,
    RECOMMENDATION_COLORS,
    render_skeleton_loader,
    render_empty_state,
    slugify_for_key,
    make_protocol_key,
    make_drug_key,
)
from .mic_breakpoints import get_common_susceptibility
from .resistance_patterns import get_antibiotic_resistance_summary
from .antibiogram import (
    get_antibiogram,
    get_available_hospitals,
    get_default_hospital_id,
    set_default_hospital_id,
)
from .components.badges import render_badge, BadgeType, BadgeSize
from .components.typography import render_guideline_badge, render_indication_text
from .protocol_versioning import get_protocol_version_info


#region agent log
def _agent_debug_log_ab(hypothesis_id: str, message: str, data: dict) -> None:
    """Lightweight NDJSON logger for antibiotics debug-session."""
    try:
        payload = {
            "sessionId": "debug-session",
            "runId": "pre-fix-ab",
            "hypothesisId": hypothesis_id,
            "location": "antibiotics/ui_antibiotics_view.py",
            "message": message,
            "data": data,
            "timestamp": int(time.time() * 1000),
        }
        with open(r"d:\1app\medical\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        # Never break UI due to logging
        pass
#endregion


def render_protocol_card(protocol: AntibioticProtocol, key_prefix: str = ""):
    """Render a single protocol card with regimens"""
    
    # Get severity class for CSS
    severity_class = f"severity-{protocol.severity.value.lower()}"
    
    # Card header with CSS classes
    st.markdown(f"""
    <div class="protocol-card {severity_class}">
        <div class="card-header">
            <h3 class="card-title">{protocol.title}</h3>
        </div>
        <div class="card-body">
            <p class="indication-text">{protocol.description or ''}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Guideline badge using component
    if protocol.guideline_source:
        guideline_html = render_guideline_badge(
            protocol.guideline_source,
            protocol.guideline_year,
            protocol.last_reviewed
        )
        st.markdown(guideline_html, unsafe_allow_html=True)

    # Version + changelog (lightweight)
    try:
        vinfo = get_protocol_version_info(protocol)
        st.caption(f"🔖 Version: **{vinfo.version}** · Cập nhật: **{vinfo.last_updated}**")
        if vinfo.changelog_md:
            with st.expander("🕘 Lịch sử cập nhật (changelog)", expanded=False):
                if vinfo.author:
                    st.markdown(f"**Tác giả:** {vinfo.author}")
                if vinfo.reason:
                    st.markdown(f"**Lý do:** {vinfo.reason}")
                st.markdown(vinfo.changelog_md)
    except Exception:
        # Never break protocol rendering due to version info issues
        pass
    
    # Link to Critical Care for sepsis/severe infections
    if protocol.infection_site == InfectionSite.SEPSIS or protocol.severity == Severity.ICU:
        if st.button(COMMON_TERMS_VI.get("Open Critical Care Protocol", "🫁 Mở Phác đồ Hồi sức"), key=f"{key_prefix}_critical_care_link", use_container_width=True):
            st.switch_page("pages/09_🫁_Critical_Care.py")
        st.markdown("---")
    
    # Render regimens
    for idx, regimen in enumerate(protocol.regimens):
        render_regimen_card(regimen, key_prefix=f"{key_prefix}_regimen_{idx}")
    
    # Notes
    if protocol.notes:
        with st.expander(COMMON_TERMS_VI.get("Notes", "📝 Ghi chú"), expanded=False):
            for note in protocol.notes:
                st.markdown(f"• {note}")
    
    # Risk factors
    if protocol.risk_factors:
        st.markdown(f"**⚠️ {COMMON_TERMS_VI.get('Risk Factors', 'Yếu tố nguy cơ')}:**")
        for risk in protocol.risk_factors:
            st.markdown(f"- {risk}")
    
    st.markdown("---")


def render_regimen_card(regimen, key_prefix: str = ""):
    """Render a single regimen card with improved design"""
    
    # Get badge type
    badge_type_map = {
        RegimenType.FIRST_LINE: BadgeType.FIRST_LINE,
        RegimenType.ALTERNATIVE: BadgeType.ALTERNATIVE,
        RegimenType.RESCUE: BadgeType.RESCUE,
        RegimenType.STEP_DOWN: BadgeType.STEP_DOWN,
    }
    badge_type = badge_type_map.get(regimen.regimen_type, BadgeType.FIRST_LINE)
    badge_text = regimen.regimen_type.get_vietnamese_label()
    
    # Render badge using component
    badge_html = render_badge(badge_text, badge_type, BadgeSize.MEDIUM)
    
    # Recommendation level badge
    rec_badge_html = ""
    if regimen.recommendation_level:
        rec_type_map = {
            RecommendationLevel.STRONG: BadgeType.STRONG,
            RecommendationLevel.WEAK: BadgeType.WEAK,
            RecommendationLevel.CONDITIONAL: BadgeType.CONDITIONAL,
        }
        rec_type = rec_type_map.get(regimen.recommendation_level, BadgeType.STRONG)
        rec_text = regimen.recommendation_level.get_vietnamese_label()
        rec_badge_html = render_badge(rec_text, rec_type, BadgeSize.SMALL)
    
    # Evidence level badge
    evidence_badge_html = ""
    if hasattr(regimen, 'evidence_level') and regimen.evidence_level:
        from .protocols_schema import EvidenceLevel
        evidence_type_map = {
            EvidenceLevel.A: BadgeType.EVIDENCE_A,
            EvidenceLevel.B: BadgeType.EVIDENCE_B,
            EvidenceLevel.C: BadgeType.EVIDENCE_C,
            EvidenceLevel.D: BadgeType.EVIDENCE_D,
        }
        evidence_type = evidence_type_map.get(regimen.evidence_level, BadgeType.EVIDENCE_C)
        evidence_text = f"Evidence: {regimen.evidence_level.value}"
        evidence_badge_html = render_badge(evidence_text, evidence_type, BadgeSize.SMALL)
    
    # Render indication text using component
    indication_html = render_indication_text(
        regimen.indication,
        COMMON_TERMS_VI.get('Indication', 'Chỉ định') + ":"
    )
    
    # Enhanced card design with CSS classes
    st.markdown(f"""
    <div class="regimen-card">
        <div class="card-badges">
            {badge_html}
            {rec_badge_html}
            {evidence_badge_html}
        </div>
        {indication_html}
    </div>
    """, unsafe_allow_html=True)
    
    # Drugs with links to Drug Detail
    st.markdown(f"**{COMMON_TERMS_VI.get('Drugs', 'Thuốc')}:**")
    for drug in regimen.drugs:
        drug_text = f"{drug.drug_name} {drug.dose} {drug.route} {drug.frequency}"
        if drug.duration:
            drug_text += f" × {drug.duration}"
        
        # Check if drug needs TDM
        tdm_drugs = ["vancomycin", "aminoglycoside", "gentamicin", "tobramycin", "amikacin"]
        needs_tdm = any(tdm in drug.drug_name.lower() for tdm in tdm_drugs)
        
        # Mobile: Stack buttons, Desktop: Side-by-side
        st.markdown("""
        <style>
        @media (max-width: 768px) {
            .drug-actions {
                display: flex;
                flex-direction: column;
                gap: 8px;
                margin-top: 8px;
            }
        }
        @media (min-width: 769px) {
            .drug-actions {
                display: flex;
                flex-direction: row;
                gap: 8px;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f"- {drug_text}")
        if drug.notes:
            st.caption(f"  ⚠️ {drug.notes}")
        
        # Actions - Mobile: Stack, Desktop: Side-by-side
        col_drug1, col_drug2 = st.columns([3, 1])
        with col_drug1:
            # Empty for spacing
            pass
        with col_drug2:
            drug_key_base = make_drug_key(key_prefix, getattr(drug, "drug_name", ""))
            # Link to Drug Detail
            if st.button(
                COMMON_TERMS_VI.get("Detail", "📖 Chi tiết"),
                key=f"{drug_key_base}_detail",
                use_container_width=True,
            ):
                st.session_state.drug_search_query = drug.drug_name
                st.switch_page("pages/07_💊_Drug_Database.py")
            
            # Link to TDM if needed
            if needs_tdm:
                if st.button(
                    COMMON_TERMS_VI.get("TDM", "📊 TDM"),
                    key=f"{drug_key_base}_tdm",
                    use_container_width=True,
                ):
                    st.switch_page("pages/08_📊_TDM.py")
    
    # Rationale
    if regimen.rationale:
        st.markdown(f"**{COMMON_TERMS_VI.get('Rationale', 'Lý do')}:** {regimen.rationale}")
    
    # MIC Breakpoints and Susceptibility (for first drug if available)
    if regimen.drugs:
        first_drug = regimen.drugs[0].drug_name
        suscept_data = get_common_susceptibility(first_drug)
        if suscept_data:
            with st.expander("🔬 Độ nhạy cảm (Việt Nam)", expanded=False):
                for org, pattern in list(suscept_data.items())[:5]:  # Show top 5
                    if org != "notes":
                        # Color code based on resistance
                        if "R:" in pattern or "R " in pattern:
                            color = "#f44336"  # Red for resistant
                        elif "S (" in pattern:
                            color = "#4caf50"  # Green for sensitive
                        else:
                            color = "#666"
                        st.markdown(f"<span style='color: {color}; font-weight: 600;'>{org}:</span> {pattern}", unsafe_allow_html=True)
                if "notes" in suscept_data:
                    st.caption(f"💡 {suscept_data['notes']}")
        # Antibiogram quick view (hospital-based, Phase 1)
        with st.expander("🧫 Antibiogram theo bệnh viện (demo)", expanded=False):
            hospitals = get_available_hospitals()
            default_hospital = get_default_hospital_id(hospitals)
            hospital_id = st.selectbox(
                "Bệnh viện",
                options=list(hospitals.keys()),
                format_func=lambda k: hospitals.get(k, k),
                index=list(hospitals.keys()).index(default_hospital),
                key=f"{key_prefix}_antibiogram_hospital",
            )
            set_default_hospital_id(hospital_id)
            metric = st.radio(
                "Chỉ số",
                options=["S (%)", "I (%)", "R (%)"],
                horizontal=True,
                key=f"{key_prefix}_antibiogram_metric",
            )
            abg = get_antibiogram(hospital_id)
            rows = []
            for org, ab_map in abg.items():
                entry = ab_map.get(first_drug)
                if entry:
                    rows.append({
                        "Vi khuẩn": org,
                        metric: entry.as_dict().get(metric),
                        "N": entry.n,
                        "Ghi chú": entry.notes or ""
                    })
            if rows:
                df_abg = st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.caption("Chưa có dữ liệu cho kháng sinh này trong antibiogram demo.")
    
    # Warnings
    if regimen.warnings:
        st.warning(f"⚠️ {COMMON_TERMS_VI.get('Warnings', 'Cảnh báo')}: " + " | ".join(regimen.warnings))
    
    # Step-down options
    if regimen.step_down_options:
        with st.expander(COMMON_TERMS_VI.get("Step-down Options (IV → PO)", "💊 Tùy chọn Giảm liều (IV → PO)"), expanded=False):
            for step_down in regimen.step_down_options:
                step_text = f"{step_down.drug_name} {step_down.dose} {step_down.route} {step_down.frequency}"
                if step_down.duration:
                    step_text += f" × {step_down.duration}"
                st.markdown(f"- {step_text}")
    
    # Special populations
    if regimen.special_populations:
        with st.expander(COMMON_TERMS_VI.get("Special Populations", "👥 Đối tượng đặc biệt"), expanded=False):
            for pop, note in regimen.special_populations.items():
                st.markdown(f"**{pop.title()}:** {note}")
    
    # Integration links and actions - Mobile: Stack, Desktop: 4 columns
    st.markdown("---")
    
    # Buttons sẽ tự động stack trên mobile nhờ CSS
    col_link1, col_link2, col_link3, col_link4 = st.columns(4)
    with col_link1:
        if st.button(COMMON_TERMS_VI.get("Global Search", "🔍 Tìm kiếm"), key=f"{key_prefix}_global_search", use_container_width=True):
            st.switch_page("pages/20_🔍_Global_Search.py")
    with col_link2:
        # Link to Critical Care for sepsis/severe infections
        if st.button(COMMON_TERMS_VI.get("Critical Care", "🫁 Hồi sức"), key=f"{key_prefix}_critical_care", use_container_width=True):
            st.switch_page("pages/09_🫁_Critical_Care.py")
    with col_link3:
        if st.button(COMMON_TERMS_VI.get("Drug Database", "💊 Thuốc"), key=f"{key_prefix}_drug_db", use_container_width=True):
            st.switch_page("pages/07_💊_Drug_Database.py")
    with col_link4:
        # Export buttons dropdown
        export_col1, export_col2 = st.columns(2)
        with export_col1:
            # Print button
            try:
                from components.print_friendly import inject_print_styles
                if st.button("📄 In", key=f"{key_prefix}_print", use_container_width=True, help="In phác đồ"):
                    inject_print_styles()
                    st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang")
            except ImportError:
                if st.button("📄 In", key=f"{key_prefix}_print", use_container_width=True, help="In phác đồ"):
                    st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang")
        
        with export_col2:
            # Export dropdown
            try:
                from antibiotics.export import render_export_buttons
                export_type = st.selectbox(
                    "📥 Xuất",
                    ["PDF", "Copy", "Excel"],
                    key=f"{key_prefix}_export_type",
                    label_visibility="collapsed"
                )
                
                if export_type == "PDF":
                    # Format regimen for export
                    regimen_data = {
                        "title": f"{regimen.indication} - {regimen.regimen_type.get_vietnamese_label()}",
                        "infection_site": "N/A",
                        "severity": "N/A",
                        "guideline": "N/A",
                        "regimens": [{
                            "name": regimen.indication,
                            "drugs": [f"{d.drug_name} {d.dose} {d.route} {d.frequency}" for d in regimen.drugs],
                            "duration": regimen.duration if hasattr(regimen, 'duration') else None,
                            "notes": regimen.rationale if regimen.rationale else None
                        }]
                    }
                    render_export_buttons(
                        content_type='protocol',
                        content_data=regimen_data,
                        title=f"Phác đồ: {regimen.indication}",
                        filename=f"phac_do_{regimen.indication.replace(' ', '_')}.pdf"
                    )
                elif export_type == "Copy":
                    # Copy regimen info to clipboard
                    regimen_text = f"""
Phác đồ: {regimen.indication}
Loại: {regimen.regimen_type.get_vietnamese_label()}
Thuốc:
"""
                    for drug in regimen.drugs:
                        regimen_text += f"- {drug.drug_name} {drug.dose} {drug.route} {drug.frequency}\n"
                    if regimen.rationale:
                        regimen_text += f"\nLý do: {regimen.rationale}\n"
                    
                    from antibiotics.export import copy_to_clipboard
                    copy_to_clipboard(regimen_text, "📋 Copy")
            except ImportError:
                pass


def render_protocols_by_infection(protocols: List[AntibioticProtocol]):
    """Render protocols grouped by infection site"""
    
    # Group by infection site
    sites = {}
    for protocol in protocols:
        site = protocol.infection_site.value
        if site not in sites:
            sites[site] = []
        sites[site].append(protocol)
    
    # Render each site with Vietnamese labels
    for site, site_protocols in sites.items():
        site_vi = InfectionSite(site).get_vietnamese_label()
        with st.expander(f"🦠 {site_vi}", expanded=True):
            for idx, protocol in enumerate(site_protocols):
                key_prefix = make_protocol_key("infection", protocol, idx)
                render_protocol_card(protocol, key_prefix=key_prefix)


def render_filters_sidebar(protocols: ProtocolCollection):
    """Render filter sidebar with Vietnamese labels"""
    
    st.markdown(f"### 🔍 {COMMON_TERMS_VI.get('Filters', 'Bộ lọc')}")
    
    # Infection site filter with Vietnamese labels
    sites = list(set([p.infection_site.value for p in protocols.protocols]))
    site_labels = {InfectionSite(s).get_vietnamese_label(): s for s in sites}
    selected_site_labels = st.multiselect(
        COMMON_TERMS_VI.get("Infection Site", "Vị trí nhiễm trùng"),
        list(site_labels.keys()),
        default=list(site_labels.keys()),
        key="filter_site"
    )
    selected_sites = [site_labels[label] for label in selected_site_labels]
    
    # Severity filter with Vietnamese labels
    severities = list(set([p.severity.value for p in protocols.protocols]))
    severity_labels = {Severity(s).get_vietnamese_label(): s for s in severities}
    selected_severity_labels = st.multiselect(
        COMMON_TERMS_VI.get("Severity", "Mức độ nặng"),
        list(severity_labels.keys()),
        default=list(severity_labels.keys()),
        key="filter_severity"
    )
    selected_severities = [severity_labels[label] for label in selected_severity_labels]
    
    # Setting filter with Vietnamese labels
    settings = list(set([p.setting.value for p in protocols.protocols]))
    setting_labels = {Setting(s).get_vietnamese_label(): s for s in settings}
    selected_setting_labels = st.multiselect(
        COMMON_TERMS_VI.get("Setting", "Môi trường điều trị"),
        list(setting_labels.keys()),
        default=list(setting_labels.keys()),
        key="filter_setting"
    )
    selected_settings = [setting_labels[label] for label in selected_setting_labels]
    
    # Guideline source filter
    sources = list(set([p.guideline_source for p in protocols.protocols if p.guideline_source]))
    if sources:
        selected_sources = st.multiselect(
            COMMON_TERMS_VI.get("Guideline Source", "Nguồn hướng dẫn"),
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
    
    # Add print-friendly styles (mobile layout tối ưu đã được xử lý qua CSS chung)
    st.markdown(
        """
    <style>
    @media print {
        .stButton, .stSidebar, .stHeader {
            display: none !important;
        }
        .main .block-container {
            max-width: 100% !important;
            padding: 10px !important;
        }
        h1, h2, h3 {
            page-break-after: avoid;
        }
        .protocol-card, .regimen-card {
            page-break-inside: avoid;
            border: 1px solid #000 !important;
        }
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    
    protocols_collection = get_antibiotic_protocols()

    #region agent log
    _agent_debug_log_ab(
        "H_ab_state",
        "render_antibiotics_by_infection_view entry",
        {
            "has_protocols": bool(protocols_collection and protocols_collection.protocols),
            "session_keys": list(getattr(st.session_state, "keys", lambda: [])()),
            "ab_search_protocols": st.session_state.get("ab_search_protocols", None),
        },
    )
    #endregion
    
    # Wizard button (prominent on mobile)
    col_wiz1, col_wiz2, col_wiz3 = st.columns([1, 2, 1])
    with col_wiz2:
        if st.button(COMMON_TERMS_VI.get("Start Antibiotic Wizard", "🧙 Bắt đầu Trợ lý Chọn Kháng Sinh"), type="primary", use_container_width=True):
            st.session_state.show_wizard = True
    
    # Show wizard if requested
    if st.session_state.get("show_wizard", False):
        from .wizard import render_antibiotic_wizard
        render_antibiotic_wizard()
        if st.button(COMMON_TERMS_VI.get("Back to Protocols", "← Quay lại Phác đồ"), key="wizard_back"):
            st.session_state.show_wizard = False
            st.rerun()
        return
    
    # Enhanced search bar with autocomplete suggestions
    # Use a separate widget key to avoid directly mutating widget-managed session_state
    current_search_state = st.session_state.get("ab_search_protocols", "")
    search_query = st.text_input(
        COMMON_TERMS_VI.get("Search protocols", "🔍 Tìm kiếm phác đồ"),
        value=current_search_state,
        placeholder=COMMON_TERMS_VI.get(
            "Search by infection, drug, or guideline...",
            "Tìm theo nhiễm trùng, thuốc hoặc hướng dẫn...",
        ),
        key="ab_search_protocols_input",
        help="Tìm kiếm theo tên nhiễm trùng, tên thuốc, hoặc nguồn hướng dẫn",
    )

    # Mirror widget value into our own state key (not bound to any widget)
    st.session_state.ab_search_protocols = search_query

    #region agent log
    _agent_debug_log_ab(
        "H_ab_state",
        "After search_input",
        {
            "search_query": search_query,
            "ab_search_protocols": st.session_state.get("ab_search_protocols", None),
        },
    )
    #endregion
    
    # Quick filter chips (only show when no search query)
    if not search_query:
        st.markdown("""
        <style>
        .quick-filter-chips {
            display: flex;
            gap: 8px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }
        
        @media (max-width: 768px) {
            .quick-filter-chips {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                padding-bottom: 8px;
                margin-bottom: 12px;
            }
            
            .quick-filter-chip {
                min-width: 80px;
                white-space: nowrap;
            }
        }
        
        @media (min-width: 769px) {
            .quick-filter-chips {
                justify-content: flex-start;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.caption("💡 Gợi ý tìm kiếm nhanh:")
        
        # Quick filter chips
        suggestions = [
            ("CAP", "CAP", "🦠"),
            ("UTI", "UTI", "💧"),
            ("Sepsis", "Sepsis", "🩸"),
            ("MRSA", "MRSA", "🦠"),
            ("ICU", "ICU", "🏥"),
            ("Pneumonia", "Pneumonia", "🫁")
        ]
        
        # Create columns for chips
        num_cols = min(len(suggestions), 6)
        cols = st.columns(num_cols)
        
        for idx, (label, value, icon) in enumerate(suggestions):
            with cols[idx % num_cols]:
                chip_key = f"quick_chip_{value.lower()}"
                # Check if this chip is active
                is_active = st.session_state.get("ab_search_protocols", "") == value
                
                chip_style = """
                <style>
                .quick-chip-button {
                    border-radius: 20px;
                    padding: 8px 16px;
                    font-size: 0.9em;
                    border: 2px solid #e0e0e0;
                    background: white;
                    transition: all 0.2s;
                }
                .quick-chip-button:active {
                    transform: scale(0.95);
                }
                </style>
                """
                
                if st.button(f"{icon} {label}", key=chip_key, use_container_width=True):
                    #region agent log
                    _agent_debug_log_ab(
                        "H_ab_state",
                        "Quick filter chip clicked",
                        {
                            "chip_value": value,
                            "prev_ab_search_protocols": st.session_state.get(
                                "ab_search_protocols", None
                            ),
                        },
                    )
                    #endregion

                    # Update our own state key (safe, not a widget key)
                    st.session_state.ab_search_protocols = value
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Filters - Mobile: Bottom sheet, Desktop: Sidebar
    try:
        from antibiotics.mobile_ui import render_mobile_filters_button, render_mobile_filters_sheet_content
        
        # Show filter button on mobile
        show_filters_sheet = render_mobile_filters_button()
        
        # Render filters in appropriate location
        if show_filters_sheet:
            # Mobile: Bottom sheet
            filters = render_mobile_filters_sheet_content(
                protocols_collection,
                render_filters_sidebar
            )
            # Use default filters if sheet returns None
            if filters is None:
                filters = {"sites": None, "severities": None, "settings": None, "sources": None}
        else:
            # Desktop: Sidebar
            with st.sidebar:
                filters = render_filters_sidebar(protocols_collection)
    except ImportError:
        # Fallback to sidebar
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
    
    # Display results with loading/empty states
    if filtered_protocols:
        # Results header with export option
        col_results1, col_results2 = st.columns([3, 1])
        with col_results1:
            st.markdown(f"**{COMMON_TERMS_VI.get('Found', 'Tìm thấy')} {len(filtered_protocols)} {COMMON_TERMS_VI.get('protocol(s)', 'phác đồ')}**")
        with col_results2:
            # Export functionality
            export_text = f"Danh sách Phác đồ Kháng Sinh\n{'='*50}\n\n"
            for protocol in filtered_protocols:
                export_text += f"{protocol.title}\n"
                export_text += f"Vị trí: {protocol.infection_site.get_vietnamese_label()}\n"
                export_text += f"Mức độ: {protocol.severity.get_vietnamese_label()}\n"
                if protocol.guideline_source:
                    export_text += f"Hướng dẫn: {protocol.guideline_source}\n"
                export_text += "\n"
            
            st.download_button(
                "📥 Xuất danh sách",
                export_text,
                file_name=f"phac_do_khang_sinh_{len(filtered_protocols)}.txt",
                mime="text/plain",
                key="download_protocols",
                use_container_width=True
            )
        st.markdown("---")
        
        # Add lazy loading class to cards
        st.markdown("""
        <script>
        // Add lazy-load-card class to all protocol cards
        setTimeout(function() {
            const cards = document.querySelectorAll('.protocol-card, .regimen-card');
            cards.forEach(function(card) {
                card.classList.add('lazy-load-card');
            });
        }, 100);
        </script>
        """, unsafe_allow_html=True)
        
        render_protocols_by_infection(filtered_protocols)
    else:
        render_empty_state(
            COMMON_TERMS_VI.get("No protocols found. Try adjusting your filters or search query.", "Không tìm thấy phác đồ"),
            "🔍"
        )


def render_antibiotics_by_drug_class_view():
    """View for 'By Drug Class' tab"""
    
    try:
        from .drug_classes_data import ALL_DRUG_CLASSES, DrugClass
        from .mic_breakpoints import get_common_susceptibility
        from .resistance_patterns import RESISTANCE_PATTERNS_VN
    except ImportError:
        st.error("Không thể tải dữ liệu nhóm thuốc. Vui lòng kiểm tra lại.")
        return
    
    # Add responsive CSS
    st.markdown("""
    <style>
    .drug-class-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-left: 4px solid #1976D2;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .drug-item-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        border-left: 3px solid #4caf50;
    }
    
    @media (max-width: 768px) {
        .drug-class-card {
            padding: 16px !important;
            margin-bottom: 16px !important;
        }
        
        .drug-item-card {
            padding: 12px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### 💊 {COMMON_TERMS_VI.get('By Drug Class', 'Theo Nhóm Thuốc')}")
    st.caption("Tổ chức kháng sinh theo nhóm thuốc với thông tin về phổ tác dụng, chỉ định, liều dùng và mô hình kháng thuốc")
    
    # Search/filter
    search_query = st.text_input(
        "🔍 Tìm kiếm nhóm thuốc hoặc thuốc",
        placeholder="Ví dụ: Beta-lactam, Vancomycin, Ciprofloxacin...",
        key="drug_class_search"
    )
    
    # Filter drug classes
    filtered_classes = ALL_DRUG_CLASSES
    if search_query:
        search_lower = search_query.lower()
        filtered_classes = [
            dc for dc in ALL_DRUG_CLASSES
            if (search_lower in dc.class_name.lower() or
                search_lower in dc.class_name_vi.lower() or
                search_lower in dc.description.lower() or
                any(search_lower in drug.name.lower() or 
                    (drug.vietnamese_name and search_lower in drug.vietnamese_name.lower())
                    for drug in dc.drugs))
        ]
    
    if not filtered_classes:
        render_empty_state(
            "Không tìm thấy nhóm thuốc phù hợp. Vui lòng thử từ khóa khác.",
            "🔍"
        )
        return
    
    st.markdown(f"**Tìm thấy {len(filtered_classes)} nhóm thuốc**")
    st.markdown("---")
    
    # Render each drug class
    for drug_class in filtered_classes:
        # Class header card
        st.markdown(f"""
        <div class="drug-class-card">
            <h2 style='margin: 0 0 8px 0; color: #1976D2; font-size: 1.8em; font-weight: 600;'>
                💊 {drug_class.class_name_vi} ({drug_class.class_name})
            </h2>
            <p style='margin: 0 0 12px 0; color: #666; font-size: 1em; line-height: 1.6;'>
                {drug_class.description}
            </p>
            <p style='margin: 0 0 16px 0; color: #555; font-size: 0.95em;'>
                <strong>Cơ chế:</strong> {drug_class.mechanism}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Spectrum summary
        with st.expander(f"📊 Phổ tác dụng", expanded=False):
            st.markdown(f"**{drug_class.spectrum_summary}**")
            
            # Show individual drug spectrums
            st.markdown("**Chi tiết theo từng thuốc:**")
            for drug in drug_class.drugs:
                if drug.spectrum:
                    st.markdown(f"- **{drug.name}**: {drug.spectrum}")
        
        # Common indications
        with st.expander(f"🎯 Chỉ định thường gặp", expanded=True):
            for indication in drug_class.common_indications:
                st.markdown(f"- {indication}")
        
        # Resistance patterns
        with st.expander(f"🦠 Mô hình kháng thuốc", expanded=False):
            st.markdown(f"**{drug_class.resistance_patterns}**")
            
            # Show resistance notes for individual drugs
            st.markdown("**Chi tiết theo từng thuốc:**")
            for drug in drug_class.drugs:
                if drug.resistance_notes:
                    st.markdown(f"- **{drug.name}**: {drug.resistance_notes}")
        
        # Clinical notes
        if drug_class.clinical_notes:
            st.info(f"💡 **Lưu ý lâm sàng:** {drug_class.clinical_notes}")
        
        # Individual drugs in this class
        st.markdown("### 📋 Thuốc trong nhóm")
        
        for drug in drug_class.drugs:
            st.markdown(f"""
            <div class="drug-item-card">
                <h3 style='margin: 0 0 8px 0; color: #212121; font-size: 1.3em; font-weight: 600;'>
                    {drug.name}
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            col_drug1, col_drug2 = st.columns([2, 1])
            
            with col_drug1:
                if drug.vietnamese_name:
                    st.caption(f"Tên tiếng Việt: {drug.vietnamese_name}")
                
                if drug.common_indications:
                    st.markdown("**Chỉ định:**")
                    for ind in drug.common_indications:
                        st.markdown(f"- {ind}")
                
                if drug.dosing_summary:
                    st.markdown(f"**Liều dùng:** {drug.dosing_summary}")
                
                if drug.spectrum:
                    st.markdown(f"**Phổ tác dụng:** {drug.spectrum}")
                
                if drug.resistance_notes:
                    st.warning(f"⚠️ **Kháng thuốc:** {drug.resistance_notes}")
                
                # AWaRe classification
                if drug.aware_classification:
                    aware_colors = {
                        "ACCESS": "#4caf50",
                        "WATCH": "#ffc107",
                        "RESERVE": "#f44336"
                    }
                    aware_color = aware_colors.get(drug.aware_classification, "#757575")
                    st.markdown(f"""
                    <span style='
                        background: {aware_color};
                        color: white;
                        padding: 4px 12px;
                        border-radius: 8px;
                        font-size: 0.85em;
                        font-weight: 600;
                    '>AWaRe: {drug.aware_classification}</span>
                    """, unsafe_allow_html=True)
            
            with col_drug2:
                # Link to Drug Database
                if st.button("📖 Chi tiết", key=f"drug_detail_{drug.name}_{drug_class.class_name}", use_container_width=True):
                    st.session_state.drug_search_query = drug.name
                    st.switch_page("pages/07_💊_Drug_Database.py")
                
                # Link to TDM if applicable
                tdm_drugs = ["vancomycin", "gentamicin", "tobramycin", "amikacin"]
                if any(tdm in drug.name.lower() for tdm in tdm_drugs):
                    if st.button("📊 TDM", key=f"tdm_{drug.name}_{drug_class.class_name}", use_container_width=True):
                        st.switch_page("pages/08_📊_TDM.py")
                
                # Show MIC/susceptibility if available
                suscept_data = get_common_susceptibility(drug.name)
                if suscept_data:
                    with st.expander("🔬 Độ nhạy cảm", expanded=False):
                        for org, pattern in list(suscept_data.items())[:3]:
                            if org != "notes":
                                st.caption(f"**{org}**: {pattern}")
        
            st.markdown("---")
        
        st.markdown("<br>", unsafe_allow_html=True)


def render_stewardship_view():
    """View for 'Stewardship & Dosing' tab"""
    
    try:
        from .stewardship import (
            render_de_escalation_view,
            render_iv_to_po_view,
            render_renal_dosing_view,
            render_treatment_duration_view,
            render_principles_view
        )
    except ImportError:
        st.error("Không thể tải các module quản lý kháng sinh. Vui lòng kiểm tra lại.")
        return
    
    st.markdown(f"### 🔄 {COMMON_TERMS_VI.get('Stewardship', 'Quản lý Kháng Sinh')}")
    st.caption("Các công cụ và hướng dẫn để quản lý kháng sinh hiệu quả")
    
    # Create tabs for different stewardship topics
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔄 De-escalation",
        "💊 IV → PO",
        "🫘 Liều theo Thận",
        "⏱️ Thời gian Điều trị",
        "📋 Nguyên tắc"
    ])
    
    with tab1:
        render_de_escalation_view()
    
    with tab2:
        render_iv_to_po_view()
    
    with tab3:
        render_renal_dosing_view()
    
    with tab4:
        render_treatment_duration_view()
    
    with tab5:
        render_principles_view()
