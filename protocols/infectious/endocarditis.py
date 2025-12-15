"""
Infective Endocarditis Protocol
AHA/IDSA 2015 Guidelines
Management of endocardial infection
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Infective Endocarditis Protocol"""
    st.subheader("🦠 Viêm nội tâm mạc nhiễm trùng (Infective Endocarditis)")
    st.caption("AHA/IDSA 2015 Guidelines - Endocardial infection management")
    
    st.error("""
    **⚠️ VIÊM NỘI TÂM MẠC NHIỄM TRÙNG = BỆNH NẶNG**
    
    **Định nghĩa:**
    - Nhiễm trùng lớp nội mạc tim (valves, endocardium)
    - Tỷ lệ tử vong: 15-30% nếu không điều trị
    - Cần điều trị kháng sinh dài ngày (4-6 tuần)
    
    **Yếu tố nguy cơ:**
    - Bệnh van tim
    - Van tim nhân tạo
    - Tiền sử viêm nội tâm mạc
    - Bệnh tim bẩm sinh
    - Tiêm chích ma túy
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán (Modified Duke Criteria)")
    
    st.warning("""
    **Chẩn đoán xác định khi có:**
    
    **1. Tiêu chuẩn mô học:**
    - Vi khuẩn hoặc mủ trong sùi hoặc áp xe
    - Hoặc sùi có viêm hoạt động
    
    **2. Tiêu chuẩn lâm sàng:**
    - **2 tiêu chuẩn chính:** HOẶC
    - **1 tiêu chuẩn chính + 3 tiêu chuẩn phụ:** HOẶC
    - **5 tiêu chuẩn phụ**
    
    **Tiêu chuẩn chính:**
    1. **Cấy máu dương tính:** Vi khuẩn điển hình (≥2 mẫu) hoặc vi khuẩn dai dẳng
    2. **Bằng chứng tổn thương nội tâm mạc:** Echo có sùi, áp xe, hở van mới
    
    **Tiêu chuẩn phụ:**
    1. Sốt >38°C
    2. Yếu tố nguy cơ (bệnh van tim, tiêm chích)
    3. Dấu hiệu mạch máu (tắc mạch, xuất huyết, nốt Osler)
    4. Dấu hiệu miễn dịch (viêm cầu thận, yếu tố dạng thấp)
    5. Cấy máu dương tính nhưng không đủ tiêu chuẩn chính
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng toàn thân:**
        - Sốt (90%)
        - Mệt mỏi
        - Sụt cân
        - Đổ mồ hôi đêm
        - Đau cơ, khớp
        
        **Triệu chứng tim:**
        - Tiếng thổi mới hoặc thay đổi
        - Suy tim
        - Rối loạn nhịp tim
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu ngoài da:**
        - Nốt Osler (nốt đau ở đầu ngón tay)
        - Xuất huyết dưới móng (splinter hemorrhage)
        - Ban Janeway (nốt không đau ở lòng bàn tay/chân)
        - Nốt Roth (xuất huyết võng mạc)
        
        **Biến chứng:**
        - Suy tim
        - Áp xe quanh van
        - Tắc mạch
        - Đột quỵ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: MICROBIOLOGY ==========
    st.markdown("### 🦠 Vi khuẩn thường gặp")
    
    st.info("""
    **Vi khuẩn thường gặp:**
    
    **1. Streptococcus viridans (30-40%):**
    - Thường ở van tự nhiên
    - Nhạy cảm với penicillin
    - Điều trị: Penicillin G + Gentamicin
    
    **2. Staphylococcus aureus (25-30%):**
    - Thường ở van nhân tạo, tiêm chích
    - Kháng methicillin (MRSA) phổ biến
    - Điều trị: Vancomycin hoặc Daptomycin
    
    **3. Enterococcus (10-15%):**
    - Thường ở van tự nhiên
    - Điều trị: Ampicillin + Gentamicin
    
    **4. Coagulase-negative Staphylococcus:**
    - Thường ở van nhân tạo
    - Điều trị: Vancomycin + Rifampin + Gentamicin
    
    **5. HACEK (5%):**
    - Haemophilus, Actinobacillus, Cardiobacterium, Eikenella, Kingella
    - Điều trị: Ceftriaxone hoặc Ampicillin
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### **1. Điều trị theo kinh nghiệm (Trước khi có kết quả cấy máu)**")
    
    st.success("""
    **Van tự nhiên (Native Valve):**
    - **Vancomycin:** 15-20 mg/kg IV q8-12h (tối đa 2 g mỗi liều)
    - **+ Gentamicin:** 1 mg/kg IV q8h
    
    **Van nhân tạo (Prosthetic Valve):**
    - **Vancomycin:** 15-20 mg/kg IV q8-12h
    - **+ Gentamicin:** 1 mg/kg IV q8h
    - **+ Rifampin:** 300 mg PO q8h
    
    **Lưu ý:** Điều chỉnh theo kết quả cấy máu và kháng sinh đồ
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Điều trị đặc hiệu (Sau khi có kết quả cấy máu)**")
    
    st.warning("""
    **Streptococcus viridans (Nhạy penicillin):**
    - **Penicillin G:** 12-18 triệu đơn vị/ngày IV (chia q4h)
    - **+ Gentamicin:** 1 mg/kg IV q8h
    - **Thời gian:** 4 tuần (van tự nhiên) hoặc 6 tuần (van nhân tạo)
    
    **Staphylococcus aureus (Nhạy methicillin - MSSA):**
    - **Nafcillin/Oxacillin:** 2 g IV q4h
    - **+ Gentamicin:** 1 mg/kg IV q8h (3-5 ngày đầu)
    - **Thời gian:** 6 tuần
    
    **Staphylococcus aureus (Kháng methicillin - MRSA):**
    - **Vancomycin:** 15-20 mg/kg IV q8-12h (duy trì nồng độ đáy 15-20 mcg/mL)
    - **Thời gian:** 6 tuần
    
    **Enterococcus:**
    - **Ampicillin:** 2 g IV q4h
    - **+ Gentamicin:** 1 mg/kg IV q8h
    - **Thời gian:** 4-6 tuần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SURGICAL INDICATIONS ==========
    st.markdown("### 🔪 Chỉ định phẫu thuật")
    
    st.error("""
    **Chỉ định phẫu thuật:**
    
    **1. Suy tim:**
    - Hở van nặng gây suy tim
    - Không đáp ứng điều trị nội khoa
    
    **2. Nhiễm trùng không kiểm soát:**
    - Sốt kéo dài >5-7 ngày dù kháng sinh đúng
    - Áp xe quanh van
    - Nhiễm trùng nấm hoặc vi khuẩn kháng thuốc
    
    **3. Nguy cơ tắc mạch:**
    - Sùi lớn (>10 mm) sau điều trị
    - Tắc mạch tái phát
    
    **4. Van nhân tạo:**
    - Nhiễm trùng van nhân tạo sớm (<1 năm)
    - Hở van nhân tạo
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Cấy máu:** Mỗi 24-48 giờ đến khi âm tính (thường 2-3 ngày)
    - **Echo:** Sau 1 tuần và khi xuất viện
    - **Dấu hiệu sinh tồn:** Mỗi 4-8 giờ
    - **Triệu chứng:** Sốt, mệt mỏi
    - **Chức năng thận:** Creatinine (nếu dùng aminoglycoside)
    - **Nồng độ vancomycin:** Nếu dùng (nồng độ đáy 15-20 mcg/mL)
    
    **Dấu hiệu cải thiện:**
    - Hết sốt
    - Cấy máu âm tính
    - Cải thiện triệu chứng
    
    **Dấu hiệu xấu đi:**
    - Sốt kéo dài
    - Cấy máu vẫn dương tính
    - Suy tim
    - Tắc mạch
    - Cần phẫu thuật
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PROPHYLAXIS ==========
    st.markdown("### 🛡️ Dự phòng")
    
    st.info("""
    **Chỉ định dự phòng (Theo AHA 2017):**
    
    **Bệnh nhân có nguy cơ cao:**
    - Van tim nhân tạo
    - Tiền sử viêm nội tâm mạc
    - Bệnh tim bẩm sinh tím
    - Ghép tim có rối loạn van
    
    **Thủ thuật cần dự phòng:**
    - Thủ thuật răng (nhổ răng, cạo vôi)
    - Thủ thuật đường hô hấp (cắt amidan, nội soi phế quản)
    - Thủ thuật da nhiễm trùng
    
    **Phác đồ:**
    - **Amoxicillin:** 2 g PO 1 giờ trước
    - **Hoặc:** Ampicillin 2 g IV/IM 30 phút trước
    - **Nếu dị ứng penicillin:** Clindamycin 600 mg PO/IV
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    references = get_references("Infective Endocarditis")
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
        1. **Baddour LM, et al. Infective Endocarditis in Adults: Diagnosis, Antimicrobial Therapy, and Management of Complications.** Circulation. 2015
        2. **AHA Scientific Statement** - Prevention of Infective Endocarditis (2017)
        3. **UpToDate:** Infective Endocarditis - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

