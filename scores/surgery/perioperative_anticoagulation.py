"""
Perioperative Anticoagulation Management Algorithm
===================================================

Algorithm for managing anticoagulation in patients undergoing surgery or procedures.
Helps determine when to stop and restart anticoagulants based on:
- Type of anticoagulant
- Bleeding risk of procedure
- Thromboembolic risk of patient
- Renal function

Reference:
- Douketis JD, et al. Perioperative management of antithrombotic therapy: 
  An American College of Chest Physicians Clinical Practice Guideline. 
  Chest. 2022;162(5):e207-e243.
- ACC/AHA Guidelines on Perioperative Cardiovascular Evaluation and Management.

Clinical Utility:
- Guides timing of anticoagulant discontinuation
- Determines need for bridging therapy
- Helps balance bleeding vs thrombotic risk
- Used daily in perioperative care
"""

import streamlit as st
from datetime import datetime, timedelta
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_perioperative_anticoagulation(
    anticoagulant_type: str,  # warfarin, doac, heparin, lmwh, antiplatelet
    procedure_bleeding_risk: str,  # low, medium, high
    thromboembolic_risk: str,  # low, medium, high, very_high
    egfr: float = None,
    procedure_date: datetime = None,
    current_date: datetime = None
) -> dict:
    """
    Calculate perioperative anticoagulation management plan
    
    Args:
        anticoagulant_type: Type of anticoagulant
        procedure_bleeding_risk: Bleeding risk of procedure
        thromboembolic_risk: Patient's thromboembolic risk
        egfr: eGFR for DOAC dosing
        procedure_date: Scheduled procedure date
        current_date: Current date
    
    Returns:
        Dictionary with management plan
    """
    recommendations = []
    stop_timing = None
    restart_timing = None
    bridging_needed = False
    bridging_details = []
    
    # Determine stop timing based on anticoagulant type
    if anticoagulant_type == "warfarin":
        if procedure_bleeding_risk == "low":
            stop_timing = 3  # days before
            recommendations.append("Ngừng warfarin 3 ngày trước phẫu thuật")
        elif procedure_bleeding_risk == "medium":
            stop_timing = 4
            recommendations.append("Ngừng warfarin 4 ngày trước phẫu thuật")
        else:  # high
            stop_timing = 5
            recommendations.append("Ngừng warfarin 5 ngày trước phẫu thuật")
        
        # Check INR before procedure
        recommendations.append("Kiểm tra INR 1-2 ngày trước phẫu thuật (mục tiêu <1.5)")
        
    elif anticoagulant_type in ["dabigatran", "rivaroxaban", "apixaban", "edoxaban"]:
        # DOACs - depends on renal function and bleeding risk
        if egfr is not None:
            if egfr < 30:
                # Severe renal impairment
                if procedure_bleeding_risk == "low":
                    stop_timing = 3
                elif procedure_bleeding_risk == "medium":
                    stop_timing = 4
                else:
                    stop_timing = 5
            elif egfr < 50:
                # Moderate renal impairment
                if procedure_bleeding_risk == "low":
                    stop_timing = 2
                elif procedure_bleeding_risk == "medium":
                    stop_timing = 3
                else:
                    stop_timing = 4
            else:
                # Normal/mild renal impairment
                if procedure_bleeding_risk == "low":
                    stop_timing = 1
                elif procedure_bleeding_risk == "medium":
                    stop_timing = 2
                else:
                    stop_timing = 3
        
        doac_name = {
            "dabigatran": "Dabigatran",
            "rivaroxaban": "Rivaroxaban",
            "apixaban": "Apixaban",
            "edoxaban": "Edoxaban"
        }.get(anticoagulant_type, "DOAC")
        
        recommendations.append(f"Ngừng {doac_name} {stop_timing} ngày trước phẫu thuật")
        
        if anticoagulant_type == "dabigatran" and egfr is not None and egfr < 50:
            recommendations.append("⚠️ Dabigatran: Cần ngừng lâu hơn nếu eGFR <50")
    
    elif anticoagulant_type == "heparin":
        recommendations.append("Ngừng heparin IV 4-6 giờ trước phẫu thuật")
        recommendations.append("Ngừng heparin dưới da 12 giờ trước phẫu thuật")
    
    elif anticoagulant_type == "lmwh":
        if procedure_bleeding_risk == "low":
            stop_timing = 1
            recommendations.append("Ngừng LMWH 12-24 giờ trước phẫu thuật")
        else:
            stop_timing = 2
            recommendations.append("Ngừng LMWH 24 giờ trước phẫu thuật")
    
    elif anticoagulant_type in ["aspirin", "clopidogrel", "prasugrel", "ticagrelor"]:
        if procedure_bleeding_risk == "low":
            recommendations.append("Có thể tiếp tục aspirin")
        elif procedure_bleeding_risk == "medium":
            if anticoagulant_type == "aspirin":
                stop_timing = 3
                recommendations.append("Ngừng aspirin 3-5 ngày trước phẫu thuật")
            else:
                stop_timing = 5
                recommendations.append(f"Ngừng {anticoagulant_type} 5-7 ngày trước phẫu thuật")
        else:  # high
            if anticoagulant_type == "aspirin":
                stop_timing = 5
                recommendations.append("Ngừng aspirin 5-7 ngày trước phẫu thuật")
            else:
                stop_timing = 7
                recommendations.append(f"Ngừng {anticoagulant_type} 7-10 ngày trước phẫu thuật")
    
    # Determine need for bridging
    if anticoagulant_type in ["warfarin", "dabigatran", "rivaroxaban", "apixaban", "edoxaban"]:
        if thromboembolic_risk in ["high", "very_high"]:
            bridging_needed = True
            bridging_details.append("Cần bridging với LMWH hoặc heparin")
            bridging_details.append("Bắt đầu LMWH 2-3 ngày sau khi ngừng warfarin/DOAC")
            bridging_details.append("Ngừng LMWH 12-24 giờ trước phẫu thuật")
        elif thromboembolic_risk == "medium":
            bridging_details.append("Cân nhắc bridging tùy từng trường hợp")
        else:
            bridging_details.append("Không cần bridging")
    
    # Determine restart timing
    if procedure_bleeding_risk == "low":
        restart_timing = 1
        recommendations.append("Có thể khởi động lại kháng đông 12-24 giờ sau phẫu thuật")
    elif procedure_bleeding_risk == "medium":
        restart_timing = 2
        recommendations.append("Khởi động lại kháng đông 24-48 giờ sau phẫu thuật")
    else:  # high
        restart_timing = 3
        recommendations.append("Khởi động lại kháng đông 48-72 giờ sau phẫu thuật (khi cầm máu tốt)")
    
    # Calculate specific dates if provided
    stop_date = None
    restart_date = None
    if procedure_date and stop_timing:
        stop_date = procedure_date - timedelta(days=stop_timing)
    if procedure_date and restart_timing:
        restart_date = procedure_date + timedelta(days=restart_timing)
    
    return {
        "stop_timing_days": stop_timing,
        "restart_timing_days": restart_timing,
        "stop_date": stop_date,
        "restart_date": restart_date,
        "bridging_needed": bridging_needed,
        "bridging_details": bridging_details,
        "recommendations": recommendations,
        "thromboembolic_risk": thromboembolic_risk,
        "procedure_bleeding_risk": procedure_bleeding_risk
    }


def render():
    """Render Perioperative Anticoagulation Management interface"""
    st.set_page_config(page_title="Perioperative Anticoagulation", layout="wide")
    
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>💊 Perioperative Anticoagulation Management</h2>
    <p style='text-align: center; color: #6B7280;'>
    Quản lý kháng đông trong phẫu thuật<br>
    Hướng dẫn ngừng và khởi động lại kháng đông
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Perioperative Anticoagulation Management Algorithm** giúp quản lý kháng đông 
        ở bệnh nhân cần phẫu thuật hoặc thủ thuật.
        
        ### Các yếu tố đánh giá:
        1. **Loại kháng đông:** Warfarin, DOAC, Heparin, LMWH, Antiplatelet
        2. **Nguy cơ chảy máu của thủ thuật:**
           - Thấp: Nội soi, sinh thiết nhỏ, nhổ răng
           - Trung bình: Phẫu thuật nhỏ, nội soi có sinh thiết
           - Cao: Phẫu thuật lớn, phẫu thuật thần kinh, phẫu thuật mắt
        3. **Nguy cơ huyết khối của bệnh nhân:**
           - Thấp: Rung nhĩ không có yếu tố nguy cơ, DVT >3 tháng
           - Trung bình: Rung nhĩ có yếu tố nguy cơ, van cơ học cũ
           - Cao: Van cơ học mới, huyết khối <3 tháng, hội chứng kháng phospholipid
           - Rất cao: Van cơ học + rung nhĩ, huyết khối <1 tháng
        
        ### Nguyên tắc:
        - Cân bằng nguy cơ chảy máu vs huyết khối
        - Ngừng đủ sớm để giảm nguy cơ chảy máu
        - Khởi động lại đủ sớm để giảm nguy cơ huyết khối
        - Cân nhắc bridging cho nguy cơ huyết khối cao
        """)
    
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    anticoagulant_type = st.selectbox(
        "Loại kháng đông",
        ["warfarin", "dabigatran", "rivaroxaban", "apixaban", "edoxaban", "heparin", "lmwh", "aspirin", "clopidogrel", "prasugrel", "ticagrelor"],
        format_func=lambda x: {
            "warfarin": "Warfarin",
            "dabigatran": "Dabigatran (Pradaxa)",
            "rivaroxaban": "Rivaroxaban (Xarelto)",
            "apixaban": "Eliquis (Apixaban)",
            "edoxaban": "Edoxaban (Savaysa)",
            "heparin": "Heparin (không phân đoạn)",
            "lmwh": "LMWH (Enoxaparin, Dalteparin)",
            "aspirin": "Aspirin",
            "clopidogrel": "Clopidogrel (Plavix)",
            "prasugrel": "Prasugrel (Effient)",
            "ticagrelor": "Ticagrelor (Brilinta)"
        }[x],
        key="peri_anticoag"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        procedure_bleeding_risk = st.selectbox(
            "Nguy cơ chảy máu của thủ thuật",
            ["low", "medium", "high"],
            format_func=lambda x: {
                "low": "Thấp (nội soi, sinh thiết nhỏ)",
                "medium": "Trung bình (phẫu thuật nhỏ)",
                "high": "Cao (phẫu thuật lớn, thần kinh, mắt)"
            }[x],
            key="peri_bleeding"
        )
    
    with col2:
        thromboembolic_risk = st.selectbox(
            "Nguy cơ huyết khối của bệnh nhân",
            ["low", "medium", "high", "very_high"],
            format_func=lambda x: {
                "low": "Thấp (AF không yếu tố nguy cơ, DVT >3 tháng)",
                "medium": "Trung bình (AF có yếu tố nguy cơ)",
                "high": "Cao (van cơ học, huyết khối <3 tháng)",
                "very_high": "Rất cao (van cơ học + AF, huyết khối <1 tháng)"
            }[x],
            key="peri_thromb"
        )
    
    # For DOACs, need eGFR
    if anticoagulant_type in ["dabigatran", "rivaroxaban", "apixaban", "edoxaban"]:
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²) - Quan trọng cho DOAC",
            min_value=0.0,
            max_value=200.0,
            value=60.0,
            step=1.0,
            format="%.1f",
            key="peri_egfr"
        )
    else:
        egfr = None
    
    # Optional: procedure date
    procedure_date = st.date_input(
        "Ngày phẫu thuật dự kiến (tùy chọn)",
        value=None,
        key="peri_date"
    )
    
    if st.button("🔬 Tính toán kế hoạch", type="primary", use_container_width=True):
        if procedure_date:
            procedure_datetime = datetime.combine(procedure_date, datetime.min.time())
            current_datetime = datetime.now()
        else:
            procedure_datetime = None
            current_datetime = None
        
        result = calculate_perioperative_anticoagulation(
            anticoagulant_type=anticoagulant_type,
            procedure_bleeding_risk=procedure_bleeding_risk,
            thromboembolic_risk=thromboembolic_risk,
            egfr=egfr,
            procedure_date=procedure_datetime,
            current_date=current_datetime
        )
        
        st.markdown("---")
        st.markdown("### 📋 Kế hoạch quản lý kháng đông")
        
        st.markdown("### ⏰ Thời điểm ngừng kháng đông")
        if result["stop_timing_days"]:
            st.info(f"**Ngừng {result['stop_timing_days']} ngày trước phẫu thuật**")
            if result["stop_date"]:
                st.markdown(f"**Ngày ngừng:** {result['stop_date'].strftime('%d/%m/%Y')}")
        else:
            st.info("Xem khuyến nghị chi tiết bên dưới")
        
        st.markdown("### 🔄 Bridging (nếu cần)")
        if result["bridging_needed"]:
            st.warning("**CẦN BRIDGING**")
            for detail in result["bridging_details"]:
                st.markdown(f"- {detail}")
        else:
            if result["bridging_details"]:
                for detail in result["bridging_details"]:
                    st.markdown(f"- {detail}")
        
        st.markdown("### ▶️ Thời điểm khởi động lại")
        if result["restart_timing_days"]:
            st.success(f"**Khởi động lại {result['restart_timing_days']} ngày sau phẫu thuật**")
            if result["restart_date"]:
                st.markdown(f"**Ngày khởi động lại:** {result['restart_date'].strftime('%d/%m/%Y')}")
        
        st.markdown("### 📝 Khuyến nghị chi tiết")
        for rec in result["recommendations"]:
            st.markdown(f"- {rec}")
        
        # Additional considerations
        st.markdown("### ⚠️ Lưu ý quan trọng")
        st.markdown("""
        - **Kiểm tra INR** (với warfarin) 1-2 ngày trước phẫu thuật, mục tiêu <1.5
        - **Đánh giá lại** nếu có thay đổi tình trạng bệnh nhân
        - **Theo dõi dấu hiệu chảy máu** sau phẫu thuật
        - **Cân nhắc khởi động lại sớm hơn** nếu nguy cơ huyết khối rất cao và cầm máu tốt
        - **Tư vấn tim mạch/huyết học** nếu nguy cơ cao hoặc phức tạp
        """)
        
        save_calculation_to_history(
            calculator_id="perioperative_anticoagulation",
            calculator_name="Perioperative Anticoagulation",
            inputs={
                "Kháng đông": anticoagulant_type,
                "Nguy cơ chảy máu": procedure_bleeding_risk,
                "Nguy cơ huyết khối": thromboembolic_risk
            },
            result={
                "Ngừng (ngày)": result["stop_timing_days"] or "N/A",
                "Khởi động lại (ngày)": result["restart_timing_days"],
                "Bridging": "Có" if result["bridging_needed"] else "Không"
            }
        )
        
        render_share_section(
            calculator_id="perioperative_anticoagulation",
            calculator_name="Perioperative Anticoagulation"
        )
        
        render_export_section(
            calculator_id="perioperative_anticoagulation",
            calculator_name="Perioperative Anticoagulation",
            data={"inputs": {"anticoagulant": anticoagulant_type}, "result": result}
        )
    
    render_history_ui(calculator_id="perioperative_anticoagulation", show_actions=True)
    
    references = get_references("Perioperative Anticoagulation")
    if references:
        render_references_section(references)

