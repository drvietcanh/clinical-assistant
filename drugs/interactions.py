"""
Drug Interaction Checker
Tool to check for drug-drug interactions
"""

import streamlit as st
from .interactions_data import (
    check_interactions,
    normalize_drug_name,
    SEVERITY_MAJOR,
    SEVERITY_MODERATE,
    SEVERITY_MINOR,
    DRUG_ALIASES
)
from components.ui.alerts import render_error_alert, render_warning_alert, render_info_alert
from components.ui.results import render_result_card


def render_interaction_checker():
    """Render drug interaction checker interface"""
    
    st.markdown("## 🔍 Kiểm Tra Tương Tác Thuốc")
    st.markdown("""
    **Công cụ kiểm tra tương tác thuốc-thuốc** giúp phát hiện các tương tác tiềm ẩn trong đơn thuốc.
    
    ⚠️ **Lưu ý:** Database hiện tại bao gồm ~50 tương tác phổ biến. Luôn tham khảo nguồn đáng tin cậy trước khi quyết định lâm sàng.
    """)
    
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
            drug = st.text_input(
                f"Thuốc {i+1}:",
                key=f"drug_{i}",
                placeholder="Ví dụ: Warfarin, Aspirin, Metformin..."
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
    
    # Check button
    if st.button("🔍 Kiểm Tra Tương Tác", type="primary", use_container_width=True):
        if len(drug_list) < 2:
            render_error_alert(
                "Vui lòng nhập ít nhất 2 thuốc để kiểm tra tương tác",
                title="Thiếu thông tin"
            )
        else:
            # Normalize drug names
            normalized_list = [normalize_drug_name(drug) for drug in drug_list]
            
            # Store in session state for display
            st.session_state['checked_drugs'] = normalized_list
            st.session_state['original_drugs'] = drug_list
            
            # Check interactions
            interactions = check_interactions(normalized_list)
            st.session_state['interactions'] = interactions
            
            # Rerun to show results
            st.rerun()
    
    # Display results
    if 'interactions' in st.session_state and st.session_state['interactions']:
        st.markdown("---")
        st.markdown("### 📋 Kết Quả Kiểm Tra")
        
        interactions = st.session_state['interactions']
        checked_drugs = st.session_state.get('checked_drugs', [])
        original_drugs = st.session_state.get('original_drugs', [])
        
        # Summary
        major_count = sum(1 for i in interactions if i['severity'] == SEVERITY_MAJOR)
        moderate_count = sum(1 for i in interactions if i['severity'] == SEVERITY_MODERATE)
        minor_count = sum(1 for i in interactions if i['severity'] == SEVERITY_MINOR)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tổng số thuốc", len(checked_drugs))
        with col2:
            st.metric("⚠️ Major", major_count, delta=None, delta_color="inverse")
        with col3:
            st.metric("⚡ Moderate", moderate_count, delta=None)
        with col4:
            st.metric("ℹ️ Minor", minor_count, delta=None)
        
        # Show checked drugs
        st.markdown("**📋 Danh sách thuốc đã kiểm tra:**")
        drugs_display = ", ".join([f"**{drug}**" for drug in checked_drugs])
        st.info(drugs_display)
        
        # Display interactions
        if interactions:
            st.markdown("---")
            st.markdown("### ⚠️ Phát Hiện Tương Tác")
            
            # Group by severity
            major_interactions = [i for i in interactions if i['severity'] == SEVERITY_MAJOR]
            moderate_interactions = [i for i in interactions if i['severity'] == SEVERITY_MODERATE]
            minor_interactions = [i for i in interactions if i['severity'] == SEVERITY_MINOR]
            
            # Major interactions
            if major_interactions:
                st.markdown("#### 🔴 Tương Tác Nghiêm Trọng (Major)")
                for interaction in major_interactions:
                    with st.expander(
                        f"**{interaction['drug1']}** ↔ **{interaction['drug2']}** - {interaction['severity']}",
                        expanded=True
                    ):
                        st.markdown(f"**Cơ chế:** {interaction['mechanism']}")
                        st.markdown(f"**Mô tả:** {interaction['description']}")
                        
                        st.markdown("**📋 Hướng xử trí:**")
                        st.warning(interaction['management'])
                        
                        if 'references' in interaction:
                            st.caption(f"📚 **Tài liệu tham khảo:** {interaction['references']}")
            
            # Moderate interactions
            if moderate_interactions:
                st.markdown("#### 🟡 Tương Tác Trung Bình (Moderate)")
                for interaction in moderate_interactions:
                    with st.expander(
                        f"**{interaction['drug1']}** ↔ **{interaction['drug2']}** - {interaction['severity']}",
                        expanded=False
                    ):
                        st.markdown(f"**Cơ chế:** {interaction['mechanism']}")
                        st.markdown(f"**Mô tả:** {interaction['description']}")
                        
                        st.markdown("**📋 Hướng xử trí:**")
                        st.info(interaction['management'])
                        
                        if 'references' in interaction:
                            st.caption(f"📚 **Tài liệu tham khảo:** {interaction['references']}")
            
            # Minor interactions
            if minor_interactions:
                st.markdown("#### 🔵 Tương Tác Nhẹ (Minor)")
                for interaction in minor_interactions:
                    with st.expander(
                        f"**{interaction['drug1']}** ↔ **{interaction['drug2']}** - {interaction['severity']}",
                        expanded=False
                    ):
                        st.markdown(f"**Cơ chế:** {interaction['mechanism']}")
                        st.markdown(f"**Mô tả:** {interaction['description']}")
                        
                        st.markdown("**📋 Hướng xử trí:**")
                        st.info(interaction['management'])
                        
                        if 'references' in interaction:
                            st.caption(f"📚 **Tài liệu tham khảo:** {interaction['references']}")
        else:
            st.success("✅ **Không phát hiện tương tác thuốc trong danh sách này**")
            st.info("💡 Lưu ý: Database hiện tại chỉ bao gồm các tương tác phổ biến. Vẫn cần tham khảo nguồn đáng tin cậy.")
        
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
    with st.expander("ℹ️ Danh sách thuốc có trong database"):
        st.markdown("""
        **Database hiện tại hỗ trợ kiểm tra tương tác cho các thuốc sau:**
        
        **Anticoagulants:** Warfarin, Aspirin, Clopidogrel  
        **Antibiotics:** Metronidazole, Ciprofloxacin, Erythromycin, Clarithromycin  
        **Antidepressants:** Fluoxetine, Sertraline, Tramadol  
        **Antihypertensives:** ACE Inhibitor, Digoxin, Amiodarone, Spironolactone  
        **Antidiabetics:** Metformin, Sulfonylurea  
        **Statins:** Atorvastatin, Simvastatin  
        **Antifungals:** Ketoconazole, Fluconazole  
        **PPI:** Omeprazole  
        **Antihistamines:** Diphenhydramine  
        **NSAIDs:** Ibuprofen  
        **Others:** Methotrexate, Oral Contraceptives  
        
        💡 Database sẽ được mở rộng thêm các thuốc phổ biến tại Việt Nam.
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

