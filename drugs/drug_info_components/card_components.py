"""Drug Info - Card Components (compact card, quick facts, black box warning)"""

import streamlit as st
import pandas as pd
from ..drug_database import DRUG_DATABASE

# Check if drug is antibiotic
try:
    from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
except ImportError:
    ANTIBIOTICS_DATABASE = {}

def render_compact_drug_card(drug_name, drug_data, key_prefix='',
    search_query=''):
    """Render a compact drug card in list view with optional search highlighting"""
    from .search import highlight_search_term
    vn_name = drug_data.get('vietnamese_name', '')
    group = drug_data.get('group', 'Unknown')
    admin = drug_data.get('administration', [])
    admin_str = ' / '.join(admin) if admin else 'N/A'
    highlighted_name = highlight_search_term(drug_name, search_query
        ) if search_query else drug_name
    highlighted_vn_name = highlight_search_term(vn_name, search_query
        ) if search_query and vn_name else vn_name
    group_colors = {'Cardiovascular': '#E91E63', 'Diabetes': '#9C27B0',
        'Gastrointestinal': '#FF9800', 'Analgesic': '#F44336',
        'Respiratory': '#00BCD4', 'Neurology': '#3F51B5', 'Psychiatry':
        '#673AB7'}
    badge_color = '#666'
    for group_key, color in group_colors.items():
        if group_key.lower() in group.lower():
            badge_color = color
            break
    group_split = group.split(' - ')[0] if ' - ' in group else group
    group_badge = f'<span style="background-color: {badge_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; margin-left: 8px;">{group_split}</span>'
    card_html = f"""
    <div style='
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 12px 15px;
        margin: 8px 0;
        transition: all 0.2s;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    '>
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 1;'>
                <div style='display: flex; align-items: center; margin-bottom: 6px;'>
                    <strong style='color: #1976D2; font-size: 1.05em; margin-right: 8px;'>{highlighted_name}</strong>
                    {group_badge}
                </div>
                {f"<div style='color: #666; font-size: 0.9em; margin-bottom: 4px;'>{highlighted_vn_name}</div>" if vn_name else ''}
                <div style='color: #888; font-size: 0.85em;'>{admin_str} | {group}</div>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        safe_drug_name = str(drug_name).replace(' ', '_').replace('-', '_'
            ).replace('/', '_')
        view_key = (f'{key_prefix}view_{safe_drug_name}' if key_prefix else
            f'view_{safe_drug_name}')
        if st.button('📖 Xem chi tiết', key=view_key, use_container_width=True):
            st.session_state['selected_drug'] = str(drug_name)
            st.session_state['show_detail'] = True
            st.rerun()
    with col2:
        compare_key = (f'{key_prefix}compare_{safe_drug_name}' if
            key_prefix else f'compare_{safe_drug_name}')
        if st.button('🔄 So sánh', key=compare_key, use_container_width=True):
            if 'drug_comparison_list' not in st.session_state:
                st.session_state['drug_comparison_list'] = []
            if drug_name not in st.session_state['drug_comparison_list']:
                st.session_state['drug_comparison_list'].append(drug_name)
                if len(st.session_state['drug_comparison_list']) > 5:
                    st.session_state['drug_comparison_list'
                        ] = st.session_state['drug_comparison_list'][-5:]
                st.success(f'✅ Đã thêm {drug_name} vào danh sách so sánh')
                st.rerun()
            else:
                st.info(f'ℹ️ {drug_name} đã có trong danh sách so sánh')
    with col3:
        st.empty()

def _render_quick_facts_box(drug_data):
    """Render quick facts box with key information"""
    facts = []
    if 'pregnancy' in drug_data:
        preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
        preg = drug_data['pregnancy']
        facts.append(f"**Thai kỳ:** {preg_icons.get(preg, '')} {preg}")
    if 'lactation' in drug_data:
        facts.append(f"**Cho con bú:** {drug_data['lactation']}")
    if 'pharmacokinetics' in drug_data and 'half_life' in drug_data[
        'pharmacokinetics']:
        half_life = drug_data['pharmacokinetics']['half_life']
        facts.append(f'**Half-life:** {half_life}')
    if 'monitoring' in drug_data:
        monitoring_list = drug_data['monitoring']
        if isinstance(monitoring_list, list) and len(monitoring_list) > 0:
            summary = ', '.join(monitoring_list[:3])
            if len(monitoring_list) > 3:
                summary += '...'
            facts.append(f'**Theo dõi:** {summary}')
    if 'administration' in drug_data:
        admin_icons = {'IV': '💉', 'IM': '💊', 'PO': '🍽️', 'Inhalation': '🌬️',
            'SC': '💉', 'Rectal': '📦'}
        admin_display = ' / '.join([f"{admin_icons.get(route, '')} {route}" for
            route in drug_data['administration']])
        facts.append(f'**Đường dùng:** {admin_display}')
    if not facts:
        return
    facts_html = ' | '.join(facts)
    st.markdown(
        f"""
    <div style='
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-left: 4px solid #0EA5E9;
        padding: 15px 20px;
        border-radius: 8px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(14, 165, 233, 0.1);
    '>
        <h4 style='margin: 0 0 10px 0; color: #0369a1; font-size: 1.1em;'>📊 Quick Facts</h4>
        <div style='color: #0c4a6e; font-size: 0.95em; line-height: 1.8;'>
            {facts_html}
        </div>
    </div>
    """
        , unsafe_allow_html=True)

def _render_black_box_warning(warning_text):
    """Render black box warning with prominent styling"""
    st.markdown(
        f"""
    <div style='
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border: 2px solid #dc2626;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(220, 38, 38, 0.2);
    '>
        <h3 style='color: #dc2626; margin: 0 0 10px 0; font-size: 1.2em; display: flex; align-items: center;'>
            <span style='font-size: 1.5em; margin-right: 10px;'>⚠️</span>
            CẢNH BÁO HỘP ĐEN
        </h3>
        <p style='color: #991b1b; font-size: 1.05em; margin: 0; line-height: 1.6; font-weight: 500;'>
            {warning_text}
        </p>
    </div>
    """
        , unsafe_allow_html=True)

