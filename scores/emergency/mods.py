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
6. Neurologic: Glasgow Coma Scale

Score: 0-4 points per organ → Total: 0-24 points

Clinical Utility:
- Assess multiple organ dysfunction
- Predict ICU mortality
- Monitor disease progression
- Research tool
"""

import streamlit as st


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
    """Cardiovascular score based on PAR (Pressure-Adjusted Heart Rate)
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
    """Neurologic score based on Glasgow Coma Scale"""
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
    
    # Educational information
    with st.expander("ℹ️ Thông Tin & Cách Sử Dụng"):
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
        4. **Tim mạch:** PAR (Pressure-Adjusted Heart Rate)
        5. **Huyết học:** Tiểu cầu
        6. **Thần kinh:** GCS
        
        Mỗi hệ: 0-4 điểm → Tổng: 0-24 điểm
        
        ### 📊 Điểm & Tử Vong
        
        | MODS Score | Tử Vong ICU |
        |------------|-------------|
        | 0 | <5% |
        | 1-4 | 5-10% |
        | 5-8 | 10-25% |
        | 9-12 | 25-50% |
        | >12 | >50% |
        
        ### 🔍 So Sánh với SOFA
        
        **MODS vs SOFA:**
        - MODS đơn giản hơn (không cần vasopressor dose)
        - SOFA phổ biến hơn (Sepsis-3)
        - Cả hai đều đánh giá 6 hệ cơ quan
        
        ### 📚 Tham Khảo
        
        - Marshall JC, et al. *Crit Care Med* 1995;23:1638-1652
        """)
    
    st.divider()
    
    st.subheader("📝 Nhập Thông Số 6 Hệ Cơ Quan")
    
    # Respiratory
    st.markdown("#### 1️⃣ Hô Hấp")
    col1, col2 = st.columns(2)
    with col1:
        pao2 = st.number_input("PaO₂ (mmHg)", 0.0, 700.0, 100.0, 1.0)
    with col2:
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0)
    
    pao2_fio2 = (pao2 / fio2) * 100 if fio2 > 0 else 0
    st.caption(f"💡 PaO₂/FiO₂ = {pao2_fio2:.0f} mmHg")
    
    st.divider()
    
    # Renal
    st.markdown("#### 2️⃣ Thận")
    creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1)
    st.caption("💡 μmol/L ÷ 88.4 = mg/dL")
    
    st.divider()
    
    # Hepatic
    st.markdown("#### 3️⃣ Gan")
    bilirubin = st.number_input("Bilirubin (mg/dL)", 0.0, 30.0, 1.0, 0.1)
    st.caption("💡 μmol/L ÷ 17.1 = mg/dL")
    
    st.divider()
    
    # Cardiovascular
    st.markdown("#### 4️⃣ Tim Mạch")
    col3, col4 = st.columns(2)
    with col3:
        heart_rate = st.number_input("Nhịp tim (/min)", 0.0, 250.0, 80.0, 1.0)
    with col4:
        map_value = st.number_input("MAP (mmHg)", 0.0, 200.0, 70.0, 1.0)
        st.caption("MAP = (SBP + 2×DBP)/3")
    
    st.divider()
    
    # Hematologic
    st.markdown("#### 5️⃣ Huyết Học")
    platelets = st.number_input("Tiểu cầu (×10³/μL)", 0.0, 500.0, 200.0, 1.0)
    
    st.divider()
    
    # Neurologic
    st.markdown("#### 6️⃣ Thần Kinh")
    gcs = st.number_input("GCS (Glasgow Coma Scale)", 3, 15, 15, 1)
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
        st.subheader("📊 Kết Quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric("**MODS Score**", f"{result['total_score']} điểm")
            st.caption("0-24 điểm")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['interpretation']}")
            st.markdown(f"**Tử vong ước tính: {result['mortality']}**")
        
        # Subscores
        with st.expander("📋 Điểm Từng Hệ Cơ Quan", expanded=True):
            cols = st.columns(6)
            organs = [
                ("Hô hấp", "respiratory"),
                ("Thận", "renal"),
                ("Gan", "hepatic"),
                ("Tim mạch", "cardiovascular"),
                ("Huyết học", "hematologic"),
                ("Thần kinh", "neurologic")
            ]
            
            for col, (name, key) in zip(cols, organs):
                with col:
                    st.metric(name, f"{result['subscores'][key]}")
            
            st.markdown("---")
            st.markdown("**Chi tiết:**")
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.info("""
        **📌 Diễn Giải MODS:**
        
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
        ⚠️ **Lưu Ý:**
        - MODS là công cụ đánh giá, không phải chẩn đoán
        - Kết hợp với đánh giá lâm sàng
        - Tính lại hàng ngày để theo dõi
        """)
        
        st.session_state['mods_result'] = result
    
    # Quick reference
    with st.expander("📖 Bảng MODS Scoring Chi Tiết"):
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
        
        \* PAR (Pressure-Adjusted Heart Rate) = HR × CVP / MAP  
        Simplified: HR / MAP
        
        ### Ưu Điểm MODS
        
        - Đơn giản, khách quan
        - Không cần liều vasopressor (khác SOFA)
        - Áp dụng rộng rãi
        - Tương quan tốt với mortality
        """)
