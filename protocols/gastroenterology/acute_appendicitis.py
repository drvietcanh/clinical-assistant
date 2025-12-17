"""
Acute Appendicitis Protocol
WSES 2020, EAST 2020
Management of acute appendicitis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Appendicitis Protocol"""
    st.subheader("🫀 Acute Appendicitis")
    st.caption("WSES 2020, EAST 2020 - Management of acute appendicitis")
    
    st.warning("""
    **⚠️ ACUTE APPENDICITIS = URGENT ASSESSMENT REQUIRED**
    
    **Triệu chứng:**
    - Đau bụng quanh rốn, di chuyển xuống hố chậu phải
    - Sốt, ớn lạnh
    - Buồn nôn, nôn
    - Chán ăn
    - McBurney's point tenderness
    
    **Cần chẩn đoán sớm để tránh biến chứng!**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC SCORES ==========
    st.markdown("### 📊 Diagnostic Scores")
    
    score_type = st.radio(
        "**Chọn thang điểm:**",
        ["Alvarado Score", "Appendicitis Inflammatory Response (AIR) Score"],
        key="appendicitis_score"
    )
    
    if score_type == "Alvarado Score":
        render_alvarado_score()
    else:
        render_air_score()
    
    st.markdown("---")
    
    # ========== SECTION 2: DIAGNOSIS ==========
    st.markdown("### 🔍 Chẩn đoán")
    
    with st.expander("📋 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Clinical Features:**
        - **Migratory pain:** Quanh rốn → hố chậu phải
        - **Anorexia:** Chán ăn
        - **Nausea/Vomiting:** Buồn nôn, nôn
        - **Fever:** Sốt
        - **McBurney's point:** Điểm đau ở 1/3 ngoài đường nối rốn-gai chậu trước trên phải
        - **Rovsing's sign:** Đau hố chậu phải khi ấn hố chậu trái
        - **Psoas sign:** Đau khi duỗi hông phải
        - **Obturator sign:** Đau khi xoay trong hông phải
        
        **Laboratory:**
        - **WBC:** Tăng (> 10,000/μL)
        - **Neutrophils:** Tăng (> 75%)
        - **CRP:** Tăng (> 10 mg/L)
        
        **Imaging:**
        - **CT:** Tiêu chuẩn vàng (độ nhạy > 95%)
        - **US:** Cho trẻ em, phụ nữ có thai
        - **MRI:** Cho phụ nữ có thai
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại")
    
    classification = st.radio(
        "**Phân loại:**",
        ["Uncomplicated", "Complicated (Perforated/Abscess)"],
        key="appendicitis_classification"
    )
    
    st.markdown("---")
    
    if classification == "Uncomplicated":
        render_uncomplicated_protocol()
    else:
        render_complicated_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 4: ANTIBIOTICS ==========
    st.markdown("### 💊 Antibiotics")
    
    with st.expander("📋 Xem liều kháng sinh", expanded=False):
        st.markdown("""
        **Pre-operative (Single dose):**
        - **Cefazolin:** 1-2 g IV
        - **Ceftriaxone:** 1-2 g IV
        - **Metronidazole:** 500 mg IV (nếu cần)
        
        **Post-operative (Uncomplicated):**
        - **Không cần** nếu appendectomy thành công
        
        **Post-operative (Complicated):**
        - **Piperacillin-tazobactam:** 4.5 g IV q8h
        - **Ceftriaxone + Metronidazole:** 1-2 g IV q24h + 500 mg IV q8h
        - **Meropenem:** 1 g IV q8h (nếu nặng)
        - **Duration:** 3-5 ngày hoặc đến khi afebrile 24-48h
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SURGICAL MANAGEMENT ==========
    st.markdown("### 🔪 Surgical Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Laparoscopic Appendectomy:**
        - **Ưu tiên:** Phương pháp chính
        - **Ưu điểm:**
          - Ít đau hơn
          - Phục hồi nhanh hơn
          - Ít biến chứng
          - Thẩm mỹ tốt hơn
        
        **Open Appendectomy:**
        - **Chỉ định:**
          - Không thể laparoscopic
          - Perforated với abscess lớn
          - Nhiều phẫu thuật trước
        """)
    
    with col2:
        st.markdown("""
        **Timing:**
        - **Early (< 24h):** Ưu tiên
        - **Delayed:** Chỉ nếu có lý do y khoa
        
        **Non-operative Management:**
        - **Chỉ định:**
          - Uncomplicated (một số trường hợp)
          - Bệnh nhân từ chối phẫu thuật
          - Không thể phẫu thuật
        - **Antibiotics:** IV → PO
        - **Theo dõi:** Sát
        - **Tỷ lệ tái phát:** 20-30%
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Triệu chứng không điển hình
        - US ưu tiên (tránh radiation)
        - Early appendectomy
        - Laparoscopic ưu tiên
        
        **Người cao tuổi:**
        - Triệu chứng không điển hình
        - Tỷ lệ perforation cao hơn
        - Biến chứng nhiều hơn
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Triệu chứng không điển hình
        - MRI ưu tiên (tránh radiation)
        - Early appendectomy
        - Laparoscopic an toàn
        - Cần tư vấn sản khoa
        
        **Bệnh nhân có bệnh nền:**
        - Điều chỉnh liều thuốc
        - Cẩn thận với biến chứng
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: REFERENCES ==========
    render_references_section(get_references("acute_appendicitis"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_alvarado_score():
    """Alvarado Score Calculator"""
    st.markdown("#### Alvarado Score")
    
    col1, col2 = st.columns(2)
    
    with col1:
        migratory_pain = st.checkbox("Migratory pain (Đau di chuyển)", key="alv_migratory")
        anorexia = st.checkbox("Anorexia (Chán ăn)", key="alv_anorexia")
        nausea_vomiting = st.checkbox("Nausea/Vomiting", key="alv_nausea")
        tenderness_ruq = st.checkbox("Tenderness RUQ", key="alv_tenderness")
    
    with col2:
        rebound_tenderness = st.checkbox("Rebound tenderness", key="alv_rebound")
        elevated_temp = st.checkbox("Temperature > 37.3°C", key="alv_temp")
        wbc_count = st.number_input("WBC (×10³/μL)", 0, 50, 10, 1, key="alv_wbc")
        neutrophils = st.number_input("Neutrophils (%)", 0, 100, 75, 1, key="alv_neutrophils")
    
    # Calculate score
    score = 0
    if migratory_pain:
        score += 1
    if anorexia:
        score += 1
    if nausea_vomiting:
        score += 1
    if tenderness_ruq:
        score += 2
    if rebound_tenderness:
        score += 1
    if elevated_temp:
        score += 1
    if wbc_count > 10:
        score += 2
    if neutrophils > 75:
        score += 1
    
    st.markdown(f"**Alvarado Score: {score}/10**")
    
    if score <= 4:
        st.success("✅ **Nguy cơ thấp** - Có thể không phải appendicitis")
    elif score <= 6:
        st.warning("⚠️ **Nguy cơ trung bình** - Cần theo dõi, cân nhắc imaging")
    else:
        st.error("🚨 **Nguy cơ cao** - Cần phẫu thuật sớm")


def render_air_score():
    """AIR Score Calculator"""
    st.markdown("#### Appendicitis Inflammatory Response (AIR) Score")
    
    col1, col2 = st.columns(2)
    
    with col1:
        vomiting = st.checkbox("Vomiting", key="air_vomiting")
        pain_ruq = st.checkbox("Pain in RUQ", key="air_pain")
        rebound = st.checkbox("Rebound tenderness", key="air_rebound")
        wbc_count = st.number_input("WBC (×10³/μL)", 0, 50, 10, 1, key="air_wbc")
    
    with col2:
        neutrophils = st.number_input("Neutrophils (%)", 0, 100, 75, 1, key="air_neutrophils")
        crp = st.number_input("CRP (mg/L)", 0, 500, 10, 1, key="air_crp")
    
    # Calculate score
    score = 0
    if vomiting:
        score += 1
    if pain_ruq:
        score += 1
    if rebound:
        score += 1
    if 10 <= wbc_count < 15:
        score += 1
    elif wbc_count >= 15:
        score += 2
    if 70 <= neutrophils < 85:
        score += 1
    elif neutrophils >= 85:
        score += 2
    if 10 <= crp < 50:
        score += 1
    elif crp >= 50:
        score += 2
    
    st.markdown(f"**AIR Score: {score}/12**")
    
    if score <= 4:
        st.success("✅ **Nguy cơ thấp** - Có thể không phải appendicitis")
    elif score <= 8:
        st.warning("⚠️ **Nguy cơ trung bình** - Cần theo dõi, cân nhắc imaging")
    else:
        st.error("🚨 **Nguy cơ cao** - Cần phẫu thuật sớm")


def render_uncomplicated_protocol():
    """Uncomplicated Appendicitis Protocol"""
    st.success("## ✅ UNCOMPLICATED APPENDICITIS")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Pre-operative:**
       - **Antibiotics:** Single dose (Cefazolin 1-2 g IV)
       - **NPO:** Không ăn uống
       - **Pain control:** Morphine 2-5 mg IV
    
    2. **Surgery:**
       - **Laparoscopic appendectomy:** Ưu tiên
       - **Timing:** Trong vòng 24 giờ
       - **Duration:** 30-60 phút
    
    3. **Post-operative:**
       - **Antibiotics:** Không cần (nếu thành công)
       - **Diet:** Bắt đầu với clear liquids
       - **Discharge:** 24-48 giờ sau phẫu thuật
    
    4. **Follow-up:**
       - 1-2 tuần sau
       - Kiểm tra vết mổ
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Early appendectomy tốt hơn delayed
    - Laparoscopic ưu tiên
    - Không cần antibiotics sau phẫu thuật nếu uncomplicated
    - Phục hồi nhanh với laparoscopic
    """)


def render_complicated_protocol():
    """Complicated Appendicitis Protocol"""
    st.error("## 🚨 COMPLICATED APPENDICITIS")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Pre-operative:**
       - **Antibiotics:** Broad-spectrum (Piperacillin-tazobactam 4.5 g IV)
       - **Resuscitation:** Fluid, vasopressors nếu cần
       - **NPO:** Không ăn uống
    
    2. **Surgery:**
       - **Laparoscopic:** Có thể
       - **Open:** Cân nhắc nếu abscess lớn
       - **Timing:** Trong vòng 24 giờ (hoặc sớm hơn nếu nặng)
       - **Drainage:** Đặt drain nếu cần
    
    3. **Post-operative:**
       - **Antibiotics:** Tiếp tục 3-5 ngày
       - **Drain:** Theo dõi, rút khi không còn dịch
       - **Diet:** Bắt đầu chậm
       - **Discharge:** 3-5 ngày sau phẫu thuật
    
    4. **Follow-up:**
       - 1-2 tuần sau
       - Kiểm tra vết mổ, drain
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Cần antibiotics lâu hơn
    - Có thể cần drain
    - Theo dõi sát biến chứng
    - Phục hồi chậm hơn uncomplicated
    """)

