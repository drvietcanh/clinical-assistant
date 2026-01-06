"""
Bleeding Risk Calculator
========================

Assess bleeding risk in patients on anticoagulation or antiplatelet therapy.

Reference:
- HAS-BLED Score (Pisters et al. Chest 2010)
- AHA/ACC Guidelines for Antithrombotic Therapy
- ESC Guidelines for Atrial Fibrillation
- ACCP Guidelines for Antithrombotic Therapy

Clinical Utility:
- Assess bleeding risk before starting anticoagulation
- Guide anticoagulation management decisions
- Balance thrombotic vs bleeding risk
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


def calculate_bleeding_risk(
    age: int = None,
    history_bleeding: bool = False,
    history_stroke: bool = False,
    labile_inr: bool = False,
    drugs_alcohol: bool = False,
    renal_disease: bool = False,
    liver_disease: bool = False,
    hypertension: bool = False,
    antiplatelet_drugs: bool = False,
    nsaid_use: bool = False,
    current_inr: float = None,
    indication: str = "atrial_fibrillation"
) -> dict:
    """
    Calculate bleeding risk score
    
    Args:
        age: Patient age (years)
        history_bleeding: History of bleeding
        history_stroke: History of stroke/TIA
        labile_inr: Labile INR (if on warfarin)
        drugs_alcohol: Drugs/alcohol use
        renal_disease: Renal disease (Cr >2.26 mg/dL or dialysis)
        liver_disease: Liver disease (cirrhosis, bilirubin >2x normal, AST/ALT >3x normal)
        hypertension: Hypertension (SBP >160 mmHg)
        antiplatelet_drugs: Antiplatelet drugs (aspirin, clopidogrel, etc.)
        nsaid_use: NSAID use
        current_inr: Current INR value (if on warfarin)
        indication: Indication for anticoagulation
    
    Returns:
        dict with bleeding risk score, level, and recommendations
    """
    score = 0
    factors = []
    
    # Age ≥65 years: 1 point
    if age and age >= 65:
        score += 1
        factors.append({"factor": "Tuổi ≥65 tuổi", "points": 1})
    
    # History of bleeding: 2 points
    if history_bleeding:
        score += 2
        factors.append({"factor": "Tiền sử chảy máu", "points": 2})
    
    # History of stroke/TIA: 1 point
    if history_stroke:
        score += 1
        factors.append({"factor": "Tiền sử đột quỵ/TIA", "points": 1})
    
    # Labile INR: 1 point (if on warfarin)
    if labile_inr or (current_inr and (current_inr < 1.5 or current_inr > 4.0)):
        score += 1
        factors.append({"factor": "INR không ổn định", "points": 1})
    
    # Drugs/alcohol: 1 point
    if drugs_alcohol:
        score += 1
        factors.append({"factor": "Thuốc/rượu", "points": 1})
    
    # Renal disease: 1 point
    if renal_disease:
        score += 1
        factors.append({"factor": "Bệnh thận (Cr >2.26 mg/dL hoặc lọc máu)", "points": 1})
    
    # Liver disease: 1 point
    if liver_disease:
        score += 1
        factors.append({"factor": "Bệnh gan (xơ gan, bilirubin >2x, AST/ALT >3x)", "points": 1})
    
    # Hypertension: 1 point
    if hypertension:
        score += 1
        factors.append({"factor": "Tăng huyết áp (SBP >160 mmHg)", "points": 1})
    
    # Antiplatelet drugs: 1 point
    if antiplatelet_drugs:
        score += 1
        factors.append({"factor": "Thuốc chống kết tập tiểu cầu", "points": 1})
    
    # NSAID use: 1 point
    if nsaid_use:
        score += 1
        factors.append({"factor": "NSAID", "points": 1})
    
    # Determine risk level
    if score == 0:
        risk_level = "low"
        risk_label = "Nguy cơ thấp"
        risk_color = "green"
        recommendations = [
            "Có thể bắt đầu kháng đông an toàn",
            "Theo dõi INR định kỳ (nếu dùng warfarin)",
            "Tái khám sau 1-3 tháng"
        ]
    elif score <= 2:
        risk_level = "moderate"
        risk_label = "Nguy cơ trung bình"
        risk_color = "orange"
        recommendations = [
            "Có thể bắt đầu kháng đông nhưng thận trọng",
            "Theo dõi INR thường xuyên hơn (mỗi 1-2 tuần)",
            "Giảm liều khởi đầu nếu có thể",
            "Tránh dùng kết hợp với NSAID hoặc antiplatelet nếu không cần thiết",
            "Tái khám sau 2-4 tuần"
        ]
    else:  # score >= 3
        risk_level = "high"
        risk_label = "Nguy cơ cao"
        risk_color = "red"
        recommendations = [
            "THẬN TRỌNG khi bắt đầu kháng đông",
            "Cân nhắc liều thấp hơn hoặc DOAC thay vì warfarin",
            "Theo dõi INR rất thường xuyên (mỗi tuần)",
            "Tránh dùng kết hợp với NSAID hoặc antiplatelet",
            "Giáo dục bệnh nhân về dấu hiệu chảy máu",
            "Tái khám sau 1-2 tuần",
            "Cân nhắc chuyển sang chuyên khoa huyết học nếu cần"
        ]
    
    return {
        "score": score,
        "risk_level": risk_level,
        "risk_label": risk_label,
        "risk_color": risk_color,
        "factors": factors,
        "recommendations": recommendations,
        "max_score": 11,
        "interpretation": f"Điểm số {score}/11 - {risk_label}"
    }


def render():
    """Render the Bleeding Risk Calculator interface"""
    st.set_page_config(page_title="Bleeding Risk Calculator", layout="wide")
    
    st.title("🩸 Bleeding Risk Calculator")
    st.markdown("### Đánh giá nguy cơ chảy máu ở bệnh nhân dùng kháng đông/chống kết tập tiểu cầu")
    
    # Load shared result if present
    shared_inputs = load_shared_result_from_url()
    
    # Sidebar for history
    with st.sidebar:
        st.header("📊 Lịch sử tính toán")
        render_history_ui("bleeding_risk")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin bệnh nhân")
        
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=int(shared_inputs.get('age', 65)) if shared_inputs.get('age') else None,
            step=1,
            help="Tuổi ≥65: +1 điểm"
        )
        
        st.markdown("### 🩸 Yếu tố nguy cơ")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            history_bleeding = st.checkbox(
                "Tiền sử chảy máu",
                value=shared_inputs.get('history_bleeding', False),
                help="+2 điểm"
            )
            
            history_stroke = st.checkbox(
                "Tiền sử đột quỵ/TIA",
                value=shared_inputs.get('history_stroke', False),
                help="+1 điểm"
            )
            
            labile_inr = st.checkbox(
                "INR không ổn định",
                value=shared_inputs.get('labile_inr', False),
                help="+1 điểm (nếu đang dùng warfarin)"
            )
            
            drugs_alcohol = st.checkbox(
                "Thuốc/rượu",
                value=shared_inputs.get('drugs_alcohol', False),
                help="+1 điểm"
            )
            
            renal_disease = st.checkbox(
                "Bệnh thận (Cr >2.26 mg/dL hoặc lọc máu)",
                value=shared_inputs.get('renal_disease', False),
                help="+1 điểm"
            )
        
        with col_b:
            liver_disease = st.checkbox(
                "Bệnh gan (xơ gan, bilirubin >2x, AST/ALT >3x)",
                value=shared_inputs.get('liver_disease', False),
                help="+1 điểm"
            )
            
            hypertension = st.checkbox(
                "Tăng huyết áp (SBP >160 mmHg)",
                value=shared_inputs.get('hypertension', False),
                help="+1 điểm"
            )
            
            antiplatelet_drugs = st.checkbox(
                "Thuốc chống kết tập tiểu cầu",
                value=shared_inputs.get('antiplatelet_drugs', False),
                help="+1 điểm"
            )
            
            nsaid_use = st.checkbox(
                "NSAID",
                value=shared_inputs.get('nsaid_use', False),
                help="+1 điểm"
            )
        
        st.markdown("### 💊 Thông tin kháng đông (Tùy chọn)")
        
        current_inr = st.number_input(
            "INR hiện tại (nếu đang dùng warfarin)",
            min_value=0.5,
            max_value=10.0,
            value=float(shared_inputs.get('current_inr')) if shared_inputs.get('current_inr') else None,
            step=0.1,
            format="%.2f",
            help="INR <1.5 hoặc >4.0: +1 điểm"
        )
        
        indication = st.selectbox(
            "Chỉ định kháng đông",
            [
                "atrial_fibrillation",
                "mechanical_valve",
                "dvt_pe",
                "other"
            ],
            format_func=lambda x: {
                "atrial_fibrillation": "Rung nhĩ",
                "mechanical_valve": "Van cơ học",
                "dvt_pe": "DVT/PE",
                "other": "Khác"
            }[x],
            index=0
        )
        
        # Calculate button
        if st.button("🔍 Tính toán", type="primary", use_container_width=True):
            if age is None:
                st.warning("⚠️ Vui lòng nhập tuổi bệnh nhân")
            else:
                result = calculate_bleeding_risk(
                    age=age,
                    history_bleeding=history_bleeding,
                    history_stroke=history_stroke,
                    labile_inr=labile_inr or (current_inr and (current_inr < 1.5 or current_inr > 4.0)),
                    drugs_alcohol=drugs_alcohol,
                    renal_disease=renal_disease,
                    liver_disease=liver_disease,
                    hypertension=hypertension,
                    antiplatelet_drugs=antiplatelet_drugs,
                    nsaid_use=nsaid_use,
                    current_inr=current_inr,
                    indication=indication
                )
                
                # Save to history
                save_calculation_to_history(
                    "bleeding_risk",
                    {
                        "age": age,
                        "history_bleeding": history_bleeding,
                        "history_stroke": history_stroke,
                        "labile_inr": labile_inr,
                        "drugs_alcohol": drugs_alcohol,
                        "renal_disease": renal_disease,
                        "liver_disease": liver_disease,
                        "hypertension": hypertension,
                        "antiplatelet_drugs": antiplatelet_drugs,
                        "nsaid_use": nsaid_use,
                        "current_inr": current_inr,
                        "indication": indication
                    },
                    result
                )
                
                # Display results
                st.markdown("---")
                st.markdown("## 📊 Kết quả")
                
                # Risk badge
                render_risk_badge(
                    result["risk_level"],
                    result["risk_label"],
                    result["score"],
                    result["max_score"]
                )
                
                # Score breakdown
                st.markdown("### Chi tiết điểm số")
                render_score_breakdown(result["factors"])
                
                # Recommendations
                st.markdown("### 💡 Khuyến nghị")
                for i, rec in enumerate(result["recommendations"], 1):
                    st.markdown(f"{i}. {rec}")
                
                # Share section
                st.markdown("---")
                render_share_section("bleeding_risk", {
                    "age": age,
                    "history_bleeding": history_bleeding,
                    "history_stroke": history_stroke,
                    "labile_inr": labile_inr,
                    "drugs_alcohol": drugs_alcohol,
                    "renal_disease": renal_disease,
                    "liver_disease": liver_disease,
                    "hypertension": hypertension,
                    "antiplatelet_drugs": antiplatelet_drugs,
                    "nsaid_use": nsaid_use,
                    "current_inr": current_inr,
                    "indication": indication
                })
                
                # Export section
                render_scores_export(result, "bleeding_risk")
    
    with col2:
        st.markdown("### 📚 Thông tin")
        st.info("""
        **Bleeding Risk Calculator** dựa trên các yếu tố nguy cơ chảy máu phổ biến.
        
        **Thang điểm:**
        - 0 điểm: Nguy cơ thấp
        - 1-2 điểm: Nguy cơ trung bình
        - ≥3 điểm: Nguy cơ cao
        
        **Lưu ý:** Đây là công cụ hỗ trợ quyết định lâm sàng, không thay thế đánh giá của bác sĩ.
        """)
        
        # References
        render_references_section(get_references("bleeding_risk"))
        
        # Suggestions
        render_suggestions("bleeding_risk")


if __name__ == "__main__":
    render()
