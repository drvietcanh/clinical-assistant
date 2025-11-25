"""
Hypocalcemia Emergency Protocol
"""

import streamlit as st


def render():
    """Hypocalcemia Emergency Protocol"""
    
    st.error("## 🚨 HYPOCALCEMIA EMERGENCY PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Severity (Total Ca):**
        
        **Mild (8.0-8.5 mg/dL):**
        - Often asymptomatic
        - Mild paresthesias
        
        **Moderate (7.0-8.0 mg/dL):**
        - Paresthesias (fingers, toes, lips)
        - Muscle cramps
        - Chvostek sign, Trousseau sign
        
        **Severe (<7.0 mg/dL):**
        - Tetany
        - Seizures
        - Laryngospasm
        - Loạn nhịp tim
        - Prolonged QT
        """)
    
    with col2:
        st.error("""
        **⚠️ Ionized Ca (iCa) - More Important:**
        
        **Normal:** 4.5-5.3 mg/dL (1.1-1.3 mmol/L)
        
        **Mild:** 4.0-4.5 mg/dL
        **Moderate:** 3.5-4.0 mg/dL
        **Severe:** <3.5 mg/dL
        
        **⚠️ Check iCa nếu:**
        - Albumin thấp
        - pH bất thường
        - Critical illness
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Correction for Albumin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_ca = st.number_input(
            "Total Ca hiện tại (mg/dL)",
            min_value=5.0,
            max_value=12.0,
            value=7.5,
            step=0.1,
            format="%.1f",
            key="ca_total"
        )
        
        albumin = st.number_input(
            "Albumin (g/dL)",
            min_value=1.0,
            max_value=5.0,
            value=4.0,
            step=0.1,
            format="%.1f",
            key="ca_albumin"
        )
        
        ionized_ca = st.number_input(
            "Ionized Ca (mg/dL) - nếu có",
            min_value=2.0,
            max_value=7.0,
            value=0.0,
            step=0.1,
            format="%.1f",
            key="ca_ionized"
        )
    
    with col2:
        # Corrected Ca = Total Ca + 0.8 × (4.0 - Albumin)
        corrected_ca = total_ca + 0.8 * (4.0 - albumin)
        
        st.markdown("### 📊 Kết Quả:")
        
        st.metric("Total Ca", f"{total_ca:.1f} mg/dL")
        st.metric("Corrected Ca", f"{corrected_ca:.1f} mg/dL")
        
        if ionized_ca > 0:
            st.metric("Ionized Ca", f"{ionized_ca:.1f} mg/dL")
            if ionized_ca < 3.5:
                st.error("🚨 **SEVERE HYPOCALCEMIA** - Cần điều trị ngay!")
            elif ionized_ca < 4.0:
                st.warning("⚠️ **MODERATE HYPOCALCEMIA**")
            else:
                st.info("✅ Ionized Ca trong giới hạn")
        else:
            if corrected_ca < 7.0:
                st.error("🚨 **SEVERE HYPOCALCEMIA** - Cần điều trị ngay!")
            elif corrected_ca < 8.0:
                st.warning("⚠️ **MODERATE HYPOCALCEMIA**")
            else:
                st.info("✅ Corrected Ca trong giới hạn")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Treatment")
    
    tab1, tab2, tab3 = st.tabs(["Severe Symptomatic", "Moderate", "Chronic"])
    
    with tab1:
        st.markdown("#### 🚨 Severe Symptomatic (<7.0 mg/dL hoặc iCa <3.5)")
        
        st.error("""
        **EMERGENCY - IV Calcium:**
        
        **Calcium Gluconate 10% (Preferred):**
        - **1-2g IV** (10-20ml) trong 10-20 phút
        - Hoặc 10-15 mg/kg (1-1.5 mEq/kg)
        - **Effect:** Immediate (within minutes)
        - **Duration:** 2-3h
        
        **Calcium Chloride 10% (Nếu không có gluconate):**
        - **0.5-1g IV** (5-10ml) trong 5-10 phút
        - Hoặc 5-10 mg/kg (0.5-1 mEq/kg)
        - **⚠️ More irritating, use central line if possible**
        
        **After initial dose:**
        - **Truyền liên tục:** 1-2g/h (10-20 mg/kg/h)
        - Hoặc **Intermittent:** 1g q4-6h
        - **Duration:** 12-24h hoặc đến khi ổn định
        
        **Monitoring:**
        - Ca²⁺ mỗi 2-4h
        - ECG (QT interval)
        - Symptoms (tetany, seizures)
        """)
        
        st.warning("""
        **⚠️ Precautions:**
        - **Hypercalcemia:** Không quá 2g trong 1h
        - **Digoxin:** Cẩn thận (nguy cơ loạn nhịp tim)
        - **IV site:** Có thể gây kích ứng (phlebitis)
        - **Renal failure:** Theo dõi sát PO4
        """)
    
    with tab2:
        st.markdown("#### ⚠️ Moderate (7.0-8.0 mg/dL hoặc iCa 3.5-4.0)")
        
        st.warning("""
        **Option 1: IV Calcium:**
        - **1g Calcium gluconate IV** trong 1h
        - Lặp lại q6-8h nếu cần
        
        **Option 2: Oral Calcium:**
        - **Calcium carbonate:** 1-2g PO q6-8h
        - Hoặc **Calcium citrate:** 1-2g PO q6-8h
        - **With meals** (tăng hấp thu)
        
        **Duration:**
        - 1-2 tuần
        - Kiểm tra Ca²⁺ sau 3-5 ngày
        """)
        
        st.info("""
        **If hypomagnesemia present:**
        - Điều chỉnh Mg²⁺ trước hoặc đồng thời
        - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
        """)
    
    with tab3:
        st.markdown("#### 📅 Chronic Hypocalcemia")
        
        st.success("""
        **Oral Calcium:**
        - **Calcium carbonate:** 1-2g PO TID (với meals)
        - Hoặc **Calcium citrate:** 1-2g PO TID
        - **Total:** 1.5-3g elemental Ca/ngày
        
        **Vitamin D:**
        - **Cholecalciferol (D3):** 1000-2000 IU/ngày
        - Hoặc **Calcitriol:** 0.25-0.5 mcg BID (nếu suy thận)
        
        **Monitoring:**
        - Ca²⁺, PO4, PTH mỗi 3-6 tháng
        - 24h urine Ca (risk nephrolithiasis)
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Common Causes")
    
    st.warning("""
    **Hypoparathyroidism:**
    - Post-surgical (thyroid, parathyroid surgery)
    - Autoimmune
    - Congenital
    
    **Vitamin D Deficiency:**
    - Malnutrition
    - Malabsorption
    - Renal failure (decreased 1,25-OH D)
    
    **Hypomagnesemia:**
    - ⚠️ Luôn kiểm tra Mg²⁺
    - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
    
    **Renal Failure:**
    - Decreased 1,25-OH D production
    - Hyperphosphatemia
    
    **Acute Pancreatitis:**
    - Saponification (Ca binds to fat)
    
    **Massive Transfusion:**
    - Citrate chelation
    
    **Hungry Bone Syndrome:**
    - Sau parathyroidectomy
    - Sau điều trị hypercalcemia
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Hypomagnesemia:**
    - ⚠️ Luôn kiểm tra và điều chỉnh Mg²⁺
    - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
    
    **Hyperphosphatemia:**
    - Điều chỉnh PO4 trước hoặc đồng thời
    - Ca × PO4 product <55 (risk precipitation)
    
    **Digoxin:**
    - Cẩn thận với IV Ca (nguy cơ loạn nhịp tim)
    - Điều chỉnh từ từ
    
    **Renal Failure:**
    - Dùng Calcitriol (1,25-OH D)
    - Điều chỉnh PO4 trước
    - Theo dõi sát Ca × PO4 product
    
    **Pregnancy:**
    - Ca²⁺ an toàn
    - Liều tương tự
    - Theo dõi sát
    """)

