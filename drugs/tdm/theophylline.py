"""
Theophylline TDM Calculator
Therapeutic Drug Monitoring cho Theophylline
"""

import streamlit as st
import math


def calculate_theophylline_half_life(age, smoking_status, crcl, other_factors=None):
    """
    Estimate Theophylline half-life
    
    Args:
        age: Patient age
        smoking_status: "smoker", "non_smoker", "ex_smoker"
        crcl: Creatinine clearance
        other_factors: dict with factors like liver_disease, heart_failure
    
    Returns:
        estimated half-life in hours
    """
    # Base half-life: ~8 hours for non-smoker, normal
    base_half_life = 8.0
    
    # Smoking increases clearance (shorter half-life)
    if smoking_status == "smoker":
        base_half_life = 5.0  # Smokers: 4-5 hours
    elif smoking_status == "ex_smoker":
        base_half_life = 6.5  # Ex-smokers: intermediate
    
    # Age: Elderly have longer half-life
    if age >= 65:
        base_half_life *= 1.3
    
    # Heart failure: Increases half-life
    if other_factors and other_factors.get('heart_failure'):
        base_half_life *= 1.5
    
    # Liver disease: Increases half-life
    if other_factors and other_factors.get('liver_disease'):
        base_half_life *= 1.8
    
    # COPD: Slightly longer half-life
    if other_factors and other_factors.get('copd'):
        base_half_life *= 1.2
    
    return round(base_half_life, 1)


def calculate_theophylline_dose(weight_kg, indication="asthma", target_level_mg_l=10):
    """
    Calculate Theophylline maintenance dose
    
    Args:
        weight_kg: Body weight
        indication: "asthma" or "copd"
        target_level_mg_l: Target level (usually 10-15 mg/L)
    
    Returns:
        dict with dose
    """
    # Typical dose: 10-15 mg/kg/day divided
    # Target level: 10-15 mg/L (asthma), 8-12 mg/L (COPD)
    
    if indication == "asthma":
        dose_mg_per_kg = 13  # mg/kg/day for 10-15 mg/L target
    else:  # COPD
        dose_mg_per_kg = 10  # mg/kg/day for 8-12 mg/L target
    
    total_dose_mg = dose_mg_per_kg * weight_kg
    
    # Common formulations: 100, 200, 300 mg tablets/capsules
    # Usually divided into 2-3 doses
    
    # Round to reasonable dose
    if total_dose_mg < 400:
        frequency = 2  # BID
        dose_per_time = round(total_dose_mg / 2 / 50) * 50
    else:
        frequency = 3  # TID (or Q8h)
        dose_per_time = round(total_dose_mg / 3 / 50) * 50
    
    return {
        "daily_dose_mg": round(total_dose_mg / 50) * 50,
        "dose_per_time_mg": dose_per_time,
        "frequency": frequency,
        "dose_mg_per_kg": dose_mg_per_kg,
        "target_level": target_level_mg_l
    }


def adjust_theophylline_dose(current_dose_mg, current_level_mg_l, target_level_mg_l=10):
    """
    Adjust Theophylline dose (linear kinetics)
    
    Args:
        current_dose_mg: Current daily dose
        current_level_mg_l: Current level
        target_level_mg_l: Target level
    
    Returns:
        dict with adjusted dose
    """
    if current_level_mg_l <= 0:
        return {"error": "Nồng độ không hợp lệ"}
    
    # Linear kinetics: simple proportional adjustment
    adjustment_factor = target_level_mg_l / current_level_mg_l
    new_dose_mg = current_dose_mg * adjustment_factor
    
    # Round to tablet sizes
    new_dose_mg_rounded = round(new_dose_mg / 50) * 50
    
    # Safety: Max 900 mg/day for adults
    if new_dose_mg_rounded > 900:
        new_dose_mg_rounded = 900
        warning = "⚠️ Liều tối đa 900mg/ngày. Cân nhắc thuốc thay thế."
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


def interpret_theophylline_level(level_mg_l, indication="asthma"):
    """
    Interpret Theophylline level
    
    Args:
        level_mg_l: Theophylline level (mg/L)
        indication: "asthma" or "copd"
    
    Returns:
        dict with interpretation
    """
    if indication == "asthma":
        target_min = 10.0
        target_max = 15.0
        therapeutic_range = "10-15 mg/L"
    else:  # COPD
        target_min = 8.0
        target_max = 12.0
        therapeutic_range = "8-12 mg/L"
    
    if level_mg_l < target_min:
        status = "subtherapeutic"
        level_text = "⬇️ Dưới mục tiêu"
        recommendation = f"Nồng độ thấp (< {target_min} mg/L). Cân nhắc tăng liều."
        color = "info"
    elif level_mg_l <= target_max:
        status = "therapeutic"
        level_text = "✅ Trong mục tiêu điều trị"
        recommendation = f"Nồng độ trong khoảng điều trị ({therapeutic_range}). Tiếp tục liều hiện tại."
        color = "success"
    elif level_mg_l <= 20:
        status = "supratherapeutic"
        level_text = "⚠️ Trên mục tiêu"
        recommendation = "Nồng độ cao (15-20 mg/L). Theo dõi triệu chứng độc tính. Cân nhắc giảm liều."
        color = "warning"
    else:
        status = "toxic"
        level_text = "🚨 ĐỘC TÍNH - Nguy hiểm"
        recommendation = "Nồng độ độc tính (> 20 mg/L)! Giảm liều hoặc ngừng ngay, theo dõi triệu chứng độc tính."
        color = "error"
    
    return {
        "status": status,
        "level_text": level_text,
        "therapeutic_range": therapeutic_range,
        "recommendation": recommendation,
        "color": color,
        "current_level": level_mg_l
    }


def render_theophylline_tdm():
    """Render Theophylline TDM Calculator Interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💊 Theophylline TDM Calculator</h2>
    <p style='text-align: center;'><em>Therapeutic Drug Monitoring & Dose Adjustment</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Theophylline TDM:**
    - Mục tiêu: 10-15 mg/L (hen phế quản), 8-12 mg/L (COPD)
    - Thời điểm lấy mẫu: Trough (trước liều) hoặc peak (1-2h sau)
    - Half-life: 5-8 giờ (thay đổi theo nhiều yếu tố)
    - Độc tính: > 20 mg/L
    - **Lưu ý:** Theophylline có TI hẹp, nhiều yếu tố ảnh hưởng clearance
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs(["🧮 Tính liều", "📊 Điều Chỉnh Liều", "⏱️ Tính Half-life"])
    
    with tab1:
        st.markdown("### 📋 Thông số bệnh nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30,
                max_value=150,
                value=70,
                step=1,
                format="%d",
                key="theo_weight"
            )
            
            indication = st.selectbox(
                "Chỉ định:",
                ["Hen phế quản (Asthma)", "COPD"],
                key="theo_indication"
            )
        
        with col2:
            target_level = st.number_input(
                "Mục tiêu nồng độ (mg/L)",
                min_value=8.0,
                max_value=15.0,
                value=12.0,
                step=0.5,
                format="%.1f",
                key="theo_target"
            )
            
            indication_code = "asthma" if "hen" in indication.lower() else "copd"
        
        st.markdown("---")
        
        if st.button("🧮 Tính liều Theophylline", type="primary", use_container_width=True):
            result = calculate_theophylline_dose(weight, indication_code, target_level)
            
            st.markdown("### 💊 Maintenance Dose:")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều hàng ngày",
                    f"{result['daily_dose_mg']:.0f} mg",
                    help=f"{result['dose_mg_per_kg']:.1f} mg/kg/ngày"
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
            
            **Liều duy trì:** {result['daily_dose_mg']:.0f} mg/ngày chia {result['frequency']} lần
            (Mỗi lần: {result['dose_per_time_mg']:.0f} mg)
            
            **Lưu ý:**
            - Bắt đầu với liều thấp, tăng từng bước
            - Theo dõi nồng độ sau 2-3 ngày (steady state)
            - Nhiều yếu tố ảnh hưởng clearance (xem tab Half-life)
            """)
            
            st.markdown("---")
            st.markdown("### 🎯 Mục tiêu TDM")
            
            st.info(f"""
            **Mục tiêu nồng độ: {result['target_level']:.1f} mg/L**
            ({'Hen phế quản: 10-15 mg/L' if indication_code == 'asthma' else 'COPD: 8-12 mg/L'})
            
            **Thời điểm lấy mẫu:**
            - **Trough:** Trước liều tiếp theo (ưu tiên)
            - **Peak:** 1-2 giờ sau uống
            - Lần đầu: Sau liều 2-3 (đạt steady state)
            
            **Tần suất theo dõi:**
            - Lần đầu: Sau 2-3 ngày
            - Khi ổn định: Mỗi 3-6 tháng
            - Khi thay đổi liều: Sau 2-3 ngày
            - Khi có tương tác thuốc: Sau 2-3 ngày
            """)
    
    with tab2:
        st.markdown("### 📊 Điều Chỉnh Liều Theo Nồng Độ")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            current_dose = st.number_input(
                "Liều hiện tại (mg/ngày)",
                min_value=100,
                max_value=900,
                value=400,
                step=50,
                format="%d",
                key="theo_adj_dose"
            )
        
        with col2:
            current_level = st.number_input(
                "Nồng độ hiện tại (mg/L)",
                min_value=0.1,
                max_value=30.0,
                value=8.0,
                step=0.5,
                format="%.1f",
                key="theo_adj_level"
            )
        
        with col3:
            target_level = st.number_input(
                "Mục tiêu (mg/L)",
                min_value=8.0,
                max_value=15.0,
                value=12.0,
                step=0.5,
                format="%.1f",
                key="theo_adj_target"
            )
        
        st.markdown("---")
        
        # Display interpretation
        indication_interp = st.selectbox(
            "Chỉ định:",
            ["Hen phế quản", "COPD"],
            key="theo_adj_indication"
        )
        indication_code = "asthma" if "hen" in indication_interp.lower() else "copd"
        
        interpretation = interpret_theophylline_level(current_level, indication_code)
        
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
            result = adjust_theophylline_dose(current_dose, current_level, target_level)
            
            if "error" in result:
                st.error(result["error"])
            else:
                st.markdown("### 💊 Liều Điều Chỉnh")
                
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
                
                if result.get('warning'):
                    st.warning(result['warning'])
                
                st.success(f"""
                **💡 Khuyến nghị:**
                
                **Điều Chỉnh:** {result['current_dose_mg']:.0f} → {result['new_dose_mg']:.0f} mg/ngày
                
                **Lưu ý:**
                - Theophylline có kinetics tuyến tính (dễ điều chỉnh hơn Phenytoin)
                - Theo dõi nồng độ sau 2-3 ngày
                - Kiểm tra tương tác thuốc
                """)
    
    with tab3:
        st.markdown("### ⏱️ Tính Half-life Theophylline")
        
        st.info("""
        **Half-life Theophylline phụ thuộc nhiều yếu tố:**
        - Hút thuốc: 4-5 giờ (tăng clearance)
        - Không hút thuốc: 6-8 giờ
        - Người già: Dài hơn
        - Suy tim: Dài hơn
        - Bệnh gan: Dài hơn
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input(
                "Tuổi (năm)",
                min_value=18,
                max_value=100,
                value=45,
                step=1,
                key="theo_half_age"
            )
            
            smoking_status = st.selectbox(
                "Hút thuốc:",
                ["Không hút", "Đang hút", "Đã bỏ"],
                key="theo_half_smoking"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=30,
                max_value=150,
                value=90,
                step=5,
                format="%d",
                key="theo_half_crcl"
            )
        
        with col2:
            st.markdown("#### Yếu tố Ảnh Hưởng:")
            
            heart_failure = st.checkbox("Suy tim", key="theo_half_hf")
            liver_disease = st.checkbox("Bệnh gan", key="theo_half_liver")
            copd = st.checkbox("COPD", key="theo_half_copd")
        
        st.markdown("---")
        
        if st.button("⏱️ Tính Half-life", type="primary", use_container_width=True):
            smoking_code = {
                "Không hút": "non_smoker",
                "Đang hút": "smoker",
                "Đã bỏ": "ex_smoker"
            }[smoking_status]
            
            other_factors = {
                "heart_failure": heart_failure,
                "liver_disease": liver_disease,
                "copd": copd
            }
            
            half_life = calculate_theophylline_half_life(age, smoking_code, crcl, other_factors)
            
            st.markdown("### ⏱️ Kết quả")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "Half-life ước tính",
                    f"{half_life:.1f} giờ"
                )
            
            with col2:
                time_to_steady_state = half_life * 5  # 5 half-lives to steady state
                st.metric(
                    "Đạt steady state sau",
                    f"{time_to_steady_state:.0f} giờ"
                )
            
            st.markdown("---")
            st.info(f"""
            **💡 Ý nghĩa:**
            
            - **Half-life:** {half_life:.1f} giờ
            - **Steady state:** Sau {time_to_steady_state:.0f} giờ (~{time_to_steady_state/24:.1f} ngày)
            - **Tần suất dùng:** Thường {3 if half_life < 7 else 2} lần/ngày
            
            **Lưu ý:**
            - Half-life này là ước tính, có thể thay đổi theo từng bệnh nhân
            - Yếu tố ảnh hưởng quan trọng nhất: Hút thuốc
            - Nếu có nhiều yếu tố: Half-life có thể dài hơn đáng kể
            """)
    
    # Toxicity
    st.markdown("---")
    with st.expander("🚨 Độc Tính Theophylline"):
        st.error("""
        **Triệu chứng độc tính (> 20 mg/L):**
        
        **Tim mạch:**
        - Nhịp tim nhanh
        - Rối loạn nhịp tim
        - Hạ huyết áp (với nồng độ rất cao)
        
        **Thần kinh:**
        - Run tay
        - Co giật
        - Lú lẫn
        
        **Tiêu hóa:**
        - Buồn nôn, nôn
        - Tiêu chảy
        
        **Xử trí:**
        - Ngừng theophylline
        - Hỗ trợ triệu chứng
        - Activated charcoal (nếu uống gần đây)
        - Hemodialysis (với nồng độ rất cao > 40 mg/L)
        """)
    
    # Drug interactions
    st.markdown("---")
    with st.expander("⚠️ Tương tác Thuốc"):
        st.markdown("""
        **Thuốc TĂNG nồng độ (giảm clearance):**
        - Cimetidine
        - Ciprofloxacin
        - Erythromycin
        - Allopurinol (liều cao)
        - Verapamil
        
        **Thuốc GIẢM nồng độ (tăng clearance):**
        - Rifampin
        - Phenytoin
        - Carbamazepine
        - Tobacco smoking (nicotine)
        """)
    
    # References
    st.markdown("---")
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        - **ATS/ERS Guidelines - Asthma & COPD**
        - **Half-life:** 5-8 giờ (thay đổi)
        - **Clearance:** Chủ yếu qua gan (CYP1A2)
        - **Therapeutic index:** Hẹp
        """)

