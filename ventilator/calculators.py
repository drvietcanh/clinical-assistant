"""
Ventilator Calculators
ARDSNet and initial ventilator settings
"""

import streamlit as st


def render_ardsnet():
    """ARDSNet Tidal Volume Calculator"""
    st.subheader("🫁 ARDSNet - Tidal Volume")
    st.caption("Lung-Protective Ventilation Strategy")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="ardsnet_sex"
        )
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=100,
            max_value=220,
            value=170,
            step=1,
            help="Chiều cao thực tế của bệnh nhân"
        )
        
        st.markdown("---")
        st.markdown("### ⚙️ Tham Số Máy Thở Hiện Tại")
        
        current_vt = st.number_input(
            "Vt hiện tại (mL)",
            min_value=0,
            max_value=1000,
            value=0,
            step=10,
            help="Để trống nếu chưa đặt máy thở"
        )
        
        if st.button("🧮 Tính ARDSNet", type="primary", key="ardsnet_calc"):
            # Calculate PBW (Predicted Body Weight)
            if sex == "Nam":
                pbw = 50 + 0.91 * (height - 152.4)
            else:  # Nữ
                pbw = 45.5 + 0.91 * (height - 152.4)
            
            pbw = round(pbw, 1)
            
            # Calculate target Vt (6-8 mL/kg PBW)
            vt_low = pbw * 6
            vt_target = pbw * 6  # Start at 6 mL/kg
            vt_high = pbw * 8
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                st.metric("PBW", f"{pbw} kg")
                st.metric("Vt Mục Tiêu", f"{vt_target:.0f} mL")
                
                st.info(f"""
                **Khoảng an toàn:**
                - Min: {vt_low:.0f} mL (6 mL/kg)
                - Max: {vt_high:.0f} mL (8 mL/kg)
                """)
            
            st.markdown("### 💡 Khuyến Cáo")
            
            if current_vt > 0:
                if current_vt > vt_high:
                    st.error(f"""
                    ⚠️ **Vt hiện tại QUÁ CAO!**
                    
                    - Hiện tại: {current_vt} mL
                    - Mục tiêu: {vt_target:.0f} mL
                    - Giảm: {current_vt - vt_target:.0f} mL
                    
                    **Hành động:**
                    - Giảm Vt từ từ (50-100 mL mỗi lần)
                    - Theo dõi pH, PaCO2
                    - Cho phép hypercapnia nếu cần
                    """)
                elif current_vt < vt_low:
                    st.warning(f"""
                    ⚠️ **Vt hiện tại thấp**
                    
                    - Hiện tại: {current_vt} mL
                    - Mục tiêu: {vt_target:.0f} mL
                    - Có thể tăng thêm: {vt_target - current_vt:.0f} mL
                    """)
                else:
                    st.success(f"""
                    ✅ **Vt trong khoảng an toàn**
                    
                    - Hiện tại: {current_vt} mL
                    - Mục tiêu: {vt_target:.0f} mL
                    - Tiếp tục theo dõi
                    """)
            
            st.markdown("---")
            st.markdown("### 📋 ARDSNet Protocol")
            
            st.info(f"""
            **Thông số khởi đầu:**
            - **Vt:** {vt_target:.0f} mL (6 mL/kg PBW)
            - **RR:** 20-35 (điều chỉnh theo pH)
            - **PEEP/FiO2:** Theo bảng PEEP/FiO2
            - **I:E:** 1:1 đến 1:3
            
            **Mục tiêu:**
            - **Plateau Pressure:** ≤30 cmH2O
            - **pH:** 7.30-7.45
            - **SpO2:** 88-95%
            - **PaO2:** 55-80 mmHg
            """)
            
            st.warning("""
            **⚠️ Lưu ý:**
            - Ưu tiên giới hạn áp lực
            - Cho phép hypercapnia (pH ≥7.15)
            - Điều chỉnh PEEP theo bảng
            - Theo dõi sát compliance, driving pressure
            """)
            
            with st.expander("📐 Công Thức PBW"):
                st.markdown(f"""
                **Predicted Body Weight (PBW):**
                
                **Nam:**
                ```
                PBW = 50 + 0.91 × (Height - 152.4)
                    = 50 + 0.91 × ({height} - 152.4)
                    = {pbw} kg
                ```
                
                **Nữ:**
                ```
                PBW = 45.5 + 0.91 × (Height - 152.4)
                ```
                
                **Target Vt:**
                ```
                Vt = 6 mL/kg × PBW
                   = 6 × {pbw}
                   = {vt_target:.0f} mL
                ```
                
                **Reference:**
                ARDSNet. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med. 2000;342(18):1301-1308.
                """)


def render_initial_settings():
    """Initial Ventilator Settings Calculator"""
    st.subheader("⚙️ Cài Đặt Ban Đầu Máy Thở")
    st.caption("Thông Số Khởi Đầu Theo Bệnh Lý")
    
    st.info("""
    **Công cụ tính toán thông số máy thở ban đầu dựa trên:**
    - Bệnh lý của bệnh nhân
    - Chiều cao, giới tính (để tính PBW)
    - Nguyên tắc lung-protective ventilation
    """)
    
    st.markdown("---")
    
    # Patient information
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="initial_sex"
        )
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=100,
            max_value=220,
            value=170,
            step=1,
            help="Chiều cao thực tế của bệnh nhân",
            key="initial_height"
        )
        
        # Calculate PBW
        if sex == "Nam":
            pbw = 50 + 0.91 * (height - 152.4)
        else:  # Nữ
            pbw = 45.5 + 0.91 * (height - 152.4)
        pbw = round(pbw, 1)
        
        st.markdown("---")
        
        st.markdown("### 🩺 Chọn Bệnh Lý")
        
        condition = st.selectbox(
            "Bệnh lý chính:",
            [
                "ARDS / ALI",
                "COPD",
                "Asthma",
                "Normal Lungs",
                "Neuromuscular",
                "Post-Operative"
            ],
            key="initial_condition"
        )
        
        # Additional context
        st.markdown("---")
        st.markdown("### 📊 Tình Trạng Hiện Tại")
        
        severity = st.radio(
            "Mức độ nghiêm trọng:",
            ["Nhẹ - Trung bình", "Nặng"],
            horizontal=True,
            key="initial_severity"
        )
        
        has_hypoxemia = st.checkbox(
            "Có giảm oxy máu nặng (SpO2 <90% với O₂ cao)",
            key="initial_hypoxemia"
        )
    
    with col2:
        st.markdown("### 📊 PBW")
        st.metric("Predicted Body Weight", f"{pbw} kg")
        st.caption(f"Chiều cao: {height} cm ({sex})")
    
    st.markdown("---")
    
    # Calculate settings based on condition
    if st.button("🧮 Tính Thông Số Máy Thở", type="primary", key="initial_calc"):
        
        # Initialize settings dictionary
        settings = {}
        
        # Calculate based on condition
        if condition == "ARDS / ALI":
            # ARDSNet protocol
            settings = {
                "mode": "AC/VC (Volume Control)",
                "vt": round(pbw * 6, 0),
                "vt_per_kg": "6 mL/kg PBW",
                "rr": "20-35",
                "rr_note": "Điều chỉnh để pH 7.30-7.45",
                "peep": "5-10" if not has_hypoxemia else "10-15",
                "peep_note": "Theo bảng PEEP/FiO2",
                "fio2": "0.4-0.6" if not has_hypoxemia else "0.6-1.0",
                "ie_ratio": "1:1 đến 1:3",
                "flow": "60 L/min",
                "trigger": "-2 cmH2O",
                "target_spo2": "88-95%",
                "target_pao2": "55-80 mmHg",
                "plateau_pressure": "≤30 cmH2O",
                "driving_pressure": "≤15 cmH2O",
                "strategy": "Lung-protective ventilation",
                "notes": [
                    "Ưu tiên giới hạn áp lực (plateau ≤30 cmH2O)",
                    "Cho phép hypercapnia nhẹ (pH ≥7.15)",
                    "PEEP theo bảng PEEP/FiO2 ARDSNet",
                    "Theo dõi driving pressure (≤15 cmH2O)",
                    "Cân nhắc prone positioning nếu nặng"
                ]
            }
        
        elif condition == "COPD":
            # COPD: Allow longer expiratory time, higher PEEP to prevent auto-PEEP
            settings = {
                "mode": "AC/VC hoặc SIMV",
                "vt": round(pbw * 6, 0),
                "vt_per_kg": "6-8 mL/kg PBW",
                "rr": "10-14",
                "rr_note": "Thấp để đảm bảo thời gian thở ra đủ",
                "peep": "5-8",
                "peep_note": "Vừa đủ để chống auto-PEEP, không quá cao",
                "fio2": "0.3-0.5",
                "ie_ratio": "1:3 đến 1:4",
                "flow": "60-80 L/min",
                "trigger": "-2 cmH2O",
                "target_spo2": "88-92%",
                "target_pao2": "55-80 mmHg",
                "plateau_pressure": "≤30 cmH2O",
                "auto_peep": "Theo dõi auto-PEEP",
                "strategy": "Tránh hyperinflation động, đảm bảo thở ra đủ",
                "notes": [
                    "Quan trọng: Thời gian thở ra đủ (I:E ≥1:3)",
                    "RR thấp (10-14) để tránh auto-PEEP",
                    "PEEP vừa phải (5-8) để chống auto-PEEP",
                    "Theo dõi auto-PEEP (plateau - PEEP)",
                    "Tránh hyperoxia (FiO2 thấp nếu có thể)"
                ]
            }
        
        elif condition == "Asthma":
            # Asthma: Similar to COPD, focus on long expiratory time
            settings = {
                "mode": "AC/VC hoặc SIMV",
                "vt": round(pbw * 6, 0),
                "vt_per_kg": "6-8 mL/kg PBW",
                "rr": "8-12",
                "rr_note": "Rất thấp để đảm bảo thời gian thở ra đủ",
                "peep": "0-5",
                "peep_note": "Cẩn thận với PEEP trong asthma",
                "fio2": "0.4-0.6",
                "ie_ratio": "1:4 đến 1:5",
                "flow": "80-100 L/min",
                "trigger": "-2 cmH2O",
                "target_spo2": ">90%",
                "target_pao2": ">60 mmHg",
                "plateau_pressure": "≤30 cmH2O",
                "auto_peep": "Theo dõi auto-PEEP chặt chẽ",
                "strategy": "Permissive hypercapnia, long expiratory time",
                "notes": [
                    "Quan trọng nhất: Thời gian thở ra dài (I:E ≥1:4)",
                    "RR rất thấp (8-12) để tránh hyperinflation",
                    "PEEP thấp hoặc 0 (tránh làm tăng áp lực)",
                    "Cho phép hypercapnia (pH có thể xuống 7.0-7.2)",
                    "Theo dõi auto-PEEP chặt chẽ",
                    "Điều trị nguyên nhân: Bronchodilators, steroids"
                ]
            }
        
        elif condition == "Normal Lungs":
            # Normal lungs: Standard settings
            settings = {
                "mode": "AC/VC hoặc SIMV",
                "vt": round(pbw * 8, 0),
                "vt_per_kg": "8-10 mL/kg PBW",
                "rr": "12-16",
                "rr_note": "Theo nhu cầu bệnh nhân",
                "peep": "5",
                "peep_note": "PEEP thông thường",
                "fio2": "0.4-0.5",
                "ie_ratio": "1:2",
                "flow": "40-60 L/min",
                "trigger": "-2 cmH2O",
                "target_spo2": ">94%",
                "target_pao2": ">80 mmHg",
                "plateau_pressure": "≤30 cmH2O",
                "strategy": "Thông số chuẩn, lung-protective",
                "notes": [
                    "Thông số chuẩn cho bệnh nhân phổi bình thường",
                    "Vẫn áp dụng lung-protective (Vt ≤8-10 mL/kg)",
                    "Theo dõi compliance, plateau pressure",
                    "Cân nhắc giảm hỗ trợ nếu có thể"
                ]
            }
        
        elif condition == "Neuromuscular":
            # Neuromuscular: Full support, normal settings
            settings = {
                "mode": "AC/VC hoặc SIMV",
                "vt": round(pbw * 8, 0),
                "vt_per_kg": "8-10 mL/kg PBW",
                "rr": "12-16",
                "rr_note": "Đủ để đảm bảo thông khí",
                "peep": "5-8",
                "peep_note": "PEEP thông thường",
                "fio2": "0.3-0.4",
                "ie_ratio": "1:2",
                "flow": "40-60 L/min",
                "trigger": "-2 cmH2O",
                "target_spo2": ">94%",
                "target_pao2": ">80 mmHg",
                "plateau_pressure": "≤30 cmH2O",
                "strategy": "Full ventilatory support",
                "notes": [
                    "Phổi thường bình thường → thông số chuẩn",
                    "Cần hỗ trợ thở đầy đủ (bệnh nhân không tự thở được)",
                    "Theo dõi áp lực (thường không có vấn đề về compliance)",
                    "Cân nhắc trach nếu thở máy kéo dài"
                ]
            }
        
        elif condition == "Post-Operative":
            # Post-operative: Quick wean, standard settings
            settings = {
                "mode": "SIMV + PS hoặc AC/VC",
                "vt": round(pbw * 8, 0),
                "vt_per_kg": "8-10 mL/kg PBW",
                "rr": "12-16",
                "rr_note": "Hỗ trợ đủ để chống lại tác dụng của thuốc mê",
                "peep": "5-8",
                "peep_note": "PEEP để phòng ngừa xẹp phổi",
                "fio2": "0.4-0.5",
                "ie_ratio": "1:2",
                "flow": "40-60 L/min",
                "trigger": "-2 cmH2O",
                "target_spo2": ">94%",
                "target_pao2": ">80 mmHg",
                "plateau_pressure": "≤30 cmH2O",
                "strategy": "Hỗ trợ tạm thời, wean sớm",
                "notes": [
                    "Thông số chuẩn cho hậu phẫu",
                    "PEEP để phòng ngừa atelectasis",
                    "Wean sớm khi bệnh nhân tỉnh và ổn định",
                    "Theo dõi chảy máu, đau (ảnh hưởng thở)"
                ]
            }
        
        # Display results
        st.markdown("---")
        st.markdown("### 📊 Thông Số Đề Xuất")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### ⚙️ Mode & Tidal Volume")
            st.metric("Mode", settings["mode"])
            st.metric("Vt", f"{settings['vt']:.0f} mL")
            st.caption(f"({settings['vt_per_kg']})")
            
            if "auto_peep" in settings:
                st.warning(f"**{settings['auto_peep']}**")
        
        with col2:
            st.markdown("#### 💨 Rate & PEEP")
            st.metric("RR", settings["rr"])
            st.caption(settings.get("rr_note", ""))
            st.metric("PEEP", settings["peep"] + " cmH2O")
            st.caption(settings.get("peep_note", ""))
        
        with col3:
            st.markdown("#### 🌬️ Oxygen & I:E")
            st.metric("FiO2", settings["fio2"])
            st.metric("I:E", settings["ie_ratio"])
            st.metric("Flow", settings.get("flow", "40-60 L/min"))
            st.caption(f"Trigger: {settings.get('trigger', '-2 cmH2O')}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎯 Mục Tiêu")
            st.success(f"""
            **Oxy hóa:**
            - SpO2: {settings['target_spo2']}
            - PaO2: {settings['target_pao2']}
            
            **Áp lực:**
            - Plateau: {settings.get('plateau_pressure', '≤30 cmH2O')}
            """)
            
            if "driving_pressure" in settings:
                st.info(f"Driving Pressure: {settings['driving_pressure']}")
        
        with col2:
            st.markdown("#### 📋 Chiến Lược")
            st.info(f"**{settings['strategy']}**")
        
        st.markdown("---")
        st.markdown("### ⚠️ Lưu Ý Quan Trọng")
        
        for i, note in enumerate(settings["notes"], 1):
            st.markdown(f"{i}. {note}")
        
        st.markdown("---")
        
        with st.expander("📚 Thông Tin Thêm"):
            st.markdown(f"""
            **Bệnh lý:** {condition}
            **PBW:** {pbw} kg (Chiều cao: {height} cm, {sex})
            **Mức độ:** {severity}
            **Giảm oxy máu:** {"Có" if has_hypoxemia else "Không"}
            
            **Lưu ý chung:**
            - Các thông số này là khởi đầu, cần điều chỉnh theo đáp ứng
            - Theo dõi ABG, compliance, plateau pressure
            - Đánh giá lại sau 30-60 phút
            - Cân nhắc wean khi bệnh nhân cải thiện
            """)
    
    st.markdown("---")
    
    with st.expander("📚 Nguyên Tắc Chung"):
        st.markdown("""
        **Lung-Protective Ventilation:**
        - Vt ≤8 mL/kg PBW (≤6 mL/kg cho ARDS)
        - Plateau pressure ≤30 cmH2O
        - Driving pressure ≤15 cmH2O
        - Cho phép hypercapnia nhẹ nếu cần (pH ≥7.15)
        
        **PEEP:**
        - Tránh atelectasis (normal lungs)
        - Tối ưu hóa recruitment (ARDS)
        - Tránh hyperinflation (COPD/Asthma)
        
        **FiO2:**
        - Bắt đầu thấp, tăng dần nếu cần
        - Tránh hyperoxia (FiO2 không cần thiết cao)
        
        **I:E Ratio:**
        - 1:2 cho phổi bình thường
        - 1:3-1:4 cho COPD
        - 1:4-1:5 cho Asthma (thở ra dài)
        
        **Reference:**
        - ARDSNet Protocol (2000)
        - ATS/ERS Guidelines on Mechanical Ventilation
        - Surviving Sepsis Campaign 2021
        """)

