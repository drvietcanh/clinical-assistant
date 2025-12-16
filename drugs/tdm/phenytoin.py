"""
Phenytoin TDM Calculator
Therapeutic Drug Monitoring cho Phenytoin
"""

import streamlit as st


def calculate_phenytoin_loading_dose(weight_kg, indication="seizure"):
    """
    Calculate Phenytoin loading dose
    
    Args:
        weight_kg: Body weight in kg
        indication: "seizure" or "status_epilepticus"
    
    Returns:
        dict with loading dose
    """
    if indication == "status_epilepticus":
        loading_dose_mg_kg = 20  # mg/kg for status
    else:
        loading_dose_mg_kg = 15  # mg/kg for routine loading
    
    total_loading_mg = loading_dose_mg_kg * weight_kg
    
    # Common IV formulation: 50 mg/mL
    # Common PO formulation: 100 mg capsules
    iv_volume_ml = total_loading_mg / 50
    po_capsules = round(total_loading_mg / 100)
    
    return {
        "loading_dose_mg": total_loading_mg,
        "loading_dose_mg_per_kg": loading_dose_mg_kg,
        "iv_volume_ml": iv_volume_ml,
        "po_capsules": po_capsules,
        "indication": indication
    }


def calculate_phenytoin_maintenance_dose(weight_kg, current_level_mg_l=None, target_level_mg_l=15):
    """
    Calculate Phenytoin maintenance dose
    Uses Michaelis-Menten kinetics
    
    Args:
        weight_kg: Body weight
        current_level_mg_l: Current phenytoin level (if available)
        target_level_mg_l: Target level (usually 10-20 mg/L)
    
    Returns:
        dict with maintenance dose
    """
    # Typical maintenance: 5-7 mg/kg/day for adults
    # Divided into 2-3 doses
    
    base_dose_mg_per_kg = 5.5  # Average
    
    if current_level_mg_l:
        # Adjust based on current level
        if current_level_mg_l < 10:
            base_dose_mg_per_kg = 6.5  # Increase
        elif current_level_mg_l > 20:
            base_dose_mg_per_kg = 4.5  # Decrease
    
    maintenance_dose_mg = base_dose_mg_per_kg * weight_kg
    
    # Round to common tablet sizes (100 mg tablets)
    maintenance_dose_mg_rounded = round(maintenance_dose_mg / 100) * 100
    
    # Frequency: Usually divided 2-3 times daily
    if maintenance_dose_mg_rounded >= 300:
        frequency = 3  # TID
    else:
        frequency = 2  # BID
    
    dose_per_time = maintenance_dose_mg_rounded / frequency
    
    return {
        "maintenance_dose_mg": maintenance_dose_mg_rounded,
        "maintenance_dose_mg_per_kg": base_dose_mg_per_kg,
        "frequency": frequency,
        "dose_per_time": dose_per_time,
        "target_level": target_level_mg_l
    }


def adjust_phenytoin_dose(current_dose_mg, current_level_mg_l, target_level_mg_l=15):
    """
    Adjust Phenytoin dose based on current level (Michaelis-Menten)
    
    Args:
        current_dose_mg: Current daily dose (mg)
        current_level_mg_l: Current phenytoin level (mg/L)
        target_level_mg_l: Target level (mg/L)
    
    Returns:
        dict with adjusted dose
    """
    # Simplified Michaelis-Menten adjustment
    # Vmax ~ 7 mg/kg/day, Km ~ 4-5 mg/L
    
    if current_level_mg_l <= 0 or current_level_mg_l > 40:
        return {
            "error": "Nồng độ không hợp lệ. Kiểm tra lại."
        }
    
    # Calculate adjustment factor
    # For linear range (level < 10): linear adjustment
    # For non-linear range (level > 10): smaller adjustments needed
    
    if current_level_mg_l < 10:
        # Linear range: simple proportional adjustment
        adjustment_factor = target_level_mg_l / current_level_mg_l
    else:
        # Non-linear range: smaller adjustment needed
        # Simplified: use 0.7x of linear adjustment
        linear_factor = target_level_mg_l / current_level_mg_l
        adjustment_factor = 1 + (linear_factor - 1) * 0.7
    
    new_dose_mg = current_dose_mg * adjustment_factor
    
    # Round to tablet sizes (50 or 100 mg)
    if new_dose_mg < 100:
        new_dose_mg_rounded = round(new_dose_mg / 50) * 50
    else:
        new_dose_mg_rounded = round(new_dose_mg / 100) * 100
    
    # Safety limits
    if new_dose_mg_rounded > 600:
        new_dose_mg_rounded = 600
        warning = "⚠️ Liều tối đa 600mg/ngày. Cân nhắc phenytoin alternatives."
    elif new_dose_mg_rounded < 100:
        new_dose_mg_rounded = 100
        warning = "⚠️ Liều tối thiểu 100mg/ngày."
    else:
        warning = None
    
    return {
        "current_dose_mg": current_dose_mg,
        "current_level_mg_l": current_level_mg_l,
        "target_level_mg_l": target_level_mg_l,
        "new_dose_mg": new_dose_mg_rounded,
        "adjustment_factor": adjustment_factor,
        "warning": warning
    }


def interpret_phenytoin_level(level_mg_l):
    """
    Interpret Phenytoin serum level
    
    Args:
        level_mg_l: Phenytoin level in mg/L (or mcg/mL)
    
    Returns:
        dict with interpretation
    """
    target_min = 10.0
    target_max = 20.0
    
    if level_mg_l < target_min:
        status = "subtherapeutic"
        level_text = "⬇️ Dưới mục tiêu"
        recommendation = f"Nồng độ thấp (< {target_min} mg/L). Cân nhắc tăng liều hoặc kiểm tra compliance, drug interactions."
        color = "info"
    elif level_mg_l <= target_max:
        status = "therapeutic"
        level_text = "✅ Trong mục tiêu điều trị"
        recommendation = "Nồng độ trong khoảng điều trị (10-20 mg/L). Tiếp tục liều hiện tại."
        color = "success"
    elif level_mg_l <= 30:
        status = "supratherapeutic"
        level_text = "⚠️ Trên mục tiêu"
        recommendation = "Nồng độ cao (> 20 mg/L). Theo dõi triệu chứng độc tính. Cân nhắc giảm liều."
        color = "warning"
    else:
        status = "toxic"
        level_text = "🚨 ĐỘC TÍNH - Nguy hiểm"
        recommendation = "Nồng độ độc tính (> 30 mg/L)! Giảm liều ngay, theo dõi triệu chứng độc tính nặng."
        color = "error"
    
    return {
        "status": status,
        "level_text": level_text,
        "therapeutic_range": "10-20 mg/L",
        "recommendation": recommendation,
        "color": color,
        "current_level": level_mg_l
    }


def render_phenytoin_tdm():
    """Render Phenytoin TDM Calculator Interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💊 Phenytoin TDM Calculator</h2>
    <p style='text-align: center;'><em>Therapeutic Drug Monitoring & Dose Adjustment</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Phenytoin TDM:**
    - Mục tiêu: 10-20 mg/L (total), 1-2 mg/L (free)
    - Thời điểm lấy mẫu: ≥ 12 giờ sau liều (trough)
    - Half-life: 12-20 giờ (dose-dependent, non-linear)
    - Độc tính: > 30 mg/L
    - **Lưu ý:** Phenytoin có kinetics không tuyến tính (Michaelis-Menten)
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs(["🔴 Liều nạp", "📅 Liều duy trì", "📊 Điều chỉnh theo nồng độ"])
    
    with tab1:
        st.markdown("### 🔴 Tính toán liều nạp")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30,
                max_value=150,
                value=70,
                step=1,
                format="%d",
                key="phenytoin_loading_weight"
            )
            
            indication = st.selectbox(
                "Chỉ định:",
                ["Động kinh thông thường", "Trạng thái động kinh (Status epilepticus)"],
                key="phenytoin_loading_indication"
            )
        
        with col2:
            route = st.radio(
                "Đường dùng:",
                ["IV", "PO"],
                horizontal=True,
                key="phenytoin_loading_route"
            )
            
            indication_code = "status_epilepticus" if "Trạng thái" in indication else "seizure"
        
        st.markdown("---")
        
        if st.button("🧮 Tính liều nạp", type="primary", use_container_width=True):
            result = calculate_phenytoin_loading_dose(weight, indication_code)
            
            st.markdown("### 💊 Liều nạp:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "Tổng liều nạp",
                    f"{result['loading_dose_mg']:.0f} mg",
                    help=f"{result['loading_dose_mg_per_kg']:.1f} mg/kg"
                )
            
            with col2:
                if route == "IV":
                    st.metric(
                        "Thể tích (50 mg/mL)",
                        f"{result['iv_volume_ml']:.1f} mL"
                    )
                else:
                    st.metric(
                        "Số viên (100 mg)",
                        f"{result['po_capsules']:.0f} viên"
                    )
            
            st.markdown("---")
            
            if route == "IV":
                st.warning("""
                **⚠️ Lưu ý khi dùng IV:**
                
                - **Tốc độ truyền:** Không quá 50 mg/phút (tránh hypotension, cardiac arrhythmias)
                - **Thời gian truyền:** {:.0f} mg ÷ 50 mg/phút = {:.0f} phút tối thiểu
                - **Monitoring:** Huyết áp, ECG liên tục trong khi truyền
                - **Dilution:** Pha trong NS (không dùng D5W - có thể kết tủa)
                - **Y-site compatibility:** Kiểm tra tương thích với thuốc khác
                """.format(result['loading_dose_mg'], result['loading_dose_mg'] / 50))
            else:
                st.info("""
                **Liều nạp uống:**
                
                - **Cách cho:** Có thể chia 2-3 lần, mỗi 2-4 giờ
                - **Hoặc:** Cho toàn bộ cùng lúc nếu bệnh nhân tỉnh táo
                - **Lưu ý:** Hấp thu có thể chậm và không hoàn toàn
                """)
            
            st.markdown("---")
            st.success("""
            **📅 Sau liều nạp:**
            - Bắt đầu liều duy trì ngay sau khi cho xong liều nạp
            - Lấy mẫu TDM sau 12-24 giờ (sau liều maintenance đầu tiên)
            """)
    
    with tab2:
        st.markdown("### 📅 Tính toán liều duy trì")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30,
                max_value=150,
                value=70,
                step=1,
                format="%d",
                key="phenytoin_maint_weight"
            )
            
            current_level = st.number_input(
                "Nồng độ hiện tại (mg/L) - nếu có",
                min_value=0.0,
                max_value=50.0,
                value=0.0,
                step=0.5,
                format="%.1f",
                key="phenytoin_maint_level",
                help="Để trống nếu chưa có nồng độ"
            )
        
        with col2:
            target_level = st.number_input(
                "Mục tiêu nồng độ (mg/L)",
                min_value=10.0,
                max_value=20.0,
                value=15.0,
                step=0.5,
                format="%.1f",
                key="phenytoin_maint_target"
            )
        
        st.markdown("---")
        
        if st.button("🧮 Tính liều duy trì", type="primary", use_container_width=True):
            current_level_val = current_level if current_level > 0 else None
            result = calculate_phenytoin_maintenance_dose(weight, current_level_val, target_level)
            
            st.markdown("### 💊 Liều duy trì:")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều hàng ngày",
                    f"{result['maintenance_dose_mg']:.0f} mg",
                    help=f"{result['maintenance_dose_mg_per_kg']:.2f} mg/kg/ngày"
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
                    f"{result['dose_per_time']:.0f} mg"
                )
            
            st.markdown("---")
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Liều duy trì:** {result['maintenance_dose_mg']:.0f} mg/ngày chia {result['frequency']} lần
            (Mỗi lần: {result['dose_per_time']:.0f} mg)
            
            **Lưu ý:**
            - Bắt đầu với liều này
            - Theo dõi nồng độ sau 5-7 ngày (steady state)
            - Phenytoin có kinetics không tuyến tính → điều chỉnh liều cẩn thận
            """)
            
            st.markdown("---")
            st.markdown("### 🎯 Mục tiêu TDM")
            
            st.info("""
            **Mục tiêu nồng độ: 10-20 mg/L (total phenytoin)**
            
            **Thời điểm lấy mẫu:**
            - Lần đầu: Sau liều 5-7 (đạt steady state)
            - Lấy mẫu: ≥ 12 giờ sau liều cuối (trough)
            - Lấy mẫu buổi sáng trước khi uống liều tiếp theo
            
            **Tần suất theo dõi:**
            - Lần đầu: Sau 5-7 ngày
            - Khi ổn định: Mỗi 3-6 tháng
            - Khi thay đổi liều: Sau 5-7 ngày
            - Khi có tương tác thuốc: Sau 3-5 ngày
            
            **Free phenytoin:**
            - Nếu albumin thấp hoặc có tương tác → đo free phenytoin
            - Mục tiêu free: 1-2 mg/L
            """)
    
    with tab3:
        st.markdown("### 📊 Điều chỉnh Liều Theo Nồng Độ")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            current_dose = st.number_input(
                "Liều hiện tại (mg/ngày)",
                min_value=100,
                max_value=600,
                value=300,
                step=50,
                format="%d",
                key="phenytoin_adj_current_dose"
            )
        
        with col2:
            current_level = st.number_input(
                "Nồng độ hiện tại (mg/L)",
                min_value=0.1,
                max_value=50.0,
                value=12.0,
                step=0.5,
                format="%.1f",
                key="phenytoin_adj_current_level"
            )
        
        with col3:
            target_level = st.number_input(
                "Mục tiêu (mg/L)",
                min_value=10.0,
                max_value=20.0,
                value=15.0,
                step=0.5,
                format="%.1f",
                key="phenytoin_adj_target"
            )
        
        st.markdown("---")
        
        # Display interpretation first
        interpretation = interpret_phenytoin_level(current_level)
        
        if interpretation['color'] == 'success':
            st.success(f"**{interpretation['level_text']}**")
        elif interpretation['color'] == 'info':
            st.info(f"**{interpretation['level_text']}**")
        elif interpretation['color'] == 'warning':
            st.warning(f"**{interpretation['level_text']}**")
        else:
            st.error(f"**{interpretation['level_text']}**")
        
        st.markdown("---")
        
        if st.button("🧮 Tính liều điều chỉnh", type="primary", use_container_width=True):
            result = adjust_phenytoin_dose(current_dose, current_level, target_level)
            
            if "error" in result:
                st.error(result["error"])
            else:
                st.markdown("### 💊 Liều Điều chỉnh")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(
                        "Liều hiện tại",
                        f"{result['current_dose_mg']:.0f} mg/ngày"
                    )
                    
                    st.metric(
                        "Nồng độ hiện tại",
                        f"{result['current_level_mg_l']:.1f} mg/L"
                    )
                
                with col2:
                    delta_dose = result['new_dose_mg'] - result['current_dose_mg']
                    delta_text = f"{delta_dose:+.0f} mg" if delta_dose != 0 else "Không đổi"
                    
                    st.metric(
                        "Liều mới đề xuất",
                        f"{result['new_dose_mg']:.0f} mg/ngày",
                        delta=delta_text
                    )
                    
                    st.metric(
                        "Mục tiêu",
                        f"{result['target_level_mg_l']:.1f} mg/L"
                    )
                
                st.markdown("---")
                
                if result.get('warning'):
                    st.warning(result['warning'])
                
                st.success(f"""
                **💡 Khuyến nghị:**
                
                **Điều chỉnh:** {result['current_dose_mg']:.0f} → {result['new_dose_mg']:.0f} mg/ngày
                
                **Lưu ý:**
                - Phenytoin có **kinetics không tuyến tính** (Michaelis-Menten)
                - Khi nồng độ > 10 mg/L: Cần tăng liều nhiều hơn để tăng nồng độ ít
                - Khi nồng độ cao: Giảm liều nhỏ có thể giảm nồng độ đáng kể
                - Theo dõi nồng độ sau **5-7 ngày** sau điều chỉnh
                - Cân nhắc tương tác thuốc (Warfarin, Valproate, etc.)
                """)
                
                st.markdown("---")
                st.warning("""
                **⚠️ Cảnh báo về Phenytoin kinetics:**
                
                - **Non-linear kinetics:** Không thể tính toán đơn giản như thuốc khác
                - **Michaelis-Menten:** Vmax ~ 7 mg/kg/day, Km ~ 4-5 mg/L
                - Khi gần Vmax: Tăng liều ít → tăng nồng độ rất ít
                - Điều chỉnh từng bước nhỏ (25-50 mg), không tăng quá nhiều một lúc
                - Nếu không đạt mục tiêu: Cân nhắc chuyển sang thuốc khác (Valproate, Levetiracetam)
                """)
        
        # Toxicity section
        if current_level > 30:
            st.markdown("---")
            st.error("""
            **🚨 ĐỘC TÍNH PHENYTOIN - Xử trí Ngay:**
            
            **Triệu chứng độc tính:**
            - Nystagmus (rung giật nhãn cầu)
            - Ataxia (mất thăng bằng)
            - Lú lẫn
            - Co giật (paradoxical - hiếm)
            - Hôn mê (với nồng độ rất cao)
            
            **Xử trí:**
            1. Giảm liều hoặc ngừng tạm thời
            2. Hỗ trợ triệu chứng
            3. Theo dõi nồng độ
            4. Cân nhắc thuốc thay thế
            """)
    
    # Drug interactions
    st.markdown("---")
    with st.expander("⚠️ Tương tác Thuốc Quan Trọng"):
        st.markdown("""
        **Thuốc TĂNG nồng độ Phenytoin:**
        - Isoniazid
        - Chloramphenicol
        - Disulfiram
        - Cimetidine
        - Fluconazole
        
        **Thuốc GIẢM nồng độ Phenytoin:**
        - Carbamazepine
        - Phenobarbital
        - Rifampin
        
        **Phenytoin TĂNG thanh thải của:**
        - Warfarin (giảm tác dụng)
        - Oral contraceptives (giảm hiệu quả)
        - Corticosteroids
        - Vitamin D
        """)
    
    # References
    st.markdown("---")
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        - **AAN/AES Guidelines 2020**
        - **Michaelis-Menten kinetics:** Vmax ~ 7 mg/kg/day, Km ~ 4-5 mg/L
        - **Half-life:** 12-20 giờ (dose-dependent)
        - **Protein binding:** 90% (albumin)
        - **Free phenytoin:** 1-2 mg/L (10% of total)
        """)

