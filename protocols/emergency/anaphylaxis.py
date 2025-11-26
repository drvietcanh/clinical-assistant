"""
Anaphylaxis Management Protocol
ACAAI/WAO 2020, NIAID 2017
Life-threatening allergic reaction requiring immediate treatment
"""

import streamlit as st


def render():
    """Anaphylaxis Management Protocol"""
    st.subheader("🚨 Anaphylaxis Management")
    st.caption("ACAAI/WAO 2020, NIAID 2017 - Immediate life-threatening allergic reaction")
    
    st.error("""
    **⚠️ ANAPHYLAXIS = MEDICAL EMERGENCY**
    
    **Triệu chứng Điển Hình:**
    - Phản ứng da/mucosa (urticaria, angioedema)
    - Hô hấp (stridor, wheezing, dyspnea)
    - Tuần hoàn (hypotension, syncope)
    - GI (nausea, vomiting, diarrhea)
    
    **Chẩn Đoán:** ≥2 hệ cơ quan hoặc hạ huyết áp sau tiếp xúc với chất gây dị ứng
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử Trí Ngay Lập Tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. EPINEPHRINE - Thuốc Đầu Tay**
        
        **IM (Ưu tiên):**
        - **Người Lớn:** 0.3-0.5 mg IM (1:1000)
        - **Trẻ Em:** 0.01 mg/kg IM (max 0.3 mg)
        - **Vị trí:** Mặt trước-bên đùi
        - **Lặp lại:** q5-15 phút nếu cần
        
        **IV (Nếu shock nặng):**
        - **Người Lớn:** 0.1 mg IV (1:10,000)
        - **Trẻ Em:** 0.01 mg/kg IV
        - **Truyền tĩnh mạch:** 1-4 mcg/min
        """)
    
    with col2:
        st.warning("""
        **2. AIRWAY & BREATHING**
        
        - **Oxygen:** 100% qua mask
        - **Nếu stridor:** Chuẩn bị intubation
        - **Nếu wheezing:** Albuterol nebulizer
        - **Cricothyrotomy:** Nếu không thể intubate
        
        **3. CIRCULATION**
        
        - **Truyền dịch:** 1-2 L NS bolus
        - **Trendelenburg position**
        - **Monitor:** BP, HR, SpO2
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị Hỗ Trợ")
    
    st.info("""
    **Sau khi đã dùng Epinephrine:**
    
    **1. Antihistamines (H1 blocker):**
    - **Diphenhydramine:** 25-50 mg IV/IM (Người Lớn)
    - **Trẻ Em:** 1 mg/kg IV/IM (max 50 mg)
    - **Hoặc:** Cetirizine 10 mg PO
    
    **2. H2 Blocker:**
    - **Ranitidine:** 50 mg IV (Người Lớn)
    - **Hoặc:** Famotidine 20 mg IV
    
    **3. Corticosteroids:**
    - **Methylprednisolone:** 125 mg IV (Người Lớn)
    - **Trẻ Em:** 1-2 mg/kg IV
    - **Hoặc:** Prednisone 60 mg PO
    - **Mục đích:** Ngăn phản ứng 2 pha (biphasic)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Loại Mức Độ")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Ngừng tim (Cardiac Arrest)"],
        key="anaphylaxis_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_anaphylaxis()
    elif "Trung bình" in severity:
        render_moderate_anaphylaxis()
    elif "Nặng" in severity:
        render_severe_anaphylaxis()
    else:
        render_cardiac_arrest()
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Biphasic Reactions")
    
    st.warning("""
    **Phản ứng 2 pha (Biphasic):**
    - Xảy ra 4-12 giờ sau phản ứng ban đầu
    - Tỷ lệ: 1-20% các trường hợp
    - **Yếu tố nguy cơ:**
      - Phản ứng ban đầu nặng
      - Dùng epinephrine muộn
      - Cần >1 liều epinephrine
    
    **Khuyến nghị:**
    - Theo dõi ít nhất 4-6 giờ (phản ứng nặng: 8-12 giờ)
    - Có thể xuất viện nếu:
      - Không triệu chứng sau 4-6 giờ
      - Đã dùng corticosteroids
      - Có EpiPen và hướng dẫn sử dụng
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Epinephrine IM (mặt trước-bên đùi)",
        "✅ Oxygen 100%",
        "✅ Truyền dịch NS 1-2 L bolus",
        "✅ Diphenhydramine IV/IM",
        "✅ Ranitidine IV",
        "✅ Methylprednisolone IV",
        "✅ Monitor BP, HR, SpO2",
        "✅ Chuẩn bị intubation nếu cần",
        "✅ Theo dõi 4-6 giờ (nặng: 8-12 giờ)"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Phụ Nữ Có Thai:**
        - Epinephrine an toàn (ưu tiên cứu mẹ)
        - Tư thế nằm nghiêng trái
        - Monitor thai nhi
        
        **Người Cao Tuổi:**
        - Cẩn thận với epinephrine (tăng nguy cơ MI)
        - Giảm liều nếu có bệnh tim mạch
        - Theo dõi ECG
        """)
    
    with col2:
        st.markdown("""
        **Trẻ Em:**
        - Liều epinephrine: 0.01 mg/kg IM
        - Auto-injector: EpiPen Jr (0.15 mg)
        - Theo dõi sát (dễ tái phát)
        
        **Bệnh tim mạch:**
        - Epinephrine vẫn cần thiết
        - Cân nhắc giảm liều
        - Monitor ECG, troponin
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục Tiêu:**
    - ✅ Huyết áp ổn định (MAP ≥65 mmHg)
    - ✅ SpO2 ≥94%
    - ✅ Không stridor/wheezing
    - ✅ Không triệu chứng sau 4-6 giờ
    - ✅ Đã dùng corticosteroids
    - ✅ Có EpiPen và hướng dẫn
    
    **Xuất viện khi:**
    - Không triệu chứng ≥4-6 giờ
    - Đã dùng đủ thuốc
    - Có kế hoạch theo dõi
    - Có EpiPen (nếu cần)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ACAAI/WAO Anaphylaxis Guidelines 2020**
       - World Allergy Organization Journal
    
    2. **NIAID Guidelines 2017**
       - National Institute of Allergy and Infectious Diseases
    
    3. **UpToDate:** Anaphylaxis: Emergency treatment
       - Last updated: 2024
    
    4. **Medscape:** Anaphylaxis Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_anaphylaxis():
    """Mild anaphylaxis protocol"""
    st.success("## 🟢 MILD ANAPHYLAXIS")
    
    st.markdown("""
    **Triệu Chứng:**
    - Chỉ có da/mucosa (urticaria, angioedema)
    - Không có hô hấp/tuần hoàn
    
    **Điều Trị:**
    1. **Epinephrine:** 0.3 mg IM (Người Lớn)
    2. **Diphenhydramine:** 25-50 mg IV/IM
    3. **Corticosteroid:** Prednisone 60 mg PO
    4. **Theo Dõi:** 2-4 giờ
    
    **Xuất viện:** Có thể sau 2-4 giờ nếu ổn định
    """)


def render_moderate_anaphylaxis():
    """Moderate anaphylaxis protocol"""
    st.warning("## 🟡 MODERATE ANAPHYLAXIS")
    
    st.markdown("""
    **Triệu Chứng:**
    - Da/mucosa + Hô hấp (wheezing, dyspnea)
    - Hoặc da/mucosa + GI (nausea, vomiting)
    - Không có hạ huyết áp
    
    **Điều Trị:**
    1. **Epinephrine:** 0.3-0.5 mg IM (lặp lại nếu cần)
    2. **Oxygen:** 100% qua mask
    3. **Albuterol:** Nebulizer nếu wheezing
    4. **Diphenhydramine:** 50 mg IV
    5. **Ranitidine:** 50 mg IV
    6. **Methylprednisolone:** 125 mg IV
    7. **Theo Dõi:** 4-6 giờ
    
    **Xuất viện:** Sau 4-6 giờ nếu ổn định
    """)


def render_severe_anaphylaxis():
    """Severe anaphylaxis protocol"""
    st.error("## 🔴 SEVERE ANAPHYLAXIS - ICU")
    
    st.markdown("""
    **Triệu Chứng:**
    - Hạ huyết áp (SBP <90 mmHg)
    - Stridor, laryngeal edema
    - Suy hô hấp
    - Rối loạn ý thức
    
    **Điều trị ngay:**
    1. **Epinephrine:** 
       - 0.5 mg IM ngay lập tức
       - Hoặc 0.1 mg IV (1:10,000)
       - Truyền tĩnh mạch: 1-4 mcg/min
    
    2. **Airway:**
       - 100% Oxygen
       - Chuẩn bị intubation ngay
       - Cricothyrotomy nếu cần
    
    3. **Fluids:**
       - NS 1-2 L bolus
       - Có thể cần 3-4 L
    
    4. **Medications:**
       - Diphenhydramine 50 mg IV
       - Ranitidine 50 mg IV
       - Methylprednisolone 125 mg IV
    
    5. **ICU Monitoring:**
       - Continuous BP, HR, SpO2
       - Arterial line nếu cần
       - ECG monitoring
    
    6. **Theo Dõi:** 8-12 giờ (nguy cơ biphasic cao)
    """)


def render_cardiac_arrest():
    """Cardiac arrest from anaphylaxis"""
    st.error("## ⚫ CARDIAC ARREST - ACLS + Anaphylaxis")
    
    st.markdown("""
    **Ngừng tim do anaphylaxis:**
    
    **1. ACLS Protocol:**
    - CPR ngay lập tức
    - Defibrillation nếu shockable rhythm
    - Advanced airway
    
    **2. Epinephrine:**
    - **ACLS dose:** 1 mg IV q3-5 min
    - **Hoặc:** 0.1 mg/kg IV (Trẻ Em)
    - **Truyền tĩnh mạch:** 5-10 mcg/min
    
    **3. Fluids:**
    - NS 2-4 L bolus
    - Có thể cần nhiều hơn
    
    **4. Reversible causes (H's & T's):**
    - **Hypovolemia:** Truyền dịch
    - **Hypoxia:** 100% Oxygen
    - **Tension pneumothorax:** Needle decompression
    - **Tamponade:** Pericardiocentesis
    
    **5. Post-resuscitation:**
    - TTM (targeted temperature management)
    - ICU care
    - Monitor 24-48 giờ
    """)

