"""
Score Links Component
Link to existing scores in the scores module
"""

import streamlit as st


def render_score_link(score_name: str, score_id: str, specialty: str, description: str = ""):
    """
    Render a link button to an existing score.
    
    Args:
        score_name: Display name of the score
        score_id: ID used in scores module
        specialty: Specialty name
        description: Optional description
    """
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"**{score_name}**")
        if description:
            st.caption(description)
    
    with col2:
        if st.button("🔗 Mở", key=f"link_{score_id}", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")
            # Note: The page will need to auto-select the score
            st.session_state['auto_select_score'] = score_id
            st.session_state['auto_select_specialty'] = specialty


def render_gcs_link():
    """Render link to GCS Calculator."""
    st.markdown("### 🧠 Glasgow Coma Scale (GCS)")
    st.info("""
    **GCS Calculator đã có sẵn trong Scores module.**
    
    **Truy cập:**
    1. Vào **Scores** page
    2. Chọn **🧠 Thần kinh (Neurology)**
    3. Chọn **GCS - Thang điểm hôn mê Glasgow**
    """)
    
    if st.button("🔗 Mở GCS Calculator", key="link_gcs", type="primary", use_container_width=True):
        st.switch_page("pages/01_📊_Scores.py")
        st.session_state['auto_select_score'] = "GCS"
        st.session_state['auto_select_specialty'] = "🧠 Thần kinh (Neurology)"


def render_rass_link():
    """Render link to RASS Calculator."""
    st.markdown("### 😴 Richmond Agitation-Sedation Scale (RASS)")
    st.info("""
    **RASS Calculator đã có sẵn trong Scores module.**
    
    **Truy cập:**
    1. Vào **Scores** page
    2. Chọn **🔪 Phẫu thuật (Surgery)**
    3. Chọn **RASS - Richmond Agitation-Sedation Scale**
    """)
    
    if st.button("🔗 Mở RASS Calculator", key="link_rass", type="primary", use_container_width=True):
        st.switch_page("pages/01_📊_Scores.py")
        st.session_state['auto_select_score'] = "RASS"
        st.session_state['auto_select_specialty'] = "🔪 Phẫu thuật (Surgery)"


def render_anion_gap_link():
    """Render link to Anion Gap Calculator."""
    st.markdown("### 🧪 Anion Gap Calculator")
    st.info("""
    **Anion Gap Calculator đã có sẵn trong Scores module.**
    
    **Truy cập:**
    1. Vào **Scores** page
    2. Chọn **🧪 Chuyển hóa (Metabolism)**
    3. Chọn **Anion Gap**
    """)
    
    if st.button("🔗 Mở Anion Gap Calculator", key="link_anion_gap", type="primary", use_container_width=True):
        st.switch_page("pages/01_📊_Scores.py")
        st.session_state['auto_select_score'] = "Anion Gap"
        st.session_state['auto_select_specialty'] = "🧪 Chuyển hóa (Metabolism)"


def render_qtc_link():
    """Render link to QTc Calculator."""
    st.markdown("### ❤️ QTc - Corrected QT Interval")
    st.info("""
    **QTc Calculator đã có sẵn trong Scores module.**
    
    **Truy cập:**
    1. Vào **Scores** page
    2. Chọn **❤️ Tim mạch (Cardiology)**
    3. Chọn **Corrected QT - QTc Interval**
    
    **Tính năng:**
    - 4 công thức: Bazett, Fridericia, Framingham, Hodges
    - Đánh giá nguy cơ Torsades
    - Danh sách thuốc gây kéo dài QT
    """)
    
    if st.button("🔗 Mở QTc Calculator", key="link_qtc", type="primary", use_container_width=True):
        st.switch_page("pages/01_📊_Scores.py")
        st.session_state['auto_select_score'] = "Corrected QT"
        st.session_state['auto_select_specialty'] = "❤️ Tim mạch (Cardiology)"


def render_sofa_link():
    """Render link to SOFA Score."""
    st.markdown("### 🫁 SOFA Score")
    st.info("""
    **SOFA Score đã có sẵn trong Scores module.**
    
    **Truy cập:**
    1. Vào **Scores** page
    2. Chọn **🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)**
    3. Chọn **SOFA** hoặc **SOFA-2 (2025)** ⭐
    
    **SOFA-2 (2025) có ưu điểm:**
    - Cập nhật với big data 2025
    - Hỗ trợ HFNC, ECMO, RRT
    - Độ chính xác cao hơn SOFA gốc
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔗 Mở SOFA", key="link_sofa", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")
            st.session_state['auto_select_score'] = "SOFA"
            st.session_state['auto_select_specialty'] = "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)"
    
    with col2:
        if st.button("🔗 Mở SOFA-2 (2025) ⭐", key="link_sofa2", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")
            st.session_state['auto_select_score'] = "SOFA-2 (2025)"
            st.session_state['auto_select_specialty'] = "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)"

