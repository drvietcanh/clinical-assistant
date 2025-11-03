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

