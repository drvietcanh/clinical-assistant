"""
Phác đồ hôn mê phù niêm (Myxedema Coma)
Hướng dẫn ATA 2014
Cấp cứu suy giáp đe dọa tính mạng
"""

import streamlit as st


def render():
    """Phác đồ hôn mê phù niêm (Myxedema Coma)"""
    st.subheader("❄️ Hôn Mê Phù Niêm (Myxedema Coma)")
    st.caption("Hướng dẫn ATA 2014 - Cấp cứu suy giáp đe dọa tính mạng")
    
    st.error("""
    **🚨 CẤP CỨU - Cần điều trị ngay lập tức**
    
    **Myxedema Coma là tình trạng cấp cứu đe dọa tính mạng, cần:**
    - Điều trị ngay tại ICU
    - Bổ sung hormone tuyến giáp ngay
    - Điều trị suy thượng thận kèm theo
    - Hỗ trợ hô hấp và tuần hoàn
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu Chuẩn Chẩn Đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Chẩn đoán Myxedema Coma khi có:**
        
        **1. Hôn mê hoặc giảm ý thức:**
        - Hôn mê (GCS <8)
        - Lú lẫn nặng
        - Giảm phản xạ
        
        **2. Dấu hiệu suy giáp nặng:**
        - Phù niêm (myxedema) - đặc biệt quanh mắt, mặt
        - Da khô, lạnh, vàng (carotenemia)
        - Tóc khô, rụng
        - Giọng nói khàn
        - Phản xạ chậm (delayed relaxation)
        
        **3. Hạ thân nhiệt:**
        - Nhiệt độ <35°C (thường 30-35°C)
        - Không đáp ứng với hạ sốt thông thường
        
        **4. Rối loạn tim mạch:**
        - Nhịp tim chậm (<60 bpm)
        - Huyết áp thấp
        - Suy tim
        - Xẹp tim (pericardial effusion)
        
        **5. Rối loạn hô hấp:**
        - Giảm thông khí (hypoventilation)
        - CO2 tăng (hypercapnia)
        - Có thể cần thở máy
        
        **6. Xác nhận suy giáp:**
        - TSH tăng cao (>20 mIU/L, thường >50)
        - Free T4 rất thấp
        - Có tiền sử suy giáp hoặc điều trị tuyến giáp trước đó
        """)
        
        st.warning("""
        **⚠️ Lưu ý:** 
        - Chẩn đoán chủ yếu dựa trên lâm sàng
        - Không cần chờ kết quả xét nghiệm để bắt đầu điều trị
        - Điều trị ngay khi nghi ngờ
        - Tỷ lệ tử vong cao (20-50%) nếu không điều trị kịp thời
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: RISK FACTORS ==========
    st.markdown("### 📊 Yếu Tố Nguy Cơ")
    
    st.markdown("""
    **Các yếu tố thúc đẩy Myxedema Coma:**
    
    - **Nhiễm trùng:** Nhiễm trùng hô hấp, tiết niệu
    - **Lạnh:** Tiếp xúc lạnh, mùa đông
    - **Thuốc:** 
      - Thuốc an thần, gây mê
      - Amiodarone
      - Lithium
      - Phenytoin, carbamazepine
    - **Phẫu thuật:** Stress phẫu thuật
    - **Ngừng thuốc:** Ngừng đột ngột levothyroxine
    - **Suy thượng thận:** Thường kèm theo
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Điều Trị Ngay Lập Tức (ICU)")
    
    st.markdown("""
    **Thứ tự ưu tiên điều trị (theo ATA 2014):**
    """)
    
    # Step 1: Supportive Care
    st.markdown("#### **1. Hồi Sức Hỗ Trợ (Supportive Care)**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **A. Hô hấp:**
        - **Oxygen:** Duy trì SpO2 >90%
        - **Thở máy:** Nếu giảm thông khí nặng, CO2 tăng
        - **Theo Dõi:** ABG, SpO2 liên tục
        
        **B. Tuần hoàn:**
        - **Dịch truyền:** NS 0.9% hoặc LR
        - **Vasopressors:** Nếu huyết áp thấp không đáp ứng dịch
          - Norepinephrine: 0.05-0.3 mcg/kg/min
        - **Theo Dõi:** Huyết áp, nhịp tim liên tục
        """)
    
    with col2:
        st.markdown("""
        **C. Hạ thân nhiệt:**
        - **Làm ấm từ từ:** Tránh làm ấm quá nhanh (có thể gây shock)
        - **Chăn ấm, sưởi ấm phòng**
        - **Dịch truyền ấm** (nếu có)
        - **Theo Dõi:** Nhiệt độ mỗi 1-2 giờ
        
        **D. Điều chỉnh điện giải:**
        - **Hyponatremia:** Thường gặp, điều chỉnh từ từ
        - **Hypoglycemia:** D5W hoặc D10W nếu cần
        """)
    
    # Step 2: Corticosteroids
    st.markdown("#### **2. Corticosteroids (QUAN TRỌNG - Điều Trị Trước Hormone Tuyến Giáp)**")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Luôn dùng Corticosteroids TRƯỚC khi dùng Levothyroxine**
    
    **Lý do:** 
    - Suy giáp nặng thường kèm suy thượng thận
    - Bổ sung hormone tuyến giáp có thể gây suy thượng thận cấp nếu không có steroids
    - Có thể gây tử vong nếu không điều trị
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Hydrocortisone (Lựa chọn hàng đầu):**
        
        **Liều:**
        - **Loading:** 100mg IV ngay
        - **Duy trì:** 50-100mg IV q8h
        - **Hoặc:** 100mg IV q6h
        
        **Thời gian:**
        - Dùng 3-5 ngày
        - Giảm dần khi ổn định
        - Có thể ngừng nếu không có suy thượng thận
        """)
    
    with col2:
        st.info("""
        **Dexamethasone (Thay thế):**
        
        **Liều:**
        - 2-4mg IV q6-8h
        
        **Lưu ý:**
        - Không có hoạt tính mineralocorticoid
        - Cần bổ sung fludrocortisone nếu cần
        """)
    
    # Step 3: Thyroid hormone replacement
    st.markdown("#### **3. Bổ Sung Hormone Tuyến Giáp (Levothyroxine)**")
    
    st.markdown("""
    **⚠️ Lưu ý:** Dùng SAU KHI đã dùng corticosteroids
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Levothyroxine IV (Lựa chọn hàng đầu):**
        
        **Liều loading:**
        - **200-500mcg IV x 1 lần** (liều cao ban đầu)
        - Hoặc 4-5 mcg/kg IV
        
        **Liều duy trì:**
        - **50-100mcg IV/ngày**
        - Chia 2 lần (sáng, chiều)
        
        **Chuyển sang PO:**
        - Khi bệnh nhân tỉnh, có thể uống
        - Liều tương đương: 75-150mcg PO/ngày
        """)
    
    with col2:
        st.info("""
        **Liothyronine (T3) - Tùy chọn:**
        
        **Chỉ Định:**
        - Bệnh nhân nặng, không đáp ứng
        - Cần tác dụng nhanh hơn
        
        **Liều:**
        - 10-20mcg IV q8-12h
        - Hoặc 25-50mcg PO q8-12h
        
        **Lưu ý:**
        - Tác dụng nhanh nhưng ngắn
        - Có thể gây loạn nhịp tim
        - Thường kết hợp với Levothyroxine
        """)
    
    st.markdown("""
    **Phác đồ kết hợp (Nếu cần tác dụng nhanh):**
    - **Levothyroxine:** 200-500mcg IV x 1, sau đó 50-100mcg/ngày
    - **Liothyronine:** 10-20mcg IV q8h x 2-3 ngày đầu
    """)
    
    # Step 4: Additional treatments
    st.markdown("#### **4. Điều Trị Bổ Sung**")
    
    st.markdown("""
    **A. Điều trị nhiễm trùng:**
    - Tìm và điều trị nhiễm trùng (nguyên nhân thúc đẩy)
    - Kháng sinh phổ rộng nếu nghi ngờ
    
    **B. Điều chỉnh điện giải:**
    - **Hyponatremia:** 
      - Nếu nhẹ: Hạn chế dịch
      - Nếu nặng: Dùng dung dịch muối ưu trương cẩn thận
      - Điều chỉnh từ từ (0.5-1 mEq/L/giờ)
    
    **C. Tránh thuốc:**
    - Tránh thuốc an thần, gây mê không cần thiết
    - Tránh thuốc làm chậm nhịp tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: MONITORING ==========
    st.markdown("### 📈 Theo Dõi")
    
    st.markdown("""
    **Theo dõi sát trong 24-48 giờ đầu:**
    
    **1. Dấu hiệu sinh tồn:**
    - **Nhiệt độ:** Mỗi 1-2 giờ (theo dõi hạ thân nhiệt)
    - **Nhịp tim:** Liên tục (monitor) - theo dõi loạn nhịp
    - **Huyết áp:** Mỗi 1-2 giờ
    - **Nhịp thở, SpO2:** Liên tục
    - **GCS:** Mỗi 2-4 giờ
    
    **2. Xét nghiệm:**
    - **TSH, Free T4:** Mỗi 24-48 giờ
    - **Cortisol:** Trước và sau điều trị (để xác định suy thượng thận)
    - **Điện giải:** Mỗi 6-12 giờ (đặc biệt Na)
    - **ABG:** Mỗi 6-12 giờ (theo dõi CO2)
    - **Công thức máu:** Mỗi 24 giờ
    
    **3. Dấu hiệu cải thiện:**
    - ✅ Nhiệt độ tăng về bình thường
    - ✅ Nhịp tim tăng, huyết áp ổn định
    - ✅ Tình trạng thần kinh cải thiện (GCS tăng)
    - ✅ TSH giảm, Free T4 tăng
    
    **4. Dấu hiệu cảnh báo:**
    - ⚠️ Nhiệt độ vẫn thấp
    - ⚠️ Huyết áp không ổn định
    - ⚠️ Tình trạng thần kinh không cải thiện
    - ⚠️ Loạn nhịp tim (do quá liều hormone)
    - 🚨 Sốc, ngừng tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Dân Số Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Giảm liều loading (200-300mcg thay vì 500mcg)
        - Theo dõi sát tim mạch
        - Điều chỉnh liều theo chức năng thận
        
        **Bệnh tim mạch:**
        - Giảm liều loading (100-200mcg)
        - Tăng liều từ từ
        - Theo dõi sát loạn nhịp tim
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - Điều chỉnh liều theo CrCl
        - Theo dõi điện giải sát
        
        **Suy gan:**
        - Cẩn thận với chuyển hóa hormone
        - Theo dõi chức năng gan
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: LONG-TERM MANAGEMENT ==========
    st.markdown("### 🔄 Điều Trị Dài Hạn")
    
    st.markdown("""
    **Sau khi qua giai đoạn cấp (3-5 ngày):**
    
    **1. Chuyển sang Levothyroxine PO:**
    - Liều: 75-150mcg PO/ngày (sáng đói)
    - Tăng dần mỗi 2-4 tuần
    - Mục tiêu: TSH 0.5-2.5 mIU/L
    
    **2. Giảm Corticosteroids:**
    - Giảm dần trong 5-7 ngày
    - Ngừng nếu không có suy thượng thận
    - Duy trì nếu có suy thượng thận
    
    **3. Theo dõi:**
    - **TSH, Free T4:** Mỗi 4-6 tuần
    - **Cortisol:** Nếu nghi ngờ suy thượng thận
    - **Tim mạch:** ECG, theo dõi triệu chứng
    
    **4. Điều chỉnh liều:**
    - Tăng liều mỗi 2-4 tuần nếu TSH còn cao
    - Mục tiêu: Đạt bình giáp trong 4-8 tuần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PROGNOSIS ==========
    st.markdown("### 📊 Tiên lượng")
    
    st.markdown("""
    **Tỷ lệ tử vong:**
    - **Không điều trị:** 50-80%
    - **Điều trị kịp thời:** 20-50%
    - **Điều trị sớm, đúng:** 10-20%
    
    **Yếu tố tiên lượng xấu:**
    - Tuổi cao
    - Hạ thân nhiệt nặng (<30°C)
    - Hôn mê sâu (GCS <5)
    - Suy tim, sốc
    - Nhiễm trùng nặng
    - Điều trị muộn
    
    **Yếu tố tiên lượng tốt:**
    - Điều trị sớm (<24 giờ)
    - Hạ thân nhiệt nhẹ (>32°C)
    - Tình trạng thần kinh còn tốt
    - Không có bệnh tim mạch nặng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **Hướng dẫn Hiệp hội Tuyến giáp Hoa Kỳ (ATA) về Suy giáp** - 2014
       - Quản lý hôn mê phù niêm
       - Tiêu chuẩn chẩn đoán và điều trị
    
    2. **Jonklaas J, et al.** Guidelines for the treatment of hypothyroidism.
       Thyroid. 2014;24(12):1670-1751.
    
    3. **UpToDate:** Hôn mê phù niêm - Cập nhật lần cuối 2024
       - Đặc điểm lâm sàng và chẩn đoán
       - Phác đồ điều trị
    
    4. **Wartofsky L.** Myxedema coma.
       Endocrinol Metab Clin North Am. 2006;35(4):687-698.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. Myxedema Coma là cấp cứu đe dọa tính mạng, cần điều trị tại ICU với theo dõi sát. Luôn dùng Corticosteroids trước khi dùng Levothyroxine.")

