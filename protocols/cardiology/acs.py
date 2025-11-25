"""
Acute Coronary Syndrome (ACS) Protocol
STEMI & NSTEMI Management
"""

import streamlit as st


def render():
    """Acute Coronary Syndrome Protocol"""
    st.subheader("💔 ACS - Hội Chứng Vành Cấp")
    st.caption("STEMI & NSTEMI Management - ESC/AHA Guidelines")
    
    st.info("""
    **ACS (Acute Coronary Syndrome)** bao gồm:
    - **STEMI:** ST-Elevation MI (ST chênh lên)
    - **NSTEMI:** Non-ST-Elevation MI
    - **UA:** Unstable Angina
    """)
    
    # Type selection
    st.markdown("### 1️⃣ Phân Loại ACS")
    
    acs_type = st.radio(
        "**Loại ACS:**",
        ["STEMI (ST chênh lên)", "NSTEMI/UA (Không ST chênh lên)"],
        key="acs_type"
    )
    
    st.markdown("---")
    
    if "STEMI" in acs_type:
        # STEMI Protocol
        st.error("## 🚨 STEMI PROTOCOL")
        st.error("**CODE STEMI - Thời gian là cơ tim!**")
        
        st.markdown("### ⏱️ Timeline Goals")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Door-to-Balloon (PCI)", "≤90 phút", "🎯 Mục tiêu")
        with col2:
            st.metric("Door-to-Needle (Fibrinolysis)", "≤30 phút", "🎯 Mục tiêu")
        
        st.markdown("---")
        st.markdown("### 2️⃣ Xử Trí Tức Thì (Trong 10 Phút Đầu)")
        
        st.error("""
        **A-B-C-D-E Approach:**
        
        **A - Aspirin:**
        - 💊 **Aspirin 300mg** nhai ngay (hoặc 150-325mg)
        - Cho dù bệnh nhân đã uống aspirin tại nhà
        
        **B - Beta-blocker:**
        - Metoprolol 50mg PO (nếu không chống chỉ định)
        - Chống chỉ định: Shock, suy tim, HR <60, SBP <100
        
        **C - Clopidogrel/Ticagrelor (P2Y12 inhibitor):**
        - **Ticagrelor 180mg** loading (ưu tiên)
        - Hoặc **Prasugrel 60mg** (nếu <75 tuổi, >60kg)
        - Hoặc **Clopidogrel 600mg** (nếu không có Ticagrelor)
        
        **D - Drugs (Anticoagulation):**
        - **Unfractionated Heparin (UFH):**
          - Loading: 60 U/kg IV bolus (max 4000 U)
          - Infusion: 12 U/kg/h (max 1000 U/h)
        - Hoặc **Enoxaparin:** 30mg IV bolus, sau đó 1mg/kg SC q12h
        
        **E - ECG & Evaluation:**
        - ECG lặp lại mỗi 15-30 phút
        - Chuẩn bị cath lab
        - Thông báo tim mạch can thiệp
        """)
        
        st.markdown("---")
        st.markdown("### 3️⃣ Chiến Lược Tái Tưới Máu")
        
        col_strat1, col_strat2 = st.columns(2)
        
        with col_strat1:
            st.success("""
            **Primary PCI (Ưu tiên):**
            
            **Điều kiện:**
            - Cath lab sẵn sàng
            - Door-to-balloon ≤90 phút (≤120 phút nếu chuyển viện)
            - Có can thiệp tim mạch 24/7
            
            **Lợi ích:**
            - Mở mạch hiệu quả >90%
            - Ít chảy máu hơn fibrinolysis
            - Tiên lượng tốt hơn
            
            **Thực hiện:**
            - Gọi cath lab NGAY
            - Tiếp tục DAPT + heparin
            - Vận chuyển thẳng đến cath lab
            """)
        
        with col_strat2:
            st.warning("""
            **Fibrinolysis (Nếu không PCI):**
            
            **Điều kiện:**
            - KHÔNG có cath lab
            - Thời gian chuyển viện >120 phút
            - Trong vòng 12h kể từ khởi phát
            - KHÔNG có chống chỉ định
            
            **Thuốc:**
            - **Tenecteplase (TNK-tPA):**
              - <60kg: 30mg IV bolus
              - 60-69kg: 35mg
              - 70-79kg: 40mg
              - 80-89kg: 45mg
              - ≥90kg: 50mg
            
            **Sau fibrinolysis:**
            - Chuyển viện để PCI (trong 3-24h)
            - Rescue PCI nếu không mở mạch
            """)
        
        st.error("""
        **Chống chỉ định Fibrinolysis:**
        
        **Tuyệt đối:**
        - Chảy máu nội sọ tiền sử
        - Đột quỵ trong 3 tháng
        - Chấn thương/phẫu thuật trong 3 tuần
        - Chảy máu đường tiêu hóa trong 1 tháng
        - Rối loạn đông máu
        
        **Tương đối:**
        - Tuổi >75
        - Đang dùng warfarin
        - THA không kiểm soát (>180/110)
        - Massage tim
        - Thai kỳ
        """)
        
    else:
        # NSTEMI/UA Protocol
        st.warning("## ⚠️ NSTEMI/UA PROTOCOL")
        
        st.markdown("### 2️⃣ Xử Trí Ban Đầu")
        
        st.success("""
        **Điều trị ngay (trong 30 phút):**
        
        **1. Aspirin 300mg** nhai (hoặc 150-325mg)
        
        **2. P2Y12 inhibitor:**
        - **Ticagrelor 180mg** (ưu tiên - Class I)
        - Hoặc **Prasugrel 60mg** (nếu biết được mạch vành)
        - Hoặc **Clopidogrel 600mg**
        
        **3. Anticoagulation:**
        - **Fondaparinux 2.5mg SC** mỗi ngày (ưu tiên nếu không PCI ngay)
        - Hoặc **Enoxaparin 1mg/kg SC** q12h
        - Hoặc **UFH** infusion (nếu PCI trong 24h)
        
        **4. Anti-ischemic therapy:**
        - Beta-blocker: Metoprolol 25-50mg PO
        - Nitrate: GTN sublingual hoặc IV (nếu còn đau)
        - Morphine: CHỈ nếu đau không giảm với nitrate
        
        **5. Statin:**
        - **Atorvastatin 80mg** PO ngay (high-intensity)
        """)
        
        st.markdown("---")
        st.markdown("### 3️⃣ Phân Tầng Nguy Cơ & Chiến Lược")
        
        st.info("""
        **Sử dụng GRACE Score hoặc TIMI Risk Score**
        
        → Xem tab **Scores > Cardiology**
        """)
        
        col_risk1, col_risk2, col_risk3 = st.columns(3)
        
        with col_risk1:
            st.success("""
            **Nguy cơ THẤP:**
            - GRACE ≤108
            - TIMI 0-2
            
            **Chiến lược:**
            - Conservative
            - Điều trị nội khoa
            - Stress test hoặc CT angio ngoại trú
            - PCI trong vài tuần nếu cần
            """)
        
        with col_risk2:
            st.warning("""
            **Nguy cơ TRUNG BÌNH:**
            - GRACE 109-140
            - TIMI 3-4
            
            **Chiến lược:**
            - Early Invasive
            - Angiography trong **24-72h**
            - PCI nếu cần
            """)
        
        with col_risk3:
            st.error("""
            **Nguy cơ CAO:**
            - GRACE >140
            - TIMI ≥5
            
            **Chiến lược:**
            - Immediate Invasive
            - Angiography **<24h**
            - PCI/CABG khẩn cấp
            """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Điều Trị Tại ICU/CCU")
    
    tabs = st.tabs(["💊 Medications", "🎯 Monitoring", "⚠️ Complications", "🏥 Discharge"])
    
    with tabs[0]:
        st.markdown("#### Thuốc Duy Trì")
        st.success("""
        **DAPT (Dual Antiplatelet Therapy):**
        - **Aspirin 75-100mg** PO mỗi ngày (trọn đời)
        - **Ticagrelor 90mg** PO x 2 lần/ngày (12 tháng)
          - Hoặc Prasugrel 10mg PO mỗi ngày
          - Hoặc Clopidogrel 75mg PO mỗi ngày
        
        **Beta-blocker:**
        - Metoprolol 25-50mg PO x 2 lần/ngày
        - Hoặc Bisoprolol, Carvedilol
        - Mục tiêu HR: 50-60 bpm
        
        **ACE Inhibitor (hoặc ARB):**
        - Ramipril 2.5-10mg PO mỗi ngày
        - Hoặc Perindopril, Enalapril
        - Bắt đầu sớm, tăng liều dần
        
        **Statin (High-Intensity):**
        - **Atorvastatin 80mg** PO mỗi ngày
        - Hoặc Rosuvastatin 20-40mg
        - Mục tiêu LDL <55 mg/dL (1.4 mmol/L)
        
        **Aldosterone antagonist (nếu EF <40%):**
        - Spironolactone 25mg PO mỗi ngày
        - Hoặc Eplerenone
        """)
    
    with tabs[1]:
        st.markdown("#### Theo Dõi")
        st.info("""
        **Theo dõi tại CCU:**
        - ✓ Theo dõi ECG liên tục
        - ✓ Dấu hiệu sống mỗi 1-2h
        - ✓ Troponin theo dõi (0h, 3h, 6h)
        - ✓ ECG hàng ngày
        - ✓ Siêu âm tim (đánh giá EF, biến chứng)
        - ✓ Hồ sơ lipid, HbA1c
        
        **Thời gian nằm viện:**
        - STEMI không biến chứng: 3-5 ngày
        - NSTEMI: 2-4 ngày
        - Có biến chứng: 7-14 ngày
        """)
    
    with tabs[2]:
        st.markdown("#### Biến Chứng")
        st.error("""
        **Biến chứng cần theo dõi:**
        
        **1. Loạn nhịp tim:**
        - VF/VT (24-48h đầu)
        - Nhịp chậm (inferior MI)
        - AF mới (15-20%)
        
        **2. Cơ học:**
        - Suy tim cấp
        - Shock tim
        - Thủng vách liên thất (ngày 3-5)
        - Đứt cơ nhú (ngày 2-7)
        - Thủng thành tim
        
        **3. Pericarditis:**
        - Viêm màng ngoài tim sớm (2-4 ngày)
        - Hội chứng Dressler (tuần 2-10)
        
        **4. Tái nhồi máu:**
        - Đau ngực tái phát
        - ST chênh lên lại
        - Troponin tăng lại
        """)
    
    with tabs[3]:
        st.markdown("#### Tiêu Chuẩn Xuất Viện & Theo Dõi")
        st.success("""
        **Tiêu chuẩn xuất viện:**
        - ✅ Không đau ngực ≥24h
        - ✅ Huyết động ổn định
        - ✅ Không loạn nhịp tim nguy hiểm
        - ✅ Đã PCI/điều trị nội khoa ổn định
        - ✅ Echo đã làm (biết EF)
        - ✅ Đã giáo dục bệnh nhân
        - ✅ Có thuốc về nhà đầy đủ
        
        **Cardiac Rehabilitation:**
        - Bắt đầu tại bệnh viện
        - Tiếp tục ngoại trú 3-6 tháng
        - Tập luyện có giám sát
        - Tư vấn dinh dưỡng, tâm lý
        """)
        
        st.info("""
        **Thuốc xuất viện (DAPT + 3 Drugs):**
        
        **1. Aspirin 75-100mg** - trọn đời
        **2. Ticagrelor 90mg x2/ngày** - 12 tháng
        **3. Atorvastatin 80mg** - trọn đời
        **4. Ramipril** hoặc ACE-I - trọn đời
        **5. Metoprolol** hoặc beta-blocker - trọn đời
        
        **(+) Spironolactone nếu EF <40%**
        
        **Theo dõi:**
        - Tuần 1-2: Tái khám
        - Tháng 1: Hồ sơ lipid, điều chỉnh statin
        - Tháng 3: Echo kiểm tra EF
        - Tháng 12: Đánh giá toàn diện, có thể ngưng P2Y12
        """)
        
        st.warning("""
        **Thay đổi lối sống (Bắt buộc):**
        - 🚭 **CAI THUỐC LÁ** (quan trọng nhất!)
        - 🏃 Tập thể dục đều đặn
        - 🥗 Chế độ ăn Mediterranean
        - 🎯 Kiểm soát ĐTĐ (HbA1c <7%)
        - 💉 Kiểm soát THA (<130/80)
        - 📊 Mục tiêu LDL <55 mg/dL
        - ⚖️ BMI 18.5-24.9
        """)
    
    st.markdown("---")
    
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **ESC Guidelines 2020 - Acute Coronary Syndromes**
        **AHA/ACC Guidelines 2021**
        
        **STEMI Management:**
        - Primary PCI preferred (<120 min door-to-balloon)
        - Fibrinolysis if PCI not available (<30 min door-to-needle)
        - DAPT for 12 months
        - High-intensity statin
        - ACE-I, Beta-blocker
        
        **NSTEMI/UA Management:**
        - Risk stratification (GRACE, TIMI)
        - Early invasive strategy if high risk
        - DAPT + anticoagulation
        - GDMT (Guideline-Directed Medical Therapy)
        
        **Timeline Goals:**
        - STEMI: Door-to-balloon ≤90 min
        - STEMI (transferred): Door-to-balloon ≤120 min
        - Fibrinolysis: Door-to-needle ≤30 min
        - High-risk NSTEMI: Angiography <24h
        - Intermediate-risk: Angiography <72h
        
        **References:**
        - Collet JP et al. Eur Heart J. 2021;42(14):1289-1367.
        - Ibanez B et al. Eur Heart J. 2018;39(2):119-177.
        - Lawton JS et al. Circulation. 2022;145(18):e18-e114.
        
        **Links:**
        - ESC 2020 NSTE-ACS: https://academic.oup.com/eurheartj/article/42/14/1289/6146063
        - ESC 2017 STEMI: https://academic.oup.com/eurheartj/article/39/2/119/4095042
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol hỗ trợ lâm sàng - CODE STEMI cần quy trình bệnh viện cụ thể")

