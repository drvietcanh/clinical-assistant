"""Drug Info - Detail View (display drug info in tabs)"""

import streamlit as st
import pandas as pd
import html
import re
import textwrap
from ..drug_database import DRUG_DATABASE
from drugs.references_config import get_drug_references
from components.references import render_references_section

# Helper function to safely escape HTML
def escape_html(text):
    """Escape HTML special characters"""
    if text is None:
        return ""
    return html.escape(str(text))

# Helper function to sanitize text that may contain HTML
def safe_render_html(text):
    """
    Convert possible HTML content into safe display text.

    - Nếu chỉ là text thường: escape HTML như bình thường.
    - Nếu chứa thẻ HTML (ví dụ các block <div style=...>): loại bỏ toàn bộ thẻ,
      chỉ giữ lại nội dung chữ, rồi escape để hiển thị sạch sẽ, không bị in code HTML.
    """
    if text is None:
        return ""
    text_str = str(text)
    # Nếu có dấu hiệu HTML tag, strip toàn bộ tag đi
    if "<" in text_str and ">" in text_str:
        text_str = re.sub(r"<[^>]+>", "", text_str)
    # Escape để đảm bảo an toàn
    return html.escape(text_str.strip())

# Check if drug is antibiotic
try:
    from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
except ImportError:
    ANTIBIOTICS_DATABASE = {}
from .card_components import _render_quick_facts_box, _render_black_box_warning

def display_drug_info(drug_name, drug_data, show_header=True):
    """Display detailed drug information in tab-based format (Epocrates style)
    
    Args:
        drug_name: Name of the drug
        drug_data: Dictionary containing drug information
        show_header: Whether to show the drug header (default: True, set False when used in dedicated page)
    """
    if show_header:
        st.markdown(
            f"""
        <div class="drug-detail-header" style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        '>
            <h2 style='margin: 0; color: white; font-size: 1.8em;'>💊 {drug_name}</h2>
            {f"<p style='margin: 8px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1em;'>{escape_html(str(drug_data.get('vietnamese_name', '')))}</p>" if drug_data.get('vietnamese_name') else ''}
        </div>
        """
            , unsafe_allow_html=True)
    # Enhanced tabs with better styling
    tab_names = ['📋 Overview', '💊 Dosing', '⚠️ Safety', '🔗 Interactions', '📊 Monitoring']
    (tab_overview, tab_dosing, tab_safety, tab_interactions, tab_monitoring) = st.tabs(tab_names)
    with tab_overview:
        if 'black_box_warnings' in drug_data:
            _render_black_box_warning(drug_data['black_box_warnings'])
        _render_quick_facts_box(drug_data)
        # Enhanced info cards layout
        info_cols = st.columns(3)
        with info_cols[0]:
            if 'vietnamese_name' in drug_data:
                st.markdown(
                    f"""
                    <div style='background: #f0f9ff; padding: 15px; border-radius: 8px; border-left: 4px solid #0EA5E9; margin-bottom: 10px;'>
                        <div style='color: #0369a1; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>📝 Tên biệt dược</div>
                        <div style='color: #0c4a6e; font-size: 1em;'>{escape_html(str(drug_data['vietnamese_name']))}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        with info_cols[1]:
            if 'group' in drug_data:
                st.markdown(
                    f"""
                    <div style='background: #fef3c7; padding: 15px; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 10px;'>
                        <div style='color: #92400e; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>🏷️ Nhóm</div>
                        <div style='color: #78350f; font-size: 1em;'>{escape_html(str(drug_data['group']))}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        with info_cols[2]:
            if 'administration' in drug_data:
                admin_icons = {'IV': '💉', 'IM': '💊', 'PO': '🍽️',
                    'Inhalation': '🌬️', 'SC': '💉', 'Rectal': '📦'}
                admin_display = ' / '.join([
                    f"{admin_icons.get(route, '')} {escape_html(str(route))}" for route in
                    drug_data['administration']])
                st.markdown(
                    f"""
                    <div style='background: #ecfdf5; padding: 15px; border-radius: 8px; border-left: 4px solid #10B981; margin-bottom: 10px;'>
                        <div style='color: #065f46; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>💊 Đường dùng</div>
                        <div style='color: #047857; font-size: 1em;'>{admin_display}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            if 'pregnancy' in drug_data:
                preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
                preg = drug_data['pregnancy']
                preg_desc = {'A': 'An toàn', 'B': 'Khá an toàn', 'C': 'Thận trọng', 'D': 'Nguy cơ', 'X': 'Chống chỉ định'}
                st.markdown(
                    f"""
                    <div style='background: #fce7f3; padding: 15px; border-radius: 8px; border-left: 4px solid #EC4899; margin-top: 10px;'>
                        <div style='color: #831843; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>🤰 Thai kỳ</div>
                        <div style='color: #9f1239; font-size: 1em;'>{preg_icons.get(preg, '')} {escape_html(str(preg))} - {escape_html(str(preg_desc.get(preg, '')))}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.markdown('---')
        if 'indications' in drug_data:
            st.markdown('### 📋 Chỉ định')
            indications_html = '<ul style="margin: 10px 0; padding-left: 20px;">'
            for ind in drug_data['indications']:
                indications_html += f'<li style="margin: 8px 0; color: #1e293b; font-size: 1em; line-height: 1.6;">{safe_render_html(ind)}</li>'
            indications_html += '</ul>'
            st.markdown(
                f"""
                <div style='background: #f8fafc; padding: 20px; border-radius: 10px; border-left: 4px solid #3B82F6; margin: 15px 0;'>
                    {indications_html}
                </div>
                """,
                unsafe_allow_html=True
            )
        if 'mechanism_of_action' in drug_data:
            st.markdown('---')
            st.markdown('### 🔬 Cơ chế tác động')
            st.markdown(
                f"""
                <div style='background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); padding: 20px; border-radius: 10px; border-left: 4px solid #0EA5E9; margin: 15px 0;'>
                    <p style='color: #0c4a6e; font-size: 1em; line-height: 1.8; margin: 0;'>{safe_render_html(drug_data['mechanism_of_action'])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        if 'pharmacokinetics' in drug_data:
            st.markdown('---')
            st.markdown('### 📈 Dược động học (Pharmacokinetics):')
            pk = drug_data['pharmacokinetics']
            pk_data = []
            if 'half_life' in pk:
                pk_data.append({'Thông số': 'Thời gian bán hủy', 'Giá trị':
                    pk['half_life']})
            if 'onset' in pk:
                pk_data.append({'Thông số': 'Thời gian bắt đầu tác dụng',
                    'Giá trị': pk['onset']})
            if 'duration' in pk:
                pk_data.append({'Thông số': 'Thời gian tác dụng', 'Giá trị':
                    pk['duration']})
            if 'protein_binding' in pk:
                pk_data.append({'Thông số': 'Gắn protein', 'Giá trị': pk[
                    'protein_binding']})
            if 'clearance' in pk:
                pk_data.append({'Thông số': 'Thanh thải', 'Giá trị': pk[
                    'clearance']})
            if pk_data:
                # Enhanced pharmacokinetics display with visual cards
                pk_df = pd.DataFrame(pk_data)
                st.markdown(
                    textwrap.dedent(
                        f"""
                        <div style='background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 10px; padding: 20px; margin: 15px 0;'>
                            <h4 style='color: #0c4a6e; margin: 0 0 15px 0; font-size: 1.1em;'>📈 Dược động học</h4>
                            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 12px;'>
                                {''.join([
                                    "<div style='background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #0EA5E9;'>"
                                    f"<div style='color: #0369a1; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>{safe_render_html(row['Thông số'])}</div>"
                                    f"<div style='color: #0c4a6e; font-size: 1em; font-weight: 500;'>{safe_render_html(row['Giá trị'])}</div>"
                                    "</div>"
                                    for _, row in pk_df.iterrows()
                                ])}
                            </div>
                        </div>
                        """
                    ),
                    unsafe_allow_html=True
                )
        if 'storage' in drug_data:
            st.markdown('---')
            st.markdown('### 📦 Bảo quản:')
            st.info(drug_data['storage'])
        
        # References section
        st.markdown('---')
        drug_group = drug_data.get('group', '')
        references = get_drug_references(drug_class=drug_group)
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
    with tab_dosing:
        if 'dosage' in drug_data:
            st.markdown('### 👤 Liều dùng người lớn:')
            dosage = drug_data['dosage']
            adult_doses = []
            if 'adult_htn' in dosage:
                adult_doses.append(f"**Tăng huyết áp:** {dosage['adult_htn']}")
            if 'adult_po' in dosage:
                adult_doses.append(f"**Uống (PO):** {dosage['adult_po']}")
            if 'adult_iv' in dosage:
                adult_doses.append(
                    f"**Tiêm tĩnh mạch (IV):** {dosage['adult_iv']}")
            if 'adult_standard' in dosage:
                adult_doses.append(
                    f"**Liều chuẩn:** {dosage['adult_standard']}")
            if 'adult_loading' in dosage:
                adult_doses.append(f"**Liều nạp:** {dosage['adult_loading']}")
            if 'adult_maintenance' in dosage:
                adult_doses.append(
                    f"**Liều duy trì:** {dosage['adult_maintenance']}")
            if adult_doses:
                # Enhanced dosing display with better visual design
                st.markdown(
                    f"""
                    <div style='background: #f0fdf4; border: 1px solid #86efac; border-radius: 10px; padding: 20px; margin: 15px 0;'>
                        <h4 style='color: #166534; margin: 0 0 15px 0; font-size: 1.1em;'>💊 Liều dùng người lớn</h4>
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px;'>
                            {''.join([f"""
                            <div style='background: white; padding: 12px 15px; border-radius: 8px; border-left: 3px solid #10B981;'>
                                <div style='color: #047857; font-size: 0.95em; line-height: 1.6;'>{escape_html(dose.replace('**', '').replace(':', ':</strong>').replace('**', '<strong>'))}</div>
                            </div>
                            """ for dose in adult_doses])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            if 'notes' in dosage:
                st.caption(f"💡 {dosage['notes']}")
        if 'dosage' in drug_data:
            # Enhanced pediatric dosing display
            ped_doses = []
            if 'pediatric' in drug_data['dosage']:
                ped_doses.append(('Tổng quát', drug_data['dosage']['pediatric']))
            if 'pediatric_6_14' in drug_data['dosage']:
                ped_doses.append(('6-14 tuổi', drug_data['dosage']['pediatric_6_14']))
            if 'pediatric_2_5' in drug_data['dosage']:
                ped_doses.append(('2-5 tuổi', drug_data['dosage']['pediatric_2_5']))
            if 'pediatric_under_2' in drug_data['dosage']:
                ped_doses.append(('< 2 tuổi', drug_data['dosage']['pediatric_under_2']))
            
            if ped_doses:
                st.markdown('---')
                st.markdown('### 👶 Liều dùng trẻ em')
                st.markdown(
                    f"""
                    <div style='background: #fef3c7; border: 1px solid #fcd34d; border-radius: 10px; padding: 20px; margin: 15px 0;'>
                        <h4 style='color: #92400e; margin: 0 0 15px 0; font-size: 1.1em;'>👶 Liều dùng theo độ tuổi</h4>
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px;'>
                            {''.join([f"""
                            <div style='background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #F59E0B;'>
                                <div style='font-weight: bold; color: #92400e; margin-bottom: 8px; font-size: 0.95em;'>{safe_render_html(age_group)}</div>
                                <div style='color: #78350f; font-size: 0.9em; line-height: 1.6;'>{safe_render_html(dose)}</div>
                            </div>
                            """ for age_group, dose in ped_doses])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        if 'renal_adjustment' in drug_data:
            st.markdown('---')
            st.markdown('### 🫘 Điều chỉnh theo chức năng thận:')
            renal = drug_data['renal_adjustment']
            renal_data = []
            if 'normal' in renal:
                renal_data.append({'CrCl (mL/min)': '≥ 60', 'Điều chỉnh':
                    renal['normal']})
            if '30_60' in renal:
                renal_data.append({'CrCl (mL/min)': '30-60', 'Điều chỉnh':
                    renal['30_60']})
            if '15_30' in renal:
                renal_data.append({'CrCl (mL/min)': '15-30', 'Điều chỉnh':
                    renal['15_30']})
            if 'under_30' in renal:
                renal_data.append({'CrCl (mL/min)': '< 30', 'Điều chỉnh':
                    renal['under_30']})
            if 'under_15' in renal:
                renal_data.append({'CrCl (mL/min)': '< 15', 'Điều chỉnh':
                    renal['under_15']})
            if 'hemodialysis' in renal:
                renal_data.append({'CrCl (mL/min)': 'Lọc máu', 'Điều chỉnh':
                    renal['hemodialysis']})
            if renal_data:
                # Enhanced renal adjustment display with visual cards
                st.markdown(
                    f"""
                    <div style='background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin: 15px 0;'>
                        <h4 style='color: #1e293b; margin: 0 0 15px 0; font-size: 1.1em;'>🫘 Điều chỉnh theo chức năng thận</h4>
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px;'>
                            {''.join([f"""
                            <div style='background: {'#d1fae5' if 'không' in str(row['Điều chỉnh']).lower() or 'normal' in str(row['Điều chỉnh']).lower() or 'không đổi' in str(row['Điều chỉnh']) else '#fef3c7' if 'giảm' in str(row['Điều chỉnh']).lower() or 'thận trọng' in str(row['Điều chỉnh']).lower() else '#fee2e2' if 'chống chỉ định' in str(row['Điều chỉnh']) or 'tránh' in str(row['Điều chỉnh']) else 'white'}; padding: 15px; border-radius: 8px; border-left: 4px solid {'#10B981' if 'không' in str(row['Điều chỉnh']).lower() or 'normal' in str(row['Điều chỉnh']).lower() or 'không đổi' in str(row['Điều chỉnh']) else '#F59E0B' if 'giảm' in str(row['Điều chỉnh']).lower() or 'thận trọng' in str(row['Điều chỉnh']).lower() else '#DC2626' if 'chống chỉ định' in str(row['Điều chỉnh']) or 'tránh' in str(row['Điều chỉnh']) else '#64748b'};'>
                                <div style='font-weight: bold; color: #1e293b; margin-bottom: 5px; font-size: 0.95em;'>{safe_render_html(row['CrCl (mL/min)'])}</div>
                                <div style='color: #475569; font-size: 0.9em; line-height: 1.5;'>{safe_render_html(row['Điều chỉnh'])}</div>
                            </div>
                            """ for row in renal_data])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        # Enhanced: Display hepatic adjustment if available (inspired by UpToDate)
        if 'hepatic_adjustment' in drug_data:
            st.markdown('---')
            st.markdown('### 🔶 Điều chỉnh theo chức năng gan:')
            hepatic = drug_data['hepatic_adjustment']
            hepatic_data = []
            
            # Handle different formats (dict or simple structure)
            if isinstance(hepatic, dict):
                if 'mild' in hepatic:
                    hepatic_data.append({'Mức độ': 'Suy gan nhẹ', 'Điều chỉnh': hepatic['mild']})
                if 'moderate' in hepatic:
                    hepatic_data.append({'Mức độ': 'Suy gan trung bình', 'Điều chỉnh': hepatic['moderate']})
                if 'severe' in hepatic:
                    hepatic_data.append({'Mức độ': 'Suy gan nặng', 'Điều chỉnh': hepatic['severe']})
                if 'cirrhosis' in hepatic:
                    hepatic_data.append({'Mức độ': 'Xơ gan', 'Điều chỉnh': hepatic['cirrhosis']})
            
            if hepatic_data:
                # Enhanced hepatic adjustment display with visual cards
                st.markdown(
                    f"""
                    <div style='background: #fefce8; border: 1px solid #fde047; border-radius: 10px; padding: 20px; margin: 15px 0;'>
                        <h4 style='color: #713f12; margin: 0 0 15px 0; font-size: 1.1em;'>🔶 Điều chỉnh theo chức năng gan</h4>
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px;'>
                            {''.join([f"""
                            <div style='background: {'#d1fae5' if 'không' in str(row['Điều chỉnh']).lower() or 'normal' in str(row['Điều chỉnh']).lower() or 'không đổi' in str(row['Điều chỉnh']) else '#fef3c7' if 'giảm' in str(row['Điều chỉnh']).lower() or 'thận trọng' in str(row['Điều chỉnh']).lower() else '#fee2e2' if 'chống chỉ định' in str(row['Điều chỉnh']) or 'tránh' in str(row['Điều chỉnh']) or 'không dùng' in str(row['Điều chỉnh']).lower() else 'white'}; padding: 15px; border-radius: 8px; border-left: 4px solid {'#10B981' if 'không' in str(row['Điều chỉnh']).lower() or 'normal' in str(row['Điều chỉnh']).lower() or 'không đổi' in str(row['Điều chỉnh']) else '#F59E0B' if 'giảm' in str(row['Điều chỉnh']).lower() or 'thận trọng' in str(row['Điều chỉnh']).lower() else '#DC2626' if 'chống chỉ định' in str(row['Điều chỉnh']) or 'tránh' in str(row['Điều chỉnh']) or 'không dùng' in str(row['Điều chỉnh']).lower() else '#F59E0B'};'>
                                <div style='font-weight: bold; color: #1e293b; margin-bottom: 5px; font-size: 0.95em;'>{safe_render_html(row['Mức độ'])}</div>
                                <div style='color: #475569; font-size: 0.9em; line-height: 1.5;'>{safe_render_html(row['Điều chỉnh'])}</div>
                            </div>
                            """ for row in hepatic_data])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        is_antibiotic = drug_name in ANTIBIOTICS_DATABASE
        if is_antibiotic:
            st.markdown('---')
            st.markdown('### 🧮 Tính liều theo CrCl/eGFR')
            
            # Enhanced dosing calculator section with comprehensive features (inspired by Epocrates)
            st.markdown(
                f"""
                <div style='background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 1px solid #86efac; border-radius: 10px; padding: 25px; margin: 15px 0;'>
                    <div style='display: flex; align-items: start; gap: 20px; flex-wrap: wrap;'>
                        <div style='flex: 1; min-width: 250px;'>
                            <h4 style='color: #166534; margin: 0 0 15px 0; font-size: 1.2em;'>💡 Tính liều tự động cho {drug_name}</h4>
                            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 15px;'>
                                <div style='background: white; padding: 12px; border-radius: 8px; border-left: 3px solid #10B981;'>
                                    <div style='color: #065f46; font-size: 0.85em; font-weight: bold; margin-bottom: 4px;'>🫘 Chức năng thận</div>
                                    <div style='color: #047857; font-size: 0.9em;'>CrCl/eGFR adjustments</div>
                                </div>
                                <div style='background: white; padding: 12px; border-radius: 8px; border-left: 3px solid #10B981;'>
                                    <div style='color: #065f46; font-size: 0.85em; font-weight: bold; margin-bottom: 4px;'>⚖️ Béo phì</div>
                                    <div style='color: #047857; font-size: 0.9em;'>ABW/IBW calculations</div>
                                </div>
                                <div style='background: white; padding: 12px; border-radius: 8px; border-left: 3px solid #10B981;'>
                                    <div style='color: #065f46; font-size: 0.85em; font-weight: bold; margin-bottom: 4px;'>👶 Trẻ em</div>
                                    <div style='color: #047857; font-size: 0.9em;'>Pediatric dosing</div>
                                </div>
                                <div style='background: white; padding: 12px; border-radius: 8px; border-left: 3px solid #10B981;'>
                                    <div style='color: #065f46; font-size: 0.85em; font-weight: bold; margin-bottom: 4px;'>💉 HD/PD</div>
                                    <div style='color: #047857; font-size: 0.9em;'>Dialysis support</div>
                                </div>
                            </div>
                            <ul style='color: #047857; margin: 0; padding-left: 20px; line-height: 1.8; font-size: 0.95em;'>
                                <li>Tính liều chi tiết dựa trên nhiều thông số</li>
                                <li>Cảnh báo tự động và hướng dẫn lâm sàng</li>
                                <li>Hỗ trợ nhiều chỉ định và phác đồ</li>
                                <li>Tích hợp với calculator chuyên dụng</li>
                            </ul>
                        </div>
                        <div style='min-width: 150px;'>
                            <div style='background: white; padding: 20px; border-radius: 8px; border: 2px solid #10B981; text-align: center; box-shadow: 0 2px 4px rgba(16,185,129,0.2);'>
                                <div style='font-size: 2.5em; margin-bottom: 8px;'>🧮</div>
                                <div style='color: #166534; font-weight: bold; font-size: 0.95em;'>Calculator</div>
                                <div style='color: #047857; font-size: 0.8em; margin-top: 4px;'>Advanced</div>
                            </div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            safe_calc_key = (
                f"calc_dose_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                )
            if st.button('🧮 Mở Calculator Tính Liều', key=safe_calc_key,
                use_container_width=True, type='primary'):
                st.session_state['preset_antibiotic_name'] = drug_name
                st.session_state['switch_to_dosing_calculator'] = True
                st.rerun()
            st.caption(
                '💡 Click nút trên để mở calculator với thuốc này đã được chọn sẵn'
                )
    with tab_safety:
        if 'contraindications' in drug_data:
            st.markdown('### ⛔ Chống chỉ định')
            contraindications = drug_data['contraindications']
            if isinstance(contraindications, dict):
                # Enhanced contraindications display
                if 'tuyệt_đối' in contraindications and contraindications['tuyệt_đối']:
                    st.markdown(
                        f"""
                        <div style='background: #fee2e2; border-left: 4px solid #DC2626; padding: 20px; border-radius: 10px; margin: 15px 0;'>
                            <h4 style='color: #991b1b; margin: 0 0 15px 0; font-size: 1.1em; font-weight: bold;'>🔴 Tuyệt đối</h4>
                            <ul style='margin: 0; padding-left: 20px; color: #7f1d1d;'>
                                {''.join([f'<li style="margin: 8px 0; font-weight: 500; line-height: 1.6;">{safe_render_html(contra)}</li>' for contra in contraindications['tuyệt_đối']])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                if 'tương_đối' in contraindications and contraindications['tương_đối']:
                    st.markdown(
                        f"""
                        <div style='background: #fef3c7; border-left: 4px solid #F59E0B; padding: 20px; border-radius: 10px; margin: 15px 0;'>
                            <h4 style='color: #92400e; margin: 0 0 15px 0; font-size: 1.1em; font-weight: bold;'>🟡 Tương đối - Thận trọng</h4>
                            <ul style='margin: 0; padding-left: 20px; color: #78350f;'>
                                {''.join([f'<li style="margin: 8px 0; line-height: 1.6;">{safe_render_html(contra)}</li>' for contra in contraindications['tương_đối']])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                # Fallback for simple list
                st.markdown(
                    f"""
                    <div style='background: #f1f5f9; border-left: 4px solid #64748b; padding: 20px; border-radius: 10px; margin: 15px 0;'>
                        <ul style='margin: 0; padding-left: 20px; color: #475569;'>
                            {''.join([f'<li style="margin: 8px 0; line-height: 1.6;">{safe_render_html(contra)}</li>' for contra in contraindications])}
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        if 'side_effects' in drug_data:
            st.markdown('---')
            st.markdown('### ⚠️ Tác dụng phụ')
            
            # Enhanced side effects display with frequency data (inspired by Drugs.com & Epocrates)
            side_effects = drug_data['side_effects']
            
            # Check if side_effects is structured data with frequency
            if isinstance(side_effects, dict):
                # Structured format: {'common': [...], 'uncommon': [...], 'rare': [...], 'serious': [...]}
                common_effects = side_effects.get('common', [])
                uncommon_effects = side_effects.get('uncommon', [])
                rare_effects = side_effects.get('rare', [])
                serious_effects = side_effects.get('serious', [])
                
                # Display with frequency labels
                if common_effects:
                    st.markdown(
                        f"""
                        <div style='background: #fef3c7; border-left: 4px solid #F59E0B; padding: 15px; border-radius: 8px; margin: 10px 0;'>
                            <div style='color: #92400e; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>🟡</span>
                                Phổ biến (≥1%)
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #78350f;'>
                                {''.join([f'<li style="margin: 5px 0; line-height: 1.6;">{safe_render_html(se)}</li>' for se in common_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if uncommon_effects:
                    st.markdown(
                        f"""
                        <div style='background: #fef3c7; border-left: 4px solid #F59E0B; padding: 15px; border-radius: 8px; margin: 10px 0; opacity: 0.8;'>
                            <div style='color: #92400e; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>🟠</span>
                                Ít gặp (0.1-1%)
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #78350f;'>
                                {''.join([f'<li style="margin: 5px 0; line-height: 1.6;">{safe_render_html(se)}</li>' for se in uncommon_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if rare_effects:
                    st.markdown(
                        f"""
                        <div style='background: #f1f5f9; border-left: 4px solid #64748b; padding: 15px; border-radius: 8px; margin: 10px 0;'>
                            <div style='color: #475569; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>⚪</span>
                                Hiếm gặp (&lt;0.1%)
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #334155;'>
                                {''.join([f'<li style="margin: 5px 0; line-height: 1.6;">{safe_render_html(se)}</li>' for se in rare_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if serious_effects:
                    st.markdown(
                        f"""
                        <div style='background: #fee2e2; border-left: 4px solid #DC2626; padding: 15px; border-radius: 8px; margin: 10px 0;'>
                            <div style='color: #991b1b; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>🔴</span>
                                Nghiêm trọng - Cần báo bác sĩ ngay
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #7f1d1d;'>
                                {''.join([f'<li style="margin: 5px 0; font-weight: 500; line-height: 1.6;">{safe_render_html(se)}</li>' for se in serious_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            
            elif isinstance(side_effects, list) and len(side_effects) > 0:
                # Legacy format: simple list - use heuristics to categorize
                # Keywords for serious side effects
                serious_keywords = ['tử vong', 'nguy hiểm', 'nghiêm trọng', 'suy gan', 'suy thận', 
                                  'phản ứng dị ứng nặng', 'sốc phản vệ', 'xuất huyết', 'chảy máu nặng',
                                  'rối loạn nhịp tim', 'nhồi máu', 'đột quỵ', 'huyết khối', 'sốc',
                                  'phù mạch', 'hội chứng stevens-johnson', 'hoại tử biểu bì']
                
                # Keywords for uncommon effects (longer descriptions, specific conditions)
                uncommon_keywords = ['hiếm', 'ít gặp', 'rất hiếm', 'đôi khi', 'thỉnh thoảng']
                
                # Separate into categories
                common_effects = []
                uncommon_effects = []
                serious_effects = []
                other_effects = []
                
                for se in side_effects:
                    se_lower = se.lower()
                    if any(keyword in se_lower for keyword in serious_keywords):
                        serious_effects.append(se)
                    elif any(keyword in se_lower for keyword in uncommon_keywords) or len(se) > 60:
                        uncommon_effects.append(se)
                    elif len(se) < 50:  # Shorter descriptions often indicate common effects
                        common_effects.append(se)
                    else:
                        other_effects.append(se)
                
                # If no categorization worked, show all as common
                if not common_effects and not serious_effects and not uncommon_effects:
                    common_effects = side_effects
                
                # Display categorized with frequency estimates
                if common_effects:
                    st.markdown(
                        f"""
                        <div style='background: #fef3c7; border-left: 4px solid #F59E0B; padding: 15px; border-radius: 8px; margin: 10px 0;'>
                            <div style='color: #92400e; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>🟡</span>
                                Phổ biến (≥1%)
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #78350f;'>
                                {''.join([f'<li style="margin: 5px 0; line-height: 1.6;">{safe_render_html(se)}</li>' for se in common_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if uncommon_effects:
                    st.markdown(
                        f"""
                        <div style='background: #fef3c7; border-left: 4px solid #F59E0B; padding: 15px; border-radius: 8px; margin: 10px 0; opacity: 0.8;'>
                            <div style='color: #92400e; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>🟠</span>
                                Ít gặp (0.1-1%)
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #78350f;'>
                                {''.join([f'<li style="margin: 5px 0; line-height: 1.6;">{safe_render_html(se)}</li>' for se in uncommon_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if serious_effects:
                    st.markdown(
                        f"""
                        <div style='background: #fee2e2; border-left: 4px solid #DC2626; padding: 15px; border-radius: 8px; margin: 10px 0;'>
                            <div style='color: #991b1b; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>🔴</span>
                                Nghiêm trọng - Cần báo bác sĩ ngay
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #7f1d1d;'>
                                {''.join([f'<li style="margin: 5px 0; font-weight: 500; line-height: 1.6;">{safe_render_html(se)}</li>' for se in serious_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if other_effects and (common_effects or serious_effects or uncommon_effects):
                    st.markdown(
                        f"""
                        <div style='background: #f1f5f9; border-left: 4px solid #64748b; padding: 15px; border-radius: 8px; margin: 10px 0;'>
                            <div style='color: #475569; font-weight: bold; margin-bottom: 8px; font-size: 1em; display: flex; align-items: center;'>
                                <span style='font-size: 1.2em; margin-right: 8px;'>⚪</span>
                                Khác
                            </div>
                            <ul style='margin: 0; padding-left: 20px; color: #334155;'>
                                {''.join([f'<li style="margin: 5px 0; line-height: 1.6;">{se}</li>' for se in other_effects])}
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                # Fallback for non-list or empty
                st.info(str(side_effects) if side_effects else "Không có thông tin về tác dụng phụ")
        if 'precautions' in drug_data:
            st.markdown('---')
            st.markdown('### ⚠️ Thận trọng')
            precautions = drug_data['precautions']
            if isinstance(precautions, list) and len(precautions) > 0:
                st.markdown(
                    f"""
                    <div style='background: #fffbeb; border-left: 4px solid #F59E0B; padding: 20px; border-radius: 10px; margin: 15px 0;'>
                        <ul style='margin: 0; padding-left: 20px; color: #78350f;'>
                            {''.join([f'<li style="margin: 10px 0; line-height: 1.7; font-size: 0.95em;">{safe_render_html(prec)}</li>' for prec in precautions])}
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.info(str(precautions) if precautions else "Không có thông tin về thận trọng")
        if 'pregnancy' in drug_data:
            st.markdown('---')
            preg = drug_data['pregnancy']
            preg_descriptions = {'A':
                'An toàn - Nghiên cứu không thấy nguy cơ', 'B':
                'An toàn - Nghiên cứu động vật không thấy nguy cơ', 'C':
                'Thận trọng - Nguy cơ không thể loại trừ', 'D':
                'Nguy cơ - Có bằng chứng nguy cơ, cân nhắc lợi ích', 'X':
                'Chống chỉ định - Nguy cơ vượt quá lợi ích'}
            desc = preg_descriptions.get(preg, '')
            preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
            st.markdown(
                f"### 🤰 **An toàn thai kỳ:** {preg_icons.get(preg, '')} {preg} - {desc}"
                )
        if 'lactation' in drug_data:
            st.markdown('---')
            st.markdown(
                f"### 🤱 **An toàn cho con bú:** {escape_html(str(drug_data['lactation']))}")
    with tab_interactions:
        if 'interactions' in drug_data:
            st.markdown('### 🔗 Tương tác thuốc:')
            for inter in drug_data['interactions']:
                st.markdown(f'- {inter}')
        else:
            st.info(
                "Không có thông tin về tương tác thuốc. Sử dụng công cụ 'Kiểm tra Tương tác Thuốc' để kiểm tra chi tiết."
                )
    with tab_monitoring:
        if 'monitoring' in drug_data:
            st.markdown('### 📊 Theo dõi (Monitoring)')
            monitoring_list = drug_data['monitoring']
            if isinstance(monitoring_list, list) and len(monitoring_list) > 0:
                # Enhanced monitoring display with categorized items
                st.markdown(
                    f"""
                    <div style='background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px; margin: 15px 0;'>
                        <h4 style='color: #1e293b; margin: 0 0 15px 0; font-size: 1.1em;'>📊 Các thông số cần theo dõi</h4>
                        <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px;'>
                            {''.join([f"""
                            <div style='background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #8B5CF6;'>
                                <div style='color: #1e293b; font-size: 0.95em; line-height: 1.6; display: flex; align-items: start;'>
                                    <span style='font-size: 1.2em; margin-right: 8px; color: #8B5CF6;'>✅</span>
                                    <span>{safe_render_html(mon)}</span>
                                </div>
                            </div>
                            """ for mon in monitoring_list])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.info(str(monitoring_list) if monitoring_list else "Không có thông tin về monitoring")
        try:
            from drugs.drug_utils.tdm_mapping import get_tdm_info, has_tdm
            if has_tdm(drug_name):
                st.markdown('---')
                st.markdown('### 📊 Theo dõi Nồng Độ Thuốc (TDM)')
                tdm_info = get_tdm_info(drug_name)
                col1, col2 = st.columns([2, 1])
                with col1:
                    therapeutic_range = tdm_info.get('therapeutic_range', 'N/A'
                        )
                    sampling_time = tdm_info.get('sampling_time', 'N/A')
                    half_life = tdm_info.get('half_life_hours', 'N/A')
                    unit = tdm_info.get('unit', 'N/A')
                    half_life_display = f'{half_life} giờ' if isinstance(
                        half_life, (int, float)) else str(half_life)
                    st.info(
                        f"""
                    **🎯 Khoảng điều trị:** {therapeutic_range}
                    
                    **⏰ Thời điểm lấy mẫu:** {sampling_time}
                    
                    **⏱️ Half-life:** {half_life_display}
                    
                    **📏 Đơn vị:** {unit}
                    """
                        )
                with col2:
                    safe_tdm_key = (
                        f"tdm_calc_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '')}"
                        )
                    if st.button('📊 Mở TDM Calculator', key=safe_tdm_key,
                        use_container_width=True, type='primary'):
                        st.session_state['preset_tdm_drug'] = drug_name
                        st.session_state['switch_to_tdm'] = True
                        st.rerun()
                st.caption(
                    '💡 Click nút trên để mở TDM calculator với thuốc này đã được chọn sẵn'
                    )
        except ImportError:
            pass
        except Exception as e:
            pass

