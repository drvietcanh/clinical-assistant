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
from .vietnamese_terms import get_vietnamese_label, COMMON_TERMS_VI
from .ui_helpers import (
    SEVERITY_COLORS, REGIMEN_BADGE_COLORS, RECOMMENDATION_COLORS,
    render_skeleton_loader, render_empty_state
)
from .mic_breakpoints import get_common_susceptibility
from .resistance_patterns import get_antibiotic_resistance_summary


def render_protocol_card(protocol: AntibioticProtocol, key_prefix: str = ""):
    """Render a single protocol card with regimens"""
    
    # Color coding based on severity using helper
    bg_color, border_color = SEVERITY_COLORS.get(protocol.severity, ("#f5f5f5", "#757575"))
    
    # Card header with improved design
    st.markdown(f"""
    <div style='
        background: {bg_color};
        border-left: 4px solid {border_color};
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    '>
        <h3 style='margin: 0 0 8px 0; color: #212121; font-size: 1.5em; font-weight: 600;'>{protocol.title}</h3>
        <p style='margin: 0 0 12px 0; color: #666; font-size: 0.95em; line-height: 1.6;'>{protocol.description or ''}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Guideline badge with improved design
    if protocol.guideline_source:
        guideline_text = f"{protocol.guideline_source}"
        if protocol.guideline_year:
            guideline_text += f" ({protocol.guideline_year})"
        if protocol.last_reviewed:
            guideline_text += f" • Cập nhật: {protocol.last_reviewed}"
        st.markdown(f"""
        <div style='margin-bottom: 12px;'>
            <span style='
                background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                color: #1976d2;
                padding: 6px 14px;
                border-radius: 12px;
                font-size: 0.85em;
                font-weight: 600;
                box-shadow: 0 2px 4px rgba(25,118,210,0.2);
            '>📋 {guideline_text}</span>
        </div>
        """, unsafe_allow_html=True)
    
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
    
    # Badge colors with Vietnamese labels using helper
    badge_color, badge_icon = REGIMEN_BADGE_COLORS.get(regimen.regimen_type, ("#757575", "💊"))
    badge_text = f"{badge_icon} {regimen.regimen_type.get_vietnamese_label()}"
    
    # Recommendation level badge with Vietnamese using helper
    rec_badge = ""
    if regimen.recommendation_level:
        rec_color = RECOMMENDATION_COLORS.get(regimen.recommendation_level, "#757575")
        rec_text = regimen.recommendation_level.get_vietnamese_label()
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
    
    # Enhanced card design with better shadows and spacing - Mobile responsive
    st.markdown(f"""
    <style>
    .regimen-card-mobile {{
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 1px solid #e0e0e0;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }}
    
    @media (max-width: 768px) {{
        .regimen-card-mobile {{
            padding: 16px !important;
            margin-bottom: 12px !important;
            border-radius: 12px !important;
        }}
    }}
    </style>
    <div class="regimen-card-mobile">
        <div style='margin-bottom: 12px;'>
            <span style='
                background: {badge_color};
                color: white;
                padding: 6px 14px;
                border-radius: 12px;
                font-size: 0.85em;
                font-weight: 600;
            '>{badge_text}</span>
            {rec_badge}
        </div>
        <p style='margin: 0 0 12px 0; color: #666; font-size: 0.95em; line-height: 1.6;'><strong>{COMMON_TERMS_VI.get('Indication', 'Chỉ định')}:</strong> {regimen.indication}</p>
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
            # Link to Drug Detail
            if st.button(COMMON_TERMS_VI.get("Detail", "📖 Chi tiết"), key=f"{key_prefix}_drug_{drug.drug_name}_detail", use_container_width=True):
                st.session_state.drug_search_query = drug.drug_name
                st.switch_page("pages/07_💊_Drug_Database.py")
            
            # Link to TDM if needed
            if needs_tdm:
                if st.button(COMMON_TERMS_VI.get("TDM", "📊 TDM"), key=f"{key_prefix}_drug_{drug.drug_name}_tdm", use_container_width=True):
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
    
    # Mobile: Stack vertically, Desktop: 4 columns
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .action-buttons-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
    }
    @media (min-width: 769px) {
        .action-buttons-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
        }
    }
    </style>
    <div class="action-buttons-container">
    """, unsafe_allow_html=True)
    
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
        # Print-friendly button - use Streamlit components approach
        try:
            from components.print_friendly import inject_print_styles
            if st.button("📄 In", key=f"{key_prefix}_print", use_container_width=True, help="In phác đồ"):
                inject_print_styles()
                st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang")
        except ImportError:
            # Fallback: just show info
            if st.button("📄 In", key=f"{key_prefix}_print", use_container_width=True, help="In phác đồ"):
                st.info("💡 Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang")
    
    st.markdown("</div>", unsafe_allow_html=True)


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
            for protocol in site_protocols:
                render_protocol_card(protocol, key_prefix=f"{site}_{protocol.severity.value}")


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
    
    # Add responsive CSS for mobile optimization and print-friendly styles
    st.markdown("""
    <style>
    /* Mobile optimizations */
    @media (max-width: 768px) {
        /* Buttons */
        .stButton > button {
            min-height: 48px !important;
            font-size: 1em !important;
            padding: 12px 16px !important;
            width: 100% !important;
            margin-bottom: 8px !important;
        }
        
        .stButton > button:active {
            transform: scale(0.98);
            opacity: 0.9;
        }
        
        /* Expanders */
        .stExpander {
            font-size: 0.95em !important;
        }
        
        /* Cards - Full width */
        .protocol-card,
        .regimen-card {
            width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            padding: 16px !important;
        }
        
        /* Columns - Stack on mobile */
        .stColumns {
            flex-direction: column !important;
        }
        
        .stColumns > div {
            width: 100% !important;
            margin-bottom: 12px !important;
        }
        
        /* Search bar */
        .stTextInput > div > div > input {
            font-size: 1em !important;
            padding: 12px !important;
        }
        
        /* Quick suggestions - Stack vertically on very small screens */
        @media (max-width: 480px) {
            .quick-suggestions {
                flex-direction: column !important;
            }
        }
    }
    
    /* Print styles */
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
    """, unsafe_allow_html=True)
    
    protocols_collection = get_antibiotic_protocols()
    
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
    
    # Enhanced search bar with autocomplete suggestions - Sticky on mobile
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .sticky-search-container {
            position: sticky;
            top: 0;
            z-index: 100;
            background: white;
            padding: 12px 0;
            margin-bottom: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        [data-theme="dark"] .sticky-search-container {
            background: #1e1e1e;
        }
    }
    </style>
    <div class="sticky-search-container">
    """, unsafe_allow_html=True)
    
    search_query = st.text_input(
        COMMON_TERMS_VI.get("Search protocols", "🔍 Tìm kiếm phác đồ"),
        placeholder=COMMON_TERMS_VI.get("Search by infection, drug, or guideline...", "Tìm theo nhiễm trùng, thuốc hoặc hướng dẫn..."),
        key="ab_search_protocols",
        help="Tìm kiếm theo tên nhiễm trùng, tên thuốc, hoặc nguồn hướng dẫn"
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
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
        
        render_protocols_by_infection(filtered_protocols)
    else:
        render_empty_state(
            COMMON_TERMS_VI.get("No protocols found. Try adjusting your filters or search query.", "Không tìm thấy phác đồ"),
            "🔍"
        )


def render_antibiotics_by_drug_class_view():
    """View for 'By Drug Class' tab"""
    
    st.info(f"💊 **{COMMON_TERMS_VI.get('By Drug Class', 'Theo Nhóm Thuốc')}** - Đang phát triển")
    st.markdown(f"""
    {COMMON_TERMS_VI.get('This view will organize antibiotics by drug class:', 'Chế độ xem này sẽ tổ chức kháng sinh theo nhóm thuốc:')}
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
    
    st.info(f"🔄 **{COMMON_TERMS_VI.get('Stewardship', 'Quản lý Kháng Sinh')}** - Đang phát triển")
    st.markdown(f"""
    {COMMON_TERMS_VI.get('This view will include:', 'Chế độ xem này sẽ bao gồm:')}
    - {COMMON_TERMS_VI.get('De-escalation guidelines', 'Hướng dẫn giảm liều')}
    - {COMMON_TERMS_VI.get('IV → PO switch criteria', 'Tiêu chí chuyển IV → PO')}
    - {COMMON_TERMS_VI.get('Renal dosing summary', 'Tóm tắt liều theo thận')}
    - {COMMON_TERMS_VI.get('Duration of therapy recommendations', 'Khuyến cáo thời gian điều trị')}
    - {COMMON_TERMS_VI.get('Antibiotic stewardship principles', 'Nguyên tắc quản lý kháng sinh')}
    """)
