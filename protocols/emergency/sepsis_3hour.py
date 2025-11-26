"""
Sepsis 3-Hour Bundle & Management Protocol
Surviving Sepsis Campaign 2021
Extended protocol covering first 3 hours of sepsis management
"""

import streamlit as st


def render():
    """Sepsis 3-Hour Bundle & Management Protocol"""
    st.subheader("🦠 Sepsis 3-Hour Bundle & Management")
    st.caption("Surviving Sepsis Campaign 2021 - Extended 3-Hour Protocol")
    
    st.info("""
    **Chẩn đoán Sepsis:**
    - Nhiễm trùng (nghi ngờ hoặc xác định)
    - qSOFA ≥2 hoặc SOFA tăng ≥2 điểm
    - Rối loạn chức năng cơ quan
    
    **Septic Shock:**
    - Sepsis + MAP <65 mmHg sau truyền dịch
    - Hoặc Lactate >2 mmol/L
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: 1-HOUR BUNDLE ==========
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle (Bắt Buộc)")
    
    st.error("""
    **Thực hiện NGAY trong vòng 1 GIỜ:**
    
    1. ✅ **Đo Lactate**
       - Lactate >2 mmol/L = septic shock
       - Đo lại sau 2-4h nếu tăng
    
    2. ✅ **Cấy máu trước khi kháng sinh**
       - 2 bộ cấy máu (từ 2 vị trí khác nhau)
       - Cấy dịch từ ổ nhiễm (nếu có)
       - ⚠️ Không trì hoãn kháng sinh để chờ cấy máu
    
    3. ✅ **Kháng sinh phổ rộng**
       - Trong vòng 1 giờ
       - Theo guideline địa phương
       - Liều đủ, đường IV
    
    4. ✅ **Truyền dịch nhanh**
       - 30 mL/kg crystalloid
       - Trong 3 giờ đầu
       - Ringer Lactate hoặc Normal Saline
    
    5. ✅ **Vasopressor nếu hạ huyết áp**
       - Nếu MAP <65 mmHg sau truyền dịch
       - Norepinephrine là thuốc đầu tay
       - Mục tiêu MAP ≥65 mmHg
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: 3-HOUR MANAGEMENT ==========
    st.markdown("### ⏱️ Quản Lý Trong 3 Giờ Đầu")
    
    st.markdown("**Các bước tiếp theo sau 1-hour bundle:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Giờ 1-2: Đánh giá đáp ứng**")
        st.warning("""
        **Sau truyền dịch 30 mL/kg:**
        
        **Đánh giá:**
        - MAP có ≥65 mmHg?
        - Lactate có giảm?
        - Urine output có ≥0.5 mL/kg/h?
        - Tình trạng lâm sàng có cải thiện?
        
        **Nếu không đáp ứng:**
        - Xem xét thêm dịch (nếu không quá tải)
        - Bắt đầu vasopressor
        - Tìm ổ nhiễm trùng
        """)
        
        st.markdown("#### **Giờ 2-3: Source Control**")
        st.error("""
        **Xác định và điều trị ổ nhiễm trùng:**
        
        **Các ổ nhiễm trùng thường gặp:**
        - Viêm phổi
        - Nhiễm trùng tiết niệu
        - Nhiễm trùng ổ bụng
        - Nhiễm trùng da/mô mềm
        - Nhiễm trùng đường máu
        
        **Source control:**
        - Dẫn lưu áp xe
        - Phẫu thuật cắt bỏ mô hoại tử
        - Loại bỏ catheter nhiễm trùng
        - Điều trị ổ nhiễm trùng cụ thể
        """)
    
    with col2:
        st.markdown("#### **Giờ 1-3: Kháng Sinh**")
        st.success("""
        **Đã cho kháng sinh trong 1 giờ đầu**
        
        **Đánh giá lại:**
        - Kháng sinh có phù hợp?
        - Có cần điều chỉnh theo kháng sinh đồ?
        - Có cần thêm kháng sinh phổ rộng?
        
        **Nếu có kháng sinh đồ:**
        - De-escalate nếu có thể
        - Điều chỉnh liều theo CrCl
        - Xem xét thời gian điều trị
        """)
        
        st.markdown("#### **Giờ 1-3: Vasopressor**")
        st.error("""
        **Nếu MAP <65 mmHg sau truyền dịch:**
        
        **1st line: Norepinephrine**
        - 0.05-2 mcg/kg/min
        - Mục tiêu MAP ≥65 mmHg
        - Titrate mỗi 5-10 phút
        
        **2nd line: Vasopressin**
        - 0.03-0.04 units/min
        - Thêm vào nếu norepinephrine không đủ
        - Giảm liều norepinephrine khi thêm vasopressin
        
        **3rd line: Epinephrine**
        - 0.05-2 mcg/kg/min
        - Nếu cần thêm vasopressor
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: ANTIBIOTIC SELECTION ==========
    st.markdown("### 💊 Lựa Chọn Kháng Sinh Thực Nghiệm")
    
    st.markdown("**Nguyên Tắc:** Kháng sinh phổ rộng trong 1 giờ đầu, điều chỉnh sau khi có kết quả")
    
    # Community vs Hospital acquired
    infection_source = st.radio(
        "Nguồn nhiễm trùng:",
        ["Nhiễm trùng cộng đồng", "Nhiễm trùng bệnh viện", "Không rõ"],
        key="sepsis_3h_source"
    )
    
    st.markdown("---")
    
    if infection_source == "Nhiễm trùng cộng đồng":
        st.success("""
        ### ✅ Nhiễm Trùng Cộng Đồng
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Ceftriaxone 2g IV q24h**
        + **Azithromycin 500mg IV q24h**
        
        **Lựa chọn 2:**
        - **Piperacillin-Tazobactam 4.5g IV q6h**
        
        **Lựa chọn 3 (Nếu dị ứng beta-lactam):**
        - **Levofloxacin 750mg IV q24h**
        + **Azithromycin 500mg IV q24h**
        
        **Thêm Vancomycin nếu:**
        - Nghi ngờ MRSA
        - Viêm phổi nặng
        - Tiền sử MRSA
        """)
        
    elif infection_source == "Nhiễm trùng bệnh viện":
        st.warning("""
        ### ⚠️ Nhiễm Trùng Bệnh Viện
        
        **Lựa chọn 1 (Ưu tiên):**
        - **Meropenem 1g IV q8h**
        + **Vancomycin 15-20mg/kg IV q8-12h** (điều chỉnh theo CrCl)
        
        **Lựa chọn 2:**
        - **Piperacillin-Tazobactam 4.5g IV q6h**
        + **Vancomycin 15-20mg/kg IV q8-12h**
        
        **Lựa chọn 3 (Nếu nghi ngờ Pseudomonas):**
        - **Cefepime 2g IV q8h**
        + **Gentamicin 5-7mg/kg IV q24h**
        + **Vancomycin** (nếu cần)
        
        **Lựa chọn 4 (Nếu dị ứng beta-lactam):**
        - **Ciprofloxacin 400mg IV q8h**
        + **Vancomycin**
        + **Metronidazole 500mg IV q8h** (nếu nghi ngờ nhiễm trùng kỵ khí
        """)
        
    else:
        st.info("""
        ### ❓ Nguồn Nhiễm Trùng Không Rõ
        
        **Khuyến nghị:** Điều trị như nhiễm trùng bệnh viện (phổ rộng hơn)
        
        **Lựa chọn:**
        - **Meropenem 1g IV q8h**
        + **Vancomycin 15-20mg/kg IV q8-12h**
        
        **Hoặc:**
        - **Piperacillin-Tazobactam 4.5g IV q6h**
        + **Vancomycin**
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: FLUID RESUSCITATION ==========
    st.markdown("### 💧 Truyền Dịch (Fluid Resuscitation)")
    
    st.markdown("**Nguyên tắc:** 30 mL/kg crystalloid trong 3 giờ đầu")
    
    # Fluid calculator
    with st.expander("🔢 Tính Lượng Dịch Cần Truyền", expanded=False):
        weight_kg = st.number_input(
            "Cân nặng (kg):",
            min_value=40.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            format="%.1f",
            key="sepsis_3h_weight"
        )
        
        fluid_ml = weight_kg * 30
        
        st.info(f"""
        **Lượng dịch cần truyền:** {fluid_ml:.0f} mL
        
        **Phân bổ:**
        - **Giờ đầu:** {fluid_ml * 0.5:.0f} mL (50%)
        - **Giờ 2-3:** {fluid_ml * 0.5:.0f} mL (50%)
        
        **Loại dịch:**
        - Ringer Lactate (ưu tiên)
        - Hoặc Normal Saline
        """)
    
    st.markdown("**Đánh giá đáp ứng dịch:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Đáp ứng tốt:**
        - MAP ≥65 mmHg
        - Urine output ≥0.5 mL/kg/h
        - Lactate giảm
        - Tình trạng lâm sàng cải thiện
        
        **Hành động:**
        - Tiếp tục truyền dịch theo kế hoạch
        - Theo dõi sát
        """)
    
    with col2:
        st.error("""
        **Không đáp ứng:**
        - MAP vẫn <65 mmHg
        - Urine output vẫn thấp
        - Lactate không giảm hoặc tăng
        - Tình trạng lâm sàng không cải thiện
        
        **Hành động:**
        - Bắt đầu vasopressor
        - Xem xét thêm dịch (nếu không quá tải)
        - Tìm ổ nhiễm trùng
        - Xem xét các chẩn đoán khác
        """)
    
    st.warning("""
    **⚠️ Cảnh báo quá tải dịch:**
    - Phù phổi
    - Tăng áp lực tĩnh mạch trung tâm (CVP)
    - Khó thở
    - Ran ẩm phổi
    
    **Nếu quá tải:**
    - Giảm tốc độ truyền dịch
    - Xem xét dùng lợi tiểu (nếu cần)
    - Ưu tiên vasopressor thay vì dịch
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: VASOPRESSOR MANAGEMENT ==========
    st.markdown("### ⚠️ Quản Lý Vasopressor")
    
    st.markdown("**Chỉ Định:** MAP <65 mmHg sau Truyền Dịch đầy đủ")
    
    st.error("""
    **1st line: Norepinephrine**
    - **Liều:** 0.05-2 mcg/kg/min
    - **Mục Tiêu:** MAP ≥65 mmHg
    - **Titrate:** Mỗi 5-10 phút
    - **Ưu điểm:** Tăng MAP, tăng cardiac output nhẹ
    - **Nhược điểm:** Tăng nhịp tim, tăng nguy cơ loạn nhịp
    
    **2nd line: Vasopressin**
    - **Liều:** 0.03-0.04 units/min (không titrate)
    - **Chỉ Định:** Thêm vào norepinephrine nếu không đủ
    - **Ưu điểm:** Giảm liều norepinephrine, ít tác dụng phụ tim mạch
    - **Nhược điểm:** Có thể gây thiếu máu cục bộ (hiếm)
    
    **3rd line: Epinephrine**
    - **Liều:** 0.05-2 mcg/kg/min
    - **Chỉ Định:** Nếu cần thêm vasopressor
    - **Ưu điểm:** Tăng MAP và cardiac output mạnh
    - **Nhược điểm:** Tăng nhịp tim, tăng nguy cơ loạn nhịp, tăng lactate
    
    **Inotrope: Dobutamine**
    - **Liều:** 2.5-20 mcg/kg/min
    - **Chỉ Định:** Nếu cardiac output thấp, MAP đã ổn định
    - **Ưu điểm:** Tăng cardiac output, giảm afterload
    - **Nhược điểm:** Có thể gây hạ huyết áp, tăng nhịp tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SOURCE CONTROL ==========
    st.markdown("### 🔍 Source Control")
    
    st.markdown("**Nguyên Tắc:** Xác định và điều trị ổ nhiễm trùng càng sớm càng tốt")
    
    source_control_options = [
        "Viêm phổi",
        "Nhiễm trùng tiết niệu",
        "Nhiễm trùng ổ bụng",
        "Nhiễm trùng da/mô mềm",
        "Nhiễm trùng đường máu (catheter)",
        "Nhiễm trùng xương/khớp",
        "Nhiễm trùng hệ thần kinh trung ương",
        "Khác"
    ]
    
    selected_sources = st.multiselect(
        "Ổ nhiễm trùng nghi ngờ:",
        source_control_options,
        key="sepsis_3h_sources"
    )
    
    if selected_sources:
        st.info(f"""
        **Ổ nhiễm trùng đã xác định:** {', '.join(selected_sources)}
        
        **Hành động:**
        - Điều trị ổ nhiễm trùng cụ thể
        - Dẫn lưu nếu có áp xe
        - Loại bỏ catheter nhiễm trùng
        - Phẫu thuật nếu cần (cắt bỏ mô hoại tử)
        - Điều chỉnh kháng sinh theo ổ nhiễm trùng
        """)
    
    st.markdown("**Timeline cho source control:**")
    st.warning("""
    - **Urgent (<12h):** Áp xe, nhiễm trùng đường máu, nhiễm trùng ổ bụng
    - **Early (<24h):** Viêm phổi, nhiễm trùng tiết niệu, nhiễm trùng da/mô mềm
    - **Delayed (>24h):** Nhiễm trùng xương/khớp (nếu không nguy hiểm)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📊 Theo Dõi Trong 3 Giờ Đầu")
    
    st.markdown("**Monitoring parameters:**")
    
    monitoring_table = {
        "Thông số": [
            "Dấu hiệu sống",
            "Lactate",
            "Urine output",
            "MAP",
            "Arterial blood gas (nếu cần)",
            "CVP (nếu có)",
            "ScvO2 (nếu có)"
        ],
        "Tần suất": [
            "Mỗi 15-30 phút",
            "Mỗi 2-4 giờ (cho đến bình thường)",
            "Mỗi giờ",
            "Liên tục (nếu có arterial line)",
            "Theo chỉ định",
            "Theo chỉ định",
            "Theo chỉ định"
        ],
        "Mục tiêu": [
            "Ổn định",
            "<2 mmol/L",
            "≥0.5 mL/kg/h",
            "≥65 mmHg",
            "pH >7.35, PaO2 >60",
            "8-12 mmHg",
            "≥70%"
        ]
    }
    
    st.table(monitoring_table)
    
    st.markdown("---")
    
    # ========== SECTION 8: RESUSCITATION GOALS ==========
    st.markdown("### 🎯 Mục Tiêu Hồi Sức (Resuscitation Goals)")
    
    st.info("""
    **Mục tiêu trong 3 giờ đầu:**
    
    - ✅ **MAP ≥65 mmHg**
    - ✅ **Urine output ≥0.5 mL/kg/h**
    - ✅ **Lactate bình thường hóa** (<2 mmol/L)
    - ✅ **ScvO2 ≥70%** (nếu đo được)
    - ✅ **CVP 8-12 mmHg** (nếu đo được)
    - ✅ **Tình trạng lâm sàng cải thiện**
    
    **Nếu không đạt mục tiêu:**
    - Xem xét thêm dịch (nếu không quá tải)
    - Tăng liều vasopressor
    - Tìm ổ nhiễm trùng
    - Xem xét các chẩn đoán khác
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: SPECIAL CONSIDERATIONS ==========
    st.markdown("### ⚠️ Các Trường Hợp Đặc Biệt")
    
    with st.expander("🔍 Xem các trường hợp đặc biệt", expanded=False):
        st.markdown("""#### **Suy Thận:**
        - Điều chỉnh liều kháng sinh theo CrCl
        - Thận trọng với truyền dịch (nguy cơ quá tải)
        - Xem xét lọc máu sớm nếu cần
        
        #### **Suy Gan:**
        - Tránh kháng sinh độc gan
        - Thận trọng với truyền dịch (nguy cơ cổ trướng)
        - Xem xét albumin nếu giảm albumin nặng
        
        #### **Suy Tim:**
        - Thận trọng với truyền dịch (nguy cơ suy tim nặng)
        - Ưu tiên vasopressor thay vì dịch
        - Xem xét inotrope (dobutamine) sớm
        
        #### **Phụ Nữ Có Thai:**
        - Tránh kháng sinh gây hại thai nhi
        - Thận trọng với vasopressor (ảnh hưởng đến thai nhi)
        - Xem xét chấm dứt thai kỳ nếu cần
        
        #### **Người Cao Tuổi:**
        - Thận trọng với truyền dịch (nguy cơ quá tải)
        - Điều chỉnh liều kháng sinh theo CrCl
        - Xem xét các bệnh lý kèm theo
        """)
    
    st.markdown("---")
    
    # ========== SECTION 10: REFERENCES ==========
    st.markdown("### 📚 Tài liệu tham khảo")
    
    references = [
        "**Surviving Sepsis Campaign Guidelines 2021:** International Guidelines for Management of Sepsis and Septic Shock",
        "**Evans L, et al.** Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit Care Med. 2021;49(11):e1063-e1143.",
        "**UpToDate:** Sepsis and septic shock in adults: Management and prognosis",
        "**IDSA:** Guidelines for the Management of Sepsis",
    ]
    
    for ref in references:
        st.markdown(f"- {ref}")
    
    st.caption("💡 Protocol này dựa trên Surviving Sepsis Campaign 2021 guidelines. Cập nhật thường xuyên theo guidelines mới nhất.")

