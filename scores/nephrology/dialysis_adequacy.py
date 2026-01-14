"""
Dialysis Adequacy Calculator
==============================

Assess dialysis adequacy based on Kt/V and URR (Urea Reduction Ratio).

Reference:
- KDOQI Clinical Practice Guidelines for Hemodialysis Adequacy (2015)
- KDIGO 2012 Clinical Practice Guideline for Acute Kidney Injury
- NKF-KDOQI Clinical Practice Guidelines for Hemodialysis Adequacy (2006)

Clinical Utility:
- Assess adequacy of hemodialysis
- Guide dialysis prescription adjustments
- Monitor dialysis quality
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


def calculate_dialysis_adequacy(
    ktv: float = None,
    urr: float = None,
    sessions_per_week: int = 3,
    dialysis_type: str = "HD",
    pre_urea: float = None,
    post_urea: float = None,
    dialysis_time_hours: float = None,
    weight_kg: float = None
) -> dict:
    """
    Calculate dialysis adequacy based on Kt/V and/or URR
    
    Args:
        ktv: Kt/V value (if directly measured)
        urr: Urea Reduction Ratio (%) (if directly measured)
        sessions_per_week: Number of dialysis sessions per week
        dialysis_type: Type of dialysis (HD/HDF)
        pre_urea: Pre-dialysis BUN (mg/dL)
        post_urea: Post-dialysis BUN (mg/dL)
        dialysis_time_hours: Dialysis time in hours
        weight_kg: Patient weight (kg) - for Kt/V calculation if needed
    
    Returns:
        dict with adequacy assessment, recommendations, and clinical guidance
    """
    # Calculate URR if pre/post urea provided
    if pre_urea and post_urea and not urr:
        if pre_urea > 0:
            urr = ((pre_urea - post_urea) / pre_urea) * 100
        else:
            urr = None
    
    # Calculate Kt/V from URR if needed (approximation)
    if urr and not ktv:
        # Simplified formula: Kt/V ≈ -ln(R) where R = 1 - URR/100
        if urr < 100:
            r = 1 - (urr / 100)
            ktv = -1 * (r ** 0.5) if r > 0 else None
            if ktv:
                # More accurate formula for single-pool Kt/V
                ktv = -1 * (r ** 0.5) - (0.008 * dialysis_time_hours) if dialysis_time_hours else ktv
    
    # Determine adequacy status
    adequacy_status = None
    adequacy_level = None
    risk_level = None
    recommendations = []
    
    # KDOQI/KDIGO Guidelines:
    # - Minimum adequate: Kt/V ≥ 1.2 or URR ≥ 65%
    # - Optimal: Kt/V ≥ 1.4 or URR ≥ 70%
    
    if ktv:
        if ktv >= 1.4:
            adequacy_status = "Adequate (Optimal)"
            adequacy_level = "optimal"
            risk_level = "low"
            recommendations = [
                "Dialysis đầy đủ, đạt mục tiêu tối ưu",
                "Tiếp tục duy trì chế độ lọc máu hiện tại",
                "Theo dõi định kỳ Kt/V mỗi tháng",
                "Đảm bảo tuân thủ lịch lọc máu"
            ]
        elif ktv >= 1.2:
            adequacy_status = "Adequate (Minimum)"
            adequacy_level = "adequate"
            risk_level = "moderate"
            recommendations = [
                "Dialysis đạt mức tối thiểu",
                "Cân nhắc tăng thời gian lọc hoặc tần suất để đạt mục tiêu tối ưu",
                "Theo dõi sát các triệu chứng lâm sàng",
                "Đánh giá lại sau 1-2 tháng"
            ]
        elif ktv >= 1.0:
            adequacy_status = "Borderline Inadequate"
            adequacy_level = "borderline"
            risk_level = "moderate"
            recommendations = [
                "Dialysis chưa đầy đủ, cần cải thiện",
                "Tăng thời gian lọc máu hoặc tần suất",
                "Kiểm tra lại lưu lượng máu và dialysate flow",
                "Xem xét tăng kích thước dialyzer",
                "Theo dõi sát và đánh giá lại sau 2-4 tuần"
            ]
        else:
            adequacy_status = "Inadequate"
            adequacy_level = "inadequate"
            risk_level = "high"
            recommendations = [
                "Dialysis KHÔNG đầy đủ - CẦN ĐIỀU CHỈNH NGAY",
                "Tăng thời gian lọc máu (tối thiểu 4 giờ)",
                "Tăng tần suất lọc (3-4 lần/tuần)",
                "Kiểm tra và tối ưu lưu lượng máu (≥300-400 mL/min)",
                "Xem xét dialyzer lớn hơn hoặc high-flux",
                "Đánh giá lại sau 1-2 tuần",
                "Theo dõi các biến chứng do lọc máu không đầy đủ"
            ]
    
    elif urr:
        if urr >= 70:
            adequacy_status = "Adequate (Optimal)"
            adequacy_level = "optimal"
            risk_level = "low"
            recommendations = [
                "Dialysis đầy đủ, đạt mục tiêu tối ưu",
                "Tiếp tục duy trì chế độ lọc máu hiện tại",
                "Theo dõi định kỳ URR mỗi tháng"
            ]
        elif urr >= 65:
            adequacy_status = "Adequate (Minimum)"
            adequacy_level = "adequate"
            risk_level = "moderate"
            recommendations = [
                "Dialysis đạt mức tối thiểu",
                "Cân nhắc tăng thời gian lọc hoặc tần suất",
                "Theo dõi sát các triệu chứng lâm sàng"
            ]
        elif urr >= 60:
            adequacy_status = "Borderline Inadequate"
            adequacy_level = "borderline"
            risk_level = "moderate"
            recommendations = [
                "Dialysis chưa đầy đủ, cần cải thiện",
                "Tăng thời gian lọc máu hoặc tần suất",
                "Kiểm tra lại lưu lượng máu",
                "Đánh giá lại sau 2-4 tuần"
            ]
        else:
            adequacy_status = "Inadequate"
            adequacy_level = "inadequate"
            risk_level = "high"
            recommendations = [
                "Dialysis KHÔNG đầy đủ - CẦN ĐIỀU CHỈNH NGAY",
                "Tăng thời gian lọc máu",
                "Tăng tần suất lọc",
                "Kiểm tra và tối ưu lưu lượng máu",
                "Đánh giá lại sau 1-2 tuần"
            ]
    else:
        adequacy_status = "Cannot Assess"
        adequacy_level = "unknown"
        risk_level = "medium"
        recommendations = [
            "Cần đo Kt/V hoặc URR để đánh giá",
            "Lấy mẫu máu trước và sau lọc máu",
            "Tính toán URR = (Pre-BUN - Post-BUN) / Pre-BUN × 100"
        ]
    
    # Additional guidance based on dialysis type
    if dialysis_type == "HDF":
        recommendations.append("HDF có thể cải thiện clearance và giảm triệu chứng")
    
    # Frequency guidance
    if sessions_per_week < 3:
        recommendations.append(f"⚠️ Tần suất lọc {sessions_per_week} lần/tuần thấp - nên tăng lên 3 lần/tuần")
    
    return {
        "ktv": ktv,
        "urr": urr,
        "sessions_per_week": sessions_per_week,
        "dialysis_type": dialysis_type,
        "adequacy_status": adequacy_status,
        "adequacy_level": adequacy_level,
        "risk_level": risk_level,
        "recommendations": recommendations,
        "pre_urea": pre_urea,
        "post_urea": post_urea,
        "interpretation": f"{adequacy_status} - {'Kt/V: ' + str(round(ktv, 2)) if ktv else ''} {'URR: ' + str(round(urr, 1)) + '%' if urr else ''}"
    }


def render():
    """Render the Dialysis Adequacy Calculator interface"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>💉 Dialysis Adequacy Calculator</h3>
    """, unsafe_allow_html=True)
    st.caption("Đánh giá mức độ đầy đủ của lọc máu dựa trên Kt/V và URR")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'dialysis_adequacy':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin Lọc Máu")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        # Dialysis type
        dialysis_type = st.selectbox(
            "Loại lọc máu",
            ["HD", "HDF"],
            format_func=lambda x: {
                "HD": "Hemodialysis (HD)",
                "HDF": "Hemodiafiltration (HDF)"
            }[x],
            index=0
        )
        
        sessions_per_week = st.number_input(
            "Số buổi lọc/tuần",
            min_value=1,
            max_value=7,
            value=int(shared_inputs.get('sessions_per_week', 3)),
            step=1,
            help="Số buổi lọc máu mỗi tuần"
        )
        
        st.markdown("### 🔬 Kết quả Xét Nghiệm")
        
        # Input method
        input_method = st.radio(
            "Phương pháp nhập",
            ["Kt/V trực tiếp", "URR trực tiếp", "Tính từ BUN"],
            index=0,
            help="Chọn cách nhập dữ liệu"
        )
        
        ktv = None
        urr = None
        pre_urea = None
        post_urea = None
        
        if input_method == "Kt/V trực tiếp":
            ktv = st.number_input(
                "Kt/V",
                min_value=0.0,
                max_value=5.0,
                value=float(shared_inputs.get('ktv', 1.2)) if shared_inputs.get('ktv') else None,
                step=0.1,
                format="%.2f",
                help="Kt/V đo được trực tiếp"
            )
        
        elif input_method == "URR trực tiếp":
            urr = st.number_input(
                "URR (%)",
                min_value=0.0,
                max_value=100.0,
                value=float(shared_inputs.get('urr', 65.0)) if shared_inputs.get('urr') else None,
                step=0.1,
                format="%.1f",
                help="Urea Reduction Ratio (%)"
            )
        
        else:  # Tính từ BUN
            col_pre, col_post = st.columns(2)
            with col_pre:
                pre_urea = st.number_input(
                    "BUN trước lọc (mg/dL)",
                    min_value=0.0,
                    max_value=300.0,
                    value=float(shared_inputs.get('pre_urea', 60.0)) if shared_inputs.get('pre_urea') else None,
                    step=1.0,
                    format="%.1f",
                    help="BUN trước khi lọc máu"
                )
            with col_post:
                post_urea = st.number_input(
                    "BUN sau lọc (mg/dL)",
                    min_value=0.0,
                    max_value=300.0,
                    value=float(shared_inputs.get('post_urea', 20.0)) if shared_inputs.get('post_urea') else None,
                    step=1.0,
                    format="%.1f",
                    help="BUN sau khi lọc máu"
                )
            
            if pre_urea and post_urea:
                if pre_urea > 0:
                    calculated_urr = ((pre_urea - post_urea) / pre_urea) * 100
                    st.info(f"📊 URR tính được: {calculated_urr:.1f}%")
                    urr = calculated_urr
        
        # Optional: Dialysis time for Kt/V calculation
        if input_method != "Kt/V trực tiếp":
            dialysis_time_hours = st.number_input(
                "Thời gian lọc (giờ) - Tùy chọn",
                min_value=0.0,
                max_value=8.0,
                value=float(shared_inputs.get('dialysis_time_hours', 4.0)) if shared_inputs.get('dialysis_time_hours') else None,
                step=0.5,
                format="%.1f",
                help="Thời gian lọc máu (để tính Kt/V từ URR)"
            )
        else:
            dialysis_time_hours = None
        
        # Validation
        errors = []
        if input_method == "Kt/V trực tiếp" and ktv is None:
            errors.append("Vui lòng nhập giá trị Kt/V")
        elif input_method == "URR trực tiếp" and urr is None:
            errors.append("Vui lòng nhập giá trị URR")
        elif input_method == "Tính từ BUN":
            if pre_urea is None or post_urea is None:
                errors.append("Vui lòng nhập cả BUN trước và sau lọc")
            elif post_urea >= pre_urea:
                errors.append("BUN sau lọc phải nhỏ hơn BUN trước lọc")
        
        if errors:
            for error in errors:
                st.error(f"⚠️ {error}")
            return
        
        # Calculate
        if st.button("🔄 Tính Toán Độ Đầy Đủ Lọc Máu", type="primary", use_container_width=True):
            result = calculate_dialysis_adequacy(
                ktv=ktv,
                urr=urr,
                sessions_per_week=sessions_per_week,
                dialysis_type=dialysis_type,
                pre_urea=pre_urea,
                post_urea=post_urea,
                dialysis_time_hours=dialysis_time_hours
            )
            
            st.session_state['dialysis_adequacy_result'] = result
            
            # Display results
            st.markdown("---")
            st.markdown("### 📊 Kết quả")
            
            # Metrics
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                if result['ktv']:
                    st.metric(
                        "Kt/V",
                        f"{result['ktv']:.2f}",
                        delta="Mục tiêu: ≥1.2 (tối thiểu), ≥1.4 (tối ưu)"
                    )
                else:
                    st.metric("Kt/V", "N/A")
            
            with col_res2:
                if result['urr']:
                    st.metric(
                        "URR",
                        f"{result['urr']:.1f}%",
                        delta="Mục tiêu: ≥65% (tối thiểu), ≥70% (tối ưu)"
                    )
                else:
                    st.metric("URR", "N/A")
            
            with col_res3:
                st.metric(
                    "Tần suất",
                    f"{result['sessions_per_week']} lần/tuần"
                )
            
            # Adequacy status
            if result['adequacy_level'] == "optimal":
                st.success(f"✅ **{result['adequacy_status']}**")
            elif result['adequacy_level'] == "adequate":
                st.info(f"ℹ️ **{result['adequacy_status']}**")
            elif result['adequacy_level'] == "borderline":
                st.warning(f"⚠️ **{result['adequacy_status']}**")
            else:
                st.error(f"🚨 **{result['adequacy_status']}**")
            
            # Recommendations
            st.markdown("### 💡 Khuyến nghị")
            for i, rec in enumerate(result['recommendations'], 1):
                st.markdown(f"{i}. {rec}")
            
            # Clinical guidance
            st.markdown("### 📋 Hướng dẫn Lâm Sàng")
            
            st.info("""
            **Tiêu chuẩn đánh giá (KDOQI/KDIGO):**
            - **Tối thiểu:** Kt/V ≥ 1.2 hoặc URR ≥ 65%
            - **Tối ưu:** Kt/V ≥ 1.4 hoặc URR ≥ 70%
            
            **Các yếu tố ảnh hưởng:**
            - Thời gian lọc máu
            - Tần suất lọc
            - Lưu lượng máu và dialysate
            - Kích thước và loại dialyzer
            - Tuân thủ lịch lọc máu
            """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="dialysis_adequacy",
                calculator_name="Dialysis Adequacy Calculator",
                inputs={
                    "Kt/V": f"{result['ktv']:.2f}" if result['ktv'] else "N/A",
                    "URR": f"{result['urr']:.1f}%" if result['urr'] else "N/A",
                    "Tần suất": f"{sessions_per_week} lần/tuần",
                    "Loại lọc": dialysis_type
                },
                result={
                    "Độ đầy đủ": result['adequacy_status'],
                    "Mức độ": result['adequacy_level']
                }
            )
            
            render_share_section(
                calculator_id="dialysis_adequacy",
                calculator_name="Dialysis Adequacy Calculator"
            )
            render_scores_export(
                calculator_id="dialysis_adequacy",
                calculator_name="Dialysis Adequacy Calculator",
                data={"result": result}
            )
            render_suggestions(calculator_id="dialysis_adequacy", result=result)
    
    with col2:
        st.markdown("### 📚 Thông tin")
        
        st.markdown("""
        **Dialysis Adequacy:**
        
        - Đánh giá chất lượng lọc máu
        - Dựa trên Kt/V và URR
        - Theo guideline KDOQI/KDIGO
        
        **Tiêu chuẩn:**
        - Tối thiểu: Kt/V ≥ 1.2, URR ≥ 65%
        - Tối ưu: Kt/V ≥ 1.4, URR ≥ 70%
        
        **Lưu ý:**
        - Đánh giá định kỳ mỗi tháng
        - Điều chỉnh khi không đạt mục tiêu
        """)
        
        if st.session_state.get('dialysis_adequacy_result'):
            result = st.session_state['dialysis_adequacy_result']
            render_risk_badge(
                result['risk_level'],
                result['adequacy_status'],
                size="large"
            )
    
    render_history_ui(calculator_id="dialysis_adequacy", show_actions=True)
    references = get_references("Dialysis Adequacy")
    if references:
        render_references_section(references)
