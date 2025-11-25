"""
Hypomagnesemia Correction Protocol
"""

import streamlit as st


def render():
    """Hypomagnesemia Correction Protocol"""
    
    st.warning("## ⚠️ HYPOMAGNESEMIA CORRECTION PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Severity:**
        
        **Mild (1.5-1.7 mg/dL):**
        - Often asymptomatic
        - Mild weakness
        
        **Moderate (1.0-1.5 mg/dL):**
        - Muscle cramps
        - Weakness
        - Tremor
        
        **Severe (<1.0 mg/dL):**
        - Seizures
        - Tetany
        - Loạn nhịp tim
        - Loạn nhịp tim
        """)
    
    with col2:
        st.error("""
        **⚠️ Important:**
        
        **Hypomagnesemia thường kèm:**
        - Hypokalemia (khó điều chỉnh nếu không bổ sung Mg)
        - Hypocalcemia (khó điều chỉnh nếu không bổ sung Mg)
        
        **⚠️ Luôn kiểm tra:**
        - K⁺, Ca²⁺, PO₄³⁻
        - Điều chỉnh đồng thời nếu cần
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Calculation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_mg = st.number_input(
            "Mg²⁺ hiện tại (mg/dL)",
            min_value=0.5,
            max_value=2.0,
            value=1.2,
            step=0.1,
            format="%.1f",
            key="mg_current"
        )
        
        target_mg = st.number_input(
            "Mục tiêu Mg²⁺ (mg/dL)",
            min_value=1.5,
            max_value=2.5,
            value=2.0,
            step=0.1,
            format="%.1f",
            key="mg_target"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            format="%.0f",
            key="mg_weight"
        )
        
        severity = st.radio(
            "Mức độ:",
            ["Nhẹ (asymptomatic)", "Trung bình (symptomatic)", "Nặng (seizures, loạn nhịp tim)"],
            key="mg_severity"
        )
    
    with col2:
        # Calculate
        mg_deficit = target_mg - current_mg
        # Total body Mg: ~0.3-0.4 mEq/kg (or ~24 mEq total)
        # 1g MgSO4 = 8.12 mEq Mg
        # Deficit (mEq) = (Target - Current) × Weight × 0.3
        mg_deficit_meq = mg_deficit * weight * 0.3  # Approximate
        
        # MgSO4 needed
        # 1g MgSO4 = 8.12 mEq Mg
        mgso4_needed = mg_deficit_meq / 8.12
        
        st.markdown("### 📊 Kết Quả")
        
        st.metric("Mg²⁺ deficit", f"{mg_deficit:.2f} mg/dL")
        st.metric("Mg²⁺ deficit", f"{mg_deficit_meq:.1f} mEq")
        st.metric("MgSO4 needed", f"{mgso4_needed:.1f} g")
        
        # Recommendations
        if "Nặng" in severity:
            st.error("""
            **🚨 SEVERE - IV Replacement:**
            - Loading: 2-4g MgSO4 IV trong 10-15 phút
            - Maintenance: 1-2g/h × 4-6h
            - Sau đó: 0.5-1g/h × 12-24h
            """)
        elif "Trung bình" in severity:
            st.warning("""
            **⚠️ MODERATE:**
            - IV: 1-2g MgSO4 IV trong 1h, lặp lại q6-8h
            - Hoặc PO: 400-800mg q8-12h
            """)
        else:
            st.success("""
            **✅ MILD:**
            - PO: 400-600mg q8-12h
            - Hoặc IV: 1g MgSO4 IV trong 1h
            """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Treatment")
    
    tab1, tab2 = st.tabs(["IV Replacement", "Oral Replacement"])
    
    with tab1:
        st.markdown("#### 💉 IV Magnesium Replacement")
        
        st.error("""
        **Severe (<1.0 mg/dL hoặc symptomatic):**
        
        **Loading dose:**
        - **MgSO4 2-4g IV** trong 10-15 phút
        - Hoặc 25-50 mg/kg (1.8-3.6 mEq/kg)
        - **⚠️ Monitor:** BP, HR, ECG (risk bradycardia, hypotension)
        
        **Maintenance:**
        - **1-2g/h × 4-6h** (8-16 mEq/h)
        - Sau đó: **0.5-1g/h × 12-24h**
        - Tổng: 6-12g trong 24h đầu
        
        **Monitoring:**
        - Mg²⁺ mỗi 4-6h
        - Deep tendon reflexes (mất phản xạ = quá liều)
        - ECG, BP, HR
        - Urine output (risk renal failure nếu quá liều)
        """)
        
        st.warning("""
        **Moderate (1.0-1.5 mg/dL):**
        
        **Option 1:**
        - **1-2g MgSO4 IV** trong 1h
        - Lặp lại q6-8h × 2-3 lần
        
        **Option 2:**
        - **1g MgSO4 IV** trong 1h q8h × 24h
        """)
        
        st.info("""
        **⚠️ Precautions:**
        - **Renal failure:** Giảm liều 50-75%
        - **Monitor reflexes:** Mất phản xạ = quá liều
        - **Antidote:** Calcium gluconate 1g IV (nếu quá liều)
        """)
    
    with tab2:
        st.markdown("#### 💊 Oral Magnesium Replacement")
        
        st.success("""
        **Mild to moderate (≥1.0 mg/dL, asymptomatic/mild symptoms):**
        
        **Options:**
        
        **1. Magnesium Oxide:**
        - 400-800mg PO q8-12h
        - Tác dụng phụ: Tiêu chảy
        
        **2. Magnesium Citrate:**
        - 200-400mg PO q8-12h
        - Dễ hấp thu hơn
        
        **3. Magnesium Gluconate:**
        - 500-1000mg PO q12h
        
        **Duration:**
        - 1-2 tuần
        - Kiểm tra Mg²⁺ sau 1 tuần
        """)
        
        st.warning("""
        **⚠️ Lưu ý:**
        - Tiêu chảy có thể hạn chế hấp thu
        - Cần thời gian để bù đủ
        - Không dùng nếu severe hoặc symptomatic
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Common Causes")
    
    st.warning("""
    **GI Losses:**
    - Diarrhea, vomiting
    - Malabsorption
    - Fistulas
    
    **Renal Losses:**
    - Diuretics (loop, thiazide)
    - Alcoholism
    - Diabetes (osmotic diuresis)
    - Hypercalcemia
    - Medications (aminoglycosides, amphotericin)
    
    **Redistribution:**
    - Hungry bone syndrome
    - Acute pancreatitis
    - Transfusion (citrate chelation)
    
    **Inadequate Intake:**
    - Malnutrition
    - TPN without Mg
    - Alcoholism
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Hypomagnesemia + Hypokalemia:**
    - Khó điều chỉnh K⁺ nếu không bổ sung Mg
    - Bổ sung Mg trước hoặc đồng thời với K⁺
    
    **Hypomagnesemia + Hypocalcemia:**
    - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
    - Bổ sung Mg trước hoặc đồng thời với Ca²⁺
    
    **Renal Failure:**
    - Giảm liều 50-75%
    - Theo dõi sát (risk hypermagnesemia)
    - Tránh dùng nếu CrCl <30
    
    **Pregnancy:**
    - MgSO4 an toàn (dùng trong preeclampsia)
    - Liều tương tự
    """)

