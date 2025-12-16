"""
Acute Exacerbation of Inflammatory Bowel Disease Protocol
ECCO Guidelines, ACG Guidelines
IBD Flare Management (Crohn's Disease & Ulcerative Colitis)
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Exacerbation of IBD Protocol"""
    st.subheader("🩸 Acute Exacerbation of IBD Protocol")
    st.caption("ECCO, ACG Guidelines - IBD Flare Management")
    
    st.info("""
    **IBD Flare là đợt xấu đi cấp tính của bệnh viêm ruột (Crohn's hoặc Ulcerative Colitis).**
    - **Triệu chứng:** Tiêu chảy, đau bụng, chảy máu trực tràng, sốt
    - **Severity:** Nhẹ, Trung bình, Nặng
    - **Management:** Phụ thuộc vào loại IBD và mức độ nặng
    """)
    
    st.markdown("---")
    
    # IBD type
    ibd_type = st.radio(
        "**Loại IBD:**",
        ["Ulcerative Colitis (UC)", "Crohn's Disease (CD)", "Chưa xác định"],
        key="ibd_type"
    )
    
    st.markdown("---")
    
    # Assessment
    st.markdown("### 1️⃣ Đánh giá Mức độ Nặng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Triệu chứng")
        diarrhea = st.number_input(
            "**Số lần tiêu chảy/ngày:**",
            min_value=0,
            max_value=20,
            value=5,
            step=1,
            key="ibd_diarrhea"
        )
        blood_stool = st.checkbox("**Phân máu**", key="ibd_blood")
        abdominal_pain = st.checkbox("**Đau bụng**", key="ibd_pain")
        fever = st.checkbox("**Sốt >37.5°C**", key="ibd_fever")
        weight_loss = st.checkbox("**Sụt cân**", key="ibd_weight")
    
    with col2:
        st.markdown("#### Dấu hiệu Nặng")
        tachycardia = st.checkbox("**Nhịp tim >90 bpm**", key="ibd_hr")
        anemia = st.checkbox("**Thiếu máu (Hgb <10 g/dL)**", key="ibd_anemia")
        elevated_crp = st.checkbox("**CRP tăng**", key="ibd_crp")
        hypoalbuminemia = st.checkbox("**Albumin <3.5 g/dL**", key="ibd_albumin")
        toxic_megacolon = st.checkbox("**Toxic megacolon**", key="ibd_toxic")
    
    # Calculate severity
    if ibd_type == "Ulcerative Colitis (UC)":
        # UC severity (Truelove-Witts)
        if diarrhea >= 6 and blood_stool and (fever or tachycardia or anemia or elevated_crp):
            severity = "Severe"
            st.error("## 🚨 UC FLARE NẶNG")
        elif diarrhea >= 4 and blood_stool:
            severity = "Moderate"
            st.warning("## ⚠️ UC FLARE TRUNG BÌNH")
        else:
            severity = "Mild"
            st.success("## ✅ UC FLARE NHẸ")
    elif ibd_type == "Crohn's Disease (CD)":
        # CD severity (CDAI or clinical)
        severe_signs = sum([diarrhea >= 6, fever, weight_loss, anemia, elevated_crp, hypoalbuminemia])
        if severe_signs >= 4 or toxic_megacolon:
            severity = "Severe"
            st.error("## 🚨 CD FLARE NẶNG")
        elif severe_signs >= 2:
            severity = "Moderate"
            st.warning("## ⚠️ CD FLARE TRUNG BÌNH")
        else:
            severity = "Mild"
            st.success("## ✅ CD FLARE NHẸ")
    else:
        severity = "Unknown"
        st.info("## ⚠️ CHƯA XÁC ĐỊNH")
    
    st.markdown("---")
    
    if ibd_type == "Ulcerative Colitis (UC)":
        render_uc_flare(severity)
    elif ibd_type == "Crohn's Disease (CD)":
        render_cd_flare(severity)
    else:
        render_unknown_ibd()
    
    st.markdown("---")
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ECCO Guidelines 2023** - Ulcerative Colitis Management
    2. **ECCO Guidelines 2023** - Crohn's Disease Management
    3. **ACG Guidelines 2019** - Ulcerative Colitis
    4. **UpToDate:** IBD Flare Management - Last updated 2024
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")


def render_uc_flare(severity):
    """Ulcerative Colitis Flare Protocol"""
    st.markdown("### 2️⃣ UC Flare Management")
    
    if severity == "Severe":
        st.error("## 🚨 UC FLARE NẶNG - CẦN NHẬP VIỆN")
        
        st.markdown("#### 💉 Điều trị Khởi Đầu")
        
        st.success("""
        **IV Corticosteroids:**
        - **Methylprednisolone:** 40-60mg IV q24h
        - Hoặc **Hydrocortisone:** 100mg IV q8h
        - **Duration:** 3-5 ngày, sau đó đánh giá
        
        **Nếu đáp ứng:**
        - Chuyển sang PO: Prednisone 40-60mg QD
        - Giảm dần: 5-10mg mỗi tuần
        
        **Nếu không đáp ứng sau 3-5 ngày:**
        - Xem xét infliximab (rescue therapy)
        - Hoặc cyclosporine (nếu không có infliximab)
        - Hoặc colectomy (nếu thất bại)
        """)
        
        st.markdown("---")
        st.markdown("#### 💊 Rescue Therapy")
        
        st.warning("""
        **Infliximab (Anti-TNF):**
        - **Loading:** 5 mg/kg IV (0, 2, 6 tuần)
        - **Maintenance:** 5 mg/kg IV q8 weeks
        - **Nếu đáp ứng:** Tiếp tục maintenance
        
        **Cyclosporine:**
        - **2-4 mg/kg IV** continuous infusion
        - **Duration:** 7-14 ngày
        - **Chuyển sang PO:** 5-7.5 mg/kg PO BID
        - **Monitor:** Levels, creatinine, BP
        """)
    
    elif severity == "Moderate":
        st.warning("## ⚠️ UC FLARE TRUNG BÌNH")
        
        st.markdown("#### 💊 Điều trị")
        
        st.success("""
        **Oral Corticosteroids:**
        - **Prednisone:** 40-60mg PO QD × 5-7 ngày
        - Sau đó giảm dần: 5-10mg mỗi tuần
        - **Duration:** 8-12 tuần total
        
        **5-ASA (Mesalamine):**
        - Tiếp tục nếu đang dùng
        - Hoặc bắt đầu: Mesalamine 2.4-4.8g/ngày
        - **Formulation:** PO hoặc enema (nếu distal disease)
        
        **Nếu không đáp ứng:**
        - Xem xét thêm azathioprine/6-MP
        - Hoặc infliximab
        """)
    
    else:
        st.success("## ✅ UC FLARE NHẸ")
        
        st.markdown("#### 💊 Điều trị")
        
        st.info("""
        **5-ASA (Mesalamine):**
        - **Mesalamine:** 2.4-4.8g/ngày PO
        - Hoặc **Sulfasalazine:** 3-4g/ngày PO
        - **Enema:** Nếu distal disease (left-sided)
        
        **Topical Steroids:**
        - **Budesonide enema:** 2mg/ngày (nếu distal)
        
        **Nếu không đáp ứng:**
        - Thêm prednisone 20-40mg QD
        """)


def render_cd_flare(severity):
    """Crohn's Disease Flare Protocol"""
    st.markdown("### 2️⃣ CD Flare Management")
    
    if severity == "Severe":
        st.error("## 🚨 CD FLARE NẶNG - CẦN NHẬP VIỆN")
        
        st.markdown("#### 💉 Điều trị Khởi Đầu")
        
        st.success("""
        **IV Corticosteroids:**
        - **Methylprednisolone:** 40-60mg IV q24h
        - Hoặc **Hydrocortisone:** 100mg IV q8h
        - **Duration:** 3-5 ngày
        
        **Nếu đáp ứng:**
        - Chuyển sang PO: Prednisone 40-60mg QD
        - Giảm dần
        
        **Nếu không đáp ứng:**
        - Xem xét infliximab (anti-TNF)
        - Hoặc vedolizumab (anti-integrin)
        - Hoặc ustekinumab (anti-IL-12/23)
        """)
        
        st.markdown("---")
        st.markdown("#### 💊 Biologics")
        
        st.warning("""
        **Infliximab:**
        - **Loading:** 5 mg/kg IV (0, 2, 6 tuần)
        - **Maintenance:** 5 mg/kg IV q8 weeks
        
        **Vedolizumab:**
        - **Loading:** 300mg IV (0, 2, 6 tuần)
        - **Maintenance:** 300mg IV q8 weeks
        
        **Ustekinumab:**
        - **Loading:** 6 mg/kg IV × 1, sau đó 90mg SC q8 weeks
        """)
    
    elif severity == "Moderate":
        st.warning("## ⚠️ CD FLARE TRUNG BÌNH")
        
        st.markdown("#### 💊 Điều trị")
        
        st.success("""
        **Oral Corticosteroids:**
        - **Prednisone:** 40-60mg PO QD × 5-7 ngày
        - Giảm dần: 5-10mg mỗi tuần
        
        **Immunomodulators:**
        - **Azathioprine:** 2-2.5 mg/kg/ngày PO
        - Hoặc **6-MP:** 1-1.5 mg/kg/ngày PO
        - **Duration:** 3-6 tháng để có tác dụng
        
        **Nếu không đáp ứng:**
        - Xem xét biologics
        """)
    
    else:
        st.success("## ✅ CD FLARE NHẸ")
        
        st.markdown("#### 💊 Điều trị")
        
        st.info("""
        **Budesonide (Enteric-coated):**
        - **9mg PO QD** × 8 tuần
        - Giảm dần: 6mg × 2 tuần, sau đó 3mg × 2 tuần
        
        **5-ASA:**
        - **Mesalamine:** 2.4-4.8g/ngày PO
        - (Hiệu quả kém hơn UC)
        
        **Nếu không đáp ứng:**
        - Thêm prednisone 20-40mg QD
        """)


def render_unknown_ibd():
    """Protocol when IBD type unknown"""
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH LOẠI IBD")
    
    st.error("""
    **Xử trí ngay trong khi chờ chẩn đoán:**
    
    1. ✅ **Lấy máu:** CBC, CRP, ESR, Albumin, LFT, Creatinine
    2. ✅ **Stool:** Calprotectin, C. difficile, cultures
    3. ✅ **Imaging:** CT abdomen/pelvis (nếu cần)
    4. ✅ **Colonoscopy:** Nếu stable (với prep)
    5. ✅ **Supportive:** IV fluids, nutrition
    
    **Điều trị empiric:**
    - **Corticosteroids:** Nếu flare nặng
    - **5-ASA:** Nếu flare nhẹ-trung bình
    - **Antibiotics:** Nếu nghi infection (C. difficile, etc.)
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("IBD Exacerbation")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

