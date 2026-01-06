"""
Warfarin Dosing Calculator
==========================

Calculate appropriate warfarin dose based on current INR, target INR, and clinical factors.

Reference:
- ACCP Guidelines for Antithrombotic Therapy
- AHA/ACC Guidelines for Atrial Fibrillation
- Warfarin dosing algorithms based on INR response

Clinical Utility:
- Guide warfarin dose adjustments
- Maintain therapeutic INR range
- Reduce bleeding and thrombotic complications
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================

from components.ui.scoring import render_score_result, render_score_breakdown
from scores.utils.validation import validate_age, validate_positive, validate_lab_value
from components.ui.validation import render_validation_errors

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
# ===================================================


def calculate_warfarin_dose(
    current_inr: float,
    target_inr_min: float,
    target_inr_max: float,
    current_daily_dose: float,
    days_since_last_dose_change: int = 7,
    age: int = None,
    weight_kg: float = None,
    indication: str = "atrial_fibrillation",
    drug_interactions: list = None,
    bleeding_risk: str = "low"
) -> dict:
    """
    Calculate recommended warfarin dose adjustment
    
    Args:
        current_inr: Current INR value
        target_inr_min: Minimum target INR
        target_inr_max: Maximum target INR
        current_daily_dose: Current daily warfarin dose (mg)
        days_since_last_dose_change: Days since last dose adjustment
        age: Patient age (years)
        weight_kg: Patient weight (kg)
        indication: Indication for warfarin
        drug_interactions: List of interacting drugs
        bleeding_risk: Bleeding risk level (low/medium/high)
    
    Returns:
        dict with recommended dose, adjustment percentage, and clinical guidance
    """
    target_inr_center = (target_inr_min + target_inr_max) / 2
    inr_ratio = current_inr / target_inr_center
    
    # Base dose adjustment algorithm
    if current_inr < target_inr_min:
        # INR too low - increase dose
        if current_inr < target_inr_min * 0.7:
            # Very low INR - increase by 15-20%
            dose_adjustment_pct = 20
            adjustment_reason = "INR rất thấp, tăng liều mạnh"
        elif current_inr < target_inr_min * 0.85:
            # Low INR - increase by 10-15%
            dose_adjustment_pct = 15
            adjustment_reason = "INR thấp, tăng liều vừa"
        else:
            # Slightly low INR - increase by 5-10%
            dose_adjustment_pct = 10
            adjustment_reason = "INR hơi thấp, tăng liều nhẹ"
    
    elif current_inr > target_inr_max:
        # INR too high - decrease dose
        if current_inr > target_inr_max * 1.5:
            # Very high INR - decrease by 20-25%
            dose_adjustment_pct = -25
            adjustment_reason = "INR rất cao, giảm liều mạnh"
        elif current_inr > target_inr_max * 1.3:
            # High INR - decrease by 15-20%
            dose_adjustment_pct = -20
            adjustment_reason = "INR cao, giảm liều vừa"
        else:
            # Slightly high INR - decrease by 5-15%
            dose_adjustment_pct = -10
            adjustment_reason = "INR hơi cao, giảm liều nhẹ"
    
    else:
        # INR in target range
        dose_adjustment_pct = 0
        adjustment_reason = "INR trong khoảng mục tiêu, giữ nguyên liều"
    
    # Adjust for days since last change
    if days_since_last_dose_change < 3:
        # Too soon to adjust - reduce adjustment
        dose_adjustment_pct = dose_adjustment_pct * 0.5
        adjustment_reason += " (chưa đủ thời gian để đánh giá)"
    
    # Adjust for age
    if age and age >= 75:
        # Elderly patients - more conservative adjustments
        dose_adjustment_pct = dose_adjustment_pct * 0.8
        adjustment_reason += " (điều chỉnh thận trọng ở người cao tuổi)"
    
    # Adjust for bleeding risk
    if bleeding_risk == "high":
        # High bleeding risk - more conservative
        dose_adjustment_pct = dose_adjustment_pct * 0.7
        adjustment_reason += " (nguy cơ chảy máu cao, điều chỉnh thận trọng)"
    elif bleeding_risk == "medium":
        dose_adjustment_pct = dose_adjustment_pct * 0.85
    
    # Calculate new dose
    new_daily_dose = current_daily_dose * (1 + dose_adjustment_pct / 100)
    
    # Round to practical dosing (0.5 mg increments for doses > 2mg, 0.25 mg for lower)
    if new_daily_dose >= 2:
        new_daily_dose = round(new_daily_dose * 2) / 2  # Round to 0.5
    else:
        new_daily_dose = round(new_daily_dose * 4) / 4  # Round to 0.25
    
    # Ensure minimum dose
    new_daily_dose = max(0.5, new_daily_dose)
    
    # Determine action needed
    if current_inr < target_inr_min:
        action = "Tăng liều"
        risk_level = "low" if current_inr > target_inr_min * 0.8 else "medium"
    elif current_inr > target_inr_max:
        action = "Giảm liều"
        risk_level = "high" if current_inr > target_inr_max * 1.3 else "medium"
    else:
        action = "Giữ nguyên liều"
        risk_level = "low"
    
    # Calculate time to next INR check
    if abs(dose_adjustment_pct) > 15:
        next_inr_days = 3
    elif abs(dose_adjustment_pct) > 5:
        next_inr_days = 5
    else:
        next_inr_days = 7
    
    return {
        "current_inr": current_inr,
        "target_inr_range": f"{target_inr_min}-{target_inr_max}",
        "target_inr_center": target_inr_center,
        "current_daily_dose": current_daily_dose,
        "new_daily_dose": new_daily_dose,
        "dose_change_mg": new_daily_dose - current_daily_dose,
        "dose_adjustment_pct": dose_adjustment_pct,
        "adjustment_reason": adjustment_reason,
        "action": action,
        "risk_level": risk_level,
        "next_inr_days": next_inr_days,
        "inr_status": "subtherapeutic" if current_inr < target_inr_min else ("supratherapeutic" if current_inr > target_inr_max else "therapeutic")
    }


def render():
    """Warfarin Dosing Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>💊 Warfarin Dosing Calculator</h3>
    """, unsafe_allow_html=True)
    st.caption("Tính toán liều warfarin dựa trên INR hiện tại và mục tiêu")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'warfarin_dosing':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin INR")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        current_inr = st.number_input(
            "INR hiện tại",
            min_value=0.5,
            max_value=10.0,
            value=float(shared_inputs.get('current_inr', 2.5)),
            step=0.1,
            format="%.2f",
            help="INR hiện tại của bệnh nhân"
        )
        
        st.markdown("### 🎯 INR Mục Tiêu")
        
        indication = st.selectbox(
            "Chỉ định dùng warfarin",
            [
                "atrial_fibrillation",
                "mechanical_valve",
                "dvt_pe",
                "other"
            ],
            format_func=lambda x: {
                "atrial_fibrillation": "Rung nhĩ (AF) - INR 2.0-3.0",
                "mechanical_valve": "Van cơ học - INR 2.5-3.5",
                "dvt_pe": "DVT/PE - INR 2.0-3.0",
                "other": "Khác (tùy chỉnh)"
            }[x],
            index=0
        )
        
        if indication == "other":
            col_inr1, col_inr2 = st.columns(2)
            with col_inr1:
                target_inr_min = st.number_input(
                    "INR mục tiêu tối thiểu",
                    min_value=1.0,
                    max_value=4.0,
                    value=2.0,
                    step=0.1,
                    format="%.1f"
                )
            with col_inr2:
                target_inr_max = st.number_input(
                    "INR mục tiêu tối đa",
                    min_value=1.0,
                    max_value=4.0,
                    value=3.0,
                    step=0.1,
                    format="%.1f"
                )
        elif indication == "mechanical_valve":
            target_inr_min = 2.5
            target_inr_max = 3.5
            st.info("INR mục tiêu: 2.5-3.5 (Van cơ học)")
        else:
            target_inr_min = 2.0
            target_inr_max = 3.0
            st.info("INR mục tiêu: 2.0-3.0 (Rung nhĩ/DVT/PE)")
        
        st.markdown("### 💊 Liều Warfarin Hiện Tại")
        
        current_daily_dose = st.number_input(
            "Liều hàng ngày hiện tại (mg)",
            min_value=0.5,
            max_value=20.0,
            value=float(shared_inputs.get('current_daily_dose', 5.0)),
            step=0.25,
            format="%.2f",
            help="Liều warfarin hàng ngày hiện tại"
        )
        
        days_since_change = st.number_input(
            "Số ngày kể từ lần điều chỉnh liều cuối",
            min_value=0,
            max_value=30,
            value=int(shared_inputs.get('days_since_change', 7)),
            help="Thời gian để INR ổn định sau điều chỉnh liều"
        )
        
        st.markdown("### 👤 Thông tin bệnh nhân (Tùy chọn)")
        
        col_age, col_weight = st.columns(2)
        with col_age:
            age = st.number_input(
                "Tuổi (năm)",
                min_value=18,
                max_value=120,
                value=int(shared_inputs.get('age', 65)) if shared_inputs.get('age') else None,
                step=1,
                help="Tuổi bệnh nhân (ảnh hưởng đến điều chỉnh liều)"
            )
        with col_weight:
            weight_kg = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=200.0,
                value=float(shared_inputs.get('weight_kg', 70.0)) if shared_inputs.get('weight_kg') else None,
                step=0.5,
                format="%.1f",
                help="Cân nặng bệnh nhân"
            )
        
        bleeding_risk = st.selectbox(
            "Nguy cơ chảy máu",
            ["low", "medium", "high"],
            format_func=lambda x: {
                "low": "Thấp",
                "medium": "Trung bình",
                "high": "Cao"
            }[x],
            index=0,
            help="Đánh giá nguy cơ chảy máu của bệnh nhân"
        )
        
        # Validation
        errors = []
        if target_inr_min >= target_inr_max:
            errors.append("INR mục tiêu tối thiểu phải nhỏ hơn tối đa")
        if current_daily_dose <= 0:
            errors.append("Liều warfarin phải > 0")
        
        if errors:
            render_validation_errors(errors)
            return
        
        # Calculate
        if st.button("🔄 Tính Toán Liều Warfarin", type="primary", use_container_width=True):
            result = calculate_warfarin_dose(
                current_inr=current_inr,
                target_inr_min=target_inr_min,
                target_inr_max=target_inr_max,
                current_daily_dose=current_daily_dose,
                days_since_last_dose_change=days_since_change,
                age=age if age else None,
                weight_kg=weight_kg if weight_kg else None,
                indication=indication,
                bleeding_risk=bleeding_risk
            )
            
            st.session_state['warfarin_result'] = result
            
            # Display results
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            # Risk badge
            risk_color = {
                "low": COLORS['success'],
                "medium": COLORS['warning'],
                "high": COLORS['danger']
            }.get(result['risk_level'], COLORS['info'])
            
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                st.metric(
                    "INR Hiện Tại",
                    f"{result['current_inr']:.2f}",
                    delta=f"Mục tiêu: {result['target_inr_range']}"
                )
            
            with col_res2:
                st.metric(
                    "Liều Hiện Tại",
                    f"{result['current_daily_dose']:.2f} mg/ngày"
                )
            
            with col_res3:
                dose_change = result['dose_change_mg']
                st.metric(
                    "Liều Đề Xuất",
                    f"{result['new_daily_dose']:.2f} mg/ngày",
                    delta=f"{dose_change:+.2f} mg" if abs(dose_change) > 0.01 else "Không đổi"
                )
            
            # Action box
            if result['inr_status'] == "therapeutic":
                st.success(f"✅ **{result['action']}** - {result['adjustment_reason']}")
            elif result['inr_status'] == "subtherapeutic":
                st.warning(f"⚠️ **{result['action']}** - {result['adjustment_reason']}")
            else:
                st.error(f"🚨 **{result['action']}** - {result['adjustment_reason']}")
            
            # Detailed breakdown
            with st.expander("📋 Chi tiết Điều Chỉnh Liều", expanded=True):
                st.markdown(f"""
                **Lý do điều chỉnh:** {result['adjustment_reason']}
                
                **Thay đổi liều:** {result['dose_adjustment_pct']:+.1f}%
                
                **Liều mới:** {result['new_daily_dose']:.2f} mg/ngày
                
                **Thời gian kiểm tra INR tiếp theo:** {result['next_inr_days']} ngày
                """)
            
            # Clinical guidance
            st.markdown("### 💡 Hướng Dẫn Lâm Sàng")
            
            if result['inr_status'] == "subtherapeutic":
                st.info("""
                **INR dưới mục tiêu:**
                - Tăng liều warfarin theo đề xuất
                - Kiểm tra INR sau 3-5 ngày
                - Xem xét các yếu tố ảnh hưởng: thuốc tương tác, chế độ ăn, tuân thủ
                - Cân nhắc tạm thời dùng heparin/LMWH nếu nguy cơ huyết khối cao
                """)
            elif result['inr_status'] == "supratherapeutic":
                st.warning("""
                **INR trên mục tiêu:**
                - Giảm liều warfarin theo đề xuất
                - Kiểm tra INR sau 3-5 ngày
                - Theo dõi dấu hiệu chảy máu
                - Nếu INR > 5.0: xem xét ngừng warfarin, dùng vitamin K nếu cần
                """)
            else:
                st.success("""
                **INR trong khoảng mục tiêu:**
                - Giữ nguyên liều hiện tại
                - Tiếp tục theo dõi INR định kỳ
                - Duy trì liều ổn định
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="warfarin_dosing",
                calculator_name="Warfarin Dosing Calculator",
                inputs={
                    "INR hiện tại": f"{current_inr:.2f}",
                    "INR mục tiêu": f"{target_inr_min}-{target_inr_max}",
                    "Liều hiện tại": f"{current_daily_dose:.2f} mg/ngày",
                    "Chỉ định": indication
                },
                result={
                    "Liều đề xuất": f"{result['new_daily_dose']:.2f} mg/ngày",
                    "Thay đổi": f"{result['dose_adjustment_pct']:+.1f}%",
                    "Hành động": result['action']
                }
            )
            
            render_share_section(
                calculator_id="warfarin_dosing",
                calculator_name="Warfarin Dosing Calculator"
            )
            render_scores_export(
                calculator_id="warfarin_dosing",
                calculator_name="Warfarin Dosing Calculator",
                data={"result": result}
            )
            render_suggestions(calculator_id="warfarin_dosing", result=result)
    
    with col2:
        st.markdown("### 📚 Thông tin")
        
        st.markdown("""
        **Warfarin Dosing:**
        
        - Dựa trên INR hiện tại và mục tiêu
        - Điều chỉnh liều từng bước
        - Kiểm tra INR thường xuyên
        
        **INR Mục Tiêu:**
        - Rung nhĩ: 2.0-3.0
        - Van cơ học: 2.5-3.5
        - DVT/PE: 2.0-3.0
        
        **Lưu ý:**
        - Điều chỉnh liều từng bước (5-20%)
        - Đợi 3-7 ngày giữa các lần điều chỉnh
        - Xem xét các yếu tố ảnh hưởng
        """)
        
        if st.session_state.get('warfarin_result'):
            result = st.session_state['warfarin_result']
            render_risk_badge(
                result['risk_level'],
                result['action'],
                size="large"
            )
    
    render_history_ui(calculator_id="warfarin_dosing", show_actions=True)
    references = get_references("Warfarin Dosing")
    if references:
        render_references_section(references)

