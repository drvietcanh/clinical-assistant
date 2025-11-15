"""
Hypophosphatemia Management Protocol
"""

import streamlit as st


def render():
    """Hypophosphatemia Management Protocol"""
    
    st.warning("## ⚠️ HYPOPHOSPHATEMIA MANAGEMENT PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Severity:**
        
        **Mild (2.0-2.5 mg/dL):**
        - Often asymptomatic
        - Mild weakness
        
        **Moderate (1.0-2.0 mg/dL):**
        - Weakness, fatigue
        - Muscle pain
        - Irritability
        
        **Severe (<1.0 mg/dL):**
        - Rhabdomyolysis
        - Respiratory failure
        - Cardiac dysfunction
        - Hemolysis
        - Seizures, coma
        """)
    
    with col2:
        st.error("""
        **⚠️ Critical Levels:**
        
        **<0.5 mg/dL:**
        - Life-threatening
        - Respiratory failure
        - Cardiac arrest
        - Hemolysis
        
        **⚠️ Risk Groups:**
        - Alcoholism
        - Refeeding syndrome
        - DKA recovery
        - TPN without phosphate
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Calculation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_phos = st.number_input(
            "PO₄³⁻ hiện tại (mg/dL)",
            min_value=0.5,
            max_value=3.0,
            value=1.5,
            step=0.1,
            format="%.1f",
            key="phos_current"
        )
        
        target_phos = st.number_input(
            "Mục tiêu PO₄³⁻ (mg/dL)",
            min_value=2.0,
            max_value=4.5,
            value=3.0,
            step=0.1,
            format="%.1f",
            key="phos_target"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            format="%.0f",
            key="phos_weight"
        )
        
        severity = st.radio(
            "Mức độ:",
            ["Nhẹ (asymptomatic)", "Trung bình (symptomatic)", "Nặng (<1.0 mg/dL)"],
            key="phos_severity"
        )
    
    with col2:
        # Calculate
        phos_deficit = target_phos - current_phos
        # Phosphate deficit (mmol) = (Target - Current) × Weight × 0.3
        # 1 mmol PO4 = 31 mg PO4
        # 1 mmol KPO4 = 1 mmol PO4 + 1 mmol K
        phos_deficit_mmol = phos_deficit * weight * 0.3 / 31  # Approximate
        
        # Potassium phosphate: 1 mmol = 31 mg PO4
        # Sodium phosphate: 1 mmol = 31 mg PO4
        # Need: phos_deficit_mmol mmol
        
        st.markdown("### 📊 Kết Quả:")
        
        st.metric("PO₄³⁻ deficit", f"{phos_deficit:.2f} mg/dL")
        st.metric("PO₄³⁻ deficit", f"{phos_deficit_mmol:.1f} mmol")
        
        # Recommendations
        if "Nặng" in severity or current_phos < 1.0:
            st.error("""
            **🚨 SEVERE - IV Replacement:**
            - 0.08-0.16 mmol/kg IV trong 2-6h
            - Hoặc 15-30 mmol IV trong 2-6h
            - Lặp lại q6-12h nếu cần
            """)
        elif "Trung bình" in severity:
            st.warning("""
            **⚠️ MODERATE:**
            - IV: 0.08 mmol/kg IV trong 2-4h
            - Hoặc 15-20 mmol IV trong 2-4h
            - Hoặc PO: 250-500mg q6-8h
            """)
        else:
            st.success("""
            **✅ MILD:**
            - PO: 250-500mg q8-12h
            - Hoặc IV: 10-15 mmol trong 2-4h
            """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Treatment")
    
    tab1, tab2 = st.tabs(["IV Replacement", "Oral Replacement"])
    
    with tab1:
        st.markdown("#### 💉 IV Phosphate Replacement")
        
        st.error("""
        **Severe (<1.0 mg/dL hoặc symptomatic):**
        
        **Dosing:**
        - **0.08-0.16 mmol/kg IV** trong 2-6h
        - Hoặc **15-30 mmol IV** trong 2-6h
        - **Max:** 0.25 mmol/kg trong 6h
        
        **Repeat:**
        - Lặp lại q6-12h nếu cần
        - Kiểm tra PO₄³⁻ sau mỗi lần truyền
        
        **⚠️ Precautions:**
        - **Risk hypocalcemia:** Theo dõi Ca²⁺
        - **Risk hyperphosphatemia:** Không quá 0.25 mmol/kg
        - **Renal failure:** Giảm liều 50-75%
        - **IV site:** Có thể gây kích ứng (phlebitis)
        """)
        
        st.warning("""
        **Moderate (1.0-2.0 mg/dL):**
        
        **Option 1:**
        - **0.08 mmol/kg IV** trong 2-4h
        - Hoặc **15-20 mmol IV** trong 2-4h
        
        **Option 2:**
        - **10-15 mmol IV** trong 2-4h q12h × 2-3 lần
        """)
        
        st.info("""
        **Formulations:**
        
        **Potassium Phosphate:**
        - 1 ml = 3 mmol PO4 + 4.4 mEq K
        - 15 mmol = 5 ml
        
        **Sodium Phosphate:**
        - 1 ml = 3 mmol PO4 + 4 mEq Na
        - 15 mmol = 5 ml
        
        **⚠️ Chọn dựa trên:**
        - K⁺ level (dùng KPO4 nếu hypokalemia)
        - Na⁺ level (dùng NaPO4 nếu hyponatremia)
        - Volume status
        """)
    
    with tab2:
        st.markdown("#### 💊 Oral Phosphate Replacement")
        
        st.success("""
        **Mild to moderate (≥1.0 mg/dL, asymptomatic/mild symptoms):**
        
        **Options:**
        
        **1. Sodium Phosphate:**
        - 250-500mg PO q6-8h
        - Tác dụng phụ: Tiêu chảy
        
        **2. Potassium Phosphate:**
        - 250-500mg PO q6-8h
        - Nếu có hypokalemia
        
        **3. Neutra-Phos:**
        - 250mg PO q6-8h
        - Balanced Na/K
        
        **Duration:**
        - 1-2 tuần
        - Kiểm tra PO₄³⁻ sau 3-5 ngày
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
    **Refeeding Syndrome:**
    - Sau nhịn đói lâu
    - TPN/enteral nutrition
    - ⚠️ Cần bổ sung PO4 sớm
    
    **Alcoholism:**
    - Malnutrition
    - Renal losses
    
    **DKA Recovery:**
    - Insulin đưa PO4 vào tế bào
    - ⚠️ Theo dõi sát khi điều trị DKA
    
    **GI Losses:**
    - Diarrhea, vomiting
    - Malabsorption
    
    **Renal Losses:**
    - Hyperparathyroidism
    - Fanconi syndrome
    - Medications (diuretics)
    
    **Redistribution:**
    - Respiratory alkalosis
    - Hungry bone syndrome
    - Sepsis
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Refeeding Syndrome:**
    - Bổ sung PO4 ngay khi bắt đầu nutrition
    - 15-30 mmol/ngày × 3-5 ngày
    - Theo dõi sát PO4, K⁺, Mg²⁺, Ca²⁺
    
    **DKA Recovery:**
    - Bổ sung PO4 khi K⁺ <4.0
    - 15-30 mmol trong 2-4h
    - Theo dõi sát
    
    **Renal Failure:**
    - Giảm liều 50-75%
    - Theo dõi sát (risk hyperphosphatemia)
    - Tránh dùng nếu CrCl <30
    
    **Hypocalcemia:**
    - Bổ sung PO4 có thể làm giảm Ca²⁺
    - Điều chỉnh Ca²⁺ trước hoặc đồng thời
    """)

