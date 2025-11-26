"""
Hyperglycemic Hyperosmolar State (HHS) Protocol
ADA 2023, Endocrine Society
Management of hyperglycemic hyperosmolar state
"""

import streamlit as st


def render():
    """Hyperglycemic Hyperosmolar State (HHS) Protocol"""
    st.subheader("🍭 Hội Chứng Tăng Đường Huyết Tăng Áp Lực Thẩm Thấu (HHS)")
    st.caption("ADA 2023, Endocrine Society - Hyperglycemic hyperosmolar state management")
    
    st.info("""
    **HHS (Hyperglycemic Hyperosmolar State):**
    - Tần suất: Ít hơn DKA nhưng tỷ lệ tử vong cao hơn (10-20%)
    - Thường gặp ở người cao tuổi, đái tháo đường type 2
    - Đặc điểm: Đường huyết rất cao, tăng áp lực thẩm thấu, không có nhiễm toan ceton
    
    **Chẩn Đoán:**
    - Glucose >600 mg/dL
    - Osmolality >320 mOsm/kg
    - pH >7.30 (không có nhiễm toan)
    - Bicarbonate >18 mEq/L
    - Ketones âm tính hoặc nhẹ
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Biệt HHS vs DKA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **HHS:**
        - Glucose: >600 mg/dL
        - Osmolality: >320
        - pH: >7.30
        - Bicarbonate: >18
        - Ketones: Âm tính/nhẹ
        - Tuổi: Thường >60
        - Type: Type 2
        """)
    
    with col2:
        st.warning("""
        **DKA:**
        - Glucose: >250 mg/dL
        - Osmolality: <320
        - pH: <7.30
        - Bicarbonate: <18
        - Ketones: Dương tính
        - Tuổi: Mọi lứa tuổi
        - Type: Type 1 hoặc 2
        """)
    
    st.markdown("---")
    
    # ========== SECTION: TREATMENT ==========
    st.markdown("### 💊 Điều Trị")
    
    treatment_tabs = st.tabs([
        "💧 Truyền Dịch",
        "💉 Insulin",
        "⚡ Điện Giải",
        "🩸 Phòng Ngừa Huyết Khối"
    ])
    
    with treatment_tabs[0]:
        st.markdown("#### 💧 Truyền Dịch (Fluid Resuscitation)")
        
        st.error("""
        **⚠️ ƯU TIÊN HÀNG ĐẦU - Truyền dịch TRƯỚC insulin**
        
        **Protocol:**
        1. **Giờ đầu:** 0.9% NS 1-2 L
        2. **Sau đó:** 200-500 mL/h (điều chỉnh theo đáp ứng)
        3. **Mục Tiêu:** Bù 50% thiếu hụt trong 12 giờ đầu
        
        **Tính thiếu hụt dịch:**
        - Ước tính: 8-12 L (10% trọng lượng cơ thể)
        - Hoặc: (Na hiện tại - 140) × 2 × trọng lượng (kg) × 0.6
        
        **Theo Dõi:**
        - Dấu hiệu sống mỗi 1-2 giờ
        - BUN, Cr mỗi 4-6 giờ
        - Osmolality mỗi 4-6 giờ
        - Dấu hiệu quá tải dịch
        """)
        
        # Fluid calculator
        with st.expander("🔢 Tính Lượng Dịch Cần Truyền", expanded=False):
            weight_kg = st.number_input(
                "Cân nặng (kg):",
                min_value=40.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                format="%.1f",
                key="hhs_weight"
            )
            
            current_na = st.number_input(
                "Na⁺ hiện tại (mEq/L):",
                min_value=120.0,
                max_value=180.0,
                value=150.0,
                step=1.0,
                format="%.1f",
                key="hhs_current_na"
            )
            
            if st.button("Tính Toán", type="primary", key="calc_hhs_fluid"):
                # Estimate fluid deficit (simplified)
                fluid_deficit_l = weight_kg * 0.1  # 10% dehydration
                
                # Adjust based on Na
                if current_na > 140:
                    na_correction = (current_na - 140) * 2 * weight_kg * 0.6 / 1000
                    fluid_deficit_l += na_correction
                
                st.info(f"""
                **Lượng dịch thiếu hụt ước tính:** {fluid_deficit_l:.1f} L
                
                **Kế hoạch truyền:**
                - **Giờ đầu:** 1-2 L
                - **12 giờ đầu:** {fluid_deficit_l * 0.5:.1f} L (50% thiếu hụt)
                - **24 giờ đầu:** {fluid_deficit_l:.1f} L (100% thiếu hụt)
                
                **Tốc độ truyền:**
                - **Giờ đầu:** 1-2 L/h
                - **Sau đó:** 200-500 mL/h
                - **Điều chỉnh:** Theo đáp ứng lâm sàng
                """)
    
    with treatment_tabs[1]:
        st.markdown("#### 💉 Insulin Therapy")
        
        st.warning("""
        **⚠️ QUAN TRỌNG:**
        - **KHÔNG bắt đầu insulin** cho đến khi đã truyền dịch ≥1 L
        - **Liều thấp hơn DKA** (0.05-0.1 vs 0.1 units/kg/h)
        - **Hạ glucose từ từ** (50-75 mg/dL/h)
        
        **Protocol:**
        1. **Bolus:** KHÔNG cần (khác DKA)
        2. **Infusion:** 0.05-0.1 units/kg/h
        3. **Mục Tiêu:** Giảm glucose 50-75 mg/dL/h
        4. **Khi glucose <300:** Thêm D5W + tiếp tục insulin
        5. **Khi glucose 200-300:** Chuyển SC insulin
        
        **Tránh:**
        - Hạ glucose quá nhanh (>100 mg/dL/h) → Nguy cơ phù não
        - Ngừng insulin đột ngột → Rebound hyperglycemia
        """)
        
        # Insulin calculator
        with st.expander("🔢 Tính Liều Insulin", expanded=False):
            weight_kg_ins = st.number_input(
                "Cân nặng (kg):",
                min_value=40.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                format="%.1f",
                key="hhs_ins_weight"
            )
            
            insulin_rate = st.radio(
                "Liều insulin:",
                ["0.05 units/kg/h (Thấp)", "0.1 units/kg/h (Chuẩn)"],
                key="hhs_ins_rate"
            )
            
            if "0.05" in insulin_rate:
                rate_per_kg = 0.05
            else:
                rate_per_kg = 0.1
            
            insulin_units_h = weight_kg_ins * rate_per_kg
            
            st.info(f"""
            **Liều insulin:**
            - **{rate_per_kg} units/kg/h × {weight_kg_ins:.1f} kg = {insulin_units_h:.2f} units/h**
            
            **Chuẩn bị:**
            - Pha 50 units regular insulin trong 50 mL NS
            - Tốc độ truyền: {insulin_units_h:.2f} units/h = {insulin_units_h:.2f} mL/h
            - Hoặc: {insulin_units_h * 60:.1f} mL/phút
            
            **Theo Dõi:**
            - Glucose mỗi 1-2 giờ
            - Điều chỉnh liều theo đáp ứng
            """)
    
    with treatment_tabs[2]:
        st.markdown("#### ⚡ Điều Chỉnh Điện Giải")
        
        st.info("""
        **Kali (K⁺):**
        - **Bổ sung ngay** (thường thiếu dù K⁺ bình thường)
        - **Liều:** 20-40 mEq/h khi K⁺ <5.5
        - **Mục Tiêu:** K⁺ 4-5 mEq/L
        - **Theo Dõi:** Mỗi 2-4 giờ
        
        **Phosphorus (PO₄³⁻):**
        - **Bổ sung nếu:** <1.0 mg/dL
        - **Liều:** 0.5-1.0 mmol/kg (truyền tĩnh mạch)
        - **Mục đích:** Phòng ngừa suy cơ hô hấp
        
        **Magnesium (Mg²⁺):**
        - **Bổ sung nếu:** <1.5 mg/dL
        - **Liều:** 1-2 g IV
        - **Mục đích:** Phòng ngừa loạn nhịp tim
        """)
    
    with treatment_tabs[3]:
        st.markdown("#### 🩸 Phòng Ngừa Huyết Khối")
        
        st.error("""
        **⚠️ NGUY CƠ HUYẾT KHỐI RẤT CAO**
        
        **Cơ chế:**
        - Tăng đông máu do tăng áp lực thẩm thấu
        - Mất nước → tăng độ nhớt máu
        - Tăng nguy cơ DVT, PE, đột quỵ
        
        **Protocol:**
        - **Heparin:** 5000 units SC q8-12h
        - **Hoặc:** Enoxaparin 40mg SC q24h
        - **Bắt đầu:** Ngay khi chẩn đoán
        - **Tiếp tục:** Cho đến khi osmolality <320
        
        **Chống chỉ định:**
        - Chảy máu đang hoạt động
        - Giảm tiểu cầu nặng
        - Rối loạn đông máu
        """)
    
    st.markdown("---")
    
    # ========== SECTION: IMMEDIATE MANAGEMENT ==========
    st.markdown("### ⚡ Xử Trí Ngay Lập Tức")
    
    st.error("""
    **Ưu tiên hàng đầu:**
    1. ✅ **ABC:** Airway, Breathing, Circulation
    2. ✅ **Truyền dịch ngay:** 0.9% NS 1-2 L trong giờ đầu
    3. ✅ **Đo glucose, ABG, điện giải ngay**
    4. ✅ **Bắt đầu insulin** sau khi đã truyền dịch
    5. ✅ **Heparin prophylaxis** (nguy cơ huyết khối cao)
    """)
    
    st.markdown("---")
    
    # ========== SECTION: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 🔍 Tiêu chuẩn chẩn đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán HHS", expanded=True):
        st.markdown("""
        **Chẩn Đoán HHS khi có TẤT CẢ:**
        1. **Glucose:** >600 mg/dL (thường >800)
        2. **Osmolality:** >320 mOsm/kg
        3. **pH:** >7.30 (KHÔNG có nhiễm toan)
        4. **Bicarbonate:** >18 mEq/L
        5. **Ketones:** Âm tính hoặc nhẹ (trace/small)
        6. **Anion gap:** <12 (bình thường)
        
        **Lưu ý:**
        - HHS có thể kết hợp với DKA (HHS-DKA overlap)
        - Cần phân biệt với DKA để điều trị đúng
        """)
    
    st.markdown("---")
    
    # ========== SECTION: OSMOLALITY CALCULATOR ==========
    st.markdown("### 📊 Tính Áp Lực Thẩm Thấu")
    
    st.info("""
    **Công thức:**
    - **Osmolality = 2 × Na + Glucose/18 + BUN/2.8**
    - **Bình thường:** 280-300 mOsm/kg
    - **HHS:** >320 mOsm/kg
    """)
    
    # Calculator
    with st.expander("🔢 Calculator Tính Osmolality", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            na = st.number_input(
                "Na⁺ (mEq/L):",
                min_value=100.0,
                max_value=180.0,
                value=145.0,
                step=1.0,
                format="%.1f",
                key="hhs_na"
            )
            
            glucose = st.number_input(
                "Glucose (mg/dL):",
                min_value=100.0,
                max_value=2000.0,
                value=800.0,
                step=10.0,
                format="%.0f",
                key="hhs_glucose"
            )
        
        with col2:
            bun = st.number_input(
                "BUN (mg/dL):",
                min_value=5.0,
                max_value=200.0,
                value=40.0,
                step=1.0,
                format="%.1f",
                key="hhs_bun"
            )
        
        if st.button("Tính Osmolality", type="primary", key="calc_hhs_osm"):
            osmolality = 2 * na + glucose/18 + bun/2.8
            
            st.markdown("### 📊 Kết quả")
            
            if osmolality > 320:
                st.error(f"""
                **Osmolality = {osmolality:.1f} mOsm/kg**
                
                **🚨 HHS XÁC ĐỊNH** (Osmolality >320)
                - Cần điều trị ngay lập tức
                - Nguy cơ tử vong cao nếu không điều trị
                """)
            elif osmolality > 300:
                st.warning(f"""
                **Osmolality = {osmolality:.1f} mOsm/kg**
                
                **⚠️ Tăng áp lực thẩm thấu** (300-320)
                - Theo dõi sát
                - Có thể tiến triển thành HHS
                """)
            else:
                st.success(f"""
                **Osmolality = {osmolality:.1f} mOsm/kg**
                
                **✅ Bình thường** (<300)
                - Không đáp ứng tiêu chuẩn HHS
                """)
            
            st.markdown(f"""
            **Chi tiết tính toán:**
            - 2 × Na = 2 × {na:.1f} = {2*na:.1f}
            - Glucose/18 = {glucose:.0f}/18 = {glucose/18:.1f}
            - BUN/2.8 = {bun:.1f}/2.8 = {bun/2.8:.1f}
            - **Tổng = {osmolality:.1f} mOsm/kg**
            """)
    
    st.markdown("---")
    
    # ========== SECTION: COMMON CAUSES ==========
    st.markdown("### 🔍 Nguyên Nhân Thường Gặp")
    
    st.warning("""
    **Nguyên nhân thúc đẩy HHS:**
    1. **Nhiễm trùng** (40-60%):
       - Viêm phổi
       - Nhiễm trùng tiết niệu
       - Nhiễm trùng da/mô mềm
       - Sepsis
    
    2. **Thuốc** (20-30%):
       - Thiazide diuretics
       - Corticosteroids
       - Beta-blockers
       - Phenytoin
       - Olanzapine, risperidone
    
    3. **Bệnh lý cấp tính** (10-20%):
       - Đột quỵ
       - Nhồi máu cơ tim
       - Suy tim
       - Viêm tụy
    
    4. **Khác:**
       - Bỏ qua insulin
       - Ăn uống quá nhiều đường
       - Mất nước (không uống đủ nước)
    """)
    
    st.markdown("---")
    
    # ========== SECTION: MONITORING ==========
    st.markdown("### 📈 Monitoring Protocol")
    
    st.markdown("""
    **Theo Dõi Trong Quá Trình Điều Trị:**
    """)
    
    monitoring_table = {
        "Thông số": [
            "Glucose",
            "Osmolality",
            "Điện giải (Na, K, PO4, Mg)",
            "BUN, Cr",
            "ABG/VBG",
            "Dấu hiệu sống",
            "Dấu hiệu phù não"
        ],
        "Tần suất": [
            "Mỗi 1-2 giờ",
            "Mỗi 4-6 giờ",
            "Mỗi 4-6 giờ",
            "Mỗi 6-12 giờ",
            "Mỗi 4-6 giờ (nếu cần)",
            "Mỗi 1-2 giờ",
            "Liên tục"
        ],
        "Mục Tiêu": [
            "Giảm 50-75 mg/dL/h",
            "Giảm <10 mOsm/kg/h",
            "K⁺ 4-5, Na⁺ bình thường",
            "Bình thường hóa",
            "pH >7.30, HCO₃⁻ >18",
            "Ổn định",
            "Không có"
        ]
    }
    
    st.table(monitoring_table)
    
    st.warning("""
    **Dấu Hiệu Cảnh Báo:**
    - Glucose giảm quá nhanh (>100 mg/dL/h) → Nguy cơ phù não
    - Osmolality không giảm → Cần tăng tốc độ truyền dịch
    - K⁺ giảm → Tăng bổ sung kali
    - Dấu hiệu quá tải dịch → Giảm tốc độ truyền
    """)
    
    st.markdown("---")
    
    # ========== SECTION: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến Chứng")
    
    st.error("""
    **1. Phù Não:**
    - Nguy cơ: Hạ glucose quá nhanh
    - Triệu chứng: Đau đầu, buồn nôn, rối loạn ý thức
    - Phòng ngừa: Hạ glucose từ từ (50-75 mg/dL/h)
    
    **2. Huyết Khối:**
    - Nguy cơ: Rất cao (tăng đông máu)
    - Phòng ngừa: Heparin prophylaxis
    
    **3. Suy Thận:**
    - Nguy cơ: Thiếu dịch nặng
    - Phòng ngừa: Truyền dịch đủ
    
    **4. Rối Loạn Điện Giải:**
    - Nguy cơ: Kali, phosphorus, magnesium
    - Phòng ngừa: Bổ sung sớm
    """)
    
    st.markdown("---")
    
    # ========== SECTION: DISCHARGE CRITERIA ==========
    st.markdown("### 🏥 Tiêu chuẩn xuất viện")
    
    st.success("""
    **Tiêu chuẩn xuất viện khi:**
    - ✅ Glucose: 200-300 mg/dL và ổn định
    - ✅ Osmolality: <320 mOsm/kg
    - ✅ Dấu hiệu sống ổn định ≥24 giờ
    - ✅ Điện giải bình thường
    - ✅ Bệnh nhân ăn uống được
    - ✅ Có kế hoạch điều trị tại nhà
    - ✅ Đã điều trị nguyên nhân thúc đẩy
    
    **Chuyển sang điều trị tại nhà:**
    - SC insulin (basal + bolus)
    - Hoặc thuốc uống (nếu phù hợp)
    - Theo dõi glucose tại nhà
    - Tái khám sau 1-2 tuần
    """)
    
    st.markdown("---")
    
    # ========== SECTION: CHECKLIST ==========
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Chẩn Đoán (Glucose >600, Osmolality >320, pH >7.30)",
        "✅ ABC: Airway, Breathing, Circulation",
        "✅ Truyền Dịch ngay (0.9% NS 1-2 L giờ đầu)",
        "✅ Insulin 0.05-0.1 units/kg/h (sau khi đã truyền dịch)",
        "✅ Bổ Sung Kali ngay",
        "✅ Heparin Prophylaxis (5000 units SC q8-12h)",
        "✅ Theo Dõi Glucose mỗi 1-2 giờ",
        "✅ Theo Dõi Osmolality mỗi 4-6 giờ",
        "✅ Theo Dõi Điện Giải mỗi 4-6 giờ",
        "✅ Tìm Và Điều Trị Nguyên Nhân (nhiễm trùng, thuốc, v.v.)"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ cao hơn
        - Cẩn thận với truyền dịch (nguy cơ quá tải)
        - Theo dõi huyết động sát
        
        **Suy thận:**
        - Cẩn thận với truyền dịch
        - Theo dõi BUN, Cr sát
        - Có thể cần RRT
        """)
    
    with col2:
        st.markdown("""
        **Suy tim:**
        - Cẩn thận với truyền dịch
        - Có thể cần CVP monitoring
        - Cân nhắc giảm tốc độ truyền
        
        **Có thai:**
        - Hiếm gặp
        - Điều trị tương tự
        - Monitor thai nhi
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục Tiêu Trong 24 Giờ Đầu:**
    - ✅ **Glucose:** 200-300 mg/dL (giảm 50-75 mg/dL/h)
    - ✅ **Osmolality:** Giảm <10 mOsm/kg/h
    - ✅ **Dấu hiệu sống:** Ổn định
    - ✅ **Điện giải:** Bình thường (K⁺ 4-5, Na⁺ bình thường)
    - ✅ **Không biến chứng:** Phù não, huyết khối, suy thận
    
    **Mục Tiêu Trong 48-72 Giờ:**
    - ✅ **Glucose:** 150-250 mg/dL
    - ✅ **Osmolality:** <310 mOsm/kg
    - ✅ **Chuyển SC insulin:** Khi glucose 200-300 và ổn định
    - ✅ **Điều trị nguyên nhân:** Đã giải quyết
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ADA 2023 Guidelines**
       - American Diabetes Association
    
    2. **Endocrine Society Guidelines**
       - Kitabchi AE, et al. Diabetes Care. 2009
    
    3. **UpToDate:** Hyperglycemic hyperosmolar state
       - Last updated: 2024
    
    4. **Medscape:** HHS Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

