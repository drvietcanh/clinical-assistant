"""
Drug Interaction Checker UI Components
Streamlit components for displaying drug interaction warnings
"""

import streamlit as st
from typing import List, Dict

try:
    from .interaction_checker import DrugInteractionChecker
    from .drug_interactions import SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR
except ImportError:
    from interaction_checker import DrugInteractionChecker
    from drug_interactions import SEVERITY_MAJOR, SEVERITY_MODERATE, SEVERITY_MINOR


def render_interaction_warning(interaction: Dict):
    """
    Render a single interaction warning with enhanced UI/UX
    Includes color coding, expandable details, and alternative suggestions
    
    Args:
        interaction: Interaction dict
    """
    severity = interaction.get('severity', SEVERITY_MODERATE)
    drug1 = interaction.get('drug1', 'Unknown')
    drug2 = interaction.get('drug2', 'Unknown')
    
    # Enhanced color coding and styling
    if severity == SEVERITY_MAJOR:
        # Major - Red with danger styling
        st.markdown(
            f"""
            <div style="
                background-color: #ffebee;
                border-left: 5px solid #d32f2f;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
            ">
                <h4 style="color: #d32f2f; margin: 0;">
                    🔴 <strong>MAJOR INTERACTION</strong>: {drug1} + {drug2}
                </h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        with st.expander("📋 Chi tiết tương tác nghiêm trọng", expanded=True):
            # Effect
            if 'effect' in interaction or 'description' in interaction:
                effect = interaction.get('effect') or interaction.get('description', 'N/A')
                st.markdown(f"**⚠️ Tác dụng:** {effect}")
            
            # Clinical significance
            if 'clinical_significance' in interaction:
                st.markdown(f"**📊 Ý nghĩa lâm sàng:** {interaction['clinical_significance']}")
            
            # Mechanism
            if 'mechanism' in interaction:
                st.markdown(f"**🔬 Cơ chế:** {interaction['mechanism']}")
            
            # Management
            if 'management' in interaction:
                st.markdown(f"**💊 Xử trí:** {interaction['management']}")
            
            # Alternatives
            if 'alternatives' in interaction:
                st.markdown("**🔄 Thuốc thay thế:**")
                alternatives = interaction['alternatives']
                if 'for_' + drug1.lower().replace(' ', '_') in str(alternatives):
                    # Find matching key
                    for key, alt_list in alternatives.items():
                        if drug1.lower() in key.lower() or drug2.lower() in key.lower():
                            st.markdown(f"- Thay thế {key.replace('for_', '')}: {', '.join(alt_list)}")
                else:
                    for key, alt_list in alternatives.items():
                        st.markdown(f"- {key}: {', '.join(alt_list)}")
            
            # References
            if 'references' in interaction:
                refs = interaction['references']
                if isinstance(refs, list):
                    st.caption(f"📚 Tài liệu: {', '.join(refs)}")
                else:
                    st.caption(f"📚 Tài liệu: {refs}")
    
    elif severity == SEVERITY_MODERATE:
        # Moderate - Orange/Yellow with warning styling
        st.markdown(
            f"""
            <div style="
                background-color: #fff3e0;
                border-left: 5px solid #f57c00;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
            ">
                <h4 style="color: #f57c00; margin: 0;">
                    🟡 <strong>MODERATE INTERACTION</strong>: {drug1} + {drug2}
                </h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        with st.expander("📋 Chi tiết tương tác vừa phải"):
            # Effect
            if 'effect' in interaction or 'description' in interaction:
                effect = interaction.get('effect') or interaction.get('description', 'N/A')
                st.markdown(f"**⚠️ Tác dụng:** {effect}")
            
            # Mechanism
            if 'mechanism' in interaction:
                st.markdown(f"**🔬 Cơ chế:** {interaction['mechanism']}")
            
            # Management
            if 'management' in interaction:
                st.markdown(f"**💊 Xử trí:** {interaction['management']}")
            
            # Alternatives
            if 'alternatives' in interaction:
                st.markdown("**🔄 Thuốc thay thế:**")
                alternatives = interaction['alternatives']
                for key, alt_list in alternatives.items():
                    st.markdown(f"- {key}: {', '.join(alt_list)}")
            
            # References
            if 'references' in interaction:
                refs = interaction['references']
                if isinstance(refs, list):
                    st.caption(f"📚 Tài liệu: {', '.join(refs)}")
                else:
                    st.caption(f"📚 Tài liệu: {refs}")
    
    else:  # MINOR
        # Minor - Blue with info styling
        st.markdown(
            f"""
            <div style="
                background-color: #e3f2fd;
                border-left: 5px solid #1976d2;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
            ">
                <h4 style="color: #1976d2; margin: 0;">
                    🔵 <strong>MINOR INTERACTION</strong>: {drug1} + {drug2}
                </h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        with st.expander("📋 Chi tiết tương tác nhẹ"):
            # Effect
            if 'effect' in interaction or 'description' in interaction:
                effect = interaction.get('effect') or interaction.get('description', 'N/A')
                st.markdown(f"**ℹ️ Tác dụng:** {effect}")
            
            # Management
            if 'management' in interaction:
                st.markdown(f"**💊 Xử trí:** {interaction['management']}")
            
            # References
            if 'references' in interaction:
                refs = interaction['references']
                if isinstance(refs, list):
                    st.caption(f"📚 Tài liệu: {', '.join(refs)}")
                else:
                    st.caption(f"📚 Tài liệu: {refs}")


def render_interaction_summary(summary: Dict):
    """
    Render interaction summary with enhanced metrics and visual indicators
    
    Args:
        summary: Summary dict from DrugInteractionChecker
    """
    st.markdown("### 📊 Tổng Kết Tương Tác Thuốc")
    
    # Enhanced metrics with color coding
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Tổng tương tác",
            summary.get('total_interactions', 0),
            delta=None
        )
    
    with col2:
        major_count = summary.get('major', 0)
        st.metric(
            "🔴 Major",
            major_count,
            delta="Nguy hiểm" if major_count > 0 else None,
            delta_color="inverse"
        )
        if major_count > 0:
            st.markdown(
                f'<div style="background-color: #ffebee; padding: 5px; border-radius: 3px; text-align: center; font-size: 0.8em; color: #d32f2f;">⚠️ Cần xử trí ngay</div>',
                unsafe_allow_html=True
            )
    
    with col3:
        moderate_count = summary.get('moderate', 0)
        st.metric(
            "🟡 Moderate",
            moderate_count,
            delta="Theo dõi" if moderate_count > 0 else None,
            delta_color="off"
        )
        if moderate_count > 0:
            st.markdown(
                f'<div style="background-color: #fff3e0; padding: 5px; border-radius: 3px; text-align: center; font-size: 0.8em; color: #f57c00;">📋 Cần theo dõi</div>',
                unsafe_allow_html=True
            )
    
    with col4:
        minor_count = summary.get('minor', 0)
        st.metric(
            "🟢 Minor",
            minor_count,
            delta="Nhẹ" if minor_count > 0 else None,
            delta_color="off"
        )
    
    # Enhanced risk level indicator with better styling
    risk_level = summary.get('risk_level', 'NONE')
    st.markdown("<br>", unsafe_allow_html=True)
    
    if risk_level == "HIGH":
        st.markdown(
            f"""
            <div style="
                background-color: #ffebee;
                border: 2px solid #d32f2f;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 10px 0;
            ">
                <h3 style="color: #d32f2f; margin: 0;">
                    ⚠️ <strong>MỨC ĐỘ RỦI RO: {risk_level}</strong>
                </h3>
                <p style="color: #d32f2f; margin: 10px 0 0 0;">
                    Tránh dùng chung nếu có thể! Cần xem xét lại phác đồ điều trị.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif risk_level == "MODERATE":
        st.markdown(
            f"""
            <div style="
                background-color: #fff3e0;
                border: 2px solid #f57c00;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 10px 0;
            ">
                <h3 style="color: #f57c00; margin: 0;">
                    ⚠️ <strong>MỨC ĐỘ RỦI RO: {risk_level}</strong>
                </h3>
                <p style="color: #f57c00; margin: 10px 0 0 0;">
                    Theo dõi bệnh nhân sát. Cân nhắc điều chỉnh liều hoặc theo dõi thêm.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif risk_level == "LOW":
        st.markdown(
            f"""
            <div style="
                background-color: #e3f2fd;
                border: 2px solid #1976d2;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 10px 0;
            ">
                <h3 style="color: #1976d2; margin: 0;">
                    ℹ️ <strong>MỨC ĐỘ RỦI RO: {risk_level}</strong>
                </h3>
                <p style="color: #1976d2; margin: 10px 0 0 0;">
                    Ít quan trọng lâm sàng. Có thể tiếp tục điều trị với theo dõi thông thường.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background-color: #e8f5e9;
                border: 2px solid #388e3c;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 10px 0;
            ">
                <h3 style="color: #388e3c; margin: 0;">
                    ✅ <strong>KHÔNG PHÁT HIỆN TƯƠNG TÁC</strong>
                </h3>
                <p style="color: #388e3c; margin: 10px 0 0 0;">
                    Không có tương tác thuốc được phát hiện. Phác đồ điều trị an toàn.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_medication_list_with_checker():
    """
    Render medication list with real-time interaction checking
    """
    st.markdown("### 💊 Danh Sách Thuốc Hiện Tại")
    
    # Initialize session state
    if 'medication_list' not in st.session_state:
        st.session_state.medication_list = []
    
    # Add new medication with autocomplete
    try:
        from .interactions_data import get_drug_autocomplete_suggestions
    except ImportError:
        from interactions_data import get_drug_autocomplete_suggestions
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        new_drug = st.text_input(
            "Thêm thuốc mới",
            placeholder="Nhập tên thuốc (có autocomplete)...",
            key="new_drug_input"
        )
        
        # Show autocomplete suggestions
        if new_drug and len(new_drug) >= 2:
            suggestions = get_drug_autocomplete_suggestions(new_drug, max_results=5)
            if suggestions:
                st.caption("💡 Gợi ý: " + " | ".join(suggestions[:5]))
    
    with col2:
        add_button = st.button("➕ Thêm", use_container_width=True, type="primary")
    
    # Check for interactions when adding new drug
    if add_button and new_drug:
        checker = DrugInteractionChecker()
        
        if new_drug not in st.session_state.medication_list:
            # Check interactions with current drugs
            new_interactions = checker.check_new_drug(
                st.session_state.medication_list,
                new_drug
            )
            
            if new_interactions:
                st.warning(f"⚠️ Cảnh báo: Thêm {new_drug} sẽ gây {len(new_interactions)} tương tác!")
                
                for interaction in new_interactions:
                    if interaction['severity'] == SEVERITY_MAJOR:
                        st.error(
                            f"🚨 MAJOR: {interaction['drug1']} + {new_drug}\n\n"
                            f"{interaction['effect']}"
                        )
                
                # Ask for confirmation
                confirm = st.checkbox(
                    f"Tôi hiểu rủi ro và vẫn muốn thêm {new_drug}",
                    key=f"confirm_{new_drug}"
                )
                
                if confirm:
                    st.session_state.medication_list.append(new_drug)
                    st.success(f"✅ Đã thêm {new_drug}")
                    st.rerun()
            else:
                # No interactions - add directly
                st.session_state.medication_list.append(new_drug)
                st.success(f"✅ Đã thêm {new_drug} (Không có tương tác)")
                st.rerun()
        else:
            st.warning(f"{new_drug} đã có trong danh sách")
    
    # Display current medications with enhanced styling
    if st.session_state.medication_list:
        st.markdown("**📋 Thuốc hiện tại:**")
        
        # Responsive grid layout for medications
        num_cols = 2  # 2 columns on mobile, can be adjusted
        for idx in range(0, len(st.session_state.medication_list), num_cols):
            cols = st.columns(num_cols)
            for col_idx, col in enumerate(cols):
                if idx + col_idx < len(st.session_state.medication_list):
                    drug = st.session_state.medication_list[idx + col_idx]
                    with col:
                        st.markdown(
                            f"""
                            <div style="
                                background-color: #f5f5f5;
                                padding: 10px;
                                border-radius: 5px;
                                margin: 5px 0;
                                border-left: 3px solid #2196F3;
                            ">
                                <strong>{idx + col_idx + 1}. {drug}</strong>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button("🗑️ Xóa", key=f"remove_{idx + col_idx}", use_container_width=True):
                            st.session_state.medication_list.pop(idx + col_idx)
                            st.rerun()
        
        # Check all interactions
        if len(st.session_state.medication_list) >= 2:
            st.markdown("---")
            checker = DrugInteractionChecker()
            summary = checker.get_summary(st.session_state.medication_list)
            
            # Show summary
            render_interaction_summary(summary)
            
            # Show detailed interactions with search/filter/sort
            if summary['interactions']:
                st.markdown("### 📋 Chi tiết Tương Tác")
                
                # Search and Filter Section
                with st.expander("🔍 Tìm Kiếm & Lọc", expanded=False):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        search_query = st.text_input(
                            "🔍 Tìm kiếm",
                            placeholder="Tên thuốc, cơ chế, tác dụng...",
                            key="interaction_search"
                        )
                    
                    with col2:
                        severity_filter = st.multiselect(
                            "📊 Lọc theo mức độ",
                            ["Major", "Moderate", "Minor"],
                            key="severity_filter"
                        )
                    
                    # Drug class filter
                    try:
                        from .interactions_data import DRUG_CLASS_MAPPINGS, get_drug_classes
                    except ImportError:
                        from interactions_data import DRUG_CLASS_MAPPINGS, get_drug_classes
                    
                    # Get unique drug classes from interactions
                    all_drugs_in_interactions = set()
                    for interaction in summary['interactions']:
                        all_drugs_in_interactions.add(interaction.get('drug1', ''))
                        all_drugs_in_interactions.add(interaction.get('drug2', ''))
                    
                    # Get classes for these drugs
                    available_classes = set()
                    for drug in all_drugs_in_interactions:
                        classes = get_drug_classes(drug)
                        available_classes.update(classes)
                    
                    if available_classes:
                        col3, col4 = st.columns(2)
                        with col3:
                            drug_class_filter = st.multiselect(
                                "💊 Lọc theo nhóm thuốc",
                                sorted(available_classes),
                                key="drug_class_filter"
                            )
                        
                        with col4:
                            sort_option = st.selectbox(
                                "🔄 Sắp xếp",
                                ["Theo mức độ (Major → Minor)", "Theo tên thuốc (A-Z)", "Theo tên thuốc (Z-A)"],
                                key="sort_option"
                            )
                    else:
                        sort_option = st.selectbox(
                            "🔄 Sắp xếp",
                            ["Theo mức độ (Major → Minor)", "Theo tên thuốc (A-Z)", "Theo tên thuốc (Z-A)"],
                            key="sort_option"
                        )
                        drug_class_filter = []
                
                # Filter interactions
                filtered_interactions = summary['interactions']
                
                # Apply search filter
                if search_query:
                    search_lower = search_query.lower()
                    filtered_interactions = [
                        i for i in filtered_interactions
                        if (search_lower in i.get('drug1', '').lower() or
                            search_lower in i.get('drug2', '').lower() or
                            search_lower in i.get('effect', '').lower() or
                            search_lower in i.get('description', '').lower() or
                            search_lower in i.get('mechanism', '').lower() or
                            search_lower in i.get('management', '').lower())
                    ]
                
                # Apply severity filter
                if severity_filter:
                    filtered_interactions = [
                        i for i in filtered_interactions
                        if i.get('severity') in severity_filter
                    ]
                
                # Apply drug class filter
                if 'drug_class_filter' in locals() and drug_class_filter:
                    try:
                        from .interactions_data import get_drug_classes
                    except ImportError:
                        from interactions_data import get_drug_classes
                    
                    class_filtered = []
                    for interaction in filtered_interactions:
                        drug1_classes = get_drug_classes(interaction.get('drug1', ''))
                        drug2_classes = get_drug_classes(interaction.get('drug2', ''))
                        
                        # Check if any class matches
                        if any(cls in drug_class_filter for cls in drug1_classes) or \
                           any(cls in drug_class_filter for cls in drug2_classes):
                            class_filtered.append(interaction)
                    
                    filtered_interactions = class_filtered
                
                # Apply sort
                if sort_option == "Theo mức độ (Major → Minor)":
                    severity_order = {SEVERITY_MAJOR: 0, SEVERITY_MODERATE: 1, SEVERITY_MINOR: 2}
                    filtered_interactions.sort(key=lambda x: severity_order.get(x.get('severity'), 3))
                elif sort_option == "Theo tên thuốc (A-Z)":
                    filtered_interactions.sort(key=lambda x: (x.get('drug1', ''), x.get('drug2', '')))
                elif sort_option == "Theo tên thuốc (Z-A)":
                    filtered_interactions.sort(key=lambda x: (x.get('drug1', ''), x.get('drug2', '')), reverse=True)
                
                # Show filtered count
                if len(filtered_interactions) != len(summary['interactions']):
                    st.info(f"📊 Hiển thị {len(filtered_interactions)}/{len(summary['interactions'])} tương tác")
                
                # Clear filters button
                has_filters = search_query or severity_filter or ('drug_class_filter' in locals() and drug_class_filter)
                if has_filters:
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if st.button("🔄 Xóa bộ lọc", key="clear_filters", use_container_width=True):
                            st.session_state.interaction_search = ""
                            st.session_state.severity_filter = []
                            if 'drug_class_filter' in st.session_state:
                                st.session_state.drug_class_filter = []
                            st.rerun()
                    with col2:
                        st.caption(f"Đang lọc: {len(filtered_interactions)}/{len(summary['interactions'])} tương tác")
                
                # Display filtered interactions
                if filtered_interactions:
                    for interaction in filtered_interactions:
                        render_interaction_warning(interaction)
                else:
                    st.info("Không tìm thấy tương tác nào phù hợp với bộ lọc.")
            
            # Show recommendations
            st.markdown("### 💡 Khuyến nghị Lâm Sàng")
            recommendations = checker.get_recommendations(st.session_state.medication_list)
            for rec in recommendations:
                st.markdown(f"- {rec}")
            
            # Export Section
            st.markdown("---")
            st.markdown("### 📤 Xuất Báo Cáo")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📄 Tạo Báo Cáo TXT", use_container_width=True):
                    report = checker.generate_report(st.session_state.medication_list)
                    st.text_area("Báo cáo tương tác thuốc", report, height=300, key="txt_report")
                    
                    st.download_button(
                        label="⬇️ Tải TXT",
                        data=report,
                        file_name=f"drug_interaction_report_{len(st.session_state.medication_list)}_drugs.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            
            with col2:
                if st.button("📊 Tạo Báo Cáo CSV", use_container_width=True):
                    import csv
                    import io
                    
                    # Create CSV report
                    output = io.StringIO()
                    writer = csv.writer(output)
                    
                    # Header
                    writer.writerow(["Drug 1", "Drug 2", "Severity", "Effect", "Mechanism", "Management"])
                    
                    # Data
                    for interaction in summary.get('interactions', []):
                        writer.writerow([
                            interaction.get('drug1', ''),
                            interaction.get('drug2', ''),
                            interaction.get('severity', ''),
                            interaction.get('effect', interaction.get('description', '')),
                            interaction.get('mechanism', ''),
                            interaction.get('management', '')
                        ])
                    
                    csv_data = output.getvalue()
                    st.download_button(
                        label="⬇️ Tải CSV",
                        data=csv_data,
                        file_name=f"drug_interaction_report_{len(st.session_state.medication_list)}_drugs.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
            
            with col3:
                if st.button("🖨️ In Báo Cáo", use_container_width=True):
                    st.info("Sử dụng Ctrl+P (Windows) hoặc Cmd+P (Mac) để in trang này")
                    st.markdown(
                        """
                        <style>
                        @media print {
                            .stApp { visibility: hidden; }
                            .print-content { visibility: visible; }
                        }
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
    else:
        st.info("Chưa có thuốc nào. Thêm thuốc để kiểm tra tương tác.")
    
    # Clear all button
    if st.session_state.medication_list:
        if st.button("🗑️ Xóa Tất Cả", type="secondary"):
            st.session_state.medication_list = []
            st.rerun()


def render_quick_interaction_check():
    """
    Quick interaction checker for 2 drugs with enhanced search
    """
    st.markdown("### ⚡ Kiểm Tra Nhanh (2 Thuốc)")
    
    try:
        from .interactions_data import get_drug_autocomplete_suggestions
    except ImportError:
        from interactions_data import get_drug_autocomplete_suggestions
    
    col1, col2 = st.columns(2)
    
    with col1:
        drug1 = st.text_input("Thuốc 1", key="quick_drug1", placeholder="Nhập tên thuốc...")
        if drug1 and len(drug1) >= 2:
            suggestions1 = get_drug_autocomplete_suggestions(drug1, max_results=3)
            if suggestions1:
                st.caption("💡 " + " | ".join(suggestions1[:3]))
    
    with col2:
        drug2 = st.text_input("Thuốc 2", key="quick_drug2", placeholder="Nhập tên thuốc...")
        if drug2 and len(drug2) >= 2:
            suggestions2 = get_drug_autocomplete_suggestions(drug2, max_results=3)
            if suggestions2:
                st.caption("💡 " + " | ".join(suggestions2[:3]))
    
    if st.button("🔍 Kiểm Tra", use_container_width=True, type="primary"):
        if drug1 and drug2:
            checker = DrugInteractionChecker()
            interaction = checker.check_pair(drug1, drug2)
            
            if interaction:
                st.markdown(f"### Kết quả: {drug1} + {drug2}")
                render_interaction_warning({
                    'drug1': drug1,
                    'drug2': drug2,
                    **interaction
                })
            else:
                st.success(f"✅ Không phát hiện tương tác giữa {drug1} và {drug2}")
        else:
            st.warning("Vui lòng nhập cả 2 thuốc")


def render_complete_interaction_checker():
    """
    Complete interaction checker page
    Main entry point with enhanced UI/UX and mobile responsive design
    """
    # Add custom CSS for mobile responsive design
    st.markdown(
        """
        <style>
        @media (max-width: 768px) {
            .stMetric {
                padding: 10px !important;
            }
            .stExpander {
                font-size: 0.9em;
            }
        }
        .interaction-card {
            margin: 10px 0;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("⚠️ Kiểm Tra Tương Tác Thuốc")
    
    st.markdown(
        """
        <div style="
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        ">
            <p style="margin: 0;">
                Công cụ kiểm tra tương tác thuốc giúp phát hiện các tương tác có ý nghĩa lâm sàng 
                giữa các thuốc để đảm bảo an toàn cho người bệnh.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Enhanced severity legend
    st.markdown("**📊 Phân loại mức độ nghiêm trọng:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div style="
                background-color: #ffebee;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #d32f2f;
            ">
                <strong>🔴 MAJOR</strong><br>
                <small>Tránh dùng chung - Có thể gây nguy hiểm tính mạng</small>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style="
                background-color: #fff3e0;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #f57c00;
            ">
                <strong>🟡 MODERATE</strong><br>
                <small>Theo dõi sát - Cần điều chỉnh liều hoặc theo dõi</small>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div style="
                background-color: #e3f2fd;
                padding: 10px;
                border-radius: 5px;
                border-left: 4px solid #1976d2;
            ">
                <strong>🟢 MINOR</strong><br>
                <small>Ít quan trọng lâm sàng</small>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Tabs
    tab1, tab2 = st.tabs(["📋 Danh Sách Thuốc", "⚡ Kiểm Tra Nhanh"])
    
    with tab1:
        render_medication_list_with_checker()
    
    with tab2:
        render_quick_interaction_check()
    
    # Database info
    with st.expander("ℹ️ Thông tin Database"):
        from drug_interactions import get_interaction_statistics
        stats = get_interaction_statistics()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tổng tương tác", stats['total_interactions'])
        
        with col2:
            st.metric("Major", stats['major'])
        
        with col3:
            st.metric("Moderate", stats['moderate'])
        
        st.caption(f"Thuốc có tương tác: {', '.join(stats['drugs_with_interactions'][:10])}...")


# Export
__all__ = [
    'render_interaction_warning',
    'render_interaction_summary',
    'render_medication_list_with_checker',
    'render_quick_interaction_check',
    'render_complete_interaction_checker'
]


# Main
if __name__ == "__main__":
    render_complete_interaction_checker()
