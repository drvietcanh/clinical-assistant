"""
Scrub Typhus (Sốt Mò) Protocol
WHO, CDC Guidelines
Orientia tsutsugamushi infection - Common in Vietnam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Scrub Typhus (Sốt Mò) Protocol"""
    st.subheader("🦟 Sốt Mò (Scrub Typhus)")
    st.caption("WHO, CDC Guidelines - Orientia tsutsugamushi Infection")
    
    st.error("""
    **⚠️ SỐT MÒ = BỆNH NGHIÊM TRỌNG - CẦN ĐIỀU TRỊ SỚM**
    - **Tác nhân:** Orientia tsutsugamushi (trước đây là Rickettsia tsutsugamushi)
    - **Vectơ:** Ấu trùng mò (chigger - Leptotrombidium)
    - **Phổ biến:** Vùng nông thôn, rừng núi, đồng cỏ ở Việt Nam
    - **Mortality:** 1-60% nếu không điều trị, <1% nếu điều trị sớm
    - **Thời gian ủ bệnh:** 6-21 ngày (trung bình 10-12 ngày)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng điển hình:**
        - Sốt cao đột ngột (39-40°C), kéo dài 1-2 tuần
        - **Eschar (vết loét đặc trưng):** Vết loét đen, có vảy, không đau, thường ở nách, bẹn, cổ, thắt lưng
        - Phát ban (rash): Maculopapular, xuất hiện ngày 4-7, thường ở thân mình, lan ra tay chân
        - Đau đầu dữ dội
        - Đau cơ, đau khớp
        - Sưng hạch lympho (lymphadenopathy)
        - Ho, khó thở (có thể có viêm phổi)
        
        **Xét nghiệm:**
        - **Huyết thanh học:** IgM/IgG ELISA, IFA (tăng 4 lần sau 2 tuần)
        - **PCR:** Phát hiện DNA Orientia tsutsugamushi
        - **Công thức máu:** Giảm bạch cầu, giảm tiểu cầu, tăng transaminase
        - **Sinh hóa:** Tăng AST, ALT, LDH, Bilirubin
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại Lâm Sàng")
    
    severity = st.radio(
        "**Mức độ bệnh:**",
        [
            "Nhẹ - Trung bình (Mild-Moderate)",
            "Nặng (Severe)",
            "Sốc (Shock)"
        ],
        key="scrub_typhus_severity"
    )
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    if "Nhẹ" in severity or "Trung bình" in severity:
        render_mild_moderate()
    elif "Nặng" in severity:
        render_severe()
    else:
        render_shock()
    
    st.markdown("---")
    
    # ========== SECTION 4: DOSING INFORMATION ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    with st.expander("📋 Xem liều thuốc", expanded=False):
        import pandas as pd
        dosing_data = {
            "Thuốc": [
                "Doxycycline",
                "Azithromycin",
                "Chloramphenicol",
                "Rifampin"
            ],
            "Liều Người Lớn": [
                "100mg PO BID x 7-15 ngày",
                "500mg PO QD x 3-5 ngày",
                "500mg PO QID x 7-14 ngày",
                "600-900mg PO QD x 7-10 ngày"
            ],
            "Liều Trẻ Em": [
                "2.2mg/kg PO BID x 7-15 ngày (max 200mg/ngày)",
                "10mg/kg PO QD x 3-5 ngày (max 500mg)",
                "25-50mg/kg/ngày PO chia 4 lần x 7-14 ngày",
                "10-20mg/kg/ngày PO chia 1-2 lần x 7-10 ngày"
            ],
            "Ghi chú": [
                "Lựa chọn 1, uống với thức ăn",
                "An toàn cho trẻ em, phụ nữ có thai",
                "Dùng khi kháng doxycycline",
                "Dùng khi kháng doxycycline"
            ]
        }
        
        st.dataframe(pd.DataFrame(dosing_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hàng ngày:**
        - Dấu hiệu sống (nhiệt độ, mạch, huyết áp, SpO2)
        - Tình trạng tổng quát
        - Triệu chứng (sốt, đau đầu, phát ban)
        - Dấu hiệu eschar
        
        **Xét nghiệm:**
        - CBC (bạch cầu, tiểu cầu)
        - Chức năng gan (AST, ALT)
        - Chức năng thận (creatinine, BUN)
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu cải thiện:**
        - Hết sốt trong 24-48h sau khi bắt đầu kháng sinh
        - Giảm đau đầu, đau cơ
        - Phát ban mờ dần
        
        **Dấu hiệu cảnh báo:**
        - Sốt kéo dài >48h sau kháng sinh
        - Tình trạng xấu đi
        - Dấu hiệu sốc, suy đa tạng
        - Cần xem xét thay đổi kháng sinh
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến Chứng")
    
    st.warning("""
    **Biến chứng có thể gặp:**
    
    **1. Biến chứng tim mạch:**
    - Viêm cơ tim (myocarditis)
    - Rối loạn nhịp tim
    - Sốc tim
    
    **2. Biến chứng hô hấp:**
    - Viêm phổi (pneumonitis)
    - ARDS
    - Suy hô hấp
    
    **3. Biến chứng thần kinh:**
    - Viêm màng não (meningitis)
    - Viêm não (encephalitis)
    - Co giật
    
    **4. Biến chứng gan:**
    - Viêm gan (hepatitis)
    - Suy gan
    
    **5. Biến chứng thận:**
    - Suy thận cấp (AKI)
    - Hội chứng thận hư
    
    **6. Biến chứng khác:**
    - DIC (rối loạn đông máu)
    - Suy đa tạng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Azithromycin là lựa chọn 1 (an toàn)
        - Doxycycline có thể dùng nếu cần (nguy cơ ố răng thấp nếu dùng ngắn ngày)
        - Theo dõi sát tình trạng sốt
        
        **Phụ nữ có thai:**
        - **Azithromycin** là lựa chọn 1 (an toàn)
        - Tránh doxycycline (category D)
        - Tránh chloramphenicol
        """)
    
    with col2:
        st.markdown("""
        **Người cao tuổi:**
        - Tăng nguy cơ biến chứng
        - Theo dõi chức năng thận
        - Điều chỉnh liều nếu suy thận
        
        **Suy thận:**
        - Điều chỉnh liều doxycycline
        - Azithromycin không cần điều chỉnh
        - Theo dõi chức năng thận
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    **Phòng ngừa sốt mò:**
    
    **1. Tránh tiếp xúc với mò:**
    - Mặc quần áo dài, bít tất khi vào rừng, đồng cỏ
    - Đi giày ủng cao
    - Tránh ngồi, nằm trực tiếp trên cỏ, đất
    
    **2. Sử dụng thuốc chống côn trùng:**
    - DEET (diethyltoluamide) 20-30%
    - Permethrin (xịt lên quần áo)
    - Áp dụng lại sau 4-6 giờ
    
    **3. Vệ sinh:**
    - Tắm rửa sau khi về từ rừng, đồng cỏ
    - Giặt quần áo bằng nước nóng
    - Kiểm tra cơ thể tìm mò
    
    **4. Phòng ngừa bằng kháng sinh (nếu cần):**
    - Doxycycline 200mg PO x 1 lần/tuần (chỉ khi ở vùng dịch tễ cao)
    - Bắt đầu 1-2 ngày trước khi vào vùng dịch tễ
    - Tiếp tục trong thời gian ở vùng dịch tễ và 2 tuần sau khi rời
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: DIFFERENTIAL DIAGNOSIS ==========
    st.markdown("### 🔍 Chẩn đoán Phân Biệt")
    
    st.markdown("""
    **Các bệnh cần phân biệt:**
    - **Sốt xuất huyết Dengue:** Sốt, phát ban, giảm tiểu cầu, không có eschar
    - **Sốt rét:** Sốt có chu kỳ, không có eschar, có thể có thiếu máu
    - **Leptospirosis:** Sốt, đau cơ, vàng da, không có eschar
    - **Typhoid:** Sốt kéo dài, đau bụng, không có eschar
    - **Rickettsia khác:** Sốt phát ban do rickettsia khác (cần xét nghiệm huyết thanh)
    - **Nhiễm virus:** Sốt, phát ban, không có eschar
    """)
    
    st.markdown("---")
    
    # ========== SECTION 10: REFERENCES ==========
    references = get_references("Scrub Typhus")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể, kháng sinh đồ địa phương, và guidelines mới nhất.")


def render_mild_moderate():
    """Mild to Moderate Scrub Typhus Protocol"""
    
    st.success("## ✅ SỐT MÒ NHẸ - TRUNG BÌNH")
    
    st.markdown("### 💊 Điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Lựa chọn 1 (Ưu tiên):**
        - **Doxycycline** 100mg PO BID x 7-15 ngày
        - Uống với thức ăn để giảm kích ứng dạ dày
        - Hiệu quả: 95-100%
        - Hết sốt trong 24-48h
        
        **Lựa chọn 2 (Phụ nữ có thai, trẻ em):**
        - **Azithromycin** 500mg PO QD x 3-5 ngày
        - An toàn cho phụ nữ có thai và trẻ em
        - Hiệu quả: 90-95%
        """)
    
    with col2:
        st.warning("""
        **Lựa chọn 3 (Kháng doxycycline):**
        - **Chloramphenicol** 500mg PO QID x 7-14 ngày
        - Hoặc **Rifampin** 600-900mg PO QD x 7-10 ngày
        - Theo dõi tác dụng phụ
        
        **Điều trị hỗ trợ:**
        - Hạ sốt: Paracetamol 500-1000mg PO q4-6h
        - Bù dịch nếu cần
        - Nghỉ ngơi
        """)
    
    st.markdown("---")
    
    st.markdown("""
    **Thời gian điều trị:**
    - Tối thiểu 7 ngày
    - Kéo dài đến 15 ngày nếu triệu chứng kéo dài
    - Điều trị ít nhất 3 ngày sau khi hết sốt
    
    **Đánh giá đáp ứng:**
    - Hết sốt trong 24-48h sau khi bắt đầu kháng sinh
    - Giảm đau đầu, đau cơ
    - Phát ban mờ dần
    """)


def render_severe():
    """Severe Scrub Typhus Protocol"""
    
    st.error("## 🚨 SỐT MÒ NẶNG")
    
    st.markdown("### 💊 Điều trị")
    
    st.error("""
    **Điều trị Khẩn Cấp:**
    
    **Lựa chọn 1 (Ưu tiên):**
    - **Doxycycline** 100mg IV q12h x 7-15 ngày
    - Chuyển sang PO khi có thể
    - Hoặc **Doxycycline** 200mg IV x 1 liều, sau đó 100mg IV q12h
    
    **Lựa chọn 2:**
    - **Azithromycin** 500mg IV QD x 3-5 ngày
    - Chuyển sang PO khi có thể
    
    **Lựa chọn 3 (Kháng doxycycline):**
    - **Chloramphenicol** 500mg IV q6h x 7-14 ngày
    - Hoặc **Rifampin** 600mg IV q12h x 7-10 ngày
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **Điều trị Hỗ trợ:**
    
    **1. Hạ sốt:**
    - Paracetamol 500-1000mg PO/IV q4-6h
    - Tránh NSAID (nguy cơ xuất huyết)
    
    **2. Bù dịch:**
    - Nước muối sinh lý 0.9% hoặc Ringer lactate
    - Theo dõi cân bằng dịch
    - Tránh quá tải dịch
    
    **3. Theo dõi:**
    - Dấu hiệu sống mỗi 2-4 giờ
    - Chức năng các cơ quan
    - Xét nghiệm: CBC, chức năng gan, thận
    
    **4. Điều trị biến chứng:**
    - Viêm phổi: Oxy, thở máy nếu cần
    - Suy thận: Điều chỉnh dịch, lọc máu nếu cần
    - Rối loạn đông máu: Truyền tiểu cầu, huyết tương nếu cần
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **Chỉ định nhập ICU:**
    - Sốc (shock)
    - Suy hô hấp
    - Suy đa tạng
    - Rối loạn ý thức
    - Co giật
    """)


def render_shock():
    """Scrub Typhus with Shock Protocol"""
    
    st.error("## 🚨🚨 SỐT MÒ CÓ SỐC - ICU")
    
    st.error("""
    **⚠️ CẤP CỨU - CẦN ĐIỀU TRỊ NGAY LẬP TỨC**
    """)
    
    st.markdown("### 💊 Điều trị Kháng sinh")
    
    st.error("""
    **Kháng sinh IV ngay lập tức:**
    
    **Lựa chọn 1:**
    - **Doxycycline** 200mg IV x 1 liều, sau đó 100mg IV q12h
    - Hoặc **Doxycycline** 100mg IV q12h
    
    **Lựa chọn 2:**
    - **Azithromycin** 500mg IV QD
    
    **Lựa chọn 3:**
    - **Chloramphenicol** 500mg IV q6h
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Sốc")
    
    st.error("""
    **1. Bù dịch:**
    - Nước muối sinh lý 0.9% hoặc Ringer lactate
    - Bolus 500-1000ml trong 30 phút
    - Lặp lại nếu cần
    - Theo dõi áp lực tĩnh mạch trung tâm (CVP)
    - Tránh quá tải dịch
    
    **2. Vận mạch (nếu cần sau bù dịch):**
    - Norepinephrine 0.1-2 mcg/kg/min
    - Hoặc Dopamine 5-20 mcg/kg/min
    - Theo dõi huyết áp, mạch
    
    **3. Theo dõi:**
    - Dấu hiệu sống mỗi 15-30 phút
    - CVP, áp lực động mạch phổi (nếu có)
    - Lượng nước tiểu (đặt sonde tiểu)
    - Lactate máu
    """)
    
    st.markdown("---")
    
    st.markdown("### 🏥 Điều trị Hỗ trợ")
    
    st.error("""
    **1. Hô hấp:**
    - Oxy qua mask hoặc nasal cannula
    - Thở máy nếu suy hô hấp
    - Theo dõi SpO2, khí máu
    
    **2. Tim mạch:**
    - Monitor ECG liên tục
    - Điều trị rối loạn nhịp
    - Theo dõi chức năng tim
    
    **3. Thận:**
    - Theo dõi lượng nước tiểu
    - Điều chỉnh dịch
    - Lọc máu nếu suy thận cấp
    
    **4. Gan:**
    - Theo dõi chức năng gan
    - Điều chỉnh thuốc nếu suy gan
    
    **5. Đông máu:**
    - Truyền tiểu cầu nếu giảm tiểu cầu nặng
    - Truyền huyết tương nếu DIC
    - Theo dõi PT, PTT, fibrinogen
    
    **6. Hạ sốt:**
    - Paracetamol 500-1000mg IV q4-6h
    - Làm mát cơ thể nếu sốt cao
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiêu chuẩn Cải Thiện")
    
    st.info("""
    **Dấu hiệu cải thiện:**
    - Huyết áp ổn định, không cần vận mạch
    - Hết sốt trong 24-48h
    - Lượng nước tiểu >0.5ml/kg/giờ
    - Lactate giảm
    - Tình trạng tổng quát cải thiện
    
    **Chuyển từ ICU:**
    - Ổn định 24-48h
    - Không cần vận mạch
    - Không cần thở máy
    - Chức năng các cơ quan ổn định
    """)

