"""
Adrenal Crisis (Acute Adrenal Insufficiency) Protocol
Endocrine Society 2016 Guidelines
Life-threatening emergency requiring immediate treatment
"""

import streamlit as st


def render():
    """Adrenal Crisis Protocol"""
    st.subheader("⚡ Adrenal Crisis (Acute Adrenal Insufficiency)")
    st.caption("Endocrine Society 2016 Guidelines - Life-threatening adrenal insufficiency emergency")
    
    st.error("""
    **🚨 CẤP CỨU - Cần điều trị ngay lập tức**
    
    **Adrenal Crisis là tình trạng cấp cứu đe dọa tính mạng, cần:**
    - Điều trị ngay tại ICU
    - Bổ sung Corticosteroids ngay lập tức
    - Bù dịch và điện giải
    - Điều trị nguyên nhân thúc đẩy
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu Chuẩn Chẩn Đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Chẩn đoán Adrenal Crisis khi có:**
        
        **1. Triệu chứng cấp tính:**
        - **Sốc:** Huyết áp thấp, không đáp ứng dịch
        - **Hạ huyết áp:** SBP <90 mmHg hoặc giảm >20 mmHg so với baseline
        - **Mệt mỏi cực độ:** Không thể đứng dậy
        - **Nôn, buồn nôn:** Thường gặp
        - **Đau bụng:** Có thể giống viêm phúc mạc
        
        **2. Dấu hiệu suy thượng thận:**
        - **Hạ huyết áp:** Đặc biệt tư thế đứng
        - **Sạm da:** Tăng sắc tố (trong suy thượng thận nguyên phát)
        - **Mệt mỏi, yếu cơ**
        - **Chán ăn, sụt cân**
        
        **3. Xác nhận suy thượng thận:**
        - **Cortisol thấp:** <18 mcg/dL (500 nmol/L) lúc stress
        - **ACTH tăng:** Trong suy thượng thận nguyên phát
        - **ACTH thấp:** Trong suy thượng thận thứ phát
        - **Hyponatremia:** Thường gặp
        - **Hyperkalemia:** Trong suy thượng thận nguyên phát
        - **Hypoglycemia:** Có thể gặp
        
        **4. Yếu tố thúc đẩy:**
        - Nhiễm trùng (đặc biệt nhiễm trùng huyết)
        - Chấn thương, phẫu thuật
        - Ngừng đột ngột corticosteroids
        - Stress nặng
        """)
        
        st.warning("""
        **⚠️ Lưu ý:** 
        - Chẩn đoán chủ yếu dựa trên lâm sàng
        - **KHÔNG chờ kết quả xét nghiệm** để bắt đầu điều trị
        - Điều trị ngay khi nghi ngờ
        - Tỷ lệ tử vong cao nếu không điều trị kịp thời
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: RISK FACTORS ==========
    st.markdown("### 📊 Yếu Tố Nguy Cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Bệnh nhân có nguy cơ:**
        
        **1. Suy thượng thận đã biết:**
        - Đang dùng corticosteroids
        - Đã phẫu thuật tuyến yên/thượng thận
        - Bệnh Addison
        - Bệnh tự miễn
        
        **2. Bệnh lý liên quan:**
        - Bệnh tuyến yên
        - Khối u tuyến yên
        - Xạ trị vùng đầu cổ
        """)
    
    with col2:
        st.markdown("""
        **Yếu tố thúc đẩy:**
        
        **1. Nhiễm trùng:**
        - Nhiễm trùng huyết
        - Viêm phổi
        - Nhiễm trùng tiết niệu
        
        **2. Stress:**
        - Phẫu thuật
        - Chấn thương
        - Đau nặng
        
        **3. Thuốc:**
        - Ngừng đột ngột corticosteroids
        - Ketoconazole, Etomidate
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Điều Trị Ngay Lập Tức (ICU)")
    
    st.markdown("""
    **Thứ tự ưu tiên điều trị (theo Endocrine Society 2016):**
    """)
    
    # Step 1: Hydrocortisone
    st.markdown("#### **1. Hydrocortisone (QUAN TRỌNG NHẤT - Điều trị ngay)**")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Điều trị Hydrocortisone NGAY LẬP TỨC, không chờ xét nghiệm**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Hydrocortisone IV (Lựa chọn hàng đầu):**
        
        **Liều loading:**
        - **100mg IV ngay lập tức**
        - Hoặc 50-100mg IV
        
        **Liều duy trì:**
        - **50-100mg IV q6-8h**
        - Hoặc 200mg/ngày chia 3-4 lần
        
        **Thời gian:**
        - Dùng liên tục đến khi ổn định
        - Giảm dần sau 24-48 giờ
        """)
    
    with col2:
        st.info("""
        **Methylprednisolone (Thay thế):**
        
        **Liều:**
        - 40-80mg IV q6-8h
        
        **Lưu ý:**
        - Không có mineralocorticoid activity
        - Cần bổ sung fludrocortisone nếu suy thượng thận nguyên phát
        """)
    
    st.markdown("""
    **Chuyển sang PO:**
    - Khi bệnh nhân ổn định, có thể uống
    - Hydrocortisone: 20mg PO q8h (tổng 60mg/ngày)
    - Hoặc Prednisone: 5-7.5mg PO q12h
    """)
    
    # Step 2: Fluid resuscitation
    st.markdown("#### **2. Bù Dịch (Fluid Resuscitation)**")
    
    st.markdown("""
    **Dịch truyền:**
    - **NS 0.9%:** 1-2L trong giờ đầu
    - Sau đó: 2-4L/ngày tùy theo nhu cầu
    - **D5NS:** Nếu có hypoglycemia
    
    **Mục tiêu:**
    - Huyết áp ổn định (SBP >90 mmHg)
    - Đi tiểu tốt (>0.5 mL/kg/h)
    - Điện giải bình thường
    """)
    
    # Step 3: Electrolyte correction
    st.markdown("#### **3. Điều Chỉnh Điện Giải**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hyponatremia:**
        - Thường tự cải thiện sau khi dùng Hydrocortisone
        - Nếu nặng: Dùng hypertonic saline cẩn thận
        - Điều chỉnh từ từ (0.5-1 mEq/L/giờ)
        
        **Hyperkalemia:**
        - Thường tự cải thiện sau khi dùng Hydrocortisone
        - Nếu nặng: Calcium gluconate, Insulin+Dextrose
        """)
    
    with col2:
        st.markdown("""
        **Hypoglycemia:**
        - D5W hoặc D10W
        - Theo dõi đường huyết
        - Thường cải thiện sau Hydrocortisone
        
        **Acidosis:**
        - Thường tự cải thiện
        - Nếu nặng: Sodium bicarbonate
        """)
    
    # Step 4: Mineralocorticoid
    st.markdown("#### **4. Mineralocorticoid (Nếu suy thượng thận nguyên phát)**")
    
    st.markdown("""
    **Fludrocortisone:**
    - **Chỉ dùng trong suy thượng thận nguyên phát**
    - **Liều:** 0.1-0.2mg PO/ngày
    - **Bắt đầu:** Khi bệnh nhân có thể uống
    - **Mục tiêu:** Điều chỉnh điện giải, huyết áp
    
    **Lưu ý:**
    - Hydrocortisone liều cao đã có một phần mineralocorticoid activity
    - Fludrocortisone cần thiết khi giảm liều Hydrocortisone
    """)
    
    # Step 5: Treat precipitating cause
    st.markdown("#### **5. Điều Trị Nguyên Nhân Thúc Đẩy**")
    
    st.markdown("""
    **Tìm và điều trị nguyên nhân:**
    
    **1. Nhiễm trùng:**
    - Kháng sinh phổ rộng ngay
    - Cấy máu, nước tiểu, đờm
    - Điều trị theo kết quả cấy
    
    **2. Stress:**
    - Điều trị đau
    - Hỗ trợ tâm lý
    
    **3. Ngừng thuốc:**
    - Không bao giờ ngừng đột ngột corticosteroids
    - Giảm dần liều
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: MONITORING ==========
    st.markdown("### 📈 Theo Dõi")
    
    st.markdown("""
    **Theo dõi sát trong 24-48 giờ đầu:**
    
    **1. Dấu hiệu sinh tồn:**
    - **Huyết áp:** Mỗi 15-30 phút (giờ đầu), sau đó mỗi 1-2 giờ
    - **Nhịp tim:** Liên tục (monitor)
    - **Nhiệt độ:** Mỗi 2-4 giờ
    - **Nhịp thở, SpO2:** Liên tục
    - **Lượng nước tiểu:** Mỗi giờ
    
    **2. Xét nghiệm:**
    - **Cortisol, ACTH:** Trước và sau điều trị (để xác nhận)
    - **Điện giải:** Mỗi 6-12 giờ (đặc biệt Na, K)
    - **Đường huyết:** Mỗi 4-6 giờ
    - **ABG:** Nếu có rối loạn hô hấp
    - **Công thức máu:** Mỗi 24 giờ
    
    **3. Dấu hiệu cải thiện:**
    - ✅ Huyết áp ổn định, tăng
    - ✅ Điện giải bình thường
    - ✅ Tình trạng tổng thể cải thiện
    - ✅ Hết nôn, buồn nôn
    
    **4. Dấu hiệu cảnh báo:**
    - ⚠️ Huyết áp vẫn thấp
    - ⚠️ Điện giải không cải thiện
    - ⚠️ Tình trạng xấu đi
    - 🚨 Sốc, ngừng tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Dân Số Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Có thai:**
        - Hydrocortisone an toàn
        - Liều tương tự
        - Theo dõi thai nhi
        
        **Người cao tuổi:**
        - Cẩn thận với bù dịch (suy tim)
        - Theo dõi sát tim mạch
        - Điều chỉnh liều theo chức năng thận
        """)
    
    with col2:
        st.markdown("""
        **Suy tim:**
        - Cẩn thận với bù dịch
        - Theo dõi sát dấu hiệu quá tải dịch
        - Có thể cần dùng vasopressors sớm
        
        **Suy thận:**
        - Điều chỉnh dịch truyền
        - Theo dõi điện giải sát
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: LONG-TERM MANAGEMENT ==========
    st.markdown("### 🔄 Điều Trị Dài Hạn")
    
    st.markdown("""
    **Sau khi qua giai đoạn cấp (24-48 giờ):**
    
    **1. Giảm liều Hydrocortisone:**
    - **Ngày 2-3:** 50mg IV q8h (150mg/ngày)
    - **Ngày 4-5:** 25mg IV q8h (75mg/ngày)
    - **Sau đó:** Chuyển sang PO
    
    **2. Liều duy trì (PO):**
    - **Hydrocortisone:** 15-25mg/ngày
      - Sáng: 10-15mg
      - Chiều: 5-10mg
    - **Hoặc Prednisone:** 5-7.5mg/ngày
      - Sáng: 5mg
      - Chiều: 2.5mg (nếu cần)
    
    **3. Fludrocortisone (Nếu suy thượng thận nguyên phát):**
    - 0.1-0.2mg PO/ngày (sáng)
    - Điều chỉnh theo huyết áp, điện giải
    
    **4. Stress dosing:**
    - **Bệnh nhẹ (sốt, cảm):** Tăng gấp 2-3 lần liều thường
    - **Bệnh nặng (nhiễm trùng):** 50-100mg q6-8h
    - **Phẫu thuật:** 100mg IV trước phẫu thuật, sau đó 50mg q6h x 24-48h
    
    **5. Theo dõi:**
    - **Huyết áp:** Mỗi lần khám
    - **Điện giải:** Mỗi 3-6 tháng
    - **Cortisol:** Không cần nếu đã xác nhận suy thượng thận
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PREVENTION ==========
    st.markdown("### 🛡️ Phòng Ngừa")
    
    st.markdown("""
    **Giáo dục bệnh nhân:**
    
    **1. Nhận biết dấu hiệu:**
    - Mệt mỏi cực độ
    - Nôn, buồn nôn
    - Hạ huyết áp, chóng mặt
    - Đau bụng
    
    **2. Stress dosing:**
    - Luôn mang theo Hydrocortisone
    - Tăng liều khi bệnh, stress
    - Biết khi nào cần đến bệnh viện
    
    **3. Medical alert:**
    - Đeo vòng/yên tay y tế
    - Mang theo thẻ bệnh
    - Thông báo cho người thân
    
    **4. Không bao giờ:**
    - Ngừng đột ngột corticosteroids
    - Bỏ qua liều khi bệnh
    - Quên tăng liều khi stress
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    st.markdown("""
    1. **Endocrine Society Clinical Practice Guideline** - 2016
       - Treatment of Primary Adrenal Insufficiency
       - Adrenal Crisis Management
    
    2. **Bornstein SR, et al.** Diagnosis and Treatment of Primary Adrenal Insufficiency:
       An Endocrine Society Clinical Practice Guideline.
       J Clin Endocrinol Metab. 2016;101(2):364-389.
    
    3. **UpToDate:** Adrenal Crisis - Last updated 2024
       - Clinical features and diagnosis
       - Treatment protocols
    
    4. **Hahner S, et al.** Adrenal insufficiency.
       Lancet. 2021;397(10274):613-629.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. Adrenal Crisis là cấp cứu đe dọa tính mạng, cần điều trị ngay lập tức. KHÔNG chờ kết quả xét nghiệm để bắt đầu điều trị.")

