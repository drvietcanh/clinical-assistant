"""
Interactive Diagnostic Algorithms
Visual flowcharts for clinical decision trees
"""

import streamlit as st
from components.flowchart import (
    FlowchartNode,
    FlowchartEdge,
    NodeType,
    render_flowchart,
    create_chest_pain_algorithm,
    create_aki_algorithm,
    render_algorithm_selector,
    render_interactive_algorithm
)


def render_algorithms_page():
    """Render main algorithms page"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px 25px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(102,126,234,0.25);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: 700;'>🔄 Interactive Diagnostic Algorithms</h1>
        <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.15em;'>
            Visual flowcharts và decision trees hỗ trợ quyết định lâm sàng
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Tính năng mới:**
    - 📊 Visual flowcharts với color-coded nodes
    - 🖱️ Interactive hover effects
    - 🔄 Step-by-step decision trees
    - 📋 Clinical algorithms cho các scenarios phổ biến
    
    **Algorithms hiện có:**
    - Chest Pain Diagnostic Algorithm
    - Acute Kidney Injury (AKI) Algorithm
    - (Đang phát triển: Dyspnea, Sepsis, Anemia)
    """)
    
    st.markdown("---")
    
    # Algorithm selector
    selected = render_algorithm_selector()
    
    if selected:
        st.markdown("---")
        render_interactive_algorithm(selected)
    
    # Additional info
    with st.expander("ℹ️ Về Interactive Algorithms"):
        st.markdown("""
        **Interactive Diagnostic Algorithms** cung cấp:
        
        - **Visual Flowcharts**: Dễ theo dõi flow của algorithm
        - **Color Coding**: 
          - 🟢 Start/End nodes
          - 🟡 Decision points
          - 🔵 Actions
          - 🟣 Tests
          - 🔴 Critical actions
        
        - **Step-by-step guidance**: Hướng dẫn từng bước trong quyết định lâm sàng
        - **Evidence-based**: Dựa trên guidelines và best practices
        
        **Lưu ý:** Algorithms này chỉ mang tính tham khảo. Luôn điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.
        """)

