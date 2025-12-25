"""
STEMI (ST-Elevation Myocardial Infarction) Protocol
ESC/ACC Guidelines 2024, AHA/ACC 2023
Acute coronary syndrome requiring immediate reperfusion
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """STEMI Management Protocol"""
    st.subheader("💔 STEMI (ST-Elevation Myocardial Infarction)")
    st.caption("ESC/ACC Guidelines 2024, AHA/ACC 2023 - Acute coronary syndrome")
    
    st.error("""
    **⚠️ STEMI = CẤP CỨU Y KHOA - TÁI TƯỚI MÁU NGAY**
    
    **Tiêu chuẩn Chẩn đoán:**
    - **ECG:** ST chênh lên ≥1mm ở ≥2 chuyển đạo liên tiếp
    - **Hoặc:** Block nhánh mới + Triệu chứng
    - **Triệu chứng:** Đau ngực, khó thở, vã mồ hôi
    
    **Mục tiêu Điều trị:**
    - **Door-to-balloon:** <90 phút
    - **Door-to-needle:** <30 phút (nếu không có PCI)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Oxygen:**
        - **Chỉ nếu:** SpO₂ <90% hoặc suy hô hấp
        - **Liều:** 2-4 L/min qua nasal cannula
        - **Lưu ý:** Tránh oxygen không cần thiết
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 5-15 phút
        
        **Truyền dịch:**
        - **NS:** 250-500 mL bolus (nếu hạ HA)
        - **Thận trọng:** Tránh quá tải
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị thuốc
        
        **4. LABS NGAY:**
        - **Troponin:** (nhưng không chờ kết quả)
        - **CK-MB:** (nếu có)
        - **CBC, BMP, Coagulation**
        - **Lipid panel:** (nếu có thể)
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Thuốc")
    
    st.success("""
    **1. ASPIRIN (Ngay lập tức)**
    
    - **Liều:** 325 mg PO (nhai) hoặc 300 mg IV
    - **Chống chỉ định:** Dị ứng nặng, xuất huyết hoạt động
    
    **2. P2Y12 INHIBITOR (Ngay lập tức)**
    
    **Ticagrelor (Ưu tiên):**
    - **Liều:** 180 mg PO (loading dose)
    - **Duy trì:** 90 mg PO bid
    
    **Hoặc Clopidogrel:**
    - **Liều:** 600 mg PO (loading dose)
    - **Duy trì:** 75 mg PO qd
    
    **Hoặc Prasugrel:**
    - **Liều:** 60 mg PO (loading dose)
    - **Duy trì:** 10 mg PO qd
    - **Chống chỉ định:** Tiền sử TIA/Stroke, tuổi ≥75
    
    **3. ATORVASTATIN (Ngay lập tức)**
    
    - **Liều:** 80 mg PO
    - **Mục tiêu:** Giảm LDL, ổn định mảng xơ vữa
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔄 Tái tưới máu (Reperfusion)")
    
    reperfusion_strategy = st.radio(
        "**Chiến lược Tái tưới máu:**",
        [
            "PCI (Primary PCI) - Ưu tiên",
            "Fibrinolysis (Nếu không có PCI)",
            "Không có cả hai (Transfer)"
        ],
        key="stemi_reperfusion"
    )
    
    st.markdown("---")
    
    if "PCI" in reperfusion_strategy:
        render_primary_pci()
    elif "Fibrinolysis" in reperfusion_strategy:
        render_fibrinolysis()
    else:
        render_transfer()
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Anticoagulation:**
    
    **Heparin (Nếu PCI):**
    - **Liều:** 70-100 units/kg IV bolus
    - **Duy trì:** 12-15 units/kg/h
    - **Mục tiêu:** aPTT 50-70s
    
    **Hoặc Enoxaparin:**
    - **Liều:** 1 mg/kg SC q12h
    - **Hoặc:** 0.75 mg/kg SC q12h (nếu CrCl <30)
    
    **2. Beta-blockers:**
    
    - **Metoprolol:** 25-50 mg PO bid (nếu không chống chỉ định)
    - **Chống chỉ định:** 
      - Suy tim nặng
      - AV block
      - Shock
      - COPD nặng
    
    **3. ACE Inhibitors:**
    
    - **Lisinopril:** 5-10 mg PO qd (nếu không chống chỉ định)
    - **Chống chỉ định:**
      - Hạ huyết áp
      - Suy thận nặng
      - Tăng K
    
    **4. Monitoring:**
    - ECG liên tục
    - Troponin (mỗi 6-12h)
    - CK-MB (nếu có)
    - Chức năng thận
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Biến chứng")
    
    with st.expander("📋 Xem các biến chứng thường gặp", expanded=False):
        st.markdown("""
        **Tim mạch:**
        - Shock tim
        - Rối loạn nhịp tim (VT, VF, bradycardia)
        - Vỡ tim
        - Hở van 2 lá cấp
        - Thủng vách tim
        
        **Cơ học:**
        - Vỡ tim
        - Hở van
        - Thủng vách
        
        **Huyết khối:**
        - Huyết khối trong stent
        - Tái nhồi máu
        
        **Khác:**
        - Suy tim
        - Viêm màng ngoài tim
        """)
    
    st.markdown("---")
    
    # References
    references = get_references("STEMI")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ESC/ACC Guidelines 2024** - European Society of Cardiology
        2. **AHA/ACC Guidelines 2023** - American Heart Association
        3. **UpToDate:** STEMI Management - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_primary_pci():
    """Primary PCI"""
    st.success("## ✅ PRIMARY PCI - ƯU TIÊN")
    
    st.markdown("""
    **Chỉ định:**
    - **Tất cả bệnh nhân STEMI** (nếu có thể)
    - **Mục tiêu:** Door-to-balloon <90 phút
    
    **Trước PCI:**
    - Aspirin 325 mg
    - P2Y12 inhibitor (loading dose)
    - Atorvastatin 80 mg
    - Heparin (nếu cần)
    
    **Trong PCI:**
    - Stent (Drug-eluting stent ưu tiên)
    - GP IIb/IIIa inhibitor (nếu cần)
    
    **Sau PCI:**
    - DAPT (Dual Antiplatelet Therapy):
      - Aspirin 81-100 mg PO qd
      - P2Y12 inhibitor (duy trì)
    - Atorvastatin 80 mg PO qd
    - Beta-blocker (nếu không chống chỉ định)
    - ACE inhibitor (nếu không chống chỉ định)
    
    **Theo dõi:**
    - ECG mỗi 6-12h
    - Troponin mỗi 6-12h
    - Chức năng thận
    """)


def render_fibrinolysis():
    """Fibrinolysis"""
    st.warning("## ⚠️ FIBRINOLYSIS - Nếu không có PCI")
    
    st.markdown("""
    **Chỉ định:**
    - **Không có PCI trong 120 phút**
    - **Triệu chứng <12h**
    - **Không chống chỉ định**
    
    **Chống chỉ định:**
    - **Tuyệt đối:**
      - Tiền sử xuất huyết nội sọ
      - Đột quỵ trong 3 tháng
      - Tổn thương não
      - Xuất huyết hoạt động
      - Phình động mạch chủ
    
    - **Tương đối:**
      - Huyết áp >180/110
      - Đột quỵ >3 tháng
      - Dùng warfarin
      - Chấn thương gần đây
    
    **Thuốc:**
    
    **Alteplase (tPA):**
    - **Liều:** 90 phút protocol
      - 15 mg IV bolus
      - 0.75 mg/kg trong 30 phút (max 50 mg)
      - 0.5 mg/kg trong 60 phút (max 35 mg)
    
    **Hoặc Tenecteplase:**
    - **Liều:** 30-50 mg IV (theo cân nặng)
    
    **Sau Fibrinolysis:**
    - **Transfer to PCI center** (nếu có thể)
    - **Rescue PCI** (nếu không đáp ứng)
    - **Routine PCI** (sau 3-24h)
    
    **Theo dõi:**
    - ECG mỗi 15-30 phút
    - Dấu hiệu tái tưới máu
    - Dấu hiệu xuất huyết
    """)


def render_transfer():
    """Transfer"""
    st.info("## ℹ️ TRANSFER TO PCI CENTER")
    
    st.markdown("""
    **Chỉ định:**
    - **Không có PCI tại bệnh viện**
    - **Có thể transfer trong 120 phút**
    
    **Trước Transfer:**
    - Aspirin 325 mg
    - P2Y12 inhibitor (loading dose)
    - Atorvastatin 80 mg
    - Heparin (nếu cần)
    - Ổn định bệnh nhân
    
    **Trong Transfer:**
    - Monitoring liên tục
    - Chuẩn bị thuốc cấp cứu
    - Liên lạc với PCI center
    
    **Mục tiêu:**
    - **First medical contact-to-device:** <120 phút
    - **Door-to-device:** <90 phút (tại PCI center)
    """)

