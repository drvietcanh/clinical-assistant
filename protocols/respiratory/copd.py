"""
COPD Exacerbation Protocol
GOLD 2023 Guidelines
"""

import streamlit as st


def render():
    """COPD Exacerbation Protocol"""
    st.subheader("🫁 COPD Exacerbation")
    st.caption("Cơn Cấp COPD - Xử Trí Theo GOLD 2023")
    
    st.info("ℹ️ **Guideline Update Note:** Vui lòng kiểm tra GOLD 2025 (nếu đã phát hành) tại https://goldcopd.org để cập nhật khuyến cáo mới nhất.")
    
    st.info("""
    **Cơn cấp COPD** là đợt xấu đi cấp tính các triệu chứng hô hấp cần điều chỉnh điều trị.
    """)
    
    # Assessment
    st.markdown("### 1️⃣ Đánh Giá Mức Độ Nặng")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Triệu Chứng")
        dyspnea_increased = st.checkbox("Khó thở tăng", key="copd_dyspnea")
        sputum_increased = st.checkbox("Đờm tăng", key="copd_sputum")
        sputum_purulent = st.checkbox("Đờm mủ", key="copd_purulent")
        
        st.markdown("#### Dấu Hiệu Nặng")
        severe_dyspnea = st.checkbox("Khó thở nặng (nói không thành câu)", key="copd_severe_dysp")
        rr_high = st.checkbox("Nhịp thở >25/phút", key="copd_rr")
        hr_high = st.checkbox("Nhịp tim >110/phút", key="copd_hr")
        cyanosis = st.checkbox("Tím tái", key="copd_cyanosis")
        confusion = st.checkbox("Lú lẫn", key="copd_confusion")
        
        st.markdown("#### Yếu Tố Nguy Cơ")
        copd_severe = st.checkbox("COPD nặng (FEV1 <50%)", key="copd_fev1")
        frequent_exac = st.checkbox("Cơn cấp thường xuyên (≥2/năm)", key="copd_freq")
        comorbid = st.checkbox("Bệnh kèm theo nặng (tim, thận...)", key="copd_comorbid")
    
    with col2:
        st.markdown("### 📊 Phân Loại")
        
        # Count severe signs
        severe_signs = sum([severe_dyspnea, rr_high, hr_high, cyanosis, confusion])
        risk_factors = sum([copd_severe, frequent_exac, comorbid])
        
        if severe_signs >= 2 or confusion or cyanosis:
            st.error("## CƠN CẤP NẶNG")
            st.error("🚨 Cần nhập viện")
            severity = "severe"
        elif severe_signs >= 1 or risk_factors >= 2:
            st.warning("## CƠN CẤP VỪA")
            st.warning("⚠️ Cân nhắc nhập viện")
            severity = "moderate"
        else:
            st.success("## CƠN CẤP NHẸ")
            st.success("✅ Có thể điều trị ngoại trú")
            severity = "mild"
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều Trị")
    
    # Treatment protocol
    tabs = st.tabs(["💨 Bronchodilators", "💊 Corticosteroids", "🦠 Antibiotics", "💉 Oxygen/NIV", "📋 Theo Dõi"])
    
    with tabs[0]:  # Bronchodilators
        st.markdown("#### Thuốc Giãn Phế Quản")
        
        st.success("""
        **SABA (Short-Acting Beta-Agonist):**
        - **Salbutamol** nebulizer 2.5-5mg hoặc MDI 4-8 puffs
        - Tần suất: Mỗi 4-6h (hoặc liên tục nếu nặng)
        
        **SAMA (Short-Acting Muscarinic Antagonist):**
        - **Ipratropium bromide** nebulizer 0.5mg hoặc MDI 4-8 puffs
        - Tần suất: Mỗi 4-6h
        - **Phối hợp SABA + SAMA hiệu quả hơn đơn trị**
        
        **Liều Khuyến Cáo:**
        """)
        
        if severity == "severe":
            st.error("""
            **Cơn cấp nặng:**
            - Salbutamol 5mg + Ipratropium 0.5mg nebulizer
            - Mỗi 4h hoặc liên tục nếu cần
            - Cân nhắc IV salbutamol nếu không đáp ứng
            """)
        elif severity == "moderate":
            st.warning("""
            **Cơn cấp vừa:**
            - Salbutamol 2.5-5mg + Ipratropium 0.5mg nebulizer
            - Mỗi 4-6h
            - Theo dõi đáp ứng sau 1h
            """)
        else:
            st.info("""
            **Cơn cấp nhẹ:**
            - Tăng liều SABA hiện tại lên (ví dụ: từ 2 puffs → 4 puffs)
            - Thêm SAMA nếu cần
            - Mỗi 4-6h trong vài ngày
            """)
    
    with tabs[1]:  # Corticosteroids
        st.markdown("#### Corticosteroids Toàn Thân")
        
        st.success("""
        **Khuyến Cáo (GOLD 2023):**
        - **Prednisolone/Prednisone 40mg PO x 5 ngày**
        - Hoặc **Methylprednisolone 32mg PO x 5 ngày**
        
        **Lợi ích:**
        - Giảm thời gian hồi phục
        - Cải thiện chức năng phổi
        - Giảm nguy cơ tái phát sớm
        - Giảm thời gian nằm viện
        
        **Lưu ý:**
        - **5 ngày tương đương 14 ngày** (REDUCE trial)
        - Không cần giảm liều dần nếu dùng ≤14 ngày
        - Cân nhắc IV nếu nôn hoặc cơn cấp rất nặng
        """)
        
        if severity == "severe":
            st.error("""
            **Cơn cấp nặng:**
            - **Methylprednisolone 125mg IV** load
            - Sau đó 40mg IV mỗi 6-8h
            - Chuyển PO khi ổn định
            - Tổng thời gian: 5-7 ngày
            """)
        else:
            st.info("""
            **Liều chuẩn:**
            - **Prednisolone 40mg PO mỗi ngày x 5 ngày**
            - Uống vào buổi sáng
            - Không cần giảm liều dần
            """)
        
        st.warning("""
        **Tác dụng phụ:**
        - Tăng đường huyết (theo dõi nếu ĐTĐ)
        - Tăng huyết áp
        - Lú lẫn (đặc biệt người cao tuổi)
        - Tăng nguy cơ nhiễm khuẩn
        """)
    
    with tabs[2]:  # Antibiotics
        st.markdown("#### Kháng Sinh")
        
        st.info("""
        **Chỉ định kháng sinh khi có:**
        1. **Đờm mủ** (dấu hiệu quan trọng nhất)
        2. Hoặc **Cơn cấp nặng** cần thở máy xâm nhập
        """)
        
        antibiotics_indicated = sputum_purulent or (severity == "severe" and st.checkbox("Cần thở máy xâm nhập", key="copd_vent"))
        
        if antibiotics_indicated:
            st.success("""
            **Lựa chọn kháng sinh (5-7 ngày):**
            
            **Lựa chọn 1 (Ưu tiên):**
            - **Amoxicillin-clavulanate** 875/125mg PO x 2 lần/ngày
            - Hoặc 2g IV x 3 lần/ngày nếu nặng
            
            **Lựa chọn 2:**
            - **Ceftriaxone** 1-2g IV x 1 lần/ngày
            - **Cefuroxime** 750mg-1.5g IV x 3 lần/ngày
            
            **Lựa chọn 3 (nếu dị ứng beta-lactam):**
            - **Levofloxacin** 500-750mg PO/IV x 1 lần/ngày
            - **Moxifloxacin** 400mg PO/IV x 1 lần/ngày
            
            **Nếu nguy cơ Pseudomonas:**
            (Cơn cấp thường xuyên, FEV1 <30%, dùng kháng sinh gần đây, hay nhập viện)
            - **Ciprofloxacin** 500-750mg PO x 2 lần/ngày
            - Hoặc Piperacillin-tazobactam IV
            """)
            
            st.warning("""
            **Yếu tố nguy cơ Pseudomonas:**
            - FEV1 <30%
            - Cơn cấp thường xuyên (≥4/năm)
            - Dùng kháng sinh trong 3 tháng qua
            - Phân lập Pseudomonas trước đây
            """)
        else:
            st.info("""
            **KHÔNG CẦN kháng sinh** nếu:
            - Đờm không mủ
            - Cơn cấp nhẹ-vừa
            - Không cần thở máy
            
            → Điều trị chỉ với bronchodilators + corticosteroids
            """)
    
    with tabs[3]:  # Oxygen/NIV
        st.markdown("#### Oxygen Therapy & NIV")
        
        st.success("""
        **Oxygen Therapy:**
        - **Mục tiêu:** SpO₂ 88-92% (KHÔNG phải 100%!)
        - **Lý do:** Tránh ức chế thở do CO₂ retention
        - **Cách cho:** Nasal cannula 1-2L/min hoặc Venturi mask 24-28%
        - **Theo dõi:** Khí máu sau 30-60 phút
        """)
        
        st.error("""
        **Chỉ định NIV (Non-Invasive Ventilation):**
        
        **Tiêu chuẩn:**
        - pH <7.35 với PaCO₂ >45 mmHg
        - Khó thở nặng với sử dụng cơ hô hấp phụ
        - Nhịp thở >25/phút
        
        **Thông số NIV:**
        - **IPAP:** 12-20 cmH₂O (bắt đầu 12, tăng dần)
        - **EPAP:** 4-8 cmH₂O (bắt đầu 4)
        - **FiO₂:** Điều chỉnh để SpO₂ 88-92%
        - **Backup rate:** 12-15 lần/phút
        
        **Đánh giá lại sau 1-2h:**
        - Nếu cải thiện → Tiếp tục NIV
        - Nếu xấu đi → Chuẩn bị đặt nội khí quản
        """)
        
        st.warning("""
        **Chỉ định thở máy xâm nhập:**
        - pH <7.25 kéo dài
        - Suy hô hấp tiến triển dù NIV
        - Ngừng thở / ngừng tim
        - Lú lẫn nặng / co giật
        - Huyết động không ổn định
        - Bài tiết đàm không hiệu quả
        """)
    
    with tabs[4]:  # Monitoring
        st.markdown("#### Theo Dõi & Tiêu Chuẩn Xuất Viện")
        
        st.success("""
        **Theo dõi tại bệnh viện:**
        - ✓ SpO₂ liên tục
        - ✓ Nhịp tim, nhịp thở, huyết áp mỗi 4h
        - ✓ Khí máu động mạch sau 30-60 phút oxygen
        - ✓ X-quang ngực (loại trừ viêm phổi, tràn khí màng phổi)
        - ✓ ĐTĐ, điện giải (nếu dùng corticosteroids)
        - ✓ ECG (loại trừ ACS, arrhythmia)
        
        **Thời gian nằm viện:**
        - Nhẹ-vừa: 3-5 ngày
        - Nặng: 7-10 ngày
        - Có NIV: Tùy theo đáp ứng
        """)
        
        st.info("""
        **Tiêu chuẩn xuất viện:**
        - ✅ Sử dụng SABA ≤ mỗi 4h
        - ✅ Tự đi lại được (nếu trước đây đi được)
        - ✅ Ăn uống, ngủ tốt
        - ✅ Ổn định lâm sàng ≥12-24h
        - ✅ SpO₂ ổn định với oxygen hoặc không oxygen
        - ✅ Bệnh nhân/gia đình hiểu cách dùng thuốc
        - ✅ Đã sắp xếp theo dõi ngoại trú (trong 4 tuần)
        """)
        
        st.warning("""
        **Sau xuất viện:**
        - 📅 Tái khám sau 4 tuần
        - 💊 Tiếp tục LABA + LAMA + ICS
        - 🚬 Tư vấn cai thuốc lá
        - 💉 Tiêm phòng cúm, phế cầu
        - 🏃 Phục hồi chức năng phổi
        - 📚 Giáo dục sử dụng inhaler đúng cách
        """)
    
    st.markdown("---")
    
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **GOLD 2023 - Global Initiative for Chronic Obstructive Lung Disease**
        
        **Định nghĩa cơn cấp COPD:**
        Đợt xấu đi cấp tính các triệu chứng hô hấp cần điều chỉnh điều trị thường quy.
        
        **Phân loại:**
        - **Nhẹ:** Chỉ cần tăng SABA
        - **Vừa:** Cần SABA + corticosteroids ± kháng sinh
        - **Nặng:** Cần nhập viện hoặc cấp cứu
        
        **Evidence-based treatment:**
        - Bronchodilators: ✓ Cải thiện triệu chứng
        - Corticosteroids 5 ngày: ✓ Non-inferior vs 14 ngày (REDUCE trial)
        - Antibiotics nếu đờm mủ: ✓ Giảm thất bại điều trị
        - NIV: ✓ Giảm tử vong & cần đặt nội khí quản
        
        **Guidelines:**
        - GOLD 2023: https://goldcopd.org
        - NICE 2018: COPD exacerbation
        - ERS/ATS 2017: COPD guidelines
        
        **References:**
        - Leuppi JD et al. JAMA. 2013;309(21):2223-2231 (REDUCE trial)
        - Walters JA et al. Cochrane Database. 2014 (Systemic corticosteroids)
        - Osadnik CR et al. Cochrane Database. 2017 (NIV)
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol hỗ trợ lâm sàng - cần cá thể hóa theo từng bệnh nhân")
