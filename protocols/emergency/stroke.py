"""
Stroke Management Protocol
AHA/ASA Guidelines 2021
Ischemic & Hemorrhagic Stroke
"""

import streamlit as st


def render():
    """Stroke Management Protocol"""
    st.subheader("🧠 Stroke Management Protocol")
    st.caption("AHA/ASA Guidelines 2021 - Ischemic & Hemorrhagic Stroke")
    
    st.info("""
    **Triệu chứng Stroke (BE FAST):**
    - **B**alance: Mất thăng bằng
    - **E**yes: Mất thị lực
    - **F**ace: Méo mặt
    - **A**rms: Yếu tay
    - **S**peech: Nói khó
    - **T**ime: Gọi cấp cứu ngay!
    """)
    
    st.markdown("---")
    
    # Stroke type selection
    stroke_type = st.radio(
        "**Loại Stroke:**",
        ["Đột quỵ thiếu máu (Ischemic)", "Đột quỵ xuất huyết (Hemorrhagic)", "Chưa xác định"],
        key="stroke_type"
    )
    
    st.markdown("---")
    
    if "thiếu máu" in stroke_type or "Ischemic" in stroke_type:
        render_ischemic_stroke()
    elif "xuất huyết" in stroke_type or "Hemorrhagic" in stroke_type:
        render_hemorrhagic_stroke()
    else:
        render_unknown_stroke()


def render_ischemic_stroke():
    """Ischemic Stroke Protocol"""
    
    st.error("## 🚨 ISCHEMIC STROKE PROTOCOL")
    st.error("**TIME IS BRAIN - Mỗi phút = 1.9 triệu tế bào não mất đi!**")
    
    st.markdown("### ⏱️ Timeline Goals")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Door-to-CT", "≤25 phút", "🎯 Mục tiêu")
    with col2:
        st.metric("Door-to-Needle (tPA)", "≤60 phút", "🎯 Mục tiêu")
    with col3:
        st.metric("Door-to-Puncture (MT)", "≤90 phút", "🎯 Mục tiêu")
    
    st.markdown("---")
    st.markdown("### 1️⃣ Xử trí tức thì (< 10 phút)")
    
    st.error("""
    **ABC - Airway, Breathing, Circulation:**
    
    **A - Airway:**
    - Đảm bảo đường thở thông thoáng
    - Cân nhắc intubation nếu GCS <8, không bảo vệ được đường thở
    
    **B - Breathing:**
    - O₂ để duy trì SpO₂ >94%
    - Tránh hyperoxia (O₂ không cần thiết nếu SpO₂ >94%)
    
    **C - Circulation:**
    - 2 đường truyền tĩnh mạch
    - Kiểm tra đường huyết
    - Hạ đường huyết: Glucose 50% 50ml IV (nếu <60 mg/dL)
    - Tăng đường huyết: Insulin (nếu >180-200 mg/dL)
    
    **D - Disability:**
    - Đánh giá GCS, NIHSS
    - Thần kinh ngay
    
    **E - Exposure:**
    - ECG
    - CBC, PT/INR, aPTT
    - Đường huyết
    - Troponin (không loại trừ MI)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Chẩn đoán - CT Scan")
    
    st.warning("""
    **CT Head NGAY (trong 25 phút):**
    
    **Mục đích:**
    - Loại trừ xuất huyết não
    - Tìm dấu hiệu sớm của nhồi máu (loss of gray-white differentiation, sulcal effacement)
    - Đánh giá ASPECTS score (nếu MT candidate)
    
    **CT Angiography (CTA):**
    - Nếu trong cửa sổ MT (thường <24h)
    - Tìm tắc mạch lớn (large vessel occlusion)
    - Đánh giá collateral flow
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Thrombolysis - tPA Criteria")
    
    st.markdown("#### ✅ Chỉ định tPA (Alteplase)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Inclusion Criteria:**
        
        ✅ **Thời gian:** < 4.5 giờ từ khi khởi phát triệu chứng
        ✅ **Tuổi:** ≥18 tuổi
        ✅ **NIHSS:** Có triệu chứng thần kinh đo được
        ✅ **CT:** Không có xuất huyết
        ✅ **Huyết áp:** SBP <185, DBP <110 mmHg
        ✅ **Đường huyết:** ≥50 mg/dL
        ✅ **Platelet:** ≥100,000/µL
        ✅ **INR:** ≤1.7
        ✅ **aPTT:** Bình thường (nếu dùng heparin gần đây)
        """)
    
    with col2:
        st.error("""
        **Exclusion Criteria (Tuyệt đối):**
        
        🚫 **Thời gian:** > 4.5 giờ từ khi khởi phát
        🚫 **Xuất huyết:** Xuất huyết não trên CT
        🚫 **Tăng áp nặng:** SBP >185 hoặc DBP >110 (không kiểm soát được)
        🚫 **Tiền sử xuất huyết nội sọ**
        🚫 **Đột quỵ gần đây:** < 3 tháng
        🚫 **Chấn thương đầu gần đây:** < 3 tháng
        🚫 **Phẫu thuật lớn gần đây:** < 14 ngày
        🚫 **Đang dùng Warfarin và INR >1.7**
        🚫 **Đang dùng NOAC (Xa inhibitor) <48h**
        🚫 **Platelet <100,000/µL**
        
        **Exclusion (Tương đối):**
        ⚠️ Tuổi >80 (có thể cân nhắc với liều thấp hơn)
        ⚠️ Tiểu đường + tiền sử đột quỵ
        """)
    
    st.markdown("---")
    st.markdown("#### 💉 tPA Dosing")
    
    st.info("""
    **Alteplase (tPA) Protocol:**
    
    **Liều:** 0.9 mg/kg (max 90 mg)
    - 10% của tổng liều: Bolus IV trong 1 phút
    - 90% còn lại: Truyền trong 60 phút
    
    **Ví dụ:** Bệnh nhân 70kg
    - Tổng liều: 70 × 0.9 = 63 mg
    - Bolus: 6.3 mg (1 phút)
    - Infusion: 56.7 mg (60 phút) = 56.7 ml/h (nếu pha 1mg/ml)
    
    **Monitoring trong khi truyền:**
    - Huyết áp: Mỗi 15 phút × 2h, sau đó mỗi 30 phút × 6h
    - Neurologic checks: Mỗi 30 phút × 6h
    - Nếu có thay đổi thần kinh: Dừng tPA, CT ngay
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Lấy huyết khối cơ học (MT)")
    
    st.warning("""
    **Chỉ định MT (Endovascular Thrombectomy):**
    
    ✅ **Thời gian:** < 24 giờ từ khi khởi phát
    ✅ **Loại mạch:** Large vessel occlusion (ICA, M1, M2, basilar)
    ✅ **NIHSS:** ≥6 (hoặc ≥4 nếu có aphasia/neglect)
    ✅ **ASPECTS:** ≥6 (trên NCCT) hoặc ≥5 (trên MRI DWI)
    ✅ **Tình trạng:** Mất <1/3 MCA territory
    ✅ **CTA/MRA:** Có tắc mạch lớn
    
    **Timeline:**
    - Door-to-Puncture: ≤90 phút
    - Door-to-Reperfusion: ≤120 phút
    
    **Kết hợp với tPA:**
    - MT có thể dùng kết hợp với tPA (Bridge therapy)
    - Hoặc dùng đơn độc nếu chống chỉ định tPA
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Hỗ trợ y tế")
    
    st.info("""
    **Huyết áp:**
    - **Nếu không dùng tPA:** Cho phép SBP đến 220 mmHg
    - **Nếu dùng tPA:** Giữ SBP <185 mmHg
    - **Thuốc:** Labetalol 10-20mg IV, hoặc Nicardipine infusion
    
    **Sốt:**
    - Hạ sốt với acetaminophen
    - Mục tiêu: <37.5°C
    
    **Nuôi dưỡng:**
    - NPO cho đến khi đánh giá nuốt
    - Nếu dysphagia: NGT hoặc PEG
    
    **Dự phòng DVT:**
    - Không dùng heparin trong 24h đầu (nếu dùng tPA)
    - Dự phòng sau 24h: Heparin SC hoặc intermittent compression
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Điều trị sau giai đoạn cấp")
    
    st.success("""
    **Antiplatelet (sau 24h nếu không dùng tPA):**
    - Aspirin 81-325mg PO ngay (hoặc sau 24h nếu dùng tPA)
    - Hoặc Clopidogrel 75mg PO
    - Không dùng kết hợp trong 21 ngày đầu (trừ TIA/minor stroke với DAPT)
    
    **Statin:**
    - Atorvastatin 80mg PO (high-intensity)
    - Hoặc Rosuvastatin 40mg PO
    
    **Kiểm soát yếu tố nguy cơ:**
    - Huyết áp: ACE-I hoặc ARB
    - Đường huyết: Kiểm soát HbA1c <7%
    - Bỏ thuốc lá
    """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Thời điểm bắt đầu anticoagulation")
    
    st.warning("""
    **Nếu có chỉ định anticoagulation (AF, DVT/PE):**
    
    **Timing:**
    - **TIA:** Có thể bắt đầu ngay
    - **Minor stroke (NIHSS <4):** Sau 3 ngày
    - **Moderate stroke (NIHSS 5-15):** Sau 7-14 ngày
    - **Severe stroke (NIHSS >15):** Sau 14-21 ngày
    
    **Lựa chọn:**
    - DOAC (Apixaban, Rivaroxaban) ưu tiên hơn Warfarin
    - Nếu Warfarin: INR mục tiêu 2.0-3.0
    """)


def render_hemorrhagic_stroke():
    """Hemorrhagic Stroke (ICH) Protocol"""
    
    st.error("## 🚨 HEMORRHAGIC STROKE (ICH) PROTOCOL")
    st.error("**CODE STROKE - Xử trí khẩn cấp!**")
    
    st.markdown("### 1️⃣ Xử trí tức thì")
    
    st.error("""
    **ABC tương tự Ischemic Stroke:**
    
    **Điểm khác biệt quan trọng:**
    - **KHÔNG dùng tPA**
    - **Hạ huyết áp ngay:** SBP <140 mmHg (nếu có thể)
    - **Đảo ngược anticoagulation** nếu đang dùng
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Kiểm soát huyết áp")
    
    st.warning("""
    **Mục tiêu huyết áp:**
    
    **Nếu SBP 150-220 mmHg:**
    - Hạ từ từ đến SBP 140 mmHg
    - Tránh hạ quá nhanh (có thể giảm tưới máu não)
    
    **Nếu SBP >220 mmHg:**
    - Hạ tích cực hơn
    - Có thể cần nitroprusside (nếu có monitoring invasif)
    
    **Thuốc:**
    - Labetalol 10-20mg IV, có thể lặp lại
    - Nicardipine infusion: 5-15 mg/h
    - Clevidipine (nếu có)
    
    **Tránh:**
    - Hạ SBP <140 quá nhanh
    - Hydralazine (không kiểm soát được)
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Đảo ngược anticoagulation")
    
    st.error("""
    **Warfarin (Vitamin K antagonist):**
    - **PCC (Prothrombin Complex Concentrate):** 25-50 U/kg
    - **Vitamin K:** 10mg IV
    - Mục tiêu INR: <1.4 trong 1h
    
    **DOAC (Xa inhibitors):**
    - **Andexanet alfa:** Nếu có (Xa inhibitors)
    - **4F-PCC:** 50 U/kg (nếu không có Andexanet)
    
    **DOAC (Thrombin inhibitors - Dabigatran):**
    - **Idarucizumab:** 5g IV (2 bolus 2.5g)
    
    **Heparin:**
    - Protamine sulfate: 1mg/100 U heparin
    
    **Thời gian:** Đảo ngược càng sớm càng tốt
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Đánh giá & quyết định phẫu thuật")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Chỉ định phẫu thuật:**
        
        ✅ **Hematoma lớn (>30ml):**
        - Supratentorial >30ml
        - Cerebellar >15ml
        
        ✅ **Dấu hiệu tăng áp nội sọ:**
        - GCS giảm
        - Midline shift >5mm
        - Hydrocephalus
        
        ✅ **Cerebellar hematoma:**
        - >3cm đường kính
        - Có dấu hiệu chèn ép
        """)
    
    with col2:
        st.warning("""
        **Chống chỉ định tương đối:**
        
        ⚠️ **GCS ≤4** (tiên lượng xấu)
        ⚠️ **Tuổi >80** (cân nhắc cẩn thận)
        ⚠️ **Hematoma nhỏ** (<30ml supratentorial)
        ⚠️ **Basal ganglia nhỏ** (thường bảo tồn)
        
        **Lưu ý:** Quyết định phẫu thuật phải cân nhắc:
        - Tuổi, GCS trước phẫu thuật
        - Kích thước và vị trí hematoma
        - Tình trạng thần kinh hiện tại
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Điều trị hỗ trợ")
    
    st.info("""
    **ICP Management (nếu có monitoring ICP):**
    - Mục tiêu ICP: <20 mmHg
    - CPP: 50-70 mmHg
    
    **Hỗ trợ thở máy:**
    - Mục tiêu PaCO₂: 35-40 mmHg
    - Tránh hyperventilation kéo dài
    
    **Sốt:**
    - Hạ sốt: Acetaminophen
    - Mục tiêu: <37.5°C
    
    **Động kinh:**
    - Dự phòng: Không khuyến cáo thường quy
    - Điều trị nếu có cơn: Levetiracetam, Phenytoin
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Theo dõi")
    
    st.success("""
    **Monitoring:**
    - Neurologic checks mỗi 1-2 giờ
    - Huyết áp liên tục
    - CT Head lặp lại nếu:
      * GCS giảm ≥2 điểm
      * Focal deficit nặng lên
      * ICP tăng
      * Sau 24h (đánh giá tiến triển)
    
    **Tiên lượng:**
    - ICH Score: 0-6 (đánh giá tử vong 30 ngày)
    - Phụ thuộc vào:
      * Tuổi
      * GCS
      * Kích thước hematoma
      * Vị trí (infratentorial)
      * OTT (intraventricular hemorrhage)
    """)


def render_unknown_stroke():
    """Protocol when stroke type unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH LOẠI STROKE")
    
    st.error("""
    **Xử trí ngay trong khi chờ CT:**
    
    1. ✅ **ABC** - Airway, Breathing, Circulation
    2. ✅ **2 đường truyền** tĩnh mạch
    3. ✅ **Lấy máu:** CBC, PT/INR, aPTT, Glucose
    4. ✅ **ECG**
    5. ✅ **Gọi CT ngay** (< 25 phút)
    6. ✅ **Thần kinh consult**
    
    **KHÔNG:**
    ❌ Dùng tPA cho đến khi có CT
    ❌ Hạ huyết áp quá mức (chờ CT)
    ❌ Dùng aspirin (nếu nghi xuất huyết)
    
    **Timeline:**
    - CT trong 25 phút
    - Sau khi có CT → quyết định Ischemic vs Hemorrhagic protocol
    """)

