"""
Emergency Dialysis Protocol
KDIGO Guidelines 2024, UpToDate 2024
Indications and management of emergency dialysis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Emergency Dialysis Management Protocol"""
    st.subheader("🧪 Lọc Máu Cấp Cứu (Emergency Dialysis)")
    st.caption("KDIGO Guidelines 2024, UpToDate 2024 - Indications and management")
    
    st.error("""
    **⚠️ LỌC MÁU CẤP CỨU = CẦN ĐIỀU TRỊ NGAY**
    
    **Chỉ định Cấp cứu:**
    - **AEIOU mnemonic:**
      - **A:** Acidosis nặng (pH <7.2)
      - **E:** Electrolytes (K >6.5 mEq/L, Na quá cao/thấp)
      - **I:** Intoxication (ngộ độc)
      - **O:** Overload (quá tải dịch, phù phổi)
      - **U:** Uremia (uremia nặng, hôn mê)
    
    **Triệu chứng:**
    - Hôn mê, lú lẫn
    - Co giật
    - Suy hô hấp
    - Phù phổi
    - Loạn nhịp tim
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu hôn mê
        - Suy hô hấp
        - Phù phổi nặng
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG** (loạn nhịp tim)
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **Thận trọng:** Tránh quá tải
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **Central line:** (cho dialysis catheter)
        - **2 đường tĩnh mạch** (nếu cần)
        
        **4. LABS NGAY:**
        - **ABG:** pH, HCO₃, CO₂
        - **Electrolytes:** K, Na, Mg, Ca, P
        - **Creatinine, BUN:** (suy thận)
        - **CBC:** (thiếu máu)
        - **Coagulation:** (nếu cần)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chỉ định Lọc máu")
    
    indication_type = st.radio(
        "**Loại chỉ định:**",
        [
            "Acidosis nặng (pH <7.2)",
            "Tăng K máu nặng (K >6.5 mEq/L)",
            "Quá tải dịch (Phù phổi, không đáp ứng diuretics)",
            "Uremia nặng (Hôn mê, co giật)",
            "Ngộ độc (Có thể lọc được)",
            "Rối loạn điện giải khác"
        ],
        key="dialysis_indication"
    )
    
    st.markdown("---")
    
    if "Acidosis" in indication_type:
        render_acidosis()
    elif "Tăng K" in indication_type:
        render_hyperkalemia()
    elif "Quá tải" in indication_type:
        render_fluid_overload()
    elif "Uremia" in indication_type:
        render_uremia()
    elif "Ngộ độc" in indication_type:
        render_intoxication()
    else:
        render_electrolyte_disorder()
    
    st.markdown("---")
    
    st.markdown("### 💉 Kỹ thuật Lọc máu")
    
    dialysis_type = st.radio(
        "**Loại Lọc máu:**",
        [
            "Hemodialysis (HD) - Ưu tiên",
            "Continuous Renal Replacement Therapy (CRRT)",
            "Peritoneal Dialysis (PD) - Ít dùng trong cấp cứu"
        ],
        key="dialysis_type"
    )
    
    st.markdown("---")
    
    if "Hemodialysis" in dialysis_type:
        render_hemodialysis()
    elif "CRRT" in dialysis_type:
        render_crrt()
    else:
        render_peritoneal_dialysis()
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Truyền máu:**
    - **PRBC:** Nếu Hct <25% hoặc xuất huyết
    - **Lưu ý:** Tránh truyền trước lọc máu (tăng K)
    
    **2. Điều chỉnh Điện giải:**
    - **Tăng K:** Điều trị trước lọc máu (nếu cần)
    - **Hạ Ca:** Bổ sung Ca (nếu cần)
    - **Hạ P:** Bổ sung P (nếu cần)
    
    **3. Monitoring:**
    - **Huyết áp, HR:** Mỗi 15-30 phút
    - **ABG:** Mỗi 2-4h (nếu acidosis)
    - **Electrolytes:** Mỗi 2-4h
    - **Creatinine, BUN:** Mỗi 6-12h
    
    **4. Biến chứng:**
    - Hạ huyết áp
    - Chuột rút
    - Buồn nôn, nôn
    - Rối loạn nhịp tim
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Chống chỉ định & Lưu ý")
    
    st.warning("""
    **Chống chỉ định Tương đối:**
    - Hạ huyết áp nặng (có thể dùng CRRT)
    - Rối loạn đông máu nặng
    - Không có đường truy cập
    
    **Lưu ý:**
    - **Dialysis catheter:** Cần đặt trước
    - **Anticoagulation:** Heparin (nếu không chống chỉ định)
    - **Tốc độ:** Thận trọng (tránh hạ huyết áp)
    - **Thời gian:** 3-4h (HD), liên tục (CRRT)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - Phụ thuộc vào nguyên nhân
    - Tốt nếu điều trị sớm
    - Xấu nếu chậm trễ
    
    **Theo dõi:**
    - **Trong lọc máu:** Huyết áp, HR (mỗi 15-30 phút)
    - **Sau lọc máu:** Electrolytes, Creatinine (mỗi 6-12h)
    - **Triệu chứng:** Mỗi ngày
    
    **Xuất viện:**
    - Ổn định sau lọc máu
    - Không chỉ định cấp cứu
    - Đã điều chỉnh thuốc
    - Theo dõi ít nhất 24-48h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Emergency Dialysis")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **KDIGO Guidelines 2024** - Kidney Disease: Improving Global Outcomes
        2. **UpToDate:** Emergency Dialysis - Last updated 2024
        3. **AJKD** - American Journal of Kidney Diseases
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_acidosis():
    """Acidosis Indication"""
    st.error("## 🚨 ACIDOSIS NẶNG - LỌC MÁU CẤP CỨU")
    
    st.markdown("""
    **Chỉ định:**
    - pH <7.2
    - HCO₃ <12 mEq/L
    - Không đáp ứng với bicarbonate
    
    **Điều trị:**
    - **Hemodialysis:** (ưu tiên)
    - **Bicarbonate dialysate:** 35-40 mEq/L
    - **Thời gian:** 3-4h
    
    **Mục tiêu:**
    - pH ≥7.2
    - HCO₃ ≥15 mEq/L
    """)


def render_hyperkalemia():
    """Hyperkalemia Indication"""
    st.error("## 🚨 TĂNG K MÁU NẶNG - LỌC MÁU CẤP CỨU")
    
    st.markdown("""
    **Chỉ định:**
    - K >6.5 mEq/L
    - Hoặc K >6.0 mEq/L + ECG thay đổi
    
    **Điều trị Trước lọc máu:**
    - **Calcium:** 1-2 g IV (bảo vệ tim)
    - **Insulin + Glucose:** 10 units + 50g
    - **Sodium Bicarbonate:** 50-100 mEq IV
    - **Kayexalate:** 15-30 g PO/PR
    
    **Lọc máu:**
    - **Hemodialysis:** (ưu tiên)
    - **K-free dialysate:** (nếu có thể)
    - **Thời gian:** 3-4h
    
    **Mục tiêu:**
    - K <5.5 mEq/L
    """)


def render_fluid_overload():
    """Fluid Overload Indication"""
    st.error("## 🚨 QUÁ TẢI DỊCH - LỌC MÁU CẤP CỨU")
    
    st.markdown("""
    **Chỉ định:**
    - Phù phổi không đáp ứng diuretics
    - Anasarca
    - Quá tải dịch >10% cân nặng
    
    **Điều trị:**
    - **Hemodialysis:** (ưu tiên, nhanh)
    - **Hoặc:** CRRT (nếu hạ huyết áp)
    - **Ultrafiltration:** 2-4 L trong 3-4h
    
    **Mục tiêu:**
    - Giảm cân 2-4 kg
    - Giảm phù phổi
    - Cải thiện hô hấp
    """)


def render_uremia():
    """Uremia Indication"""
    st.error("## 🚨 UREMIA NẶNG - LỌC MÁU CẤP CỨU")
    
    st.markdown("""
    **Chỉ định:**
    - BUN >100 mg/dL
    - Hôn mê, lú lẫn
    - Co giật
    - Viêm màng ngoài tim
    
    **Điều trị:**
    - **Hemodialysis:** (ưu tiên)
    - **Thời gian:** 3-4h
    - **Lặp lại:** Mỗi ngày nếu cần
    
    **Mục tiêu:**
    - BUN <80 mg/dL
    - Cải thiện triệu chứng
    """)


def render_intoxication():
    """Intoxication Indication"""
    st.warning("## ⚠️ NGỘ ĐỘC - LỌC MÁU (Nếu có thể)")
    
    st.markdown("""
    **Chỉ định:**
    - Ngộ độc có thể lọc được
    - Nồng độ cao
    - Không đáp ứng điều trị khác
    
    **Có thể lọc:**
    - Lithium
    - Salicylates
    - Methanol, Ethylene Glycol
    - Theophylline
    - Barbiturates
    
    **Không thể lọc:**
    - TCA
    - Digoxin
    - Benzodiazepines
    
    **Điều trị:**
    - **Hemodialysis:** (ưu tiên)
    - **Hoặc:** Hemoperfusion (nếu có)
    - **Thời gian:** 3-4h
    """)


def render_electrolyte_disorder():
    """Electrolyte Disorder Indication"""
    st.warning("## ⚠️ RỐI LOẠN ĐIỆN GIẢI KHÁC")
    
    st.markdown("""
    **Chỉ định:**
    - Na quá cao/thấp (nếu nặng)
    - Ca quá cao/thấp (nếu nặng)
    - P quá cao (nếu nặng)
    
    **Điều trị:**
    - **Hemodialysis:** (nếu cần)
    - **Điều chỉnh dialysate:** Theo nhu cầu
    
    **Mục tiêu:**
    - Điện giải bình thường
    """)


def render_hemodialysis():
    """Hemodialysis"""
    st.success("## ✅ HEMODIALYSIS - ƯU TIÊN")
    
    st.markdown("""
    **Chỉ định:**
    - Hầu hết các trường hợp cấp cứu
    - Nhanh, hiệu quả
    
    **Kỹ thuật:**
    - **Dialysis catheter:** Đặt vào tĩnh mạch lớn
    - **Blood flow:** 200-400 mL/min
    - **Dialysate flow:** 500-800 mL/min
    - **Thời gian:** 3-4h
    - **Tần suất:** Mỗi ngày (nếu cần)
    
    **Lợi ích:**
    - Nhanh
    - Hiệu quả
    - Có thể điều chỉnh
    
    **Nhược điểm:**
    - Cần đường truy cập
    - Có thể hạ huyết áp
    - Không liên tục
    """)


def render_crrt():
    """CRRT"""
    st.info("## ℹ️ CRRT - LIÊN TỤC")
    
    st.markdown("""
    **Chỉ định:**
    - Hạ huyết áp nặng
    - Quá tải dịch nặng
    - Cần lọc máu liên tục
    
    **Kỹ thuật:**
    - **Dialysis catheter:** Đặt vào tĩnh mạch lớn
    - **Blood flow:** 100-200 mL/min
    - **Dialysate flow:** 1-3 L/h
    - **Thời gian:** Liên tục 24h
    - **Tần suất:** Mỗi ngày
    
    **Lợi ích:**
    - Liên tục
    - Ít hạ huyết áp
    - Có thể điều chỉnh
    
    **Nhược điểm:**
    - Chậm hơn HD
    - Cần monitoring sát
    - Tốn kém hơn
    """)


def render_peritoneal_dialysis():
    """Peritoneal Dialysis"""
    st.warning("## ⚠️ PERITONEAL DIALYSIS - ÍT DÙNG")
    
    st.markdown("""
    **Chỉ định:**
    - Không có đường truy cập tĩnh mạch
    - Hạ huyết áp nặng
    - Chống chỉ định HD
    
    **Kỹ thuật:**
    - **PD catheter:** Đặt vào ổ bụng
    - **Dialysate:** 1-2 L mỗi lần
    - **Thời gian:** 30-60 phút mỗi lần
    - **Tần suất:** 4-6 lần/ngày
    
    **Lợi ích:**
    - Không cần đường truy cập tĩnh mạch
    - Ít hạ huyết áp
    
    **Nhược điểm:**
    - Chậm
    - Có thể nhiễm trùng
    - Không hiệu quả bằng HD
    """)

