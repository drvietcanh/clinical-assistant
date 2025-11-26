"""
Digoxin TDM Calculator
Therapeutic Drug Monitoring cho Digoxin
"""

import streamlit as st
import math


def calculate_digoxin_dose(weight_kg, crcl, indication="heart_failure"):
    """
    Calculate Digoxin maintenance dose
    
    Args:
        weight_kg: Body weight in kg
        crcl: Creatinine clearance (mL/min)
        indication: "heart_failure" or "atrial_fibrillation"
    
    Returns:
        dict with dose information
    """
    # Loading dose (for rapid digitalization)
    loading_dose_mcg = weight_kg * 10  # 10 mcg/kg total, usually divided
    loading_dose_mg = loading_dose_mcg / 1000
    
    # Maintenance dose based on renal function
    # Formula: Daily dose (mcg) = (CrCl + 40) / 14 * weight (kg)
    # Target: 0.5-0.9 ng/mL (heart failure), 0.5-1.0 ng/mL (AF)
    
    if crcl >= 90:
        maintenance_dose_mcg_kg = 4.5  # mcg/kg/day
    elif crcl >= 60:
        maintenance_dose_mcg_kg = 3.5
    elif crcl >= 30:
        maintenance_dose_mcg_kg = 2.5
    elif crcl >= 15:
        maintenance_dose_mcg_kg = 1.5
    else:
        maintenance_dose_mcg_kg = 1.0  # CrCl < 15
    
    maintenance_dose_mcg = maintenance_dose_mcg_kg * weight_kg
    
    # Round to common tablet sizes
    tablet_sizes = [62.5, 125, 250]  # mcg
    closest_dose = min(tablet_sizes, key=lambda x: abs(x - maintenance_dose_mcg))
    
    # Frequency: Usually daily, may be QOD if very low
    frequency = 1 if crcl >= 15 else 0.5  # Every other day if very low
    
    return {
        "loading_dose_mcg": loading_dose_mcg,
        "loading_dose_mg": loading_dose_mg,
        "maintenance_dose_mcg": maintenance_dose_mcg,
        "maintenance_dose_mcg_per_kg": maintenance_dose_mcg_kg,
        "closest_tablet_mcg": closest_dose,
        "frequency": frequency,
        "indication": indication
    }


def interpret_digoxin_level(level_ng_ml, indication="heart_failure"):
    """
    Interpret Digoxin serum level
    
    Args:
        level_ng_ml: Digoxin level in ng/mL
        indication: "heart_failure" or "atrial_fibrillation"
    
    Returns:
        dict with interpretation
    """
    if indication == "heart_failure":
        target_min = 0.5
        target_max = 0.9
        therapeutic_range = "0.5-0.9 ng/mL"
    else:  # atrial_fibrillation
        target_min = 0.5
        target_max = 1.0
        therapeutic_range = "0.5-1.0 ng/mL"
    
    if level_ng_ml < target_min:
        status = "subtherapeutic"
        level_text = "⬇️ Dưới mục tiêu"
        recommendation = f"Nồng độ thấp (< {target_min} ng/mL). Cân nhắc tăng liều hoặc kiểm tra compliance."
        color = "info"
    elif level_ng_ml <= target_max:
        status = "therapeutic"
        level_text = "✅ Trong mục tiêu điều trị"
        recommendation = "Nồng độ trong khoảng điều trị. Tiếp tục liều hiện tại."
        color = "success"
    elif level_ng_ml <= 2.0:
        status = "supratherapeutic"
        level_text = "⚠️ Trên mục tiêu (chấp nhận được)"
        recommendation = "Nồng độ hơi cao nhưng có thể chấp nhận. Theo dõi triệu chứng độc tính. Cân nhắc giảm liều."
        color = "warning"
    else:
        status = "toxic"
        level_text = "🚨 ĐỘC TÍNH - Nguy hiểm"
        recommendation = "Nồng độ độc tính (> 2.0 ng/mL)! Ngừng digoxin ngay, kiểm tra kali máu, ECG. Cân nhắc Digibind nếu triệu chứng nặng."
        color = "error"
    
    return {
        "status": status,
        "level_text": level_text,
        "therapeutic_range": therapeutic_range,
        "recommendation": recommendation,
        "color": color,
        "current_level": level_ng_ml
    }


def render_digoxin_tdm():
    """Render Digoxin TDM Calculator Interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>💊 Digoxin TDM Calculator</h2>
    <p style='text-align: center;'><em>Therapeutic Drug Monitoring & Dose Adjustment</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Digoxin TDM:**
    - Mục tiêu: 0.5-0.9 ng/mL (suy tim), 0.5-1.0 ng/mL (rung nhĩ)
    - Thời điểm lấy mẫu: ≥ 6-8 giờ sau liều cuối (trough)
    - Độc tính: > 2.0 ng/mL
    - Half-life: 36-48 giờ (người lớn, chức năng thận bình thường)
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2 = st.tabs(["🧮 Tính Liều", "📊 Giải thích Nồng Độ"])
    
    with tab1:
        st.markdown("### 📋 Thông số bệnh nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="digoxin_weight"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=5.0,
                max_value=150.0,
                value=60.0,
                step=5.0,
                format="%.1f",
                key="digoxin_crcl",
                help="Creatinine clearance"
            )
        
        with col2:
            indication = st.selectbox(
                "Chỉ định:",
                ["Suy tim (Heart Failure)", "Rung nhĩ (Atrial Fibrillation)"],
                key="digoxin_indication"
            )
            
            indication_code = "heart_failure" if "Suy tim" in indication else "atrial_fibrillation"
            
            need_loading = st.checkbox(
                "Cần loading dose?",
                key="digoxin_loading",
                help="Loading dose cho digitalization nhanh"
            )
        
        st.markdown("---")
        
        if st.button("🧮 Tính Liều Digoxin", type="primary", use_container_width=True):
            result = calculate_digoxin_dose(weight, crcl, indication_code)
            
            st.markdown("### 💊 Kết quả Tính Liều")
            
            if need_loading:
                st.markdown("#### 🔴 Loading Dose (Digitalization):")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.info(f"""
                    **Tổng loading dose:**
                    {result['loading_dose_mcg']:.0f} mcg
                    ({result['loading_dose_mg']:.2f} mg)
                    """)
                
                with col2:
                    st.warning("""
                    **Cách cho:**
                    - Chia 3 liều: 50% liều 1, 25% liều 2, 25% liều 3
                    - Khoảng cách: 6-8 giờ
                    - Hoặc: Cho 1/2 liều, đánh giá, cho tiếp nếu cần
                    """)
            
            st.markdown("---")
            st.markdown("#### 📅 Maintenance Dose (Liều Duy Trì):")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều tính được",
                    f"{result['maintenance_dose_mcg']:.0f} mcg/ngày",
                    help=f"{result['maintenance_dose_mcg_per_kg']:.2f} mcg/kg/ngày"
                )
            
            with col2:
                if result['frequency'] == 1:
                    freq_text = "Mỗi ngày"
                else:
                    freq_text = "Cách ngày"
                
                st.metric("Tần suất", freq_text)
            
            with col3:
                tablet_size = result['closest_tablet_mcg']
                st.metric(
                    "Viên gần nhất",
                    f"{tablet_size:.0f} mcg",
                    delta=f"{abs(result['maintenance_dose_mcg'] - tablet_size):.0f} mcg chênh lệch" if abs(result['maintenance_dose_mcg'] - tablet_size) > 10 else "Phù hợp"
                )
            
            st.markdown("---")
            
            # Recommendation
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Liều duy trì:** {result['closest_tablet_mcg']:.0f} mcg **{freq_text}**
            
            **Lưu ý:**
            - Bắt đầu với liều thấp hơn ở người già
            - Theo dõi nồng độ sau 5-7 ngày (steady state)
            - Kiểm tra kali máu trước khi bắt đầu (hypokalemia tăng độc tính)
            - CrCl {crcl:.0f} mL/min: Dùng liều điều chỉnh cho suy thận
            """)
            
            st.markdown("---")
            st.markdown("### 🎯 Mục Tiêu TDM")
            
            if indication_code == "heart_failure":
                st.info("""
                **Mục tiêu nồng độ: 0.5-0.9 ng/mL**
                
                **Thời điểm lấy mẫu:**
                - Lần đầu: Sau liều 5-7 (đạt steady state)
                - Lấy mẫu: ≥ 6-8 giờ sau liều cuối (trough)
                - Lấy mẫu buổi sáng trước khi uống liều tiếp theo
                
                **Tần suất theo dõi:**
                - Lần đầu: Sau 5-7 ngày
                - Khi ổn định: Mỗi 3-6 tháng
                - Khi thay đổi liều: Sau 5-7 ngày
                - Khi có triệu chứng độc tính: Ngay lập tức
                """)
            else:
                st.info("""
                **Mục tiêu nồng độ: 0.5-1.0 ng/mL (rung nhĩ)**
                
                **Thời điểm lấy mẫu:**
                - Lần đầu: Sau liều 5-7 (đạt steady state)
                - Lấy mẫu: ≥ 6-8 giờ sau liều cuối (trough)
                - Lấy mẫu buổi sáng trước khi uống liều tiếp theo
                
                **Tần suất theo dõi:**
                - Tương tự suy tim
                """)
            
            st.markdown("---")
            st.markdown("### ⚠️ Cảnh Báo Độc Tính")
            
            st.error("""
            **Triệu chứng độc tính Digoxin:**
            
            **Tim mạch:**
            - Nhịp tim chậm (bradycardia)
            - Block nhĩ thất (AV block)
            - Nhịp nhanh thất (VT)
            - Rung thất (VF)
            
            **Tiêu hóa:**
            - Buồn nôn, nôn
            - Chán ăn
            
            **Thần kinh:**
            - Lú lẫn
            - Rối loạn thị giác (màu vàng)
            - Mệt mỏi
            
            **Yếu tố tăng nguy cơ độc tính:**
            - Hypokalemia (giảm kali máu)
            - Hypomagnesemia (giảm magne máu)
            - Hypercalcemia (tăng canxi máu)
            - Suy thận (tăng nồng độ)
            - Thuốc tương tác (Amiodarone, Verapamil, etc.)
            """)
    
    with tab2:
        st.markdown("### 📊 Giải thích Nồng Độ Digoxin")
        
        col1, col2 = st.columns(2)
        
        with col1:
            level = st.number_input(
                "Nồng độ Digoxin (ng/mL)",
                min_value=0.0,
                max_value=5.0,
                value=0.8,
                step=0.1,
                format="%.2f",
                key="digoxin_level"
            )
            
            indication_interp = st.selectbox(
                "Chỉ định:",
                ["Suy tim (Heart Failure)", "Rung nhĩ (Atrial Fibrillation)"],
                key="digoxin_indication_interp"
            )
        
        with col2:
            time_since_dose = st.number_input(
                "Thời gian sau liều cuối (giờ)",
                min_value=0.0,
                max_value=24.0,
                value=12.0,
                step=1.0,
                format="%.1f",
                key="digoxin_time",
                help="Thời điểm lấy mẫu so với liều cuối"
            )
            
            if time_since_dose < 6:
                st.warning("⚠️ Mẫu lấy quá sớm (< 6 giờ). Nồng độ có thể không phản ánh đúng trough level.")
        
        st.markdown("---")
        
        if st.button("📊 Giải thích Nồng Độ", type="primary", use_container_width=True):
            indication_code = "heart_failure" if "Suy tim" in indication_interp else "atrial_fibrillation"
            interpretation = interpret_digoxin_level(level, indication_code)
            
            st.markdown("### 📈 Kết quả Giải thích")
            
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
                    f"{interpretation['current_level']:.2f} ng/mL"
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
            
            # Adjustment guide
            if interpretation['status'] == "subtherapeutic":
                st.markdown("---")
                st.markdown("#### 🔼 Hướng Dẫn Tăng Liều:")
                
                current_dose_mcg = st.number_input(
                    "Liều hiện tại (mcg/ngày)",
                    min_value=62.5,
                    max_value=500.0,
                    value=125.0,
                    step=62.5,
                    key="current_dose_adjust",
                    format="%.0f"
                )
                
                if st.button("Tính liều mới"):
                    # Simple adjustment: increase by 25-50% if subtherapeutic
                    suggested_increase = 0.375  # 37.5% increase
                    new_dose = current_dose_mcg * (1 + suggested_increase)
                    
                    # Round to tablet size
                    tablet_sizes = [62.5, 125, 250]
                    new_dose_rounded = min(tablet_sizes, key=lambda x: abs(x - new_dose))
                    
                    st.success(f"""
                    **Liều đề xuất:** {new_dose_rounded:.0f} mcg/ngày
                    
                    **Lưu ý:**
                    - Tăng từ {current_dose_mcg:.0f} → {new_dose_rounded:.0f} mcg/ngày
                    - Theo dõi nồng độ sau 5-7 ngày
                    - Kiểm tra kali máu
                    """)
            
            elif interpretation['status'] == "toxic":
                st.markdown("---")
                st.markdown("#### 🔽 Xử Trí Độc Tính:")
                
                st.error("""
                **🚨 Xử trí ngay lập tức:**
                
                1. **Ngừng digoxin ngay**
                2. **Kiểm tra:**
                   - Kali máu (thường giảm trong độc tính)
                   - Magne máu
                   - ECG (tìm block nhĩ thất, VT)
                   - Creatinine, eGFR
                
                3. **Điều trị triệu chứng:**
                   - Hypokalemia: Bù kali (thận trọng với block AV)
                   - Hypomagnesemia: Bù magne
                   - Block AV: Có thể cần pacing
                
                4. **Digibind (Digoxin Immune Fab):**
                   - Chỉ định: Độc tính nặng, rối loạn nhịp nguy hiểm
                   - Liều: Tính theo nồng độ digoxin
                   - Chỉ dùng khi thật sự cần thiết
                
                5. **Theo Dõi:**
                   - ECG liên tục
                   - Nồng độ digoxin (có thể tăng sau Digibind do giải phóng từ mô)
                """)
            
            elif interpretation['status'] == "supratherapeutic":
                st.markdown("---")
                st.markdown("#### 🔽 Hướng Dẫn Giảm Liều:")
                
                current_dose_mcg = st.number_input(
                    "Liều hiện tại (mcg/ngày)",
                    min_value=62.5,
                    max_value=500.0,
                    value=125.0,
                    step=62.5,
                    key="current_dose_reduce",
                    format="%.0f"
                )
                
                if st.button("Tính liều giảm"):
                    # Reduce by 25-30%
                    reduction = 0.25
                    new_dose = current_dose_mcg * (1 - reduction)
                    
                    # Round to tablet size
                    tablet_sizes = [62.5, 125, 250]
                    new_dose_rounded = min(tablet_sizes, key=lambda x: abs(x - new_dose))
                    
                    st.warning(f"""
                    **Liều đề xuất:** {new_dose_rounded:.0f} mcg/ngày
                    
                    **Lưu ý:**
                    - Giảm từ {current_dose_mcg:.0f} → {new_dose_rounded:.0f} mcg/ngày
                    - Theo dõi nồng độ sau 5-7 ngày
                    - Theo dõi triệu chứng độc tính
                    """)
    
    # References
    st.markdown("---")
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        - **ACC/AHA Heart Failure Guidelines 2022**
        - **Digoxin TDM Guidelines**
        - **Half-life:** 36-48 giờ (normal renal function), 3-5 ngày (ESRD)
        - **Protein binding:** 20-30%
        - **Volume of distribution:** 4-7 L/kg
        """)

