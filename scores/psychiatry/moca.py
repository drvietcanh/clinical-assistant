"""
MoCA - Montreal Cognitive Assessment
Đánh giá nhận thức Montreal - Nhạy hơn MMSE với suy giảm nhận thức nhẹ
"""

import streamlit as st


def render():
    """Render MoCA calculator"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #7C3AED;'>🧠 MoCA - Montreal Cognitive Assessment</h2>
    <p style='text-align: center;'><em>Đánh giá nhận thức Montreal</em></p>
    """, unsafe_allow_html=True)
    
    # Introduction
    with st.expander("ℹ️ Giới thiệu về MoCA"):
        st.markdown("""
        **MoCA (Montreal Cognitive Assessment)** là công cụ đánh giá nhận thức nhanh.
        
        **Ưu điểm so với MMSE:**
        - ✅ Nhạy hơn với suy giảm nhận thức nhẹ (MCI)
        - ✅ Phát hiện tốt hơn với bệnh nhân giáo dục cao
        - ✅ Thời gian: 10-15 phút
        
        **Thang điểm:** 0-30 điểm
        
        **Điểm cắt:** < 26 → Suy giảm nhận thức (MCI hoặc Dementia)
        
        **Lưu ý:** 
        - Cộng 1 điểm nếu học ≤ 12 năm
        - Không cộng nếu học > 12 năm
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Nhập điểm từng phần")
    
    col1, col2 = st.columns(2)
    
    with col1:
        visuospatial = st.number_input(
            "Thị-không gian (0-5)",
            min_value=0,
            max_value=5,
            value=5,
            help="Vẽ khối lập phương, đồng hồ"
        )
        
        naming = st.number_input(
            "Đặt tên (0-3)",
            min_value=0,
            max_value=3,
            value=3,
            help="Đặt tên động vật"
        )
        
        attention = st.number_input(
            "Chú ý (0-6)",
            min_value=0,
            max_value=6,
            value=6,
            help="Đếm ngược, tính trừ, bắt chữ"
        )
        
        language = st.number_input(
            "Ngôn ngữ (0-3)",
            min_value=0,
            max_value=3,
            value=3,
            help="Nhắc lại câu, lưu loát"
        )
    
    with col2:
        abstraction = st.number_input(
            "Trừu tượng (0-2)",
            min_value=0,
            max_value=2,
            value=2,
            help="Tìm điểm chung"
        )
        
        memory = st.number_input(
            "Trí nhớ (0-5)",
            min_value=0,
            max_value=5,
            value=5,
            help="Nhắc lại 5 từ (2 lần), nhắc lại sau"
        )
        
        orientation = st.number_input(
            "Định hướng (0-6)",
            min_value=0,
            max_value=6,
            value=6,
            help="Ngày, tháng, năm, địa điểm"
        )
    
    st.markdown("---")
    
    # Education adjustment
    education = st.checkbox(
        "+1 điểm nếu học ≤ 12 năm",
        help="Điều chỉnh cho người có trình độ học vấn thấp"
    )
    
    # Calculate
    total = visuospatial + naming + attention + language + abstraction + memory + orientation
    
    if education:
        total += 1
    
    # Maximum is 30
    total = min(total, 30)
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Tính MoCA", type="primary", use_container_width=True):
        # Interpret score
        if total >= 26:
            status = "Bình thường"
            color = "#28a745"
            icon = "✅"
            interpretation = "Không có suy giảm nhận thức"
        else:
            status = "Suy giảm nhận thức"
            color = "#fd7e14"
            icon = "⚠️"
            if total >= 18:
                interpretation = "Suy giảm nhận thức nhẹ (MCI)"
            else:
                interpretation = "Suy giảm nhận thức nặng (Dementia)"
        
        # Display result
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} MoCA: {total}/30
            </h2>
            <p style='text-align: center; font-size: 1.2em; margin-top: 10px; font-weight: bold;'>
                {status}
            </p>
            <p style='text-align: center; margin-top: 10px;'>
                {interpretation}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Chi tiết
        st.markdown("### 📊 Chi tiết điểm:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            - **Thị-không gian:** {visuospatial}/5
            - **Đặt tên:** {naming}/3
            - **Chú ý:** {attention}/6
            - **Ngôn ngữ:** {language}/3
            """)
        
        with col2:
            st.markdown(f"""
            - **Trừu tượng:** {abstraction}/2
            - **Trí nhớ:** {memory}/5
            - **Định hướng:** {orientation}/6
            {"- **Điều chỉnh giáo dục:** +1" if education else ""}
            """)
        
        st.markdown(f"**Tổng điểm:** {total}/30")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Giải thích:")
        
        if total >= 26:
            st.success("""
            **✅ Bình thường (≥26 điểm)**
            
            - Không có bằng chứng suy giảm nhận thức
            - Nếu có triệu chứng, cân nhắc nguyên nhân khác
            - Theo dõi nếu có yếu tố nguy cơ
            """)
        else:
            st.warning(f"""
            **⚠️ Suy giảm nhận thức (<26 điểm)**
            
            **Điểm hiện tại: {total}/30**
            
            {"**Mức độ:** Nhẹ (MCI) - 18-25 điểm" if total >= 18 else "**Mức độ:** Nặng (Dementia) - <18 điểm"}
            
            **Bước tiếp theo:**
            - Đánh giá lâm sàng chi tiết hơn
            - Xét nghiệm máu (B12, TSH, HIV...)
            - Chẩn đoán hình ảnh (CT/MRI não)
            - Đánh giá chức năng hàng ngày
            - Hội chẩn thần kinh/nội khoa
            """)
        
        # Comparison with MMSE
        with st.expander("🔄 So sánh MoCA vs MMSE"):
            st.markdown("""
            | Đặc điểm | MoCA | MMSE |
            |:---------|:-----|:-----|
            | **Thang điểm** | 0-30 | 0-30 |
            | **Điểm cắt** | < 26 | < 24-27 |
            | **Độ nhạy MCI** | Cao hơn | Thấp hơn |
            | **Thời gian** | 10-15 phút | 5-10 phút |
            | **Bệnh nhân giáo dục cao** | Phù hợp hơn | Có thể bình thường giả |
            | **Giấy phép** | Miễn phí | Miễn phí |
            
            **Khuyến cáo:**
            - Dùng **MoCA** khi nghi ngờ suy giảm nhận thức nhẹ
            - Dùng **MMSE** cho sàng lọc nhanh
            - Dùng **cả hai** để đánh giá toàn diện
            """)
        
        # Clinical guidance
        with st.expander("📋 Hướng dẫn lâm sàng"):
            if total >= 26:
                st.markdown("""
                **Với điểm MoCA ≥ 26:**
                
                - Không có bằng chứng suy giảm nhận thức trên test này
                - Nếu vẫn có triệu chứng: đánh giá thêm
                - Theo dõi nếu có yếu tố nguy cơ (tuổi cao, đái tháo đường, tăng huyết áp)
                """)
            else:
                st.markdown(f"""
                **Với điểm MoCA {total}/30 (<26):**
                
                **1. Đánh giá nguyên nhân có thể điều chỉnh:**
                - Thiếu vitamin B12, folate
                - Suy giáp
                - Nhiễm trùng (HIV, giang mai)
                - Rối loạn tâm thần (trầm cảm)
                - Thuốc (anticholinergic, benzodiazepine)
                - Rượu
                
                **2. Chẩn đoán hình ảnh:**
                - CT/MRI não (tìm tổn thương, teo não)
                - Có thể cần PET scan
                
                **3. Đánh giá chức năng:**
                - ADL (Activities of Daily Living)
                - IADL (Instrumental ADL)
                - Bảng hỏi người thân
                
                **4. Hội chẩn:**
                - Thần kinh (nếu nghi ngờ Dementia)
                - Tâm thần (nếu có trầm cảm/lo âu)
                - Nội khoa (điều chỉnh yếu tố nguy cơ)
                
                **5. Theo dõi:**
                - Lặp lại MoCA sau 6-12 tháng
                - Đánh giá tiến triển
                """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Nasreddine ZS, Phillips NA, Bédirian V, et al.** The Montreal Cognitive Assessment, MoCA: 
               a brief screening tool for mild cognitive impairment. J Am Geriatr Soc. 2005;53(4):695-9.
            
            2. **Davis DH, Creavin ST, Noel-Storr A, et al.** Montreal Cognitive Assessment for the diagnosis 
               of Alzheimer's disease and other dementias. Cochrane Database Syst Rev. 2015;(10):CD010775.
            
            3. **Carson N, Leach L, Murphy KJ.** A re-examination of Montreal Cognitive Assessment (MoCA) cutoff scores. 
               Int J Geriatr Psychiatry. 2018;33(2):379-88.
            """)
    
    # Quick reference
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    - **MoCA ≥ 26:** Bình thường
    - **MoCA 18-25:** Suy giảm nhận thức nhẹ (MCI)
    - **MoCA < 18:** Suy giảm nhận thức nặng (Dementia)
    - **Điều Chỉnh:** +1 điểm nếu học ≤ 12 năm
    - **Thời gian:** 10-15 phút
    - **Nhạy hơn MMSE** với suy giảm nhận thức nhẹ
    """)


if __name__ == "__main__":
    render()
