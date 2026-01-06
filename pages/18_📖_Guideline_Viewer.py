"""
Guideline Viewer - Enhanced Viewer for Clinical Guidelines
Comprehensive viewer with search, filter, decision trees, and statistics
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from components.guideline_viewer import (
    render_guideline_viewer,
    render_guideline_filters,
    render_guideline_search_bar,
    render_guideline_statistics
)
from components.decision_tree import render_guideline_decision_tree

# Standard page setup
setup_page(
    page_title="Guideline Viewer",
    page_icon="📖",
    description="Xem và tìm kiếm clinical guidelines với decision trees"
)

# Initialize session state
if 'guideline_viewer_show_details' not in st.session_state:
    st.session_state.guideline_viewer_show_details = False

# Hero Section
render_hero(
    title="📖 Guideline Viewer",
    subtitle="Xem và tìm kiếm clinical guidelines",
    description="Truy cập guidelines từ các tổ chức quốc tế với decision trees và khuyến nghị chi tiết"
)

st.markdown("---")

# Statistics Section
render_guideline_statistics()

st.markdown("---")

# Filters in Sidebar
with st.sidebar:
    filters = render_guideline_filters()
    st.markdown("---")
    st.session_state.guideline_viewer_show_details = st.checkbox(
        "Hiển thị chi tiết",
        value=st.session_state.guideline_viewer_show_details,
        key="guideline_show_details"
    )

# Search Bar
search_query = render_guideline_search_bar()

st.markdown("---")

# Main Content: Guideline Viewer
render_guideline_viewer(
    search_query=search_query,
    category_filter=filters["category"],
    organization_filter=filters["organization"],
    year_min=filters["year_min"],
    year_max=filters["year_max"],
    show_details=st.session_state.guideline_viewer_show_details
)

st.markdown("---")

# Decision Trees Section (Example)
st.markdown("### 🌳 Clinical Decision Trees")
st.info("💡 Decision trees sẽ được hiển thị khi xem chi tiết guideline có sẵn decision tree.")

# Example: Show decision tree for heart failure guidelines
example_guideline_id = "acc_aha_heart_failure_2022"
if st.checkbox("Hiển thị ví dụ Decision Tree (Heart Failure)", key="show_example_tree"):
    render_guideline_decision_tree(example_guideline_id)

st.markdown("---")

# Footer
render_standard_footer()
