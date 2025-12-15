"""
Hyperkalemia Emergency Protocol
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hyperkalemia Emergency Protocol"""
    
    st.error("## 🚨 HYPERKALEMIA EMERGENCY PROTOCOL")
    
    st.markdown("### 1️⃣ ECG Changes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **ECG Progression:**
        
        **K⁺ 5.5-6.5:**
        - Tall peaked T waves
        - QT shortening
        
        **K⁺ 6.5-7.5:**
        - PR prolongation
        - QRS widening
        - P waves flatten/disappear
        
        **K⁺ >7.5:**
        - Sine wave pattern
        - Ventricular fibrillation
        - Asystole
        
        **⚠️ Nếu có ECG changes:** Treat as EMERGENCY
        """)
    
    with col2:
        st.warning("""
        **Severity:**
        
        **Mild (5.5-6.0):**
        - Often asymptomatic
        - Monitor, treat cause
        
        **Moderate (6.0-7.0):**
        - May have ECG changes
        - Requires treatment
        
        **Severe (>7.0):**
        - Dangerous ECG changes
        - EMERGENCY!
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Treatment Ladder")
    
    st.info("""
    **Phase 1: Membrane Stabilization (< 5 minutes)**
    
    **✅ Calcium:**
    - **Calcium gluconate 10%:** 1g IV (10ml) trong 2-3 phút
    - Hoặc **Calcium chloride 10%:** 0.5-1g IV (5-10ml)
    - **Effect:** Immediate (within 1-3 min)
    - **Duration:** 30-60 min
    - **⚠️ Không giảm K⁺, chỉ bảo vệ tim!**
    """)
    
    st.markdown("---")
    st.success("""
    **Phase 2: Shift K⁺ into Cells (5-15 minutes)**
    
    **A. Insulin + Dextrose:**
    - **Regular insulin:** 10 U IV
    - **D50:** 50ml IV (hoặc 1 amp)
    - **Effect:** Onset 15-30 min
    - **Duration:** 4-6h
    - **Kiểm tra glucose:** Mỗi 1h × 4h (risk hypoglycemia!)
    
    **B. Albuterol:**
    - **10-20mg nebulized**
    - **Effect:** Onset 15-30 min
    - **Duration:** 2-3h
    - **Additive với insulin**
    
    **C. NaHCO₃ (nếu acidotic):**
    - **50-100 mEq IV** trong 5-10 min
    - **Chỉ nếu pH <7.2**
    - **Effect:** Onset 15-30 min
    - **⚠️ Không dùng nếu volume overload**
    """)
    
    st.markdown("---")
    st.warning("""
    **Phase 3: Remove K⁺ from Body (30 min - hours)**
    
    **A. Loop Diuretics:**
    - **Furosemide 40-80mg IV**
    - **Chỉ nếu:** Normal/high UO, volume overload
    - **Effect:** Onset 30 min
    - **⚠️ Không dùng nếu oliguric/anuric**
    
    **B. Potassium Binders:**
    - **Sodium Polystyrene Sulfonate (Kayexalate):**
      * 15-30g PO/PR q4-6h
      * Effect: Onset 1-2h
      * Duration: 4-6h
    - **Patiromer (Veltassa):** 8.4-25.2g PO q24h
    - **Sodium Zirconium Cyclosilicate (Lokelma):** 10g TID
    
    **C. Hemodialysis:**
    - **Indication:**
      * K⁺ >6.5 không đáp ứng
      * Renal failure
      * Oliguric/anuric
      * Severe ECG changes
    - **Effect:** Immediate removal
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Protocol by K⁺ Level")
    
    tab1, tab2, tab3 = st.tabs(["K⁺ 5.5-6.0", "K⁺ 6.0-7.0", "K⁺ >7.0"])
    
    with tab1:
        st.markdown("#### ⚠️ Mild Hyperkalemia (5.5-6.0)")
        
        st.info("""
        **Các Bước:**
        1. ✅ Kiểm tra ECG (nếu có changes → treat as moderate)
        2. ✅ Xác định nguyên nhân
        3. ✅ Ngừng bổ sung K⁺, thuốc lợi tiểu giữ K⁺
        4. ✅ Theo dõi K⁺ mỗi 4-6h
        5. ✅ Cân nhắc:
           * Loop diuretic
           * K⁺ binder (Kayexalate)
        
        **Thường:** Không cấp cứu, điều trị nguyên nhân
        """)
    
    with tab2:
        st.markdown("#### 🚨 Moderate Hyperkalemia (6.0-7.0)")
        
        st.error("""
        **Hành Động Ngay Lập Tức:**
        1. ✅ **ECG ngay** - Nếu có changes → Treat as severe
        2. ✅ **Đặt đường truyền tĩnh mạch**
        3. ✅ **Theo dõi ECG liên tục**
        
        **Điều trị:**
        1. **Calcium:** 1g IV (if ECG changes)
        2. **Insulin + D50:** 10U + 50ml
        3. **Albuterol:** 10-20mg nebulized
        4. **Furosemide:** 40-80mg IV (nếu có UO)
        5. **K⁺ binder:** Kayexalate 15-30g
        
        **Theo dõi:**
        - K⁺ mỗi 2-4h
        - ECG mỗi 1-2h
        - Glucose mỗi 1h (nếu dùng insulin)
        """)
    
    with tab3:
        st.markdown("#### 🚨🚨 Severe Hyperkalemia (>7.0)")
        
        st.error("""
        **CODE HYPERKALEMIA - EMERGENCY!**
        
        **Immediate (< 5 min):**
        1. ✅ **ECG ngay** - Theo dõi continuously
        2. ✅ **IV access** (2 lines)
        3. ✅ **Calcium:** 1g IV trong 2-3 phút
        4. ✅ **Repeat calcium** nếu ECG không cải thiện
        
        **Within 15 min:**
        1. ✅ **Insulin + D50:** 10U + 50ml
        2. ✅ **Albuterol:** 20mg nebulized
        3. ✅ **NaHCO₃:** 50-100 mEq (nếu acidotic)
        
        **Within 30-60 min:**
        1. ✅ **Furosemide:** 80-120mg IV (nếu có UO)
        2. ✅ **Kayexalate:** 30g PO/PR
        3. ✅ **Nephrology consult** - Prepare for HD
        
        **Chỉ định Lọc máu:**
        - K⁺ >7.0 với ECG changes
        - Oliguric/anuric
        - Renal failure
        - Không đáp ứng điều trị
        
        **Theo dõi:**
        - K⁺ mỗi 1-2h
        - ECG liên tục
        - Glucose mỗi 1h × 4h
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Nguyên nhân thường gặp")
    
    st.warning("""
    **Pseudohyperkalemia:**
    - Hemolysis
    - Thrombocytosis (>1M)
    - Leukocytosis (>100k)
    - Recheck nếu nghi ngờ
    
    **True Hyperkalemia:**
    - **Renal failure:** AKI, CKD
    - **Medications:**
      * K⁺-sparing diuretics (Spironolactone, Amiloride)
      * ACE-I, ARBs
      * NSAIDs
      * Cyclosporine, Tacrolimus
    - **Acidosis:** Metabolic acidosis
    - **Tissue breakdown:** Rhabdo, tumor lysis
    - **Adrenal insufficiency**
    - **K⁺ supplements**
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Hyperkalemia")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

