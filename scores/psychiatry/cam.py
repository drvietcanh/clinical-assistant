"""
CAM - Confusion Assessment Method
Đánh giá hôn mê lú lẫn (Delirium)
"""

import streamlit as st

def render():
    st.markdown("<h2 style='text-align: center; color: #7C3AED;'>🧠 CAM - Confusion Assessment Method</h2><p style='text-align: center;'><em>Chẩn đoán Delirium</em></p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu CAM"):
        st.markdown("""
        **CAM** chẩn đoán delirium dựa trên 4 tiêu chí.
        
        **Chẩn đoán Delirium:** Cần có cả:
        - Tiêu chí 1 (Khởi phát cấp + dao động) VÀ
        - Tiêu chí 2 (Giảm chú ý) VÀ
        - Tiêu chí 3 (Tư duy rối loạn) HOẶC 4 (Ý thức thay đổi)
        """)
    
    st.markdown("---")
    
    feature1 = st.checkbox("**1. Khởi phát cấp và dao động**\n\nCó thay đổi cấp tính trạng thái tâm thần so với baseline? Có dao động trong ngày không?")
    feature2 = st.checkbox("**2. Giảm chú ý**\n\nKhó tập trung, dễ bị phân tâm, khó theo dõi câu chuyện?")
    feature3 = st.checkbox("**3. Tư duy rối loạn**\n\nSuy nghĩ không mạch lạc, câu chuyện lan man, ý tưởng không rõ ràng?")
    feature4 = st.checkbox("**4. Thay đổi mức độ ý thức**\n\nTỉnh táo bình thường / Li bì / Lơ mơ / Hôn mê")
    
    st.markdown("---")
    
    if st.button("🔬 Đánh giá CAM", type="primary", use_container_width=True):
        has_delirium = feature1 and feature2 and (feature3 or feature4)
        
        if has_delirium:
            st.error("""
            🚨 **DƯƠNG TÍNH - Chẩn đoán DELIRIUM**
            
            **Đáp ứng đủ tiêu chí CAM:**
            - ✅ Tiêu chí 1: Khởi phát cấp + dao động
            - ✅ Tiêu chí 2: Giảm chú ý
            - ✅ Tiêu chí 3 hoặc 4
            
            **Xử trí:**
            1. Tìm nguyên nhân (nhiễm trùng, thuốc, rối loạn chuyển hóa...)
            2. Điều trị nguyên nhân
            3. Không dùng thuốc (trừ kích động nguy hiểm)
            4. Định hướng lại, môi trường yên tĩnh
            5. Huy động gia đình
            """)
        else:
            st.success("""
            ✅ **ÂM TÍNH - Không đủ tiêu chí Delirium**
            
            Không đáp ứng tiêu chí CAM. Tuy nhiên:
            - Theo dõi tiếp
            - Đánh giá lại nếu có thay đổi
            - Cân nhắc nguyên nhân khác của thay đổi tâm thần
            """)
        
        with st.expander("📋 Phân loại Delirium"):
            st.markdown("""
            **3 kiểu delirium:**
            - **Hyperactive:** Kích động, ảo giác
            - **Hypoactive:** Lơ mơ, ít nói (dễ bỏ sót)
            - **Mixed:** Kết hợp
            """)

if __name__ == "__main__":
    render()

