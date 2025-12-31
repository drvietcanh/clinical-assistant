import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

def render_homepage_doctor():
    """
    Renders the modern "Smart Dashboard" for doctors (2025 Design)
    """
    
    # 1. Greeting & Date
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Chào buổi sáng"
    elif 12 <= current_hour < 18:
        greeting = "Chào buổi chiều"
    else:
        greeting = "Chào buổi tối"
        
    date_str = datetime.now().strftime("%d tháng %m, %Y")
    
    st.markdown(f"""
    <div style="margin-bottom: 2rem;">
        <p style="color: #546e7a; font-size: 0.9rem; margin-bottom: 0;">{date_str}</p>
        <h1 style="color: #00897B; font-size: 2.2rem; margin-top: 0;">{greeting}, Bác sĩ</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Morning Briefing (Fake Data for Phase 1)
    st.markdown("### 🌅 Điểm tin sáng")
    st.info("""
    **Cập nhật mới:**
    - 📘 **Guideline 2025:** Đã cập nhật phác đồ điều trị Tăng huyết áp theo JNC 9.
    - 💊 **Thuốc mới:** Thêm dữ liệu về *SGLT2 inhibitors* trong suy tim.
    - ⚠️ **Cảnh báo:** Lưu ý tương tác thuốc giữa *Clarithromycin* và *Simvastatin*.
    """)
    
    st.markdown("---")
    
    # 3. Quick Actions (Grid Layout)
    st.markdown("### ⚡ Tác vụ nhanh")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔢 Tính CrCl", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")
            
    with col2:
        if st.button("💊 Liều Kháng Sinh", use_container_width=True):
            st.switch_page("pages/02_💊_Antibiotics.py")
            
    with col3:
        if st.button("⚠️ Tương tác thuốc", use_container_width=True):
             st.switch_page("pages/07_💊_Drug_Database.py")
             
    with col4:
        if st.button("📋 Phác đồ Cấp cứu", use_container_width=True):
            st.switch_page("pages/09_🫁_Critical_Care.py")
            
    st.markdown("---")
