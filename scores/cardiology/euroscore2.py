"""
EuroSCORE II Calculator
========================

Predicts 30-day mortality after cardiac surgery

Reference:
- Nashef SA, et al. EuroSCORE II. Eur J Cardiothorac Surg. 2012;41(4):734-744.

EuroSCORE II Components (18 factors):
- Age
- Gender (female)
- Chronic lung disease
- Poor mobility
- Previous cardiac surgery
- Chronic kidney disease
- Active endocarditis
- Critical preoperative state
- Diabetes on insulin
- NYHA class
- CCS class 4 angina
- LVEF
- Recent MI
- Pulmonary hypertension
- Urgency
- Weight of intervention
- Surgery on thoracic aorta
- Post-infarct septal rupture

Risk Categories:
- Low risk: <2%
- Medium risk: 2-5%
- High risk: >5%

Clinical Utility:
- Predict 30-day mortality after cardiac surgery
- Risk stratification for surgical planning
- Informed consent discussion
"""

import streamlit as st
import math
from config.theme import COLORS
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_euroscore2(
    age: float,
    is_female: bool,
    chronic_lung_disease: bool,
    poor_mobility: bool,
    previous_cardiac_surgery: bool,
    ckd: bool,
    active_endocarditis: bool,
    critical_preop_state: bool,
    diabetes_insulin: bool,
    nyha_class: int,
    ccs_class4: bool,
    lvef: float,
    recent_mi: bool,
    pulmonary_htn: bool,
    urgency: str,
    weight_intervention: str,
    surgery_thoracic_aorta: bool,
    post_infarct_septal_rupture: bool
) -> dict:
    """
    Calculate EuroSCORE II
    
    Args:
        age: Age in years
        is_female: Female gender
        chronic_lung_disease: Chronic lung disease
        poor_mobility: Poor mobility (severe impairment)
        previous_cardiac_surgery: Previous cardiac surgery
        ckd: Chronic kidney disease (creatinine >200 μmol/L or on dialysis)
        active_endocarditis: Active endocarditis
        critical_preop_state: Critical preoperative state (ventricular tachycardia/fibrillation, cardiac massage, ventilation, inotropes, IABP, acute renal failure)
        diabetes_insulin: Diabetes on insulin
        nyha_class: NYHA class (1-4)
        ccs_class4: CCS class 4 angina
        lvef: Left ventricular ejection fraction (%)
        recent_mi: Recent MI (<90 days)
        pulmonary_htn: Pulmonary hypertension (systolic PA pressure >60 mmHg)
        urgency: Urgency (elective, urgent, emergency, salvage)
        weight_intervention: Weight of intervention (isolated CABG, single non-CABG, 2 procedures, 3+ procedures)
        surgery_thoracic_aorta: Surgery on thoracic aorta
        post_infarct_septal_rupture: Post-infarct septal rupture
    
    Returns:
        Dictionary with mortality risk, risk category, and interpretation
    """
    # EuroSCORE II logistic regression coefficients
    # Base constant
    constant = -5.324537
    
    # Age coefficient (per year over 60)
    age_coef = 0.0285181
    age_score = max(0, (age - 60)) * age_coef
    
    # Gender (female)
    gender_score = 0.2196434 if is_female else 0
    
    # Chronic lung disease
    lung_score = 0.2681475 if chronic_lung_disease else 0
    
    # Poor mobility
    mobility_score = 0.6066301 if poor_mobility else 0
    
    # Previous cardiac surgery
    prev_surgery_score = 0.6558917 if previous_cardiac_surgery else 0
    
    # Chronic kidney disease
    ckd_score = 0.6521653 if ckd else 0
    
    # Active endocarditis
    endocarditis_score = 1.086517 if active_endocarditis else 0
    
    # Critical preoperative state
    critical_score = 1.086517 if critical_preop_state else 0
    
    # Diabetes on insulin
    diabetes_score = 0.3164261 if diabetes_insulin else 0
    
    # NYHA class
    nyha_scores = {
        1: 0,
        2: 0.1070545,
        3: 0.2958358,
        4: 0.5597929
    }
    nyha_score = nyha_scores.get(nyha_class, 0)
    
    # CCS class 4 angina
    ccs_score = 0.2226147 if ccs_class4 else 0
    
    # LVEF
    if lvef >= 50:
        lvef_score = 0
    elif lvef >= 30:
        lvef_score = 0.3150652
    else:
        lvef_score = 0.8084096
    
    # Recent MI
    mi_score = 0.1528943 if recent_mi else 0
    
    # Pulmonary hypertension
    phtn_score = 0.3491475 if pulmonary_htn else 0
    
    # Urgency
    urgency_scores = {
        "elective": 0,
        "urgent": 0.3174673,
        "emergency": 0.7039121,
        "salvage": 1.362947
    }
    urgency_score = urgency_scores.get(urgency.lower(), 0)
    
    # Weight of intervention
    intervention_scores = {
        "isolated_cabg": 0,
        "single_non_cabg": 0.0062118,
        "two_procedures": 0.5521478,
        "three_plus_procedures": 1.101926
    }
    intervention_score = intervention_scores.get(weight_intervention.lower(), 0)
    
    # Surgery on thoracic aorta
    aorta_score = 0.6194522 if surgery_thoracic_aorta else 0
    
    # Post-infarct septal rupture
    septal_rupture_score = 1.462009 if post_infarct_septal_rupture else 0
    
    # Calculate total score
    total_score = (
        constant +
        age_score +
        gender_score +
        lung_score +
        mobility_score +
        prev_surgery_score +
        ckd_score +
        endocarditis_score +
        critical_score +
        diabetes_score +
        nyha_score +
        ccs_score +
        lvef_score +
        mi_score +
        phtn_score +
        urgency_score +
        intervention_score +
        aorta_score +
        septal_rupture_score
    )
    
    # Calculate mortality risk using logistic function
    mortality_risk = 1 / (1 + math.exp(-total_score)) * 100
    
    # Determine risk category
    if mortality_risk < 2:
        risk_category = "Thấp"
        risk_class = "LOW"
        color = COLORS["success"]
    elif mortality_risk < 5:
        risk_category = "Trung bình"
        risk_class = "MEDIUM"
        color = COLORS["warning"]
    else:
        risk_category = "Cao"
        risk_class = "HIGH"
        color = COLORS["error"]
    
    # Build details
    details = []
    details.append(f"Tuổi: {age:.0f} tuổi → {age_score:.3f} điểm")
    if is_female:
        details.append(f"Giới tính nữ → {gender_score:.3f} điểm")
    if chronic_lung_disease:
        details.append(f"Bệnh phổi mạn → {lung_score:.3f} điểm")
    if poor_mobility:
        details.append(f"Vận động kém → {mobility_score:.3f} điểm")
    if previous_cardiac_surgery:
        details.append(f"Phẫu thuật tim trước đây → {prev_surgery_score:.3f} điểm")
    if ckd:
        details.append(f"Suy thận mạn → {ckd_score:.3f} điểm")
    if active_endocarditis:
        details.append(f"Viêm nội tâm mạc hoạt động → {endocarditis_score:.3f} điểm")
    if critical_preop_state:
        details.append(f"Tình trạng tiền phẫu nguy kịch → {critical_score:.3f} điểm")
    if diabetes_insulin:
        details.append(f"Đái tháo đường dùng insulin → {diabetes_score:.3f} điểm")
    details.append(f"NYHA class {nyha_class} → {nyha_score:.3f} điểm")
    if ccs_class4:
        details.append(f"CCS class 4 → {ccs_score:.3f} điểm")
    details.append(f"LVEF {lvef:.0f}% → {lvef_score:.3f} điểm")
    if recent_mi:
        details.append(f"Nhồi máu cơ tim gần đây → {mi_score:.3f} điểm")
    if pulmonary_htn:
        details.append(f"Tăng áp động mạch phổi → {phtn_score:.3f} điểm")
    details.append(f"Độ khẩn cấp: {urgency} → {urgency_score:.3f} điểm")
    details.append(f"Can thiệp: {weight_intervention} → {intervention_score:.3f} điểm")
    if surgery_thoracic_aorta:
        details.append(f"Phẫu thuật động mạch chủ ngực → {aorta_score:.3f} điểm")
    if post_infarct_septal_rupture:
        details.append(f"Vỡ vách sau nhồi máu → {septal_rupture_score:.3f} điểm")
    
    return {
        'mortality_risk': mortality_risk,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'color': color,
        'details': details,
        'total_score': total_score
    }


def render():
    """Render EuroSCORE II calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>❤️ EuroSCORE II</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Dự đoán tử vong 30 ngày sau phẫu thuật tim**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'euroscore2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **EuroSCORE II** dự đoán tử vong 30 ngày sau phẫu thuật tim:
        - Được phát triển từ 22,381 bệnh nhân tại 154 trung tâm châu Âu
        - Cập nhật từ EuroSCORE ban đầu (1999) với dữ liệu mới nhất
        - Dự đoán chính xác hơn EuroSCORE ban đầu
        
        ### 🎯 Yếu tố nguy cơ (18 yếu tố)
        
        1. **Tuổi** (mỗi năm trên 60)
        2. **Giới tính** (nữ)
        3. **Bệnh phổi mạn**
        4. **Vận động kém**
        5. **Phẫu thuật tim trước đây**
        6. **Suy thận mạn** (creatinine >200 μmol/L hoặc chạy thận)
        7. **Viêm nội tâm mạc hoạt động**
        8. **Tình trạng tiền phẫu nguy kịch**
        9. **Đái tháo đường dùng insulin**
        10. **NYHA class** (1-4)
        11. **CCS class 4** đau thắt ngực
        12. **LVEF** (%)
        13. **Nhồi máu cơ tim gần đây** (<90 ngày)
        14. **Tăng áp động mạch phổi** (systolic PA >60 mmHg)
        15. **Độ khẩn cấp** (elective, urgent, emergency, salvage)
        16. **Trọng lượng can thiệp** (isolated CABG, single non-CABG, 2 procedures, 3+ procedures)
        17. **Phẫu thuật động mạch chủ ngực**
        18. **Vỡ vách sau nhồi máu**
        
        ### 📊 Phân loại nguy cơ
        
        | Nguy cơ tử vong | Phân loại |
        |----------------|-----------|
        | <2% | Thấp |
        | 2-5% | Trung bình |
        | >5% | Cao |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho phẫu thuật tim ở người lớn
        - Đánh giá trước phẫu thuật
        - Hỗ trợ quyết định phẫu thuật và thảo luận với bệnh nhân
        - Kết hợp với đánh giá lâm sàng toàn diện
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="euroscore2",
            calculator_name="EuroSCORE II",
            category="Tim mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Bệnh nhân")
        age = st.number_input(
            "Tuổi (năm)",
            18, 120, 65, 1,
            format="%d",
            help="Tuổi bệnh nhân"
        )
        
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True)
        is_female = (sex == "Nữ")
        
        chronic_lung_disease = st.checkbox(
            "Bệnh phổi mạn",
            help="COPD hoặc bệnh phổi mạn tính khác"
        )
        
        poor_mobility = st.checkbox(
            "Vận động kém",
            help="Suy giảm vận động nghiêm trọng"
        )
        
        previous_cardiac_surgery = st.checkbox(
            "Phẫu thuật tim trước đây",
            help="Đã từng phẫu thuật tim"
        )
        
        ckd = st.checkbox(
            "Suy thận mạn",
            help="Creatinine >200 μmol/L hoặc đang chạy thận"
        )
        
        active_endocarditis = st.checkbox(
            "Viêm nội tâm mạc hoạt động",
            help="Viêm nội tâm mạc đang hoạt động"
        )
        
        critical_preop_state = st.checkbox(
            "Tình trạng tiền phẫu nguy kịch",
            help="VT/VF, cardiac massage, ventilation, inotropes, IABP, acute renal failure"
        )
        
        diabetes_insulin = st.checkbox(
            "Đái tháo đường dùng insulin",
            help="Đái tháo đường đang điều trị bằng insulin"
        )
    
    with col2:
        st.markdown("#### 🫀 Chức năng Tim")
        nyha_class = st.selectbox(
            "NYHA Class",
            [1, 2, 3, 4],
            index=1,
            help="Phân loại chức năng suy tim"
        )
        
        ccs_class4 = st.checkbox(
            "CCS Class 4 đau thắt ngực",
            help="Đau thắt ngực khi nghỉ"
        )
        
        lvef = st.number_input(
            "LVEF (%)",
            0.0, 100.0, 55.0, 1.0,
            format="%.0f",
            help="Phân suất tống máu thất trái"
        )
        
        recent_mi = st.checkbox(
            "Nhồi máu cơ tim gần đây",
            help="Nhồi máu cơ tim trong vòng 90 ngày"
        )
        
        pulmonary_htn = st.checkbox(
            "Tăng áp động mạch phổi",
            help="Systolic PA pressure >60 mmHg"
        )
        
        st.markdown("---")
        st.markdown("#### 🔪 Thông tin Phẫu thuật")
        
        urgency = st.selectbox(
            "Độ khẩn cấp",
            ["Elective", "Urgent", "Emergency", "Salvage"],
            index=0,
            help="Độ khẩn cấp của phẫu thuật"
        )
        
        weight_intervention = st.selectbox(
            "Trọng lượng can thiệp",
            ["Isolated CABG", "Single non-CABG", "Two procedures", "Three+ procedures"],
            index=0,
            help="Loại và số lượng can thiệp"
        )
        
        surgery_thoracic_aorta = st.checkbox(
            "Phẫu thuật động mạch chủ ngực",
            help="Phẫu thuật trên động mạch chủ ngực"
        )
        
        post_infarct_septal_rupture = st.checkbox(
            "Vỡ vách sau nhồi máu",
            help="Vỡ vách liên thất sau nhồi máu cơ tim"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính EuroSCORE II", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation
        is_valid_age, age_error = validate_age(age)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        # LVEF validation
        if lvef < 0 or lvef > 100:
            validation_errors.append("LVEF phải trong khoảng 0-100%")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_euroscore2(
            age=age,
            is_female=is_female,
            chronic_lung_disease=chronic_lung_disease,
            poor_mobility=poor_mobility,
            previous_cardiac_surgery=previous_cardiac_surgery,
            ckd=ckd,
            active_endocarditis=active_endocarditis,
            critical_preop_state=critical_preop_state,
            diabetes_insulin=diabetes_insulin,
            nyha_class=nyha_class,
            ccs_class4=ccs_class4,
            lvef=lvef,
            recent_mi=recent_mi,
            pulmonary_htn=pulmonary_htn,
            urgency=urgency,
            weight_intervention=weight_intervention,
            surgery_thoracic_aorta=surgery_thoracic_aorta,
            post_infarct_septal_rupture=post_infarct_septal_rupture
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Use render_score_result for main score display
        icon_map = {
            "LOW": "✅",
            "MEDIUM": "⚠️",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "❤️")
        
        render_score_result(
            title="EuroSCORE II",
            score=f"{result['mortality_risk']:.2f}%",
            interpretation=f"{result['risk_category'].upper()} Risk - Nguy cơ tử vong 30 ngày: {result['mortality_risk']:.2f}%",
            mortality=f"{result['mortality_risk']:.2f}%",
            color=result['color'],
            icon=icon,
            show_mortality=True
        )
        
        # Details
        with st.expander("📋 Chi tiết tính toán", expanded=False):
            st.markdown("### Các yếu tố đóng góp:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **Nguy cơ thấp** - Tỷ lệ tử vong 30 ngày dự kiến: **{result['mortality_risk']:.2f}%**
            
            - Nguy cơ tử vong sau phẫu thuật thấp
            - Phẫu thuật có thể được chỉ định với nguy cơ chấp nhận được
            - Tiên lượng tốt
            """)
        elif result['risk_class'] == "MEDIUM":
            st.warning(f"""
            **Nguy cơ trung bình** - Tỷ lệ tử vong 30 ngày dự kiến: **{result['mortality_risk']:.2f}%**
            
            - Nguy cơ tử vong sau phẫu thuật ở mức trung bình
            - Cần đánh giá kỹ lợi ích/nguy cơ
            - Theo dõi sát sau phẫu thuật
            """)
        else:
            st.error(f"""
            **Nguy cơ cao** - Tỷ lệ tử vong 30 ngày dự kiến: **{result['mortality_risk']:.2f}%**
            
            - Nguy cơ tử vong sau phẫu thuật cao
            - Cần cân nhắc kỹ lợi ích/nguy cơ trước khi quyết định phẫu thuật
            - Có thể cần điều chỉnh các yếu tố nguy cơ trước phẫu thuật
            - Thảo luận kỹ với bệnh nhân và gia đình về nguy cơ
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - EuroSCORE II là công cụ hỗ trợ quyết định, không thay thế đánh giá lâm sàng
        - Kết hợp với đánh giá toàn diện của bác sĩ phẫu thuật tim
        - Thảo luận kỹ với bệnh nhân và gia đình về nguy cơ
        - Cân nhắc điều chỉnh các yếu tố nguy cơ có thể thay đổi được trước phẫu thuật
        - Theo dõi sát sau phẫu thuật, đặc biệt ở bệnh nhân nguy cơ cao
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'euroscore2',
            'calculator_name': 'EuroSCORE II',
            'inputs': {
                'age': age,
                'is_female': is_female,
                'chronic_lung_disease': chronic_lung_disease,
                'poor_mobility': poor_mobility,
                'previous_cardiac_surgery': previous_cardiac_surgery,
                'ckd': ckd,
                'active_endocarditis': active_endocarditis,
                'critical_preop_state': critical_preop_state,
                'diabetes_insulin': diabetes_insulin,
                'nyha_class': nyha_class,
                'ccs_class4': ccs_class4,
                'lvef': lvef,
                'recent_mi': recent_mi,
                'pulmonary_htn': pulmonary_htn,
                'urgency': urgency,
                'weight_intervention': weight_intervention,
                'surgery_thoracic_aorta': surgery_thoracic_aorta,
                'post_infarct_septal_rupture': post_infarct_septal_rupture
            },
            'results': {
                'mortality_risk': result['mortality_risk'],
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('euroscore2')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Nashef SA, et al. EuroSCORE II. Eur J Cardiothorac Surg. 2012;41(4):734-744.
        - EuroSCORE II Interactive Calculator: https://www.euroscore.org/calc.html
        """)
    
    # History
    render_history_ui(calculator_id="euroscore2", show_actions=True)
