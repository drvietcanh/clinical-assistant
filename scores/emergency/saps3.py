"""
SAPS III Score (Simplified Acute Physiology Score III)
======================================================

ICU mortality prediction score - Updated version

Reference:
- Moreno RP, et al. SAPS 3--From evaluation of the patient to evaluation of the intensive care unit. 
  Part 1: Objectives, methods and cohort description. Intensive Care Med. 2005;31(10):1336-1344.
- Metnitz PG, et al. SAPS 3--From evaluation of the patient to evaluation of the intensive care unit. 
  Part 2: Development of a prognostic model for hospital mortality at ICU admission. 
  Intensive Care Med. 2005;31(10):1345-1355.

SAPS III Components:
- 20 variables (physiological, demographic, admission characteristics)
- More accurate than SAPS II
- Global database (more than 16,000 patients)

Total: 0-217 points (theoretical maximum)

Clinical Utility:
- ICU mortality prediction (more accurate than SAPS II)
- Risk stratification
- Quality improvement
- Research
"""

import streamlit as st
import math
from components.ui.scoring import render_score_result
from components.ui.results import render_result_box, render_result_card


def get_saps3_age_points(age: int) -> float:
    """Age points for SAPS III"""
    if age < 40:
        return 0
    elif age < 50:
        return 7
    elif age < 60:
        return 12
    elif age < 70:
        return 18
    elif age < 80:
        return 24
    else:
        return 30


def get_saps3_sbp_points(sbp: float) -> float:
    """Systolic BP points"""
    if sbp < 70:
        return 15
    elif sbp < 100:
        return 10
    elif sbp < 200:
        return 0
    else:
        return 6


def get_saps3_hr_points(hr: float) -> float:
    """Heart rate points"""
    if hr < 40:
        return 11
    elif hr < 70:
        return 2
    elif hr < 120:
        return 0
    elif hr < 150:
        return 4
    else:
        return 7


def get_saps3_temp_points(temp: float) -> float:
    """Temperature points"""
    if temp < 36:
        return 3
    elif temp < 38.5:
        return 0
    else:
        return 3


def get_saps3_pao2_fio2_points(pao2: float, fio2: float, is_ventilated: bool) -> float:
    """PaO2/FiO2 points"""
    if not is_ventilated:
        return 0
    
    if fio2 == 0:
        return 0
    
    ratio = (pao2 / fio2) * 100
    
    if ratio < 100:
        return 11
    elif ratio < 200:
        return 9
    else:
        return 6


def get_saps3_ph_points(ph: float) -> float:
    """pH points"""
    if ph < 7.15:
        return 12
    elif ph < 7.25:
        return 3
    elif ph < 7.35:
        return 0
    elif ph < 7.45:
        return 0
    elif ph < 7.50:
        return 3
    else:
        return 3


def get_saps3_na_points(na: float) -> float:
    """Sodium points"""
    if na < 125:
        return 5
    elif na < 145:
        return 0
    else:
        return 1


def get_saps3_k_points(k: float) -> float:
    """Potassium points"""
    if k < 3.0:
        return 3
    elif k < 5.0:
        return 0
    else:
        return 3


def get_saps3_wbc_points(wbc: float) -> float:
    """White blood cell count points"""
    if wbc < 1.0:
        return 12
    elif wbc < 20.0:
        return 0
    else:
        return 3


def get_saps3_bilirubin_points(bilirubin: float) -> float:
    """Bilirubin points (mg/dL)"""
    if bilirubin < 2.0:
        return 0
    elif bilirubin < 6.0:
        return 4
    else:
        return 9


def calculate_saps3(params: dict) -> dict:
    """
    Calculate SAPS III score
    
    Args:
        params: Dictionary with patient parameters
        
    Returns:
        Dictionary with score and interpretation
    """
    total_score = 0.0
    details = []
    
    # Age
    age_points = get_saps3_age_points(params['age'])
    total_score += age_points
    details.append(f"Tuổi {params['age']} → {age_points:.0f} điểm")
    
    # SBP
    sbp_points = get_saps3_sbp_points(params['sbp'])
    total_score += sbp_points
    details.append(f"SBP {params['sbp']:.0f} mmHg → {sbp_points:.0f} điểm")
    
    # Heart rate
    hr_points = get_saps3_hr_points(params['hr'])
    total_score += hr_points
    details.append(f"Nhịp tim {params['hr']:.0f} /min → {hr_points:.0f} điểm")
    
    # Temperature
    temp_points = get_saps3_temp_points(params['temp'])
    total_score += temp_points
    details.append(f"Nhiệt độ {params['temp']:.1f}°C → {temp_points:.0f} điểm")
    
    # PaO2/FiO2 (if ventilated)
    if params.get('is_ventilated', False):
        pao2_fio2_points = get_saps3_pao2_fio2_points(
            params['pao2'], params['fio2'], params['is_ventilated']
        )
        total_score += pao2_fio2_points
        ratio = (params['pao2'] / params['fio2']) * 100 if params['fio2'] > 0 else 0
        details.append(f"PaO2/FiO2 {ratio:.0f} → {pao2_fio2_points:.0f} điểm")
    
    # pH
    ph_points = get_saps3_ph_points(params['ph'])
    total_score += ph_points
    details.append(f"pH {params['ph']:.2f} → {ph_points:.0f} điểm")
    
    # Sodium
    na_points = get_saps3_na_points(params['na'])
    total_score += na_points
    details.append(f"Na {params['na']:.0f} mEq/L → {na_points:.0f} điểm")
    
    # Potassium
    k_points = get_saps3_k_points(params['k'])
    total_score += k_points
    details.append(f"K {params['k']:.1f} mEq/L → {k_points:.0f} điểm")
    
    # WBC
    wbc_points = get_saps3_wbc_points(params['wbc'])
    total_score += wbc_points
    details.append(f"WBC {params['wbc']:.1f} ×10³/µL → {wbc_points:.0f} điểm")
    
    # Bilirubin
    bilirubin_points = get_saps3_bilirubin_points(params['bilirubin'])
    total_score += bilirubin_points
    details.append(f"Bilirubin {params['bilirubin']:.1f} mg/dL → {bilirubin_points:.0f} điểm")
    
    # Calculate predicted mortality using SAPS III formula
    # Logit = -32.6659 + (ln(SAPS III + 1) × 7.3068)
    logit = -32.6659 + (math.log(total_score + 1) * 7.3068)
    predicted_mortality = (math.exp(logit) / (1 + math.exp(logit))) * 100
    
    # Interpretation
    if predicted_mortality < 10:
        interpretation = "Nguy cơ tử vong thấp"
        color = "success"
        severity = "Thấp"
    elif predicted_mortality < 30:
        interpretation = "Nguy cơ tử vong trung bình"
        color = "warning"
        severity = "Trung bình"
    else:
        interpretation = "Nguy cơ tử vong cao"
        color = "error"
        severity = "Cao"
    
    return {
        "total_score": round(total_score, 1),
        "predicted_mortality": round(predicted_mortality, 1),
        "interpretation": interpretation,
        "color": color,
        "severity": severity,
        "details": details
    }


def render():
    """SAPS III Score Calculator"""
    st.subheader("🚨 SAPS III - Simplified Acute Physiology Score III")
    st.caption("Dự đoán tử vong ICU - Phiên bản cập nhật (chính xác hơn SAPS II)")
    
    st.markdown("""
    **SAPS III** là phiên bản cập nhật của SAPS II, chính xác hơn trong dự đoán tử vong ICU.
    
    **Đặc điểm:**
    - 20 biến số (sinh lý, nhân khẩu học, đặc điểm nhập viện)
    - Database toàn cầu (>16,000 bệnh nhân)
    - Công thức dự đoán tử vong chính xác hơn SAPS II
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📝 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm):",
            min_value=0,
            max_value=120,
            value=60,
            step=1,
            key="saps3_age"
        )
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=0.0,
            max_value=300.0,
            value=120.0,
            step=1.0,
            key="saps3_sbp"
        )
        
        hr = st.number_input(
            "Nhịp tim (/phút):",
            min_value=0.0,
            max_value=250.0,
            value=80.0,
            step=1.0,
            key="saps3_hr"
        )
        
        temp = st.number_input(
            "Nhiệt độ (°C):",
            min_value=30.0,
            max_value=45.0,
            value=37.0,
            step=0.1,
            key="saps3_temp"
        )
    
    with col2:
        ph = st.number_input(
            "pH (động mạch):",
            min_value=6.5,
            max_value=8.0,
            value=7.40,
            step=0.01,
            key="saps3_ph"
        )
        
        na = st.number_input(
            "Na (mEq/L):",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            key="saps3_na"
        )
        
        k = st.number_input(
            "K (mEq/L):",
            min_value=1.0,
            max_value=10.0,
            value=4.0,
            step=0.1,
            key="saps3_k"
        )
        
        wbc = st.number_input(
            "WBC (×10³/µL):",
            min_value=0.0,
            max_value=100.0,
            value=7.0,
            step=0.1,
            key="saps3_wbc"
        )
    
    # Ventilation status
    is_ventilated = st.checkbox(
        "Đang thở máy hoặc CPAP",
        key="saps3_ventilated"
    )
    
    if is_ventilated:
        col3, col4 = st.columns(2)
        with col3:
            pao2 = st.number_input(
                "PaO₂ (mmHg):",
                min_value=0.0,
                max_value=600.0,
                value=100.0,
                step=1.0,
                key="saps3_pao2"
            )
        with col4:
            fio2 = st.number_input(
                "FiO₂ (0.21-1.0):",
                min_value=0.21,
                max_value=1.0,
                value=0.4,
                step=0.01,
                key="saps3_fio2"
            )
    else:
        pao2 = 0
        fio2 = 0.21
    
    bilirubin = st.number_input(
        "Bilirubin (mg/dL):",
        min_value=0.0,
        max_value=50.0,
        value=1.0,
        step=0.1,
        key="saps3_bilirubin"
    )
    
    st.markdown("---")
    
    if st.button("🧮 Tính SAPS III", type="primary", use_container_width=True):
        params = {
            'age': age,
            'sbp': sbp,
            'hr': hr,
            'temp': temp,
            'ph': ph,
            'na': na,
            'k': k,
            'wbc': wbc,
            'bilirubin': bilirubin,
            'is_ventilated': is_ventilated,
            'pao2': pao2,
            'fio2': fio2
        }
        
        result = calculate_saps3(params)
        
        # Display results
        st.markdown("### 📊 Kết quả")
        
        render_result_box(
            "SAPS III Score",
            f"{result['total_score']:.1f} điểm",
            subtitle=f"Dự đoán tử vong: {result['predicted_mortality']:.1f}%",
            color=result['color'],
            icon="📊"
        )
        
        st.markdown(f"**Đánh giá:** {result['interpretation']}")
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        for detail in result['details']:
            st.markdown(f"- {detail}")
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến nghị")
        
        if result['severity'] == "Cao":
            st.error("""
            **🚨 Nguy cơ tử vong cao:**
            - Điều trị tích cực
            - Theo dõi sát
            - Hội chẩn chuyên khoa
            - Thảo luận với gia đình về tiên lượng
            """)
        elif result['severity'] == "Trung bình":
            st.warning("""
            **⚠️ Nguy cơ tử vong trung bình:**
            - Điều trị chuẩn
            - Theo dõi định kỳ
            - Đánh giá lại thường xuyên
            """)
        else:
            st.success("""
            **✅ Nguy cơ tử vong thấp:**
            - Điều trị chuẩn
            - Theo dõi định kỳ
            - Có thể cân nhắc chuyển khoa thường
            """)
        
        st.markdown("---")
        st.info("""
        **💡 Lưu ý:**
        - SAPS III chính xác hơn SAPS II trong dự đoán tử vong
        - Kết hợp với đánh giá lâm sàng để quyết định điều trị
        - Đánh giá lại thường xuyên khi tình trạng thay đổi
        """)
    
    st.markdown("---")
    
    with st.expander("📖 Thông tin về SAPS III"):
        st.markdown("""
        **SAPS III (Simplified Acute Physiology Score III)** là phiên bản cập nhật của SAPS II.
        
        **Cải tiến so với SAPS II:**
        - Chính xác hơn trong dự đoán tử vong
        - Database toàn cầu lớn hơn
        - Bao gồm thêm các yếu tố nhân khẩu học và đặc điểm nhập viện
        
        **Công thức dự đoán tử vong:**
        - Logit = -32.6659 + (ln(SAPS III + 1) × 7.3068)
        - Predicted Mortality = e^Logit / (1 + e^Logit) × 100
        
        **Tài liệu tham khảo:**
        - Moreno RP, et al. SAPS 3--From evaluation of the patient to evaluation of the intensive care unit. 
          Part 1: Objectives, methods and cohort description. Intensive Care Med. 2005;31(10):1336-1344.
        - Metnitz PG, et al. SAPS 3--From evaluation of the patient to evaluation of the intensive care unit. 
          Part 2: Development of a prognostic model for hospital mortality at ICU admission. 
          Intensive Care Med. 2005;31(10):1345-1355.
        """)
    
    st.caption("⚠️ SAPS III chỉ là công cụ hỗ trợ. Đánh giá lâm sàng toàn diện vẫn là quan trọng nhất.")

