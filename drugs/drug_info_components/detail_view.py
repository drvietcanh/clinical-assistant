"""Drug Info - Detail View (display drug info in tabs)"""

import streamlit as st
import pandas as pd
from ..drug_database import DRUG_DATABASE
from drugs.references_config import get_drug_references
from components.references import render_references_section

# Check if drug is antibiotic
try:
    from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
except ImportError:
    ANTIBIOTICS_DATABASE = {}
from .card_components import _render_quick_facts_box, _render_black_box_warning

def display_drug_info(drug_name, drug_data):
    """Display detailed drug information in tab-based format (Epocrates style)"""
    st.markdown(
        f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    '>
        <h2 style='margin: 0; color: white; font-size: 1.8em;'>💊 {drug_name}</h2>
        {f"<p style='margin: 8px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1em;'>{drug_data.get('vietnamese_name', '')}</p>" if drug_data.get('vietnamese_name') else ''}
    </div>
    """
        , unsafe_allow_html=True)
    (tab_overview, tab_dosing, tab_safety, tab_interactions, tab_monitoring
        ) = (st.tabs(['📋 Overview', '💊 Dosing', '⚠️ Safety',
        '🔗 Interactions', '📊 Monitoring']))
    with tab_overview:
        if 'black_box_warnings' in drug_data:
            _render_black_box_warning(drug_data['black_box_warnings'])
        _render_quick_facts_box(drug_data)
        col1, col2 = st.columns([2, 1])
        with col1:
            if 'vietnamese_name' in drug_data:
                st.markdown(
                    f"**📝 Tên biệt dược:** {drug_data['vietnamese_name']}")
            if 'group' in drug_data:
                st.markdown(f"**🏷️ Nhóm:** {drug_data['group']}")
        with col2:
            if 'administration' in drug_data:
                admin_icons = {'IV': '💉', 'IM': '💊', 'PO': '🍽️',
                    'Inhalation': '🌬️', 'SC': '💉', 'Rectal': '📦'}
                admin_display = ' / '.join([
                    f"{admin_icons.get(route, '')} {route}" for route in
                    drug_data['administration']])
                st.markdown(f'**💊 Đường dùng:** {admin_display}')
            if 'pregnancy' in drug_data:
                preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
                preg = drug_data['pregnancy']
                st.markdown(f"**🤰 Thai kỳ:** {preg_icons.get(preg, '')} {preg}"
                    )
        st.markdown('---')
        if 'indications' in drug_data:
            st.markdown('### 📋 Chỉ định:')
            for ind in drug_data['indications']:
                st.markdown(f'- {ind}')
        if 'mechanism_of_action' in drug_data:
            st.markdown('---')
            st.markdown('### 🔬 Cơ chế tác động:')
            st.info(drug_data['mechanism_of_action'])
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
                st.dataframe(pd.DataFrame(pk_data), use_container_width=
                    True, hide_index=True)
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
                col1, col2 = st.columns(2)
                mid = len(adult_doses) // 2 + len(adult_doses) % 2
                for i, dose in enumerate(adult_doses[:mid]):
                    with col1:
                        st.info(dose)
                for i, dose in enumerate(adult_doses[mid:], start=mid):
                    with col2:
                        st.info(dose)
            if 'notes' in dosage:
                st.caption(f"💡 {dosage['notes']}")
        if 'dosage' in drug_data and 'pediatric' in drug_data['dosage']:
            st.markdown('---')
            st.markdown('### 👶 Liều dùng trẻ em:')
            ped_dose = drug_data['dosage']['pediatric']
            st.info(ped_dose)
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
                st.dataframe(pd.DataFrame(renal_data), use_container_width=
                    True, hide_index=True)
        is_antibiotic = drug_name in ANTIBIOTICS_DATABASE
        if is_antibiotic:
            st.markdown('---')
            st.markdown('### 🧮 Tính liều theo CrCl/eGFR')
            col1, col2 = st.columns([2, 1])
            with col1:
                st.info(
                    f"""
                **💡 Tính liều tự động cho {drug_name}:**
                - Dựa trên chức năng thận (CrCl/eGFR)
                - Hỗ trợ HD, PD, béo phì, trẻ em
                - Tính liều chi tiết và cảnh báo tự động
                """
                    )
            with col2:
                safe_calc_key = (
                    f"calc_dose_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                    )
                if st.button('🧮 Tính liều theo CrCl', key=safe_calc_key,
                    use_container_width=True, type='primary'):
                    st.session_state['preset_antibiotic_name'] = drug_name
                    st.session_state['switch_to_dosing_calculator'] = True
                    st.rerun()
            st.caption(
                '💡 Click nút trên để mở calculator với thuốc này đã được chọn sẵn'
                )
    with tab_safety:
        if 'contraindications' in drug_data:
            st.markdown('### ⛔ Chống chỉ định:')
            contraindications = drug_data['contraindications']
            if isinstance(contraindications, dict):
                if 'tuyệt_đối' in contraindications and contraindications[
                    'tuyệt_đối']:
                    st.markdown('**🔴 Tuyệt đối:**')
                    for contra in contraindications['tuyệt_đối']:
                        st.markdown(f'- {contra}')
                if 'tương_đối' in contraindications and contraindications[
                    'tương_đối']:
                    st.markdown('**🟡 Tương đối:**')
                    for contra in contraindications['tương_đối']:
                        st.markdown(f'- {contra}')
            else:
                for contra in contraindications:
                    st.markdown(f'- {contra}')
        if 'side_effects' in drug_data:
            st.markdown('---')
            st.markdown('### ⚠️ Tác dụng phụ:')
            for se in drug_data['side_effects']:
                st.markdown(f'- {se}')
        if 'precautions' in drug_data:
            st.markdown('---')
            st.markdown('### ⚠️ Thận trọng:')
            for prec in drug_data['precautions']:
                st.markdown(f'- {prec}')
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
                f"### 🤱 **An toàn cho con bú:** {drug_data['lactation']}")
    with tab_interactions:
        if 'interactions' in drug_data:
            st.markdown('### 🔗 Tương tác thuốc:')
            for inter in drug_data['interactions']:
                st.markdown(f'- {inter}')
        else:
            st.info(
                "Không có thông tin về tương tác thuốc. Sử dụng công cụ 'Kiểm Tra Tương tác Thuốc' để kiểm tra chi tiết."
                )
    with tab_monitoring:
        if 'monitoring' in drug_data:
            st.markdown('### 📊 Theo dõi (Monitoring):')
            monitoring_list = drug_data['monitoring']
            if isinstance(monitoring_list, list):
                for mon in monitoring_list:
                    st.markdown(f'- ✅ {mon}')
            else:
                st.info(monitoring_list)
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

