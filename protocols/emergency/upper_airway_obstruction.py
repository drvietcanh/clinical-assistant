"""
Acute Upper Airway Obstruction Protocol
AHA 2020, ATLS 2021
Management of acute upper airway obstruction
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Upper Airway Obstruction Protocol"""
    st.subheader("🫀 Acute Upper Airway Obstruction")
    st.caption("AHA 2020, ATLS 2021 - Management of acute upper airway obstruction")
    
    st.error("""
    **🚨 ACUTE UPPER AIRWAY OBSTRUCTION = IMMEDIATE LIFE-THREATENING EMERGENCY**
    
    **Triệu chứng:**
    - Khó thở, stridor (tiếng thở rít)
    - Thở nhanh, tăng công thở
    - Tím tái, vã mồ hôi
    - Không nói được, ho khan
    - Kích động, lú lẫn
    
    **Cần xử trí ngay lập tức - Có thể đe dọa tính mạng trong vài phút!**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CAUSES ==========
    st.markdown("### 🔍 Nguyên nhân")
    
    cause = st.selectbox(
        "**Nguyên nhân:**",
        [
            "Chọn nguyên nhân...",
            "Anaphylaxis",
            "Epiglottitis",
            "Croup (Laryngotracheobronchitis)",
            "Foreign Body Aspiration",
            "Angioedema",
            "Laryngeal Edema",
            "Retropharyngeal Abscess",
            "Peritonsillar Abscess",
            "Trauma",
            "Burns (Inhalation)"
        ],
        key="airway_cause"
    )
    
    st.markdown("---")
    
    if cause != "Chọn nguyên nhân...":
        render_cause_specific_protocol(cause)
    
    st.markdown("---")
    
    # ========== SECTION 2: INITIAL ASSESSMENT ==========
    st.markdown("### ⚡ Đánh giá Ban Đầu")
    
    with st.expander("🔍 Xem đánh giá ban đầu", expanded=True):
        st.markdown("""
        **1. ABC (Airway, Breathing, Circulation):**
        - **Airway:** Đánh giá tắc nghẽn, stridor, ho
        - **Breathing:** Tần số thở, công thở, SpO₂
        - **Circulation:** Mạch, huyết áp, tưới máu
        
        **2. Dấu hiệu nguy hiểm:**
        - Stridor nặng, không nói được
        - Tần số thở < 8 hoặc > 40 lần/phút
        - SpO₂ < 90% với O₂ hỗ trợ
        - Lú lẫn, kích động, hôn mê
        - Tím tái, vã mồ hôi
        - Mệt mỏi cơ hô hấp
        
        **3. Xét nghiệm cần thiết:**
        - **Lateral neck X-ray:** Đánh giá đường thở
        - **Chest X-ray:** Nếu nghi ngờ foreign body
        - **CT neck:** Nếu nghi ngờ abscess
        - **Labs:** CBC, cultures (nếu nhiễm trùng)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE MANAGEMENT ==========
    st.markdown("### ⚡ Xử trí Ngay Lập Tức")
    
    st.markdown("""
    **1. Position:**
    - Đặt bệnh nhân ở tư thế thoải mái nhất
    - Tránh nằm ngửa nếu có thể
    - Trẻ em: Ngồi trên lòng cha mẹ
    
    **2. Oxygen:**
    - **High-flow O₂:** 100% qua face mask
    - **Heliox:** 70/30 hoặc 80/20 (nếu có)
    - **Mục tiêu:** SpO₂ ≥ 90%
    
    **3. Medications:**
    - **Epinephrine (racemic):** 0.5 mL 2.25% nebulized (croup, anaphylaxis)
    - **Corticosteroids:**
      - **Dexamethasone:** 0.6 mg/kg IV/IM/PO (max 10 mg)
      - **Methylprednisolone:** 1-2 mg/kg IV
    - **Antihistamines:** Diphenhydramine 1 mg/kg IV (anaphylaxis)
    
    **4. Intubation:**
    - Chỉ định nếu:
      - SpO₂ < 90% với O₂ hỗ trợ
      - Mệt mỏi cơ hô hấp
      - Lú lẫn, hôn mê
    - **RSI:** Cần chuẩn bị kỹ, có thể khó
    - **Surgical airway:** Cân nhắc nếu intubation thất bại
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: EMERGENCY CRICOTHYROTOMY ==========
    st.markdown("### 🔪 Emergency Cricothyrotomy")
    
    with st.expander("⚠️ Xem chỉ định và kỹ thuật cricothyrotomy", expanded=False):
        st.markdown("""
        **Chỉ định:**
        - Không thể intubate, không thể ventilate
        - Tắc nghẽn đường thở trên hoàn toàn
        - Chấn thương mặt/đường thở nặng
        
        **Kỹ thuật (Needle Cricothyrotomy):**
        1. Xác định vị trí: Giữa cricoid và thyroid cartilage
        2. Chọc kim 14-16G qua màng cricothyroid
        3. Kết nối với 3 mL syringe
        4. Kết nối với O₂ source (15 L/min với Y-connector)
        5. Ventilate: 1 giây on, 4 giây off
        
        **Kỹ thuật (Surgical Cricothyrotomy):**
        1. Rạch da ngang 2-3 cm
        2. Rạch màng cricothyroid
        3. Đặt tube 6.0-7.0 mm
        4. Cố định tube
        
        **Lưu ý:**
        - Chỉ là biện pháp tạm thời
        - Cần chuyển sang tracheostomy trong 24-48h
        - Biến chứng: Chảy máu, tổn thương cấu trúc, nhiễm trùng
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - **Croup:** Phổ biến nhất (6 tháng - 3 tuổi)
        - **Epiglottitis:** Hiếm hơn (do vaccine)
        - **Foreign body:** Phổ biến ở trẻ nhỏ
        - **Liều thuốc:** Dựa trên cân nặng
        - **Intubation:** Khó hơn, cần ống nhỏ hơn
        
        **Người cao tuổi:**
        - **Angioedema:** Có thể do ACEi
        - **Tumors:** Phổ biến hơn
        - **Ngưỡng intubation:** Thấp hơn
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Tránh nằm ngửa (aortocaval compression)
        - Corticosteroids an toàn
        - Intubation khó hơn (phù nề)
        - Cần tư vấn sản khoa
        
        **Bệnh nhân có bệnh nền:**
        - **COPD/Asthma:** Cẩn thận với corticosteroids
        - **Suy thận:** Điều chỉnh liều
        - **Suy gan:** Điều chỉnh liều
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: REFERENCES ==========
    render_references_section(get_references("upper_airway_obstruction"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_cause_specific_protocol(cause: str):
    """Render cause-specific protocol"""
    
    if cause == "Anaphylaxis":
        st.error("## 🚨 ANAPHYLAXIS - UPPER AIRWAY OBSTRUCTION")
        st.markdown("""
        **Quy trình:**
        
        1. **Epinephrine:**
           - **IM:** 0.3-0.5 mg (1:1000) - Ưu tiên
           - **IV:** 0.1 mg (1:10,000) nếu shock nặng
           - **Lặp lại:** q5-15 phút nếu cần
        
        2. **Oxygen:**
           - High-flow O₂ 100%
           - Cân nhắc intubation nếu stridor nặng
        
        3. **Antihistamines:**
           - **Diphenhydramine:** 25-50 mg IV
           - **Ranitidine:** 50 mg IV
        
        4. **Corticosteroids:**
           - **Methylprednisolone:** 125 mg IV
           - **Dexamethasone:** 10 mg IV
        
        5. **Fluid:**
           - Truyền dịch tích cực (hypotension)
        """)
        st.info("💡 Xem thêm protocol Anaphylaxis chi tiết")
    
    elif cause == "Epiglottitis":
        st.error("## 🚨 EPIGLOTTITIS - URGENT")
        st.markdown("""
        **Đặc điểm:**
        - Trẻ em 2-7 tuổi (hiếm hơn do vaccine)
        - Người lớn: Thường do H. influenzae type B
        - Khởi phát nhanh, sốt cao
        
        **Quy trình:**
        
        1. **Không kích thích:**
           - Tránh khám họng (có thể gây tắc nghẽn hoàn toàn)
           - Để trẻ ngồi trên lòng cha mẹ
        
        2. **Oxygen:**
           - High-flow O₂
           - Cân nhắc intubation sớm (trong OR)
        
        3. **Antibiotics:**
           - **Ceftriaxone:** 50-100 mg/kg IV (max 2 g)
           - **Cefotaxime:** 50-100 mg/kg IV
           - **Vancomycin:** Nếu nghi ngờ MRSA
        
        4. **Corticosteroids:**
           - **Dexamethasone:** 0.6 mg/kg IV
        
        5. **Intubation:**
           - Trong OR với ENT sẵn sàng
           - Có thể cần surgical airway
        """)
    
    elif cause == "Croup (Laryngotracheobronchitis)":
        st.warning("## ⚠️ CROUP (LARYNGOTRACHEOBRONCHITIS)")
        st.markdown("""
        **Đặc điểm:**
        - Trẻ em 6 tháng - 3 tuổi
        - Thường do virus (parainfluenza)
        - Khởi phát từ từ, ho khan đặc trưng
        
        **Quy trình:**
        
        1. **Epinephrine (racemic):**
           - **Nebulized:** 0.5 mL 2.25% trong 3 mL NS
           - **Lặp lại:** q20 phút nếu cần
        
        2. **Corticosteroids:**
           - **Dexamethasone:** 0.6 mg/kg PO/IM/IV (max 10 mg)
           - **Budesonide:** 2 mg nebulized
        
        3. **Oxygen:**
           - Nếu SpO₂ < 90%
        
        4. **Intubation:**
           - Hiếm khi cần (< 1%)
           - Chỉ nếu suy hô hấp nặng
        """)
    
    elif cause == "Foreign Body Aspiration":
        st.error("## 🚨 FOREIGN BODY ASPIRATION - URGENT")
        st.markdown("""
        **Đặc điểm:**
        - Trẻ em < 3 tuổi phổ biến nhất
        - Người lớn: Thường do thức ăn
        - Có thể tắc nghẽn hoàn toàn hoặc một phần
        
        **Quy trình:**
        
        1. **Nếu tắc nghẽn hoàn toàn:**
           - **Heimlich maneuver:** Người lớn, trẻ > 1 tuổi
           - **Back blows + chest thrusts:** Trẻ < 1 tuổi
           - **Finger sweep:** Chỉ nếu nhìn thấy vật
        
        2. **Nếu tắc nghẽn một phần:**
           - Không can thiệp nếu thở được
           - Theo dõi sát
           - Cân nhắc lấy trong OR
        
        3. **Bronchoscopy:**
           - Lấy foreign body
           - Trong OR với ENT/Pulmonology
        """)
    
    elif cause == "Angioedema":
        st.warning("## ⚠️ ANGIOEDEMA")
        st.markdown("""
        **Đặc điểm:**
        - Phù mặt, môi, lưỡi, họng
        - Có thể do:
          - Allergic (histamine-mediated)
          - ACEi-induced (bradykinin-mediated)
          - Hereditary (C1 esterase deficiency)
        
        **Quy trình:**
        
        1. **Nếu do ACEi:**
           - Ngừng ACEi ngay
           - **Icatibant:** 30 mg SC (nếu có)
           - **Fresh frozen plasma:** 2 units (nếu có)
           - **C1 esterase inhibitor:** Nếu hereditary
        
        2. **Nếu allergic:**
           - **Epinephrine:** 0.3-0.5 mg IM
           - **Antihistamines:** Diphenhydramine 25-50 mg IV
           - **Corticosteroids:** Methylprednisolone 125 mg IV
        
        3. **Oxygen:**
           - High-flow O₂
           - Cân nhắc intubation sớm
        """)
    
    elif cause == "Laryngeal Edema":
        st.warning("## ⚠️ LARYNGEAL EDEMA")
        st.markdown("""
        **Nguyên nhân:**
        - Anaphylaxis
        - Angioedema
        - Burns (inhalation)
        - Trauma
        - Infection
        
        **Quy trình:**
        
        1. **Oxygen:**
           - High-flow O₂
           - Heliox nếu có
        
        2. **Corticosteroids:**
           - **Methylprednisolone:** 1-2 mg/kg IV
           - **Dexamethasone:** 0.6 mg/kg IV
        
        3. **Epinephrine (racemic):**
           - **Nebulized:** 0.5 mL 2.25% trong 3 mL NS
        
        4. **Intubation:**
           - Cân nhắc sớm
           - Có thể khó do phù nề
        """)
    
    elif cause == "Retropharyngeal Abscess":
        st.error("## 🚨 RETROPHARYNGEAL ABSCESS - URGENT")
        st.markdown("""
        **Đặc điểm:**
        - Trẻ em < 5 tuổi phổ biến nhất
        - Người lớn: Hiếm, thường do trauma
        - Sốt, đau họng, khó nuốt
        
        **Quy trình:**
        
        1. **Antibiotics:**
           - **Ampicillin-sulbactam:** 50 mg/kg IV q6h
           - **Clindamycin:** 10-15 mg/kg IV q8h
           - **Vancomycin:** Nếu nghi ngờ MRSA
        
        2. **CT neck:**
           - Đánh giá kích thước, vị trí
           - Quyết định phẫu thuật
        
        3. **Surgical drainage:**
           - Nếu abscess lớn hoặc không đáp ứng
           - Trong OR với ENT
        
        4. **Intubation:**
           - Cân nhắc nếu tắc nghẽn nặng
           - Trong OR với ENT sẵn sàng
        """)
    
    elif cause == "Peritonsillar Abscess":
        st.warning("## ⚠️ PERITONSILLAR ABSCESS")
        st.markdown("""
        **Đặc điểm:**
        - Thanh thiếu niên, người trẻ
        - Đau họng một bên, khó nuốt
        - Giọng nói "hot potato"
        
        **Quy trình:**
        
        1. **Antibiotics:**
           - **Penicillin G:** 2-4 million units IV q4h
           - **Clindamycin:** 600-900 mg IV q8h
           - **Ampicillin-sulbactam:** 3 g IV q6h
        
        2. **Needle aspiration:**
           - Chọc hút mủ
           - Có thể lặp lại nếu cần
        
        3. **Surgical drainage:**
           - Nếu aspiration thất bại
           - Trong OR với ENT
        
        4. **Intubation:**
           - Hiếm khi cần
           - Chỉ nếu tắc nghẽn nặng
        """)
    
    elif cause == "Trauma":
        st.error("## 🚨 TRAUMA - UPPER AIRWAY OBSTRUCTION")
        st.markdown("""
        **Nguyên nhân:**
        - Chấn thương mặt/đường thở
        - Gãy xương hàm
        - Tổn thương thanh quản
        - Hematoma
        
        **Quy trình:**
        
        1. **Immobilization:**
           - Cột sống cổ (nếu nghi ngờ)
           - Xương hàm
        
        2. **Oxygen:**
           - High-flow O₂
           - Cẩn thận với mask (có thể làm nặng thêm)
        
        3. **Intubation:**
           - Cân nhắc sớm
           - Có thể khó do tổn thương
           - Cân nhắc surgical airway
        
        4. **Surgical airway:**
           - Nếu intubation thất bại
           - Cricothyrotomy hoặc tracheostomy
        """)
    
    elif cause == "Burns (Inhalation)":
        st.error("## 🚨 INHALATION BURNS - URGENT")
        st.markdown("""
        **Đặc điểm:**
        - Phù nề đường thở trên
        - Có thể tiến triển nhanh
        - Cần theo dõi sát
        
        **Quy trình:**
        
        1. **Oxygen:**
           - High-flow O₂
           - Cân nhắc hyperbaric O₂ nếu CO poisoning
        
        2. **Intubation:**
           - Chỉ định sớm (trước khi phù nề nặng)
           - Có thể khó sau 24-48h
        
        3. **Corticosteroids:**
           - **Methylprednisolone:** 1-2 mg/kg IV
           - Còn tranh cãi
        
        4. **Bronchoscopy:**
           - Đánh giá tổn thương
           - Làm sạch đường thở
        """)

