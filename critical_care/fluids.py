"""
Fluid Therapy Calculator
Calculate maintenance fluids, deficits, and electrolyte replacements
"""

import streamlit as st
from components.ui.inputs import render_number_input_with_unit
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def calculate_maintenance_fluids(weight_kg: float, age_years: float = None) -> dict:
    """
    Calculate daily maintenance fluid requirements using Holliday-Segar method
    
    Args:
        weight_kg: Weight in kg
        age_years: Age in years (optional, for adults use 18+)
    
    Returns:
        Dictionary with fluid requirements
    """
    if age_years is None or age_years >= 18:
        # Adult: 30-35 ml/kg/day (or 25-30 ml/kg/day for elderly)
        if age_years and age_years >= 65:
            daily_ml = weight_kg * 25
            hourly_ml = daily_ml / 24
        else:
            daily_ml = weight_kg * 30
            hourly_ml = daily_ml / 24
    else:
        # Pediatric: Holliday-Segar method
        if weight_kg <= 10:
            daily_ml = weight_kg * 100
        elif weight_kg <= 20:
            daily_ml = 1000 + (weight_kg - 10) * 50
        else:
            daily_ml = 1500 + (weight_kg - 20) * 20
        
        hourly_ml = daily_ml / 24
    
    # Electrolyte requirements (per day)
    sodium = weight_kg * 2  # mEq/kg/day
    potassium = weight_kg * 1  # mEq/kg/day
    
    return {
        "daily_ml": daily_ml,
        "hourly_ml": hourly_ml,
        "daily_liters": daily_ml / 1000,
        "sodium_mmol": sodium,
        "potassium_mmol": potassium,
    }


def calculate_fluid_deficit(weight_kg: float, current_na: float, target_na: float = 140) -> dict:
    """
    Calculate fluid deficit in hypernatremia
    
    Args:
        weight_kg: Weight in kg
        current_na: Current serum sodium (mmol/L)
        target_na: Target serum sodium (mmol/L, default 140)
    
    Returns:
        Dictionary with fluid deficit calculation
    """
    if current_na <= target_na:
        return {
            "deficit_liters": 0,
            "deficit_ml": 0,
            "note": "Không có tăng natri máu"
        }
    
    # Free water deficit = TBW × [(Na_current - Na_target) / Na_target]
    # TBW (Total Body Water) = 0.6 × weight (adult male) or 0.5 × weight (adult female/elderly)
    # Using average 0.55 for calculation
    tbw_liters = weight_kg * 0.55
    
    deficit_liters = tbw_liters * ((current_na - target_na) / target_na)
    deficit_ml = deficit_liters * 1000
    
    # Correction rate: không quá 0.5 mmol/L/hour để tránh phù não
    na_correction_needed = current_na - target_na
    hours_to_correct = na_correction_needed / 0.5  # Maximum safe rate
    hourly_rate_ml = deficit_ml / hours_to_correct if hours_to_correct > 0 else 0
    
    return {
        "deficit_liters": deficit_liters,
        "deficit_ml": deficit_ml,
        "hours_to_correct": hours_to_correct,
        "hourly_rate_ml": hourly_rate_ml,
        "sodium_correction_needed": na_correction_needed,
    }


def calculate_hyponatremia_correction(weight_kg: float, current_na: float, target_na: float = 135) -> dict:
    """
    Calculate sodium correction for hyponatremia
    
    Args:
        weight_kg: Weight in kg
        current_na: Current serum sodium (mmol/L)
        target_na: Target serum sodium (mmol/L, default 135)
    
    Returns:
        Dictionary with correction calculation
    """
    if current_na >= target_na:
        return {
            "sodium_needed_mmol": 0,
            "note": "Không có hạ natri máu"
        }
    
    # Sodium deficit = TBW × (Target_Na - Current_Na)
    tbw_liters = weight_kg * 0.55
    
    na_deficit_mmol = tbw_liters * (target_na - current_na)
    
    # 3% NaCl contains 513 mmol Na/L
    # 0.9% NaCl contains 154 mmol Na/L
    # NS (0.9%) correction
    ns_liters_needed = na_deficit_mmol / 154
    
    # Hypertonic saline (3% NaCl) correction (if severe)
    if current_na < 120:
        hypertonic_liters = na_deficit_mmol / 513
        hypertonic_ml = hypertonic_liters * 1000
    else:
        hypertonic_liters = 0
        hypertonic_ml = 0
    
    # Safe correction rate: 6-8 mmol/L in first 24h, không quá 10-12 mmol/L
    na_correction_needed = target_na - current_na
    max_24h_correction = min(na_correction_needed, 8)  # Maximum safe in 24h
    
    return {
        "na_deficit_mmol": na_deficit_mmol,
        "ns_liters_needed": ns_liters_needed,
        "ns_ml_needed": ns_liters_needed * 1000,
        "hypertonic_ml_needed": hypertonic_ml,
        "hypertonic_liters_needed": hypertonic_liters,
        "safe_24h_correction": max_24h_correction,
        "correction_needed": na_correction_needed,
    }


def calculate_maintenance_electrolytes(weight_kg: float) -> dict:
    """
    Calculate daily maintenance electrolyte requirements
    
    Args:
        weight_kg: Weight in kg
    
    Returns:
        Dictionary with electrolyte requirements
    """
    sodium = weight_kg * 2  # mEq/kg/day = mmol/kg/day
    potassium = weight_kg * 1  # mEq/kg/day = mmol/kg/day
    chloride = weight_kg * 1.5  # Approximate
    
    # Common IV solutions:
    # NS (0.9% NaCl): 154 mmol Na/L, 154 mmol Cl/L
    # D5W: 0 mmol/L
    # Lactated Ringer's: 130 mmol Na/L, 109 mmol Cl/L, 4 mmol K/L, 28 mmol Lactate/L
    
    # To provide sodium from NS
    ns_ml_for_na = (sodium / 154) * 1000
    
    return {
        "sodium_mmol": sodium,
        "potassium_mmol": potassium,
        "chloride_mmol": chloride,
        "ns_ml_for_sodium": ns_ml_for_na,
    }


def render_fluid_calculator():
    """Render fluid therapy calculator interface"""
    
    st.markdown("## 💧 Tính Toán Dịch Truyền")
    st.markdown("""
    Công cụ tính toán dịch truyền và điện giải cho bệnh nhân.
    
    **Tính năng:**
    - Maintenance fluids (Holliday-Segar)
    - Fluid deficit trong tăng natri máu
    - Điều chỉnh natri trong hạ natri máu
    - Nhu cầu điện giải hàng ngày
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3, tab4 = st.tabs([
        "💧 Maintenance Fluids",
        "⬆️ Tăng Natri (Fluid Deficit)",
        "⬇️ Hạ Natri (Correction)",
        "🧪 Electrolytes"
    ])
    
    # ========== TAB 1: MAINTENANCE FLUIDS ==========
    with tab1:
        st.markdown("### 💧 Maintenance Fluids (Holliday-Segar)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg):",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                key="maintenance_weight"
            )
        
        with col2:
            age = st.number_input(
                "Tuổi (năm):",
                min_value=0.0,
                max_value=120.0,
                value=30.0,
                step=1.0,
                key="maintenance_age",
                help="Để trống hoặc ≥18 cho người lớn"
            )
        
        if st.button("Tính toán", key="calc_maintenance", type="primary"):
            results = calculate_maintenance_fluids(weight, age if age > 0 else None)
            
            st.markdown("---")
            st.markdown("### 📊 Kết Quả")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                render_result_box(
                    "Dịch/ngày",
                    f"{results['daily_liters']:.2f} L",
                    subtitle=f"{results['daily_ml']:.0f} ml",
                    color="primary",
                    icon="💧"
                )
            
            with col2:
                render_result_box(
                    "Dịch/giờ",
                    f"{results['hourly_ml']:.1f} ml/h",
                    color="info",
                    icon="⏱️"
                )
            
            with col3:
                render_result_box(
                    "Dịch/ngày (kg)",
                    f"{results['daily_ml']/weight:.1f} ml/kg",
                    color="success"
                )
            
            st.markdown("---")
            
            # Electrolyte requirements
            st.markdown("### 🧪 Nhu Cầu Điện Giải (Hàng Ngày)")
            
            metrics = [
                {"label": "Natri (Na)", "value": f"{results['sodium_mmol']:.1f} mmol", "icon": "🧂"},
                {"label": "Kali (K)", "value": f"{results['potassium_mmol']:.1f} mmol", "icon": "🥬"},
            ]
            
            render_result_card("Nhu Cầu Điện Giải", metrics, color="info")
            
            # Recommendations
            st.markdown("---")
            st.markdown("### 💡 Khuyến Nghị")
            
            if age and age < 18:
                st.info(f"""
                **Trẻ em ({age:.0f} tuổi, {weight:.1f} kg):**
                - Maintenance: **{results['daily_ml']:.0f} ml/ngày** ({results['daily_ml']/weight:.1f} ml/kg/ngày)
                - Chia đều: **{results['hourly_ml']:.1f} ml/giờ**
                - Dung dịch phù hợp: D5W + 0.45% NaCl hoặc D5W + 0.9% NaCl + KCl
                """)
            else:
                st.info(f"""
                **Người lớn ({weight:.1f} kg):**
                - Maintenance: **{results['daily_ml']:.0f} ml/ngày** (30 ml/kg/ngày)
                - Chia đều: **{results['hourly_ml']:.1f} ml/giờ**
                - Dung dịch phù hợp: D5W + 0.45% NaCl hoặc Lactated Ringer's
                """)
    
    # ========== TAB 2: FLUID DEFICIT (HYPERNATREMIA) ==========
    with tab2:
        st.markdown("### ⬆️ Tính Toán Thiếu Dịch (Tăng Natri Máu)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight_deficit = st.number_input(
                "Cân nặng (kg):",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                key="deficit_weight"
            )
        
        with col2:
            current_na = st.number_input(
                "Natri máu hiện tại (mmol/L):",
                min_value=120.0,
                max_value=180.0,
                value=155.0,
                step=0.1,
                key="current_na_deficit"
            )
        
        target_na_deficit = st.number_input(
            "Natri máu mục tiêu (mmol/L):",
            min_value=135.0,
            max_value=145.0,
            value=140.0,
            step=0.1,
            key="target_na_deficit",
            help="Thường là 140 mmol/L"
        )
        
        if st.button("Tính toán", key="calc_deficit", type="primary"):
            results = calculate_fluid_deficit(weight_deficit, current_na, target_na_deficit)
            
            if results.get("note"):
                st.warning(results["note"])
            else:
                st.markdown("---")
                st.markdown("### 📊 Kết Quả")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    render_result_box(
                        "Thiếu dịch",
                        f"{results['deficit_liters']:.2f} L",
                        subtitle=f"{results['deficit_ml']:.0f} ml",
                        color="warning",
                        icon="💧"
                    )
                
                with col2:
                    render_result_box(
                        "Tốc độ an toàn",
                        f"{results['hourly_rate_ml']:.1f} ml/h",
                        subtitle=f"Trong {results['hours_to_correct']:.1f} giờ",
                        color="info",
                        icon="⏱️"
                    )
                
                st.markdown("---")
                st.warning(f"""
                **⚠️ Lưu ý quan trọng:**
                - Tốc độ điều chỉnh: **không quá 0.5 mmol/L/giờ** để tránh phù não
                - Ưu tiên bù dịch nhược trương (D5W hoặc 0.45% NaCl)
                - Theo dõi natri máu mỗi 2-4 giờ
                - Tổng thời gian điều chỉnh: **{results['hours_to_correct']:.1f} giờ**
                """)
    
    # ========== TAB 3: HYPONATREMIA CORRECTION ==========
    with tab3:
        st.markdown("### ⬇️ Điều Chỉnh Hạ Natri Máu")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight_hyponatremia = st.number_input(
                "Cân nặng (kg):",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                key="hyponatremia_weight"
            )
        
        with col2:
            current_na_hyponatremia = st.number_input(
                "Natri máu hiện tại (mmol/L):",
                min_value=100.0,
                max_value=135.0,
                value=120.0,
                step=0.1,
                key="current_na_hyponatremia"
            )
        
        target_na_hyponatremia = st.number_input(
            "Natri máu mục tiêu (mmol/L):",
            min_value=125.0,
            max_value=140.0,
            value=135.0,
            step=0.1,
            key="target_na_hyponatremia",
            help="Thường là 135 mmol/L, không vượt quá 10 mmol/L trong 24h đầu"
        )
        
        if st.button("Tính toán", key="calc_hyponatremia", type="primary"):
            results = calculate_hyponatremia_correction(
                weight_hyponatremia, 
                current_na_hyponatremia, 
                target_na_hyponatremia
            )
            
            if results.get("note"):
                st.warning(results["note"])
            else:
                st.markdown("---")
                st.markdown("### 📊 Kết Quả")
                
                # Severe hyponatremia warning
                if current_na_hyponatremia < 120:
                    render_warning_alert(
                        "Hạ natri máu nặng (<120)! Cân nhắc dùng dung dịch ưu trương (3% NaCl)",
                        title="⚠️ Cảnh báo"
                    )
                
                col1, col2 = st.columns(2)
                
                with col1:
                    render_result_box(
                        "Thiếu natri",
                        f"{results['na_deficit_mmol']:.1f} mmol",
                        color="warning",
                        icon="🧂"
                    )
                
                with col2:
                    if results['hypertonic_ml_needed'] > 0:
                        render_result_box(
                            "3% NaCl cần",
                            f"{results['hypertonic_ml_needed']:.0f} ml",
                            subtitle="(Nếu hạ natri nặng)",
                            color="error",
                            icon="💉"
                        )
                    else:
                        render_result_box(
                            "0.9% NaCl cần",
                            f"{results['ns_ml_needed']:.0f} ml",
                            subtitle=f"({results['ns_liters_needed']:.2f} L)",
                            color="info",
                            icon="💧"
                        )
                
                st.markdown("---")
                st.warning(f"""
                **⚠️ An toàn:**
                - Điều chỉnh tối đa: **{results['safe_24h_correction']:.1f} mmol/L trong 24h đầu**
                - Tổng điều chỉnh cần: **{results['correction_needed']:.1f} mmol/L**
                - Nếu hạ natri cấp (<48h, có triệu chứng thần kinh): cân nhắc 3% NaCl
                - Nếu hạ natri mạn (>48h): điều chỉnh chậm để tránh myelinolysis
                """)
    
    # ========== TAB 4: ELECTROLYTES ==========
    with tab4:
        st.markdown("### 🧪 Nhu Cầu Điện Giải Hàng Ngày")
        
        weight_electrolytes = st.number_input(
            "Cân nặng (kg):",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            key="electrolytes_weight"
        )
        
        if st.button("Tính toán", key="calc_electrolytes", type="primary"):
            results = calculate_maintenance_electrolytes(weight_electrolytes)
            
            st.markdown("---")
            st.markdown("### 📊 Kết Quả")
            
            metrics = [
                {"label": "Natri (Na)", "value": f"{results['sodium_mmol']:.1f} mmol/ngày", "icon": "🧂"},
                {"label": "Kali (K)", "value": f"{results['potassium_mmol']:.1f} mmol/ngày", "icon": "🥬"},
                {"label": "Chloride (Cl)", "value": f"{results['chloride_mmol']:.1f} mmol/ngày", "icon": "🧪"},
            ]
            
            render_result_card("Nhu Cầu Điện Giải", metrics, color="info")
            
            st.markdown("---")
            st.markdown("### 💡 Thành Phần Dung Dịch")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**0.9% NaCl (NS)**")
                st.info("""
                - Na: 154 mmol/L
                - Cl: 154 mmol/L
                - K: 0 mmol/L
                """)
            
            with col2:
                st.markdown("**Lactated Ringer's**")
                st.info("""
                - Na: 130 mmol/L
                - Cl: 109 mmol/L
                - K: 4 mmol/L
                - Lactate: 28 mmol/L
                """)
            
            with col3:
                st.markdown("**D5W**")
                st.info("""
                - Na: 0 mmol/L
                - Cl: 0 mmol/L
                - K: 0 mmol/L
                - Glucose: 50 g/L
                """)
    
    # Disclaimer
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các tính toán này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Theo dõi điện giải và cân bằng dịch thường xuyên
    - Tuân thủ hướng dẫn địa phương và quy định bệnh viện
    """)

