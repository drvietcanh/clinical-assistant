"""
Severe Hypoglycemia Protocol
ADA Guidelines 2024, Endocrine Society 2023
Life-threatening condition requiring immediate treatment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Severe Hypoglycemia Management Protocol"""
    st.subheader("🍭 Hạ Đường Huyết Cấp Cứu (Severe Hypoglycemia)")
    st.caption("ADA Guidelines 2024, Endocrine Society 2023 - Life-threatening condition")
    
    st.error("""
    **⚠️ HẠ ĐƯỜNG HUYẾT NẶNG = CẤP CỨU Y KHOA**
    
    **Định nghĩa:**
    - **Hạ đường huyết:** Glucose <70 mg/dL (3.9 mmol/L)
    - **Hạ đường huyết nặng:** Glucose <54 mg/dL (3.0 mmol/L) + Triệu chứng
    - **Hạ đường huyết rất nặng:** Giảm ý thức, không thể tự điều trị
    
    **Triệu chứng Điển Hình:**
    - **Thần kinh tự động:** Run tay, vã mồ hôi, tim đập nhanh, đói
    - **Thần kinh:** Lú lẫn, yếu, mệt, co giật, hôn mê
    - **Tim mạch:** Rối loạn nhịp tim, đau ngực
    - **Không triệu chứng:** (Hypoglycemia unawareness)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức nặng (GCS <8)
        - Suy hô hấp
        - Co giật không kiểm soát
        
        **Oxygen:**
        - 2-4 L/min qua nasal cannula
        - Nếu SpO₂ <90%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG** (rối loạn nhịp tim)
        - **BP, HR:** Mỗi 5-15 phút
        - **Glucose:** Mỗi 15-30 phút
        """)
    
    with col2:
        st.warning("""
        **3. GLUCOSE CHECK**
        
        **Ngay lập tức:**
        - **Fingerstick glucose** (nếu có)
        - **Lab glucose** (nếu có)
        - **Không chờ kết quả** nếu nghi ngờ cao
        
        **4. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị truyền glucose
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Mức độ Nghiêm trọng")
    
    # Glucose level
    glucose = st.number_input(
        "**Nồng độ Glucose (mg/dL):**",
        min_value=0,
        max_value=500,
        value=0,
        step=5,
        help="Nồng độ glucose trong máu"
    )
    
    if glucose > 0:
        if glucose >= 70:
            st.success("✅ **Glucose bình thường** - Không hạ đường huyết")
        elif glucose >= 54:
            st.warning("⚠️ **Hạ đường huyết nhẹ** - Cần điều trị")
        elif glucose >= 40:
            st.error("🚨 **Hạ đường huyết nặng** - Điều trị ngay!")
        else:
            st.error("🚨🚨 **Hạ đường huyết rất nặng** - Điều trị cấp cứu!")
    
    # Mental status
    mental_status = st.radio(
        "**Tình trạng ý thức:**",
        ["Tỉnh táo, có thể uống", "Lú lẫn, không thể uống", "Hôn mê, không đáp ứng"],
        key="hypo_mental_status"
    )
    
    # Check for symptoms
    has_seizure = st.checkbox("Co giật", key="hypo_seizure")
    has_arrhythmia = st.checkbox("Rối loạn nhịp tim", key="hypo_arrhythmia")
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Đặc hiệu")
    
    if mental_status == "Tỉnh táo, có thể uống":
        st.success("## ⚠️ ĐIỀU TRỊ - Bệnh nhân Tỉnh táo")
        
        st.markdown("""
        **1. GLUCOSE PO (Ưu tiên)**
        
        **Liều:**
        - **15-20 g glucose** (tương đương):
          - 4 viên glucose (4g mỗi viên)
          - 120-180 mL nước trái cây
          - 1 thìa canh đường/mật ong
          - 150-200 mL soda (không diet)
        
        **Đánh giá sau 15 phút:**
        - Nếu glucose vẫn <70: Lặp lại 15-20 g
        - Nếu glucose ≥70: Cho ăn bữa ăn/bữa phụ
        
        **Lưu ý:**
        - Không dùng quá nhiều (gây tăng đường huyết phản ứng)
        - Theo dõi glucose mỗi 15 phút
        """)
        
    elif mental_status == "Lú lẫn, không thể uống":
        st.warning("## 🚨 ĐIỀU TRỊ - Bệnh nhân Lú lẫn")
        
        st.markdown("""
        **1. GLUCOSE IV (Ưu tiên)**
        
        **Dextrose 50% (D50):**
        - **Liều:** 50 mL (25 g glucose) IV bolus
        - **Tốc độ:** Trong 1-3 phút
        - **Lặp lại:** Nếu glucose vẫn <70 sau 15 phút
        
        **Hoặc Dextrose 10%:**
        - **Liều:** 250 mL (25 g glucose) IV
        - **Tốc độ:** Trong 5-10 phút
        
        **2. GLUCAGON IM (Nếu không có đường tĩnh mạch)**
        
        **Liều:**
        - **Người lớn:** 1 mg IM
        - **Trẻ em:** 0.5 mg IM (<20 kg) hoặc 1 mg IM (≥20 kg)
        
        **Hiệu quả:**
        - Bắt đầu: 10-15 phút
        - Tối đa: 20-30 phút
        
        **Lưu ý:**
        - Chỉ hiệu quả nếu còn glycogen dự trữ
        - Có thể gây nôn
        """)
        
    else:  # Comatose
        st.error("## 🚨🚨 ĐIỀU TRỊ - Bệnh nhân Hôn mê")
        
        st.markdown("""
        **1. GLUCOSE IV (Ngay lập tức)**
        
        **Dextrose 50% (D50):**
        - **Liều:** 50-100 mL (25-50 g glucose) IV bolus
        - **Tốc độ:** Trong 1-3 phút
        - **Lặp lại:** Nếu glucose vẫn <70 sau 15 phút
        
        **2. TRUYỀN GLUCOSE LIÊN TỤC (Nếu cần)**
        
        **Dextrose 10%:**
        - **Tốc độ:** 100-200 mL/h
        - **Mục tiêu:** Glucose 100-180 mg/dL
        - **Theo dõi:** Glucose mỗi 30-60 phút
        
        **3. GLUCAGON IM (Nếu không có đường tĩnh mạch)**
        
        - **Liều:** 1-2 mg IM
        - **Lặp lại:** Nếu cần sau 15-20 phút
        """)
    
    if has_seizure:
        st.error("""
        **4. CO GIẬT**
        
        **Điều trị:**
        1. **Glucose IV:** (ưu tiên, thường hết co giật)
        2. **Benzodiazepines:** Nếu co giật kéo dài
           - **Lorazepam:** 2-4 mg IV
           - **Diazepam:** 5-10 mg IV
        
        **Lưu ý:**
        - Co giật do hạ đường huyết thường hết sau khi glucose bình thường
        - Tránh dùng thuốc chống co giật không cần thiết
        """)
    
    if has_arrhythmia:
        st.warning("""
        **5. RỐI LOẠN NHỊP TIM**
        
        **Điều trị:**
        1. **Glucose IV:** (ưu tiên)
        2. **Theo dõi ECG:** Liên tục
        3. **Điều trị loạn nhịp:** Nếu cần (sau khi glucose bình thường)
        
        **Lưu ý:**
        - Rối loạn nhịp thường hết sau khi glucose bình thường
        - Tránh điều trị loạn nhịp không cần thiết
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Tìm Nguyên nhân")
    
    with st.expander("📋 Xem các nguyên nhân thường gặp", expanded=False):
        st.markdown("""
        **Thuốc (Phổ biến nhất):**
        - **Insulin:** Quá liều, sai thời điểm
        - **Sulfonylureas:** Quá liều, tương tác thuốc
        - **Meglitinides:** Quá liều
        - **Tương tác thuốc:** Quinine, Pentamidine, etc.
        
        **Bệnh lý:**
        - **Suy thận:** Giảm thải trừ insulin
        - **Suy gan:** Giảm tạo glucose
        - **Suy thượng thận:** Thiếu cortisol
        - **Suy giáp:** Giảm chuyển hóa
        - **Nhiễm trùng:** Tăng tiêu thụ glucose
        
        **Chế độ ăn:**
        - Bỏ bữa
        - Ăn ít carbohydrate
        - Uống rượu (ức chế tạo glucose)
        
        **Vận động:**
        - Vận động quá mức
        - Không điều chỉnh insulin
        
        **Khác:**
        - Insulinoma
        - Bệnh tự miễn (anti-insulin antibodies)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Theo dõi Glucose:**
    - **Mỗi 15 phút:** Cho đến khi glucose ≥70
    - **Mỗi 30-60 phút:** Sau khi glucose ổn định
    - **Mục tiêu:** Glucose 100-180 mg/dL (tránh tăng quá cao)
    
    **2. Bữa ăn/Bữa phụ:**
    - **Sau khi glucose ≥70:** Cho ăn bữa ăn hoặc bữa phụ
    - **Carbohydrate:** 15-30 g
    - **Protein:** 10-15 g (duy trì glucose)
    
    **3. Điều chỉnh Thuốc:**
    - **Ngừng insulin/sulfonylurea:** Nếu quá liều
    - **Giảm liều:** Nếu hạ đường huyết tái phát
    - **Điều chỉnh:** Theo nguyên nhân
    
    **4. Điều trị Nguyên nhân:**
    - **Suy thận:** Điều chỉnh liều insulin
    - **Nhiễm trùng:** Điều trị nhiễm trùng
    - **Suy thượng thận:** Bổ sung cortisol
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Lưu ý Đặc biệt")
    
    st.warning("""
    **1. Sulfonylurea Overdose:**
    - Hạ đường huyết có thể kéo dài 24-48h
    - Cần truyền glucose liên tục
    - Có thể cần Octreotide
    
    **2. Insulin Overdose:**
    - Hạ đường huyết có thể kéo dài vài giờ
    - Theo dõi sát glucose
    - Có thể cần truyền glucose liên tục
    
    **3. Hypoglycemia Unawareness:**
    - Bệnh nhân không cảm nhận được hạ đường huyết
    - Nguy cơ cao hạ đường huyết nặng
    - Cần điều chỉnh mục tiêu glucose cao hơn
    
    **4. Tăng đường huyết Phản ứng (Rebound Hyperglycemia):**
    - Sau khi điều trị hạ đường huyết
    - Không cần điều trị trừ khi glucose >250-300
    - Theo dõi và điều chỉnh thuốc
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Tốt:** Nếu điều trị sớm và đúng
    - **Xấu:** Nếu hạ đường huyết kéo dài (tổn thương não)
    - **Yếu tố nguy cơ:**
      - Hạ đường huyết nặng (glucose <40)
      - Hạ đường huyết kéo dài
      - Co giật
      - Hôn mê
    
    **Theo dõi:**
    - **Glucose:** Mỗi 15-30 phút (cho đến khi ổn định)
    - **Triệu chứng:** Mỗi 15-30 phút
    - **ECG:** Nếu có rối loạn nhịp
    - **Thần kinh:** Đánh giá chức năng thần kinh
    
    **Xuất viện:**
    - Glucose ổn định ≥70
    - Không triệu chứng
    - Đã điều chỉnh thuốc
    - Bệnh nhân hiểu cách phòng ngừa
    - Theo dõi ít nhất 2-4h
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Điều chỉnh theo Đặc điểm Bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ cao hơn
        - Có thể không có triệu chứng điển hình
        - Thận trọng với glucose thấp
        - Mục tiêu glucose: 100-180 mg/dL
        
        **Suy thận:**
        - Giảm thải trừ insulin
        - Cần giảm liều insulin
        - Theo dõi sát glucose
        
        **Suy gan:**
        - Giảm tạo glucose
        - Cần truyền glucose liên tục
        - Theo dõi sát glucose
        """)
    
    with col2:
        st.markdown("""
        **Trẻ em:**
        - Liều glucose: 0.5-1 g/kg
        - Glucagon: 0.5 mg IM (<20 kg)
        - Theo dõi sát hơn
        
        **Có thai:**
        - Hạ đường huyết nguy hiểm cho thai nhi
        - Điều trị tích cực
        - Mục tiêu glucose: 70-140 mg/dL
        
        **Đái tháo đường type 1:**
        - Nguy cơ cao hơn
        - Cần điều chỉnh insulin
        - Giáo dục bệnh nhân
        """)
    
    st.markdown("---")
    
    # References
    references = get_references("Severe Hypoglycemia")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ADA Guidelines 2024** - American Diabetes Association
        2. **Endocrine Society Guidelines 2023** - Endocrine Society
        3. **UpToDate:** Hypoglycemia in Adults - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

