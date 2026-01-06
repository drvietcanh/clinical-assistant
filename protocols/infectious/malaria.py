"""
Malaria (Sốt Rét) Protocol
WHO Guidelines 2023
Plasmodium falciparum, P. vivax, P. malariae, P. ovale
Very common in Vietnam, especially in forest/mountain areas
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Malaria (Sốt Rét) Protocol"""
    st.subheader("🦟 Sốt Rét (Malaria)")
    st.caption("WHO Guidelines 2023 - Plasmodium Infection - Phổ biến ở Việt Nam, đặc biệt vùng rừng núi")
    
    st.error("""
    **⚠️ SỐT RÉT = BỆNH NGHIÊM TRỌNG - CẦN ĐIỀU TRỊ SỚM**
    - **Tác nhân:** Plasmodium falciparum, P. vivax, P. malariae, P. ovale
    - **Vector:** Muỗi Anopheles
    - **Phổ biến:** Vùng rừng núi, biên giới Việt Nam
    - **Mortality:** 10-20% (P. falciparum nặng) nếu không điều trị, <1% nếu điều trị sớm
    - **Thời gian ủ bệnh:** 7-30 ngày (P. falciparum: 7-14 ngày, P. vivax: 8-17 ngày)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLINICAL CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại Lâm Sàng")
    
    classification = st.radio(
        "**Phân loại sốt rét:**",
        [
            "Sốt rét đơn giản (Uncomplicated Malaria)",
            "Sốt rét nặng (Severe Malaria)",
            "Sốt rét tái phát (Relapsing Malaria - P. vivax/ovale)"
        ],
        key="malaria_classification"
    )
    
    st.markdown("---")
    
    # ========== SECTION 2: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng điển hình:**
        - Sốt có chu kỳ (febrile paroxysm): Rét run → Sốt cao → Vã mồ hôi
        - Chu kỳ 48 giờ (P. falciparum, P. vivax, P. ovale) hoặc 72 giờ (P. malariae)
        - Đau đầu, đau cơ, mệt mỏi
        - Buồn nôn, nôn
        - Thiếu máu (anemia)
        - Lách to (splenomegaly)
        
        **Xét nghiệm:**
        - **Kính hiển vi:** Phết máu ngoại biên (thick/thin smear) - tiêu chuẩn vàng
        - **Test nhanh:** RDT (Rapid Diagnostic Test) - phát hiện kháng nguyên
        - **PCR:** Phát hiện DNA Plasmodium (nếu có)
        - **Công thức máu:** Giảm hồng cầu, tiểu cầu, tăng bạch cầu
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: SPECIES IDENTIFICATION ==========
    st.markdown("### 🦠 Xác Định Loài Plasmodium")
    
    species = st.radio(
        "**Loài Plasmodium (nếu đã xác định):**",
        [
            "Chưa xác định / Tất cả",
            "P. falciparum",
            "P. vivax",
            "P. malariae",
            "P. ovale"
        ],
        key="malaria_species"
    )
    
    st.markdown("---")
    
    # Route to appropriate protocol
    if "Nặng" in classification or "Severe" in classification:
        render_severe_malaria()
    elif "Tái phát" in classification or "Relapsing" in classification:
        render_relapsing_malaria()
    else:
        render_uncomplicated_malaria(species)
    
    st.markdown("---")
    
    # ========== SECTION 4: DOSING INFORMATION ==========
    st.markdown("### 💉 Liều Thuốc Chi tiết")
    
    with st.expander("📋 Xem liều thuốc", expanded=False):
        import pandas as pd
        dosing_data = {
            "Thuốc": [
                "Artemether-Lumefantrine (ACT)",
                "Artesunate + Amodiaquine (ACT)",
                "Artesunate + Mefloquine (ACT)",
                "Dihydroartemisinin-Piperaquine (ACT)",
                "Artesunate IV",
                "Quinine IV",
                "Primaquine (radical cure)"
            ],
            "Liều Người Lớn": [
                "4 viên PO (80/480mg) ngày 1, sau đó 4 viên sau 8h, sau đó 4 viên BID x 2 ngày",
                "Artesunate 100mg + Amodiaquine 270mg PO QD x 3 ngày",
                "Artesunate 100mg + Mefloquine 250mg PO QD x 3 ngày",
                "DHA 40mg + Piperaquine 320mg PO QD x 3 ngày",
                "2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12h và 24h, sau đó QD",
                "20mg/kg IV loading, sau đó 10mg/kg q8h",
                "15mg base PO QD x 14 ngày (P. vivax/ovale)"
            ],
            "Liều Trẻ Em": [
                "Theo cân nặng: 5-15kg, 15-25kg, 25-35kg, >35kg",
                "Theo cân nặng",
                "Theo cân nặng",
                "Theo cân nặng",
                "2.4mg/kg IV ngay, sau đó 1.2mg/kg q12h",
                "20mg/kg IV loading, sau đó 10mg/kg q8h",
                "0.25-0.5mg/kg base PO QD x 14 ngày"
            ],
            "Ghi chú": [
                "ACT lựa chọn 1, uống với thức ăn có chất béo",
                "ACT, kiểm tra G6PD trước dùng primaquine",
                "ACT, có thể gây rối loạn tâm thần",
                "ACT, hiệu quả cao",
                "Dùng cho sốt rét nặng",
                "Dùng khi không có artesunate",
                "Diệt thể ngủ (hypnozoite) P. vivax/ovale"
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
        - Tình trạng tổng quát, ý thức
        - Triệu chứng (sốt, đau đầu)
        - Lượng nước tiểu
        
        **Xét nghiệm:**
        - Phết máu (parasitemia) mỗi 6-12h (sốt rét nặng)
        - CBC (hồng cầu, tiểu cầu)
        - Chức năng gan, thận
        - Đường huyết (glucose)
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu cải thiện:**
        - Hết sốt trong 24-48h
        - Giảm parasitemia
        - Tình trạng tổng quát cải thiện
        - Hết triệu chứng
        
        **Dấu hiệu cảnh báo:**
        - Sốt kéo dài >48h sau điều trị
        - Parasitemia tăng
        - Tình trạng xấu đi
        - Dấu hiệu sốt rét nặng
        - Cần xem xét thay đổi phác đồ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến Chứng Sốt Rét Nặng")
    
    st.warning("""
    **Tiêu chuẩn sốt rét nặng (WHO):**
    
    **1. Rối loạn ý thức:**
    - Hôn mê (cerebral malaria)
    - Lú lẫn, co giật
    
    **2. Thiếu máu nặng:**
    - Hb <5g/dL hoặc Hct <15%
    - Parasitemia >10%
    
    **3. Suy thận cấp:**
    - Creatinine >265 μmol/L
    - Thiểu niệu, vô niệu
    
    **4. Suy hô hấp:**
    - ARDS
    - Acidosis hô hấp
    
    **5. Hạ đường huyết:**
    - Glucose <2.2 mmol/L
    
    **6. Sốc:**
    - Huyết áp tâm thu <70 mmHg
    - Lactate >5 mmol/L
    
    **7. Rối loạn đông máu:**
    - DIC
    - Chảy máu tự phát
    
    **8. Toan chuyển hóa:**
    - pH <7.35
    - Bicarbonate <15 mmol/L
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Tăng nguy cơ sốt rét nặng
        - Liều theo cân nặng chính xác
        - Theo dõi sát đường huyết
        - ACT an toàn cho trẻ em
        
        **Phụ nữ có thai:**
        - **Tam cá nguyệt 1:** Quinine + Clindamycin
        - **Tam cá nguyệt 2-3:** ACT (tránh artesunate + mefloquine)
        - Tránh primaquine (chống chỉ định)
        - Theo dõi sát
        """)
    
    with col2:
        st.markdown("""
        **Người cao tuổi:**
        - Tăng nguy cơ biến chứng
        - Theo dõi chức năng thận
        - Điều chỉnh liều nếu suy thận
        
        **Suy thận:**
        - Điều chỉnh liều quinine
        - ACT không cần điều chỉnh
        - Theo dõi chức năng thận
        - Có thể cần lọc máu
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    **Phòng ngừa sốt rét:**
    
    **1. Tránh muỗi đốt:**
    - Màn tẩm hóa chất (ITN - Insecticide Treated Net)
    - Mặc quần áo dài, sáng màu
    - Sử dụng thuốc chống côn trùng (DEET 20-30%)
    - Tránh ra ngoài vào chiều tối/đêm
    
    **2. Phòng ngừa bằng thuốc (Chemoprophylaxis):**
    - **Doxycycline** 100mg PO QD (bắt đầu 1-2 ngày trước, tiếp tục 4 tuần sau)
    - **Atovaquone-Proguanil** 250/100mg PO QD (bắt đầu 1-2 ngày trước, tiếp tục 7 ngày sau)
    - **Mefloquine** 250mg PO x 1 lần/tuần (bắt đầu 2 tuần trước, tiếp tục 4 tuần sau)
    
    **3. Điều trị dự phòng (Standby treatment):**
    - Mang theo ACT khi đi vùng dịch tễ
    - Dùng ngay khi có triệu chứng sốt rét
    - Đến cơ sở y tế sau đó
    
    **4. Vệ sinh môi trường:**
    - Loại bỏ nơi muỗi đẻ trứng
    - Phun hóa chất diệt muỗi
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: DRUG RESISTANCE ==========
    st.markdown("### 💊 Kháng Thuốc")
    
    st.warning("""
    **Tình hình kháng thuốc:**
    
    **1. Kháng Chloroquine:**
    - P. falciparum: Kháng phổ biến ở Việt Nam
    - P. vivax: Một số vùng kháng
    - **Không dùng chloroquine** cho P. falciparum
    
    **2. Kháng ACT:**
    - Một số vùng Đông Nam Á có kháng artemisinin
    - Cần theo dõi đáp ứng điều trị
    - Có thể cần phác đồ thay thế
    
    **3. Xử trí kháng thuốc:**
    - Thay đổi phác đồ ACT
    - Dùng quinine + doxycycline/tetracycline
    - Theo dõi sát đáp ứng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 10: REFERENCES ==========
    references = get_references("Malaria")
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
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể, kháng sinh đồ địa phương, tình hình kháng thuốc, và guidelines mới nhất.")


def render_uncomplicated_malaria(species):
    """Uncomplicated Malaria Protocol"""
    
    st.success("## ✅ SỐT RÉT ĐƠN GIẢN (Uncomplicated Malaria)")
    
    st.markdown("### 💊 Điều trị")
    
    if "falciparum" in species or "Chưa" in species or "Tất cả" in species:
        st.markdown("#### **P. falciparum hoặc chưa xác định:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **Lựa chọn 1 (Ưu tiên - ACT):**
            - **Artemether-Lumefantrine** (Coartem)
            - Liều: 4 viên (80/480mg) PO ngày 1, sau đó 4 viên sau 8h, sau đó 4 viên BID x 2 ngày
            - Tổng: 6 liều trong 3 ngày
            - Uống với thức ăn có chất béo
            - Hiệu quả: 95-98%
            
            **Lựa chọn 2 (ACT):**
            - **Artesunate + Amodiaquine**
            - Artesunate 100mg + Amodiaquine 270mg PO QD x 3 ngày
            - Kiểm tra G6PD trước dùng primaquine (nếu cần)
            """)
        
        with col2:
            st.warning("""
            **Lựa chọn 3 (ACT):**
            - **Dihydroartemisinin-Piperaquine**
            - DHA 40mg + Piperaquine 320mg PO QD x 3 ngày
            - Hiệu quả cao
            
            **Lựa chọn 4 (khi không có ACT):**
            - **Quinine** 600mg PO TID x 7 ngày
            + **Doxycycline** 100mg PO BID x 7 ngày
            - Hoặc **Clindamycin** 300mg PO QID x 7 ngày
            """)
    
    if "vivax" in species or "ovale" in species or "Chưa" in species or "Tất cả" in species:
        st.markdown("#### **P. vivax hoặc P. ovale:**")
        
        st.info("""
        **Điều trị giai đoạn cấp:**
        - **ACT** (như P. falciparum) x 3 ngày
        
        **Điều trị radical cure (diệt thể ngủ):**
        - **Primaquine** 15mg base PO QD x 14 ngày (người lớn)
        - **QUAN TRỌNG:** Kiểm tra G6PD trước khi dùng primaquine
        - Nếu thiếu G6PD: Dùng primaquine 45mg base PO x 1 lần/tuần x 8 tuần
        - Hoặc không dùng primaquine nếu thiếu G6PD nặng
        """)
    
    if "malariae" in species:
        st.markdown("#### **P. malariae:**")
        
        st.info("""
        **Điều trị:**
        - **ACT** (như P. falciparum) x 3 ngày
        - Hoặc **Chloroquine** 600mg base PO ngày 1, sau đó 300mg base PO sau 6-8h, sau đó 300mg base PO QD x 2 ngày
        - Không cần primaquine (không có thể ngủ)
        """)
    
    st.markdown("---")
    
    st.markdown("""
    **Thời gian điều trị:**
    - ACT: 3 ngày
    - Quinine + Doxycycline: 7 ngày
    - Primaquine (radical cure): 14 ngày
    
    **Đánh giá đáp ứng:**
    - Hết sốt trong 24-48h
    - Giảm parasitemia
    - Cải thiện triệu chứng
    """)


def render_severe_malaria():
    """Severe Malaria Protocol"""
    
    st.error("## 🚨 SỐT RÉT NẶNG (Severe Malaria) - ICU")
    
    st.error("""
    **⚠️ CẤP CỨU - CẦN ĐIỀU TRỊ NGAY LẬP TỨC**
    """)
    
    st.markdown("### 💊 Điều trị Kháng sinh")
    
    st.error("""
    **Kháng sinh IV ngay lập tức:**
    
    **Lựa chọn 1 (Ưu tiên):**
    - **Artesunate** 2.4mg/kg IV ngay
    - Sau đó 1.2mg/kg IV sau 12h và 24h
    - Sau đó 1.2mg/kg IV QD cho đến khi có thể uống
    - Chuyển sang ACT PO khi có thể (hoàn thành 3 ngày ACT)
    
    **Lựa chọn 2 (khi không có artesunate):**
    - **Quinine** 20mg/kg IV loading (trong 4h)
    - Sau đó 10mg/kg IV q8h
    - Chuyển sang PO khi có thể (600mg PO TID x 7 ngày)
    + **Doxycycline** 100mg IV/PO BID x 7 ngày
    """)
    
    st.markdown("---")
    
    st.markdown("### 🏥 Điều trị Hỗ trợ")
    
    st.error("""
    **1. Hạ sốt:**
    - Paracetamol 500-1000mg IV/PO q4-6h
    - Làm mát cơ thể nếu sốt cao
    
    **2. Hạ đường huyết:**
    - Theo dõi glucose mỗi 4-6h
    - Truyền glucose 10% nếu glucose <4 mmol/L
    - Đặc biệt quan trọng ở trẻ em và phụ nữ có thai
    
    **3. Thiếu máu:**
    - Truyền máu nếu Hb <5g/dL hoặc Hct <15%
    - Hoặc nếu có dấu hiệu thiếu máu nặng
    
    **4. Suy thận:**
    - Điều chỉnh dịch
    - Lọc máu nếu cần (AKI)
    
    **5. Co giật:**
    - Benzodiazepine (Diazepam, Midazolam)
    - Phenobarbital nếu cần
    
    **6. Sốc:**
    - Bù dịch: Nước muối sinh lý 0.9% hoặc Ringer lactate
    - Vận mạch nếu cần (Norepinephrine)
    
    **7. ARDS:**
    - Oxy, thở máy nếu cần
    - PEEP thấp
    
    **8. Toan chuyển hóa:**
    - Bicarbonate nếu pH <7.1
    - Điều chỉnh dịch
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiêu chuẩn Cải Thiện")
    
    st.info("""
    **Dấu hiệu cải thiện:**
    - Tỉnh táo, ý thức cải thiện
    - Hết sốt
    - Parasitemia giảm
    - Huyết động ổn định
    - Chức năng các cơ quan cải thiện
    
    **Chuyển từ ICU:**
    - Ổn định 24-48h
    - Có thể uống được
    - Chuyển sang ACT PO
    - Chức năng các cơ quan ổn định
    """)


def render_relapsing_malaria():
    """Relapsing Malaria (P. vivax/ovale) Protocol"""
    
    st.warning("## ⚠️ SỐT RÉT TÁI PHÁT (Relapsing Malaria - P. vivax/ovale)")
    
    st.markdown("### 💊 Điều trị")
    
    st.info("""
    **Điều trị giai đoạn cấp:**
    - **ACT** (như sốt rét đơn giản) x 3 ngày
    
    **Điều trị radical cure (diệt thể ngủ - hypnozoite):**
    - **Primaquine** 15mg base PO QD x 14 ngày (người lớn)
    - Trẻ em: 0.25-0.5mg/kg base PO QD x 14 ngày
    
    **QUAN TRỌNG:**
    - **PHẢI kiểm tra G6PD trước khi dùng primaquine**
    - Nếu thiếu G6PD nhẹ-trung bình: Primaquine 45mg base PO x 1 lần/tuần x 8 tuần
    - Nếu thiếu G6PD nặng: Không dùng primaquine, điều trị lại khi tái phát
    
    **Chống chỉ định primaquine:**
    - Thiếu G6PD nặng
    - Phụ nữ có thai
    - Trẻ em <6 tháng
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **Theo dõi:**
    - Đánh giá đáp ứng điều trị giai đoạn cấp
    - Theo dõi tác dụng phụ primaquine (thiếu máu tan máu)
    - Kiểm tra G6PD nếu có triệu chứng thiếu máu
    
    **Tái phát:**
    - Điều trị lại như sốt rét đơn giản
    - Cân nhắc lại primaquine (nếu chưa dùng hoặc dùng không đủ)
    """)

