"""
Acute Pancreatitis Prediction Model
===================================

Estimates the likelihood of acute pancreatitis in patients with elevated 
serum lipase levels prior to imaging confirmation.

Reference:
- Various studies on acute pancreatitis prediction models
- Combines clinical and laboratory factors to predict acute pancreatitis

Components:
- Age
- Sex
- Abdominal pain location
- Pain characteristics
- Serum lipase level
- Serum amylase level
- White blood cell count
- C-reactive protein (CRP)
- History of gallstones
- History of alcohol use
- Previous pancreatitis

Output:
- Probability of acute pancreatitis (%)
- Risk category
- Recommendation for imaging

Clinical Utility:
- Early diagnosis before imaging
- Guides initial management
- Helps prioritize imaging studies
- Used in emergency and GI medicine
"""

import streamlit as st
from scores.utils.validation import validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_acute_pancreatitis_probability(
    age: int,
    is_female: bool,
    epigastric_pain: bool,
    pain_radiates_back: bool,
    pain_severe: bool,
    serum_lipase: float,
    serum_amylase: float,
    wbc: float,
    crp: float,
    gallstones: bool,
    alcohol_use: bool,
    previous_pancreatitis: bool
) -> dict:
    """
    Calculate Acute Pancreatitis Probability
    
    Args:
        age: Age (years)
        is_female: Female sex
        epigastric_pain: Epigastric pain location
        pain_radiates_back: Pain radiates to back
        pain_severe: Severe pain
        serum_lipase: Serum lipase (U/L) - normal <60
        serum_amylase: Serum amylase (U/L) - normal <100
        wbc: White blood cell count (×10³/μL)
        crp: C-reactive protein (mg/L)
        gallstones: History of gallstones
        alcohol_use: History of alcohol use
        previous_pancreatitis: Previous pancreatitis
    
    Returns:
        Dictionary with probability, risk category, and recommendation
    """
    score = 0
    details = []
    
    # Age (older patients at higher risk)
    if age >= 60:
        score += 2
        details.append(f"Tuổi {age} (≥60) → +2 điểm")
    elif age >= 40:
        score += 1
        details.append(f"Tuổi {age} (40-59) → +1 điểm")
    else:
        details.append(f"Tuổi {age} (<40) → 0 điểm")
    
    # Sex (females more common with gallstones)
    if is_female:
        score += 1
        details.append("Giới tính nữ → +1 điểm")
    else:
        details.append("Giới tính nam → 0 điểm")
    
    # Pain location - epigastric
    if epigastric_pain:
        score += 3
        details.append("Đau thượng vị → +3 điểm")
    else:
        details.append("Không đau thượng vị → 0 điểm")
    
    # Pain radiates to back
    if pain_radiates_back:
        score += 2
        details.append("Đau lan ra sau lưng → +2 điểm")
    else:
        details.append("Đau không lan ra sau lưng → 0 điểm")
    
    # Severe pain
    if pain_severe:
        score += 2
        details.append("Đau dữ dội → +2 điểm")
    else:
        details.append("Đau không dữ dội → 0 điểm")
    
    # Serum lipase (most specific)
    if serum_lipase >= 600:
        score += 5
        details.append(f"Lipase {serum_lipase:.0f} U/L (≥600, rất cao) → +5 điểm")
    elif serum_lipase >= 300:
        score += 4
        details.append(f"Lipase {serum_lipase:.0f} U/L (300-599, cao) → +4 điểm")
    elif serum_lipase >= 180:
        score += 3
        details.append(f"Lipase {serum_lipase:.0f} U/L (180-299, tăng) → +3 điểm")
    elif serum_lipase >= 60:
        score += 1
        details.append(f"Lipase {serum_lipase:.0f} U/L (60-179, tăng nhẹ) → +1 điểm")
    else:
        details.append(f"Lipase {serum_lipase:.0f} U/L (<60, bình thường) → 0 điểm")
    
    # Serum amylase
    if serum_amylase >= 300:
        score += 3
        details.append(f"Amylase {serum_amylase:.0f} U/L (≥300, rất cao) → +3 điểm")
    elif serum_amylase >= 200:
        score += 2
        details.append(f"Amylase {serum_amylase:.0f} U/L (200-299, cao) → +2 điểm")
    elif serum_amylase >= 100:
        score += 1
        details.append(f"Amylase {serum_amylase:.0f} U/L (100-199, tăng) → +1 điểm")
    else:
        details.append(f"Amylase {serum_amylase:.0f} U/L (<100, bình thường) → 0 điểm")
    
    # WBC (inflammation marker)
    if wbc >= 15:
        score += 2
        details.append(f"WBC {wbc:.1f} ×10³/μL (≥15, tăng cao) → +2 điểm")
    elif wbc >= 12:
        score += 1
        details.append(f"WBC {wbc:.1f} ×10³/μL (12-14.9, tăng) → +1 điểm")
    else:
        details.append(f"WBC {wbc:.1f} ×10³/μL (<12, bình thường) → 0 điểm")
    
    # CRP (inflammation marker)
    if crp >= 150:
        score += 2
        details.append(f"CRP {crp:.1f} mg/L (≥150, rất cao) → +2 điểm")
    elif crp >= 100:
        score += 1
        details.append(f"CRP {crp:.1f} mg/L (100-149, cao) → +1 điểm")
    else:
        details.append(f"CRP {crp:.1f} mg/L (<100, bình thường/tăng nhẹ) → 0 điểm")
    
    # Risk factors
    if gallstones:
        score += 3
        details.append("Tiền sử sỏi mật → +3 điểm")
    else:
        details.append("Không có tiền sử sỏi mật → 0 điểm")
    
    if alcohol_use:
        score += 2
        details.append("Tiền sử uống rượu → +2 điểm")
    else:
        details.append("Không có tiền sử uống rượu → 0 điểm")
    
    if previous_pancreatitis:
        score += 3
        details.append("Tiền sử viêm tụy → +3 điểm")
    else:
        details.append("Không có tiền sử viêm tụy → 0 điểm")
    
    # Convert score to probability (simplified model)
    # Higher score = higher probability
    max_score = 30  # Theoretical maximum
    probability = min(95.0, max(5.0, (score / max_score) * 100))
    
    # Risk category
    if probability >= 70:
        risk_category = "Khả năng rất cao"
        recommendation = "Chẩn đoán viêm tụy cấp rất có thể. Chụp CT bụng để xác nhận và đánh giá biến chứng."
    elif probability >= 50:
        risk_category = "Khả năng cao"
        recommendation = "Chẩn đoán viêm tụy cấp có thể. Chụp CT bụng để xác nhận."
    elif probability >= 30:
        risk_category = "Khả năng trung bình"
        recommendation = "Có thể là viêm tụy cấp. Cân nhắc chụp CT bụng nếu lâm sàng nghi ngờ."
    else:
        risk_category = "Khả năng thấp"
        recommendation = "Khả năng viêm tụy cấp thấp. Theo dõi và đánh giá lại."
    
    return {
        "score": score,
        "probability": probability,
        "risk_category": risk_category,
        "recommendation": recommendation,
        "details": details
    }


def render():
    """Render Acute Pancreatitis Prediction Model interface"""
    import streamlit as st
    
    st.set_page_config(page_title="Acute Pancreatitis Prediction", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🩺 Acute Pancreatitis Prediction Model</h2>
    <p style='text-align: center; color: #6B7280;'>
    Ước tính khả năng viêm tụy cấp ở bệnh nhân có nồng độ lipase huyết thanh tăng cao<br>
    Trước khi xác nhận bằng hình ảnh
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Acute Pancreatitis Prediction Model"):
        st.markdown("""
        **Acute Pancreatitis Prediction Model** là công cụ dự đoán khả năng viêm tụy cấp 
        ở bệnh nhân có nồng độ lipase huyết thanh tăng cao trước khi xác nhận bằng hình ảnh.
        
        ### Các yếu tố đánh giá:
        - Tuổi, giới tính
        - Đặc điểm đau bụng (vị trí, mức độ, lan tỏa)
        - Xét nghiệm: Lipase, Amylase, WBC, CRP
        - Yếu tố nguy cơ: Sỏi mật, rượu, viêm tụy trước đó
        
        ### Phân loại khả năng:
        - **≥70%:** Khả năng rất cao
        - **50-69%:** Khả năng cao
        - **30-49%:** Khả năng trung bình
        - **<30%:** Khả năng thấp
        
        ### Ứng dụng lâm sàng:
        - Chẩn đoán sớm trước khi có hình ảnh
        - Hướng dẫn quản lý ban đầu
        - Giúp ưu tiên chỉ định chụp CT
        - Dùng trong cấp cứu và tiêu hóa
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=50,
            step=1,
            key="ap_age"
        )
    
    with col2:
        is_female = st.selectbox(
            "Giới tính",
            ["Nam", "Nữ"],
            key="ap_sex"
        ) == "Nữ"
    
    st.markdown("### 😣 Đặc điểm đau bụng")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        epigastric_pain = st.checkbox(
            "Đau thượng vị",
            key="ap_epigastric"
        )
    
    with col2:
        pain_radiates_back = st.checkbox(
            "Đau lan ra sau lưng",
            key="ap_radiates"
        )
    
    with col3:
        pain_severe = st.checkbox(
            "Đau dữ dội",
            key="ap_severe"
        )
    
    st.markdown("### 🧪 Xét nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        serum_lipase = st.number_input(
            "Lipase huyết thanh (U/L)",
            min_value=0.0,
            max_value=5000.0,
            value=200.0,
            step=10.0,
            format="%.0f",
            key="ap_lipase",
            help="Bình thường <60 U/L"
        )
        
        serum_amylase = st.number_input(
            "Amylase huyết thanh (U/L)",
            min_value=0.0,
            max_value=2000.0,
            value=150.0,
            step=10.0,
            format="%.0f",
            key="ap_amylase",
            help="Bình thường <100 U/L"
        )
    
    with col2:
        wbc = st.number_input(
            "Số lượng bạch cầu (×10³/μL)",
            min_value=0.0,
            max_value=50.0,
            value=10.0,
            step=0.1,
            format="%.1f",
            key="ap_wbc"
        )
        
        crp = st.number_input(
            "C-reactive protein (CRP) (mg/L)",
            min_value=0.0,
            max_value=500.0,
            value=50.0,
            step=1.0,
            format="%.1f",
            key="ap_crp"
        )
    
    st.markdown("### 🩺 Yếu tố nguy cơ")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gallstones = st.checkbox("Tiền sử sỏi mật", key="ap_gallstones")
    
    with col2:
        alcohol_use = st.checkbox("Tiền sử uống rượu", key="ap_alcohol")
    
    with col3:
        previous_pancreatitis = st.checkbox("Tiền sử viêm tụy", key="ap_previous")
    
    if st.button("🔬 Tính khả năng viêm tụy cấp", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        if serum_lipase < 0 or serum_lipase > 5000:
            errors.append("Lipase phải từ 0-5000 U/L")
        if serum_amylase < 0 or serum_amylase > 2000:
            errors.append("Amylase phải từ 0-2000 U/L")
        if wbc < 0 or wbc > 50:
            errors.append("WBC phải từ 0-50 ×10³/μL")
        if crp < 0 or crp > 500:
            errors.append("CRP phải từ 0-500 mg/L")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_acute_pancreatitis_probability(
                age=age,
                is_female=is_female,
                epigastric_pain=epigastric_pain,
                pain_radiates_back=pain_radiates_back,
                pain_severe=pain_severe,
                serum_lipase=serum_lipase,
                serum_amylase=serum_amylase,
                wbc=wbc,
                crp=crp,
                gallstones=gallstones,
                alcohol_use=alcohol_use,
                previous_pancreatitis=previous_pancreatitis
            )
            
            # Display results
            st.markdown("---")
            st.markdown("### 📋 Kết quả dự đoán")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Điểm số", f"{result['score']}")
            
            with col2:
                st.metric(
                    "Khả năng viêm tụy cấp",
                    f"{result['probability']:.1f}%"
                )
            
            with col3:
                st.metric(
                    "Phân loại",
                    result['risk_category']
                )
            
            # Details
            st.markdown("### 📝 Chi tiết tính điểm")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            # Recommendation
            st.markdown("### 💡 Khuyến nghị")
            
            if result['probability'] >= 70:
                st.error(f"**{result['risk_category']}**")
                st.markdown(f"{result['recommendation']}")
                st.markdown("""
                **Hành động ngay:**
                - Chụp CT bụng có cản quang
                - Đánh giá mức độ nặng (BISAP, Ranson)
                - Điều trị hỗ trợ tích cực
                - Theo dõi sát tại bệnh viện
                """)
            elif result['probability'] >= 50:
                st.warning(f"**{result['risk_category']}**")
                st.markdown(f"{result['recommendation']}")
                st.markdown("""
                **Hành động:**
                - Chụp CT bụng để xác nhận
                - Điều trị hỗ trợ
                - Theo dõi tại bệnh viện
                """)
            elif result['probability'] >= 30:
                st.info(f"**{result['risk_category']}**")
                st.markdown(f"{result['recommendation']}")
                st.markdown("""
                **Hành động:**
                - Theo dõi lâm sàng
                - Cân nhắc chụp CT nếu không cải thiện
                - Điều trị triệu chứng
                """)
            else:
                st.success(f"**{result['risk_category']}**")
                st.markdown(f"{result['recommendation']}")
                st.markdown("""
                **Hành động:**
                - Theo dõi và đánh giá lại
                - Điều trị triệu chứng
                - Tìm nguyên nhân khác nếu cần
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="acute_pancreatitis",
                calculator_name="Acute Pancreatitis Prediction",
                inputs={
                    "Tuổi": f"{age}",
                    "Giới tính": "Nữ" if is_female else "Nam",
                    "Lipase": f"{serum_lipase:.0f}",
                    "Amylase": f"{serum_amylase:.0f}",
                    "WBC": f"{wbc:.1f}",
                    "CRP": f"{crp:.1f}"
                },
                result={
                    "Điểm": f"{result['score']}",
                    "Khả năng": f"{result['probability']:.1f}%",
                    "Phân loại": result['risk_category']
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="acute_pancreatitis",
                calculator_name="Acute Pancreatitis Prediction"
            )
            
            render_export_section(
                calculator_id="acute_pancreatitis",
                calculator_name="Acute Pancreatitis Prediction",
                data={
                    "inputs": {
                        "age": age,
                        "is_female": is_female,
                        "epigastric_pain": epigastric_pain,
                        "pain_radiates_back": pain_radiates_back,
                        "pain_severe": pain_severe,
                        "serum_lipase": serum_lipase,
                        "serum_amylase": serum_amylase,
                        "wbc": wbc,
                        "crp": crp,
                        "gallstones": gallstones,
                        "alcohol_use": alcohol_use,
                        "previous_pancreatitis": previous_pancreatitis
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="acute_pancreatitis", show_actions=True)
    
    # References
    references = get_references("Acute Pancreatitis Prediction Model")
    if references:
        render_references_section(references)

