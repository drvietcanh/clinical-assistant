"""
Smart Calculator Suggestions Component
Suggest related calculators based on context and usage patterns
"""

import streamlit as st
from typing import List, Dict, Optional, Any
from config.calculators import ALL_CALCULATORS


# Calculator relationships map
CALCULATOR_RELATIONSHIPS: Dict[str, List[str]] = {
    # Cardiology relationships
    "cha2ds2vasc": ["hasbled", "qtc", "nyha", "killip", "grace", "timi"],
    "hasbled": ["cha2ds2vasc", "padua", "wells_dvt", "wells_pe"],
    "nyha": ["killip", "grace", "heart", "ascvd", "score2"],
    "killip": ["nyha", "grace", "heart", "timi"],
    "grace": ["timi", "heart", "nyha", "killip"],
    "timi": ["grace", "heart", "nyha", "killip"],
    "heart": ["grace", "timi", "nyha"],
    "ascvd": ["score2", "score2_op", "framingham", "nyha"],
    "score2": ["score2_op", "ascvd", "framingham"],
    "score2_op": ["score2", "ascvd", "framingham"],
    "qtc": ["cha2ds2vasc", "hasbled"],
    
    # Emergency relationships
    "qsofa": ["sofa", "sofa2", "news2", "mews", "saps2", "apache2"],
    "sofa": ["qsofa", "sofa2", "saps2", "apache2", "mods", "lods"],
    "sofa2": ["sofa", "qsofa", "saps2", "apache2"],
    "news2": ["mews", "qsofa", "sofa"],
    "mews": ["news2", "qsofa"],
    "saps2": ["saps3", "apache2", "apache3", "sofa"],
    "saps3": ["saps2", "apache3", "sofa"],
    "apache2": ["apache3", "saps2", "saps3", "sofa"],
    "apache3": ["apache2", "saps3", "sofa"],
    "mods": ["lods", "sofa"],
    "lods": ["mods", "sofa"],
    
    # Respiratory relationships
    "wells_pe": ["perc", "pesi", "wells_dvt"],
    "perc": ["wells_pe", "pesi"],
    "pesi": ["wells_pe", "perc"],
    "curb65": ["psi_port", "smartcop", "bode"],
    "psi_port": ["curb65", "smartcop"],
    "smartcop": ["curb65", "psi_port"],
    "bode": ["curb65", "psi_port"],
    "ards_berlin": ["sofa", "sofa2"],
    
    # Neurology relationships
    "gcs": ["nihss", "four_score", "hunt_hess", "ich_score", "mrs"],
    "nihss": ["gcs", "aspects", "abcd2", "mrs"],
    "ich_score": ["gcs", "hunt_hess", "mrs"],
    "hunt_hess": ["gcs", "ich_score"],
    "mrs": ["nihss", "gcs", "ich_score", "abcd2"],
    "abcd2": ["nihss", "mrs"],
    "aspects": ["nihss"],
    "four_score": ["gcs"],
    "barthel": ["mrs", "gcs"],
    
    # GI/Hepatology relationships
    "child_pugh": ["meld", "meld_na", "bisap"],
    "meld": ["meld_na", "child_pugh"],
    "meld_na": ["meld", "child_pugh"],
    "bisap": ["ranson", "child_pugh"],
    "ranson": ["bisap"],
    "glasgow_blatchford": ["rockall", "aims65"],
    "rockall": ["glasgow_blatchford", "aims65"],
    "aims65": ["glasgow_blatchford", "rockall"],
    
    # Nephrology relationships
    "egfr": ["kdigo", "rifle", "akin", "crcl", "fena"],
    "kdigo": ["egfr", "rifle", "akin"],
    "rifle": ["akin", "kdigo", "egfr"],
    "akin": ["rifle", "kdigo", "egfr"],
    "crcl": ["egfr", "kdigo"],
    "fena": ["egfr", "rifle", "akin"],
    
    # Hematology relationships
    "padua": ["wells_dvt", "wells_pe", "hasbled"],
    "wells_dvt": ["wells_pe", "padua", "four_ts"],
    "four_ts": ["wells_dvt", "dic_score"],
    "dic_score": ["four_ts"],
    
    # Trauma relationships
    "rts": ["iss", "triss"],
    "iss": ["rts", "triss"],
    "triss": ["rts", "iss"],
    "nexus": ["canadian_cspine"],
    "canadian_cspine": ["nexus"],
    
    # Pediatrics relationships
    "apgar": ["pews", "pediatric_gcs"],
    "pews": ["apgar", "pediatric_gcs", "pelod2", "prism3", "pim2"],
    "pediatric_gcs": ["gcs", "pews", "apgar"],
    "westley_croup": ["pews"],
    "pelod2": ["prism3", "pim2", "pews", "pediatric_sofa"],
    "prism3": ["pelod2", "pim2", "pediatric_sofa"],
    "pim2": ["pelod2", "prism3", "pediatric_sofa"],
    "pediatric_sofa": ["sofa", "pelod2", "prism3", "pim2"],
    
    # Surgery/Anesthesia relationships
    "asa": ["rcri", "goldman_cardiac", "gupta_cardiac"],
    "rcri": ["asa", "goldman_cardiac", "gupta_cardiac"],
    "goldman_cardiac": ["gupta_cardiac", "rcri", "asa"],
    "gupta_cardiac": ["goldman_cardiac", "rcri", "asa"],
    "caprini": ["padua", "wells_dvt"],
    "mallampati": ["cormack_lehane", "lemon", "el_ganzouri"],
    "cormack_lehane": ["mallampati", "lemon"],
    "lemon": ["mallampati", "cormack_lehane"],
    "el_ganzouri": ["mallampati"],
    "aldrete": ["ramsay", "rass"],
    "ramsay": ["aldrete", "rass"],
    "rass": ["ramsay", "aldrete"],
    
    # Psychiatry relationships
    "phq9": ["gad7", "mmse", "moca"],
    "gad7": ["phq9"],
    "mmse": ["moca", "cam", "phq9"],
    "moca": ["mmse", "cam"],
    "cam": ["mmse", "moca"],
    "ciwa": ["cows"],
    "cows": ["ciwa"],
    
    # Pain relationships
    "nrs": ["vas", "wong_baker", "flacc"],
    "vas": ["nrs", "wong_baker"],
    "wong_baker": ["nrs", "vas", "flacc"],
    "flacc": ["nrs", "wong_baker", "nips"],
    "nips": ["flacc"],
    "dn4": ["nrs", "vas"],
    
    # Metabolism relationships
    "bmi_ibw_bsa": ["crcl", "egfr"],
    "anion_gap": ["winter_formula", "osmolality"],
    "corrected_calcium": ["anion_gap"],
    "osmolality": ["anion_gap", "winter_formula"],
    "winter_formula": ["anion_gap", "osmolality"],
    "hba1c_eag": ["bmi_ibw_bsa"],
    "fena": ["egfr", "rifle", "akin"],
    
    # Obstetrics relationships
    "preeclampsia": ["bishop", "modified_bishop"],
    "bishop": ["modified_bishop", "preeclampsia"],
    "modified_bishop": ["bishop", "preeclampsia"],
    
    # Rheumatology relationships
    "das28": ["cdai", "sdai", "acr_ra"],
    "cdai": ["das28", "sdai"],
    "sdai": ["das28", "cdai"],
    "acr_ra": ["das28", "cdai", "sdai"],
    "sledai": ["slicc"],
    "slicc": ["sledai"],
    
    # Infectious relationships
    "centor": ["feverpain"],
    "feverpain": ["centor"],
    "sirs": ["qsofa", "sofa"],
    "mascc": ["pitt_bacteremia"],
    "pitt_bacteremia": ["mascc"],
    
    # Dermatology relationships
    "pasi": ["scorad", "dlqi"],
    "scorad": ["pasi", "dlqi"],
    "dlqi": ["pasi", "scorad"],
    "burn_tbsa": ["parkland"],
    "parkland": ["burn_tbsa"],
    
    # Oncology relationships
    "ecog": ["karnofsky", "pps"],
    "karnofsky": ["ecog", "pps"],
    "pps": ["ecog", "karnofsky"],
    
    # ENT relationships
    "stop_bang": ["epworth"],
    "epworth": ["stop_bang"],
}


def get_related_calculators(calculator_id: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Get related calculators for a given calculator
    
    Args:
        calculator_id: Current calculator ID
        limit: Maximum number of suggestions
    
    Returns:
        List of related calculator dictionaries
    """
    related_ids = CALCULATOR_RELATIONSHIPS.get(calculator_id, [])
    
    suggestions = []
    for calc_id in related_ids[:limit]:
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            suggestions.append({
                'id': calc_id,
                'name': calc_info['name'],
                'category': calc_info['category'],
                'icon': calc_info.get('icon', '📊'),
                'page': calc_info.get('page', 'Scores')
            })
    
    return suggestions


def get_suggestions_by_category(category: str, exclude_id: Optional[str] = None, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Get calculators in the same category
    
    Args:
        category: Calculator category
        exclude_id: Calculator ID to exclude
        limit: Maximum number of suggestions
    
    Returns:
        List of calculator dictionaries
    """
    suggestions = []
    for calc_id, calc_info in ALL_CALCULATORS.items():
        if calc_id == exclude_id:
            continue
        if calc_info.get('category') == category:
            suggestions.append({
                'id': calc_id,
                'name': calc_info['name'],
                'category': calc_info['category'],
                'icon': calc_info.get('icon', '📊'),
                'page': calc_info.get('page', 'Scores')
            })
            if len(suggestions) >= limit:
                break
    
    return suggestions


def get_popular_calculators(limit: int = 5) -> List[Dict[str, Any]]:
    """
    Get popular calculators (based on usage or predefined list)
    
    Args:
        limit: Maximum number of suggestions
    
    Returns:
        List of popular calculator dictionaries
    """
    # Popular calculators (can be based on analytics in the future)
    popular_ids = [
        "cha2ds2vasc", "hasbled", "sofa", "qsofa", "gcs",
        "egfr", "crcl", "nyha", "killip", "curb65",
        "wells_pe", "perc", "child_pugh", "meld", "nihss"
    ]
    
    suggestions = []
    for calc_id in popular_ids[:limit]:
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            suggestions.append({
                'id': calc_id,
                'name': calc_info['name'],
                'category': calc_info['category'],
                'icon': calc_info.get('icon', '📊'),
                'page': calc_info.get('page', 'Scores')
            })
    
    return suggestions


def render_suggestions(
    calculator_id: str,
    calculator_name: str,
    category: Optional[str] = None,
    show_related: bool = True,
    show_category: bool = True,
    show_popular: bool = False,
    limit: int = 5
) -> None:
    """
    Render smart calculator suggestions
    
    Args:
        calculator_id: Current calculator ID
        calculator_name: Current calculator name
        category: Current calculator category
        show_related: Show related calculators
        show_category: Show calculators in same category
        show_popular: Show popular calculators
        limit: Maximum suggestions per section
    """
    st.markdown("---")
    st.subheader("💡 Gợi ý Calculators liên quan")
    
    suggestions_shown = False
    
    # Related calculators
    if show_related:
        related = get_related_calculators(calculator_id, limit=limit)
        if related:
            suggestions_shown = True
            st.markdown("#### 🔗 Calculators liên quan")
            st.caption(f"Dựa trên mối quan hệ với {calculator_name}")
            
            cols = st.columns(min(len(related), 3))
            for idx, calc in enumerate(related):
                with cols[idx % len(cols)]:
                    st.markdown(f"""
                    <div style="
                        padding: 1rem;
                        background: #f8f9fa;
                        border-radius: 8px;
                        border-left: 4px solid #007bff;
                        margin-bottom: 0.5rem;
                    ">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{calc['icon']}</div>
                        <div style="font-weight: bold; margin-bottom: 0.25rem;">{calc['name']}</div>
                        <div style="font-size: 0.85rem; color: #6c757d;">{calc['category']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"▶️ Mở {calc['name']}", key=f"suggest_{calc['id']}"):
                        # Navigate to calculator
                        st.session_state['selected_calculator'] = calc['id']
                        st.rerun()
    
    # Same category calculators
    if show_category and category:
        category_calcs = get_suggestions_by_category(category, exclude_id=calculator_id, limit=limit)
        if category_calcs:
            suggestions_shown = True
            st.markdown("#### 📂 Cùng chuyên khoa")
            st.caption(f"Các calculators khác trong {category}")
            
            cols = st.columns(min(len(category_calcs), 3))
            for idx, calc in enumerate(category_calcs):
                with cols[idx % len(cols)]:
                    st.markdown(f"""
                    <div style="
                        padding: 1rem;
                        background: #f8f9fa;
                        border-radius: 8px;
                        border-left: 4px solid #28a745;
                        margin-bottom: 0.5rem;
                    ">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{calc['icon']}</div>
                        <div style="font-weight: bold; margin-bottom: 0.25rem;">{calc['name']}</div>
                        <div style="font-size: 0.85rem; color: #6c757d;">{calc['category']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"▶️ Mở {calc['name']}", key=f"category_{calc['id']}"):
                        st.session_state['selected_calculator'] = calc['id']
                        st.rerun()
    
    # Popular calculators
    if show_popular:
        popular = get_popular_calculators(limit=limit)
        if popular:
            suggestions_shown = True
            st.markdown("#### ⭐ Calculators phổ biến")
            st.caption("Các calculators được sử dụng nhiều nhất")
            
            cols = st.columns(min(len(popular), 3))
            for idx, calc in enumerate(popular):
                with cols[idx % len(cols)]:
                    st.markdown(f"""
                    <div style="
                        padding: 1rem;
                        background: #fff3cd;
                        border-radius: 8px;
                        border-left: 4px solid #ffc107;
                        margin-bottom: 0.5rem;
                    ">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{calc['icon']}</div>
                        <div style="font-weight: bold; margin-bottom: 0.25rem;">{calc['name']}</div>
                        <div style="font-size: 0.85rem; color: #6c757d;">{calc['category']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"▶️ Mở {calc['name']}", key=f"popular_{calc['id']}"):
                        st.session_state['selected_calculator'] = calc['id']
                        st.rerun()
    
    if not suggestions_shown:
        st.info("💡 Không có gợi ý nào cho calculator này.")

