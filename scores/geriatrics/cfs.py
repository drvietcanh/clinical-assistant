"""
Clinical Frailty Scale (CFS)
Đánh giá frailty (từ 1-9)
Quan trọng cho tiên lượng và quyết định điều trị
"""

import streamlit as st

def render_cfs(score_id: str = "CFS"):
    """Render Clinical Frailty Scale calculator"""
    
    st.markdown("### Clinical Frailty Scale (CFS)")
    st.markdown("**Đánh giá frailty ở bệnh nhân cao tuổi**")
    st.info("""
    **Clinical Frailty Scale** đánh giá mức độ frailty từ 1 (Very Fit) đến 9 (Terminally Ill).
    
    Quan trọng cho:
    - Tiên lượng bệnh nhân
    - Quyết định điều trị
    - Lập kế hoạch chăm sóc
    """)
    
    st.markdown("---")
    
    # CFS Levels
    st.markdown("#### Chọn mức độ Frailty")
    
    cfs_levels = {
        1: {
            "name": "1. Very Fit",
            "description": "Hoạt động thể chất tốt, năng động, nhiệt tình, thường xuyên tập thể dục"
        },
        2: {
            "name": "2. Well",
            "description": "Không có bệnh lý hoạt động, nhưng ít năng động hơn nhóm 1"
        },
        3: {
            "name": "3. Managing Well",
            "description": "Có bệnh lý được kiểm soát tốt, ít hoặc không có triệu chứng"
        },
        4: {
            "name": "4. Vulnerable",
            "description": "Có bệnh lý không hoạt động nhưng hoạt động thể chất giảm nhẹ"
        },
        5: {
            "name": "5. Mildly Frail",
            "description": "Nhu cầu hỗ trợ nhẹ trong hoạt động hàng ngày (IADL)"
        },
        6: {
            "name": "6. Moderately Frail",
            "description": "Cần hỗ trợ trong cả IADL và một số ADL (tắm, mặc quần áo)"
        },
        7: {
            "name": "7. Severely Frail",
            "description": "Phụ thuộc hoàn toàn vào người khác trong ADL, vẫn ổn định"
        },
        8: {
            "name": "8. Very Severely Frail",
            "description": "Hoàn toàn phụ thuộc, gần cuối đời"
        },
        9: {
            "name": "9. Terminally Ill",
            "description": "Bệnh nhân giai đoạn cuối, tiên lượng < 6 tháng"
        }
    }
    
    selected_level = st.selectbox(
        "Mức độ Frailty:",
        options=list(cfs_levels.keys()),
        format_func=lambda x: cfs_levels[x]["name"],
        key="cfs_level"
    )
    
    st.markdown(f"**Mô tả:** {cfs_levels[selected_level]['description']}")
    
    st.markdown("---")
    
    # Interpretation
    st.markdown("#### Interpretation")
    
    if selected_level <= 3:
        st.success("**Fit to Managing Well (1-3)**: Bệnh nhân có thể trạng tốt")
        st.markdown("""
        - Tiên lượng tốt
        - Có thể chịu đựng điều trị tích cực
        - Phù hợp cho phẫu thuật và thủ thuật
        """)
    elif selected_level <= 5:
        st.warning("**Vulnerable to Mildly Frail (4-5)**: Cần đánh giá cẩn thận")
        st.markdown("""
        - Cân nhắc điều trị, có thể cần điều chỉnh
        - Tăng nguy cơ biến chứng
        - Cần theo dõi sát
        """)
    elif selected_level <= 7:
        st.error("**Moderately to Severely Frail (6-7)**: Frailty nặng")
        st.markdown("""
        - Tiên lượng xấu
        - Cần cân nhắc goals of care
        - Có thể không phù hợp cho điều trị tích cực
        - Ưu tiên chất lượng cuộc sống
        """)
    else:
        st.error("**Very Severely Frail to Terminally Ill (8-9)**: Frailty rất nặng / Giai đoạn cuối")
        st.markdown("""
        - Tiên lượng rất xấu
        - Nên tập trung vào chăm sóc giảm nhẹ
        - Thảo luận goals of care với bệnh nhân và gia đình
        """)
    
    st.markdown("---")
    
    # References
    st.markdown("#### References")
    st.markdown("""
    - Rockwood K, et al. A global clinical measure of fitness and frailty in elderly people. CMAJ. 2005;173(5):489-495.
    - Clinical Frailty Scale Version 2.0. Dalhousie University.
    """)
