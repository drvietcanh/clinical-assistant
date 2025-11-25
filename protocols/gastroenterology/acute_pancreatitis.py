"""
Acute Pancreatitis Protocol
ACG 2013, AGA 2018
Management of acute pancreatitis
"""

import streamlit as st


def render():
    """Acute Pancreatitis Protocol"""
    st.subheader("🫀 Viêm Tụy Cấp (Acute Pancreatitis)")
    st.caption("ACG 2013, AGA 2018 - Acute pancreatitis management")
    
    st.info("""
    **Viêm tụy cấp:**
    - Tần suất: ~40-50/100,000 người/năm
    - Nguyên nhân: Sỏi mật (40%), rượu (30%), khác (30%)
    - Tỷ lệ tử vong: 5-10% (nặng)
    
    **Chẩn đoán (≥2 trong 3):**
    1. Đau bụng đặc trưng
    2. Lipase/Amylase >3x ULN
    3. Hình ảnh (CT/MRI/US) phù hợp
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh Giá Mức Độ Nặng")
    
    severity_score = st.radio(
        "**Hệ thống đánh giá:**",
        ["Ranson Criteria", "BISAP Score", "APACHE II", "CT Severity Index"],
        key="pancreatitis_score"
    )
    
    st.markdown("---")
    
    if "Ranson" in severity_score:
        render_ranson()
    elif "BISAP" in severity_score:
        render_bisap()
    elif "APACHE" in severity_score:
        render_apache()
    else:
        render_ctsi()
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị")
    
    st.warning("""
    **1. Fluid Resuscitation (Ưu tiên hàng đầu):**
    - **Liều:** 250-500 mL/h trong 24-48 giờ đầu
    - **Loại:** Lactated Ringer (ưu tiên) hoặc Normal Saline
    - **Mục Tiêu:** Urine output ≥0.5 mL/kg/h
    - **Theo Dõi:** Dấu hiệu sống, BUN, Cr
    
    **2. Pain Management:**
    - **Opioid:** Morphine, fentanyl (không dùng meperidine)
    - **NSAID:** Có thể dùng nếu không chống chỉ định
    - **PCA:** Nếu đau nặng
    
    **3. Nutrition:**
    - **Early enteral feeding:** Trong vòng 24-48 giờ (nếu có thể)
    - **Route:** Nasogastric hoặc nasoduodenal
    - **Tránh:** NPO kéo dài (trừ khi không dung nạp)
    
    **4. Antibiotics:**
    - **Chỉ dùng khi:** Infected necrosis (có bằng chứng)
    - **Không dùng:** Prophylactic antibiotics
    - **Lựa chọn:** Carbapenem, quinolone + metronidazole
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 ERCP Indications")
    
    st.info("""
    **ERCP chỉ định khi:**
    - Viêm tụy cấp do sỏi mật + cholangitis
    - Viêm tụy cấp do sỏi mật + tắc nghẽn đường mật
    - Viêm tụy cấp do sỏi mật + không cải thiện sau 24 giờ
    
    **Timing:**
    - Trong vòng 24-72 giờ nếu có chỉ định
    - Không cần ERCP nếu không có cholangitis/tắc nghẽn
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Loại Mức Độ")
    
    severity = st.radio(
        "**Mức độ viêm tụy:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)"],
        key="pancreatitis_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_pancreatitis()
    elif "Trung bình" in severity:
        render_moderate_pancreatitis()
    else:
        render_severe_pancreatitis()
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Chẩn đoán (≥2 trong 3 tiêu chuẩn)",
        "✅ Đánh giá mức độ nặng (Ranson/BISAP/APACHE)",
        "✅ Truyền dịch tích cực (250-500 mL/h)",
        "✅ Giảm đau (opioid)",
        "✅ Early enteral feeding (24-48 giờ)",
        "✅ ERCP nếu có chỉ định (sỏi mật + cholangitis)",
        "✅ Theo dõi dấu hiệu sống, BUN, Cr",
        "✅ CT scan nếu không cải thiện sau 48-72 giờ",
        "✅ Điều trị nguyên nhân (sỏi mật, rượu)"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ biến chứng cao hơn
        - Cần theo dõi sát
        - Cẩn thận với truyền dịch (nguy cơ quá tải)
        
        **Suy thận:**
        - Cẩn thận với truyền dịch
        - Theo dõi BUN, Cr sát
        - Có thể cần RRT
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Nguyên nhân thường là sỏi mật
        - ERCP an toàn (với bảo vệ thai nhi)
        - Tránh CT scan nếu có thể
        
        **Trẻ em:**
        - Nguyên nhân thường khác (chấn thương, thuốc)
        - Liều truyền dịch tính theo kg
        - Theo dõi sát
        """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ACG 2013 Guidelines**
       - Tenner S, et al. Am J Gastroenterol. 2013
    
    2. **AGA 2018 Guidelines**
       - Crockett SD, et al. Gastroenterology. 2018
    
    3. **UpToDate:** Acute pancreatitis
       - Last updated: 2024
    
    4. **Medscape:** Acute Pancreatitis Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_ranson():
    """Ranson criteria"""
    st.info("## 📊 Ranson Criteria")
    
    st.markdown("""
    **On Admission:**
    - Age >55
    - WBC >16,000
    - Glucose >200 mg/dL
    - AST >250 U/L
    - LDH >350 U/L
    
    **48 Hours:**
    - Hct drop >10%
    - BUN increase >5 mg/dL
    - Ca <8 mg/dL
    - PaO2 <60 mmHg
    - Base deficit >4 mEq/L
    - Fluid sequestration >6 L
    
    **Điểm số:**
    - **0-2:** Nhẹ (tỷ lệ tử vong <1%)
    - **3-4:** Trung bình (tỷ lệ tử vong 15%)
    - **≥5:** Nặng (tỷ lệ tử vong 40%)
    """)


def render_bisap():
    """BISAP score"""
    st.info("## 📊 BISAP Score")
    
    st.markdown("""
    **5 tiêu chí (mỗi tiêu chí 1 điểm):**
    - **B:** BUN >25 mg/dL
    - **I:** Impaired mental status
    - **S:** SIRS (≥2 tiêu chí)
    - **A:** Age >60
    - **P:** Pleural effusion
    
    **Điểm số:**
    - **0-2:** Nguy cơ tử vong thấp (<2%)
    - **3-4:** Nguy cơ tử vong trung bình (5-15%)
    - **5:** Nguy cơ tử vong cao (>20%)
    """)


def render_apache():
    """APACHE II score"""
    st.info("## 📊 APACHE II Score")
    
    st.markdown("""
    **Đánh Giá:**
    - 12 tiêu chí (0-71 điểm)
    - Bao gồm: Tuổi, dấu hiệu sống, xét nghiệm
    
    **Điểm số:**
    - **<8:** Nhẹ
    - **8-15:** Trung bình
    - **>15:** Nặng
    """)


def render_ctsi():
    """CT Severity Index"""
    st.info("## 📊 CT Severity Index (CTSI)")
    
    st.markdown("""
    **Đánh giá trên CT:**
    - Phù tụy: 0-2 điểm
    - Hoại tử: 0-6 điểm
    
    **Điểm số:**
    - **0-3:** Nhẹ
    - **4-6:** Trung bình
    - **7-10:** Nặng
    """)


def render_mild_pancreatitis():
    """Mild pancreatitis protocol"""
    st.success("## 🟢 Viêm Tụy Cấp Nhẹ")
    
    st.markdown("""
    **Đặc điểm:**
    - Không có suy cơ quan
    - Không có biến chứng cục bộ
    - Tỷ lệ tử vong: <1%
    
    **Điều Trị:**
    1. **Truyền dịch:** 250-500 mL/h x 24-48 giờ
    2. **Giảm đau:** Opioid
    3. **Early enteral feeding:** Trong 24-48 giờ
    4. **Theo Dõi:** Dấu hiệu sống, BUN, Cr
    
    **Thời gian nằm viện:** 3-5 ngày
    """)


def render_moderate_pancreatitis():
    """Moderate pancreatitis protocol"""
    st.warning("## 🟡 Viêm Tụy Cấp Trung Bình")
    
    st.markdown("""
    **Đặc điểm:**
    - Có biến chứng cục bộ (pseudocyst, necrosis)
    - Không có suy cơ quan kéo dài
    - Tỷ lệ tử vong: 5-10%
    
    **Điều Trị:**
    1. **Truyền dịch:** 250-500 mL/h x 48-72 giờ
    2. **Giảm đau:** Opioid, có thể cần PCA
    3. **Early enteral feeding:** Trong 24-48 giờ
    4. **CT scan:** Nếu không cải thiện sau 48-72 giờ
    5. **Theo Dõi:** ICU nếu cần
    
    **Thời gian nằm viện:** 5-10 ngày
    """)


def render_severe_pancreatitis():
    """Severe pancreatitis protocol"""
    st.error("## 🔴 Viêm Tụy Cấp Nặng - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Suy cơ quan kéo dài (>48 giờ)
    - Có thể có hoại tử tụy
    - Tỷ lệ tử vong: 20-40%
    
    **Điều Trị:**
    1. **ICU care:**
       - Monitor liên tục
       - Hỗ trợ hô hấp nếu cần
       - Hỗ trợ huyết động nếu cần
    
    2. **Truyền dịch:** 250-500 mL/h, điều chỉnh theo đáp ứng
    
    3. **Giảm đau:** Opioid, PCA
    
    4. **Early enteral feeding:** Trong 24-48 giờ (nếu có thể)
    
    5. **CT scan:** Sau 48-72 giờ để đánh giá hoại tử
    
    6. **Antibiotics:** Chỉ khi có infected necrosis
    
    7. **Theo Dõi:** Dấu hiệu sống, BUN, Cr, lactate
    
    **Thời gian nằm viện:** 2-4 tuần hoặc lâu hơn
    """)

