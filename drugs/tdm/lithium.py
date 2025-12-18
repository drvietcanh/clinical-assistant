"""
Lithium TDM Calculator
Therapeutic Drug Monitoring cho Lithium
"""

import streamlit as st


def calculate_lithium_dose(weight_kg, indication="bipolar"):
    """
    Calculate Lithium starting dose
    
    Args:
        weight_kg: Body weight in kg
        indication: "bipolar" (acute) or "maintenance"
    
    Returns:
        dict with dose information
    """
    # Typical starting dose: 300-600 mg 2-3 times daily
    # Target level: 0.6-1.2 mEq/L (acute), 0.6-0.8 mEq/L (maintenance)
    
    if indication == "bipolar_acute":
        starting_dose_mg_kg = 10  # mg/kg/day, divided
    else:  # maintenance
        starting_dose_mg_kg = 7  # mg/kg/day
    
    total_dose_mg = starting_dose_mg_kg * weight_kg
    
    # Round to common tablet sizes (150, 300, 450, 600 mg)
    tablet_sizes = [150, 300, 450, 600]
    
    # Try to divide into 2-3 doses
    daily_dose = round(total_dose_mg / 300) * 300  # Round to nearest 300
    if daily_dose < 300:
        daily_dose = 300
    
    # Divide into 2-3 times
    if daily_dose >= 900:
        frequency = 3
        dose_per_time = round(daily_dose / 3 / 150) * 150  # Round to 150mg increments
    else:
        frequency = 2
        dose_per_time = round(daily_dose / 2 / 150) * 150
    
    return {
        "daily_dose_mg": daily_dose,
        "dose_per_time_mg": dose_per_time,
        "frequency": frequency,
        "starting_dose_mg_per_kg": starting_dose_mg_kg,
        "indication": indication
    }


def interpret_lithium_level(level_mEq_L, indication="bipolar", time_since_dose_hours=12):
    """
    Interpret Lithium serum level
    
    Args:
        level_mEq_L: Lithium level in mEq/L (or mmol/L)
        indication: "bipolar_acute", "bipolar_maintenance", or "depression"
        time_since_dose_hours: Hours since last dose (for trough)
    
    Returns:
        dict with interpretation
    """
    if indication == "bipolar_acute":
        target_min = 0.8
        target_max = 1.2
        therapeutic_range = "0.8-1.2 mEq/L"
    elif indication == "bipolar_maintenance":
        target_min = 0.6
        target_max = 0.8
        therapeutic_range = "0.6-0.8 mEq/L"
    else:  # depression
        target_min = 0.6
        target_max = 1.0
        therapeutic_range = "0.6-1.0 mEq/L"
    
    # Check if trough level (should be 12 hours post-dose)
    if time_since_dose_hours < 10:
        trough_warning = "⚠️ Mẫu lấy < 10 giờ sau liều - có thể không phải trough level đúng."
    elif time_since_dose_hours > 14:
        trough_warning = "⚠️ Mẫu lấy > 14 giờ sau liều - có thể đã quá trough."
    else:
        trough_warning = None
    
    if level_mEq_L < target_min:
        status = "subtherapeutic"
        level_text = "⬇️ Dưới mục tiêu"
        recommendation = f"Nồng độ thấp (< {target_min} mEq/L). Cân nhắc tăng liều hoặc kiểm tra compliance."
        color = "info"
    elif level_mEq_L <= target_max:
        status = "therapeutic"
        level_text = "✅ Trong mục tiêu điều trị"
        recommendation = f"Nồng độ trong khoảng điều trị ({therapeutic_range}). Tiếp tục liều hiện tại."
        color = "success"
    elif level_mEq_L <= 1.5:
        status = "supratherapeutic"
        level_text = "⚠️ Trên mục tiêu"
        recommendation = "Nồng độ cao (1.2-1.5 mEq/L). Theo dõi triệu chứng độc tính. Cân nhắc giảm liều."
        color = "warning"
    else:
        status = "toxic"
        level_text = "🚨 ĐỘC TÍNH - Nguy hiểm"
        recommendation = "Nồng độ độc tính (> 1.5 mEq/L)! Giảm liều hoặc ngừng ngay, theo dõi triệu chứng độc tính."
        color = "error"
    
    return {
        "status": status,
        "level_text": level_text,
        "therapeutic_range": therapeutic_range,
        "recommendation": recommendation,
        "color": color,
        "current_level": level_mEq_L,
        "trough_warning": trough_warning
    }


def render_lithium_tdm():
    """Render Lithium TDM Calculator Interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💊 Lithium TDM Calculator</h2>
    <p style='text-align: center;'><em>Therapeutic Drug Monitoring & Dose Adjustment</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Lithium TDM:**
    - Mục tiêu: 0.6-0.8 mEq/L (duy trì), 0.8-1.2 mEq/L (điều trị cấp)
    - Thời điểm lấy mẫu: 12 giờ sau liều cuối (trough) - QUAN TRỌNG!
    - Half-life: 18-36 giờ
    - Độc tính: > 1.5 mEq/L
    - **Lưu ý:** Lithium có TI (therapeutic index) hẹp - cần theo dõi chặt chẽ
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2 = st.tabs(["🧮 Tính liều", "📊 Giải thích nồng độ"])
    
    with tab1:
        st.markdown("### 📋 Thông số bệnh nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=40,
                max_value=150,
                value=50,
                step=1,
                format="%d",
                key="lithium_weight"
            )
            
            indication = st.selectbox(
                "Chỉ định:",
                ["Rối loạn lưỡng cực - Điều trị cấp", "Rối loạn lưỡng cực - Duy trì", "Trầm cảm (augmentation)"],
                key="lithium_indication"
            )
        
        with col2:
            age = st.number_input(
                "Tuổi (năm)",
                min_value=18,
                max_value=100,
                value=45,
                step=1,
                format="%d",
                key="lithium_age"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=30,
                max_value=150,
                value=90,
                step=5,
                format="%d",
                key="lithium_crcl",
                help="Lithium thải qua thận - CrCl quan trọng!"
            )
        
        # Check for contraindications
        st.markdown("#### ⚠️ Kiểm tra Chống chỉ định")
        has_ckd = crcl < 60
        is_elderly = age >= 65
        
        if has_ckd:
            st.error(f"🚨 **Suy thận:** CrCl = {crcl:.0f} mL/min. Lithium CHỐNG CHỈ ĐỊNH tương đối. Thận trọng tuyệt đối!")
        
        if is_elderly:
            st.warning("⚠️ **Người già (≥65):** Cần liều thấp hơn, theo dõi sát hơn.")
        
        st.markdown("---")
        
        if st.button("🧮 Tính liều Lithium", type="primary", use_container_width=True):
            indication_code = "bipolar_acute" if "Điều trị cấp" in indication else ("bipolar_maintenance" if "Duy trì" in indication else "depression")
            
            # Adjust for elderly or renal impairment
            result = calculate_lithium_dose(weight, indication_code)
            
            if has_ckd or is_elderly:
                # Reduce dose by 25-50%
                result['daily_dose_mg'] = int(result['daily_dose_mg'] * 0.6)  # 40% reduction
                result['daily_dose_mg'] = round(result['daily_dose_mg'] / 150) * 150
                result['dose_per_time_mg'] = round(result['daily_dose_mg'] / result['frequency'] / 150) * 150
                adjustment_note = "⚠️ Đã giảm liều do suy thận/người già"
            else:
                adjustment_note = None
            
            st.markdown("### 💊 Kết quả tính liều")
            
            if adjustment_note:
                st.warning(adjustment_note)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều hàng ngày",
                    f"{result['daily_dose_mg']:.0f} mg",
                    help=f"{result['starting_dose_mg_per_kg']:.1f} mg/kg/ngày"
                )
            
            with col2:
                freq_text = f"{result['frequency']} lần/ngày"
                if result['frequency'] == 2:
                    freq_text = "2 lần/ngày (BID)"
                elif result['frequency'] == 3:
                    freq_text = "3 lần/ngày (TID)"
                
                st.metric("Tần suất", freq_text)
            
            with col3:
                st.metric(
                    "Liều mỗi lần",
                    f"{result['dose_per_time_mg']:.0f} mg"
                )
            
            st.markdown("---")
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Liều khởi đầu:** {result['daily_dose_mg']:.0f} mg/ngày chia {result['frequency']} lần
            (Mỗi lần: {result['dose_per_time_mg']:.0f} mg)
            
            **Lưu ý:**
            - Bắt đầu với liều này, tăng từng bước
            - Theo dõi nồng độ sau 5-7 ngày (steady state)
            - **BẮT BUỘC:** Lấy mẫu đúng 12 giờ sau liều (trough level)
            - Kiểm tra CrCl, TSH, T4, Creatinine, Na+ trước khi bắt đầu
            """)
            
            st.markdown("---")
            st.markdown("### 🎯 Mục tiêu TDM")
            
            if indication_code == "bipolar_acute":
                target_range = "0.8-1.2 mEq/L"
                target_note = "Điều trị cấp - nồng độ cao hơn"
            elif indication_code == "bipolar_maintenance":
                target_range = "0.6-0.8 mEq/L"
                target_note = "Duy trì - nồng độ thấp hơn để giảm độc tính"
            else:
                target_range = "0.6-1.0 mEq/L"
                target_note = "Trầm cảm augmentation"
            
            st.info(f"""
            **Mục tiêu nồng độ: {target_range}**
            ({target_note})
            
            **Thời điểm lấy mẫu:**
            - **QUAN TRỌNG:** Phải lấy đúng 12 giờ sau liều cuối (trough)
            - Lấy mẫu buổi sáng trước liều tiếp theo (nếu uống tối)
            - Lần đầu: Sau liều 5-7 (đạt steady state)
            
            **Tần suất theo dõi:**
            - Lần đầu: Sau 5-7 ngày
            - Khi ổn định: Mỗi 3-6 tháng
            - Khi thay đổi liều: Sau 5-7 ngày
            - Khi có triệu chứng độc tính: Ngay lập tức
            - Khi thay đổi chức năng thận: Ngay lập tức
            """)
            
            st.markdown("---")
            st.markdown("### 📋 Monitoring Trước Khi Bắt Đầu")
            
            st.warning("""
            **Cần kiểm tra TRƯỚC khi bắt đầu Lithium:**
            
            1. **Chức năng thận:**
               - CrCl/eGFR
               - Creatinine
               - Nếu CrCl < 60: Chống chỉ định tương đối
            
            2. **Chức năng tuyến giáp:**
               - TSH, Free T4
               - Lithium có thể gây suy giáp
            
            3. **Điện giải:**
               - Na+ (natri máu)
               - Lithium và Na+ có tương quan nghịch
            
            4. **ECG (nếu có bệnh tim):**
               - Tìm bất thường nhịp tim
            """)
    
    with tab2:
        st.markdown("### 📊 Giải thích nồng độ Lithium")
        
        col1, col2 = st.columns(2)
        
        with col1:
            level = st.number_input(
                "Nồng độ Lithium (mEq/L hoặc mmol/L)",
                min_value=0.0,
                max_value=3.0,
                value=0.7,
                step=0.1,
                format="%.2f",
                key="lithium_level"
            )
            
            indication_interp = st.selectbox(
                "Chỉ định:",
                ["Rối loạn lưỡng cực - Điều trị cấp", "Rối loạn lưỡng cực - Duy trì", "Trầm cảm"],
                key="lithium_indication_interp"
            )
        
        with col2:
            time_since_dose = st.number_input(
                "Thời gian sau liều cuối (giờ)",
                min_value=0.0,
                max_value=24.0,
                value=12.0,
                step=1.0,
                format="%.1f",
                key="lithium_time",
                help="QUAN TRỌNG: Phải là 12 giờ để đúng trough level"
            )
            
            if abs(time_since_dose - 12) > 1:
                st.error(f"⚠️ Mẫu lấy không đúng thời điểm! Trough level phải lấy đúng 12 giờ sau liều (hiện tại: {time_since_dose:.1f} giờ)")
        
        st.markdown("---")
        
        if st.button("📊 Giải thích nồng độ", type="primary", use_container_width=True):
            indication_code = "bipolar_acute" if "Điều trị cấp" in indication_interp else ("bipolar_maintenance" if "Duy trì" in indication_interp else "depression")
            
            interpretation = interpret_lithium_level(level, indication_code, time_since_dose)
            
            st.markdown("### 📈 Kết quả Giải thích")
            
            if interpretation.get('trough_warning'):
                st.warning(interpretation['trough_warning'])
            
            # Display status
            if interpretation['color'] == 'success':
                st.success(f"**{interpretation['level_text']}**")
            elif interpretation['color'] == 'info':
                st.info(f"**{interpretation['level_text']}**")
            elif interpretation['color'] == 'warning':
                st.warning(f"**{interpretation['level_text']}**")
            else:
                st.error(f"**{interpretation['level_text']}**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "Nồng độ hiện tại",
                    f"{interpretation['current_level']:.2f} mEq/L"
                )
            
            with col2:
                st.metric(
                    "Mục tiêu điều trị",
                    interpretation['therapeutic_range']
                )
            
            st.markdown("---")
            st.markdown(f"### 💡 Khuyến nghị")
            
            if interpretation['color'] == 'error':
                st.error(interpretation['recommendation'])
            elif interpretation['color'] == 'warning':
                st.warning(interpretation['recommendation'])
            elif interpretation['color'] == 'info':
                st.info(interpretation['recommendation'])
            else:
                st.success(interpretation['recommendation'])
            
            # Toxicity management
            if interpretation['status'] == "toxic":
                st.markdown("---")
                st.error("""
                **🚨 XỬ TRÍ ĐỘC TÍNH LITHIUM:**
                
                **Triệu chứng độc tính:**
                - Nôn, tiêu chảy
                - Run tay nặng
                - Lú lẫn
                - Co giật
                - Hôn mê (với nồng độ rất cao)
                
                **Xử trí:**
                1. **Ngừng lithium ngay**
                2. **Bù dịch:** NS 0.9% để tăng thải lithium
                3. **Theo dõi:**
                   - Nồng độ lithium (mỗi 12-24h)
                   - Điện giải (Na+, K+)
                   - Creatinine, CrCl
                   - Triệu chứng thần kinh
                
                3. **Hemodialysis:**
                   - Chỉ định: Nồng độ > 2.5 mEq/L hoặc triệu chứng nặng
                   - Lithium thải tốt qua HD
                
                4. **Theo dõi nồng độ:** Có thể tăng lại sau HD do redistribution
                """)
    
    # Drug interactions
    st.markdown("---")
    with st.expander("⚠️ Tương tác & Lưu ý"):
        st.markdown("""
        **Thuốc TĂNG nồng độ Lithium:**
        - Diuretics (thiazide): Tăng nguy cơ độc tính
        - ACE inhibitors/ARBs
        - NSAIDs
        
        **Yếu tố ảnh hưởng:**
        - **Natri máu:** Giảm Na+ → Tăng Li+ (nguy hiểm!)
        - **Mất nước:** Tăng nồng độ
        - **Suy thận:** Tăng nồng độ, tích lũy
        
        **Theo dõi định kỳ:**
        - Creatinine, CrCl mỗi 3-6 tháng
        - TSH, T4 mỗi 6-12 tháng
        - Lithium level mỗi 3-6 tháng (khi ổn định)
        """)
    
    # References
    st.markdown("---")
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        - **APA Guidelines - Bipolar Disorder**
        - **Half-life:** 18-36 giờ
        - **Therapeutic index:** Hẹp - cần theo dõi chặt chẽ
        - **Elimination:** 100% qua thận (không chuyển hóa)
        """)

