"""
Drug Interaction Checker
Tool to check for drug-drug interactions
"""

import streamlit as st
from .interactions_data import (
    check_interactions,
    normalize_drug_name,
    get_drug_autocomplete_suggestions,
    get_drug_classes,
    SEVERITY_MAJOR,
    SEVERITY_MODERATE,
    SEVERITY_MINOR,
    DRUG_ALIASES
)
from .interactions_food_alcohol import (
    check_food_interactions,
    check_alcohol_interactions
)
from components.ui.alerts import render_error_alert, render_warning_alert, render_info_alert
from components.ui.results import render_result_card
from components.drug_interaction_matrix import (
    render_interaction_matrix,
    render_interaction_summary
)


def render_interaction_checker():
    """Render drug interaction checker interface"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>🔍 Kiểm tra Tương tác Thuốc</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Phát hiện tương tác thuốc-thuốc với mức độ nghiêm trọng và khuyến nghị xử trí • An toàn cho bệnh nhân
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Tính năng mới (Week 2 Enhancements):**
    - 📊 Ma trận tương tác trực quan với color-coding
    - ⚕️ Ý nghĩa lâm sàng chi tiết
    - 💡 Gợi ý thuốc thay thế
    - 📋 Hướng dẫn xử trí cụ thể
    - 🔍 **Tìm kiếm thông minh với autocomplete** - Tự động gợi ý khi gõ
    - 🎯 **Class-based interactions** - Tự động nhận diện tương tác theo nhóm thuốc (ví dụ: "ACE Inhibitor" + "Spironolactone")
    - 🔤 **Fuzzy matching cải thiện** - Tìm thuốc ngay cả khi gõ sai chính tả, thiếu chữ, hoặc dùng tên khác
    - 📈 **Database mở rộng** - 514+ tương tác (Anticoagulants 52+, Antibiotics 107+, Cardiovascular 81+)
    
    ⚠️ **Lưu ý:** Database hiện tại bao gồm **514+ tương tác** phổ biến. Luôn tham khảo nguồn đáng tin cậy trước khi quyết định lâm sàng.
    """)
    
    st.markdown("---")
    
    # Quick examples
    st.markdown("### 💡 Ví dụ nhanh:")
    col_ex1, col_ex2, col_ex3 = st.columns(3)
    
    # Check if we need to update widget states from button clicks
    # Use separate keys to avoid StreamlitAPIException when setting widget state
    if 'interactions_set_input_method' in st.session_state:
        st.session_state['input_method'] = st.session_state['interactions_set_input_method']
        del st.session_state['interactions_set_input_method']
    if 'interactions_set_num_drugs' in st.session_state:
        st.session_state['num_drugs'] = st.session_state['interactions_set_num_drugs']
        del st.session_state['interactions_set_num_drugs']
    if 'interactions_set_drugs' in st.session_state:
        for key, value in st.session_state['interactions_set_drugs'].items():
            st.session_state[key] = value
        del st.session_state['interactions_set_drugs']
    
    with col_ex1:
        if st.button("🔍 Warfarin + Aspirin", use_container_width=True, key="example_warf_asp"):
            st.session_state['interactions_set_input_method'] = "Nhập từng thuốc"
            st.session_state['interactions_set_num_drugs'] = 2
            st.session_state['interactions_set_drugs'] = {'drug_0': "Warfarin", 'drug_1': "Aspirin"}
            st.rerun()
    
    with col_ex2:
        if st.button("🔍 Metformin + Furosemide", use_container_width=True, key="example_met_furo"):
            st.session_state['interactions_set_input_method'] = "Nhập từng thuốc"
            st.session_state['interactions_set_num_drugs'] = 2
            st.session_state['interactions_set_drugs'] = {'drug_0': "Metformin", 'drug_1': "Furosemide"}
            st.rerun()
    
    with col_ex3:
        if st.button("🔍 Omeprazole + Warfarin", use_container_width=True, key="example_omep_warf"):
            st.session_state['interactions_set_input_method'] = "Nhập từng thuốc"
            st.session_state['interactions_set_num_drugs'] = 2
            st.session_state['interactions_set_drugs'] = {'drug_0': "Omeprazole", 'drug_1': "Warfarin"}
            st.rerun()
    
    st.markdown("---")
    
    # Drug input section
    st.markdown("### 💊 Nhập Danh Sách Thuốc")
    
    # Input method selection
    input_method = st.radio(
        "Cách nhập:",
        ["Nhập từng thuốc", "Nhập danh sách (mỗi dòng một thuốc)"],
        horizontal=True,
        key="input_method"
    )
    
    drug_list = []
    
    if input_method == "Nhập từng thuốc":
        # Individual drug input
        num_drugs = st.number_input(
            "Số lượng thuốc:",
            min_value=1,
            max_value=20,
            value=3,
            step=1,
            key="num_drugs"
        )
        
        for i in range(num_drugs):
            # Get autocomplete suggestions
            drug_input_key = f"drug_{i}"
            current_value = st.session_state.get(drug_input_key, "")
            
            # Check if we need to update this drug input from button click
            if f'interactions_set_{drug_input_key}' in st.session_state:
                st.session_state[drug_input_key] = st.session_state[f'interactions_set_{drug_input_key}']
                del st.session_state[f'interactions_set_{drug_input_key}']
            
            # Show autocomplete suggestions
            if current_value and len(current_value) >= 1:
                suggestions = get_drug_autocomplete_suggestions(current_value, max_results=5)
                if suggestions:
                    with st.expander(f"💡 Gợi ý cho '{current_value}'", expanded=False):
                        for sug in suggestions:
                            if st.button(f"✓ {sug}", key=f"sug_{i}_{sug}", use_container_width=True):
                                st.session_state[f'interactions_set_{drug_input_key}'] = sug
                                st.rerun()
            
            drug = st.text_input(
                f"Thuốc {i+1}:",
                key=drug_input_key,
                placeholder="Ví dụ: Warfarin, Aspirin, Metformin...",
                help="Nhập tên thuốc (tiếng Anh hoặc tiếng Việt). Hệ thống sẽ tự động gợi ý."
            )
            if drug and drug.strip():
                drug_list.append(drug.strip())
    else:
        # Bulk input
        drug_text = st.text_area(
            "Nhập danh sách thuốc (mỗi dòng một thuốc):",
            height=150,
            placeholder="Warfarin\nAspirin\nMetformin\nOmeprazole",
            key="drug_list_text"
        )
        
        if drug_text:
            drug_list = [d.strip() for d in drug_text.split('\n') if d.strip()]
    
    # Show instructions if no drugs entered yet
    if len(drug_list) < 2:
        st.info("""
        **📝 Hướng dẫn sử dụng:**
        1. Chọn cách nhập: từng thuốc hoặc danh sách
        2. Nhập tên thuốc (tiếng Anh hoặc tiếng Việt)
        3. Hệ thống sẽ tự động gợi ý khi bạn nhập
        4. Nhấn nút "Kiểm tra tương tác" để xem kết quả
        
        **💡 Mẹo:**
        - Có thể nhập tên thuốc bằng tiếng Anh hoặc tiếng Việt
        - Hệ thống tự động nhận diện thuốc ngay cả khi gõ sai chính tả
        - Hỗ trợ class-based matching (ví dụ: nhập "SSRI" sẽ tự động kiểm tra tất cả SSRIs)
        """)
        st.markdown("---")
    
    # Check button
    if st.button("🔍 Kiểm tra Tương tác", type="primary", use_container_width=True):
        if len(drug_list) < 2:
            render_error_alert(
                "Vui lòng nhập ít nhất 2 thuốc để kiểm tra tương tác",
                title="Thiếu thông tin"
            )
        else:
            # Normalize drug names with fuzzy matching
            normalized_list = [normalize_drug_name(drug, use_fuzzy=True) for drug in drug_list]
            
            # Store mapping of original -> normalized for display
            drug_mapping = {}
            for orig, norm in zip(drug_list, normalized_list):
                if orig != norm:
                    drug_mapping[orig] = norm
            
            # Store in session state for display
            st.session_state['checked_drugs'] = normalized_list
            st.session_state['original_drugs'] = drug_list
            st.session_state['drug_mapping'] = drug_mapping
            
            # Check interactions
            interactions = check_interactions(normalized_list)
            st.session_state['interactions'] = interactions
            
            # Rerun to show results
            st.rerun()
    
    # Display results
    if 'interactions' in st.session_state and st.session_state['interactions']:
        st.markdown("---")
        st.markdown("### 📋 Kết quả Kiểm tra")
        
        interactions = st.session_state['interactions']
        checked_drugs = st.session_state.get('checked_drugs', [])
        original_drugs = st.session_state.get('original_drugs', [])
        drug_mapping = st.session_state.get('drug_mapping', {})
        
        # Summary with visual metrics
        render_interaction_summary(interactions)
        
        # CDS Alerts Panel
        try:
            from components.cds_alerts import (
                check_drug_interactions as cds_check_interactions,
                render_cds_alerts_panel
            )
            
            # Generate CDS alerts from interactions
            cds_alerts = []
            for interaction in interactions:
                if interaction.get('severity') == SEVERITY_MAJOR:
                    cds_alerts.append({
                        'type': 'interaction',
                        'severity': 'critical',
                        'title': f"Tương tác nghiêm trọng: {interaction.get('drug1')} + {interaction.get('drug2')}",
                        'message': interaction.get('description', ''),
                        'recommendation': interaction.get('management', ''),
                        'drugs': [interaction.get('drug1'), interaction.get('drug2')]
                    })
                elif interaction.get('severity') == SEVERITY_MODERATE:
                    cds_alerts.append({
                        'type': 'interaction',
                        'severity': 'warning',
                        'title': f"Tương tác vừa: {interaction.get('drug1')} + {interaction.get('drug2')}",
                        'message': interaction.get('description', ''),
                        'recommendation': interaction.get('management', ''),
                        'drugs': [interaction.get('drug1'), interaction.get('drug2')]
                    })
            
            if cds_alerts:
                st.markdown("---")
                st.markdown("### 🚨 CDS Alerts")
                render_cds_alerts_panel(cds_alerts)
        except ImportError:
            pass
        
        # Show checked drugs with normalization info
        st.markdown("**📋 Danh sách thuốc đã kiểm tra:**")
        drugs_display_parts = []
        for orig, norm in zip(original_drugs, checked_drugs):
            if orig != norm:
                drugs_display_parts.append(f"**{orig}** → *{norm}*")
            else:
                drugs_display_parts.append(f"**{norm}**")
        drugs_display = ", ".join(drugs_display_parts)
        st.info(drugs_display)
        
        # Show drug classes if available
        if checked_drugs:
            with st.expander("ℹ️ Thông tin nhóm thuốc (Drug Classes)"):
                for drug in checked_drugs:
                    classes = get_drug_classes(drug)
                    if classes:
                        st.caption(f"**{drug}**: {', '.join(classes)}")
                    else:
                        st.caption(f"**{drug}**: Không xác định được nhóm")
        
        # Display interactions
        if interactions:
            st.markdown("---")
            st.markdown("### ⚠️ Phát hiện Tương tác")
            
            # Visual Interaction Matrix
            st.markdown("#### 📊 Ma Trận Tương tác Trực Quan")
            render_interaction_matrix(
                drugs=checked_drugs,
                interactions=interactions,
                show_tooltips=True,
                compact=False
            )
            
            st.markdown("---")
            st.markdown("#### 📋 Chi tiết Tương tác")
            
            # Filter options
            col1, col2 = st.columns([2, 1])
            with col1:
                search_query = st.text_input(
                    "🔍 Tìm kiếm trong tương tác:",
                    placeholder="Nhập từ khóa để tìm...",
                    key="interaction_search"
                )
            with col2:
                severity_filter = st.multiselect(
                    "Lọc theo mức độ:",
                    [SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR],
                    default=[SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR],
                    key="severity_filter"
                )
            
            # Filter interactions
            filtered_interactions = interactions
            if search_query:
                search_lower = search_query.lower()
                filtered_interactions = [
                    i for i in filtered_interactions
                    if (search_lower in i.get('drug1', '').lower() or
                        search_lower in i.get('drug2', '').lower() or
                        search_lower in i.get('mechanism', '').lower() or
                        search_lower in i.get('description', '').lower() or
                        search_lower in i.get('management', '').lower())
                ]
            
            if severity_filter:
                filtered_interactions = [
                    i for i in filtered_interactions
                    if i.get('severity') in severity_filter
                ]
            
            # Group by severity
            major_interactions = [i for i in filtered_interactions if i['severity'] == SEVERITY_MAJOR]
            moderate_interactions = [i for i in filtered_interactions if i['severity'] == SEVERITY_MODERATE]
            minor_interactions = [i for i in filtered_interactions if i['severity'] == SEVERITY_MINOR]
            
            # Major interactions
            if major_interactions:
                st.markdown("##### 🔴 Tương tác Nghiêm Trọng (Major)")
                for interaction in major_interactions:
                    with st.expander(
                        f"**{interaction['drug1']}** ↔ **{interaction['drug2']}** - {interaction['severity']}",
                        expanded=True
                    ):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.markdown(f"**🔬 Cơ chế:** {interaction['mechanism']}")
                            st.markdown(f"**📝 Mô tả:** {interaction['description']}")
                            
                            # Clinical significance
                            if 'clinical_significance' in interaction:
                                st.markdown(f"**⚕️ Ý nghĩa lâm sàng:**")
                                st.error(interaction['clinical_significance'])
                            
                            st.markdown("**📋 Hướng xử trí:**")
                            st.warning(interaction['management'])

                        # Timing & monitoring
                        onset = interaction.get('onset')
                        if onset:
                            st.caption(f"⏱️ Khởi phát: {onset}")
                        monitoring = interaction.get('monitoring')
                        if monitoring:
                            st.caption("🩺 Theo dõi: " + ", ".join(monitoring))
                        special = interaction.get('special_populations')
                        if special:
                            st.caption("👥 Bối cảnh đặc biệt: " + ", ".join(special))
                        evidence = interaction.get('evidence_level')
                        if evidence:
                            st.caption(f"📖 Mức độ chứng cứ: {evidence}")
                            
                            if 'references' in interaction:
                                st.caption(f"📚 **Tài liệu tham khảo:** {interaction['references']}")
                        
                        with col2:
                            # Alternatives
                            if 'alternatives' in interaction:
                                st.markdown("**💡 Thuốc thay thế:**")
                                alt = interaction['alternatives']
                                
                                # Check for drug1 alternatives
                                drug1_key = f"for_{interaction['drug1'].lower().replace(' ', '_')}"
                                drug2_key = f"for_{interaction['drug2'].lower().replace(' ', '_')}"
                                
                                if drug1_key in alt:
                                    st.info(f"**Thay {interaction['drug1']}:**\n" + ", ".join(alt[drug1_key]))
                                
                                if drug2_key in alt:
                                    st.info(f"**Thay {interaction['drug2']}:**\n" + ", ".join(alt[drug2_key]))
                                
                                # Generic alternatives (other keys)
                                for key, value in alt.items():
                                    if key not in [drug1_key, drug2_key] and isinstance(value, list):
                                        st.info(f"**{key.replace('_', ' ').title()}:**\n" + ", ".join(value))
            
            # Moderate interactions
            if moderate_interactions:
                st.markdown("##### 🟡 Tương tác Trung Bình (Moderate)")
                for interaction in moderate_interactions:
                    with st.expander(
                        f"**{interaction['drug1']}** ↔ **{interaction['drug2']}** - {interaction['severity']}",
                        expanded=False
                    ):
                        st.markdown(f"**🔬 Cơ chế:** {interaction['mechanism']}")
                        st.markdown(f"**📝 Mô tả:** {interaction['description']}")
                        
                        # Clinical significance
                        if 'clinical_significance' in interaction:
                            st.markdown(f"**⚕️ Ý nghĩa lâm sàng:**")
                            st.warning(interaction['clinical_significance'])
                        
                        st.markdown("**📋 Hướng xử trí:**")
                        st.info(interaction['management'])

                        onset = interaction.get('onset')
                        if onset:
                            st.caption(f"⏱️ Khởi phát: {onset}")
                        monitoring = interaction.get('monitoring')
                        if monitoring:
                            st.caption("🩺 Theo dõi: " + ", ".join(monitoring))
                        special = interaction.get('special_populations')
                        if special:
                            st.caption("👥 Bối cảnh đặc biệt: " + ", ".join(special))
                        evidence = interaction.get('evidence_level')
                        if evidence:
                            st.caption(f"📖 Mức độ chứng cứ: {evidence}")
                        
                        # Alternatives
                        if 'alternatives' in interaction:
                            st.markdown("**💡 Thuốc thay thế:**")
                            alt = interaction['alternatives']
                            drug1_key = f"for_{interaction['drug1'].lower().replace(' ', '_')}"
                            drug2_key = f"for_{interaction['drug2'].lower().replace(' ', '_')}"
                            
                            if drug1_key in alt:
                                st.caption(f"**Thay {interaction['drug1']}:** {', '.join(alt[drug1_key])}")
                            if drug2_key in alt:
                                st.caption(f"**Thay {interaction['drug2']}:** {', '.join(alt[drug2_key])}")
                            
                            for key, value in alt.items():
                                if key not in [drug1_key, drug2_key] and isinstance(value, list):
                                    st.caption(f"**{key.replace('_', ' ').title()}:** {', '.join(value)}")
                        
                        if 'references' in interaction:
                            st.caption(f"📚 **Tài liệu tham khảo:** {interaction['references']}")
            
            # Minor interactions
            if minor_interactions:
                st.markdown("##### 🔵 Tương tác Nhẹ (Minor)")
                for interaction in minor_interactions:
                    with st.expander(
                        f"**{interaction['drug1']}** ↔ **{interaction['drug2']}** - {interaction['severity']}",
                        expanded=False
                    ):
                        st.markdown(f"**🔬 Cơ chế:** {interaction['mechanism']}")
                        st.markdown(f"**📝 Mô tả:** {interaction['description']}")
                        
                        st.markdown("**📋 Hướng xử trí:**")
                        st.info(interaction['management'])

                        onset = interaction.get('onset')
                        if onset:
                            st.caption(f"⏱️ Khởi phát: {onset}")
                        monitoring = interaction.get('monitoring')
                        if monitoring:
                            st.caption("🩺 Theo dõi: " + ", ".join(monitoring))
                        special = interaction.get('special_populations')
                        if special:
                            st.caption("👥 Bối cảnh đặc biệt: " + ", ".join(special))
                        evidence = interaction.get('evidence_level')
                        if evidence:
                            st.caption(f"📖 Mức độ chứng cứ: {evidence}")
                        
                        if 'references' in interaction:
                            st.caption(f"📚 **Tài liệu tham khảo:** {interaction['references']}")
        else:
            st.success("✅ **Không phát hiện tương tác thuốc trong danh sách này**")
            st.info("💡 Lưu ý: Database hiện tại chỉ bao gồm các tương tác phổ biến. Vẫn cần tham khảo nguồn đáng tin cậy.")
        
        # Food and Alcohol Interactions
        st.markdown("---")
        st.markdown("### 🍽️ Tương tác với Thực phẩm & Rượu")
        
        # Check food interactions
        food_interactions = check_food_interactions(checked_drugs)
        alcohol_interactions = check_alcohol_interactions(checked_drugs)
        
        if food_interactions or alcohol_interactions:
            # Food interactions
            if food_interactions:
                st.markdown("#### 🥗 Tương tác với Thực phẩm")
                for drug, food_data in food_interactions.items():
                    if 'foods' in food_data:
                        with st.expander(f"**{drug}** - Tương tác với thực phẩm", expanded=False):
                            for food_name, interaction_info in food_data['foods'].items():
                                severity = interaction_info.get('severity', SEVERITY_MODERATE)
                                severity_icon = "🔴" if severity == SEVERITY_MAJOR else "🟡" if severity == SEVERITY_MODERATE else "🔵"
                                
                                st.markdown(f"##### {severity_icon} **{food_name}** - {severity}")
                                st.markdown(f"**🔬 Cơ chế:** {interaction_info.get('mechanism', 'N/A')}")
                                st.markdown(f"**📝 Mô tả:** {interaction_info.get('description', 'N/A')}")
                                
                                if 'foods_list' in interaction_info:
                                    st.markdown(f"**📋 Thực phẩm cần tránh:** {', '.join(interaction_info['foods_list'])}")
                                
                                st.markdown("**📋 Hướng xử trí:**")
                                if severity == SEVERITY_MAJOR:
                                    st.error(interaction_info.get('management', 'N/A'))
                                elif severity == SEVERITY_MODERATE:
                                    st.warning(interaction_info.get('management', 'N/A'))
                                else:
                                    st.info(interaction_info.get('management', 'N/A'))
            
            # Alcohol interactions
            if alcohol_interactions:
                st.markdown("#### 🍷 Tương tác với Rượu")
                for drug, interaction_info in alcohol_interactions.items():
                    severity = interaction_info.get('severity', SEVERITY_MODERATE)
                    severity_icon = "🔴" if severity == SEVERITY_MAJOR else "🟡" if severity == SEVERITY_MODERATE else "🔵"
                    
                    with st.expander(f"**{drug}** - Tương tác với rượu {severity_icon}", expanded=True if severity == SEVERITY_MAJOR else False):
                        st.markdown(f"**Mức độ:** {severity}")
                        st.markdown(f"**🔬 Cơ chế:** {interaction_info.get('mechanism', 'N/A')}")
                        st.markdown(f"**📝 Mô tả:** {interaction_info.get('description', 'N/A')}")
                        
                        st.markdown("**📋 Hướng xử trí:**")
                        if severity == SEVERITY_MAJOR:
                            st.error(interaction_info.get('management', 'N/A'))
                        elif severity == SEVERITY_MODERATE:
                            st.warning(interaction_info.get('management', 'N/A'))
                        else:
                            st.info(interaction_info.get('management', 'N/A'))
        else:
            st.info("✅ **Không phát hiện tương tác với thực phẩm hoặc rượu** cho các thuốc đã kiểm tra.")
        
        # Clear button
        if st.button("🗑️ Xóa kết quả", use_container_width=True):
            if 'interactions' in st.session_state:
                del st.session_state['interactions']
            if 'checked_drugs' in st.session_state:
                del st.session_state['checked_drugs']
            if 'original_drugs' in st.session_state:
                del st.session_state['original_drugs']
            st.rerun()
    
    # Available drugs info
    with st.expander("ℹ️ Thông tin Database"):
        st.markdown("""
        **📊 Database hiện tại:**
        - **500+ tương tác thuốc** được phân loại theo 8 nhóm chính
        - **Hỗ trợ class-based matching** - Tự động nhận diện tương tác theo nhóm thuốc
        - **Fuzzy matching** - Tìm thuốc ngay cả khi gõ sai chính tả
        - **Autocomplete** - Gợi ý thuốc khi nhập
        
        **Các nhóm thuốc được hỗ trợ:**
        - **Anticoagulants:** Warfarin, DOACs (Dabigatran, Rivaroxaban, Apixaban), Heparin, LMWH
        - **Antibiotics:** Beta-lactams, Quinolones, Macrolides, Tetracyclines, Vancomycin, Linezolid, TMP-SMX, Aminoglycosides, Rifampin
        - **Cardiovascular:** ACE Inhibitors, ARBs, Beta-blockers, CCBs, Digoxin, Amiodarone, Statins, Diuretics
        - **Antidiabetics:** Metformin, Sulfonylureas, DPP-4 inhibitors, SGLT2 inhibitors, GLP-1 agonists, Insulin, TZDs
        - **Psychiatry:** SSRIs, SNRIs, TCAs, Mood Stabilizers, Antipsychotics, Benzodiazepines, MAO Inhibitors
        - **GI:** PPIs, H2 Blockers, Antacids, Metoclopramide, Cholestyramine
        - **Oncology:** Methotrexate, 5-FU, Cyclophosphamide, Doxorubicin, Paclitaxel, TKIs, Immunosuppressants
        - **Other:** NSAIDs, Opioids, Corticosteroids, Antihistamines, Antifungals, Antivirals, Anticonvulsants, Oral Contraceptives, Thyroid Hormones, Theophylline, Iron, Calcium, Herbal/Supplements
        
        💡 **Day 8 Enhancements:** Đã thêm fuzzy matching, class-based interactions, và autocomplete!
        """)
    
    # Disclaimer
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    
    - Công cụ này **CHỈ mục đích hỗ trợ** quyết định lâm sàng
    - **KHÔNG thay thế** đánh giá lâm sàng và kinh nghiệm của bác sĩ
    - Database có thể **không đầy đủ** - luôn tham khảo nguồn đáng tin cậy (Micromedex, AHFS, Clinical Pharmacology)
    - Bác sĩ phải **tự xác minh** kết quả trước khi áp dụng
    - **Tuân thủ** chính sách và quy định địa phương
    """)

