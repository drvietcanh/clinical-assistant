"""
Cardiac Markers
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Cardiac Markers"""
    st.subheader("❤️ Cardiac Markers - Dấu Ấn Tim Mạch")
    st.caption("Xét nghiệm chẩn đoán nhồi máu cơ tim và suy tim")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Nhập Kết Quả")
        
        trop_i = st.number_input(
            "Troponin I (ng/mL)", 
            0.0, 10.0, 0.02, 0.01,
            help="Bình thường: <0.04 ng/mL"
        )
        bnp = st.number_input(
            "BNP - B-type Natriuretic Peptide (pg/mL)", 
            0.0, 5000.0, 50.0, 10.0,
            help="Bình thường: <100 pg/mL"
        )
        ckmb = st.number_input(
            "CK-MB - Creatine Kinase MB (ng/mL)", 
            0.0, 50.0, 2.0, 0.1,
            help="Bình thường: <5 ng/mL"
        )
    
    with col2:
        st.markdown("#### 📊 Giải Thích Kết Quả")
        
        # Troponin I
        if trop_i < 0.04:
            st.success(f"**Troponin I:** {trop_i} ng/mL - Bình thường ✓")
        else:
            st.error(f"**Troponin I:** {trop_i} ng/mL - TĂNG CAO ⚠️ (Gợi ý nhồi máu cơ tim)")
        
        # BNP
        if bnp < 100:
            st.success(f"**BNP:** {bnp} pg/mL - Bình thường ✓")
            st.caption("→ Suy tim không khả năng")
        elif bnp < 400:
            st.warning(f"**BNP:** {bnp} pg/mL - Ngưỡng biên")
            st.caption("→ Có thể suy tim")
        else:
            st.error(f"**BNP:** {bnp} pg/mL - Tăng cao")
            st.caption("→ Gợi ý suy tim")
        
        # CK-MB
        if ckmb < 5:
            st.success(f"**CK-MB:** {ckmb} ng/mL - Bình thường ✓")
        else:
            st.warning(f"**CK-MB:** {ckmb} ng/mL - Tăng cao")
            st.caption("→ Tổn thương cơ tim hoặc cơ vân")
    
    st.markdown("---")
    with st.expander("📚 Hướng Dẫn Diễn Giải"):
        st.markdown("""
        ### **Troponin I:**
        - **Tăng:** 3-4 giờ sau nhồi máu cơ tim
        - **Đỉnh:** 12-24 giờ
        - **Kéo dài:** 7-10 ngày
        - **Ý nghĩa:** Dấu ấn vàng chẩn đoán nhồi máu cơ tim cấp
        
        ### **BNP (B-type Natriuretic Peptide):**
        - **<100 pg/mL:** Suy tim không khả năng
        - **100-400 pg/mL:** Có thể suy tim, cần đánh giá thêm
        - **>400 pg/mL:** Rất có khả năng suy tim
        - **>900 pg/mL:** Suy tim nặng
        
        ### **CK-MB (Creatine Kinase MB):**
        - Kém đặc hiệu hơn Troponin
        - Có thể tăng trong: tổn thương cơ vân, phẫu thuật, chấn thương
        - Hiện nay ít dùng hơn, thay bằng Troponin
        
        ### **Nguyên Tắc Chung:**
        - ✅ **Luôn kết hợp với lâm sàng và ECG**
        - ✅ **Xét nghiệm serial** (0h, 3h, 6h) để theo dõi xu hướng
        - ✅ **Troponin âm tính không loại trừ ACS** nếu <3 giờ từ khởi phát
        """)
    
    st.markdown("---")
    st.warning("""
    ⚠️ **Lưu ý quan trọng:**
    - Kết quả chỉ có giá trị khi kết hợp với triệu chứng lâm sàng và ECG
    - Troponin có thể tăng trong: CKD, sepsis, tắc mạch phổi, viêm cơ tim
    - BNP có thể tăng trong: CKD, cao tuổi, béo phì giảm BNP
    """)
