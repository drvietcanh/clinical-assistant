"""
Hypoglycemia Protocol
ADA Guidelines
Management of low blood glucose
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hypoglycemia Protocol"""
    st.subheader("🍭 Hạ đường huyết (Hypoglycemia)")
    st.caption("ADA Guidelines - Low blood glucose management")
    
    st.error("""
    **⚠️ HẠ ĐƯỜNG HUYẾT = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Đường huyết <70 mg/dL (<3.9 mmol/L)
    - **Có triệu chứng:** Run, vã mồ hôi, lo âu, đói, lú lẫn, hôn mê
    - **Nghiêm trọng:** Cần hỗ trợ người khác để điều trị
    
    **Nguyên nhân:**
    - Thuốc đái tháo đường (insulin, sulfonylureas)
    - Nhịn ăn kéo dài
    - Uống rượu
    - Suy gan, thận
    - U tụy (insulinoma)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng tự chủ (Autonomic):**
        - Run (tremor)
        - Vã mồ hôi (diaphoresis)
        - Lo âu (anxiety)
        - Đói (hunger)
        - Đánh trống ngực (palpitations)
        - Tăng huyết áp, nhịp nhanh
        """)
    
    with col2:
        st.markdown("""
        **Triệu chứng thần kinh:**
        - Lú lẫn (confusion)
        - Yếu, mệt mỏi
        - Rối loạn thị giác
        - Co giật (seizures)
        - Hôn mê (coma)
        - Tử vong (nếu không điều trị)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: SEVERITY ASSESSMENT ==========
    st.markdown("### 📊 Phân loại mức độ")
    
    severity = st.radio(
        "**Mức độ hạ đường huyết:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)"],
        key="hypoglycemia_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_hypoglycemia()
    elif "Trung bình" in severity:
        render_moderate_hypoglycemia()
    else:
        render_severe_hypoglycemia()
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE TREATMENT ==========
    st.markdown("### 🚨 Điều trị ngay lập tức")
    
    st.error("""
    **1. Đo đường huyết:**
    - Đo ngay nếu nghi ngờ
    - Không chờ kết quả nếu bệnh nhân hôn mê
    
    **2. Điều trị ngay:**
    - **Nếu tỉnh táo:** Cho uống đường (15-20g glucose)
    - **Nếu hôn mê:** Dextrose 50% 50 mL IV hoặc Glucagon 1 mg IM
    
    **3. Theo dõi:**
    - Đo lại đường huyết sau 15 phút
    - Lặp lại nếu cần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT OPTIONS ==========
    st.markdown("### 💊 Các phương pháp điều trị")
    
    st.markdown("#### **1. Đường uống (Nếu tỉnh táo)**")
    
    st.success("""
    **Lựa chọn (15-20g glucose):**
    - **Glucose tablets:** 3-4 viên
    - **Nước đường:** 4 muỗng cà phê đường trong nước
    - **Nước ngọt:** 150-200 mL (không diet)
    - **Kẹo:** 5-6 viên
    - **Mật ong:** 1 muỗng canh
    
    **Sau 15 phút:**
    - Đo lại đường huyết
    - Lặp lại nếu <70 mg/dL
    - Ăn bữa ăn nhẹ nếu đã ổn định
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Dextrose IV (Nếu hôn mê hoặc không uống được)**")
    
    st.warning("""
    **Dextrose 50% (D50):**
    - **Liều:** 50 mL IV (25g glucose)
    - **Tốc độ:** Bolus nhanh
    - **Lặp lại:** Nếu cần sau 15 phút
    
    **Dextrose 10% (D10):**
    - **Liều:** 250-500 mL IV
    - **Dùng khi:** Cần duy trì đường huyết
    
    **Lưu ý:**
    - Cẩn thận thấm dịch (extravasation)
    - Theo dõi đường huyết
    """)
    
    st.markdown("---")
    
    st.markdown("#### **3. Glucagon IM (Nếu không có đường truyền)**")
    
    st.info("""
    **Glucagon:**
    - **Liều:** 1 mg IM (hoặc SC)
    - **Tác dụng:** Kích thích gan giải phóng glucose
    - **Hiệu quả:** Sau 10-15 phút
    
    **Lưu ý:**
    - Không hiệu quả nếu gan không có glycogen (nhịn ăn, uống rượu)
    - Có thể gây nôn
    - Cần ăn sau khi tỉnh
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL SITUATIONS ==========
    st.markdown("### 🔍 Tình huống đặc biệt")
    
    st.markdown("#### **Sulfonylurea Overdose**")
    
    st.error("""
    **Đặc điểm:**
    - Hạ đường huyết kéo dài (có thể vài ngày)
    - Cần điều trị tích cực
    
    **Điều trị:**
    - Dextrose IV liên tục
    - Octreotide: 50-100 mcg SC q6-8h (ức chế giải phóng insulin)
    - Theo dõi sát trong 24-48 giờ
    """)
    
    st.markdown("---")
    
    st.markdown("#### **Uống rượu**")
    
    st.warning("""
    **Đặc điểm:**
    - Rượu ức chế tân tạo glucose
    - Hạ đường huyết có thể kéo dài
    - Glucagon không hiệu quả
    
    **Điều trị:**
    - Dextrose IV
    - Thiamine: 100 mg IV (phòng Wernicke encephalopathy)
    - Theo dõi sát
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    **Giáo dục bệnh nhân:**
    - Nhận biết triệu chứng sớm
    - Luôn mang theo đường
    - Đo đường huyết thường xuyên
    - Ăn đúng giờ
    
    **Điều chỉnh thuốc:**
    - Giảm liều insulin/sulfonylurea nếu hạ đường huyết tái phát
    - Tránh bỏ bữa
    - Điều chỉnh liều khi tập thể dục
    
    **Theo dõi:**
    - HbA1c
    - Tần suất hạ đường huyết
    - Điều chỉnh mục tiêu đường huyết nếu cần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Đường huyết:** Mỗi 15 phút đến khi ổn định
    - **Triệu chứng:** Run, vã mồ hôi, lú lẫn
    - **Dấu hiệu sinh tồn:** BP, HR
    
    **Dấu hiệu cải thiện:**
    - Tăng đường huyết (>100 mg/dL)
    - Hết triệu chứng
    - Tỉnh táo
    
    **Dấu hiệu xấu đi:**
    - Đường huyết tiếp tục giảm
    - Hôn mê
    - Co giật
    - Cần điều trị tích cực
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    references = get_references("Hypoglycemia")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **ADA Standards of Medical Care** - Hypoglycemia (2024)
        2. **UpToDate:** Hypoglycemia in adults - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_hypoglycemia():
    """Mild Hypoglycemia"""
    st.success("## ⚠️ MILD HYPOGLYCEMIA")
    
    st.markdown("""
    **Triệu chứng:**
    - Run, vã mồ hôi, lo âu
    - Đường huyết: 50-70 mg/dL
    - Tỉnh táo
    
    **Điều trị:**
    1. **Cho uống đường:** 15-20g glucose
    2. **Đo lại sau 15 phút**
    3. **Lặp lại nếu cần**
    4. **Ăn bữa ăn nhẹ** nếu đã ổn định
    
    **Tiên lượng:** Tốt, thường tự khỏi
    """)


def render_moderate_hypoglycemia():
    """Moderate Hypoglycemia"""
    st.warning("## 🚨 MODERATE HYPOGLYCEMIA")
    
    st.markdown("""
    **Triệu chứng:**
    - Lú lẫn, yếu
    - Đường huyết: 30-50 mg/dL
    - Có thể tự điều trị hoặc cần hỗ trợ
    
    **Điều trị:**
    1. **Cho uống đường:** 15-20g glucose (nếu có thể)
    2. **Hoặc:** Dextrose 50% 25-50 mL IV
    3. **Đo lại sau 15 phút**
    4. **Lặp lại nếu cần**
    5. **Ăn bữa ăn nhẹ** sau khi ổn định
    
    **Tiên lượng:** Tốt với điều trị
    """)


def render_severe_hypoglycemia():
    """Severe Hypoglycemia"""
    st.error("## 🚨🚨 SEVERE HYPOGLYCEMIA - EMERGENCY")
    
    st.markdown("""
    **Triệu chứng:**
    - Hôn mê, co giật
    - Đường huyết: <30 mg/dL
    - Cần hỗ trợ người khác
    
    **Điều trị ngay:**
    1. **Dextrose 50%:** 50 mL IV bolus
    2. **Hoặc:** Glucagon 1 mg IM (nếu không có đường truyền)
    3. **Theo dõi:** Đo lại đường huyết sau 15 phút
    4. **Lặp lại:** Nếu cần
    5. **Duy trì:** Dextrose 10% IV nếu cần
    
    **Theo dõi sát:**
    - Đường huyết mỗi 15 phút
    - Triệu chứng thần kinh
    - Dấu hiệu sinh tồn
    
    **Tiên lượng:** Nghiêm trọng, cần điều trị tích cực
    """)

