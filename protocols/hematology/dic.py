"""
DIC (Disseminated Intravascular Coagulation) Protocol
ISTH Guidelines 2024, ASH Guidelines 2024
Life-threatening coagulopathy
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """DIC Management Protocol"""
    st.subheader("🩸 DIC (Disseminated Intravascular Coagulation)")
    st.caption("ISTH Guidelines 2024, ASH Guidelines 2024 - Life-threatening coagulopathy")
    
    st.error("""
    **⚠️ DIC = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - Kích hoạt đông máu lan tỏa
    - Tiêu thụ các yếu tố đông máu
    - Huyết khối vi mạch + Xuất huyết
    
    **Nguyên nhân:**
    - **Nhiễm trùng:** Sepsis (phổ biến nhất)
    - **Chấn thương:** Chấn thương nặng, bỏng
    - **Sản khoa:** Nhau bong non, sản giật
    - **Ung thư:** Đặc biệt ung thư máu
    - **Khác:** Viêm tụy, phản ứng truyền máu
    
    **Triệu chứng:**
    - Xuất huyết (da, niêm mạc, nội tạng)
    - Huyết khối (vi mạch, đại mạch)
    - Suy đa tạng
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức
        - Suy hô hấp
        - Xuất huyết đường thở
        
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
        - **Thận trọng:** Suy thận, phù phổi
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị truyền máu
        
        **4. LABS NGAY:**
        - **PT/INR, aPTT:** (kéo dài)
        - **Fibrinogen:** (giảm)
        - **D-dimer:** (tăng cao)
        - **Platelets:** (giảm)
        - **FDP:** (tăng)
        - **CBC, BMP**
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán (ISTH Score):**
    
    **1. Nguyên nhân rõ ràng:** +2 điểm
    - Sepsis, chấn thương, sản khoa, ung thư
    
    **2. PT/INR:**
    - <1.25: 0 điểm
    - 1.25-1.66: +1 điểm
    - >1.66: +2 điểm
    
    **3. Platelets:**
    - >100,000/μL: 0 điểm
    - 50-100,000/μL: +1 điểm
    - <50,000/μL: +2 điểm
    
    **4. Fibrinogen:**
    - >100 mg/dL: 0 điểm
    - <100 mg/dL: +1 điểm
    
    **5. D-dimer/FDP:**
    - Bình thường: 0 điểm
    - Tăng nhẹ: +2 điểm
    - Tăng nặng: +3 điểm
    
    **Chẩn đoán:**
    - **≥5 điểm:** DIC xác định
    - **<5 điểm:** Theo dõi, đánh giá lại
    """)
    
    # DIC Score Calculator
    st.markdown("### 📊 DIC Score Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        has_underlying_cause = st.checkbox("Có nguyên nhân rõ ràng (Sepsis, chấn thương, sản khoa, ung thư)", key="dic_cause")
        pt_inr = st.number_input("**PT/INR:**", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
        platelet_count = st.number_input("**Số lượng Tiểu cầu (×10³/μL):**", min_value=0, max_value=500, value=100, step=5)
    
    with col2:
        fibrinogen = st.number_input("**Fibrinogen (mg/dL):**", min_value=0, max_value=500, value=200, step=10)
        d_dimer_level = st.radio(
            "**D-dimer/FDP:**",
            ["Bình thường", "Tăng nhẹ", "Tăng nặng"],
            key="dic_ddimer"
        )
    
    if st.button("Tính DIC Score"):
        score = 0
        
        if has_underlying_cause:
            score += 2
        
        if pt_inr < 1.25:
            score += 0
        elif pt_inr <= 1.66:
            score += 1
        else:
            score += 2
        
        if platelet_count > 100:
            score += 0
        elif platelet_count >= 50:
            score += 1
        else:
            score += 2
        
        if fibrinogen > 100:
            score += 0
        else:
            score += 1
        
        if d_dimer_level == "Bình thường":
            score += 0
        elif d_dimer_level == "Tăng nhẹ":
            score += 2
        else:
            score += 3
        
        st.markdown(f"### DIC Score: **{score}**")
        
        if score >= 5:
            st.error("🚨 **DIC XÁC ĐỊNH** - Cần điều trị ngay!")
        else:
            st.warning("⚠️ **Chưa đủ tiêu chuẩn DIC** - Theo dõi, đánh giá lại")
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị")
    
    st.error("## 🚨 ĐIỀU TRỊ NGUYÊN NHÂN - ƯU TIÊN")
    
    st.success("""
    **1. ĐIỀU TRỊ NGUYÊN NHÂN (Quan trọng nhất!)**
    
    **Nếu Sepsis:**
    - Kháng sinh phù hợp
    - Điều trị sốc
    - Source control
    
    **Nếu Chấn thương:**
    - Kiểm soát chảy máu
    - Phẫu thuật (nếu cần)
    
    **Nếu Sản khoa:**
    - Lấy thai (nếu cần)
    - Điều trị sản giật
    
    **Nếu Ung thư:**
    - Hóa trị (nếu có thể)
    
    **Lưu ý:** DIC sẽ không cải thiện nếu không điều trị nguyên nhân!
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Hỗ trợ")
    
    treatment_focus = st.radio(
        "**Trọng tâm Điều trị:**",
        [
            "Xuất huyết nổi trội (Bleeding dominant)",
            "Huyết khối nổi trội (Thrombosis dominant)",
            "Cả hai (Mixed)"
        ],
        key="dic_treatment_focus"
    )
    
    st.markdown("---")
    
    if "Bleeding" in treatment_focus:
        render_bleeding_dominant()
    elif "Thrombosis" in treatment_focus:
        render_thrombosis_dominant()
    else:
        render_mixed()
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi")
    
    st.info("""
    **Theo dõi:**
    - **PT/INR, aPTT:** Mỗi 6-12h
    - **Fibrinogen:** Mỗi 6-12h
    - **Platelets:** Mỗi 6-12h
    - **D-dimer:** Mỗi 12-24h
    - **Triệu chứng:** Xuất huyết, huyết khối
    
    **Dấu hiệu Cải thiện:**
    - ✅ PT/INR giảm
    - ✅ Fibrinogen tăng
    - ✅ Platelets tăng
    - ✅ D-dimer giảm
    - ✅ Giảm xuất huyết
    
    **Tiên lượng:**
    - Phụ thuộc vào nguyên nhân
    - Tử vong: 30-50% (nếu nặng)
    - Tốt hơn nếu điều trị nguyên nhân sớm
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("DIC")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ISTH Guidelines 2024** - International Society on Thrombosis and Haemostasis
        2. **ASH Guidelines 2024** - American Society of Hematology
        3. **UpToDate:** DIC Management - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_bleeding_dominant():
    """Bleeding Dominant DIC"""
    st.error("## 🚨 XUẤT HUYẾT NỔI TRỘI")
    
    st.markdown("""
    **Đặc điểm:**
    - Xuất huyết nhiều
    - Giảm tiểu cầu nặng
    - Fibrinogen giảm
    - PT/INR kéo dài
    
    **Điều trị:**
    
    **1. Truyền máu:**
    - **FFP:** 10-15 mL/kg (bổ sung yếu tố đông máu)
    - **Platelets:** 1 đơn vị/10 kg (nếu <50,000/μL và xuất huyết)
    - **Cryoprecipitate:** 10 đơn vị (nếu fibrinogen <100 mg/dL)
    
    **2. Anticoagulation:**
    - **KHÔNG dùng** (làm nặng xuất huyết)
    
    **3. Monitoring:**
    - Xuất huyết
    - PT/INR, Fibrinogen
    - Platelets
    """)


def render_thrombosis_dominant():
    """Thrombosis Dominant DIC"""
    st.warning("## ⚠️ HUYẾT KHỐI NỔI TRỘI")
    
    st.markdown("""
    **Đặc điểm:**
    - Huyết khối nhiều
    - Có thể có xuất huyết nhẹ
    - D-dimer tăng rất cao
    
    **Điều trị:**
    
    **1. Anticoagulation:**
    - **Heparin:** 10-15 units/kg/h IV (thận trọng)
    - **Hoặc:** LMWH (nếu ổn định)
    - **Mục đích:** Giảm huyết khối
    
    **2. Truyền máu:**
    - **Thận trọng:** Chỉ nếu xuất huyết nặng
    - **FFP:** Nếu cần
    - **Platelets:** Chỉ nếu xuất huyết
    
    **3. Monitoring:**
    - Huyết khối
    - PT/INR, aPTT
    - D-dimer
    """)


def render_mixed():
    """Mixed DIC"""
    st.error("## 🚨 CẢ HAI - XUẤT HUYẾT VÀ HUYẾT KHỐI")
    
    st.markdown("""
    **Đặc điểm:**
    - Có cả xuất huyết và huyết khối
    - Phức tạp nhất
    
    **Điều trị:**
    
    **1. Cân bằng:**
    - **Truyền máu:** Nếu xuất huyết nặng
    - **Anticoagulation:** Thận trọng, liều thấp
    
    **2. Monitoring:**
    - Cả xuất huyết và huyết khối
    - PT/INR, Fibrinogen, Platelets
    - D-dimer
    
    **3. Điều chỉnh:**
    - Theo triệu chứng nổi trội
    - Thận trọng với cả hai
    """)

