"""
Transfusion Protocol Calculator
Blood product transfusion dosing and guidelines
"""

import streamlit as st
from components.ui.inputs import render_number_input_with_unit
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def calculate_prbc_transfusion(weight_kg: float, current_hgb: float, target_hgb: float, 
                                hgb_units: str = "g/dL") -> dict:
    """
    Calculate PRBC transfusion requirements
    
    Args:
        weight_kg: Patient weight in kg
        current_hgb: Current hemoglobin level
        target_hgb: Target hemoglobin level
        hgb_units: Units for hemoglobin (g/dL or g/L)
    
    Returns:
        Dictionary with transfusion calculations
    """
    # Convert units if needed
    if hgb_units == "g/L":
        current_hgb = current_hgb / 10
        target_hgb = target_hgb / 10
    
    # Calculate Hgb deficit
    hgb_deficit = target_hgb - current_hgb
    
    # One unit of PRBC typically raises Hgb by ~1 g/dL (or ~10 g/L)
    # For adults: 1 unit ≈ 250-300 ml, raises Hgb by ~1 g/dL
    # Expected rise: ~1 g/dL per unit in adults (70 kg)
    
    # Adjusted for weight: expected rise = (1 g/dL) * (70 / weight_kg)
    expected_rise_per_unit = 1.0 * (70 / weight_kg) if weight_kg > 0 else 1.0
    
    # Calculate units needed
    if hgb_deficit > 0:
        units_needed = hgb_deficit / expected_rise_per_unit
        units_needed = max(1, round(units_needed, 1))  # Minimum 1 unit
    else:
        units_needed = 0
    
    # Volume calculation (1 unit ≈ 250-300 ml)
    volume_ml = units_needed * 275  # Average
    
    # Expected Hgb after transfusion
    expected_hgb_after = current_hgb + (units_needed * expected_rise_per_unit)
    
    return {
        "units_needed": units_needed,
        "volume_ml": volume_ml,
        "volume_liters": volume_ml / 1000,
        "expected_hgb_rise": units_needed * expected_rise_per_unit,
        "expected_hgb_after": expected_hgb_after,
        "hgb_deficit": hgb_deficit
    }


def calculate_platelet_transfusion(weight_kg: float, current_platelet: int, 
                                   target_platelet: int, platelet_type: str = "apheresis") -> dict:
    """
    Calculate platelet transfusion requirements
    
    Args:
        weight_kg: Patient weight in kg
        current_platelet: Current platelet count (x10^9/L)
        target_platelet: Target platelet count (x10^9/L)
        platelet_type: Type of platelet product (apheresis or pooled)
    
    Returns:
        Dictionary with platelet transfusion calculations
    """
    # Calculate deficit
    platelet_deficit = target_platelet - current_platelet
    
    if platelet_deficit <= 0:
        return {
            "units_needed": 0,
            "expected_rise": 0,
            "expected_platelet_after": current_platelet,
            "platelet_deficit": 0
        }
    
    # Expected rise per unit
    # Apheresis: 1 unit ≈ 30-60 x10^9/L rise (adult 70 kg)
    # Pooled: 1 unit ≈ 20-40 x10^9/L rise (adult 70 kg)
    
    if platelet_type == "apheresis":
        base_rise_per_unit = 45  # x10^9/L for 70 kg adult
    else:  # pooled
        base_rise_per_unit = 30  # x10^9/L for 70 kg adult
    
    # Adjust for weight
    expected_rise_per_unit = base_rise_per_unit * (70 / weight_kg) if weight_kg > 0 else base_rise_per_unit
    
    # Calculate units needed
    units_needed = max(1, round(platelet_deficit / expected_rise_per_unit))
    
    # Expected platelet count after transfusion
    expected_platelet_after = current_platelet + (units_needed * expected_rise_per_unit)
    
    return {
        "units_needed": units_needed,
        "expected_rise": units_needed * expected_rise_per_unit,
        "expected_platelet_after": expected_platelet_after,
        "platelet_deficit": platelet_deficit,
        "platelet_type": platelet_type
    }


def calculate_ffp_transfusion(weight_kg: float, current_inr: float, target_inr: float = 1.5) -> dict:
    """
    Calculate FFP transfusion for coagulopathy correction
    
    Args:
        weight_kg: Patient weight in kg
        current_inr: Current INR
        target_inr: Target INR (typically 1.5 for correction)
    
    Returns:
        Dictionary with FFP transfusion calculations
    """
    # Typical FFP dose: 10-15 ml/kg
    # One unit of FFP ≈ 200-250 ml
    
    # Calculate dose based on INR
    if current_inr > 2.5:
        ml_per_kg = 15
    elif current_inr > 1.5:
        ml_per_kg = 10
    else:
        ml_per_kg = 0  # No transfusion needed
    
    total_ml = weight_kg * ml_per_kg
    units_needed = max(1, round(total_ml / 225))  # Average unit size
    
    # Adjust to actual volume
    actual_ml = units_needed * 225
    
    return {
        "units_needed": units_needed,
        "volume_ml": actual_ml,
        "volume_liters": actual_ml / 1000,
        "ml_per_kg": ml_per_kg,
        "current_inr": current_inr,
        "target_inr": target_inr
    }


def calculate_massive_transfusion(blood_loss_ml: float, protocol_type: str = "trauma") -> dict:
    """
    Calculate massive transfusion protocol (1:1:1 ratio)
    
    Args:
        blood_loss_ml: Estimated blood loss in ml
        protocol_type: Type of protocol (trauma or non-trauma)
    
    Returns:
        Dictionary with MTP calculations
    """
    # 1:1:1 ratio = PRBC:FFP:Platelets
    # Typically: 1 unit PRBC : 1 unit FFP : 1 unit platelets
    
    # Estimate blood loss as percentage of blood volume
    # Average adult blood volume ≈ 70 ml/kg
    
    # Calculate units based on blood loss
    # Rule of thumb: Replace 1:1 with blood loss
    # If loss > 50% blood volume → Massive transfusion
    
    # Calculate units needed (approximate)
    # 1 unit PRBC ≈ 250 ml
    prbc_units = max(1, round(blood_loss_ml / 250))
    
    # 1:1:1 ratio
    ffp_units = prbc_units
    platelet_units = prbc_units
    
    # Additional considerations
    # Calcium repletion: 1-2 g CaCl2 per 4 units PRBC
    calcium_grams = max(1, round(prbc_units / 4))
    
    # Cryoprecipitate: 1 unit per 10 kg (if fibrinogen < 100)
    cryo_units = max(0, round(70 / 10))  # For average 70 kg adult
    
    return {
        "prbc_units": prbc_units,
        "ffp_units": ffp_units,
        "platelet_units": platelet_units,
        "calcium_grams": calcium_grams,
        "cryo_units": cryo_units,
        "protocol_type": protocol_type,
        "estimated_blood_loss_ml": blood_loss_ml
    }


def render_prbc_calculator():
    """Render PRBC transfusion calculator"""
    st.subheader("🩸 Truyền Hồng Cầu (PRBC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="prbc_weight"
        )
        
        hgb_units = st.radio(
            "Đơn vị Hemoglobin",
            ["g/dL", "g/L"],
            key="prbc_hgb_units"
        )
    
    with col2:
        current_hgb = st.number_input(
            f"Hemoglobin hiện tại ({hgb_units})",
            min_value=1.0,
            max_value=25.0 if hgb_units == "g/dL" else 250.0,
            value=7.0 if hgb_units == "g/dL" else 70.0,
            step=0.1,
            format="%.1f",  # Chỉ hiển thị 1 số thập phân
            key="prbc_current_hgb"
        )
        
        target_hgb = st.number_input(
            f"Hemoglobin mục tiêu ({hgb_units})",
            min_value=1.0,
            max_value=25.0 if hgb_units == "g/dL" else 250.0,
            value=10.0 if hgb_units == "g/dL" else 100.0,
            step=0.1,
            format="%.1f",  # Chỉ hiển thị 1 số thập phân
            key="prbc_target_hgb"
        )
    
    # Calculate
    if st.button("📊 Tính Toán", key="prbc_calculate", type="primary"):
        result = calculate_prbc_transfusion(weight_kg, current_hgb, target_hgb, hgb_units)
        
        if result["units_needed"] > 0:
            st.success(f"**Cần truyền:** {result['units_needed']} đơn vị PRBC")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                render_result_card(
                    f"{result['volume_ml']:.0f} ml",
                    "Tổng thể tích",
                    "blue"
                )
            with col2:
                render_result_card(
                    f"+{result['expected_hgb_rise']:.1f} {hgb_units}",
                    "Dự kiến tăng Hb",
                    "green"
                )
            with col3:
                render_result_card(
                    f"{result['expected_hgb_after']:.1f} {hgb_units}",
                    "Hb sau truyền",
                    "purple"
                )
            
            # Guidelines
            st.markdown("---")
            st.markdown("### 📋 Hướng Dẫn")
            
            if current_hgb < 7.0 if hgb_units == "g/dL" else current_hgb < 70:
                render_warning_alert(
                    "⚠️ Thiếu máu nặng",
                    "Xem xét truyền ngay. Ngưỡng truyền thường < 7 g/dL (hoặc < 8 g/dL nếu có bệnh tim mạch)"
                )
            elif current_hgb < 8.0 if hgb_units == "g/dL" else current_hgb < 80:
                render_info_alert(
                    "ℹ️ Thiếu máu trung bình",
                    "Ngưỡng truyền: < 8 g/dL nếu có bệnh tim mạch, phẫu thuật, hoặc chảy máu cấp"
                )
            else:
                render_info_alert(
                    "ℹ️ Thiếu máu nhẹ",
                    "Thường không cần truyền trừ khi có triệu chứng hoặc chảy máu cấp"
                )
        else:
            st.info("Hemoglobin hiện tại đã đạt mục tiêu, không cần truyền.")


def render_platelet_calculator():
    """Render platelet transfusion calculator"""
    st.subheader("🩸 Truyền Tiểu Cầu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="platelet_weight"
        )
        
        platelet_type = st.selectbox(
            "Loại tiểu cầu",
            ["apheresis", "pooled"],
            format_func=lambda x: "Apheresis (1 đơn vị)" if x == "apheresis" else "Pooled (6 đơn vị)",
            key="platelet_type"
        )
    
    with col2:
        current_platelet = st.number_input(
            "Số lượng tiểu cầu hiện tại (x10⁹/L)",
            min_value=0,
            max_value=1000,
            value=20,
            step=1,
            format="%d",
            key="platelet_current"
        )
        
        target_platelet = st.number_input(
            "Số lượng tiểu cầu mục tiêu (x10⁹/L)",
            min_value=0,
            max_value=1000,
            value=50,
            step=1,
            format="%d",
            key="platelet_target"
        )
    
    # Calculate
    if st.button("📊 Tính Toán", key="platelet_calculate", type="primary"):
        result = calculate_platelet_transfusion(weight_kg, current_platelet, target_platelet, platelet_type)
        
        if result["units_needed"] > 0:
            st.success(f"**Cần truyền:** {result['units_needed']} đơn vị tiểu cầu")
            
            col1, col2 = st.columns(2)
            with col1:
                render_result_card(
                    f"+{result['expected_rise']:.0f} x10⁹/L",
                    "Dự kiến tăng",
                    "green"
                )
            with col2:
                render_result_card(
                    f"{result['expected_platelet_after']:.0f} x10⁹/L",
                    "Số lượng sau truyền",
                    "purple"
                )
            
            # Guidelines
            st.markdown("---")
            st.markdown("### 📋 Ngưỡng Truyền Tiểu Cầu")
            
            if current_platelet < 10:
                render_warning_alert(
                    "⚠️ Nguy cơ chảy máu cao",
                    "Truyền ngay khi < 10 x10⁹/L (ngay cả khi không chảy máu)"
                )
            elif current_platelet < 20:
                render_warning_alert(
                    "⚠️ Chảy máu tự phát",
                    "Truyền khi < 20 x10⁹/L nếu có chảy máu hoặc phẫu thuật"
                )
            elif current_platelet < 50:
                render_info_alert(
                    "ℹ️ Phẫu thuật",
                    "Truyền khi < 50 x10⁹/L trước phẫu thuật lớn hoặc chảy máu"
                )
            else:
                render_info_alert(
                    "ℹ️ Mức an toàn",
                    "Thường không cần truyền trừ khi có chảy máu hoặc phẫu thuật lớn"
                )
        else:
            st.info("Số lượng tiểu cầu đã đạt mục tiêu.")


def render_ffp_calculator():
    """Render FFP/Cryoprecipitate calculator"""
    st.subheader("🩸 Truyền Huyết Tương (FFP) / Cryoprecipitate")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="ffp_weight"
        )
        
        current_inr = st.number_input(
            "INR hiện tại",
            min_value=1.0,
            max_value=10.0,
            value=2.5,
            step=0.1,
            format="%.1f",
            key="ffp_current_inr"
        )
    
    with col2:
        target_inr = st.number_input(
            "INR mục tiêu",
            min_value=1.0,
            max_value=3.0,
            value=1.5,
            step=0.1,
            format="%.1f",
            key="ffp_target_inr"
        )
        
        fibrinogen = st.number_input(
            "Fibrinogen (mg/dL)",
            min_value=0.0,
            max_value=1000.0,
            value=150.0,
            step=10.0,
            format="%.0f",
            key="ffp_fibrinogen",
            help="Cần cho tính toán Cryoprecipitate"
        )
    
    # Calculate
    if st.button("📊 Tính Toán", key="ffp_calculate", type="primary"):
        result = calculate_ffp_transfusion(weight_kg, current_inr, target_inr)
        
        if result["units_needed"] > 0:
            st.success(f"**Cần truyền:** {result['units_needed']} đơn vị FFP")
            
            col1, col2 = st.columns(2)
            with col1:
                render_result_card(
                    f"{result['volume_ml']:.0f} ml",
                    "Tổng thể tích",
                    "blue"
                )
            with col2:
                render_result_card(
                    f"{result['ml_per_kg']:.0f} ml/kg",
                    "Liều/kg",
                    "green"
                )
            
            # Cryoprecipitate if needed
            if fibrinogen < 100:
                cryo_units = max(1, round(weight_kg / 10))
                st.warning(f"**Cần thêm Cryoprecipitate:** {cryo_units} đơn vị (Fibrinogen < 100 mg/dL)")
            
            # Guidelines
            st.markdown("---")
            st.markdown("### 📋 Chỉ định truyền FFP")
            
            render_info_alert(
                "ℹ️ Chỉ định chính",
                """
                - INR > 1.5 và chảy máu hoặc trước phẫu thuật
                - INR > 2.5 (ngay cả khi không chảy máu)
                - Thiếu hụt yếu tố đông máu đã biết
                - Đảo ngược thuốc chống đông (warfarin)
                """
            )
        else:
            st.info("INR hiện tại đã ở mức an toàn, không cần truyền FFP.")


def render_massive_transfusion_calculator():
    """Render massive transfusion protocol calculator"""
    st.subheader("🩸 Massive Transfusion Protocol (MTP)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        blood_loss_ml = st.number_input(
            "Lượng máu mất ước tính (ml)",
            min_value=0,
            max_value=10000,
            value=2000,
            step=100,
            format="%d",
            key="mtp_blood_loss"
        )
        
        protocol_type = st.selectbox(
            "Loại protocol",
            ["trauma", "non-trauma"],
            format_func=lambda x: "Chấn thương" if x == "trauma" else "Không chấn thương",
            key="mtp_protocol_type"
        )
    
    with col2:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="mtp_weight"
        )
        
        estimated_blood_volume_ml = weight_kg * 70  # Average blood volume
        blood_loss_percent = (blood_loss_ml / estimated_blood_volume_ml) * 100
        
        st.metric(
            "Mất máu (%)",
            f"{blood_loss_percent:.1f}%",
            help=f"Tổng thể tích máu ước tính: {estimated_blood_volume_ml:.0f} ml"
        )
    
    # Calculate
    if st.button("📊 Tính Toán", key="mtp_calculate", type="primary"):
        result = calculate_massive_transfusion(blood_loss_ml, protocol_type)
        
        st.success("**Kế hoạch truyền máu (Tỷ lệ 1:1:1):**")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_result_card(
                f"{result['prbc_units']} đơn vị",
                "Hồng cầu (PRBC)",
                "red"
            )
        with col2:
            render_result_card(
                f"{result['ffp_units']} đơn vị",
                "Huyết tương (FFP)",
                "blue"
            )
        with col3:
            render_result_card(
                f"{result['platelet_units']} đơn vị",
                "Tiểu cầu",
                "purple"
            )
        with col4:
            render_result_card(
                f"{result['calcium_grams']} g",
                "Canxi (CaCl₂)",
                "orange"
            )
        
        if result['cryo_units'] > 0:
            st.info(f"**Cryoprecipitate:** {result['cryo_units']} đơn vị (nếu fibrinogen < 100)")
        
        # Guidelines
        st.markdown("---")
        st.markdown("### 📋 Massive Transfusion Protocol")
        
        render_warning_alert(
            "⚠️ Chỉ định",
            "Mất máu > 50% thể tích máu hoặc > 4 đơn vị PRBC trong 1 giờ"
        )
        
        render_info_alert(
            "ℹ️ Tỷ lệ 1:1:1",
            """
            - PRBC : FFP : Platelets = 1:1:1
            - Canxi: 1-2 g CaCl₂ mỗi 4 đơn vị PRBC
            - Theo dõi: INR, Fibrinogen, Ca²⁺, pH, Lactate
            - Hồi sức cầm máu (hemostatic resuscitation)
            """
        )


def render_transfusion_calculator():
    """Main function to render transfusion calculator"""
    st.header("🩸 Transfusion Protocol Calculator")
    st.caption("Tính toán liều truyền máu và các sản phẩm máu")
    
    # Calculator selection
    calculator_type = st.selectbox(
        "Chọn loại tính toán:",
        [
            "🩸 Truyền Hồng Cầu (PRBC)",
            "🩸 Truyền Tiểu Cầu",
            "🩸 Truyền Huyết Tương (FFP)",
            "🩸 Massive Transfusion Protocol"
        ],
        key="transfusion_calc_type"
    )
    
    st.markdown("---")
    
    # Route to appropriate calculator
    if "PRBC" in calculator_type or "Hồng Cầu" in calculator_type:
        render_prbc_calculator()
    elif "Tiểu Cầu" in calculator_type:
        render_platelet_calculator()
    elif "FFP" in calculator_type or "Huyết Tương" in calculator_type:
        render_ffp_calculator()
    elif "Massive" in calculator_type or "MTP" in calculator_type:
        render_massive_transfusion_calculator()
    
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")

