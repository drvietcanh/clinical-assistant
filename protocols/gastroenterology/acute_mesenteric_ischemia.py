"""
Acute Mesenteric Ischemia Protocol
WSES 2017, SVS 2020
Management of acute mesenteric ischemia
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Mesenteric Ischemia Protocol"""
    st.subheader("🫀 Acute Mesenteric Ischemia")
    st.caption("WSES 2017, SVS 2020 - Management of acute mesenteric ischemia")
    
    st.error("""
    **🚨 ACUTE MESENTERIC ISCHEMIA = URGENT ASSESSMENT REQUIRED**
    
    **Triệu chứng:**
    - Đau bụng dữ dội, không tương xứng với khám
    - Buồn nôn, nôn
    - Tiêu chảy, có thể có máu
    - Sốt, nhiễm trùng
    - Tăng lactate, acidosis
    
    **Tỷ lệ tử vong cao nếu không điều trị sớm!**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại")
    
    ischemia_type = st.radio(
        "**Loại thiếu máu mạc treo:**",
        ["Arterial (Embolic/Thrombotic)", "Venous", "Non-occlusive"],
        key="mesenteric_ischemia_type"
    )
    
    st.markdown("---")
    
    if ischemia_type == "Arterial (Embolic/Thrombotic)":
        render_arterial_protocol()
    elif ischemia_type == "Venous":
        render_venous_protocol()
    else:
        render_nonocclusive_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 2: INITIAL ASSESSMENT ==========
    st.markdown("### ⚡ Đánh giá Ban Đầu")
    
    with st.expander("🔍 Xem đánh giá ban đầu", expanded=True):
        st.markdown("""
        **1. ABC (Airway, Breathing, Circulation):**
        - **Airway:** Đảm bảo thông thoáng
        - **Breathing:** Đánh giá suy hô hấp
        - **Circulation:** Đánh giá shock, tưới máu
        
        **2. Dấu hiệu nguy hiểm:**
        - Đau bụng dữ dội, không tương xứng
        - Sốc, hạ huyết áp
        - Tăng lactate (> 2 mmol/L)
        - Acidosis nặng (pH < 7.2)
        - Peritonitis
        - Lú lẫn, kích động
        
        **3. Xét nghiệm cần thiết:**
        - **Lactate:** Tăng (> 2 mmol/L)
        - **ABG:** Acidosis
        - **D-dimer:** Tăng
        - **CBC:** Tăng WBC, có thể giảm platelets
        - **BMP:** Tăng creatinine, tăng K+
        - **LFTs:** Có thể tăng
        - **CT angiography:** Tiêu chuẩn vàng
        - **Mesenteric angiography:** Nếu nghi ngờ
        
        **4. Imaging:**
        - **CT angiography:** Ưu tiên (nhanh, chính xác)
        - **Mesenteric angiography:** Nếu cần can thiệp
        - **Plain X-ray:** Có thể thấy ileus, free air
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: RESUSCITATION ==========
    st.markdown("### 💉 Resuscitation")
    
    st.markdown("""
    **1. Fluid Resuscitation:**
    - **NS/LR:** 1-2 L bolus
    - **Mục tiêu:** MAP ≥ 65 mmHg
    - **Theo dõi:** CVP, lượng nước tiểu
    
    **2. Vasopressors:**
    - **Norepinephrine:** 0.05-0.5 mcg/kg/min
    - **Mục tiêu:** MAP ≥ 65 mmHg
    - **Lưu ý:** Tránh vasopressin (có thể làm nặng thêm)
    
    **3. Correction of Acidosis:**
    - **Sodium bicarbonate:** Cân nhắc nếu pH < 7.2
    - **Mục tiêu:** pH ≥ 7.2
    
    **4. Electrolytes:**
    - **K+:** Điều chỉnh nếu tăng
    - **Ca2+:** Bổ sung nếu giảm
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: ANTICOAGULATION ==========
    st.markdown("### 💊 Anticoagulation")
    
    with st.expander("📋 Xem liều thuốc chống đông", expanded=False):
        st.markdown("""
        **Heparin:**
        - **Bolus:** 80 units/kg IV
        - **Infusion:** 18 units/kg/h
        - **Mục tiêu:** aPTT 1.5-2.5x normal
        - **Chỉ định:** Tất cả loại (trừ chống chỉ định)
        
        **LMWH:**
        - **Enoxaparin:** 1 mg/kg SC q12h
        - **Chỉ định:** Sau khi ổn định
        
        **Lưu ý:**
        - Bắt đầu ngay khi chẩn đoán
        - Trừ khi có chống chỉ định rõ ràng
        - Tiếp tục sau phẫu thuật
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SURGICAL MANAGEMENT ==========
    st.markdown("### 🔪 Surgical Management")
    
    with st.expander("🏥 Xem chỉ định phẫu thuật", expanded=False):
        st.markdown("""
        **Chỉ định:**
        - **Peritonitis:** Dấu hiệu thủng ruột
        - **Free air:** Trên X-ray/CT
        - **Progressive:** Không đáp ứng với điều trị nội khoa
        - **Arterial occlusion:** Cần revascularization
        
        **Procedures:**
        - **Exploratory laparotomy:** Đánh giá tổn thương
        - **Resection:** Cắt bỏ ruột hoại tử
        - **Revascularization:** Khôi phục tưới máu
        - **Second-look:** 24-48h sau (nếu cần)
        
        **Timing:**
        - **Emergent:** Nếu peritonitis, free air
        - **Urgent:** Nếu không đáp ứng với điều trị nội khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: PROGNOSIS ==========
    st.markdown("### 📊 Prognosis")
    
    st.markdown("""
    **Yếu tố tiên lượng tốt:**
    - Chẩn đoán sớm (< 12 giờ)
    - Venous hoặc non-occlusive
    - Không có peritonitis
    - Lactate < 4 mmol/L
    - pH ≥ 7.2
    
    **Yếu tố tiên lượng xấu:**
    - Chẩn đoán muộn (> 24 giờ)
    - Arterial occlusion
    - Peritonitis, free air
    - Lactate > 4 mmol/L
    - pH < 7.2
    - Tuổi cao, bệnh nền nặng
    
    **Tỷ lệ tử vong:**
    - **Sớm (< 12h):** 20-30%
    - **Muộn (> 24h):** 60-80%
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Tỷ lệ tử vong cao hơn
        - Triệu chứng không điển hình
        - Cần chẩn đoán sớm
        - Cân nhắc chất lượng cuộc sống
        
        **Bệnh nhân có bệnh nền:**
        - **AF:** Tăng nguy cơ embolic
        - **CAD:** Tăng nguy cơ thrombotic
        - **Hypercoagulable:** Tăng nguy cơ
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Hiếm gặp
        - Cần tư vấn sản khoa
        - Cẩn thận với imaging
        - Cân nhắc anticoagulation
        
        **Trẻ em:**
        - Hiếm gặp
        - Thường do nguyên nhân khác
        - Cần tư vấn nhi khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    render_references_section(get_references("acute_mesenteric_ischemia"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_arterial_protocol():
    """Arterial (Embolic/Thrombotic) Protocol"""
    st.error("## 🚨 ARTERIAL (EMBOLIC/THROMBOTIC) ISCHEMIA")
    
    st.markdown("""
    **Đặc điểm:**
    - **Embolic:** Khởi phát đột ngột, thường SMA
    - **Thrombotic:** Khởi phát từ từ, thường do atherosclerosis
    
    **Quy trình:**
    
    1. **Resuscitation:**
       - Fluid, vasopressors
       - Correction of acidosis
    
    2. **Anticoagulation:**
       - **Heparin:** Bolus 80 units/kg, infusion 18 units/kg/h
       - Mục tiêu: aPTT 1.5-2.5x normal
    
    3. **Revascularization:**
       - **Endovascular:** Thrombolysis, angioplasty, stenting
       - **Surgical:** Embolectomy, bypass
       - **Timing:** Càng sớm càng tốt
    
    4. **Surgery:**
       - Nếu peritonitis, free air
       - Resection ruột hoại tử
       - Second-look 24-48h
    
    5. **Theo dõi:**
       - Lactate, ABG
       - Clinical exam
       - CT nếu cần
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Embolic thường ở SMA (superior mesenteric artery)
    - Thrombotic thường ở celiac/SMA origins
    - Cần revascularization sớm
    - Tỷ lệ tử vong cao nếu muộn
    """)


def render_venous_protocol():
    """Venous Protocol"""
    st.warning("## ⚠️ VENOUS ISCHEMIA")
    
    st.markdown("""
    **Đặc điểm:**
    - Khởi phát từ từ hơn
    - Thường do hypercoagulable state
    - Tiên lượng tốt hơn arterial
    
    **Quy trình:**
    
    1. **Resuscitation:**
       - Fluid, vasopressors
       - Correction of acidosis
    
    2. **Anticoagulation:**
       - **Heparin:** Bolus 80 units/kg, infusion 18 units/kg/h
       - Mục tiêu: aPTT 1.5-2.5x normal
       - Chuyển sang LMWH sau ổn định
    
    3. **Thrombolysis:**
       - Cân nhắc nếu early (< 48h)
       - Trong OR với interventional radiology
    
    4. **Surgery:**
       - Chỉ nếu peritonitis, free air
       - Resection ruột hoại tử
       - Second-look 24-48h
    
    5. **Theo dõi:**
       - Lactate, ABG
       - Clinical exam
       - CT nếu cần
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Tiên lượng tốt hơn arterial
    - Thường đáp ứng với anticoagulation
    - Cần tìm nguyên nhân hypercoagulable
    - Có thể cần anticoagulation lâu dài
    """)


def render_nonocclusive_protocol():
    """Non-occlusive Protocol"""
    st.warning("## ⚠️ NON-OCCLUSIVE ISCHEMIA")
    
    st.markdown("""
    **Đặc điểm:**
    - Không có occlusion mạch máu
    - Thường do low flow state
    - Tiên lượng phụ thuộc vào nguyên nhân
    
    **Quy trình:**
    
    1. **Resuscitation:**
       - Fluid, vasopressors
       - Correction of acidosis
       - **Lưu ý:** Tránh vasopressin (có thể làm nặng thêm)
    
    2. **Điều trị nguyên nhân:**
       - **Heart failure:** Inotropes, diuretics
       - **Shock:** Fluid, vasopressors
       - **Sepsis:** Antibiotics, source control
    
    3. **Vasodilators:**
       - **Papaverine:** 30-60 mg/h IV (nếu có)
       - Có thể cải thiện tưới máu
    
    4. **Anticoagulation:**
       - **Heparin:** Cân nhắc
       - Không rõ lợi ích
    
    5. **Surgery:**
       - Chỉ nếu peritonitis, free air
       - Resection ruột hoại tử
       - Second-look 24-48h
    
    6. **Theo dõi:**
       - Lactate, ABG
       - Clinical exam
       - CT nếu cần
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Điều trị nguyên nhân là quan trọng nhất
    - Tránh vasopressin
    - Cân nhắc vasodilators
    - Tiên lượng phụ thuộc vào nguyên nhân
    """)

