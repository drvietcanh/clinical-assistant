"""
Acute Coronary Syndrome (ACS) Protocol
STEMI & NSTEMI Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)


def render():
    """Acute Coronary Syndrome Protocol"""
    st.subheader("💔 ACS - Hội Chứng Vành Cấp")
    st.caption("STEMI & NSTEMI Management - ESC/AHA Guidelines")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="ACS",
        guideline_source="ACC/AHA/SCAI 2024",
        show_version=True,
        show_evidence_summary=True
    )
    
    st.info("""
    **ACS (Acute Coronary Syndrome)** bao gồm:
    - **STEMI:** ST-Elevation MI (ST chênh lên)
    - **NSTEMI:** Non-ST-Elevation MI
    - **UA:** Unstable Angina
    """)
    
    # Type selection
    st.markdown("### 1️⃣ Phân loại ACS")
    
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
        st.markdown("### 2️⃣ Xử tríTức Thì (Trong 10 Phút Đầu)")
        
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
        
        st.markdown("### 2️⃣ High-Sensitivity Troponin (hs-Tn) Algorithms")
        
        st.info("""
        **ESC 2020, AHA 2021 Guidelines:**
        - **High-sensitivity troponin** cho phép rule-out/rule-in nhanh
        - **0/1h Algorithm:** Rule-out trong 1 giờ
        - **0/2h Algorithm:** Alternative
        - **0/3h Algorithm:** Nếu không có hs-Tn
        """)
        
        troponin_algorithm = st.radio(
            "**Chọn Algorithm:**",
            ["0/1h Algorithm (Ưu tiên)", "0/2h Algorithm", "0/3h Algorithm (Standard)"],
            key="troponin_algorithm"
        )
        
        if troponin_algorithm == "0/1h Algorithm (Ưu tiên)":
            st.success("""
            **0/1h hs-Troponin Algorithm:**
            
            **Lấy mẫu:**
            - **T0:** Ngay khi đến
            - **T1:** Sau 1 giờ
            
            **Interpretation:**
            
            **Rule-Out (Loại trừ MI):**
            - T0 < LoD (Limit of Detection) VÀ T1 < LoD
            - Hoặc T0 < LoD VÀ delta <2 ng/L
            - **→ Có thể xuất viện** (nếu low risk)
            
            **Rule-In (Chẩn đoán MI):**
            - T0 ≥ 52 ng/L HOẶC T1 ≥ 52 ng/L
            - Hoặc delta ≥5 ng/L
            - **→ Chẩn đoán NSTEMI, điều trị ngay**
            
            **Observe Zone:**
            - Không rule-out, không rule-in
            - **→ Theo dõi thêm, lấy T2 (sau 2-3h)**
            
            **Lưu ý:** Ngưỡng có thể khác nhau tùy assay
            """)
            
            col1, col2 = st.columns(2)
            with col1:
                t0_troponin = st.number_input(
                    "**T0 hs-Troponin (ng/L):**",
                    min_value=0.0,
                    max_value=1000.0,
                    value=10.0,
                    step=1.0,
                    key="t0_troponin"
                )
            with col2:
                t1_troponin = st.number_input(
                    "**T1 hs-Troponin (ng/L):**",
                    min_value=0.0,
                    max_value=1000.0,
                    value=12.0,
                    step=1.0,
                    key="t1_troponin"
                )
            
            delta = abs(t1_troponin - t0_troponin)
            
            if t0_troponin < 5 and t1_troponin < 5:
                st.success("**✅ Rule-Out: Loại trừ MI** - Có thể xuất viện nếu low risk")
            elif t0_troponin >= 52 or t1_troponin >= 52 or delta >= 5:
                st.error("**🚨 Rule-In: Chẩn đoán NSTEMI** - Điều trị ngay")
            else:
                st.warning(f"**⚠️ Observe Zone** - Delta: {delta:.1f} ng/L. Theo dõi thêm, lấy T2")
        
        elif troponin_algorithm == "0/2h Algorithm":
            st.info("""
            **0/2h hs-Troponin Algorithm:**
            
            **Lấy mẫu:**
            - **T0:** Ngay khi đến
            - **T2:** Sau 2 giờ
            
            **Interpretation:**
            
            **Rule-Out:**
            - T0 < LoD VÀ T2 < LoD
            - Hoặc T0 < LoD VÀ delta <3 ng/L
            
            **Rule-In:**
            - T0 ≥ 52 ng/L HOẶC T2 ≥ 52 ng/L
            - Hoặc delta ≥5 ng/L
            
            **Observe Zone:**
            - Theo dõi thêm, lấy T3 (sau 3h)
            """)
        
        else:  # 0/3h Algorithm
            st.warning("""
            **0/3h Standard Troponin Algorithm:**
            
            **Lấy mẫu:**
            - **T0:** Ngay khi đến
            - **T3:** Sau 3 giờ
            
            **Interpretation:**
            - **Rule-Out:** T0 và T3 đều < URL (Upper Reference Limit)
            - **Rule-In:** T0 hoặc T3 ≥ URL, hoặc delta ≥20% (hoặc ≥50% tùy assay)
            
            **Lưu ý:** Chậm hơn 0/1h và 0/2h algorithms
            """)
        
        st.markdown("---")
        st.markdown("### 2️⃣ Xử tríBan Đầu")
        
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
        st.markdown("### 3️⃣ Phân tầng Nguy cơ & Chiến Lược")
        
        st.info("""
        **Sử dụng GRACE Score hoặc TIMI Risk Score**
        
        → Xem tab **Scores > Cardiology**
        """)
        
        st.markdown("#### 🔍 Coronary CT Angiography (CCTA)")
        
        st.info("""
        **ESC 2020 Guidelines:**
        - **Chỉ định:** Low-intermediate risk NSTEMI/UA
        - **Rule-out:** Nếu CCTA negative → có thể discharge
        - **Rule-in:** Nếu CCTA positive → invasive angiography
        """)
        
        use_ccta = st.radio(
            "**Có chỉ định CCTA?**",
            ["Có (Low-intermediate risk)", "Không (High risk hoặc đã có troponin positive)"],
            key="use_ccta"
        )
        
        if use_ccta == "Có (Low-intermediate risk)":
            st.success("""
            **CCTA Protocol:**
            
            **Chỉ định:**
            - Low-intermediate risk (GRACE <140, TIMI 0-2)
            - Troponin negative hoặc borderline
            - Không có ECG changes rõ ràng
            - Stable hemodynamics
            
            **Kết quả:**
            - **CCTA Negative:** Không có hẹp >50% → Có thể discharge với follow-up
            - **CCTA Positive:** Có hẹp >50% → Invasive angiography
            
            **Ưu điểm:**
            - Rule-out nhanh, giảm nhập viện không cần thiết
            - Non-invasive
            
            **Nhược điểm:**
            - Cần contrast, radiation
            - Không phù hợp nếu high risk
            """)
        
        st.markdown("---")
        
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
        st.markdown("#### ⏱️ Early Invasive Strategy - Timing Chi Tiết (ESC 2020)")
        
        st.info("""
        **ESC 2020 Guidelines - Timing của Invasive Strategy:**
        """)
        
        invasive_timing = st.radio(
            "**Chọn timing:**",
            [
                "Immediate (<2h)",
                "Early (<24h)",
                "Delayed (24-72h)",
                "Conservative (>72h hoặc không)"
            ],
            key="invasive_timing"
        )
        
        if invasive_timing == "Immediate (<2h)":
            st.error("""
            **Immediate Invasive Strategy (<2h):**
            
            **Chỉ định:**
            - **Refractory angina** (đau ngực không đáp ứng với điều trị)
            - **Hemodynamic instability** (shock, hypotension)
            - **Life-threatening arrhythmias** (VT, VF, complete heart block)
            - **Mechanical complications** (MR, VSD, free wall rupture)
            
            **Quy trình:**
            1. Gọi cath lab NGAY
            2. Chuẩn bị PCI/CABG
            3. Tiếp tục DAPT + anticoagulation
            4. Angiography trong <2h
            
            **Mục tiêu:** Mở mạch càng sớm càng tốt
            """)
        
        elif invasive_timing == "Early (<24h)":
            st.warning("""
            **Early Invasive Strategy (<24h):**
            
            **Chỉ định:**
            - **GRACE Score >140**
            - **TIMI Risk Score ≥5**
            - **Dynamic ECG changes** (ST depression, T wave inversion mới)
            - **Elevated troponin** (hs-Tn positive)
            - **Diabetes mellitus**
            - **Renal dysfunction** (eGFR <60)
            - **LVEF <40%**
            - **Early post-infarction angina**
            - **PCI trong 6 tháng**
            - **CABG trước đó**
            
            **Quy trình:**
            1. Điều trị nội khoa tối ưu
            2. Angiography trong 24h
            3. PCI nếu có chỉ định
            4. CABG nếu không phù hợp PCI
            
            **Mục tiêu:** Giảm mortality và recurrent MI
            """)
        
        elif invasive_timing == "Delayed (24-72h)":
            st.info("""
            **Delayed Invasive Strategy (24-72h):**
            
            **Chỉ định:**
            - **GRACE Score 109-140**
            - **TIMI Risk Score 3-4**
            - **Intermediate risk** nhưng stable
            - **Không có high-risk features**
            
            **Quy trình:**
            1. Điều trị nội khoa tối ưu
            2. Angiography trong 24-72h
            3. PCI nếu cần
            
            **Mục tiêu:** Giảm nhập viện và tái phát
            """)
        
        else:  # Conservative
            st.success("""
            **Conservative Strategy (>72h hoặc không invasive):**
            
            **Chỉ định:**
            - **GRACE Score ≤108**
            - **TIMI Risk Score 0-2**
            - **Low risk** và stable
            - **Troponin negative** hoặc borderline
            
            **Quy trình:**
            1. Điều trị nội khoa tối ưu
            2. Stress test hoặc CCTA ngoại trú
            3. PCI elective nếu cần (trong vài tuần)
            
            **Mục tiêu:** Tránh invasive procedure không cần thiết
            """)
        
        st.markdown("---")
        st.markdown("#### 💉 Glycoprotein IIb/IIIa Inhibitors")
        
        st.info("""
        **ESC 2020 Guidelines:**
        - **Không routine:** Chỉ dùng khi có chỉ định cụ thể
        - **Chỉ định:** High-risk PCI, high thrombus burden
        """)
        
        use_gp2b3a = st.radio(
            "**Có chỉ định GP IIb/IIIa inhibitors?**",
            ["Có (High-risk PCI)", "Không (Routine không cần)"],
            key="use_gp2b3a"
        )
        
        if use_gp2b3a == "Có (High-risk PCI)":
            st.warning("""
            **Chỉ định GP IIb/IIIa Inhibitors:**
            
            **1. High-risk PCI:**
            - Complex lesions (bifurcation, thrombus, long lesions)
            - High thrombus burden trên angiography
            - Suboptimal result sau PCI
            
            **2. High-risk patients:**
            - Diabetes mellitus
            - Elevated troponin
            - Large territory at risk
            
            **Thuốc:**
            
            **Abciximab:**
            - **Liều:** 0.25 mg/kg IV bolus, sau đó 0.125 mcg/kg/min × 12h
            - **Ưu điểm:** Tác dụng mạnh, lâu dài
            - **Nhược điểm:** Tăng nguy cơ chảy máu
            
            **Eptifibatide:**
            - **Liều:** 180 mcg/kg IV bolus × 2 (10 phút apart), sau đó 2 mcg/kg/min × 18h
            - **Ưu điểm:** Tác dụng ngắn, có thể reverse
            - **Nhược điểm:** Cần infusion lâu
            
            **Tirofiban:**
            - **Liều:** 25 mcg/kg IV bolus, sau đó 0.15 mcg/kg/min × 18h
            - **Ưu điểm:** Tương tự eptifibatide
            - **Nhược điểm:** Cần infusion lâu
            
            **Lưu ý:**
            - Dùng kết hợp với DAPT và heparin
            - Monitoring: Platelet count, bleeding
            - Chống chỉ định: Active bleeding, thrombocytopenia
            """)
        
        else:
            st.success("""
            **Không cần GP IIb/IIIa inhibitors:**
            
            **Lý do:**
            - Routine PCI không cần GP IIb/IIIa inhibitors
            - DAPT (aspirin + P2Y12) đã đủ trong hầu hết trường hợp
            - GP IIb/IIIa chỉ tăng nguy cơ chảy máu mà không cải thiện outcomes đáng kể
            
            **Chỉ dùng khi:**
            - High-risk PCI với thrombus burden cao
            - Suboptimal result sau PCI
            - Có chỉ định cụ thể
            """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Điều trị Tại ICU/CCU")
    
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
        st.markdown("#### Theo dõi")
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
        st.markdown("#### Biến chứng")
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
        st.markdown("#### Tiêu chuẩn xuất viện & Theo dõi")
        st.success("""
        **Tiêu Chuẩn Xuất Viện:**
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
    
    with st.expander("📚 Tài liệu tham khảo"):
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
        
        """)
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("ACS")
    
    st.markdown("---")
    st.caption("⚠️ Protocol hỗ trợ lâm sàng - CODE STEMI cần quy trình bệnh viện cụ thể")

