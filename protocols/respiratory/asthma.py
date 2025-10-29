"""
Acute Asthma Protocol
GINA 2023 Guidelines
"""

import streamlit as st


def render():
    """Acute Asthma Protocol"""
    st.subheader("🫁 Cơn Hen Cấp")
    st.caption("Xử Trí Cơn Hen Theo GINA 2023")
    
    st.info("ℹ️ **Guideline Update Note:** Vui lòng kiểm tra GINA 2025 (nếu đã phát hành) tại https://ginasthma.org để cập nhật khuyến cáo mới nhất.")
    
    st.info("""
    **Cơn hen cấp** là đợt xấu đi cấp tính hoặc tiến triển của triệu chứng hen.
    """)
    
    # Assessment
    st.markdown("### 1️⃣ Đánh Giá Mức Độ Nặng")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Triệu Chứng & Dấu Hiệu")
        
        # Symptoms
        difficulty_speaking = st.checkbox("Khó nói thành câu / từng cụm từ", key="asthma_speech")
        agitation = st.checkbox("Kích động hoặc lú lẫn", key="asthma_agitation")
        drowsy = st.checkbox("Buồn ngủ hoặc lơ mơ", key="asthma_drowsy")
        
        # Vital signs
        rr = st.number_input("Nhịp thở (/phút)", min_value=0, max_value=60, value=20, step=1, key="asthma_rr")
        hr = st.number_input("Nhịp tim (/phút)", min_value=0, max_value=250, value=80, step=1, key="asthma_hr")
        spo2 = st.number_input("SpO₂ (%)", min_value=50, max_value=100, value=95, step=1, key="asthma_spo2")
        
        # PEFR
        pefr_measured = st.checkbox("Đo được PEFR/FEV1", key="asthma_pefr_check")
        if pefr_measured:
            pefr_percent = st.slider("PEFR/FEV1 (% dự đoán)", 10, 100, 60, 5, key="asthma_pefr")
        else:
            pefr_percent = None
        
        # Accessory muscles
        accessory_muscles = st.checkbox("Sử dụng cơ hô hấp phụ", key="asthma_muscles")
        
        # Silent chest
        silent_chest = st.checkbox("Silent chest (không nghe thấy thở)", key="asthma_silent")
    
    with col2:
        st.markdown("### 📊 Mức Độ Nặng")
        
        # Calculate severity
        severe_signs = 0
        life_threatening = False
        
        # Life-threatening features
        if drowsy or silent_chest or (spo2 < 92):
            life_threatening = True
        
        # Severe features
        if difficulty_speaking:
            severe_signs += 1
        if rr >= 25:
            severe_signs += 1
        if hr >= 110:
            severe_signs += 1
        if pefr_percent and pefr_percent <= 50:
            severe_signs += 2
        if spo2 < 95:
            severe_signs += 1
        
        if life_threatening:
            st.error("## CƠN HEN")
            st.error("🚨 ĐE DỌA TÍNH MẠNG")
            severity = "life-threatening"
        elif severe_signs >= 3 or (pefr_percent and pefr_percent <= 50):
            st.error("## CƠN HEN NẶNG")
            st.error("❗ Cần xử trí tích cực")
            severity = "severe"
        elif severe_signs >= 1:
            st.warning("## CƠN HEN VỪA")
            st.warning("⚠️ Theo dõi sát")
            severity = "moderate"
        else:
            st.success("## CƠN HEN NHẸ")
            st.success("✅ Điều trị thường quy")
            severity = "mild"
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều Trị")
    
    tabs = st.tabs(["💨 Bronchodilators", "💊 Corticosteroids", "💉 Add-on Therapy", "🏥 ICU Criteria", "📋 Theo Dõi"])
    
    with tabs[0]:  # Bronchodilators
        st.markdown("#### Thuốc Giãn Phế Quản")
        
        st.success("""
        **SABA (Short-Acting Beta-2 Agonist):**
        - **Salbutamol** nebulizer 5mg hoặc MDI 4-8 puffs
        - **Tần suất:** Mỗi 20 phút x 3 lần đầu (giờ đầu)
        - Sau đó: Mỗi 1-4h tùy đáp ứng
        
        **Ipratropium Bromide (Anticholinergic):**
        - **Phối hợp với SABA** hiệu quả hơn đơn trị
        - Ipratropium 0.5mg nebulizer
        - Mỗi 20 phút x 3 lần đầu
        - Sau đó: Mỗi 4-6h
        """)
        
        if severity == "life-threatening":
            st.error("""
            **Cơn hen đe dọa tính mạng:**
            - Salbutamol 5mg + Ipratropium 0.5mg nebulizer
            - **LIÊN TỤC** hoặc mỗi 20 phút
            - Cân nhắc Salbutamol IV nếu không đáp ứng:
              - Loading: 15 mcg/kg IV trong 10 phút
              - Maintenance: 0.1-0.2 mcg/kg/phút
            """)
        elif severity == "severe":
            st.error("""
            **Cơn hen nặng:**
            - Salbutamol 5mg + Ipratropium 0.5mg nebulizer
            - Mỗi 20 phút x 3 lần (giờ đầu)
            - Đánh giá lại sau 1h
            - Nếu cải thiện → Kéo dài interval
            - Nếu không cải thiện → Cân nhắc ICU
            """)
        else:
            st.info("""
            **Cơn hen nhẹ-vừa:**
            - Salbutamol 2.5-5mg nebulizer hoặc MDI 4-8 puffs
            - Mỗi 20 phút x 3 lần (giờ đầu)
            - Thêm Ipratropium nếu đáp ứng kém
            - Sau đó: Mỗi 1-4h tùy đáp ứng
            """)
    
    with tabs[1]:  # Corticosteroids
        st.markdown("#### Corticosteroids Toàn Thân")
        
        st.success("""
        **Khuyến Cáo (GINA 2023):**
        - **Cho NGAY** trong giờ đầu tiên
        - Hiệu quả tương đương IV và PO
        
        **Liều:**
        - **Prednisolone 40-50mg PO** x 5-7 ngày
        - Hoặc **Methylprednisolone 40mg IV** x 5-7 ngày
        - **KHÔNG cần giảm liều dần** nếu <2 tuần
        
        **Lợi ích:**
        - Giảm tái phát
        - Giảm thời gian nằm viện
        - Cải thiện chức năng phổi nhanh hơn
        - Giảm tử vong
        """)
        
        if severity in ["severe", "life-threatening"]:
            st.error("""
            **Cơn hen nặng/đe dọa tính mạng:**
            - **Methylprednisolone 125mg IV** loading
            - Sau đó 40mg IV mỗi 6h
            - Hoặc Hydrocortisone 100mg IV mỗi 6h
            - Chuyển PO khi ổn định
            - Tổng thời gian: 5-7 ngày
            """)
        else:
            st.info("""
            **Liều chuẩn:**
            - **Prednisolone 40-50mg PO** mỗi ngày
            - Uống một lần vào buổi sáng
            - Thời gian: 5-7 ngày
            - Không cần giảm liều dần
            """)
    
    with tabs[2]:  # Add-on therapy
        st.markdown("#### Điều Trị Bổ Sung")
        
        st.success("""
        **Oxygen:**
        - **Mục tiêu:** SpO₂ 93-95% (người lớn)
        - SpO₂ 94-98% (trẻ em)
        - Nasal cannula hoặc mask
        
        **Magnesium Sulfate:**
        - **Chỉ định:** Cơn hen nặng không đáp ứng với điều trị ban đầu
        - **Liều:** 2g IV trong 20 phút
        - **Cơ chế:** Giãn phế quản
        - **Evidence:** Giảm tỷ lệ nhập viện
        """)
        
        if severity in ["severe", "life-threatening"]:
            st.error("""
            **Cơn hen nặng - Thêm vào điều trị:**
            
            **1. Magnesium Sulfate 2g IV:**
            - Pha trong 100ml NS
            - Truyền trong 20 phút
            - Có thể lặp lại sau 20 phút nếu cần
            
            **2. Aminophylline IV (nếu ICU):**
            - Loading: 5-6 mg/kg IV trong 20-30 phút
            - Maintenance: 0.5-0.7 mg/kg/h
            - **LƯU Ý:** Chỉ dùng ở ICU, có monitor ECG
            - Nguy cơ tác dụng phụ cao
            
            **3. Heliox (nếu có):**
            - Hỗn hợp Helium-Oxygen
            - Giảm công thở
            - Cho phép nebulizer hiệu quả hơn
            """)
        
        st.warning("""
        **KHÔNG khuyến cáo:**
        - ❌ Kháng sinh (trừ khi có bằng chứng nhiễm khuẩn)
        - ❌진 an thần (nguy hiểm!)
        - ❌ Mucolytic
        - ❌ Chest physiotherapy trong cơn cấp
        """)
    
    with tabs[3]:  # ICU criteria
        st.markdown("#### Tiêu Chí Nhập ICU & Thở Máy")
        
        st.error("""
        **Chỉ định nhập ICU:**
        
        **Dấu hiệu đe dọa tính mạng:**
        - 🚨 Buồn ngủ, lơ mơ, lú lẫn
        - 🚨 Silent chest (phổi câm)
        - 🚨 Nhịp tim chậm (bradycardia)
        - 🚨 Hạ huyết áp
        - 🚨 SpO₂ <92% dù oxy
        - 🚨 PaCO₂ >45 mmHg (giữ CO₂)
        - 🚨 pH <7.35
        
        **Không đáp ứng điều trị:**
        - Không cải thiện sau 1-2h điều trị tối ưu
        - PEFR <33% dự đoán
        - Kiệt sức
        """)
        
        st.warning("""
        **Thông số NIV (nếu dùng):**
        - **Cẩn thận:** NIV không phải lựa chọn đầu tiên trong hen
        - Chỉ dùng ở bệnh nhân còn tỉnh táo, hợp tác
        - IPAP: 10-15 cmH₂O
        - EPAP: 4-5 cmH₂O
        - Theo dõi sát, chuẩn bị đặt nội khí quản
        """)
        
        st.error("""
        **Chỉ định đặt nội khí quản:**
        - Ngừng thở hoặc ngừng tim
        - Lơ mơ, hôn mê
        - Kiệt sức
        - PaCO₂ tăng tiến triển dù điều trị tối ưu
        
        **Thông số thở máy (nếu cần):**
        - **Mode:** Volume control
        - **Tidal volume:** 6-8 mL/kg IBW
        - **Respiratory rate:** 10-14/phút (cho phép I:E ratio dài)
        - **PEEP:** Thấp (3-5 cmH₂O)
        - **Mục tiêu:** Cho phép "permissive hypercapnia"
        - **Nguy cơ:** Dynamic hyperinflation, barotrauma
        """)
    
    with tabs[4]:  # Monitoring
        st.markdown("#### Theo Dõi & Xuất Viện")
        
        st.success("""
        **Theo dõi tại cấp cứu/bệnh viện:**
        - ✓ SpO₂ liên tục
        - ✓ PEFR mỗi 30-60 phút ban đầu
        - ✓ Vital signs mỗi 15-30 phút
        - ✓ Khí máu động mạch nếu nặng
        - ✓ X-quang ngực (nếu nghi ngờ biến chứng)
        - ✓ ECG (nếu nguy cơ tim mạch)
        
        **Thời gian theo dõi:**
        - Nhẹ-vừa: 1-4h
        - Nặng: 4-24h hoặc nhập viện
        - Đe dọa tính mạng: ICU
        """)
        
        st.info("""
        **Tiêu chuẩn xuất viện:**
        - ✅ SpO₂ >94% trong không khí phòng
        - ✅ PEFR >70% dự đoán hoặc best personal
        - ✅ Không cần SABA >4h
        - ✅ Triệu chứng ổn định ≥12-24h
        - ✅ Đã dùng corticosteroid ít nhất 24h
        - ✅ Hiểu cách dùng inhaler
        - ✅ Có kế hoạch theo dõi ngoại trú
        - ✅ Có thuốc về nhà
        """)
        
        st.warning("""
        **Thuốc xuất viện:**
        
        **1. Controller (Duy trì):**
        - ICS + LABA (ưu tiên)
        - Budesonide-Formoterol 160/4.5mcg x 2 lần/ngày
        - Hoặc Fluticasone-Salmeterol 250/25mcg x 2 lần/ngày
        
        **2. Reliever (Cấp cứu):**
        - Salbutamol MDI 100mcg, 2 puffs khi cần
        - Tối đa mỗi 4h
        
        **3. Prednisolone:**
        - 40-50mg PO mỗi ngày
        - Tiếp tục 5-7 ngày (tổng cộng)
        - Không cần giảm liều
        
        **4. Giáo dục:**
        - ✓ Kỹ thuật sử dụng inhaler
        - ✓ Asthma action plan
        - ✓ Nhận biết triệu chứng xấu đi
        - ✓ Khi nào cần tái khám
        - ✓ Tránh trigger factors
        
        **5. Theo dõi:**
        - Tái khám sau 2-7 ngày
        - Đánh giá lại kỹ thuật inhaler
        - Điều chỉnh điều trị duy trì
        """)
    
    st.markdown("---")
    
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **GINA 2023 - Global Initiative for Asthma**
        
        **Định nghĩa:**
        Cơn hen cấp là đợt xấu đi cấp tính hoặc tiến triển của triệu chứng và chức năng phổi.
        
        **Phân loại mức độ nặng:**
        - **Mild-Moderate:** Có thể nói thành câu, RR <25, HR <110, SpO₂ >95%, PEFR >50%
        - **Severe:** Nói từng cụm từ, RR ≥25, HR ≥110, SpO₂ 90-95%, PEFR 33-50%
        - **Life-threatening:** Silent chest, cyanosis, poor respiratory effort, arrhythmia, hypotension, drowsy/confused, SpO₂ <90%, PEFR <33%
        
        **Evidence-based treatment:**
        - SABA: ✓ First-line bronchodilator
        - Ipratropium + SABA: ✓ Better than SABA alone (severe asthma)
        - Systemic corticosteroids: ✓ Reduce relapse, hospital admission
        - Magnesium sulfate: ✓ Reduce hospital admission (severe asthma)
        
        **Guidelines:**
        - GINA 2023: https://ginasthma.org
        - BTS/SIGN 2019: British Thoracic Society
        - NAEPP EPR-4 2020: US Guidelines
        
        **References:**
        - Rowe BH et al. Cochrane Database. 2013 (Magnesium sulfate)
        - Griffiths B et al. Cochrane Database. 2016 (Ipratropium bromide)
        - Rowe BH et al. Cochrane Database. 2001 (Systemic corticosteroids)
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol hỗ trợ lâm sàng - cần cá thể hóa theo từng bệnh nhân")
