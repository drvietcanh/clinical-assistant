"""
Heat Stroke Protocol
Exertional and non-exertional heat stroke
Life-threatening hyperthermia with CNS dysfunction
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Heat Stroke Protocol"""
    st.subheader("🌡️ Sốc Nhiệt (Heat Stroke)")
    st.caption("Exertional and non-exertional heat stroke - Hyperthermia with CNS dysfunction")
    
    st.error("""
    **⚠️ SỐC NHIỆT = CẤP CỨU Y TẾ - TỶ LỆ TỬ VONG 10-50%**
    
    **Định nghĩa:**
    - Nhiệt độ cơ thể >40°C (>104°F)
    - Rối loạn chức năng hệ thần kinh trung ương
    - Đây là bệnh nặng nhất trong các bệnh do nhiệt
    
    **Phân loại:**
    - **Sốc nhiệt do gắng sức:** Vận động viên, công nhân
    - **Sốc nhiệt cổ điển:** Người già, trẻ em, bệnh mạn tính
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá Nguy cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        body_temp = st.number_input(
            "**Nhiệt độ cơ thể (°C):**",
            min_value=35.0,
            max_value=45.0,
            value=37.0,
            step=0.1,
            help="Nhiệt độ đo được (nên đo trực tràng)"
        )
        
        exposure_duration = st.number_input(
            "**Thời gian phơi nhiễm (giờ):**",
            min_value=0.0,
            max_value=24.0,
            value=0.0,
            step=0.5,
            help="Thời gian ở môi trường nóng"
        )
        
        has_cns_symptoms = st.checkbox("Có triệu chứng thần kinh", value=False)
    
    with col2:
        if body_temp > 0:
            temp_f = body_temp * 9/5 + 32
            st.info(f"""
            **Nhiệt độ:** {body_temp:.1f}°C ({temp_f:.1f}°F)
            
            **Đánh giá:**
            - **Bình thường:** 36-37.5°C
            - **Sốt:** 37.5-38.5°C
            - **Kiệt sức do nhiệt:** 38.5-40°C
            - **Sốc nhiệt:** >40°C
            """)
            
            if body_temp >= 40:
                st.error("🚨 **SỐC NHIỆT** - Cần làm mát ngay lập tức!")
            elif body_temp >= 38.5:
                st.warning("⚠️ **KIỆT SỨC DO NHIỆT** - Cần điều trị")
            else:
                st.success("✅ **NHIỆT ĐỘ BÌNH THƯỜNG**")
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL PRESENTATION ==========
    st.markdown("### 🔍 Triệu chứng Lâm sàng")
    
    st.markdown("""
    **Triệu chứng thần kinh (Bắt buộc để chẩn đoán):**
    - Rối loạn ý thức
    - Lú lẫn, kích động
    - Co giật
    - Hôn mê
    - Rối loạn vận động
    
    **Triệu chứng khác:**
    - Da nóng, khô (cổ điển) hoặc ẩm (gắng sức)
    - Nhịp tim nhanh
    - Huyết áp thấp
    - Thở nhanh
    - Buồn nôn, nôn
    
    **Dấu hiệu nguy hiểm:**
    - 🚨 Hôn mê
    - 🚨 Co giật
    - 🚨 Sốc
    - 🚨 Rối loạn đông máu
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: DIAGNOSIS ==========
    st.markdown("### 📋 Chẩn đoán")
    
    st.warning("""
    **Chẩn đoán sốc nhiệt khi có:**
    
    1. **Nhiệt độ cơ thể >40°C (>104°F)**
       - Đo trực tràng là chính xác nhất
       - Nhiệt độ da có thể thấp hơn
    
    2. **Rối loạn chức năng hệ thần kinh trung ương**
       - Bắt buộc để chẩn đoán
       - Có thể từ lú lẫn nhẹ đến hôn mê
    
    3. **Tiền sử phơi nhiễm nhiệt**
       - Môi trường nóng
       - Gắng sức trong nhiệt độ cao
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác Đồ Điều trị")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Kiệt sức do nhiệt (Heat Exhaustion)", "Sốc nhiệt nhẹ (Mild)", "Sốc nhiệt nặng (Severe)"],
        key="heat_stroke_severity"
    )
    
    st.markdown("---")
    
    if "Kiệt sức" in severity:
        render_heat_exhaustion()
    elif "nhẹ" in severity:
        render_mild_heat_stroke()
    else:
        render_severe_heat_stroke()
    
    st.markdown("---")
    
    # ========== SECTION 5: COOLING METHODS ==========
    st.markdown("### ❄️ Phương Pháp Làm Mát")
    
    st.error("""
    **Mục tiêu:** Giảm nhiệt độ xuống <39°C trong 30 phút
    
    **Phương pháp làm mát ngoài (Evaporative Cooling):**
    1. **Cởi quần áo:** Ngay lập tức
    2. **Phun nước:** Nước lạnh hoặc ấm
    3. **Quạt:** Tăng bay hơi
    4. **Chườm đá:** Nách, bẹn, cổ
    
    **Phương pháp làm mát xâm lấn:**
    1. **Rửa dạ dày:** Nước lạnh qua ống thông
    2. **Rửa bàng quang:** Nước lạnh
    3. **Rửa màng phổi:** Nước lạnh (hiếm)
    4. **Lọc máu:** Nếu sốc nhiệt kháng trị
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MEDICAL MANAGEMENT ==========
    st.markdown("### 💉 Điều trị Y Tế")
    
    st.info("""
    **Điều trị hỗ trợ:**
    
    **1. Bù dịch:**
    - NS hoặc LR: 1-2L ban đầu
    - Thận trọng với quá tải dịch
    - Theo dõi áp lực tĩnh mạch trung ương
    
    **2. Điều chỉnh rối loạn điện giải:**
    - Na+: Có thể giảm hoặc tăng
    - K+: Có thể giảm
    - Bổ sung theo xét nghiệm
    
    **3. Điều trị co giật:**
    - Benzodiazepines: Midazolam, lorazepam
    - Phenytoin nếu cần
    
    **4. Điều trị sốc:**
    - Bù dịch
    - Vasopressors nếu cần
    
    **5. Điều trị rối loạn đông máu:**
    - FFP, platelets nếu cần
    - Theo dõi DIC
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Trong quá trình điều trị:**
    
    **Dấu hiệu sinh tồn:**
    - **Nhiệt độ:** Mỗi 5-10 phút (đo trực tràng)
    - **Huyết áp:** Continuous
    - **Nhịp tim:** Continuous
    - **SpO2:** Continuous
    
    **Xét nghiệm:**
    - **Điện giải:** Mỗi 2-4 giờ
    - **Chức năng thận:** Creatinine, BUN
    - **Chức năng gan:** ALT, AST, Bilirubin
    - **Đông máu:** PT/INR, platelets
    - **CK:** Nếu nghi ngờ tiêu cơ vân
    
    **Dấu hiệu cảnh báo:**
    - 🚨 Nhiệt độ không giảm sau 30 phút
    - 🚨 Rối loạn đông máu
    - 🚨 Suy thận cấp
    - 🚨 Tiêu cơ vân
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("heat_stroke"))


def render_heat_exhaustion():
    """Heat Exhaustion Protocol"""
    st.warning("## ⚠️ KIỆT SỨC DO NHIỆT (Heat Exhaustion)")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: 38.5-40°C
    - Không có rối loạn ý thức
    - Triệu chứng: Mệt mỏi, đau đầu, buồn nôn
    
    **Điều trị:**
    1. **Di chuyển:** Ra khỏi môi trường nóng
    2. **Làm mát:** Phun nước, quạt
    3. **Bù dịch:** NS hoặc LR, uống hoặc IV
    4. **Nghỉ ngơi:** Trong môi trường mát
    
    **Theo dõi:**
    - Nhiệt độ mỗi 30 phút
    - Triệu chứng
    - Có thể xuất viện khi nhiệt độ <38°C và không có triệu chứng
    """)


def render_mild_heat_stroke():
    """Mild Heat Stroke Protocol"""
    st.error("## 🚨 SỐC NHIỆT NHẸ (Mild Heat Stroke)")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: >40°C
    - Rối loạn ý thức nhẹ: Lú lẫn, kích động
    - Không có co giật hoặc hôn mê
    
    **Điều trị:**
    1. **Làm mát ngay lập tức:**
       - Phun nước + quạt
       - Chườm đá: Nách, bẹn, cổ
       - Mục tiêu: <39°C trong 30 phút
    
    2. **Bù dịch:** NS hoặc LR, 1-2L
    
    3. **Theo dõi:**
       - Nhiệt độ mỗi 5-10 phút
       - Mức độ ý thức
       - Xét nghiệm: Điện giải, chức năng thận
    
    **Mục tiêu:**
    - Nhiệt độ <39°C trong 30 phút
    - Cải thiện ý thức
    - Không có biến chứng
    """)


def render_severe_heat_stroke():
    """Severe Heat Stroke Protocol"""
    st.error("## 🚨🚨 SỐC NHIỆT NẶNG (Severe Heat Stroke) - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: >40°C
    - Hôn mê hoặc co giật
    - Sốc
    - Rối loạn đông máu
    - Suy đa tạng
    
    **Điều trị khẩn cấp:**
    1. **ABC:** Ngay lập tức
    2. **Làm mát tích cực:**
       - Phun nước + quạt
       - Chườm đá
       - Rửa dạ dày/bàng quang nếu cần
       - Lọc máu nếu kháng trị
    
    3. **Điều trị hỗ trợ:**
       - Đặt nội khí quản nếu cần
       - Bù dịch: NS hoặc LR
       - Vasopressors nếu sốc
       - Điều trị co giật
    
    4. **ICU Monitoring:**
       - Continuous monitoring
       - Nhiệt độ mỗi 5 phút
       - Xét nghiệm mỗi 2-4 giờ
    
    **Mục tiêu:**
    - Nhiệt độ <39°C trong 30 phút
    - Ổn định huyết động
    - Không có biến chứng nặng
    """)

