"""
Dyslipidemia Management Protocol
ESC/EAS 2019 Guidelines + 2023 Updates (SCORE2)
Management of Dyslipidemias for CVD Prevention
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section

def render():
    """Dyslipidemia Management Protocol (ESC/EAS 2019 + 2023 Update)"""
    st.subheader("🩸 Dyslipidemia Management")
    st.caption("ESC/EAS 2019 Guidelines + 2023 Updates (SCORE2 Risk Stratification)")
    
    st.info("""
    **Cập nhật quan trọng:**
    - **Mục tiêu LDL-C:** Càng thấp càng tốt (Low is better).
    - **Nguy cơ rất cao:** LDL-C < 55 mg/dL (< 1.4 mmol/L) & giảm > 50% so với nền.
    - **Nguy cơ cao:** LDL-C < 70 mg/dL (< 1.8 mmol/L) & giảm > 50% so với nền.
    - **Sàng lọc Lp(a):** Ít nhất 1 lần trong đời (ESC 2023).
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CARDIOVASCULAR RISK ASSESSMENT ==========
    st.markdown("### 1️⃣ Đánh giá Nguy cơ Tim mạch (CV Risk)")
    
    risk_category = st.radio(
        "**Phân tầng nguy cơ:**",
        [
            "Very High Risk (Nguy cơ rất cao)",
            "High Risk (Nguy cơ cao)",
            "Moderate Risk (Nguy cơ trung bình)",
            "Low Risk (Nguy cơ thấp)"
        ],
        key="dyslipidemia_risk"
    )
    
    if "Very High" in risk_category:
        st.error("""
        **Very High Risk (Nguy cơ rất cao) bao gồm:**
        - Tiền sử **ASCVD** (ACS, Stable Angina, Stroke/TIA, PAD).
        - **Đái tháo đường** có tổn thương cơ quan đích HOẶC ≥3 yếu tố nguy cơ.
        - **CKD nặng** (eGFR < 30).
        - **FH** (Familial Hypercholesterolemia) + ASCVD hoặc 1 yếu tố nguy cơ chính.
        - **SCORE2** ≥ 7.5% (dưới 50 tuổi) hoặc ≥ 10% (50-69 tuổi).
        
        🎯 **Mục tiêu LDL-C:** < 55 mg/dL (< 1.4 mmol/L)
        """)
        target_ldl = 55
        
    elif "High Risk" in risk_category:
        st.warning("""
        **High Risk (Nguy cơ cao) bao gồm:**
        - **Đái tháo đường** không tổn thương cơ quan đích (bệnh kéo dài ≥10 năm).
        - **CKD trung bình** (eGFR 30-59).
        - **FH** đơn thuần.
        - Một yếu tố nguy cơ rất cao (TC > 310, LDL > 190, BP > 180/110).
        - **SCORE2** 2.5-7.5%.
        
        🎯 **Mục tiêu LDL-C:** < 70 mg/dL (< 1.8 mmol/L)
        """)
        target_ldl = 70
        
    elif "Moderate Risk" in risk_category:
        st.info("""
        **Moderate Risk (Nguy cơ trung bình) bao gồm:**
        - **Đái tháo đường** trẻ (<10 năm type 1 hoặc <50 tuổi).
        - **SCORE2** 1-2.5% (dưới 50 tuổi).
        
        🎯 **Mục tiêu LDL-C:** < 100 mg/dL (< 2.6 mmol/L)
        """)
        target_ldl = 100
        
    else:
        st.success("""
        **Low Risk (Nguy cơ thấp) bao gồm:**
        - **SCORE2** < 1%.
        
        🎯 **Mục tiêu LDL-C:** < 116 mg/dL (< 3.0 mmol/L)
        """)
        target_ldl = 116
    
    st.markdown("---")
    
    # ========== SECTION 2: LDL-C GOAL CALCULATOR ==========
    st.markdown("### 2️⃣ Tính toán điều trị")
    
    current_ldl = st.number_input(
        "**LDL-C hiện tại (mg/dL):**",
        min_value=20,
        max_value=500,
        value=130,
        step=5,
        key="dyslipidemia_current_ldl"
    )
    
    if current_ldl:
        reduction_needed_mg = current_ldl - target_ldl
        reduction_percent = (reduction_needed_mg / current_ldl) * 100
        
        if reduction_needed_mg > 0:
            st.warning(f"Cần giảm: **{reduction_needed_mg} mg/dL** ({reduction_percent:.1f}%)")
            
            # Suggest therapy based on reduction needed
            st.markdown("#### ✅ Khuyến cáo điều trị:")
            
            if reduction_percent < 30:
                st.info("- **Statin cường độ trung bình** (Moderate-intensity Statin)")
                
            elif 30 <= reduction_percent < 50:
                st.warning("- **Statin cường độ cao** (High-intensity Statin)")
                st.write("*Ví dụ: Atorvastatin 40-80mg, Rosuvastatin 20-40mg*")
                
            else: # > 50%
                st.error("- **Statin cường độ cao + Ezetimibe**")
                st.write("*Cần phối hợp thuốc ngay từ đầu hoặc theo dõi sát để thêm thuốc.*")
                
        else:
            st.success("✅ Đã đạt mục tiêu LDL-C!")
            
    st.markdown("---")
    
    # ========== SECTION 3: STEPWISE PHARMACOTHERAPY ==========
    st.markdown("### 3️⃣ Các bước dùng thuốc (Stepwise Approach)")
    
    st.info("""
    **Bước 1: High-Intensity Statin**
    - Atorvastatin 40-80 mg
    - Rosuvastatin 20-40 mg
    - *Đánh giá lại sau 4-6 tuần.*
    
    **Bước 2: Thêm Ezetimibe (nếu chưa đạt mục tiêu)**
    - Ezetimibe 10 mg
    - *Giảm thêm được ~15-20% LDL-C.*
    
    **Bước 3: Thêm PCSK9 Inhibitor (nếu nguy cơ rất cao)**
    - Evolocumab hoặc Alirocumab (SC injection)
    - *Giảm thêm được ~50-60% LDL-C.*
    
    **Lựa chọn thay thế (khi không dung nạp Statin):**
    - Bempedoic acid
    - Ezetimibe đơn độc (hiệu quả thấp)
    - PCSK9i
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: HYPERTRIGLYCERIDEMIA ==========
    st.markdown("### 4️⃣ Tăng Triglyceride")
    
    tg_level = st.number_input(
        "**Triglyceride (mg/dL):**",
        min_value=50,
        max_value=2000,
        value=150,
        step=10,
        key="dyslipidemia_tg"
    )
    
    if tg_level > 500:
        st.error("🚨 **Nguy cơ viêm tụy cấp!**")
        st.write("Cần dùng **Fibrate** (Fenofibrate) ngay. Tránh dùng Gemfibrozil với Statin.")
    elif tg_level > 200:
        st.warning("⚠️ Cân nhắc dùng Fenofibrate hoặc Omega-3 (Icosapent ethyl) nếu LDL đã đạt mục tiêu nhưng TG vẫn cao.")
        
    st.markdown("---")
    
    # ========== REFERENCES ==========
    references = get_references("Dyslipidemia")
    if references:
        render_references_section(references)
    else:
        st.caption("Reference: ESC/EAS 2019 Guidelines for the Management of Dyslipidaemias")
