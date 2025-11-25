"""
DVT/PE Management Protocol
ACCP 2016, ESC 2019
Deep vein thrombosis and pulmonary embolism management
"""

import streamlit as st


def render():
    """DVT/PE Management Protocol"""
    st.subheader("🩸 Huyết Khối Tĩnh Mạch Sâu / Thuyên Tắc Phổi")
    st.caption("ACCP 2016, ESC 2019 - DVT/PE management")
    
    st.info("""
    **Huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE):**
    - Là biểu hiện của cùng một bệnh: Venous thromboembolism (VTE)
    - Tần suất: ~1-2/1000 người/năm
    - Nguy cơ: Tái phát, tử vong (PE)
    
    **Yếu tố nguy cơ (Virchow's Triad):**
    - Tổn thương nội mạc
    - Ứ trệ máu
    - Tăng đông máu
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Chẩn Đoán")
    
    condition_type = st.radio(
        "**Loại bệnh:**",
        [
            "DVT (Huyết khối tĩnh mạch sâu)",
            "PE (Thuyên tắc phổi)",
            "Đánh giá nguy cơ (Risk Assessment)"
        ],
        key="vte_type"
    )
    
    st.markdown("---")
    
    if "DVT" in condition_type:
        render_dvt_protocol()
    elif "PE" in condition_type:
        render_pe_protocol()
    else:
        render_risk_assessment()
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị Chống Đông")
    
    st.warning("""
    **DOACs (Ưu tiên cho DVT/PE):**
    
    **1. Apixaban:**
    - **Liều điều trị:** 10 mg PO bid x 7 ngày, sau đó 5 mg bid
    - **Thời gian:** 3-6 tháng (hoặc lâu hơn nếu cần)
    
    **2. Rivaroxaban:**
    - **Liều điều trị:** 15 mg PO bid x 21 ngày, sau đó 20 mg qd
    - **Thời gian:** 3-6 tháng
    
    **3. Edoxaban:**
    - **Liều điều trị:** 60 mg PO qd (sau 5-10 ngày LMWH)
    - **Thời gian:** 3-6 tháng
    
    **4. Dabigatran:**
    - **Liều điều trị:** 150 mg PO bid (sau 5-10 ngày LMWH)
    - **Thời gian:** 3-6 tháng
    
    **LMWH (Low Molecular Weight Heparin):**
    - **Enoxaparin:** 1 mg/kg SC bid hoặc 1.5 mg/kg SC qd
    - **Tinzaparin:** 175 units/kg SC qd
    - **Dùng khi:** Không thể dùng DOAC, suy thận nặng
    
    **Warfarin:**
    - **Liều:** 2-10 mg PO qd (điều chỉnh theo INR)
    - **Mục tiêu INR:** 2.0-3.0
    - **Dùng với:** LMWH trong 5-10 ngày đầu
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Điều Trị Cấp Cứu (PE)")
    
    st.error("""
    **Chỉ định điều trị cấp cứu:**
    - PE không ổn định huyết động (shock, hạ huyết áp)
    - PE nguy cơ cao (high-risk PE)
    
    **1. Thrombolysis:**
    - **Alteplase (tPA):** 100 mg IV trong 2 giờ
    - **Hoặc:** 0.6 mg/kg (max 50 mg) trong 15 phút
    - **Chống Chỉ Định:** Chảy máu nội sọ, phẫu thuật gần đây, chấn thương
    
    **2. Embolectomy:**
    - Phẫu thuật hoặc catheter-directed
    - Khi thrombolysis chống chỉ định/thất bại
    
    **3. Hỗ trợ:**
    - Oxygen, truyền dịch
    - Vasopressor nếu cần
    - ICU monitoring
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Loại Nguy Cơ PE")
    
    st.info("""
    **High-Risk (Nguy cơ cao):**
    - Shock, hạ huyết áp
    - Cần điều trị cấp cứu (thrombolysis/embolectomy)
    
    **Intermediate-High:**
    - PESI class III-V hoặc sPESI ≥1
    - Dấu hiệu RV dysfunction
    - Troponin/BNP tăng
    - Cân nhắc điều trị cấp cứu
    
    **Intermediate-Low:**
    - PESI class III-V hoặc sPESI ≥1
    - Không có dấu hiệu RV dysfunction
    - Điều trị chống đông
    
    **Low-Risk:**
    - PESI class I-II hoặc sPESI = 0
    - Có thể điều trị ngoại trú
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Đánh giá nguy cơ (Wells score, PERC, PESI)",
        "✅ D-dimer nếu nguy cơ thấp",
        "✅ CT scan hoặc siêu âm nếu nghi ngờ",
        "✅ Đánh giá ổn định huyết động (PE)",
        "✅ Bắt đầu chống đông ngay (nếu không chống chỉ định)",
        "✅ Thrombolysis nếu PE nguy cơ cao",
        "✅ Quyết định thời gian điều trị (3-6 tháng hoặc lâu hơn)",
        "✅ Điều trị nguyên nhân (nếu có)"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Có thai:**
        - LMWH an toàn (không qua nhau thai)
        - Tránh warfarin (teratogenic)
        - DOAC không khuyến nghị
        - Điều trị đến 6 tuần sau sinh
        
        **Suy thận:**
        - CrCl <30: Dùng LMWH hoặc warfarin
        - CrCl 30-50: Cẩn thận với DOAC
        - Theo dõi chức năng thận
        """)
    
    with col2:
        st.markdown("""
        **Ung thư:**
        - LMWH ưu tiên (3-6 tháng)
        - Hoặc DOAC (apixaban, rivaroxaban)
        - Điều trị lâu hơn (6-12 tháng hoặc lâu hơn)
        
        **Người cao tuổi:**
        - Cẩn thận với chống đông (nguy cơ té ngã)
        - Cân nhắc giảm liều DOAC
        - Theo dõi chức năng thận
        """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ACCP 2016 Guidelines**
       - Kearon C, et al. Chest. 2016
    
    2. **ESC 2019 Guidelines**
       - Konstantinides SV, et al. Eur Heart J. 2020
    
    3. **UpToDate:** Deep vein thrombosis, Pulmonary embolism
       - Last updated: 2024
    
    4. **Medscape:** DVT/PE Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_dvt_protocol():
    """DVT protocol"""
    st.success("## 🟢 Huyết Khối Tĩnh Mạch Sâu (DVT)")
    
    st.markdown("""
    **Triệu Chứng:**
    - Sưng, đau chân (thường một bên)
    - Đỏ, nóng da
    - Tăng chu vi chân
    
    **Chẩn Đoán:**
    - **Wells Score:** Đánh giá nguy cơ
    - **D-dimer:** Nếu nguy cơ thấp
    - **Siêu âm Doppler:** Xác nhận
    
    **Điều Trị:**
    1. **Chống đông ngay:**
       - DOAC (apixaban, rivaroxaban) - ưu tiên
       - Hoặc LMWH + warfarin
    
    2. **Nâng chân, băng ép:**
       - Giảm phù nề
       - Phòng ngừa hội chứng sau huyết khối
    
    3. **Thời gian điều trị:**
       - 3 tháng (nguyên nhân tạm thời)
       - 6-12 tháng hoặc lâu hơn (nguyên nhân vĩnh viễn)
    """)


def render_pe_protocol():
    """PE protocol"""
    st.error("## 🔴 Thuyên Tắc Phổi (PE)")
    
    st.markdown("""
    **Triệu Chứng:**
    - Khó thở đột ngột
    - Đau ngực (kiểu màng phổi)
    - Ho, ho ra máu
    - Ngất, hạ huyết áp
    
    **Chẩn Đoán:**
    - **Wells Score / PERC:** Đánh giá nguy cơ
    - **D-dimer:** Nếu nguy cơ thấp
    - **CTPA:** Xác nhận (tiêu chuẩn vàng)
    - **V/Q scan:** Nếu không thể CT
    
    **Điều Trị:**
    1. **Nếu ổn định:**
       - DOAC hoặc LMWH + warfarin
       - Oxygen, hỗ trợ hô hấp
    
    2. **Nếu không ổn định:**
       - Thrombolysis (alteplase)
       - Hoặc embolectomy
    
    3. **Theo Dõi:**
       - Huyết động, hô hấp
       - Dấu hiệu tái phát
    """)


def render_risk_assessment():
    """Risk assessment tools"""
    st.info("## 📊 Đánh Giá Nguy Cơ")
    
    st.markdown("""
    **Wells Score (DVT):**
    - Active cancer: 1 điểm
    - Paralysis/paresis: 1 điểm
    - Recent bed rest >3 days: 1 điểm
    - Localized tenderness: 1 điểm
    - Entire leg swollen: 1 điểm
    - Calf swelling >3 cm: 1 điểm
    - Pitting edema: 1 điểm
    - Collateral superficial veins: 1 điểm
    - Alternative diagnosis: -2 điểm
    
    **Wells Score (PE):**
    - Clinical signs of DVT: 3 điểm
    - PE most likely: 3 điểm
    - Heart rate >100: 1.5 điểm
    - Immobilization/surgery: 1.5 điểm
    - Previous PE/DVT: 1.5 điểm
    - Hemoptysis: 1 điểm
    - Malignancy: 1 điểm
    - Alternative diagnosis: -3 điểm
    
    **PERC Rule (PE):**
    - 8 tiêu chí (nếu tất cả âm tính → loại trừ PE)
    """)

