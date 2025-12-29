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
    search_query='', card_index=None):
    """Render a compact drug card in list view with optional search highlighting"""
    from .search import highlight_search_term
    import hashlib
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
    # Make card more clickable with hover effect (inspired by medical reference sites)
    card_html = f"""
    <div style='
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px 18px;
        margin: 10px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        cursor: pointer;
    ' 
    onmouseover="this.style.borderColor='#1976D2'; this.style.boxShadow='0 4px 12px rgba(25,118,210,0.2)'; this.style.transform='translateY(-2px)';"
    onmouseout="this.style.borderColor='#e0e0e0'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.08)'; this.style.transform='translateY(0)';">
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 1;'>
                <div style='display: flex; align-items: center; margin-bottom: 8px;'>
                    <strong style='color: #1976D2; font-size: 1.1em; margin-right: 8px; cursor: pointer;'>{highlighted_name}</strong>
                    {group_badge}
                </div>
                {f"<div style='color: #666; font-size: 0.9em; margin-bottom: 5px;'>{highlighted_vn_name}</div>" if vn_name else ''}
                <div style='color: #888; font-size: 0.85em;'>{admin_str} | {group}</div>
            </div>
            <div style='color: #1976D2; font-size: 1.2em; margin-left: 10px;'>→</div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    # Action buttons row - optimized layout (inspired by Epocrates/Drugs.com)
    col1, col2, col3 = st.columns([2, 1.5, 1])
    with col1:
        safe_drug_name = str(drug_name).replace(' ', '_').replace('-', '_'
            ).replace('/', '_').replace('(', '_').replace(')', '_')
        # Generate unique key using drug name, index, and a hash of the data
        # Always include both card_index and data hash to ensure uniqueness
        if card_index is not None:
            # Use both index and hash to ensure uniqueness even if index repeats
            data_hash = hashlib.md5(f"{drug_name}_{str(drug_data)}".encode()).hexdigest()[:8]
            unique_suffix = f'_{card_index}_{data_hash}'
        else:
            # Fallback: use hash of drug name + data to ensure uniqueness
            data_hash = hashlib.md5(f"{drug_name}_{str(drug_data)}".encode()).hexdigest()[:8]
            unique_suffix = f'_{data_hash}'
        view_key = (f'{key_prefix}view_{safe_drug_name}{unique_suffix}' if key_prefix else
            f'view_{safe_drug_name}{unique_suffix}')
        # Primary action button - more prominent
        if st.button('📖 Xem chi tiết', key=view_key, use_container_width=True, type='primary'):
            # Navigate to dedicated drug detail page
            st.session_state['view_drug_name'] = str(drug_name)
            st.switch_page("pages/Drug_Detail.py")
    with col2:
        compare_key = (f'{key_prefix}compare_{safe_drug_name}{unique_suffix}' if
            key_prefix else f'compare_{safe_drug_name}{unique_suffix}')
        if st.button('🔄 So sánh', key=compare_key, use_container_width=True, type='secondary'):
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
    """Render enhanced quick facts box with key information (inspired by Epocrates)"""
    facts_cards = []
    
    # Pregnancy
    if 'pregnancy' in drug_data:
        preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
        preg = drug_data['pregnancy']
        preg_colors = {'A': '#10B981', 'B': '#F59E0B', 'C': '#F97316', 'D': '#EF4444', 'X': '#1F2937'}
        facts_cards.append(f"""
            <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid {preg_colors.get(preg, "#64748b")}; flex: 1; min-width: 150px;'>
                <div style='color: #64748b; font-size: 0.8em; font-weight: bold; margin-bottom: 4px;'>🤰 Thai kỳ</div>
                <div style='color: #1e293b; font-size: 1em; font-weight: 600;'>{preg_icons.get(preg, '')} {preg}</div>
            </div>
        """)
    
    # Lactation
    if 'pregnancy_lactation' in drug_data and 'lactation' in drug_data['pregnancy_lactation']:
        lactation = drug_data['pregnancy_lactation']['lactation']
        safety = lactation.get('safety', 'Unknown') if isinstance(lactation, dict) else str(lactation)
        safety_icons = {'Compatible': '✅', 'Compatible with monitoring': '⚠️', 'Unknown': '❓'}
        facts_cards.append(f"""
            <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid #8B5CF6; flex: 1; min-width: 150px;'>
                <div style='color: #64748b; font-size: 0.8em; font-weight: bold; margin-bottom: 4px;'>🤱 Cho con bú</div>
                <div style='color: #1e293b; font-size: 1em; font-weight: 600;'>{safety_icons.get(safety, '❓')} {safety}</div>
            </div>
        """)
    elif 'lactation' in drug_data:
        lactation = drug_data['lactation']
        facts_cards.append(f"""
            <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid #8B5CF6; flex: 1; min-width: 150px;'>
                <div style='color: #64748b; font-size: 0.8em; font-weight: bold; margin-bottom: 4px;'>🤱 Cho con bú</div>
                <div style='color: #1e293b; font-size: 1em; font-weight: 600;'>{lactation}</div>
            </div>
        """)
    
    # Half-life
    if 'pharmacokinetics' in drug_data and 'half_life' in drug_data['pharmacokinetics']:
        half_life = drug_data['pharmacokinetics']['half_life']
        facts_cards.append(f"""
            <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid #3B82F6; flex: 1; min-width: 150px;'>
                <div style='color: #64748b; font-size: 0.8em; font-weight: bold; margin-bottom: 4px;'>⏱️ Half-life</div>
                <div style='color: #1e293b; font-size: 1em; font-weight: 600;'>{half_life}</div>
            </div>
        """)
    
    # Administration
    if 'administration' in drug_data:
        admin_icons = {'IV': '💉', 'IM': '💊', 'PO': '🍽️', 'Inhalation': '🌬️', 'SC': '💉', 'Rectal': '📦'}
        admin_routes = drug_data['administration'][:3]  # Limit to 3
        admin_display = ' '.join([f"{admin_icons.get(route, '💊')}" for route in admin_routes])
        facts_cards.append(f"""
            <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid #10B981; flex: 1; min-width: 150px;'>
                <div style='color: #64748b; font-size: 0.8em; font-weight: bold; margin-bottom: 4px;'>💊 Đường dùng</div>
                <div style='color: #1e293b; font-size: 1em; font-weight: 600;'>{admin_display}</div>
            </div>
        """)
    
    # Monitoring summary
    if 'monitoring' in drug_data:
        monitoring_list = drug_data['monitoring']
        if isinstance(monitoring_list, list) and len(monitoring_list) > 0:
            count = len(monitoring_list)
            facts_cards.append(f"""
                <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid #8B5CF6; flex: 1; min-width: 150px;'>
                    <div style='color: #64748b; font-size: 0.8em; font-weight: bold; margin-bottom: 4px;'>📊 Theo dõi</div>
                    <div style='color: #1e293b; font-size: 1em; font-weight: 600;'>{count} mục cần theo dõi</div>
                </div>
            """)
    
    if not facts_cards:
        return
    
    st.markdown(
        f"""
        <div class="quick-facts-box" style='
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border: 2px solid #e2e8f0;
            border-left: 5px solid #3B82F6;
            padding: 20px;
            border-radius: 12px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        '>
            <h4 style='margin: 0 0 15px 0; color: #1e293b; font-size: 1.2em; display: flex; align-items: center;'>
                <span style='font-size: 1.3em; margin-right: 8px;'>⚡</span>
                Quick Facts
            </h4>
            <div style='display: flex; flex-wrap: wrap; gap: 12px;'>
                {''.join(facts_cards)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def _render_black_box_warning(warning_text):
    """Render black box warning with prominent styling"""
    st.markdown(
        f"""
    <div class="black-box-warning" style='
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

