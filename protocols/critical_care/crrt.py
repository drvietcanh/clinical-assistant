"""
CRRT (Continuous Renal Replacement Therapy) Protocol
KDIGO Guidelines 2024, UpToDate 2024
Continuous dialysis for critically ill patients
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """CRRT Management Protocol"""
    st.subheader("🧪 CRRT (Continuous Renal Replacement Therapy)")
    st.caption("KDIGO Guidelines 2024, UpToDate 2024 - Continuous dialysis")
    
    st.error("""
    **⚠️ CRRT = ĐIỀU TRỊ HỒI SỨC - CẦN MONITORING SÁT**
    
    **Định nghĩa:**
    - Lọc máu liên tục 24h
    - Dùng cho bệnh nhân ICU không ổn định
    - Ít hạ huyết áp hơn Hemodialysis
    
    **Chỉ định:**
    - **Hạ huyết áp nặng:** (không thể Hemodialysis)
    - **Quá tải dịch nặng:** (cần lọc máu liên tục)
    - **Suy đa tạng:** (cần điều trị nhẹ nhàng)
    - **Rối loạn điện giải:** (cần điều chỉnh chậm)
    - **Ngộ độc:** (một số trường hợp)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chỉ định CRRT")
    
    indication = st.radio(
        "**Chỉ định CRRT:**",
        [
            "Hạ huyết áp nặng (Không thể Hemodialysis)",
            "Quá tải dịch nặng (Cần lọc máu liên tục)",
            "Suy đa tạng (Cần điều trị nhẹ nhàng)",
            "Rối loạn điện giải (Cần điều chỉnh chậm)",
            "Ngộ độc (Một số trường hợp)"
        ],
        key="crrt_indication"
    )
    
    st.markdown("---")
    
    st.markdown("### 💉 Kỹ thuật CRRT")
    
    crrt_mode = st.radio(
        "**Chế độ CRRT:**",
        [
            "CVVH (Continuous Veno-Venous Hemofiltration)",
            "CVVHD (Continuous Veno-Venous Hemodialysis)",
            "CVVHDF (Continuous Veno-Venous Hemodiafiltration)"
        ],
        key="crrt_mode"
    )
    
    st.markdown("---")
    
    if "CVVH" in crrt_mode:
        render_cvvh()
    elif "CVVHD" in crrt_mode:
        render_cvvhd()
    else:
        render_cvvhdf()
    
    st.markdown("---")
    
    st.markdown("### 📊 Tính toán Liều")
    
    col1, col2 = st.columns(2)
    
    with col1:
        patient_weight = st.number_input(
            "**Cân nặng (kg):**",
            min_value=0,
            max_value=200,
            value=70,
            step=1,
            format="%d"
        )
        
        target_uf_rate = st.number_input(
            "**Tốc độ Ultrafiltration (mL/h):**",
            min_value=0,
            max_value=2000,
            value=100,
            step=50
        )
    
    with col2:
        dialysate_rate = st.number_input(
            "**Tốc độ Dialysate (mL/h):**",
            min_value=0,
            max_value=5000,
            value=1000,
            step=100
        )
        
        replacement_rate = st.number_input(
            "**Tốc độ Replacement (mL/h):**",
            min_value=0,
            max_value=5000,
            value=1000,
            step=100
        )
    
    if st.button("Tính Liều CRRT"):
        # Effluent rate = UF + Dialysate + Replacement
        effluent_rate = target_uf_rate + dialysate_rate + replacement_rate
        dose_per_kg = effluent_rate / patient_weight if patient_weight > 0 else 0
        
        st.markdown(f"### Effluent Rate: **{effluent_rate} mL/h**")
        st.markdown(f"### Dose: **{dose_per_kg:.1f} mL/kg/h**")
        
        if dose_per_kg >= 25:
            st.success("✅ **Liều đủ** - ≥25 mL/kg/h (KDIGO khuyến nghị)")
        elif dose_per_kg >= 20:
            st.warning("⚠️ **Liều trung bình** - 20-25 mL/kg/h")
        else:
            st.error("🚨 **Liều thấp** - <20 mL/kg/h - Cần tăng")
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Anticoagulation:**
    
    **Heparin:**
    - **Liều:** 5-10 units/kg/h
    - **Mục tiêu:** aPTT 40-50s
    - **Lưu ý:** Có thể gây xuất huyết
    
    **Citrate (Ưu tiên):**
    - **Liều:** 3-4 mmol/L blood flow
    - **Lợi ích:** Ít xuất huyết hơn
    - **Lưu ý:** Cần theo dõi Ca
    
    **2. Monitoring:**
    - **Huyết áp, HR:** Mỗi 15-30 phút
    - **Electrolytes:** Mỗi 4-6h
    - **Creatinine, BUN:** Mỗi 12-24h
    - **Cân bằng nước:** Mỗi giờ
    
    **3. Complications:**
    - Hạ huyết áp
    - Rối loạn điện giải
    - Xuất huyết (nếu dùng heparin)
    - Nhiễm trùng catheter
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("CRRT")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **KDIGO Guidelines 2024** - Kidney Disease: Improving Global Outcomes
        2. **UpToDate:** CRRT - Last updated 2024
        3. **AJKD** - American Journal of Kidney Diseases
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_cvvh():
    """CVVH"""
    st.info("## ℹ️ CVVH - HEMOFILTRATION")
    
    st.markdown("""
    **Cơ chế:**
    - Convection (kéo theo nước)
    - Loại bỏ chất hòa tan
    
    **Thông số:**
    - **Blood flow:** 100-200 mL/min
    - **Replacement:** 1-3 L/h
    - **UF rate:** 100-500 mL/h
    
    **Chỉ định:**
    - Quá tải dịch
    - Cần loại bỏ chất hòa tan lớn
    """)


def render_cvvhd():
    """CVVHD"""
    st.info("## ℹ️ CVVHD - HEMODIALYSIS")
    
    st.markdown("""
    **Cơ chế:**
    - Diffusion (khuếch tán)
    - Loại bỏ chất hòa tan nhỏ
    
    **Thông số:**
    - **Blood flow:** 100-200 mL/min
    - **Dialysate:** 1-3 L/h
    - **UF rate:** 100-500 mL/h
    
    **Chỉ định:**
    - Suy thận
    - Cần loại bỏ chất hòa tan nhỏ
    """)


def render_cvvhdf():
    """CVVHDF"""
    st.success("## ✅ CVVHDF - HEMODIAFILTRATION (Ưu tiên)")
    
    st.markdown("""
    **Cơ chế:**
    - Cả convection và diffusion
    - Loại bỏ cả chất hòa tan nhỏ và lớn
    
    **Thông số:**
    - **Blood flow:** 100-200 mL/min
    - **Dialysate:** 1-2 L/h
    - **Replacement:** 1-2 L/h
    - **UF rate:** 100-500 mL/h
    
    **Chỉ định:**
    - Hầu hết các trường hợp
    - Hiệu quả nhất
    """)

