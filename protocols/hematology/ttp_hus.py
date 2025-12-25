"""
TTP/HUS (Thrombotic Thrombocytopenic Purpura / Hemolytic Uremic Syndrome) Protocol
ASH Guidelines 2024, UpToDate 2024
Life-threatening microangiopathic hemolytic anemia
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """TTP/HUS Management Protocol"""
    st.subheader("🩸 TTP/HUS (Thrombotic Thrombocytopenic Purpura / Hemolytic Uremic Syndrome)")
    st.caption("ASH Guidelines 2024, UpToDate 2024 - Life-threatening microangiopathic hemolytic anemia")
    
    st.error("""
    **⚠️ TTP/HUS = CẤP CỨU Y KHOA - TỬ VONG CAO NẾU KHÔNG ĐIỀU TRỊ**
    
    **Định nghĩa:**
    - **TTP:** Thiếu ADAMTS13 → Huyết khối vi mạch
    - **HUS:** Thường do E. coli O157:H7 → Tổn thương thận
    - **Đặc điểm:** Tan máu vi mạch, giảm tiểu cầu, suy thận
    
    **Triệu chứng (Pentad - TTP):**
    - **Fever:** Sốt
    - **Thrombocytopenia:** Giảm tiểu cầu
    - **Microangiopathic hemolytic anemia:** Tan máu vi mạch
    - **Renal failure:** Suy thận
    - **Neurologic symptoms:** Triệu chứng thần kinh
    
    **Lưu ý:** Không cần đủ 5 triệu chứng để chẩn đoán
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức nặng
        - Suy hô hấp
        - Co giật
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 500-1000 mL bolus (nếu hạ HA)
        - **Thận trọng:** Suy thận
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị plasma exchange
        
        **4. LABS NGAY:**
        - **CBC:** Hct, Hb, Platelets
        - **Peripheral smear:** Mảnh vỡ hồng cầu (schistocytes)
        - **LDH:** (tăng cao)
        - **Haptoglobin:** (giảm)
        - **Creatinine, BUN:** (suy thận)
        - **ADAMTS13:** (nếu có, cho TTP)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    
    **TTP:**
    - Giảm tiểu cầu
    - Tan máu vi mạch (schistocytes trên peripheral smear)
    - LDH tăng cao
    - Haptoglobin giảm
    - ADAMTS13 <10% (nếu có)
    - Triệu chứng thần kinh (thường gặp)
    - Suy thận (có thể)
    
    **HUS:**
    - Giảm tiểu cầu
    - Tan máu vi mạch
    - Suy thận nặng (đặc trưng)
    - Tiêu chảy (thường do E. coli)
    - ADAMTS13 bình thường
    
    **Xét nghiệm:**
    - **Peripheral smear:** Schistocytes (quan trọng!)
    - **LDH:** Tăng cao (>1000 U/L)
    - **Haptoglobin:** Giảm hoặc không phát hiện
    - **ADAMTS13:** <10% (TTP), bình thường (HUS)
    - **Creatinine, BUN:** Tăng (suy thận)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Đặc hiệu")
    
    st.error("## 🚨 PLASMA EXCHANGE - ĐIỀU TRỊ CHÍNH")
    
    st.success("""
    **1. PLASMA EXCHANGE (PLEX) - Thuốc đầu tay**
    
    **Chỉ định:**
    - Tất cả bệnh nhân TTP
    - HUS nặng (nếu cần)
    
    **Kỹ thuật:**
    - **Thể tích:** 1-1.5 × thể tích huyết tương
    - **Tần suất:** Mỗi ngày
    - **Thời gian:** Cho đến khi cải thiện
    
    **Mục tiêu:**
    - Tiểu cầu tăng
    - LDH giảm
    - Triệu chứng cải thiện
    
    **Hiệu quả:**
    - Bắt đầu: 1-3 ngày
    - Tối đa: 5-7 ngày
    - Tỷ lệ đáp ứng: 70-80%
    
    **Lưu ý:**
    - Cần catheter tĩnh mạch trung tâm
    - Có thể cần nhiều lần
    - Theo dõi sát biến chứng
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Corticosteroids:**
    
    **Methylprednisolone:**
    - **Liều:** 1-2 mg/kg/ngày IV
    - **Hoặc:** Prednisone 1-2 mg/kg/ngày PO
    - **Mục đích:** Ức chế miễn dịch
    
    **2. Rituximab (Nếu TTP):**
    
    - **Liều:** 375 mg/m² IV mỗi tuần × 4 tuần
    - **Chỉ định:** Nếu không đáp ứng PLEX
    - **Hoặc:** Dùng sớm để giảm tái phát
    
    **3. Truyền máu:**
    
    - **PRBC:** Nếu Hct <25% hoặc xuất huyết
    - **Platelets:** CHỈ nếu xuất huyết nặng (tránh huyết khối)
    - **FFP:** Không dùng (dùng PLEX thay thế)
    
    **4. Điều trị HUS:**
    
    - **Hỗ trợ:** Nếu do E. coli, thường tự khỏi
    - **Lọc máu:** Nếu suy thận nặng
    - **Antibiotics:** Không dùng (có thể làm nặng)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Đáp ứng")
    
    st.info("""
    **Dấu hiệu Cải thiện:**
    - ✅ Tiểu cầu tăng (≥50,000/μL)
    - ✅ LDH giảm
    - ✅ Haptoglobin tăng
    - ✅ Giảm triệu chứng thần kinh
    - ✅ Creatinine giảm (nếu suy thận)
    
    **Dấu hiệu Không đáp ứng:**
    - ⚠️ Tiểu cầu không tăng sau 3-5 ngày
    - ⚠️ LDH không giảm
    - ⚠️ Triệu chứng thần kinh nặng thêm
    - ⚠️ Suy thận nặng thêm
    
    **Điều chỉnh:**
    - Tăng tần suất PLEX
    - Thêm Rituximab
    - Đánh giá lại chẩn đoán
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Biến chứng")
    
    with st.expander("📋 Xem các biến chứng thường gặp", expanded=False):
        st.markdown("""
        **Thần kinh:**
        - Đột quỵ
        - Co giật
        - Hôn mê
        - Tổn thương não vĩnh viễn
        
        **Thận:**
        - Suy thận cấp
        - Cần lọc máu
        - Suy thận mạn (sau này)
        
        **Tim mạch:**
        - Rối loạn nhịp tim
        - Nhồi máu cơ tim
        - Shock
        
        **Khác:**
        - Xuất huyết
        - Nhiễm trùng
        - Tử vong (nếu không điều trị)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **TTP:** Tử vong 90% nếu không điều trị, <20% với PLEX
    - **HUS:** Tử vong 5-10% (thường tự khỏi)
    - **Yếu tố nguy cơ:**
      - Chậm trễ điều trị
      - Triệu chứng thần kinh nặng
      - Suy thận nặng
    
    **Theo dõi:**
    - **CBC:** Mỗi ngày (tiểu cầu)
    - **LDH, Haptoglobin:** Mỗi 1-2 ngày
    - **Creatinine:** Mỗi ngày
    - **Thần kinh:** Mỗi ngày
    - **PLEX:** Mỗi ngày cho đến khi cải thiện
    
    **Xuất viện:**
    - Tiểu cầu ≥50,000/μL
    - LDH bình thường
    - Không triệu chứng
    - Theo dõi ít nhất 1-2 tuần
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("TTP/HUS")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ASH Guidelines 2024** - American Society of Hematology
        2. **UpToDate:** TTP/HUS Management - Last updated 2024
        3. **Blood Journal** - TTP/HUS Treatment Guidelines
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

