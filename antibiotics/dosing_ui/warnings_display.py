"""
Warnings and Alerts Display
Hiển thị cảnh báo và khuyến cáo
"""

import streamlit as st
from ..dosing_calculator import check_warnings


def render_warnings_section(selected_ab, crcl, age, is_pregnant, is_breastfeeding, other_drugs):
    """Render warnings and alerts section"""
    st.markdown("---")
    st.markdown("### ⚠️ Cảnh Báo & Khuyến Cáo:")
    
    warnings = check_warnings(
        selected_ab, crcl, age, 
        is_pregnant=is_pregnant,
        is_breastfeeding=is_breastfeeding,
        other_drugs=other_drugs
    )
    
    if warnings:
        for warning in warnings:
            if warning['level'] == 'high':
                st.error(f"{warning['icon']} **{warning['message']}**")
            elif warning['level'] == 'medium':
                st.warning(f"{warning['icon']} **{warning['message']}**")
            else:
                st.info(f"{warning['icon']} **{warning['message']}**")
    else:
        st.success("✅ Không có cảnh báo đặc biệt cho trường hợp này")
    
    # Drug Interaction Checker Integration
    if other_drugs and len(other_drugs) > 0:
        st.markdown("---")
        st.markdown("### 🔍 Kiểm Tra Tương Tác Thuốc:")
        
        try:
            from drugs.interactions_data import check_interactions, normalize_drug_name, SEVERITY_MAJOR, SEVERITY_MODERATE
            
            # Create drug list including selected antibiotic
            all_drugs = [selected_ab] + other_drugs
            normalized_drugs = [normalize_drug_name(drug) for drug in all_drugs]
            
            # Check interactions
            interactions_found = check_interactions(normalized_drugs)
            
            if interactions_found:
                # Filter interactions involving the selected antibiotic
                ab_interactions = [
                    i for i in interactions_found 
                    if normalize_drug_name(selected_ab) in [i.get('drug1', ''), i.get('drug2', '')]
                ]
                
                if ab_interactions:
                    # Group by severity
                    major_interactions = [i for i in ab_interactions if i.get('severity') == SEVERITY_MAJOR]
                    moderate_interactions = [i for i in ab_interactions if i.get('severity') == SEVERITY_MODERATE]
                    minor_interactions = [i for i in ab_interactions if i.get('severity') == 'Minor']
                    
                    # Display major interactions
                    if major_interactions:
                        st.error("🚨 **Tương Tác Nghiêm Trọng (Major):**")
                        for interaction in major_interactions:
                            other_drug = interaction.get('drug2', '') if normalize_drug_name(selected_ab) == interaction.get('drug1', '') else interaction.get('drug1', '')
                            st.error(f"""
                            **{selected_ab} + {other_drug}**
                            - **Cơ chế:** {interaction.get('mechanism', 'N/A')}
                            - **Mô tả:** {interaction.get('description', 'N/A')}
                            - **Xử trí:** {interaction.get('management', 'N/A')}
                            """)
                    
                    # Display moderate interactions
                    if moderate_interactions:
                        st.warning("⚠️ **Tương Tác Trung Bình (Moderate):**")
                        for interaction in moderate_interactions:
                            other_drug = interaction.get('drug2', '') if normalize_drug_name(selected_ab) == interaction.get('drug1', '') else interaction.get('drug1', '')
                            st.warning(f"""
                            **{selected_ab} + {other_drug}**
                            - **Cơ chế:** {interaction.get('mechanism', 'N/A')}
                            - **Mô tả:** {interaction.get('description', 'N/A')}
                            - **Xử trí:** {interaction.get('management', 'N/A')}
                            """)
                    
                    # Display minor interactions (collapsed)
                    if minor_interactions:
                        with st.expander(f"ℹ️ Tương Tác Nhẹ (Minor) - {len(minor_interactions)} tương tác"):
                            for interaction in minor_interactions:
                                other_drug = interaction.get('drug2', '') if normalize_drug_name(selected_ab) == interaction.get('drug1', '') else interaction.get('drug1', '')
                                st.info(f"**{selected_ab} + {other_drug}:** {interaction.get('description', 'N/A')}")
                else:
                    st.success(f"✅ Không phát hiện tương tác giữa {selected_ab} và các thuốc đang dùng")
            else:
                st.success(f"✅ Không phát hiện tương tác giữa {selected_ab} và các thuốc đang dùng")
                
        except ImportError:
            st.info("💡 **Gợi ý:** Sử dụng công cụ 'Kiểm Tra Tương Tác Thuốc' trong module Tra Cứu Thuốc để kiểm tra chi tiết")
        except Exception as e:
            st.info("💡 **Gợi ý:** Sử dụng công cụ 'Kiểm Tra Tương Tác Thuốc' trong module Tra Cứu Thuốc để kiểm tra chi tiết")

