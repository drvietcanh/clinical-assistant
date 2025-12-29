"""
Clinical Guidelines Tracker Module
Track and monitor clinical practice guidelines updates
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from guidelines.tracker import (
    get_all_guidelines,
    get_guidelines_by_category,
    get_guidelines_by_organization,
    search_guidelines,
    get_recent_guidelines,
    check_guideline_updates,
    get_guideline_info
)
from guidelines.data import get_category_list, get_organization_list

# Standard page setup
setup_page(
    page_title="Theo dõi Guidelines",
    page_icon="📋",
    description="Theo dõi và cập nhật các hướng dẫn thực hành lâm sàng"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Theo dõi Guidelines")
    st.caption("Module **Theo dõi Guidelines** – theo dõi các hướng dẫn thực hành lâm sàng.")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Tất cả", "Gần đây", "Cần cập nhật", "Tìm kiếm"],
        key="guidelines_view_mode"
    )
    
    # Filters
    if view_mode == "Tất cả":
        category_filter = st.selectbox(
            "Lọc theo chuyên khoa:",
            ["Tất cả"] + get_category_list(),
            key="guidelines_category_filter"
        )
        
        org_filter = st.selectbox(
            "Lọc theo tổ chức:",
            ["Tất cả"] + get_organization_list(),
            key="guidelines_org_filter"
        )
    
    st.markdown("---")
    st.info("""
    **📋 Guidelines Tracker:**
    - Theo dõi **guidelines** từ các tổ chức uy tín
    - **AHA/ACC**, **ESC**, **IDSA**, **KDIGO**, **GOLD**, **GINA**, etc.
    - Liên kết với **protocols** trong app
    - Cảnh báo guidelines **cần cập nhật**
    
    **💡 Lưu ý:**
    - Guidelines được cập nhật thường xuyên
    - Luôn tham khảo phiên bản mới nhất
    - Click vào link để xem guideline đầy đủ
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 📋 Theo dõi Guidelines")
st.markdown("""
**Theo dõi và cập nhật các hướng dẫn thực hành lâm sàng từ các tổ chức uy tín**

Guidelines từ: AHA/ACC, ESC, IDSA, KDIGO, GOLD, GINA, SSC, ADA, và nhiều tổ chức khác
""")

# Display based on view mode
if view_mode == "Tất cả":
    st.markdown("### 📚 Tất cả Guidelines")
    
    # Apply filters
    category = None if category_filter == "Tất cả" else category_filter
    org = None if org_filter == "Tất cả" else org_filter
    
    if category:
        guidelines = get_guidelines_by_category(category)
    elif org:
        guidelines = get_guidelines_by_organization(org)
    else:
        guidelines = get_all_guidelines()
    
    if org and category:
        # Filter by both
        guidelines = [g for g in guidelines if org in g.organization]
    
    if guidelines:
        st.success(f"✅ Tìm thấy {len(guidelines)} guidelines")
        
        # Display guidelines
        for guideline in guidelines:
            with st.expander(f"**{guideline.title_vn}** ({guideline.year})", expanded=False):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Tổ chức:** {guideline.organization}")
                    st.markdown(f"**Năm:** {guideline.year}")
                    st.markdown(f"**Phiên bản:** {guideline.version}")
                    st.markdown(f"**Chuyên khoa:** {guideline.category}")
                with col2:
                    if guideline.last_updated:
                        st.markdown(f"**Cập nhật:** {guideline.last_updated}")
                    if guideline.url:
                        st.markdown(f"[🔗 Xem guideline đầy đủ]({guideline.url})")
                    if guideline.related_protocol:
                        st.markdown(f"**Protocol liên quan:** {guideline.related_protocol}")
                
                if guideline.description:
                    st.markdown(f"**Mô tả:** {guideline.description}")
                
                if guideline.key_recommendations:
                    st.markdown("**Khuyến nghị chính:**")
                    for rec in guideline.key_recommendations:
                        st.markdown(f"- {rec}")
    else:
        st.warning("Không tìm thấy guidelines với bộ lọc đã chọn.")

elif view_mode == "Gần đây":
    st.markdown("### 🆕 Guidelines Gần Đây")
    
    recent = get_recent_guidelines(limit=20, min_year=2020)
    
    if recent:
        st.success(f"✅ Tìm thấy {len(recent)} guidelines gần đây (từ 2020)")
        
        for guideline in recent:
            with st.expander(f"**{guideline.title_vn}** ({guideline.year})", expanded=False):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Tổ chức:** {guideline.organization}")
                    st.markdown(f"**Năm:** {guideline.year}")
                    st.markdown(f"**Chuyên khoa:** {guideline.category}")
                with col2:
                    if guideline.url:
                        st.markdown(f"[🔗 Xem guideline đầy đủ]({guideline.url})")
                    if guideline.related_protocol:
                        st.markdown(f"**Protocol liên quan:** {guideline.related_protocol}")
                
                if guideline.description:
                    st.markdown(f"**Mô tả:** {guideline.description}")
    else:
        st.warning("Không tìm thấy guidelines gần đây.")

elif view_mode == "Cần cập nhật":
    st.markdown("### ⚠️ Guidelines Cần Cập Nhật")
    st.info("Guidelines cũ hơn 2020 có thể cần được cập nhật. Vui lòng kiểm tra phiên bản mới nhất.")
    
    old_guidelines = check_guideline_updates(year_threshold=2020)
    
    if old_guidelines:
        st.warning(f"⚠️ Tìm thấy {len(old_guidelines)} guidelines có thể cần cập nhật")
        
        for guideline in old_guidelines:
            with st.expander(f"**{guideline.title_vn}** ({guideline.year}) ⚠️", expanded=False):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Tổ chức:** {guideline.organization}")
                    st.markdown(f"**Năm:** {guideline.year} ⚠️")
                    st.markdown(f"**Chuyên khoa:** {guideline.category}")
                with col2:
                    if guideline.url:
                        st.markdown(f"[🔗 Kiểm tra cập nhật]({guideline.url})")
                    if guideline.related_protocol:
                        st.markdown(f"**Protocol liên quan:** {guideline.related_protocol}")
                
                st.info("💡 Vui lòng kiểm tra website của tổ chức để xem phiên bản mới nhất.")
    else:
        st.success("✅ Tất cả guidelines đều gần đây (từ 2020 trở lên).")

else:  # Tìm kiếm
    st.markdown("### 🔍 Tìm kiếm Guidelines")
    
    search_query = st.text_input(
        "Nhập từ khóa tìm kiếm:",
        placeholder="Ví dụ: Heart failure, Sepsis, Diabetes...",
        key="guidelines_search_query"
    )
    
    if search_query:
        results = search_guidelines(search_query)
        
        if results:
            st.success(f"✅ Tìm thấy {len(results)} kết quả")
            
            for guideline in results:
                with st.expander(f"**{guideline.title_vn}** ({guideline.year})", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Tổ chức:** {guideline.organization}")
                        st.markdown(f"**Năm:** {guideline.year}")
                        st.markdown(f"**Chuyên khoa:** {guideline.category}")
                    with col2:
                        if guideline.url:
                            st.markdown(f"[🔗 Xem guideline đầy đủ]({guideline.url})")
                        if guideline.related_protocol:
                            st.markdown(f"**Protocol liên quan:** {guideline.related_protocol}")
                    
                    if guideline.description:
                        st.markdown(f"**Mô tả:** {guideline.description}")
        else:
            st.warning("Không tìm thấy kết quả. Vui lòng thử lại với từ khóa khác.")

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Guidelines")
st.markdown("""
**Các tổ chức guidelines chính:**

1. **AHA/ACC** - American Heart Association / American College of Cardiology
   - Cardiology guidelines (Heart failure, ACS, Hypertension, Atrial fibrillation)

2. **ESC** - European Society of Cardiology
   - European cardiology guidelines

3. **IDSA** - Infectious Diseases Society of America
   - Infectious diseases guidelines (Pneumonia, Sepsis)

4. **KDIGO** - Kidney Disease: Improving Global Outcomes
   - Nephrology guidelines (AKI, CKD)

5. **GOLD** - Global Initiative for Chronic Obstructive Lung Disease
   - COPD guidelines

6. **GINA** - Global Initiative for Asthma
   - Asthma guidelines

7. **SSC** - Surviving Sepsis Campaign
   - Sepsis and septic shock guidelines

8. **ADA** - American Diabetes Association
   - Diabetes guidelines

**Lưu ý:**
- Guidelines được cập nhật thường xuyên
- Luôn tham khảo phiên bản mới nhất từ website chính thức
- Một số guidelines có thể có phiên bản cập nhật không được liệt kê ở đây
- Click vào link để xem guideline đầy đủ và phiên bản mới nhất
""")

# Footer
render_standard_footer(disclaimer=True)

