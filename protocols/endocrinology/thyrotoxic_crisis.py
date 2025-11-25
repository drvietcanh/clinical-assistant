"""
Phác đồ cơn bão giáp (Thyrotoxic Crisis)
Hướng dẫn ATA 2016
Cấp cứu đe dọa tính mạng cần điều trị ngay lập tức
"""

import streamlit as st


def render():
    """Phác đồ cơn bão giáp (Thyrotoxic Crisis)"""
    st.subheader("⚡ Cơn Bão Giáp (Thyrotoxic Crisis)")
    st.caption("Hướng dẫn ATA 2016 - Cấp cứu cường giáp đe dọa tính mạng")
    
    st.error("""
    **🚨 CẤP CỨU - Cần điều trị ngay lập tức**
    
    **Thyrotoxic Crisis là tình trạng cấp cứu đe dọa tính mạng, cần:**
    - Điều trị ngay tại ICU
    - Phối hợp nhiều thuốc
    - Theo dõi sát các dấu hiệu sinh tồn
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu Chuẩn Chẩn Đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Chẩn đoán Thyrotoxic Crisis khi có:**
        
        **1. Nhiệt độ cơ thể:**
        - Sốt cao >38.5°C (thường >39°C)
        - Không đáp ứng với hạ sốt thông thường
        
        **2. Triệu chứng thần kinh:**
        - Lú lẫn, kích động, mê sảng
        - Hôn mê (trong trường hợp nặng)
        - Co giật (hiếm)
        
        **3. Tim mạch:**
        - Nhịp tim nhanh >130 bpm
        - Rung nhĩ hoặc loạn nhịp khác
        - Suy tim cấp
        - Sốc tim
        
        **4. Rối loạn tiêu hóa:**
        - Nôn, buồn nôn
        - Tiêu chảy
        - Vàng da (suy gan)
        
        **5. Xác nhận cường giáp:**
        - TSH rất thấp (<0.01 mIU/L)
        - Free T4 và/hoặc Free T3 tăng cao
        - Có tiền sử cường giáp hoặc bệnh Graves
        """)
        
        st.warning("""
        **⚠️ Lưu ý:** 
        - Chẩn đoán chủ yếu dựa trên lâm sàng
        - Không cần chờ kết quả xét nghiệm để bắt đầu điều trị
        - Điều trị ngay khi nghi ngờ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: BWS SCORE (OPTIONAL) ==========
    st.markdown("### 📊 Burch-Wartofsky Point Scale (BWPS)")
    
    with st.expander("🔢 Tính điểm BWPS (tùy chọn)", expanded=False):
        st.markdown("""
        **Hệ thống điểm để đánh giá mức độ nghiêm trọng:**
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**1. Nhiệt độ (°C):**")
            temp = st.number_input("Nhiệt độ:", min_value=35.0, max_value=45.0, value=37.0, step=0.1, format="%.1f", key="thyrotoxic_temp")
            temp_score = 0
            if temp >= 37.2 and temp < 37.8:
                temp_score = 5
            elif temp >= 37.8 and temp < 38.3:
                temp_score = 10
            elif temp >= 38.3 and temp < 38.9:
                temp_score = 15
            elif temp >= 38.9 and temp < 39.4:
                temp_score = 20
            elif temp >= 39.4 and temp < 40:
                temp_score = 25
            elif temp >= 40:
                temp_score = 30
            
            st.caption(f"Điểm nhiệt độ: {temp_score}")
        
        with col2:
            st.markdown("**2. Rối loạn thần kinh:**")
            neuro = st.selectbox(
                "Mức độ:",
                ["Bình thường", "Kích động nhẹ", "Lú lẫn", "Mê sảng", "Co giật", "Hôn mê"],
                key="thyrotoxic_neuro"
            )
            neuro_scores = {
                "Bình thường": 0,
                "Kích động nhẹ": 10,
                "Lú lẫn": 20,
                "Mê sảng": 30,
                "Co giật": 40,
                "Hôn mê": 50
            }
            neuro_score = neuro_scores.get(neuro, 0)
            st.caption(f"Điểm thần kinh: {neuro_score}")
        
        hr = st.number_input("Nhịp tim (bpm):", min_value=60, max_value=250, value=80, format="%d", key="thyrotoxic_hr")
        hr_score = 0
        if hr >= 99 and hr < 109:
            hr_score = 5
        elif hr >= 109 and hr < 119:
            hr_score = 10
        elif hr >= 119 and hr < 129:
            hr_score = 15
        elif hr >= 129 and hr < 139:
            hr_score = 20
        elif hr >= 139:
            hr_score = 25
        
        st.caption(f"Điểm nhịp tim: {hr_score}")
        
        afib = st.checkbox("Rung nhĩ", key="thyrotoxic_afib")
        afib_score = 10 if afib else 0
        
        chf = st.checkbox("Suy tim", key="thyrotoxic_chf")
        chf_score = 5 if chf else 0
        
        gi = st.selectbox(
            "Triệu chứng tiêu hóa:",
            ["Không có", "Tiêu chảy", "Nôn/buồn nôn", "Vàng da"],
            key="thyrotoxic_gi"
        )
        gi_scores = {
            "Không có": 0,
            "Tiêu chảy": 10,
            "Nôn/buồn nôn": 15,
            "Vàng da": 20
        }
        gi_score = gi_scores.get(gi, 0)
        
        total_score = temp_score + neuro_score + hr_score + afib_score + chf_score + gi_score
        
        st.markdown("---")
        st.markdown(f"### **Tổng điểm BWPS: {total_score}**")
        
        if total_score < 25:
            st.success("✅ **Không phải Thyroid Storm** - Cường giáp nặng")
        elif total_score < 45:
            st.warning("⚠️ **Nghi ngờ Thyroid Storm** - Cần điều trị tích cực")
        else:
            st.error("🚨 **Thyroid Storm xác định** - Cần điều trị cấp cứu ngay")
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Điều trị ngay lập tức (ICU)")
    
    st.markdown("""
    **Thứ tự ưu tiên điều trị (theo ATA 2016):**
    """)
    
    # Step 1: Supportive Care
    st.markdown("#### **1. Hồi sức hỗ trợ (Supportive Care)**")
    st.markdown("""
    - **Oxygen:** Duy trì SpO2 >90%
    - **Dịch truyền:** NS 0.9% hoặc LR, bù dịch theo nhu cầu
    - **Hạ sốt:** 
      - Paracetamol 1g IV q6h (tránh aspirin - có thể tăng T3/T4)
      - Làm mát ngoài (cooling blanket)
    - **Điều chỉnh điện giải:** Theo kết quả xét nghiệm
    """)
    
    # Step 2: Beta-blockers
    st.markdown("#### **2. Beta-Blockers (Ưu tiên cao nhất)**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Propranolol (Lựa chọn hàng đầu):**
        
        **Liều:**
        - 60-80mg PO q4-6h
        - Hoặc 1-2mg IV chậm, lặp lại q15-30 phút đến khi đạt nhịp tim mục tiêu
        
        **Mục Tiêu:**
        - Nhịp tim <100 bpm
        - Giảm triệu chứng tim mạch
        
        **Lưu ý:**
        - Chống chỉ định: Suy tim nặng, hen phế quản
        - Theo dõi: Huyết áp, nhịp tim, dấu hiệu suy tim
        """)
    
    with col2:
        st.info("""
        **Esmolol (Nếu cần tác dụng nhanh, ngắn):**
        
        **Liều:**
        - 50-100 mcg/kg/min IV (truyền liên tục)
        - Tăng dần đến khi đạt nhịp tim mục tiêu
        
        **Ưu điểm:**
        - Tác dụng nhanh, ngắn
        - Dễ điều chỉnh liều
        - An toàn hơn trong suy tim
        """)
    
    # Step 3: Antithyroid drugs
    st.markdown("#### **3. Thuốc kháng giáp (Antithyroid Drugs)**")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: Dùng PTU (Propylthiouracil) thay vì Methimazole trong Thyroid Storm**
    
    **Lý do:** PTU ức chế cả chuyển đổi T4→T3 (ngoài ức chế tổng hợp hormone)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **PTU (Propylthiouracil) - Lựa chọn hàng đầu:**
        
        **Liều:**
        - 600-1000mg PO/NG đầu tiên
        - Sau đó 200-250mg PO q4-6h
        - Tổng liều: 1200-1500mg/ngày
        
        **Cách dùng:**
        - Nếu không uống được: Nghiền, trộn với nước, bơm qua ống thông dạ dày
        - Hoặc dùng dạng viên nhỏ (nếu có)
        
        **Theo Dõi:**
        - Công thức máu (giảm bạch cầu)
        - Chức năng gan (độc gan)
        """)
    
    with col2:
        st.info("""
        **Methimazole (Nếu không có PTU):**
        
        **Liều:**
        - 60-80mg PO/NG đầu tiên
        - Sau đó 20-30mg PO q6-8h
        
        **Lưu ý:**
        - Không ức chế chuyển đổi T4→T3
        - Cần kết hợp với thuốc khác để ức chế chuyển đổi
        """)
    
    # Step 4: Iodine
    st.markdown("#### **4. Iodine (Ức chế giải phóng hormone)**")
    
    st.markdown("""
    **⚠️ QUAN TRỌNG: Chỉ dùng Iodine SAU KHI đã dùng thuốc kháng giáp ≥1 giờ**
    
    **Lý do:** Nếu dùng trước, Iodine có thể làm tăng tổng hợp hormone (Jod-Basedow effect)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Lugol's Solution (Iodine 5% + KI 10%):**
        
        **Liều:**
        - 5-10 giọt PO q6-8h
        - Hoặc 0.5-1ml PO q6-8h
        
        **Thời gian:**
        - Dùng 7-10 ngày
        - Ngừng khi đạt bình giáp
        """)
    
    with col2:
        st.info("""
        **Sodium Iodide IV (Nếu không uống được):**
        
        **Liều:**
        - 0.5-1g IV q8-12h
        
        **Lưu ý:**
        - Dùng cẩn thận, có thể gây phản ứng
        - Chỉ dùng khi thật sự cần thiết
        """)
    
    # Step 5: Corticosteroids
    st.markdown("#### **5. Corticosteroids (Ức chế chuyển đổi T4→T3 + Hỗ trợ thượng thận)**")
    
    st.markdown("""
    **Dexamethasone hoặc Hydrocortisone:**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Dexamethasone (Lựa chọn hàng đầu):**
        
        **Liều:**
        - 2mg IV q6h
        - Hoặc 4mg IV q12h
        
        **Thời gian:**
        - 3-5 ngày
        - Giảm dần khi đạt bình giáp
        """)
    
    with col2:
        st.info("""
        **Hydrocortisone (Nếu nghi ngờ suy thượng thận):**
        
        **Liều:**
        - 100mg IV q8h
        - Hoặc 50mg IV q6h
        
        **Chỉ Định:**
        - Nghi ngờ suy thượng thận kèm theo
        - Bệnh Graves có thể kèm suy thượng thận
        """)
    
    # Step 6: Additional treatments
    st.markdown("#### **6. Điều trị bổ sung**")
    
    st.markdown("""
    **A. Cholestyramine (Nếu có):**
    - 4g PO q6h
    - Giúp tăng đào thải hormone qua đường tiêu hóa
    
    **B. Lithium (Nếu không dung nạp Iodine):**
    - 300mg PO q8h
    - Theo dõi nồng độ lithium (mục tiêu: 0.6-1.0 mEq/L)
    
    **C. Plasmapheresis (Trường hợp nặng, không đáp ứng):**
    - Loại bỏ hormone khỏi máu
    - Chỉ dùng khi các biện pháp khác thất bại
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Theo dõi sát trong 24-48 giờ đầu:**
    
    **1. Dấu hiệu sinh tồn:**
    - Nhiệt độ: Mỗi 1-2 giờ
    - Nhịp tim: Liên tục (monitor)
    - Huyết áp: Mỗi 1-2 giờ
    - Nhịp thở: Mỗi 2-4 giờ
    
    **2. Xét nghiệm:**
    - **TSH, Free T4, Free T3:** Mỗi 24-48 giờ
    - **Công thức máu:** Mỗi 24 giờ (theo dõi giảm bạch cầu do PTU)
    - **Chức năng gan:** Mỗi 24-48 giờ (theo dõi độc gan)
    - **Điện giải:** Mỗi 12-24 giờ
    
    **3. Dấu hiệu cải thiện:**
    - ✅ Nhiệt độ giảm
    - ✅ Nhịp tim giảm về <100 bpm
    - ✅ Tình trạng thần kinh cải thiện
    - ✅ Free T4, T3 giảm
    
    **4. Dấu hiệu cảnh báo:**
    - ⚠️ Sốt không hạ
    - ⚠️ Nhịp tim vẫn nhanh
    - ⚠️ Tình trạng thần kinh xấu đi
    - ⚠️ Suy tim nặng lên
    - 🚨 Sốc, hôn mê
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Dân số đặc biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Có thai:**
        - **PTU là lựa chọn hàng đầu** (an toàn hơn Methimazole trong 3 tháng đầu)
        - Liều: 600-800mg/ngày chia 3-4 lần
        - Tránh Iodine (có thể gây bướu cổ thai nhi)
        - Beta-blockers: Dùng cẩn thận, theo dõi thai nhi
        
        **Người cao tuổi:**
        - Giảm liều beta-blockers
        - Theo dõi sát suy tim
        - Điều chỉnh liều theo chức năng thận
        """)
    
    with col2:
        st.markdown("""
        **Suy tim:**
        - Tránh Propranolol (có thể làm nặng suy tim)
        - Dùng Esmolol hoặc Metoprolol (selective beta-1)
        - Điều trị suy tim song song
        
        **Suy gan:**
        - Cẩn thận với PTU (độc gan)
        - Cân nhắc Methimazole
        - Theo dõi chức năng gan sát
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: LONG-TERM MANAGEMENT ==========
    st.markdown("### 🔄 Điều trị dài hạn")
    
    st.markdown("""
    **Sau khi qua giai đoạn cấp (24-48 giờ):**
    
    **1. Giảm liều dần:**
    - Beta-blockers: Giảm khi nhịp tim ổn định
    - Corticosteroids: Giảm dần trong 5-7 ngày
    - Iodine: Ngừng sau 7-10 ngày
    
    **2. Duy trì thuốc kháng giáp:**
    - PTU: 100-150mg uống q8h
    - Hoặc Methimazole: 10-15mg uống q8h
    - Điều trị 12-18 tháng
    
    **3. Lựa chọn điều trị dài hạn:**
    - Tiếp tục thuốc kháng giáp
    - Iod phóng xạ (RAI)
    - Phẫu thuật cắt tuyến giáp
    
    **4. Theo dõi:**
    - TSH, Free T4: Mỗi 4-6 tuần
    - Công thức máu: Mỗi 2-4 tuần (3 tháng đầu)
    - Chức năng gan: Mỗi 2-4 tuần (3 tháng đầu)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: REFERENCES ==========
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **Hướng dẫn Hiệp hội Tuyến giáp Hoa Kỳ (ATA) về Cường giáp** - 2016
       - Quản lý cơn bão giáp
       - Tiêu chuẩn chẩn đoán và điều trị
    
    2. **Burch HB, Wartofsky L.** Life-threatening thyrotoxicosis. Thyroid storm.
       Endocrinol Metab Clin North Am. 1993;22(2):263-277.
    
    3. **UpToDate:** Cơn bão giáp (Thyrotoxic Crisis) - Cập nhật lần cuối 2024
       - Đặc điểm lâm sàng và chẩn đoán
       - Phác đồ điều trị
    
    4. **Ross DS, et al.** 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis.
       Thyroid. 2016;26(10):1343-1421.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. Thyroid Storm là cấp cứu đe dọa tính mạng, cần điều trị tại ICU với theo dõi sát.")

