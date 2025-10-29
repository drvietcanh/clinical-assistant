"""
Scores Module - Clinical Scoring Systems
Organized by Specialty
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Scores - Clinical Assistant", page_icon="📊", layout="wide")

# ========== HEADER ==========
st.title("📊 Thang Điểm Lâm Sàng")
st.markdown("Calculators phân loại theo chuyên khoa")
st.markdown("---")

# ========== SCORING SYSTEMS ORGANIZED BY SPECIALTY ==========
SCORES_BY_SPECIALTY = {
    "🚨 Cấp Cứu & Hồi Sức (Emergency & Critical Care)": {
        "qSOFA": {"name": "qSOFA - Quick SOFA", "desc": "Sàng lọc nhiễm trùng huyết", "status": "✅"},
        "SOFA": {"name": "SOFA - Sequential Organ Failure Assessment", "desc": "Đánh giá suy cơ quan", "status": "🚧"},
        "APACHE II": {"name": "APACHE II", "desc": "Dự đoán tử vong ICU", "status": "🚧"},
        "SAPS II": {"name": "SAPS II - Simplified Acute Physiology Score", "desc": "Độ nặng bệnh nhân ICU", "status": "📋"},
        "MODS": {"name": "MODS - Multiple Organ Dysfunction Score", "desc": "Rối loạn đa cơ quan", "status": "📋"},
    },
    
    "❤️ Tim Mạch (Cardiology)": {
        "CHA2DS2-VASc": {"name": "CHA₂DS₂-VASc", "desc": "Nguy cơ đột quỵ trong rung nhĩ", "status": "🚧"},
        "HAS-BLED": {"name": "HAS-BLED", "desc": "Nguy cơ chảy máu khi dùng kháng đông", "status": "🚧"},
        "TIMI Risk": {"name": "TIMI Risk Score", "desc": "Nguy cơ NSTEMI/STEMI", "status": "📋"},
        "GRACE Score": {"name": "GRACE Score", "desc": "Tiên lượng ACS", "status": "📋"},
        "HEART Score": {"name": "HEART Score", "desc": "Đau ngực cấp - nguy cơ ACS", "status": "📋"},
        "Framingham": {"name": "Framingham Risk Score", "desc": "Nguy cơ tim mạch 10 năm", "status": "📋"},
    },
    
    "🫁 Hô Hấp (Respiratory)": {
        "CURB-65": {"name": "CURB-65", "desc": "Mức độ nặng viêm phổi", "status": "🚧"},
        "PSI/PORT": {"name": "PSI/PORT Score", "desc": "Tiên lượng viêm phổi cộng đồng", "status": "📋"},
        "SMART-COP": {"name": "SMART-COP", "desc": "Cần hỗ trợ hô hấp trong viêm phổi", "status": "📋"},
        "BODE Index": {"name": "BODE Index", "desc": "Tiên lượng COPD", "status": "📋"},
        "Wells PE": {"name": "Wells PE Score", "desc": "Nguy cơ th栓 tắc phổi", "status": "📋"},
    },
    
    "🧠 Thần Kinh (Neurology)": {
        "GCS": {"name": "GCS - Glasgow Coma Scale", "desc": "Mức độ ý thức", "status": "🚧"},
        "NIHSS": {"name": "NIHSS - NIH Stroke Scale", "desc": "Mức độ nặng đột quỵ", "status": "📋"},
        "ICH Score": {"name": "ICH Score", "desc": "Tiên lượng xuất huyết nội sọ", "status": "📋"},
        "Hunt & Hess": {"name": "Hunt & Hess Scale", "desc": "Phân loại xuất huyết dưới nhện", "status": "📋"},
        "mRS": {"name": "mRS - Modified Rankin Scale", "desc": "Mức độ khuyết tật sau đột quỵ", "status": "📋"},
    },
    
    "🩸 Tiêu Hóa - Gan Mật (GI/Hepatology)": {
        "Rockall Score": {"name": "Rockall Score", "desc": "Nguy cơ xuất huyết tiêu hóa trên", "status": "📋"},
        "Glasgow-Blatchford": {"name": "Glasgow-Blatchford Score", "desc": "UGIB - cần can thiệp", "status": "📋"},
        "Child-Pugh": {"name": "Child-Pugh Score", "desc": "Mức độ xơ gan", "status": "📋"},
        "MELD": {"name": "MELD Score", "desc": "Tiên lượng bệnh gan mạn", "status": "📋"},
        "MELD-Na": {"name": "MELD-Na", "desc": "MELD điều chỉnh theo Na", "status": "🚧"},
        "Ranson": {"name": "Ranson Criteria", "desc": "Tiên lượng viêm tụy cấp", "status": "📋"},
    },
    
    "🩺 Huyết Học & Đông Máu (Hematology)": {
        "Wells DVT": {"name": "Wells DVT Score", "desc": "Nguy cơ huyết khối tĩnh mạch sâu", "status": "📋"},
        "4Ts Score": {"name": "4Ts Score - HIT", "desc": "Giảm tiểu cầu do heparin", "status": "📋"},
        "DIC Score": {"name": "DIC Score (ISTH)", "desc": "Đông máu rải rác trong lòng mạch", "status": "📋"},
    },
    
    "🧪 Thận - Điện Giải (Nephrology)": {
        "RIFLE": {"name": "RIFLE Criteria", "desc": "Phân loại AKI", "status": "📋"},
        "AKIN": {"name": "AKIN Criteria", "desc": "Suy thận cấp", "status": "📋"},
        "KDIGO": {"name": "KDIGO Staging", "desc": "Giai đoạn AKI", "status": "📋"},
    },
    
    "🦴 Chấn Thương & Chỉnh Hình (Trauma/Orthopedics)": {
        "ISS": {"name": "ISS - Injury Severity Score", "desc": "Mức độ nặng đa chấn thương", "status": "📋"},
        "RTS": {"name": "RTS - Revised Trauma Score", "desc": "Tiên lượng chấn thương", "status": "📋"},
        "NEXUS": {"name": "NEXUS C-Spine", "desc": "Cần chụp X-quang cột sống cổ", "status": "📋"},
        "Canadian C-Spine": {"name": "Canadian C-Spine Rule", "desc": "Chỉ định chụp cột sống cổ", "status": "📋"},
    },
    
    "👶 Nhi Khoa (Pediatrics)": {
        "PEWS": {"name": "PEWS - Pediatric Early Warning Score", "desc": "Cảnh báo sớm nhi", "status": "📋"},
        "APGAR": {"name": "APGAR Score", "desc": "Đánh giá trẻ sơ sinh", "status": "📋"},
        "Pediatric GCS": {"name": "Pediatric GCS", "desc": "Ý thức trẻ em", "status": "📋"},
    },
    
    "🤰 Sản Khoa (Obstetrics)": {
        "Bishop Score": {"name": "Bishop Score", "desc": "Đánh giá cổ tử cung", "status": "📋"},
        "Modified Bishop": {"name": "Modified Bishop Score", "desc": "Dự đoán chuyển dạ", "status": "📋"},
    },
    
    "💉 Nội Tiết - Chuyển Hóa (Endocrinology/Metabolism)": {
        "HbA1c": {"name": "HbA1c - eAG Converter", "desc": "Chuyển đổi HbA1c sang đường huyết trung bình", "status": "📋"},
        "Corrected Ca": {"name": "Corrected Calcium", "desc": "Canxi điều chỉnh theo albumin", "status": "📋"},
        "FENa": {"name": "FENa - Fractional Excretion of Sodium", "desc": "Phân biệt AKI tiền thận/thận", "status": "📋"},
        "Anion Gap": {"name": "Anion Gap", "desc": "Khoảng trống anion - rối loạn acid-base", "status": "📋"},
        "Winter Formula": {"name": "Winter Formula", "desc": "PCO2 dự đoán trong toan chuyển hóa", "status": "📋"},
        "Corrected QT": {"name": "QTc - Corrected QT Interval", "desc": "QT điều chỉnh theo nhịp tim", "status": "📋"},
        "Free T4 Index": {"name": "Free T4 Index (FTI)", "desc": "Chỉ số T4 tự do", "status": "📋"},
    },
    
    "🦴 Thấp Khớp - Miễn Dịch (Rheumatology/Immunology)": {
        "DAS28": {"name": "DAS28 - Disease Activity Score", "desc": "Hoạt động bệnh viêm khớp dạng thấp", "status": "📋"},
        "CDAI": {"name": "CDAI - Clinical Disease Activity Index", "desc": "Chỉ số hoạt động lâm sàng RA", "status": "📋"},
        "SDAI": {"name": "SDAI - Simplified Disease Activity Index", "desc": "Chỉ số đơn giản hóa RA", "status": "📋"},
        "ACR Criteria": {"name": "ACR/EULAR RA Classification", "desc": "Tiêu chuẩn chẩn đoán viêm khớp dạng thấp", "status": "📋"},
        "SLICC": {"name": "SLICC Criteria", "desc": "Tiêu chuẩn lupus ban đỏ hệ thống", "status": "📋"},
        "SLEDAI": {"name": "SLEDAI - SLE Disease Activity Index", "desc": "Hoạt động bệnh lupus", "status": "📋"},
        "Gout Diagnostic": {"name": "ACR/EULAR Gout Classification", "desc": "Chẩn đoán bệnh gout", "status": "📋"},
    },
    
    "🦠 Nhiễm Khuẩn (Infectious Disease)": {
        "SIRS": {"name": "SIRS - Systemic Inflammatory Response", "desc": "Hội chứng đáp ứng viêm toàn thân", "status": "📋"},
        "Pitt Bacteremia": {"name": "Pitt Bacteremia Score", "desc": "Tiên lượng nhiễm khuẩn huyết", "status": "📋"},
        "MASCC": {"name": "MASCC Risk Index", "desc": "Nguy cơ sốt giảm bạch cầu hạt", "status": "📋"},
        "Centor": {"name": "Centor Score", "desc": "Viêm họng do liên cầu", "status": "📋"},
        "FeverPAIN": {"name": "FeverPAIN Score", "desc": "Viêm amidan - cần kháng sinh", "status": "📋"},
    },
    
    "🩹 Da Liễu (Dermatology)": {
        "PASI": {"name": "PASI - Psoriasis Area Severity Index", "desc": "Mức độ nặng vẩy nến", "status": "📋"},
        "SCORAD": {"name": "SCORAD - SCORing Atopic Dermatitis", "desc": "Điểm viêm da cơ địa", "status": "📋"},
        "DLQI": {"name": "DLQI - Dermatology Life Quality Index", "desc": "Chất lượng cuộc sống bệnh da", "status": "📋"},
        "Burn TBSA": {"name": "TBSA - Total Body Surface Area", "desc": "Diện tích bỏng (quy tắc số 9)", "status": "📋"},
        "Parkland Formula": {"name": "Parkland Formula", "desc": "Truyền dịch ban đầu cho bỏng", "status": "📋"},
    },
    
    "🎗️ Ung Thư (Oncology)": {
        "ECOG": {"name": "ECOG Performance Status", "desc": "Trạng thái thể trạng bệnh nhân ung thư", "status": "📋"},
        "Karnofsky": {"name": "Karnofsky Performance Scale", "desc": "Thang đo thể trạng", "status": "📋"},
        "Palliative Performance": {"name": "PPS - Palliative Performance Scale", "desc": "Thể trạng chăm sóc giảm nhẹ", "status": "📋"},
        "CIPN Grading": {"name": "CIPN Grading", "desc": "Phân độ tổn thương thần kinh ngoại biên", "status": "📋"},
    },
    
    "🧠 Tâm Thần - Tâm Lý (Psychiatry/Psychology)": {
        "PHQ-9": {"name": "PHQ-9 - Patient Health Questionnaire", "desc": "Sàng lọc trầm cảm", "status": "📋"},
        "GAD-7": {"name": "GAD-7 - Generalized Anxiety Disorder", "desc": "Rối loạn lo âu lan tỏa", "status": "📋"},
        "MMSE": {"name": "MMSE - Mini Mental State Exam", "desc": "Đánh giá nhận thức", "status": "📋"},
        "MoCA": {"name": "MoCA - Montreal Cognitive Assessment", "desc": "Đánh giá nhận thức Montreal", "status": "📋"},
        "CAM": {"name": "CAM - Confusion Assessment Method", "desc": "Đánh giá hôn mê lú lẫn", "status": "📋"},
        "CIWA-Ar": {"name": "CIWA-Ar", "desc": "Cai rượu - mức độ nặng", "status": "📋"},
        "COWS": {"name": "COWS - Clinical Opiate Withdrawal", "desc": "Cai opioid", "status": "📋"},
    },
    
    "🔪 Phẫu Thuật & Gây Mê (Surgery/Anesthesia)": {
        "ASA": {"name": "ASA Physical Status", "desc": "Phân loại nguy cơ phẫu thuật", "status": "📋"},
        "P-POSSUM": {"name": "P-POSSUM Score", "desc": "Nguy cơ tử vong phẫu thuật", "status": "📋"},
        "RCRI": {"name": "RCRI - Revised Cardiac Risk Index", "desc": "Nguy cơ tim mạch phẫu thuật", "status": "📋"},
        "Caprini": {"name": "Caprini VTE Risk Score", "desc": "Nguy cơ huyết khối sau phẫu thuật", "status": "📋"},
        "Aldrete Score": {"name": "Aldrete Score", "desc": "Hồi tỉnh sau gây mê", "status": "📋"},
        "Mallampati": {"name": "Mallampati Classification", "desc": "Đánh giá đường thở khó", "status": "📋"},
    },
    
    "👁️ Mắt (Ophthalmology)": {
        "Intraocular Pressure": {"name": "IOP Correction", "desc": "Điều chỉnh nhãn áp theo CCT", "status": "📋"},
    },
    
    "👂 Tai Mũi Họng (ENT)": {
        "Epworth": {"name": "Epworth Sleepiness Scale", "desc": "Mức độ buồn ngủ ban ngày", "status": "📋"},
        "STOP-BANG": {"name": "STOP-BANG Questionnaire", "desc": "Sàng lọc ngưng thở khi ngủ", "status": "📋"},
    },
}

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Chọn Chuyên Khoa")
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        list(SCORES_BY_SPECIALTY.keys()),
        index=0  # Default: Emergency & Critical Care
    )
    
    st.markdown("---")
    
    st.subheader("Thang Điểm Có Sẵn")
    
    # Display scores for selected specialty
    scores_in_specialty = SCORES_BY_SPECIALTY[specialty]
    
    score_options = []
    for score_id, score_info in scores_in_specialty.items():
        score_options.append(f"{score_info['status']} {score_info['name']}")
    
    selected_score_display = st.radio(
        "Calculator:",
        score_options,
        label_visibility="collapsed"
    )
    
    # Extract score_id from selection
    selected_score_id = None
    for score_id, score_info in scores_in_specialty.items():
        if score_info['name'] in selected_score_display:
            selected_score_id = score_id
            break
    
    st.markdown("---")
    st.info("""
    **Chú thích:**
    - ✅ Hoàn thành
    - 🚧 Đang phát triển
    - 📋 Kế hoạch
    """)
    
    st.markdown("---")
    st.caption(f"**{len([s for specialty_scores in SCORES_BY_SPECIALTY.values() for s in specialty_scores])}** calculators")
    st.caption("**Evidence-based**")

# ========== MAIN CONTENT ==========

# Display specialty overview
st.info(f"""
**Chuyên khoa:** {specialty}

**Số lượng calculators:** {len(scores_in_specialty)}

**Đang xem:** {SCORES_BY_SPECIALTY[specialty][selected_score_id]['name'] if selected_score_id else 'Chọn calculator bên trái'}
""")

# ===== qSOFA =====
if selected_score_id == "qSOFA":
    st.subheader("🩺 qSOFA (Quick SOFA)")
    st.caption("Sepsis-3 Criteria for Sepsis Screening")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Patient Parameters")
        
        # Inputs
        rr = st.number_input(
            "Respiratory Rate (/min)",
            min_value=0,
            max_value=60,
            value=20,
            step=1,
            help="Normal: 12-20 /min"
        )
        
        sbp = st.number_input(
            "Systolic Blood Pressure (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=1,
            help="Normal: 90-120 mmHg"
        )
        
        gcs = st.number_input(
            "Glasgow Coma Scale",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            help="Normal: 15; Coma: 3"
        )
        
        # Calculate button
        if st.button("🔢 Calculate qSOFA", type="primary"):
            # Calculation
            score = 0
            details = []
            
            if rr >= 22:
                score += 1
                details.append("✓ Respiratory rate ≥22 /min (+1)")
            else:
                details.append("✗ Respiratory rate <22 /min (0)")
            
            if sbp <= 100:
                score += 1
                details.append("✓ Systolic BP ≤100 mmHg (+1)")
            else:
                details.append("✗ Systolic BP >100 mmHg (0)")
            
            if gcs < 15:
                score += 1
                details.append("✓ Altered mentation (GCS <15) (+1)")
            else:
                details.append("✗ GCS = 15 (0)")
            
            # Display result
            with col2:
                st.markdown("### Result")
                
                # Score display
                if score >= 2:
                    st.error(f"## qSOFA = {score}")
                    st.error("⚠️ **CONCERNING FOR SEPSIS**")
                    interpretation = """
                    **Action Required:**
                    - Assess for infection source
                    - Consider blood cultures
                    - Start antibiotics if indicated
                    - Monitor closely
                    - Calculate full SOFA score
                    """
                elif score == 1:
                    st.warning(f"## qSOFA = {score}")
                    st.warning("⚡ Intermediate Risk")
                    interpretation = """
                    **Consider:**
                    - Close monitoring
                    - Reassess frequently
                    - Look for other sepsis signs
                    """
                else:
                    st.success(f"## qSOFA = {score}")
                    st.success("✅ Low Risk")
                    interpretation = """
                    **Interpretation:**
                    - Low probability of sepsis
                    - Routine monitoring
                    - Reassess if clinical change
                    """
                
                st.markdown(interpretation)
            
            # Details
            st.markdown("### Breakdown")
            for detail in details:
                st.write(detail)
            
            # Reference
            with st.expander("📚 Clinical Reference"):
                st.markdown("""
                **qSOFA (Quick SOFA) Score**
                
                **Purpose:** Rapid bedside screening for sepsis outside ICU
                
                **Criteria (1 point each):**
                1. Respiratory rate ≥ 22/min
                2. Altered mentation (GCS < 15)
                3. Systolic blood pressure ≤ 100 mmHg
                
                **Interpretation:**
                - **qSOFA ≥ 2:** Concerning for sepsis
                  - Increased risk of death or prolonged ICU stay
                  - Triggers full SOFA assessment
                  - Consider sepsis bundle
                
                - **qSOFA < 2:** Lower risk
                  - Does NOT rule out infection
                  - Clinical judgment still essential
                
                **Limitations:**
                - NOT for diagnosis, only screening
                - Less sensitive than SIRS criteria
                - Better specificity for adverse outcomes
                
                **Reference:**
                Singer M, et al. The Third International Consensus Definitions 
                for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810.
                doi:10.1001/jama.2016.0287
                
                **Guidelines:**
                - Surviving Sepsis Campaign 2021
                - Use as part of clinical assessment
                - Not a standalone diagnostic tool
                """)
    
    # Additional tools
    st.markdown("---")
    st.info("""
    **Next Steps:**
    - If qSOFA ≥2 → Calculate full **SOFA score**
    - Consider **Sepsis Bundle** protocol
    - Review **Antibiotic** selection
    """)

# ===== SOFA =====
elif selected_score_id == "SOFA":
    st.subheader("🏥 SOFA Score")
    st.caption("Sequential Organ Failure Assessment")
    
    st.warning("""
    🚧 **Under Development**
    
    SOFA calculator đang được phát triển.
    
    **Dự kiến hoàn thành:** Week 2
    
    **Sẽ bao gồm:**
    - Respiratory (PaO₂/FiO₂)
    - Coagulation (Platelets)
    - Liver (Bilirubin)
    - Cardiovascular (MAP, Vasopressors)
    - CNS (GCS)
    - Renal (Creatinine, Urine output)
    """)
    
    st.markdown("### Preview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pao2_fio2 = st.number_input("PaO₂/FiO₂ (mmHg)", value=350)
    with col2:
        platelets = st.number_input("Platelets (×10³/µL)", value=150)
    with col3:
        bilirubin = st.number_input("Bilirubin (mg/dL)", value=1.0, step=0.1)
    
    st.info("Full SOFA calculator coming soon...")

# ===== CHA2DS2-VASc =====
elif selected_score_id == "CHA2DS2-VASc":
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Stroke Risk Stratification in Atrial Fibrillation")
    
    st.warning("🚧 **Under Development** - Expected: Week 2")
    
    st.markdown("""
    **Will include:**
    - C: Congestive heart failure (1 point)
    - H: Hypertension (1 point)
    - A₂: Age ≥75 (2 points)
    - D: Diabetes (1 point)
    - S₂: Prior Stroke/TIA (2 points)
    - V: Vascular disease (1 point)
    - A: Age 65-74 (1 point)
    - Sc: Sex category (Female = 1 point)
    
    **Reference:** ESC AF Guidelines 2020
    """)

# ===== HAS-BLED =====
elif selected_score_id == "HAS-BLED":
    st.subheader("🩸 HAS-BLED Score")
    st.caption("Bleeding Risk in Anticoagulated Patients")
    
    st.warning("🚧 **Under Development** - Expected: Week 3")

# ===== CURB-65 =====
elif selected_score_id == "CURB-65":
    st.subheader("🫁 CURB-65")
    st.caption("Pneumonia Severity Assessment")
    
    st.warning("🚧 **Under Development** - Expected: Week 3")

# ===== GCS =====
elif selected_score_id == "GCS":
    st.subheader("🧠 Glasgow Coma Scale")
    st.caption("Level of Consciousness Assessment")
    
    st.warning("🚧 **Under Development** - Expected: Week 2")

# ===== Default: Show all calculators in specialty =====
else:
    st.subheader(f"📋 Danh Sách Calculators - {specialty}")
    
    # Display as cards
    for score_id, score_info in scores_in_specialty.items():
        with st.expander(f"{score_info['status']} {score_info['name']}", expanded=False):
            st.markdown(f"**Mô tả:** {score_info['desc']}")
            
            if score_info['status'] == "✅":
                st.success("✅ Đã hoàn thành - Click để sử dụng")
            elif score_info['status'] == "🚧":
                st.warning("🚧 Đang phát triển - Sắp ra mắt")
            else:
                st.info("📋 Trong kế hoạch phát triển")

# ========== FOOTER ==========
st.markdown("---")
st.caption("📚 All scores based on international guidelines and peer-reviewed literature")
st.caption("⚠️ For reference only - Always use clinical judgment")

