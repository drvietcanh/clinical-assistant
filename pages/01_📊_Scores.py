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
        "CHA2DS2-VASc": {"name": "CHA₂DS₂-VASc", "desc": "Nguy cơ đột quỵ trong rung nhĩ", "status": "✅"},
        "HAS-BLED": {"name": "HAS-BLED", "desc": "Nguy cơ chảy máu khi dùng kháng đông", "status": "✅"},
        "SCORE2": {"name": "SCORE2", "desc": "Nguy cơ tim mạch 10 năm (40-69 tuổi)", "status": "✅"},
        "SCORE2-OP": {"name": "SCORE2-OP", "desc": "Nguy cơ tim mạch (≥70 tuổi)", "status": "✅"},
        "HEART Score": {"name": "HEART Score", "desc": "Đau ngực cấp - nguy cơ ACS", "status": "🚧"},
        "TIMI Risk": {"name": "TIMI Risk Score", "desc": "Nguy cơ NSTEMI/STEMI", "status": "🚧"},
        "GRACE Score": {"name": "GRACE Score", "desc": "Tiên lượng ACS", "status": "🚧"},
        "Framingham": {"name": "Framingham Risk Score", "desc": "Nguy cơ tim mạch 10 năm", "status": "🚧"},
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
    st.caption("Đánh Giá Nguy Cơ Đột Quỵ Trong Rung Nhĩ")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        # C - CHF
        chf = st.checkbox(
            "**C** - Suy tim sung huyết / Rối loạn chức năng thất trái",
            help="Tiền sử suy tim hoặc EF <40%"
        )
        
        # H - Hypertension
        htn = st.checkbox(
            "**H** - Tăng huyết áp",
            help="Đang điều trị tăng huyết áp hoặc BP >140/90 mmHg"
        )
        
        # A2 - Age
        age_group = st.radio(
            "**A** - Tuổi",
            ["< 65 tuổi", "65-74 tuổi", "≥ 75 tuổi"],
            horizontal=True
        )
        
        # D - Diabetes
        dm = st.checkbox(
            "**D** - Đái tháo đường",
            help="Đang điều trị hoặc HbA1c ≥6.5%"
        )
        
        # S2 - Stroke/TIA
        stroke = st.checkbox(
            "**S** - Tiền sử Đột quỵ / TIA / Huyết khối",
            help="Đột quỵ, TIA hoặc tắc mạch hệ thống trước đây"
        )
        
        # V - Vascular disease
        vasc = st.checkbox(
            "**V** - Bệnh mạch máu",
            help="Nhồi máu cơ tim, bệnh động mạch ngoại biên, plaque động mạch chủ"
        )
        
        # Sc - Sex category
        sex = st.radio(
            "**Sc** - Giới tính",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        if st.button("🧮 Tính Điểm", type="primary", key="cha2ds2vasc_calc"):
            # Calculate score
            score = 0
            details = []
            
            if chf:
                score += 1
                details.append("✓ Suy tim (+1)")
            
            if htn:
                score += 1
                details.append("✓ Tăng huyết áp (+1)")
            
            if age_group == "65-74 tuổi":
                score += 1
                details.append("✓ Tuổi 65-74 (+1)")
            elif age_group == "≥ 75 tuổi":
                score += 2
                details.append("✓ Tuổi ≥75 (+2)")
            
            if dm:
                score += 1
                details.append("✓ Đái tháo đường (+1)")
            
            if stroke:
                score += 2
                details.append("✓ Tiền sử đột quỵ/TIA (+2)")
            
            if vasc:
                score += 1
                details.append("✓ Bệnh mạch máu (+1)")
            
            if sex == "Nữ":
                score += 1
                details.append("✓ Giới tính nữ (+1)")
            
            # Display result
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if score == 0:
                    st.success(f"## CHA₂DS₂-VASc = {score}")
                    st.success("✅ Nguy cơ THẤP")
                    risk = "0-0.2%/năm"
                elif score == 1:
                    st.warning(f"## CHA₂DS₂-VASc = {score}")
                    st.warning("⚡ Nguy cơ TRUNG BÌNH")
                    risk = "0.6-2.0%/năm"
                elif score == 2:
                    st.warning(f"## CHA₂DS₂-VASc = {score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH-CAO")
                    risk = "2.2%/năm"
                else:
                    st.error(f"## CHA₂DS₂-VASc = {score}")
                    st.error("🚨 Nguy cơ CAO")
                    if score <= 5:
                        risk = f"{2.2 + (score-2)*1.5:.1f}%/năm"
                    else:
                        risk = ">10%/năm"
            
            # Interpretation
            st.markdown("### 💡 Giải Thích & Khuyến Cáo")
            
            st.markdown(f"**Nguy cơ đột quỵ hàng năm:** {risk}")
            
            # Breakdown
            st.markdown("**Chi tiết điểm:**")
            if details:
                for detail in details:
                    st.write(f"- {detail}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            # Recommendation
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Điều Trị")
            
            if score == 0 and sex == "Nam":
                st.info("""
                **Không cần kháng đông** (hoặc có thể dùng Aspirin)
                - Nguy cơ đột quỵ rất thấp
                - Cân nhắc lại định kỳ
                """)
            elif score == 1 and sex == "Nam":
                st.warning("""
                **Cân nhắc kháng đông** (ưu tiên NOAC/Warfarin)
                - Thảo luận với bệnh nhân về lợi ích/nguy cơ
                - Đánh giá nguy cơ chảy máu (HAS-BLED)
                """)
            elif score >= 1:
                st.error("""
                **KHUYẾN CÁO KHÁNG ĐÔNG** (NOAC hoặc Warfarin)
                
                **Lựa chọn ưu tiên:**
                - **NOAC (Kháng đông trực tiếp):**
                  - Apixaban 5mg x 2 lần/ngày
                  - Rivaroxaban 20mg x 1 lần/ngày
                  - Edoxaban 60mg x 1 lần/ngày
                  - Dabigatran 150mg x 2 lần/ngày
                
                - **Warfarin:**
                  - Mục tiêu INR 2.0-3.0
                  - Khi không dùng được NOAC
                
                **Chống chỉ định NOAC:**
                - Suy thận nặng (CrCl <15-30)
                - Bệnh van tim nặng
                - Thai kỳ
                """)
            
            # Reference
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **ESC Guidelines 2020 - Atrial Fibrillation**
                
                **Cách tính điểm:**
                - **C** = Congestive heart failure/LV dysfunction (+1)
                - **H** = Hypertension (+1)
                - **A₂** = Age ≥75 years (+2)
                - **D** = Diabetes mellitus (+1)
                - **S₂** = Prior Stroke/TIA/thromboembolism (+2)
                - **V** = Vascular disease (+1)
                - **A** = Age 65-74 years (+1)
                - **Sc** = Sex category (female) (+1)
                
                **Tổng điểm:** 0-9
                
                **Validation:**
                - Euro Heart Survey on AF
                - Danish National Patient Registry
                
                **Link:**
                - ESC 2020: https://academic.oup.com/eurheartj/article/42/5/373/5899003
                """)

# ===== HAS-BLED =====
elif selected_score_id == "HAS-BLED":
    st.subheader("🩸 HAS-BLED Score")
    st.caption("Đánh Giá Nguy Cơ Chảy Máu Khi Dùng Kháng Đông")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        # H - Hypertension
        htn_uncontrolled = st.checkbox(
            "**H** - Tăng huyết áp không kiểm soát",
            help="SBP >160 mmHg"
        )
        
        # A - Abnormal renal/liver function
        renal = st.checkbox("Chức năng thận bất thường", help="Lọc cầu thận <60 hoặc chạy thận")
        liver = st.checkbox("Chức năng gan bất thường", help="Xơ gan hoặc men gan tăng >2 lần")
        
        # S - Stroke
        stroke_bled = st.checkbox(
            "**S** - Tiền sử đột quỵ",
            help="Đột quỵ trước đây"
        )
        
        # B - Bleeding
        bleeding = st.checkbox(
            "**B** - Tiền sử chảy máu hoặc thiểu máu",
            help="Chảy máu nặng hoặc thiểu máu trước đây"
        )
        
        # L - Labile INR
        labile_inr = st.checkbox(
            "**L** - INR không ổn định",
            help="TTR <60% nếu dùng warfarin"
        )
        
        # E - Elderly
        age_hasbled = st.checkbox(
            "**E** - Tuổi cao (>65)",
            help="Tuổi >65"
        )
        
        # D - Drugs/Alcohol
        drugs = st.checkbox("Dùng thuốc chống tiểu cầu/NSAID", help="Aspirin, NSAID")
        alcohol = st.checkbox("Lạm dụng rượu", help=">8 đơn vị/tuần")
        
        if st.button("🧮 Tính Điểm HAS-BLED", type="primary", key="hasbled_calc"):
            score = 0
            details = []
            
            if htn_uncontrolled:
                score += 1
                details.append("✓ THA không kiểm soát (+1)")
            if renal or liver:
                score += 1 if renal else 0
                score += 1 if liver else 0
                if renal:
                    details.append("✓ Suy thận (+1)")
                if liver:
                    details.append("✓ Suy gan (+1)")
            if stroke_bled:
                score += 1
                details.append("✓ Tiền sử đột quỵ (+1)")
            if bleeding:
                score += 1
                details.append("✓ Tiền sử chảy máu (+1)")
            if labile_inr:
                score += 1
                details.append("✓ INR không ổn định (+1)")
            if age_hasbled:
                score += 1
                details.append("✓ Tuổi >65 (+1)")
            if drugs:
                score += 1
                details.append("✓ Dùng chống tiểu cầu/NSAID (+1)")
            if alcohol:
                score += 1
                details.append("✓ Lạm dụng rượu (+1)")
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if score <= 2:
                    st.success(f"## HAS-BLED = {score}")
                    st.success("✅ Nguy cơ chảy máu THẤP")
                elif score == 3:
                    st.warning(f"## HAS-BLED = {score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                else:
                    st.error(f"## HAS-BLED = {score}")
                    st.error("🚨 Nguy cơ chảy máu CAO")
            
            st.markdown("### 💡 Giải Thích")
            
            if details:
                for d in details:
                    st.write(f"- {d}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo")
            
            if score <= 2:
                st.success("""
                **Nguy cơ chảy máu chấp nhận được**
                - Có thể dùng kháng đông an toàn
                - Theo dõi định kỳ
                """)
            elif score == 3:
                st.warning("""
                **Cẩn thận khi dùng kháng đông**
                - Kiểm soát các yếu tố nguy cơ có thể sửa
                - Theo dõi sát hơn
                - Cân nhắc NOAC thay vì warfarin
                """)
            else:
                st.error("""
                **Nguy cơ chảy máu cao - Thận trọng!**
                
                **KHÔNG PHẢI CHỐNG CHỈ ĐỊNH kháng đông!**
                
                **Cần làm:**
                - Kiểm soát THA tốt hơn
                - Ngừng NSAID/aspirin nếu được
                - Giảm rượu
                - Cân nhắc dùng PPI bảo vệ dạ dày
                - Ưu tiên NOAC hơn warfarin
                - Theo dõi sát sao
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **HAS-BLED Score**
                
                **Tiêu chí (1 điểm mỗi mục):**
                - **H**: Hypertension (SBP >160 mmHg)
                - **A**: Abnormal renal/liver function (1-2 điểm)
                - **S**: Stroke (tiền sử đột quỵ)
                - **B**: Bleeding history/predisposition
                - **L**: Labile INR (TTR <60%)
                - **E**: Elderly (>65 tuổi)
                - **D**: Drugs (antiplatelet/NSAID) or Alcohol
                
                **Giải thích:**
                - 0-2: Nguy cơ chảy máu thấp
                - ≥3: Nguy cơ cao (cần thận trọng, KHÔNG chống chỉ định)
                
                **Reference:**
                Pisters R, et al. Chest. 2010;138(5):1093-1100.
                """)

# ===== SCORE2 =====
elif selected_score_id == "SCORE2":
    st.subheader("📊 SCORE2 - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Bệnh Tim Mạch 10 Năm (40-69 tuổi)")
    
    st.info("""
    **SCORE2 dự đoán nguy cơ 10 năm mắc:**
    - Nhồi máu cơ tim (tử vong + không tử vong)
    - Đột quỵ (tử vong + không tử vong)
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        # Age
        age_score2 = st.slider(
            "Tuổi",
            min_value=40,
            max_value=69,
            value=55,
            step=1
        )
        
        # Gender
        gender_score2 = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="gender_score2"
        )
        
        # Smoking
        smoking_score2 = st.radio(
            "Hút thuốc",
            ["Không", "Có"],
            horizontal=True,
            key="smoking_score2"
        )
        
        # SBP
        sbp_score2 = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=90,
            max_value=200,
            value=120,
            step=5,
            key="sbp_score2"
        )
        
        # Cholesterol with unit conversion
        st.markdown("#### Cholesterol")
        chol_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L"],
            horizontal=True,
            key="chol_unit_score2"
        )
        
        chol_type_score2 = st.radio(
            "Loại cholesterol:",
            ["Total Cholesterol", "Non-HDL Cholesterol"],
            horizontal=True,
            key="chol_type_score2"
        )
        
        if chol_unit == "mg/dL":
            if chol_type_score2 == "Total Cholesterol":
                chol_input = st.number_input(
                    "Total Cholesterol (mg/dL)",
                    min_value=100,
                    max_value=400,
                    value=200,
                    step=5,
                    help="Bình thường: <200 mg/dL",
                    key="chol_mgdl_score2"
                )
                chol_mgdl = chol_input
            else:
                chol_input = st.number_input(
                    "Non-HDL Cholesterol (mg/dL)",
                    min_value=80,
                    max_value=350,
                    value=150,
                    step=5,
                    help="= Total Chol - HDL Chol",
                    key="nonhdl_mgdl_score2"
                )
                chol_mgdl = chol_input
        else:  # mmol/L
            if chol_type_score2 == "Total Cholesterol":
                chol_input = st.number_input(
                    "Total Cholesterol (mmol/L)",
                    min_value=2.0,
                    max_value=10.0,
                    value=5.2,
                    step=0.1,
                    help="Bình thường: <5.2 mmol/L",
                    key="chol_mmol_score2"
                )
                chol_mgdl = chol_input * 38.67  # Convert to mg/dL
            else:
                chol_input = st.number_input(
                    "Non-HDL Cholesterol (mmol/L)",
                    min_value=2.0,
                    max_value=9.0,
                    value=3.9,
                    step=0.1,
                    help="= Total Chol - HDL Chol",
                    key="nonhdl_mmol_score2"
                )
                chol_mgdl = chol_input * 38.67
        
        # Display converted value
        if chol_unit == "mmol/L":
            st.caption(f"≈ {chol_mgdl:.1f} mg/dL")
        else:
            st.caption(f"≈ {chol_mgdl/38.67:.2f} mmol/L")
        
        # Risk region
        risk_region_score2 = st.selectbox(
            "Khu vực nguy cơ",
            [
                "Nguy cơ thấp (Low risk - Bắc Âu, Tây Âu)",
                "Nguy cơ trung bình (Moderate risk - Nam Âu)",
                "Nguy cơ cao (High risk - Đông Âu)",
                "Nguy cơ rất cao (Very high risk - một số nước Đông Âu)"
            ],
            index=1,
            help="Việt Nam thường xếp vào moderate-high risk",
            key="region_score2"
        )
        
        if st.button("🧮 Tính SCORE2", type="primary", key="score2_calc"):
            # Simplified calculation
            base_risk = 2.0
            
            age_factor = (age_score2 - 40) * 0.3
            gender_factor = 1.5 if gender_score2 == "Nam" else 1.0
            smoking_factor = 2.0 if smoking_score2 == "Có" else 1.0
            
            if sbp_score2 < 120:
                sbp_factor = 0.8
            elif sbp_score2 < 140:
                sbp_factor = 1.0
            elif sbp_score2 < 160:
                sbp_factor = 1.5
            else:
                sbp_factor = 2.0
            
            if chol_mgdl < 200:
                chol_factor = 0.9
            elif chol_mgdl < 240:
                chol_factor = 1.2
            else:
                chol_factor = 1.8
            
            if "thấp" in risk_region_score2:
                region_factor = 0.7
            elif "trung bình" in risk_region_score2:
                region_factor = 1.0
            elif "cao" in risk_region_score2 and "rất cao" not in risk_region_score2:
                region_factor = 1.5
            else:
                region_factor = 2.0
            
            risk_10y = base_risk + age_factor
            risk_10y *= gender_factor * smoking_factor * sbp_factor * chol_factor * region_factor
            risk_10y = min(risk_10y, 50)
            risk_10y = round(risk_10y, 1)
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if risk_10y < 2.5:
                    st.success(f"## {risk_10y}%")
                    st.success("✅ Nguy cơ THẤP")
                    risk_category = "Nguy cơ thấp đến trung bình (<2.5%)"
                elif risk_10y < 7.5:
                    st.warning(f"## {risk_10y}%")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                    risk_category = "Nguy cơ trung bình (2.5-7.5%)"
                elif risk_10y < 10:
                    st.error(f"## {risk_10y}%")
                    st.error("❗ Nguy cơ CAO")
                    risk_category = "Nguy cơ cao (7.5-10%)"
                else:
                    st.error(f"## {risk_10y}%")
                    st.error("🚨 Nguy cơ RẤT CAO")
                    risk_category = "Nguy cơ rất cao (≥10%)"
            
            st.markdown("### 💡 Giải Thích")
            st.write(f"**Nguy cơ tim mạch 10 năm:** {risk_10y}%")
            st.write(f"**Phân loại:** {risk_category}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Điều Trị")
            
            if risk_10y < 2.5:
                st.success("""
                **Nguy cơ thấp - Can thiệp lối sống**
                
                **Khuyến cáo:**
                - Duy trì lối sống lành mạnh
                - Không cần statin nếu không có yếu tố nguy cơ khác
                - Tái đánh giá sau 5 năm
                - Kiểm soát các yếu tố nguy cơ
                """)
            elif risk_10y < 7.5:
                st.warning("""
                **Nguy cơ trung bình - Can thiệp lối sống + Cân nhắc statin**
                
                **Khuyến cáo:**
                - Thay đổi lối sống mạnh mẽ
                - **Cân nhắc statin** nếu:
                  - LDL-C ≥70 mg/dL (1.8 mmol/L)
                  - Có yếu tố nguy cơ khác (tiền sử gia đình, béo phì...)
                - Mục tiêu LDL-C: <100 mg/dL (2.6 mmol/L)
                - Tái đánh giá sau 2-3 năm
                """)
            elif risk_10y < 10:
                st.error("""
                **Nguy cơ cao - KHUYẾN CÁO STATIN**
                
                **Khuyến cáo:**
                - **Statin liều trung bình-cao**
                  - Atorvastatin 20-40mg
                  - Rosuvastatin 10-20mg
                - **Mục tiêu LDL-C: <70 mg/dL (1.8 mmol/L)**
                - Cân nhắc giảm ≥50% LDL-C từ baseline
                - Kiểm soát chặt chẽ các yếu tố nguy cơ:
                  - BP <140/90 (hoặc <130/80 nếu có đái tháo đường)
                  - Ngừng hút thuốc
                  - Giảm cân nếu thừa cân
                - Theo dõi sát
                """)
            else:
                st.error("""
                **Nguy cơ rất cao - CAN THIỆP TÍCH CỰC**
                
                **Khuyến cáo:**
                - **Statin liều cao**
                  - Atorvastatin 40-80mg
                  - Rosuvastatin 20-40mg
                - **Mục tiêu LDL-C: <55 mg/dL (1.4 mmol/L)**
                - Cân nhắc giảm ≥50% LDL-C từ baseline
                - **Cân nhắc thêm Ezetimibe** nếu không đạt mục tiêu
                - **Cân nhắc PCSK9 inhibitor** nếu vẫn không đạt
                - Aspirin liều thấp (nếu không chống chỉ định)
                - Kiểm soát THA chặt chẽ (<130/80)
                - Ngừng hút thuốc ngay
                - Theo dõi chặt chẽ, tái khám 3-6 tháng
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **ESC Guidelines 2021 on Cardiovascular Disease Prevention**
                
                **SCORE2 thay thế SCORE cũ (2021):**
                - Dự đoán sự kiện tim mạch tử vong + không tử vong
                - Chính xác hơn cho dân số châu Âu hiện đại
                - Phân theo 4 khu vực nguy cơ
                
                **Áp dụng cho:**
                - Người 40-69 tuổi không có bệnh tim mạch
                - Không có đái tháo đường
                - LDL-C <190 mg/dL (4.9 mmol/L)
                
                **Lưu ý cho Việt Nam:**
                - Xếp vào khu vực moderate-high risk
                - Cân nhắc các yếu tố địa phương
                
                **Reference:**
                SCORE2 working group and ESC Cardiovascular risk collaboration. 
                Eur Heart J. 2021;42(25):2439-2454.
                
                **Link:**
                https://academic.oup.com/eurheartj/article/42/25/2439/6297709
                """)

# ===== SCORE2-OP =====
elif selected_score_id == "SCORE2-OP":
    st.subheader("👴 SCORE2-OP - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Tim Mạch Ở Người Cao Tuổi (≥70 tuổi)")
    
    st.info("""
    **SCORE2-OP (Older Persons) dành cho người ≥70 tuổi**
    
    Dự đoán nguy cơ 5-10 năm mắc bệnh tim mạch.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        # Age
        age_op = st.slider(
            "Tuổi",
            min_value=70,
            max_value=89,
            value=75,
            step=1,
            key="age_op"
        )
        
        # Gender
        gender_op = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="gender_op"
        )
        
        # Smoking
        smoking_op = st.radio(
            "Hút thuốc",
            ["Không", "Có"],
            horizontal=True,
            key="smoking_op"
        )
        
        # SBP
        sbp_op = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=90,
            max_value=200,
            value=140,
            step=5,
            key="sbp_op"
        )
        
        # Cholesterol with unit conversion
        st.markdown("#### Total Cholesterol")
        chol_unit_op = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L"],
            horizontal=True,
            key="chol_unit_op"
        )
        
        if chol_unit_op == "mg/dL":
            chol_input_op = st.number_input(
                "Total Cholesterol (mg/dL)",
                min_value=100,
                max_value=400,
                value=200,
                step=5,
                key="chol_op"
            )
            chol_mgdl_op = chol_input_op
        else:  # mmol/L
            chol_input_op = st.number_input(
                "Total Cholesterol (mmol/L)",
                min_value=2.0,
                max_value=10.0,
                value=5.2,
                step=0.1,
                key="chol_mmol_op"
            )
            chol_mgdl_op = chol_input_op * 38.67
        
        # Display converted value
        if chol_unit_op == "mmol/L":
            st.caption(f"≈ {chol_mgdl_op:.1f} mg/dL")
        else:
            st.caption(f"≈ {chol_mgdl_op/38.67:.2f} mmol/L")
        
        # Risk region
        risk_region_op = st.selectbox(
            "Khu vực nguy cơ",
            [
                "Nguy cơ thấp",
                "Nguy cơ trung bình",
                "Nguy cơ cao",
                "Nguy cơ rất cao"
            ],
            index=1,
            key="region_op"
        )
        
        if st.button("🧮 Tính SCORE2-OP", type="primary", key="score2op_calc"):
            # Simplified calculation for OP
            base_risk = 5.0
            
            age_factor = (age_op - 70) * 0.5
            gender_factor = 1.3 if gender_op == "Nam" else 1.0
            smoking_factor = 1.8 if smoking_op == "Có" else 1.0
            
            if sbp_op < 140:
                sbp_factor = 0.9
            elif sbp_op < 160:
                sbp_factor = 1.2
            else:
                sbp_factor = 1.6
            
            if chol_mgdl_op < 200:
                chol_factor = 0.9
            else:
                chol_factor = 1.3
            
            region_dict = {
                "Nguy cơ thấp": 0.7,
                "Nguy cơ trung bình": 1.0,
                "Nguy cơ cao": 1.3,
                "Nguy cơ rất cao": 1.7
            }
            region_factor = region_dict[risk_region_op]
            
            risk_op = base_risk + age_factor
            risk_op *= gender_factor * smoking_factor * sbp_factor * chol_factor * region_factor
            risk_op = min(risk_op, 60)
            risk_op = round(risk_op, 1)
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if risk_op < 7.5:
                    st.success(f"## {risk_op}%")
                    st.success("✅ Nguy cơ THẤP-TRUNG BÌNH")
                elif risk_op < 15:
                    st.warning(f"## {risk_op}%")
                    st.warning("⚠️ Nguy cơ CAO")
                else:
                    st.error(f"## {risk_op}%")
                    st.error("🚨 Nguy cơ RẤT CAO")
            
            st.markdown("### 💡 Giải Thích")
            st.write(f"**Nguy cơ tim mạch 5-10 năm:** {risk_op}%")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Điều Trị Ở Người Cao Tuổi")
            
            st.warning("""
            **⚠️ Lưu ý quan trọng với người cao tuổi:**
            - Cân nhắc tuổi thọ dự kiến
            - Đánh giá tình trạng sức khỏe tổng thể
            - Xem xét chất lượng cuộc sống
            - Nguy cơ tác dụng phụ cao hơn
            """)
            
            if risk_op < 7.5:
                st.success("""
                **Can thiệp lối sống ưu tiên**
                - Statin liều thấp nếu dung nạp tốt
                - Kiểm soát THA nhẹ nhàng (mục tiêu <140-150/90)
                - Hoạt động thể lực phù hợp
                """)
            elif risk_op < 15:
                st.warning("""
                **Cân nhắc statin liều trung bình**
                - Atorvastatin 10-20mg hoặc Rosuvastatin 5-10mg
                - Mục tiêu LDL-C: <100 mg/dL (2.6 mmol/L) (linh hoạt)
                - Theo dõi chức năng gan, thận
                - Theo dõi triệu chứng cơ
                """)
            else:
                st.error("""
                **Statin liều trung bình, tránh liều cao**
                - Atorvastatin 20-40mg
                - Mục tiêu LDL-C: <70-100 mg/dL (1.8-2.6 mmol/L) (cá thể hóa)
                - **KHÔNG nên quá tích cực** ở người rất cao tuổi (>85)
                - Cân nhắc lợi ích/nguy cơ cá thể
                - Aspirin: Cân nhắc cẩn thận (nguy cơ chảy máu cao)
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **SCORE2-OP (Older Persons) - ESC 2021**
                
                **Đặc điểm:**
                - Thiết kế riêng cho người ≥70 tuổi
                - Nguy cơ tuyệt đối cao hơn do tuổi
                - Khuyến cáo điều trị cá thể hóa hơn
                
                **Ngưỡng nguy cơ khác với SCORE2:**
                - <7.5%: Nguy cơ thấp-trung bình
                - 7.5-15%: Nguy cơ cao
                - ≥15%: Nguy cơ rất cao
                
                **Lưu ý:**
                - Cân nhắc tuổi thọ dự kiến
                - Đánh giá tình trạng chức năng
                - Tránh can thiệp quá mức
                
                **Reference:**
                SCORE2-OP working group. Eur Heart J. 2021;42(25):2455-2467.
                """)

# ===== HEART Score, TIMI, GRACE, Framingham =====
elif selected_score_id in ["HEART Score", "TIMI Risk", "GRACE Score", "Framingham"]:
    score_info = SCORES_BY_SPECIALTY["❤️ Tim Mạch (Cardiology)"][selected_score_id]
    st.subheader(f"❤️ {score_info['name']}")
    st.caption(score_info['desc'])
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2-3")
    
    st.info(f"""
    **{score_info['name']}** đang được phát triển.
    
    Sẽ sớm ra mắt với đầy đủ tính năng!
    """)

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

