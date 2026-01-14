"""
Lactulose Calculator
====================

Calculate appropriate lactulose dosing for hepatic encephalopathy.

Reference:
- AASLD Practice Guidelines: Management of Hepatic Encephalopathy (2014)
- EASL Clinical Practice Guidelines on the management of hepatic encephalopathy (2022)
- AGA Clinical Practice Update on the Management of Hepatic Encephalopathy (2022)

Clinical Utility:
- Guide lactulose dosing for hepatic encephalopathy
- Achieve target bowel movements (2-3 soft stools/day)
- Prevent over/under-dosing
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
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.scores_export import render_export_section as render_scores_export


def calculate_lactulose_dose(
    he_grade: int = 1,
    current_bm_frequency: float = 1.0,
    weight_kg: float = 70.0,
    ammonia_level: float = None,
    current_dose_ml: float = None,
    current_dose_g: float = None
) -> dict:
    """
    Calculate appropriate lactulose dosing for hepatic encephalopathy
    
    Args:
        he_grade: Hepatic encephalopathy grade (1-4)
        current_bm_frequency: Current bowel movement frequency per day
        weight_kg: Patient weight (kg)
        ammonia_level: Blood ammonia level (μmol/L) - optional
        current_dose_ml: Current lactulose dose in mL
        current_dose_g: Current lactulose dose in grams
    
    Returns:
        dict with recommended dose, adjustments, and clinical guidance
    """
    # Target: 2-3 soft bowel movements per day
    target_bm_min = 2.0
    target_bm_max = 3.0
    
    # Base dosing recommendations by HE grade
    # Lactulose syrup: 10g/15mL
    base_dose_ml = {
        1: 15,  # Mild: 15-30 mL BID-TID
        2: 30,  # Moderate: 30-45 mL TID-QID
        3: 45,  # Severe: 45-60 mL QID
        4: 60   # Coma: 60 mL QID + retention enema
    }
    
    base_dose_g = {
        1: 10,  # 10-20g BID-TID
        2: 20,  # 20-30g TID-QID
        3: 30,  # 30-40g QID
        4: 40   # 40g QID + retention enema
    }
    
    frequency = {
        1: "BID-TID",  # 2-3 times daily
        2: "TID-QID",  # 3-4 times daily
        3: "QID",      # 4 times daily
        4: "QID + Enema"  # 4 times daily + retention enema
    }
    
    # Get base dose
    recommended_dose_ml = base_dose_ml.get(he_grade, 30)
    recommended_dose_g = base_dose_g.get(he_grade, 20)
    recommended_frequency = frequency.get(he_grade, "TID")
    
    # Adjust based on current BM frequency
    dose_adjustment = 0
    adjustment_reason = ""
    
    if current_bm_frequency < target_bm_min:
        # Too few BMs - increase dose
        if current_bm_frequency < 1:
            dose_adjustment = 1.5  # Increase by 50%
            adjustment_reason = "Số lần đi ngoài quá ít, cần tăng liều mạnh"
        elif current_bm_frequency < 1.5:
            dose_adjustment = 1.25  # Increase by 25%
            adjustment_reason = "Số lần đi ngoài ít, cần tăng liều"
        else:
            dose_adjustment = 1.1  # Increase by 10%
            adjustment_reason = "Số lần đi ngoài hơi ít, tăng liều nhẹ"
    elif current_bm_frequency > target_bm_max:
        # Too many BMs - decrease dose
        if current_bm_frequency > 5:
            dose_adjustment = 0.5  # Decrease by 50%
            adjustment_reason = "Số lần đi ngoài quá nhiều, giảm liều mạnh"
        elif current_bm_frequency > 4:
            dose_adjustment = 0.7  # Decrease by 30%
            adjustment_reason = "Số lần đi ngoài nhiều, giảm liều"
        else:
            dose_adjustment = 0.9  # Decrease by 10%
            adjustment_reason = "Số lần đi ngoài hơi nhiều, giảm liều nhẹ"
    else:
        # Target range
        dose_adjustment = 1.0
        adjustment_reason = "Số lần đi ngoài trong khoảng mục tiêu, giữ nguyên liều"
    
    # Adjust recommended dose
    adjusted_dose_ml = recommended_dose_ml * dose_adjustment
    adjusted_dose_g = recommended_dose_g * dose_adjustment
    
    # Round to practical dosing (5mL increments for mL, 5g increments for grams)
    adjusted_dose_ml = round(adjusted_dose_ml / 5) * 5
    adjusted_dose_g = round(adjusted_dose_g / 5) * 5
    
    # Ensure minimum dose
    adjusted_dose_ml = max(10, adjusted_dose_ml)
    adjusted_dose_g = max(10, adjusted_dose_g)
    
    # Calculate daily total
    if he_grade == 1:
        daily_total_ml = adjusted_dose_ml * 2.5  # Average BID-TID
        daily_total_g = adjusted_dose_g * 2.5
    elif he_grade == 2:
        daily_total_ml = adjusted_dose_ml * 3.5  # Average TID-QID
        daily_total_g = adjusted_dose_g * 3.5
    else:
        daily_total_ml = adjusted_dose_ml * 4  # QID
        daily_total_g = adjusted_dose_g * 4
    
    # Determine risk level
    if current_bm_frequency < target_bm_min:
        risk_level = "moderate" if current_bm_frequency < 1 else "low"
    elif current_bm_frequency > target_bm_max:
        risk_level = "high" if current_bm_frequency > 5 else "moderate"
    else:
        risk_level = "low"
    
    # Recommendations
    recommendations = []
    
    if he_grade == 1:
        recommendations.extend([
            "Điều trị HE nhẹ (Grade 1)",
            f"Liều khởi đầu: {adjusted_dose_ml} mL ({adjusted_dose_g}g) {recommended_frequency}",
            f"Tổng liều hàng ngày: ~{daily_total_ml:.0f} mL (~{daily_total_g:.0f}g)",
            "Điều chỉnh liều để đạt 2-3 lần đi ngoài mềm/ngày",
            "Theo dõi triệu chứng và tần suất đi ngoài"
        ])
    elif he_grade == 2:
        recommendations.extend([
            "Điều trị HE trung bình (Grade 2)",
            f"Liều khởi đầu: {adjusted_dose_ml} mL ({adjusted_dose_g}g) {recommended_frequency}",
            f"Tổng liều hàng ngày: ~{daily_total_ml:.0f} mL (~{daily_total_g:.0f}g)",
            "Điều chỉnh liều để đạt 2-3 lần đi ngoài mềm/ngày",
            "Theo dõi sát triệu chứng thần kinh",
            "Xem xét thêm rifaximin nếu không đáp ứng"
        ])
    elif he_grade == 3:
        recommendations.extend([
            "Điều trị HE nặng (Grade 3)",
            f"Liều khởi đầu: {adjusted_dose_ml} mL ({adjusted_dose_g}g) {recommended_frequency}",
            f"Tổng liều hàng ngày: ~{daily_total_ml:.0f} mL (~{daily_total_g:.0f}g)",
            "Điều chỉnh liều để đạt 2-3 lần đi ngoài mềm/ngày",
            "Theo dõi sát trong ICU",
            "Xem xét thêm rifaximin và điều trị nguyên nhân"
        ])
    else:  # Grade 4
        recommendations.extend([
            "Điều trị HE hôn mê (Grade 4)",
            f"Liều uống: {adjusted_dose_ml} mL ({adjusted_dose_g}g) {recommended_frequency}",
            f"Thêm thụt giữ: 200-300 mL lactulose pha loãng",
            f"Tổng liều hàng ngày: ~{daily_total_ml:.0f} mL (~{daily_total_g:.0f}g) + enema",
            "Theo dõi sát trong ICU",
            "Điều trị nguyên nhân khởi phát",
            "Xem xét thêm rifaximin và các biện pháp khác"
        ])
    
    # Add adjustment-specific recommendations
    if current_bm_frequency < target_bm_min:
        recommendations.append(f"⚠️ {adjustment_reason}")
        recommendations.append("Tăng liều từng bước, đánh giá sau 2-3 ngày")
    elif current_bm_frequency > target_bm_max:
        recommendations.append(f"⚠️ {adjustment_reason}")
        recommendations.append("Giảm liều từng bước, tránh táo bón")
    
    # Ammonia guidance
    if ammonia_level:
        if ammonia_level > 100:
            recommendations.append(f"⚠️ Ammonia cao ({ammonia_level:.0f} μmol/L) - cần điều trị tích cực")
        elif ammonia_level > 50:
            recommendations.append(f"ℹ️ Ammonia tăng ({ammonia_level:.0f} μmol/L) - theo dõi sát")
    
    # Warnings
    warnings = []
    if current_bm_frequency > 5:
        warnings.append("🚨 Số lần đi ngoài quá nhiều - nguy cơ mất nước, rối loạn điện giải")
    if he_grade >= 3:
        warnings.append("🚨 HE nặng - cần điều trị tích cực và theo dõi ICU")
    if ammonia_level and ammonia_level > 150:
        warnings.append("🚨 Ammonia rất cao - cần điều trị khẩn cấp")
    
    return {
        "he_grade": he_grade,
        "current_bm_frequency": current_bm_frequency,
        "target_bm_range": f"{target_bm_min}-{target_bm_max}",
        "weight_kg": weight_kg,
        "ammonia_level": ammonia_level,
        "recommended_dose_ml": adjusted_dose_ml,
        "recommended_dose_g": adjusted_dose_g,
        "recommended_frequency": recommended_frequency,
        "daily_total_ml": daily_total_ml,
        "daily_total_g": daily_total_g,
        "dose_adjustment": dose_adjustment,
        "adjustment_reason": adjustment_reason,
        "risk_level": risk_level,
        "recommendations": recommendations,
        "warnings": warnings,
        "interpretation": f"Liều đề xuất: {adjusted_dose_ml} mL ({adjusted_dose_g}g) {recommended_frequency}"
    }


def render():
    """Render the Lactulose Calculator interface"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>💊 Lactulose Calculator</h3>
    """, unsafe_allow_html=True)
    st.caption("Tính toán liều lactulose cho bệnh nhân bệnh não gan")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'lactulose_calculator':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin bệnh nhân")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        # HE Grade
        he_grade = st.selectbox(
            "Grade bệnh não gan (HE)",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "Grade 1 - Nhẹ (thay đổi nhẹ, rối loạn giấc ngủ)",
                2: "Grade 2 - Trung bình (lơ mơ, thay đổi tính cách)",
                3: "Grade 3 - Nặng (ngủ gà, lú lẫn)",
                4: "Grade 4 - Hôn mê"
            }[x],
            index=0,
            help="Mức độ bệnh não gan theo West Haven Criteria"
        )
        
        # Current BM frequency
        current_bm_frequency = st.number_input(
            "Tần suất đi ngoài hiện tại (lần/ngày)",
            min_value=0.0,
            max_value=10.0,
            value=float(shared_inputs.get('current_bm_frequency', 1.0)),
            step=0.5,
            format="%.1f",
            help="Số lần đi ngoài mỗi ngày hiện tại (mục tiêu: 2-3 lần/ngày)"
        )
        
        # Weight
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=float(shared_inputs.get('weight_kg', 70.0)),
            step=0.5,
            format="%.1f",
            help="Cân nặng bệnh nhân"
        )
        
        # Ammonia (optional)
        ammonia_level = st.number_input(
            "Ammonia máu (μmol/L) - Tùy chọn",
            min_value=0.0,
            max_value=500.0,
            value=float(shared_inputs.get('ammonia_level')) if shared_inputs.get('ammonia_level') else None,
            step=1.0,
            format="%.0f",
            help="Nồng độ ammonia trong máu (bình thường: <50 μmol/L)"
        )
        
        # Current dose (optional)
        st.markdown("### 💊 Liều Hiện Tại (Tùy chọn)")
        col_dose1, col_dose2 = st.columns(2)
        with col_dose1:
            current_dose_ml = st.number_input(
                "Liều hiện tại (mL)",
                min_value=0.0,
                max_value=200.0,
                value=float(shared_inputs.get('current_dose_ml')) if shared_inputs.get('current_dose_ml') else None,
                step=5.0,
                format="%.0f",
                help="Liều lactulose hiện tại tính bằng mL"
            )
        with col_dose2:
            current_dose_g = st.number_input(
                "Liều hiện tại (g)",
                min_value=0.0,
                max_value=200.0,
                value=float(shared_inputs.get('current_dose_g')) if shared_inputs.get('current_dose_g') else None,
                step=5.0,
                format="%.0f",
                help="Liều lactulose hiện tại tính bằng gram"
            )
        
        # Validation
        errors = []
        if current_bm_frequency < 0:
            errors.append("Tần suất đi ngoài phải ≥ 0")
        if weight_kg <= 0:
            errors.append("Cân nặng phải > 0")
        
        if errors:
            for error in errors:
                st.error(f"⚠️ {error}")
            return
        
        # Calculate
        if st.button("🔄 Tính Toán Liều Lactulose", type="primary", use_container_width=True):
            result = calculate_lactulose_dose(
                he_grade=he_grade,
                current_bm_frequency=current_bm_frequency,
                weight_kg=weight_kg,
                ammonia_level=ammonia_level,
                current_dose_ml=current_dose_ml,
                current_dose_g=current_dose_g
            )
            
            st.session_state['lactulose_result'] = result
            
            # Display results
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            # Metrics
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                st.metric(
                    "Liều Đề Xuất",
                    f"{result['recommended_dose_ml']} mL",
                    delta=f"{result['recommended_dose_g']}g"
                )
            
            with col_res2:
                st.metric(
                    "Tần Suất",
                    result['recommended_frequency']
                )
            
            with col_res3:
                st.metric(
                    "Tổng Liều/Ngày",
                    f"~{result['daily_total_ml']:.0f} mL",
                    delta=f"~{result['daily_total_g']:.0f}g"
                )
            
            # Target BM frequency
            target_range = result['target_bm_range']
            if float(target_range.split('-')[0]) <= current_bm_frequency <= float(target_range.split('-')[1]):
                st.success(f"✅ Tần suất đi ngoài hiện tại ({current_bm_frequency:.1f} lần/ngày) trong khoảng mục tiêu ({target_range} lần/ngày)")
            elif current_bm_frequency < float(target_range.split('-')[0]):
                st.warning(f"⚠️ Tần suất đi ngoài hiện tại ({current_bm_frequency:.1f} lần/ngày) thấp hơn mục tiêu ({target_range} lần/ngày)")
            else:
                st.error(f"🚨 Tần suất đi ngoài hiện tại ({current_bm_frequency:.1f} lần/ngày) cao hơn mục tiêu ({target_range} lần/ngày)")
            
            # Warnings
            if result['warnings']:
                for warning in result['warnings']:
                    st.warning(warning)
            
            # Recommendations
            st.markdown("### 💡 Khuyến nghị")
            for i, rec in enumerate(result['recommendations'], 1):
                st.markdown(f"{i}. {rec}")
            
            # Clinical guidance
            st.markdown("### 📋 Hướng dẫn Lâm Sàng")
            
            st.info("""
            **Mục tiêu điều trị:**
            - Đạt 2-3 lần đi ngoài mềm mỗi ngày
            - Giảm triệu chứng bệnh não gan
            - Duy trì liều tối thiểu hiệu quả
            
            **Cơ chế:**
            - Lactulose làm acid hóa phân, giảm hấp thu ammonia
            - Tăng thải ammonia qua phân
            - Thay đổi hệ vi khuẩn đường ruột
            
            **Lưu ý:**
            - Điều chỉnh liều từng bước
            - Tránh quá liều (tiêu chảy, mất nước)
            - Tránh thiếu liều (táo bón, không hiệu quả)
            - Theo dõi điện giải và tình trạng mất nước
            """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="lactulose_calculator",
                calculator_name="Lactulose Calculator",
                inputs={
                    "HE Grade": he_grade,
                    "Tần suất đi ngoài": f"{current_bm_frequency:.1f} lần/ngày",
                    "Cân nặng": f"{weight_kg:.1f} kg",
                    "Ammonia": f"{ammonia_level:.0f} μmol/L" if ammonia_level else "N/A"
                },
                result={
                    "Liều đề xuất": f"{result['recommended_dose_ml']} mL ({result['recommended_dose_g']}g) {result['recommended_frequency']}",
                    "Tổng liều/ngày": f"~{result['daily_total_ml']:.0f} mL (~{result['daily_total_g']:.0f}g)"
                }
            )
            
            render_share_section(
                calculator_id="lactulose_calculator",
                calculator_name="Lactulose Calculator"
            )
            render_scores_export(
                calculator_id="lactulose_calculator",
                calculator_name="Lactulose Calculator",
                data={"result": result}
            )
            render_suggestions(calculator_id="lactulose_calculator", result=result)
    
    with col2:
        st.markdown("### 📚 Thông tin")
        
        st.markdown("""
        **Lactulose:**
        
        - Điều trị bệnh não gan
        - Liều: 10-60 mL (10-40g) tùy mức độ
        - Mục tiêu: 2-3 lần đi ngoài mềm/ngày
        
        **HE Grades:**
        - Grade 1: Nhẹ
        - Grade 2: Trung bình
        - Grade 3: Nặng
        - Grade 4: Hôn mê
        
        **Lưu ý:**
        - Điều chỉnh liều từng bước
        - Tránh quá/thiếu liều
        - Theo dõi điện giải
        """)
        
        if st.session_state.get('lactulose_result'):
            result = st.session_state['lactulose_result']
            render_risk_badge(
                result['risk_level'],
                f"Grade {result['he_grade']}",
                size="large"
            )
    
    render_history_ui(calculator_id="lactulose_calculator", show_actions=True)
    references = get_references("Lactulose")
    if references:
        render_references_section(references)
