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
    st.markdown("### 📋 Hướng dẫn Chi tiết: Pha và Sử dụng Insulin (Actrapid) cho Tăng Kali máu")
    
    with st.expander("💉 Xem chi tiết pha insulin cho hyperkalemia", expanded=False):
        st.markdown("""
        **I. Điều trị Cấp cứu Tăng Kali máu (Hyperkalemia)**
        
        **Nguyên lý:**
        - Insulin kích thích bơm Na+/K+-ATPase, đẩy K+ từ ngoại bào vào nội bào
        - Glucose được phối hợp để dự phòng hạ đường huyết do Insulin, không nhằm mục đích nuôi dưỡng
        
        **Phác đồ chuẩn:** 10 UI Actrapid + 25g - 50g Glucose
        
        **Cách pha và đường dùng:**
        
        **1. Bolus tĩnh mạch (Tiêm nhanh/Bơm tiêm điện):**
        - Pha **10 UI Actrapid + 50mL Glucose 50%**
        - Ưu tiên dùng bơm tiêm điện hoặc tiêm tĩnh mạch chậm
        - **Thời gian:** Tiêm chậm trong 5-10 phút
        
        **2. Truyền tĩnh mạch (IV Drip):**
        - **10 UI Actrapid** pha trong **500mL Glucose 5%** (Chứa 25g đường)
        - Hoặc: **10 UI Actrapid** pha trong **250mL Glucose 10%** (Chứa 25g đường)
        - **Thời gian truyền:** 30 – 60 phút
        
        **Lưu ý:**
        - Tỷ lệ này áp dụng chung cho cả bệnh nhân đái tháo đường (ĐTĐ) và không ĐTĐ
        - Cần theo dõi sát đường huyết mao mạch (Capillary Blood Glucose - CBG) ở bệnh nhân ĐTĐ do đường huyết nền đã cao
        - **KHÔNG bổ sung Kali** trong trường hợp này (đang điều trị tăng kali máu!)
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
    st.markdown("### 📊 Nuôi dưỡng và Kiểm soát Đường huyết (Phác đồ GIK)")
    
    with st.expander("🍽️ Xem phác đồ GIK cho nuôi dưỡng", expanded=False):
        st.markdown("""
        **Nguyên lý:**
        - Cung cấp năng lượng (Glucose) kèm Insulin ngoại sinh để chuyển hóa
        - Ngăn ngừa tăng đường huyết phản ứng (đặc biệt trong stress ngoại khoa, nhiễm trùng)
        
        **Quy tắc tính toán:**
        - Tính tổng lượng đường (gam) trong chai dịch
        - Áp dụng tỷ lệ nhạy cảm Insulin tương ứng
        
        **Ví dụ:**
        - Chai Glucose 5% (500mL) chứa **25g đường**
        - Chai Glucose 10% (500mL) chứa **50g đường**
        """)
        
        st.markdown("---")
        st.markdown("#### 📋 Bảng Tỷ lệ Pha Insulin (Actrapid) trong Dịch truyền Glucose")
        
        # Create table using HTML for better formatting
        st.markdown("""
        <style>
        .insulin-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9rem;
        }
        .insulin-table th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }
        .insulin-table td {
            padding: 10px 12px;
            border-bottom: 1px solid #e0e0e0;
        }
        .insulin-table tr:hover {
            background-color: #f5f5f5;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <table class="insulin-table">
        <thead>
        <tr>
            <th>Phân loại Bệnh nhân</th>
            <th>Tỷ lệ (Insulin : Glucose)</th>
            <th>Số lượng Insulin trong chai G5% (25g đường)</th>
            <th>Số lượng Insulin trong chai G10% (50g đường)</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td><strong>Người bình thường</strong><br>(Không tiền sử ĐTĐ)</td>
            <td>1 UI : 4 - 6g đường<br><em>(Thường dùng 1:5)</em></td>
            <td>4 - 6 UI<br><em>(Trung bình: 5 UI)</em></td>
            <td>8 - 12 UI<br><em>(Trung bình: 10 UI)</em></td>
        </tr>
        <tr>
            <td><strong>Bệnh nhân ĐTĐ</strong><br>(Tiền sử ĐTĐ)</td>
            <td>1 UI : 3 - 4g đường<br><em>(Thường dùng 1:3 hoặc 1:4)</em></td>
            <td>6 - 8 UI<br><em>(Trung bình: 7 UI)</em></td>
            <td>12 - 16 UI<br><em>(Trung bình: 14 UI)</em></td>
        </tr>
        <tr>
            <td><strong>Kháng Insulin cao</strong><br>(Nhiễm trùng nặng, dùng Corticoid)</td>
            <td>1 UI : 2 - 3g đường</td>
            <td>8 - 12 UI</td>
            <td>16 - 25 UI</td>
        </tr>
        </tbody>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("#### 🏥 Phác đồ Alberti kinh điển (Nuôi dưỡng)")
        
        st.info("""
        **Phác đồ chuẩn:**
        - **500mL Glucose 10%** + **10-15 UI Actrapid** + **10-20 mmol KCl**
        - **Tốc độ truyền:** 100 mL/h
        
        **Chỉ định:**
        - Khi dùng Glucose nồng độ cao (10%, 20%...) để nuôi dưỡng
        - Stress-induced hyperglycemia (nhiễm trùng, phẫu thuật)
        - Bệnh nhân không ăn được, cần nuôi dưỡng qua đường tĩnh mạch
        
        **Không cần Insulin:**
        - Không có tiền sử ĐTĐ + đường huyết nền < 10 mmol/L + chỉ dùng Glucose 5%
        """)
        
        st.markdown("---")
        st.markdown("#### ⚠️ Ba Nguyên tắc An toàn Bắt buộc")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.error("""
            **1. Kiểm soát Kali máu (Tránh Hạ Kali)**
            
            **Nguy cơ:** Insulin gây hạ kali máu
            
            **Chỉ định (Nuôi dưỡng):**
            - **LUÔN BỔ SUNG KALI** nếu chức năng thận tốt và K+ bình thường
            
            **Chống chỉ định (Cấp cứu Tăng K+):**
            - **KHÔNG BỔ SUNG KALI** khi đang điều trị tăng kali máu!
            """)
            
            st.warning("""
            **2. Hiện tượng Hấp phụ Insulin (Adsorption)**
            
            **Nguy cơ:** Mất 20-50% insulin vào đường truyền PVC
            
            **Xử trí:**
            - **Chính xác:** Prime đường truyền / Dùng bơm tiêm riêng
            - **Thường quy:** Chấp nhận mất / Thêm 1-2 UI để bù
            """)
        
        with col2:
            st.info("""
            **3. Theo dõi Đường huyết (Monitoring)**
            
            **Không ĐTĐ:**
            - Test mỗi 6-12 giờ
            
            **ĐTĐ / Bệnh nặng:**
            - Test mỗi 1-3 giờ (giai đoạn đầu)
            - Theo dõi sát để điều chỉnh liều insulin
            
            **Mục tiêu đường huyết:**
            - **ICU:** 140-180 mg/dL (7.8-10 mmol/L)
            - **Ward:** 100-180 mg/dL (5.6-10 mmol/L)
            """)
        
        st.markdown("---")
        st.markdown("#### 💡 Lời khuyên Lâm sàng")
        
        st.success("""
        **Chỉ định dùng Insulin:**
        - Khi dùng Glucose nồng độ cao (10%, 20%...) để nuôi dưỡng
        - Stress-induced hyperglycemia (nhiễm trùng, phẫu thuật, chấn thương)
        - Bệnh nhân ĐTĐ cần nuôi dưỡng qua đường tĩnh mạch
        
        **Không cần Insulin:**
        - Không có tiền sử ĐTĐ + đường huyết nền < 10 mmol/L + chỉ dùng Glucose 5%
        - Bệnh nhân ăn được bình thường
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

