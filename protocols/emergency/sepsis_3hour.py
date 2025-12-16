"""
Sepsis 3-Hour Bundle & Management Protocol
Surviving Sepsis Campaign 2021
Extended protocol covering first 3 hours of sepsis management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


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
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle (Bắt buộc)")
    
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
    st.markdown("### ⏱️ Quản lý Trong 3 Giờ Đầu")
    
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
        st.markdown("#### **Giờ 1-3: Kháng sinh**")
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
    st.markdown("### 💊 Lựa chọn kháng sinh thực nghiệm")
    
    st.markdown("**Nguyên tắc:** Kháng sinh phổ rộng trong 1 giờ đầu, điều chỉnh sau khi có kết quả")
    
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
    st.markdown("### 💧 Truyền dịch (Fluid Resuscitation)")
    
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
    st.markdown("### ⚠️ Quản lý Vasopressor")
    
    st.markdown("**Chỉ định:** MAP <65 mmHg sau Truyền dịch đầy đủ")
    
    st.error("""
    **1st line: Norepinephrine**
    - **Liều:** 0.05-2 mcg/kg/min
    - **Mục tiêu:** MAP ≥65 mmHg
    - **Titrate:** Mỗi 5-10 phút
    - **Ưu điểm:** Tăng MAP, tăng cardiac output nhẹ
    - **Nhược điểm:** Tăng nhịp tim, tăng nguy cơ loạn nhịp
    
    **2nd line: Vasopressin**
    - **Liều:** 0.03-0.04 units/min (không titrate)
    - **Chỉ định:** Thêm vào norepinephrine nếu không đủ
    - **Ưu điểm:** Giảm liều norepinephrine, ít tác dụng phụ tim mạch
    - **Nhược điểm:** Có thể gây thiếu máu cục bộ (hiếm)
    
    **3rd line: Epinephrine**
    - **Liều:** 0.05-2 mcg/kg/min
    - **Chỉ định:** Nếu cần thêm vasopressor
    - **Ưu điểm:** Tăng MAP và cardiac output mạnh
    - **Nhược điểm:** Tăng nhịp tim, tăng nguy cơ loạn nhịp, tăng lactate
    
    **Inotrope: Dobutamine**
    - **Liều:** 2.5-20 mcg/kg/min
    - **Chỉ định:** Nếu cardiac output thấp, MAP đã ổn định
    - **Ưu điểm:** Tăng cardiac output, giảm afterload
    - **Nhược điểm:** Có thể gây hạ huyết áp, tăng nhịp tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SOURCE CONTROL ==========
    st.markdown("### 🔍 Source Control")
    
    st.markdown("**Nguyên tắc:** Xác định và điều trị ổ nhiễm trùng càng sớm càng tốt")
    
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
    st.markdown("### 📊 Theo dõi Trong 3 Giờ Đầu")
    
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
    st.markdown("### 🎯 Mục tiêu Hồi sức (Resuscitation Goals)")
    
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
    
    # ========== SECTION 9: CORTICOSTEROIDS ==========
    st.markdown("### 💉 Corticosteroids trong Septic Shock")
    
    st.warning("""
    **Chỉ định (Surviving Sepsis Campaign 2021):**
    - Septic shock với vasopressor không đáp ứng sau truyền dịch đầy đủ
    - Hoặc cần vasopressor >0.1 mcg/kg/min norepinephrine
    - Hoặc MAP <65 mmHg sau 30 mL/kg dịch
    """)
    
    use_corticosteroids = st.radio(
        "**Có chỉ định corticosteroids?**",
        ["Có", "Không", "Không chắc chắn"],
        key="sepsis_corticosteroids"
    )
    
    if use_corticosteroids == "Có":
        st.success("""
        **Hydrocortisone Protocol:**
        
        **Liều:**
        - **Hydrocortisone 200mg/day** (khuyến nghị)
        - **Cách 1:** 50mg IV q6h
        - **Cách 2:** 200mg/day continuous infusion
        
        **Thời gian:**
        - 7 ngày hoặc đến khi không cần vasopressor
        - Không cần tapering nếu <7 ngày
        
        **Monitoring:**
        - Đường huyết (tăng nguy cơ hyperglycemia)
        - Đáp ứng vasopressor (có thể giảm liều)
        - Dấu hiệu nhiễm trùng mới
        
        **Lưu ý:**
        - Không dùng nếu không có septic shock
        - Không dùng nếu có chống chỉ định (nhiễm nấm hệ thống, v.v.)
        """)
    elif use_corticosteroids == "Không chắc chắn":
        st.info("""
        **Đánh giá lại:**
        - MAP có <65 mmHg sau truyền dịch đầy đủ?
        - Có cần vasopressor >0.1 mcg/kg/min?
        - Có bằng chứng septic shock?
        
        **Nếu không đủ tiêu chuẩn:** Không dùng corticosteroids
        """)
    
    st.markdown("---")
    
    # ========== SECTION 10: RENAL REPLACEMENT THERAPY ==========
    st.markdown("### 🩸 Renal Replacement Therapy (RRT)")
    
    st.markdown("**Chỉ định RRT trong Sepsis:**")
    
    rrt_indications = st.multiselect(
        "**Chỉ định RRT:**",
        [
            "AKI Stage 2-3 với oliguria/anuria",
            "Uremia (BUN >100 mg/dL)",
            "Acidosis nặng (pH <7.15) không đáp ứng",
            "Quá tải dịch không đáp ứng lợi tiểu",
            "Hyperkalemia nặng (>6.5 mEq/L)",
            "Tăng ure máu với triệu chứng (uremic encephalopathy, pericarditis)",
            "Khác"
        ],
        key="sepsis_rrt_indications"
    )
    
    if rrt_indications:
        st.error("""
        **Chỉ định RRT đã xác định**
        
        **Loại RRT:**
        - **CRRT (Continuous RRT):** Ưu tiên nếu hemodynamically unstable
        - **IHD (Intermittent HD):** Nếu hemodynamically stable
        - **SLED (Sustained Low-Efficiency Dialysis):** Compromise giữa CRRT và IHD
        
        **Timing:**
        - **Early RRT:** Có thể cải thiện outcomes trong một số trường hợp
        - **Standard:** Khi có chỉ định rõ ràng
        
        **Anticoagulation:**
        - **CRRT:** Cần anticoagulation (heparin, citrate)
        - **IHD:** Thường không cần nếu không có chống chỉ định
        
        **Monitoring:**
        - Fluid balance
        - Electrolytes (K, Na, Phos, Ca)
        - Acid-base status
        - Clearance (Kt/V cho IHD, effluent rate cho CRRT)
        """)
    else:
        st.info("""
        **Chưa có chỉ định RRT rõ ràng**
        
        **Theo dõi:**
        - Creatinine, BUN
        - Urine output
        - Electrolytes
        - Acid-base status
        
        **Xem xét RRT nếu:**
        - Creatinine tăng nhanh
        - Urine output giảm
        - Có các chỉ định trên
        """)
    
    st.markdown("---")
    
    # ========== SECTION 11: GLUCOSE MANAGEMENT ==========
    st.markdown("### 🍭 Glucose Management")
    
    st.info("""
    **Mục tiêu đường huyết (Surviving Sepsis Campaign 2021):**
    - **140-180 mg/dL** (7.8-10.0 mmol/L)
    - **Tránh <110 mg/dL** (tăng mortality)
    - **Tránh >180 mg/dL** (tăng nguy cơ nhiễm trùng)
    """)
    
    current_glucose = st.number_input(
        "**Đường huyết hiện tại (mg/dL):**",
        min_value=0.0,
        max_value=600.0,
        value=150.0,
        step=1.0,
        key="sepsis_glucose"
    )
    
    if current_glucose < 110:
        st.error("""
        **⚠️ Đường huyết QUÁ THẤP (<110 mg/dL)**
        
        **Xử trí:**
        - **D50W 50ml IV** nếu có triệu chứng
        - **D10W infusion** nếu cần duy trì
        - **Giảm insulin** nếu đang dùng
        - **Mục tiêu:** 140-180 mg/dL
        
        **Nguy cơ:** Tăng mortality nếu đường huyết thấp kéo dài
        """)
    elif current_glucose > 180:
        st.warning("""
        **⚠️ Đường huyết CAO (>180 mg/dL)**
        
        **Xử trí:**
        - **Insulin infusion:** Bắt đầu nếu >180 mg/dL
        - **Liều:** 0.05-0.1 U/kg/h (tùy mức độ)
        - **Titrate:** Mỗi 1-2h để đạt 140-180 mg/dL
        - **Monitoring:** Glucose mỗi 1-2h
        
        **Mục tiêu:** 140-180 mg/dL
        """)
    else:
        st.success("""
        **✅ Đường huyết trong mục tiêu (140-180 mg/dL)**
        
        **Theo dõi:**
        - Glucose mỗi 4-6h nếu ổn định
        - Glucose mỗi 1-2h nếu đang điều chỉnh insulin
        - Điều chỉnh insulin để duy trì trong mục tiêu
        """)
    
    st.markdown("---")
    
    # ========== SECTION 12: VTE PROPHYLAXIS ==========
    st.markdown("### 🩸 VTE Prophylaxis")
    
    st.info("""
    **Khuyến nghị (Surviving Sepsis Campaign 2021):**
    - **LMWH** hoặc **UFH** cho tất cả bệnh nhân sepsis không chống chỉ định
    - **Bắt đầu trong 24h đầu** nếu không có chống chỉ định
    """)
    
    vte_contraindications = st.multiselect(
        "**Chống chỉ định VTE prophylaxis:**",
        [
            "Không có chống chỉ định",
            "Chảy máu đang hoạt động",
            "Rối loạn đông máu nặng",
            "Giảm tiểu cầu nặng (<50k)",
            "Suy gan nặng",
            "Khác"
        ],
        key="sepsis_vte_contra",
        default=["Không có chống chỉ định"]
    )
    
    if "Không có chống chỉ định" in vte_contraindications and len(vte_contraindications) == 1:
        st.success("""
        **✅ Có chỉ định VTE Prophylaxis**
        
        **Lựa chọn:**
        - **LMWH:** Enoxaparin 40mg SC q24h (ưu tiên)
        - **UFH:** 5000 U SC q8-12h
        - **Fondaparinux:** 2.5mg SC q24h (nếu dị ứng heparin)
        
        **Bắt đầu:** Trong 24h đầu
        **Tiếp tục:** Cho đến khi xuất viện hoặc không còn nguy cơ
        """)
    else:
        st.warning("""
        **⚠️ Có chống chỉ định VTE prophylaxis**
        
        **Đánh giá lại:**
        - Chống chỉ định có còn không?
        - Có thể dùng mechanical prophylaxis (SCD, compression stockings)?
        
        **Nếu chống chỉ định hết:**
        - Bắt đầu VTE prophylaxis ngay
        """)
    
    st.markdown("---")
    
    # ========== SECTION 13: SPECIAL CONSIDERATIONS ==========
    st.markdown("### ⚠️ Các trường hợp đặc biệt")
    
    with st.expander("🔍 Xem các trường hợp đặc biệt", expanded=False):
        st.markdown("""#### **Suy thận:**
        - Điều chỉnh liều kháng sinh theo CrCl
        - Thận trọng với truyền dịch (nguy cơ quá tải)
        - Xem xét lọc máu sớm nếu cần (xem section RRT)
        
        #### **Suy gan:**
        - Tránh kháng sinh độc gan
        - Thận trọng với truyền dịch (nguy cơ cổ trướng)
        - Xem xét albumin nếu giảm albumin nặng
        
        #### **Suy tim:**
        - Thận trọng với truyền dịch (nguy cơ suy tim nặng)
        - Ưu tiên vasopressor thay vì dịch
        - Xem xét inotrope (dobutamine) sớm
        
        #### **Phụ nữ có thai:**
        - Tránh kháng sinh gây hại thai nhi
        - Thận trọng với vasopressor (ảnh hưởng đến thai nhi)
        - Xem xét chấm dứt thai kỳ nếu cần
        
        #### **Người cao tuổi:**
        - Thận trọng với truyền dịch (nguy cơ quá tải)
        - Điều chỉnh liều kháng sinh theo CrCl
        - Xem xét các bệnh lý kèm theo
        
        #### **Stress Ulcer Prophylaxis:**
        - Xem protocol **Stress Ulcer Prophylaxis** trong Critical Care
        - PPI hoặc H2 blocker cho bệnh nhân có nguy cơ
        """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Sepsis 3-Hour")
    if not references:
        references = get_references("Sepsis")  # Fallback to general Sepsis references
    
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.caption("💡 Protocol này dựa trên Surviving Sepsis Campaign 2021 guidelines. Cập nhật thường xuyên theo guidelines mới nhất.")

