"""
Clinical Scenarios for Critical Care
Step-by-step guidance for common ICU scenarios
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def render_sepsis_scenario():
    """Render Sepsis clinical scenario"""
    st.subheader("🦠 Sepsis Scenario")
    st.caption("Hướng dẫn từng bước xử lý nhiễm trùng huyết")
    
    st.markdown("""
    **Sepsis** là một tình trạng đe dọa tính mạng do phản ứng của cơ thể với nhiễm trùng.
    Cần xử lý nhanh chóng theo **Sepsis-3 Guidelines** và **1-Hour Bundle**.
    """)
    
    st.markdown("---")
    
    # Step 1: Recognition
    with st.expander("📋 Bước 1: Nhận diện Sepsis", expanded=True):
        st.markdown("""
        **Tiêu chuẩn Sepsis-3:**
        - Nhiễm trùng nghi ngờ hoặc xác định
        - **SOFA score ≥2** (tăng ≥2 điểm so với baseline)
        
        **qSOFA (Quick SOFA) - Sàng lọc:**
        - Huyết áp tâm thu ≤100 mmHg
        - Nhịp thở ≥22 lần/phút
        - Thay đổi ý thức (GCS <15)
        
        **≥2/3 tiêu chí qSOFA** → Nghi ngờ sepsis cao
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Tính SOFA Score", key="sepsis_sofa"):
                st.session_state['sepsis_scenario_tool'] = 'sofa'
        with col2:
            if st.button("⚡ Tính qSOFA", key="sepsis_qsofa"):
                st.session_state['sepsis_scenario_tool'] = 'qsofa'
    
    # Step 2: 1-Hour Bundle
    with st.expander("⏱️ Bước 2: 1-Hour Bundle (Bắt buộc)", expanded=True):
        st.markdown("""
        **Phải hoàn thành trong 1 giờ đầu:**
        
        1. **Lấy máu cấy** (trước khi dùng kháng sinh)
        2. **Đo lactate** (nếu tăng → đo lại)
        3. **Dùng kháng sinh phổ rộng** (trong 1 giờ)
        4. **Bù dịch 30ml/kg** (nếu hạ huyết áp hoặc lactate ≥4)
        5. **Vasopressor** (nếu hạ huyết áp sau bù dịch)
        """)
        
        st.warning("""
        **⚠️ QUAN TRỌNG:**
        - Không được trì hoãn kháng sinh để chờ cấy máu
        - Bù dịch tích cực nếu có shock
        - Theo dõi lactate clearance
        """)
        
        if st.button("🦠 Xem Sepsis Protocols", key="sepsis_protocols"):
            st.session_state['sepsis_scenario_tool'] = 'protocols'
    
    # Step 3: Fluid Resuscitation
    with st.expander("💧 Bước 3: Bù Dịch", expanded=True):
        st.markdown("""
        **Mục tiêu:**
        - MAP ≥65 mmHg
        - Lactate clearance ≥20% trong 2 giờ
        - Urine output ≥0.5 ml/kg/h
        
        **Dịch truyền:**
        - **30ml/kg** trong 1 giờ đầu (nếu shock)
        - Crystalloid (NS, LR) ưu tiên
        - Theo dõi đáp ứng (PLR test)
        """)
        
        if st.button("💧 Tính Fluid Therapy", key="sepsis_fluid"):
            st.session_state['sepsis_scenario_tool'] = 'fluid'
    
    # Step 4: Vasopressors
    with st.expander("💉 Bước 4: Vasopressor", expanded=True):
        st.markdown("""
        **Chỉ định:**
        - MAP <65 mmHg sau bù dịch đầy đủ
        - Shock không đáp ứng với dịch
        
        **Lựa chọn:**
        - **Norepinephrine** (ưu tiên hàng đầu)
        - **Vasopressin** (nếu cần liều NE cao)
        - **Epinephrine** (nếu cần inotrope)
        """)
        
        if st.button("💉 Xem Vasopressor Guide", key="sepsis_vaso"):
            st.session_state['sepsis_scenario_tool'] = 'vasopressor'
    
    # Step 5: Monitoring
    with st.expander("📊 Bước 5: Theo Dõi", expanded=True):
        st.markdown("""
        **Theo dõi:**
        - **Lactate clearance:** Đo lại sau 2-4 giờ
        - **Vital signs:** Liên tục
        - **Urine output:** Mỗi giờ
        - **ABG:** Nếu có suy hô hấp
        
        **Mục tiêu:**
        - Lactate clearance ≥20% trong 2 giờ
        - MAP ≥65 mmHg
        - Urine output ≥0.5 ml/kg/h
        """)
        
        if st.button("📊 Tính Lactate Clearance", key="sepsis_lactate"):
            st.session_state['sepsis_scenario_tool'] = 'lactate'
    
    st.markdown("---")
    st.info("""
    **💡 Tài liệu tham khảo:**
    - Surviving Sepsis Campaign Guidelines 2021
    - Sepsis-3 Definitions (JAMA 2016)
    - IDSA Guidelines
    """)


def render_ards_scenario():
    """Render ARDS clinical scenario"""
    st.subheader("🫁 ARDS Scenario")
    st.caption("Hướng dẫn xử lý hội chứng suy hô hấp cấp")
    
    st.markdown("""
    **ARDS (Acute Respiratory Distress Syndrome)** là suy hô hấp cấp do tổn thương phổi lan tỏa.
    Cần xử lý theo **ARDSNet Protocol** với lung-protective ventilation.
    """)
    
    st.markdown("---")
    
    # Step 1: Diagnosis
    with st.expander("📋 Bước 1: Chẩn Đoán ARDS", expanded=True):
        st.markdown("""
        **Tiêu chuẩn Berlin Definition (2012):**
        
        1. **Khởi phát:** Trong vòng 1 tuần
        2. **X-quang:** Bóng mờ 2 bên phổi
        3. **Không do:** Suy tim hoặc quá tải dịch
        4. **P/F ratio:**
           - **Mild:** 200-300 mmHg
           - **Moderate:** 100-200 mmHg
           - **Severe:** <100 mmHg
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            pao2 = st.number_input("PaO₂ (mmHg):", min_value=0, max_value=500, value=80, key="ards_pao2")
        with col2:
            fio2 = st.number_input("FiO₂ (0-1):", min_value=0.0, max_value=1.0, value=0.6, step=0.1, key="ards_fio2")
        
        if pao2 > 0 and fio2 > 0:
            pf_ratio = pao2 / fio2
            st.markdown(f"**P/F Ratio:** {pf_ratio:.0f} mmHg")
            
            if pf_ratio >= 300:
                st.success("Không phải ARDS (P/F ≥300)")
            elif pf_ratio >= 200:
                st.warning("ARDS Mild (P/F 200-300)")
            elif pf_ratio >= 100:
                st.error("ARDS Moderate (P/F 100-200)")
            else:
                st.error("ARDS Severe (P/F <100)")
    
    # Step 2: Ventilator Settings
    with st.expander("🫁 Bước 2: Cài Đặt Máy Thở", expanded=True):
        st.markdown("""
        **ARDSNet Protocol (Lung-Protective Ventilation):**
        
        - **Tidal Volume:** 6 ml/kg IBW (không quá 6 ml/kg)
        - **PEEP:** Theo PEEP/FiO₂ table
        - **Plateau Pressure:** ≤30 cmH₂O
        - **FiO₂:** Giảm dần khi có thể
        - **I:E ratio:** 1:1 hoặc 1:2
        """)
        
        st.warning("""
        **⚠️ QUAN TRỌNG:**
        - **KHÔNG** dùng tidal volume >6 ml/kg IBW
        - **KHÔNG** để plateau pressure >30 cmH₂O
        - Theo dõi driving pressure (Pplat - PEEP) <15 cmH₂O
        """)
        
        if st.button("🫁 ARDSNet Calculator", key="ards_calc"):
            st.session_state['ards_scenario_tool'] = 'ardsnet'
    
    # Step 3: PEEP/FiO₂ Table
    with st.expander("📊 Bước 3: PEEP/FiO₂ Table", expanded=True):
        st.markdown("""
        **Sử dụng PEEP/FiO₂ table để điều chỉnh:**
        - Bắt đầu từ PEEP thấp
        - Tăng PEEP nếu FiO₂ >0.6
        - Giảm PEEP khi FiO₂ giảm
        """)
        
        if st.button("📊 Xem PEEP/FiO₂ Table", key="ards_peep_table"):
            st.session_state['ards_scenario_tool'] = 'peep_table'
    
    # Step 4: Prone Positioning
    with st.expander("🔄 Bước 4: Nằm Sấp (Prone)", expanded=True):
        st.markdown("""
        **Chỉ định:**
        - ARDS Moderate-Severe (P/F <150)
        - FiO₂ >0.6, PEEP ≥10
        - Không cải thiện sau 12-24h
        
        **Lợi ích:**
        - Cải thiện oxygenation
        - Giảm VILI (ventilator-induced lung injury)
        - Giảm mortality (PROSEVA trial)
        
        **Thời gian:** 16-18 giờ/ngày
        """)
        
        st.info("""
        **💡 Lưu ý:**
        - Cần team có kinh nghiệm
        - Theo dõi sát trong quá trình prone
        - Đánh giá lại sau 4-6 giờ
        """)
    
    # Step 5: Rescue Therapies
    with st.expander("🚨 Bước 5: Điều Trị Cứu Hộ", expanded=True):
        st.markdown("""
        **Khi ARDS không đáp ứng:**
        
        1. **ECMO** (Extracorporeal Membrane Oxygenation)
           - ARDS Severe, P/F <80
           - Refractory hypoxemia
           - Cần trung tâm có ECMO
        
        2. **Neuromuscular Blockade**
           - ARDS Severe, P/F <150
           - Patient-ventilator dyssynchrony
           - Cisatracurium 37.5 mg/h
        
        3. **Inhaled Nitric Oxide (iNO)**
           - Refractory hypoxemia
           - Tác dụng tạm thời
        """)
    
    st.markdown("---")
    st.info("""
    **💡 Tài liệu tham khảo:**
    - ARDSNet Protocol (NEJM 2000)
    - Berlin Definition (JAMA 2012)
    - PROSEVA Trial (NEJM 2013)
    """)


def render_shock_scenario():
    """Render Shock clinical scenario"""
    st.subheader("💉 Shock Scenario")
    st.caption("Hướng dẫn xử lý sốc - Huyết động không ổn định")
    
    st.markdown("""
    **Shock** là tình trạng giảm tưới máu mô dẫn đến thiếu oxy tế bào.
    Cần xác định loại shock và xử lý phù hợp.
    """)
    
    st.markdown("---")
    
    # Step 1: Classification
    with st.expander("📋 Bước 1: Phân Loại Shock", expanded=True):
        st.markdown("""
        **4 Loại Shock:**
        
        1. **Hypovolemic (Giảm thể tích)**
           - Mất máu, mất dịch
           - CVP thấp, CO thấp
           - Điều trị: Bù dịch, truyền máu
        
        2. **Cardiogenic (Tim)**
           - Suy tim, nhồi máu cơ tim
           - CVP cao, CO thấp
           - Điều trị: Inotrope, giảm afterload
        
        3. **Distributive (Phân bố)**
           - Sepsis, anaphylaxis, neurogenic
           - CVP thấp, CO cao
           - Điều trị: Bù dịch, vasopressor
        
        4. **Obstructive (Tắc nghẽn)**
           - PE, tamponade, tension pneumothorax
           - CVP cao, CO thấp
           - Điều trị: Giải quyết nguyên nhân
        """)
        
        if st.button("💉 Xem Shock Classification", key="shock_classify"):
            st.session_state['shock_scenario_tool'] = 'classification'
    
    # Step 2: Assessment
    with st.expander("📊 Bước 2: Đánh Giá", expanded=True):
        st.markdown("""
        **Đánh giá huyết động:**
        
        - **MAP:** Mục tiêu ≥65 mmHg
        - **CO/CI:** Cardiac output/index
        - **CVP:** Central venous pressure
        - **SVR:** Systemic vascular resistance
        - **Lactate:** Tưới máu mô
        - **Urine output:** Tưới máu thận
        """)
        
        st.warning("""
        **⚠️ QUAN TRỌNG:**
        - Đánh giá đầy đủ trước khi điều trị
        - Xác định loại shock để điều trị đúng
        - Theo dõi đáp ứng điều trị
        """)
    
    # Step 3: Fluid Responsiveness
    with st.expander("💧 Bước 3: Đánh Giá Đáp Ứng Dịch", expanded=True):
        st.markdown("""
        **Test đáp ứng dịch:**
        
        1. **Passive Leg Raise (PLR)**
           - Nâng chân 45° trong 1 phút
           - Tăng CO ≥10% → Đáp ứng dịch
        
        2. **Fluid Challenge**
           - 250-500ml NS trong 10-15 phút
           - Tăng CO ≥10% → Đáp ứng dịch
        
        3. **SVV (Stroke Volume Variation)**
           - SVV >12% → Đáp ứng dịch
        """)
        
        if st.button("💧 Xem Fluid Responsiveness", key="shock_fluid"):
            st.session_state['shock_scenario_tool'] = 'fluid_responsiveness'
    
    # Step 4: Vasopressor Selection
    with st.expander("💉 Bước 4: Chọn Vasopressor", expanded=True):
        st.markdown("""
        **Lựa chọn theo loại shock:**
        
        **Distributive (Sepsis):**
        - **Norepinephrine** (ưu tiên)
        - Vasopressin (nếu cần liều NE cao)
        
        **Cardiogenic:**
        - **Dobutamine** (inotrope)
        - Norepinephrine + Dobutamine
        
        **Hypovolemic:**
        - Bù dịch trước
        - Norepinephrine tạm thời
        """)
        
        if st.button("💉 Xem Vasopressor Guide", key="shock_vaso"):
            st.session_state['shock_scenario_tool'] = 'vasopressor'
    
    # Step 5: Monitoring
    with st.expander("📊 Bước 5: Theo Dõi", expanded=True):
        st.markdown("""
        **Theo dõi:**
        - **MAP:** ≥65 mmHg
        - **Lactate:** Giảm dần
        - **Urine output:** ≥0.5 ml/kg/h
        - **CO/CI:** Cải thiện
        - **SvO₂/ScvO₂:** ≥70%
        """)
    
    st.markdown("---")
    st.info("""
    **💡 Tài liệu tham khảo:**
    - Surviving Sepsis Guidelines
    - Shock Management Protocols
    """)


def render_ventilator_weaning_scenario():
    """Render Ventilator Weaning scenario"""
    st.subheader("🔄 Ventilator Weaning Scenario")
    st.caption("Hướng dẫn cai máy thở")
    
    st.markdown("""
    **Cai máy thở** là quá trình giảm dần hỗ trợ máy thở để bệnh nhân tự thở.
    Cần đánh giá sẵn sàng và thực hiện SBT (Spontaneous Breathing Trial).
    """)
    
    st.markdown("---")
    
    # Step 1: Readiness Assessment
    with st.expander("📋 Bước 1: Đánh Giá Sẵn Sàng", expanded=True):
        st.markdown("""
        **Tiêu chí sẵn sàng:**
        
        **ABG:**
        - P/F ratio ≥200
        - pH 7.30-7.50
        - PaCO₂ 35-50 mmHg
        
        **Máy thở:**
        - PEEP ≤8 cmH₂O
        - FiO₂ ≤50%
        
        **Sinh tồn:**
        - HR 60-120 bpm
        - SBP 90-180 mmHg
        - Temp 36-38.5°C
        
        **Thần kinh:**
        - GCS ≥13
        - RASS -1 đến 0
        - Không có delirium nặng
        
        **Yếu tố khác:**
        - Không có nhiễm trùng huyết
        - Huyết động ổn định
        """)
        
        if st.button("🔄 Đánh Giá Sẵn Sàng", key="weaning_readiness"):
            st.session_state['weaning_scenario_tool'] = 'readiness'
    
    # Step 2: RSBI
    with st.expander("📊 Bước 2: RSBI (Rapid Shallow Breathing Index)", expanded=True):
        st.markdown("""
        **RSBI = RR / Vt (L)**
        
        **Đánh giá:**
        - **<105:** Tốt - Có thể cai máy thở
        - **105-130:** Trung bình - Cần theo dõi
        - **>130:** Kém - Khó cai máy thở
        
        **Lưu ý:**
        - Chỉ là một chỉ số
        - Cần đánh giá toàn diện
        """)
        
        if st.button("📊 Tính RSBI", key="weaning_rsbi"):
            st.session_state['weaning_scenario_tool'] = 'rsbi'
    
    # Step 3: SBT Protocol
    with st.expander("⏱️ Bước 3: SBT (Spontaneous Breathing Trial)", expanded=True):
        st.markdown("""
        **SBT Protocol:**
        
        **Chuẩn bị:**
        - Đánh giá sẵn sàng
        - Giảm sedation
        - Đảm bảo huyết động ổn định
        
        **Cài đặt SBT:**
        - Mode: CPAP 5-8 cmH₂O hoặc T-piece
        - FiO₂: Giữ nguyên hoặc tăng 10%
        - Thời gian: 30-120 phút
        
        **Theo dõi:**
        - Vital signs mỗi 15 phút
        - ABG sau 30-60 phút
        - Đánh giá sự thoải mái
        """)
        
        st.markdown("""
        **Tiêu chí thành công:**
        - RR <35 lần/phút
        - SpO₂ ≥88-90%
        - HR <140 bpm
        - SBP 90-180 mmHg
        - Không có signs of distress
        - pH ≥7.32
        
        **Tiêu chí thất bại:**
        - RR >35 lần/phút
        - SpO₂ <88-90%
        - HR >140 bpm
        - SBP <90 hoặc >180 mmHg
        - Signs of distress
        - pH <7.32
        """)
        
        if st.button("⏱️ Xem SBT Protocol", key="weaning_sbt"):
            st.session_state['weaning_scenario_tool'] = 'sbt'
    
    # Step 4: Extubation
    with st.expander("✅ Bước 4: Extubation", expanded=True):
        st.markdown("""
        **Sau SBT thành công:**
        
        **Đánh giá:**
        - Cough strength (mạnh)
        - Secretions (ít)
        - Gag reflex (có)
        - Mental status (tỉnh)
        
        **Chuẩn bị:**
        - NPO (nhịn ăn) 4-6 giờ
        - Có sẵn reintubation equipment
        - Team sẵn sàng
        
        **Sau extubation:**
        - Theo dõi sát 24-48 giờ
        - Hỗ trợ thở oxy
        - Đánh giá lại nếu cần
        """)
    
    st.markdown("---")
    st.info("""
    **💡 Tài liệu tham khảo:**
    - ATS/ERS Weaning Guidelines
    - SBT Protocol
    """)


def render_sedation_scenario():
    """Render Sedation scenario"""
    st.subheader("💤 Sedation Scenario")
    st.caption("Hướng dẫn an thần và giảm đau trong ICU")
    
    st.markdown("""
    **Sedation** trong ICU cần cân bằng giữa an thần đủ và tránh quá liều.
    Mục tiêu: **RASS -1 đến 0** (calm, alert).
    """)
    
    st.markdown("---")
    
    # Step 1: Assessment
    with st.expander("📋 Bước 1: Đánh Giá", expanded=True):
        st.markdown("""
        **Đánh giá mức độ an thần:**
        
        **RASS (Richmond Agitation-Sedation Scale):**
        - **+4:** Combative
        - **+3:** Very agitated
        - **+2:** Agitated
        - **+1:** Restless
        - **0:** Alert and calm (MỤC TIÊU)
        - **-1:** Drowsy
        - **-2:** Light sedation
        - **-3:** Moderate sedation
        - **-4:** Deep sedation
        - **-5:** Unarousable
        
        **Mục tiêu:** RASS -1 đến 0
        """)
        
        if st.button("📊 Tính RASS", key="sedation_rass"):
            st.session_state['sedation_scenario_tool'] = 'rass'
    
    # Step 2: Pain Assessment
    with st.expander("😣 Bước 2: Đánh Giá Đau", expanded=True):
        st.markdown("""
        **Đánh giá đau:**
        
        **Numeric Rating Scale (NRS):**
        - 0: Không đau
        - 1-3: Đau nhẹ
        - 4-6: Đau vừa
        - 7-10: Đau nặng
        
        **Mục tiêu:** NRS <4
        
        **Lưu ý:**
        - Đánh giá đau trước khi an thần
        - Điều trị đau trước
        - Đau không kiểm soát → tăng agitation
        """)
    
    # Step 3: Sedation Strategy
    with st.expander("💊 Bước 3: Chiến Lược An Thần", expanded=True):
        st.markdown("""
        **Lựa chọn thuốc:**
        
        **Propofol:**
        - An thần ngắn, dễ điều chỉnh
        - Liều: 5-50 mcg/kg/min
        - Lưu ý: Propofol infusion syndrome
        
        **Dexmedetomidine:**
        - An thần nhẹ, giữ ý thức
        - Liều: 0.2-1.5 mcg/kg/h
        - Lưu ý: Bradycardia, hypotension
        
        **Midazolam:**
        - An thần trung bình
        - Liều: 0.02-0.1 mg/kg/h
        - Lưu ý: Tích lũy, delirium
        
        **Lorazepam:**
        - An thần dài
        - Liều: 0.01-0.1 mg/kg/h
        - Lưu ý: Tích lũy
        """)
        
        if st.button("💤 Xem Sedation Calculator", key="sedation_calc"):
            st.session_state['sedation_scenario_tool'] = 'calculator'
    
    # Step 4: Analgesia
    with st.expander("💉 Bước 4: Giảm Đau", expanded=True):
        st.markdown("""
        **Opioids:**
        
        **Fentanyl:**
        - Tác dụng nhanh, ngắn
        - Liều: 0.5-2 mcg/kg/h
        - Ưu tiên cho ngắn hạn
        
        **Morphine:**
        - Tác dụng dài
        - Liều: 0.05-0.2 mg/kg/h
        - Lưu ý: Histamine release
        
        **Hydromorphone:**
        - Tác dụng trung bình
        - Liều: 0.5-2 mg/h
        - Ít tác dụng phụ hơn morphine
        """)
    
    # Step 5: Delirium Prevention
    with st.expander("🧠 Bước 5: Phòng Ngừa Delirium", expanded=True):
        st.markdown("""
        **CAM-ICU (Confusion Assessment Method):**
        
        **Tiêu chí:**
        1. Thay đổi ý thức cấp tính
        2. Không chú ý
        3. Rối loạn tư duy
        4. Thay đổi mức độ ý thức
        
        **≥2/4 tiêu chí** → Delirium
        
        **Phòng ngừa:**
        - Giảm sedation
        - Early mobilization
        - Sleep protocol
        - Tránh benzodiazepine
        """)
        
        if st.button("🧠 Tính CAM-ICU", key="sedation_cam"):
            st.session_state['sedation_scenario_tool'] = 'cam'
    
    # Step 6: Daily Sedation Interruption
    with st.expander("⏰ Bước 6: Ngừng An Thần Hàng Ngày", expanded=True):
        st.markdown("""
        **Daily Sedation Interruption (DSI):**
        
        **Mục đích:**
        - Giảm thời gian thở máy
        - Giảm delirium
        - Đánh giá sẵn sàng cai máy thở
        
        **Thực hiện:**
        - Ngừng sedation mỗi ngày
        - Đánh giá RASS, GCS
        - Nếu RASS >0 → Giảm liều
        - Nếu RASS <0 → Tăng liều
        """)
    
    st.markdown("---")
    st.info("""
    **💡 Tài liệu tham khảo:**
    - SCCM Sedation Guidelines
    - PADIS Guidelines (Pain, Agitation, Delirium)
    - RASS, CAM-ICU
    """)


def render_scenarios_calculator():
    """Main function to render clinical scenarios"""
    
    st.markdown("## 🎯 Clinical Scenarios - Tình Huống Lâm Sàng")
    st.markdown("""
    Hướng dẫn từng bước xử lý các tình huống lâm sàng phổ biến trong ICU:
    - Sepsis
    - ARDS
    - Shock
    - Ventilator Weaning
    - Sedation
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🦠 Sepsis",
        "🫁 ARDS",
        "💉 Shock",
        "🔄 Weaning",
        "💤 Sedation"
    ])
    
    with tab1:
        render_sepsis_scenario()
    
    with tab2:
        render_ards_scenario()
    
    with tab3:
        render_shock_scenario()
    
    with tab4:
        render_ventilator_weaning_scenario()
    
    with tab5:
        render_sedation_scenario()
    
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các hướng dẫn này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Tuân thủ hướng dẫn của Bộ Y tế, Bệnh viện
    - Tư vấn chuyên khoa khi cần
    """)

