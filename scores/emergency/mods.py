"""
MODS Score (Multiple Organ Dysfunction Score)
==============================================

Quantifies organ dysfunction in ICU patients

Reference:
- Marshall JC, et al. Multiple organ dysfunction score: a reliable descriptor of a
  complex clinical outcome. Crit Care Med. 1995;23(10):1638-1652.

MODS Components (6 organ systems):
1. Respiratory: PaO₂/FiO₂ ratio
2. Renal: Serum creatinine
3. Hepatic: Serum bilirubin
4. Cardiovascular: Pressure-adjusted heart rate (PAR)
5. Hematologic: Platelet count
6. Neurologic: Thang điểm hôn mê Glasgow

Score: 0-4 points per organ → Total: 0-24 points

Clinical Utility:
- Assess multiple organ dysfunction
- Predict ICU mortality
- Monitor disease progression
- Research tool
"""

import streamlit as st
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_heart_rate,
    validate_lab_value,
    safe_divide
)
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def get_respiratory_score(pao2_fio2: float) -> int:
    """Respiratory score based on PaO2/FiO2 ratio"""
    if pao2_fio2 > 300:
        return 0
    elif pao2_fio2 > 226:
        return 1
    elif pao2_fio2 > 151:
        return 2
    elif pao2_fio2 > 76:
        return 3
    else:
        return 4


def get_renal_score(creatinine: float) -> int:
    """Renal score based on serum creatinine"""
    if creatinine <= 1.1:
        return 0
    elif creatinine <= 1.7:
        return 1
    elif creatinine <= 2.5:
        return 2
    elif creatinine <= 3.6:
        return 3
    else:
        return 4


def get_hepatic_score(bilirubin: float) -> int:
    """Hepatic score based on serum bilirubin"""
    if bilirubin <= 1.2:
        return 0
    elif bilirubin <= 3.5:
        return 1
    elif bilirubin <= 7.1:
        return 2
    elif bilirubin <= 10.6:
        return 3
    else:
        return 4


def get_cardiovascular_score(hr: float, map_val: float) -> int:
    """Cardiovascular score based on PAR (Pressure-Adjusted Nhịp tim)
    PAR = HR × CVP / MAP (simplified: HR / MAP when CVP not available)
    Using simplified version: HR × (Right Atrial Pressure / MAP)
    Even more simplified: Just use HR and MAP relationship
    """
    # Simplified PAR calculation
    if map_val > 0:
        par = hr / map_val
    else:
        par = 10  # Default high value
    
    if par <= 10.0:
        return 0
    elif par <= 15.0:
        return 1
    elif par <= 20.0:
        return 2
    elif par <= 30.0:
        return 3
    else:
        return 4


def get_hematologic_score(platelets: float) -> int:
    """Hematologic score based on platelet count"""
    if platelets > 120:
        return 0
    elif platelets > 80:
        return 1
    elif platelets > 50:
        return 2
    elif platelets > 20:
        return 3
    else:
        return 4


def get_neurologic_score(gcs: int) -> int:
    """Neurologic score based on Thang điểm hôn mê Glasgow"""
    if gcs >= 15:
        return 0
    elif gcs >= 13:
        return 1
    elif gcs >= 10:
        return 2
    elif gcs >= 7:
        return 3
    else:
        return 4


def calculate_mods(
    pao2: float,
    fio2: float,
    creatinine: float,
    bilirubin: float,
    heart_rate: float,
    map_value: float,
    platelets: float,
    gcs: int
) -> dict:
    """Calculate MODS score"""
    
    # Calculate PaO2/FiO2 ratio
    pao2_fio2 = (pao2 / fio2) * 100 if fio2 > 0 else 500
    
    # Calculate subscores
    subscores = {}
    details = []
    
    resp_score = get_respiratory_score(pao2_fio2)
    subscores['respiratory'] = resp_score
    details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → {resp_score} điểm")
    
    renal_score = get_renal_score(creatinine)
    subscores['renal'] = renal_score
    details.append(f"**Thận:** Creatinine = {creatinine:.1f} mg/dL → {renal_score} điểm")
    
    hepatic_score = get_hepatic_score(bilirubin)
    subscores['hepatic'] = hepatic_score
    details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} mg/dL → {hepatic_score} điểm")
    
    cv_score = get_cardiovascular_score(heart_rate, map_value)
    subscores['cardiovascular'] = cv_score
    par = heart_rate / map_value if map_value > 0 else 0
    details.append(f"**Tim mạch:** HR/MAP = {par:.1f} → {cv_score} điểm")
    
    hematologic_score = get_hematologic_score(platelets)
    subscores['hematologic'] = hematologic_score
    details.append(f"**Huyết học:** Tiểu cầu = {platelets:.0f} → {hematologic_score} điểm")
    
    neurologic_score = get_neurologic_score(gcs)
    subscores['neurologic'] = neurologic_score
    details.append(f"**Thần kinh:** GCS = {gcs} → {neurologic_score} điểm")
    
    # Total score
    total_score = sum(subscores.values())
    
    # Interpretation (based on original Marshall study)
    if total_score == 0:
        interpretation = "Không có rối loạn cơ quan"
        mortality = "<5%"
        risk_class = "NONE"
        color = "🟢"
    elif total_score <= 4:
        interpretation = "Rối loạn cơ quan nhẹ"
        mortality = "5-10%"
        risk_class = "MILD"
        color = "🟡"
    elif total_score <= 8:
        interpretation = "Rối loạn cơ quan trung bình"
        mortality = "10-25%"
        risk_class = "MODERATE"
        color = "🟡"
    elif total_score <= 12:
        interpretation = "Rối loạn cơ quan nặng"
        mortality = "25-50%"
        risk_class = "SEVERE"
        color = "🟠"
    else:
        interpretation = "Rối loạn cơ quan rất nặng"
        mortality = ">50%"
        risk_class = "CRITICAL"
        color = "🔴"
    
    return {
        'total_score': total_score,
        'subscores': subscores,
        'interpretation': interpretation,
        'mortality': mortality,
        'risk_class': risk_class,
        'color': color,
        'details': details
    }


def render():
    """Render MODS calculator"""
    
    st.title("🏥 MODS Score")
    st.markdown("**Multiple Organ Dysfunction Score - Đánh giá rối loạn đa cơ quan**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mods':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Smart Suggestions (sidebar)
    with st.sidebar:
        render_suggestions(
            calculator_id="mods",
            calculator_name="MODS Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **MODS (Multiple Organ Dysfunction Score)** là thang điểm:
        - Lượng hóa rối loạn đa cơ quan
        - Dự đoán tử vong ICU
        - Theo dõi diễn tiến bệnh
        - Đơn giản, khách quan
        
        ### 🎯 6 Hệ Cơ Quan
        
        1. **Hô hấp:** PaO₂/FiO₂ ratio
        2. **Thận:** Creatinine
        3. **Gan:** Bilirubin
        4. **Tim mạch:** PAR (Pressure-Adjusted Nhịp tim)
        5. **Huyết học:** Tiểu cầu
        6. **Thần kinh:** GCS
        
        Mỗi hệ: 0-4 điểm → Tổng: 0-24 điểm
        
        ### 📊 Điểm & Tử vong
        
        | MODS Score | Tử vong ICU |
        |------------|-------------|
        | 0 | <5% |
        | 1-4 | 5-10% |
        | 5-8 | 10-25% |
        | 9-12 | 25-50% |
        | >12 | >50% |
        
        ### 🔍 So sánh với SOFA
        
        **MODS vs SOFA:**
        - MODS đơn giản hơn (không cần vasopressor dose)
        - SOFA phổ biến hơn (Sepsis-3)
        - Cả hai đều đánh giá 6 hệ cơ quan
        
        ### 📚 Tham khảo
        
        - Marshall JC, et al. *Crit Care Med* 1995;23:1638-1652
        """)
    
    st.divider()
    
    st.subheader("📝 Nhập thông số 6 hệ cơ quan")
    
    # Respiratory
    st.markdown("#### 1️⃣ Hô hấp")
    col1, col2 = st.columns(2)
    with col1:
        pao2 = st.number_input("PaO₂ (mmHg)", 0, 700, 100, 1, format="%d")
    with col2:
        fio2 = st.number_input("FiO₂ (%)", 21, 100, 21, 1, format="%d")
    
    pao2_fio2 = (pao2 / fio2) * 100 if fio2 > 0 else 0
    st.caption(f"💡 PaO₂/FiO₂ = {pao2_fio2:.0f} mmHg")
    
    st.divider()
    
    # Renal
    st.markdown("#### 2️⃣ Thận")
    creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f")
    st.caption("💡 μmol/L ÷ 88.4 = mg/dL")
    
    st.divider()
    
    # Hepatic
    st.markdown("#### 3️⃣ Gan")
    bilirubin = st.number_input("Bilirubin (mg/dL)", 0.0, 30.0, 1.0, 0.1, format="%.1f")
    st.caption("💡 μmol/L ÷ 17.1 = mg/dL")
    
    st.divider()
    
    # Cardiovascular
    st.markdown("#### 4️⃣ Tim mạch")
    col3, col4 = st.columns(2)
    with col3:
        heart_rate = st.number_input("Nhịp tim (/min)", 0, 250, 80, 1, format="%d")
    with col4:
        map_value = st.number_input("MAP (mmHg)", 0, 200, 70, 1, format="%d")
        st.caption("MAP = (SBP + 2×DBP)/3")
    
    st.divider()
    
    # Hematologic
    st.markdown("#### 5️⃣ Huyết học")
    platelets = st.number_input("Tiểu cầu (×10³/μL)", 0, 500, 200, 1, format="%d")
    
    st.divider()
    
    # Neurologic
    st.markdown("#### 6️⃣ Thần kinh")
    gcs = st.number_input("GCS (Thang điểm hôn mê Glasgow) - Thang điểm hôn mê Glasgow", 3, 15, 15, 1, format="%d")
    st.caption("3 (tệ nhất) → 15 (bình thường)")
    
    st.divider()
    
    # Calculate
    if st.button("🧮 Tính MODS Score", type="primary", use_container_width=True):
        result = calculate_mods(
            pao2=pao2,
            fio2=fio2,
            creatinine=creatinine,
            bilirubin=bilirubin,
            heart_rate=heart_rate,
            map_value=map_value,
            platelets=platelets,
            gcs=gcs
        )
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Map color emoji to hex
        color_map_hex = {
            "🟢": "#28a745",
            "🟡": "#ffc107",
            "🟠": "#fd7e14",
            "🔴": "#dc3545"
        }
        score_color = color_map_hex.get(result['color'], "#6c757d")
        
        # Use render_score_result for main score display
        render_score_result(
            title="MODS Score",
            score=result['total_score'],
            interpretation=result['interpretation'],
            mortality=f"Tử vong ICU: {result['mortality']}",
            color=score_color,
            icon=result['color'],
            size="large"
        )
        
        # Use render_score_breakdown for organ system scores
        render_score_breakdown(
            title="Điểm Từng Hệ Cơ Quan",
            subscores={
                "🫁 Hô hấp": result['subscores']['respiratory'],
                "🫘 Thận": result['subscores']['renal'],
                "🫀 Gan": result['subscores']['hepatic'],
                "❤️ Tim mạch": result['subscores']['cardiovascular'],
                "🩸 Huyết học": result['subscores']['hematologic'],
                "🧠 Thần kinh": result['subscores']['neurologic']
            },
            total_score=result['total_score']
        )
        
        # Details
        with st.expander("📋 Chi tiết tính điểm", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.info("""
        **📌 Diễn giải MODS:**
        
        - MODS tăng dần → tiên lượng xấu
        - MODS giảm → đáp ứng điều trị tốt
        - Tính hàng ngày để theo dõi diễn tiến
        - Đơn giản hơn SOFA (không cần vasopressor dose)
        """)
        
        if result['total_score'] >= 9:
            st.error("""
            **🚨 MODS SCORE CAO:**
            
            - Rối loạn đa cơ quan NẶNG
            - Nguy cơ tử vong >25%
            - Cần hồi sức tích cực
            - Xem xét mức độ chăm sóc và tiên lượng
            """)
        
        st.warning("""
        ⚠️ **Lưu ý:**
        - MODS là công cụ đánh giá, không phải chẩn đoán
        - Kết hợp với đánh giá lâm sàng
        - Tính lại hàng ngày để theo dõi
        """)
        
        # Prepare inputs for history and share
        inputs_dict = {
            "PaO₂": f"{pao2} mmHg",
            "FiO₂": f"{fio2}%",
            "Creatinine": f"{creatinine:.1f} mg/dL",
            "Bilirubin": f"{bilirubin:.1f} mg/dL",
            "Heart Rate": f"{heart_rate} /min",
            "MAP": f"{map_value} mmHg",
            "Platelets": f"{platelets} ×10³/μL",
            "GCS": f"{gcs}"
        }
        
        results_dict = {
            "MODS Score": f"{result['total_score']} điểm",
            "Interpretation": result['interpretation'],
            "Mortality": result['mortality'],
            "Risk Class": result['risk_class'],
            "Subscores": result['subscores']
        }
        
        # Save to history
        # Export section
        render_export_section(
                title="MODS Score",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="MODS Score"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mods",
            calculator_name="MODS Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="mods",
            calculator_name="MODS Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="mods", show_actions=True)
        
        st.session_state['mods_result'] = result
    
    # Quick reference
    with st.expander("📖 Bảng MODS Scoring Chi tiết"):
        st.markdown("""
        ### MODS Scoring Table
        
        | Hệ Cơ Quan | 0 | 1 | 2 | 3 | 4 |
        |------------|---|---|---|---|---|
        | **Hô hấp** PaO₂/FiO₂ | >300 | 226-300 | 151-225 | 76-150 | ≤75 |
        | **Thận** Creatinine (mg/dL) | ≤1.1 | 1.2-1.7 | 1.8-2.5 | 2.6-3.6 | >3.6 |
        | **Gan** Bilirubin (mg/dL) | ≤1.2 | 1.3-3.5 | 3.6-7.1 | 7.2-10.6 | >10.6 |
        | **Tim mạch** PAR* | ≤10.0 | 10.1-15.0 | 15.1-20.0 | 20.1-30.0 | >30.0 |
        | **Huyết học** Platelets (×10³/μL) | >120 | 81-120 | 51-80 | 21-50 | ≤20 |
        | **Thần kinh** GCS | 15 | 13-14 | 10-12 | 7-9 | ≤6 |
        
        * PAR (Pressure-Adjusted Nhịp tim) = HR × CVP / MAP  
        Simplified: HR / MAP
        
        ### Ưu Điểm MODS
        
        - Đơn giản, khách quan
        - Không cần liều vasopressor (khác SOFA)
        - Áp dụng rộng rãi
        - Tương quan tốt với mortality
        """)
    
    # References section
    references = get_references("MODS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
