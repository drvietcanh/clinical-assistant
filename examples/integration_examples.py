"""
Integration Examples
Example code showing how to integrate new components into pages
"""

# ========== EXAMPLE 1: Calculator Visuals in Score Page ==========

def example_score_with_visual():
    """
    Example: Adding calculator visuals to a score page
    """
    code = '''
# In scores/emergency/sofa.py or similar

from components.calculator_visuals_helper import render_score_with_visual, get_default_risk_levels

# After calculating score
result = calculate_sofa(...)

# Replace old result display with:
render_score_with_visual(
    score=result['total_score'],
    score_name="SOFA Score",
    min_score=0,
    max_score=24,
    risk_levels=get_default_risk_levels("sofa"),
    interpretation=result['interpretation'],
    show_chart=True,
    show_interpretation=True
)
'''
    return code


# ========== EXAMPLE 2: Print-Friendly in Protocol Page ==========

def example_print_friendly_protocol():
    """
    Example: Adding print-friendly to a protocol page
    """
    code = '''
# In protocols/emergency/sepsis.py or similar

from components.print_friendly_helper import setup_print_friendly_page, add_print_metadata

# At the top of render() function
setup_print_friendly_page(
    page_title="Sepsis 1-Hour Bundle Protocol",
    show_button=True,
    button_position="top"
)

# Add metadata
add_print_metadata(
    title="Sepsis 1-Hour Bundle",
    author="Clinical Assistant",
    description="Surviving Sepsis Campaign 2021"
)
'''
    return code


# ========== EXAMPLE 3: Evidence Badge in Protocol ==========

def example_evidence_badge():
    """
    Example: Adding evidence badge to protocol recommendation
    """
    code = '''
# In protocols/emergency/sepsis.py

from utils.evidence_helper import quick_evidence_badge

# When showing a recommendation
st.markdown("### Recommendation")
st.markdown("Administer antibiotics within 1 hour of recognition")

# Add evidence badge
quick_evidence_badge(
    level="A",
    citation="Rhodes A, et al. Surviving Sepsis Campaign 2021...",
    doi="10.1007/s00134-021-06506-y",
    last_reviewed="2024-12-01",
    synopsis="High-quality evidence from systematic review"
)
'''
    return code


# ========== EXAMPLE 4: CDS Alerts in Drug Interaction ==========

def example_cds_alerts():
    """
    Example: CDS alerts are already integrated in drugs/interactions.py
    This is just for reference
    """
    code = '''
# Already integrated in drugs/interactions.py

from components.cds_alerts import render_cds_alerts_panel

# After checking interactions
interactions = check_interactions(drug_list)

# Generate CDS alerts
cds_alerts = []
for interaction in interactions:
    if interaction.get('severity') == SEVERITY_MAJOR:
        cds_alerts.append({
            'type': 'interaction',
            'severity': 'critical',
            'title': f"Tương tác nghiêm trọng: {interaction['drug1']} + {interaction['drug2']}",
            'message': interaction.get('description', ''),
            'recommendation': interaction.get('management', ''),
            'drugs': [interaction['drug1'], interaction['drug2']]
        })

# Render alerts
if cds_alerts:
    render_cds_alerts_panel(cds_alerts)
'''
    return code


# ========== EXAMPLE 5: Pricing/Formulary in Drug Detail ==========

def example_drug_pricing():
    """
    Example: Pricing/Formulary already integrated in drugs/drug_info_components/detail_view.py
    This is just for reference
    """
    code = '''
# Already integrated in drugs/drug_info_components/detail_view.py

# In display_drug_info() function, tab_pricing section:

from drugs.pricing import get_drug_price, format_price
from drugs.formulary import get_formulary_info, get_formulary_status_badge

# Get pricing
pricing = get_drug_price(drug_name)
if pricing:
    price_display = format_price(pricing['price_vnd'], show_usd=True)
    st.markdown(f"**Giá:** {price_display}")

# Get formulary
formulary = get_formulary_info(drug_name)
if formulary:
    badge_html = get_formulary_status_badge(formulary.status)
    st.markdown(badge_html, unsafe_allow_html=True)
'''
    return code


# ========== EXAMPLE 6: Dashboard Widgets ==========

def example_dashboard_widgets():
    """
    Example: Dashboard widgets already integrated
    """
    code = '''
# Already integrated in pages/17_🎯_Unified_Dashboard.py

from components.dashboard_widgets import render_dashboard_layout

# In Overview tab
render_dashboard_layout(
    show_quick_access=True,
    show_activity=True,
    show_recommendations=True,
    show_stats=True
)
'''
    return code


# ========== EXAMPLE 7: Calculator Comparison ==========

def example_calculator_comparison():
    """
    Example: Comparing multiple calculators
    """
    code = '''
# In a page that shows multiple scores

from components.calculator_comparison import render_calculator_comparison

# After calculating multiple scores
scores = [
    {
        'name': 'SOFA',
        'result': 8,
        'interpretation': 'Moderate severity',
        'risk_level': 'Moderate'
    },
    {
        'name': 'APACHE II',
        'result': 18,
        'interpretation': 'Moderate risk',
        'risk_level': 'Moderate'
    }
]

render_calculator_comparison(scores, title="So sánh Scores ICU")
'''
    return code


__all__ = [
    'example_score_with_visual',
    'example_print_friendly_protocol',
    'example_evidence_badge',
    'example_cds_alerts',
    'example_drug_pricing',
    'example_dashboard_widgets',
    'example_calculator_comparison',
]

