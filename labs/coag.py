"""
Coagulation Panel
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Coagulation Panel"""
    st.subheader("🩸 Coagulation Panel - Đông Máu")
    st.caption("Xét nghiệm đánh giá chức năng đông máu và điều trị chống đông")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Nhập Kết Quả")
        
        pt = st.number_input(
            "PT - Prothrombin Time (giây)", 
            0.0, 100.0, 12.0, 0.1,
            help="Bình thường: 11-13.5 giây"
        )
        inr = st.number_input(
            "INR - International Normalized Ratio", 
            0.0, 10.0, 1.0, 0.1,
            help="Bình thường: 0.8-1.2"
        )
        aptt = st.number_input(
            "aPTT - activated Partial Thromboplastin Time (giây)", 
            0.0, 150.0, 30.0, 0.1,
            help="Bình thường: 25-35 giây"
        )
        d_dimer = st.number_input(
            "D-dimer (µg/mL hoặc FEU)", 
            0.0, 10.0, 0.3, 0.1,
            help="Bình thường: <0.5 µg/mL"
        )
    
    with col2:
        st.markdown("#### 📊 Giải Thích Kết Quả")
        
        # INR
        if inr < 1.2:
            st.success(f"**INR:** {inr} - Bình thường ✓")
        elif inr < 2.0:
            st.info(f"**INR:** {inr} - Tăng nhẹ")
        elif inr <= 3.5:
            st.success(f"**INR:** {inr} - Trong mục tiêu điều trị ✓")
            st.caption("→ Phù hợp cho đa số chỉ định chống đông")
        elif inr < 5:
            st.warning(f"**INR:** {inr} - Cao ⚠️")
            st.caption("→ Nguy cơ chảy máu tăng")
        else:
            st.error(f"**INR:** {inr} - CỰC KỲ CAO 🚨")
            st.caption("→ NGUY CƠ CHẢY MÁU NGHIÊM TRỌNG!")
        
        # aPTT
        if 25 <= aptt <= 35:
            st.success(f"**aPTT:** {aptt} giây - Bình thường ✓")
        elif aptt < 25:
            st.warning(f"**aPTT:** {aptt} giây - Ngắn")
            st.caption("→ Có thể tăng đông")
        elif aptt <= 80:
            st.warning(f"**aPTT:** {aptt} giây - Kéo dài")
            st.caption("→ Kiểm tra heparin level nếu đang dùng")
        else:
            st.error(f"**aPTT:** {aptt} giây - Kéo dài rõ rệt ⚠️")
            st.caption("→ Nguy cơ chảy máu, đánh giá ngay")
        
        # D-dimer
        if d_dimer < 0.5:
            st.success(f"**D-dimer:** {d_dimer} µg/mL - Bình thường ✓")
            st.caption("→ Loại trừ huyết khối tĩnh mạch")
        else:
            st.warning(f"**D-dimer:** {d_dimer} µg/mL - Tăng cao")
            st.caption("→ Cần đánh giá thêm (không đặc hiệu)")
    
    st.markdown("---")
    with st.expander("📚 Hướng Dẫn Diễn Giải"):
        st.markdown("""
        ### **INR - Mục Tiêu Điều Trị:**
        
        **Rung nhĩ (AF):**
        - Mục tiêu: **2.0 - 3.0**
        - Giảm nguy cơ đột quỵ
        
        **Van tim cơ học:**
        - Van hai lá (mitral): **2.5 - 3.5**
        - Van động mạch chủ (aortic): **2.0 - 3.0**
        
        **Huyết khối tĩnh mạch (DVT/PE):**
        - Mục tiêu: **2.0 - 3.0**
        - Thời gian: 3-6 tháng (tùy nguy cơ tái phát)
        
        ---
        
        ### **aPTT - Sử Dụng:**
        
        **Theo dõi Heparin không phân đoạn:**
        - Mục tiêu: **1.5 - 2.5 x baseline** (~ 60-80 giây)
        - Kiểm tra 6h sau thay đổi liều
        
        **Chẩn đoán:**
        - Kéo dài: thiếu yếu tố đông máu, kháng đông lupus, hemophilia
        - Ngắn: tăng đông máu
        
        ---
        
        ### **D-dimer - Ý Nghĩa:**
        
        **✅ Độ nhạy cao, ✅ giá trị dự đoán âm tính cao**
        - **D-dimer bình thường → Loại trừ VTE** (với xác suất tiền test thấp/trung bình)
        
        **❌ Độ đặc hiệu thấp**
        - Tăng trong: Huyết khối, DIC, phẫu thuật, chấn thương, ung thư, thai kỳ, nhiễm trùng, cao tuổi
        
        **Khi nào dùng:**
        - Wells score thấp/trung bình + D-dimer âm → Loại trừ VTE
        - Wells score cao → Chụp CTPA/US ngay, không cần D-dimer
        
        ---
        
        ### **Nguyên Tắc Giải Thích:**
        
        1. ✅ **INR** - Theo dõi Warfarin (đường uống)
        2. ✅ **aPTT** - Theo dõi Heparin (tiêm tĩnh mạch)
        3. ✅ **D-dimer** - Sàng lọc/loại trừ huyết khối
        4. ⚠️ **Luôn kết hợp lâm sàng** - Không chỉ dựa vào xét nghiệm!
        """)
    
    st.markdown("---")
    st.warning("""
    ⚠️ **Lưu ý quan trọng:**
    - **INR >5:** Nguy cơ chảy máu cao, xem xét giảm/ngừng Warfarin, cho Vitamin K
    - **aPTT kéo dài trên Heparin:** Điều chỉnh liều theo protocol
    - **D-dimer:** CHỈ dùng để loại trừ, KHÔNG dùng để chẩn đoán xác định VTE
    - **Luôn đánh giá nguy cơ chảy máu vs. nguy cơ huyết khối**
    """)
