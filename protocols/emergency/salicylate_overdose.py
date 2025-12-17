"""
Salicylate Overdose Protocol
Acute aspirin poisoning management
Life-threatening metabolic acidosis and CNS toxicity
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Salicylate Overdose Protocol"""
    st.subheader("💊 Ngộ Độc Salicylate (Aspirin)")
    st.caption("Acute salicylate poisoning - Metabolic acidosis and CNS toxicity")
    
    st.error("""
    **⚠️ NGỘ ĐỘC SALICYLATE = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Liều độc: >150 mg/kg
    - Liều gây tử vong: >500 mg/kg
    - Tỷ lệ tử vong: 1-2% nếu không điều trị
    
    **Cơ chế:**
    - Kích thích trung tâm hô hấp → Tăng thông khí
    - Rối loạn chuyển hóa → Nhiễm toan chuyển hóa
    - Tổn thương thần kinh trung ương
    - Rối loạn đông máu
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá nguy cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        time_since_ingestion = st.number_input(
            "**Thời gian từ khi uống (giờ):**",
            min_value=0.0,
            max_value=168.0,
            value=4.0,
            step=0.5,
            help="Nhập số giờ từ khi uống salicylate"
        )
        
        amount_ingested = st.number_input(
            "**Liều đã uống (mg):**",
            min_value=0,
            max_value=100000,
            value=0,
            step=100,
            help="Tổng liều salicylate đã uống (mg)"
        )
        
        weight = st.number_input(
            "**Cân nặng (kg):**",
            min_value=1.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
            help="Cân nặng bệnh nhân"
        )
    
    with col2:
        if amount_ingested > 0 and weight > 0:
            dose_per_kg = amount_ingested / weight
            
            st.info(f"""
            **Liều tính theo kg:** {dose_per_kg:.1f} mg/kg
            
            **Đánh giá:**
            - **Liều an toàn:** <150 mg/kg
            - **Liều độc:** ≥150 mg/kg
            - **Liều gây tử vong:** ≥500 mg/kg
            """)
            
            if dose_per_kg >= 500:
                st.error("🚨 **NGUY CƠ RẤT CAO** - Liều gây tử vong!")
            elif dose_per_kg >= 150:
                st.warning("⚠️ **NGUY CƠ CAO** - Liều độc, cần điều trị ngay!")
            else:
                st.success("✅ **NGUY CƠ THẤP** - Liều an toàn")
    
    st.markdown("---")
    
    # ========== SECTION 2: SERUM LEVEL ==========
    st.markdown("### 📈 Nồng Độ Huyết Thanh")
    
    has_serum_level = st.checkbox("Có kết quả nồng độ salicylate trong huyết thanh", value=False)
    
    if has_serum_level:
        serum_level = st.number_input(
            "**Nồng độ salicylate (mg/dL):**",
            min_value=0.0,
            max_value=200.0,
            value=0.0,
            step=0.1,
            help="Nồng độ salicylate trong huyết thanh (mg/dL)"
        )
        
        if serum_level > 0:
            if serum_level >= 100:
                st.error(f"""
                🚨 **NGUY CƠ RẤT CAO** - Nồng độ: {serum_level:.1f} mg/dL
                
                - Cần lọc máu ngay lập tức
                - Tiên lượng xấu
                """)
            elif serum_level >= 60:
                st.warning(f"""
                ⚠️ **NGUY CƠ CAO** - Nồng độ: {serum_level:.1f} mg/dL
                
                - Cần điều trị tích cực
                - Cân nhắc lọc máu
                """)
            elif serum_level >= 30:
                st.warning(f"""
                ⚠️ **NGUY CƠ TRUNG BÌNH** - Nồng độ: {serum_level:.1f} mg/dL
                
                - Cần điều trị
                - Theo dõi chặt chẽ
                """)
            else:
                st.success(f"""
                ✅ **NGUY CƠ THẤP** - Nồng độ: {serum_level:.1f} mg/dL
                
                - Có thể theo dõi
                - Điều trị nếu có triệu chứng
                """)
    
    st.markdown("---")
    
    # ========== SECTION 3: CLINICAL PRESENTATION ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    st.markdown("""
    **Triệu chứng sớm (0-6 giờ):**
    - Buồn nôn, nôn
    - Ù tai, giảm thính lực
    - Chóng mặt
    - Tăng thông khí (hyperventilation)
    
    **Triệu chứng nặng:**
    - Sốt, đổ mồ hôi
    - Mất nước
    - Rối loạn ý thức, lú lẫn
    - Co giật
    - Phù phổi
    - Suy thận
    
    **Dấu hiệu nguy hiểm:**
    - 🚨 Rối loạn ý thức
    - 🚨 Co giật
    - 🚨 Nhiễm toan nặng (pH <7.2)
    - 🚨 Phù phổi
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: LABORATORY FINDINGS ==========
    st.markdown("### 🧪 Xét nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Xét nghiệm cần làm:**
        - **Salicylate level:** Ngay lập tức
        - **ABG:** Nhiễm toan chuyển hóa + kiềm hô hấp
        - **Điện giải:** Na, K, Cl, HCO3
        - **Đường huyết:** Có thể tăng hoặc giảm
        - **Chức năng thận:** Creatinine, BUN
        """)
    
    with col2:
        st.markdown("""
        **Đặc điểm ABG:**
        - **pH:** Giảm (nhiễm toan)
        - **PaCO2:** Giảm (tăng thông khí)
        - **HCO3:** Giảm (nhiễm toan chuyển hóa)
        - **Anion gap:** Tăng (>12)
        
        **Triệu chứng "kiềm hô hấp":**
        - Tăng thông khí bù trừ
        - PaCO2 có thể <20 mmHg
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác đồ điều trị")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Rất nặng (Critical)"],
        key="salicylate_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_protocol()
    elif "Trung bình" in severity:
        render_moderate_protocol()
    elif "Nặng" in severity:
        render_severe_protocol()
    else:
        render_critical_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 6: ALKALINIZATION ==========
    st.markdown("### 💉 Kiềm Hóa Nước tiểu (Urine Alkalinization)")
    
    st.info("""
    **Mục đích:** Tăng đào thải salicylate qua thận
    
    **Cơ chế:**
    - Salicylate là acid yếu (pKa = 3.0)
    - Kiềm hóa nước tiểu (pH >7.5) → Ion hóa salicylate
    - Ion hóa không tái hấp thu → Tăng đào thải
    
    **Phác đồ:**
    - **NaHCO3:** 1-2 mEq/kg IV bolus, sau đó 100-150 mEq trong 1L D5W
    - **Mục tiêu:** Urine pH >7.5
    - **Theo dõi:** pH nước tiểu mỗi giờ, K+ (có thể giảm)
    """)
    
    weight_alk = st.number_input(
        "**Cân nặng (kg):**",
        min_value=1.0,
        max_value=200.0,
        value=70.0,
        step=0.5,
        key="alk_weight"
    )
    
    if weight_alk > 0:
        bolus_dose = weight_alk * 1.5  # 1.5 mEq/kg
        maintenance_dose = 100  # 100-150 mEq/L
        
        st.success(f"""
        **Liều NaHCO3 (cho {weight_alk:.1f} kg):**
        
        - **Liều nạp:** {bolus_dose:.0f} mEq IV bolus
        - **Liều duy trì:** {maintenance_dose} mEq trong 1L D5W
        - **Tốc độ:** 200-250 mL/giờ
        - **Mục tiêu:** Urine pH >7.5
        
        **Lưu ý:**
        - Bổ sung K+ nếu cần (K+ giảm do kiềm hóa)
        - Theo dõi pH nước tiểu mỗi giờ
        - Ngừng khi salicylate level <30 mg/dL
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: HEMODIALYSIS ==========
    st.markdown("### 🔄 Lọc máu (Hemodialysis)")
    
    st.error("""
    **Chỉ định lọc máu:**
    
    **Tuyệt đối:**
    - Salicylate level >100 mg/dL
    - Rối loạn ý thức nặng
    - Co giật
    - Suy thận cấp
    - Phù phổi
    
    **Tương đối:**
    - Salicylate level >60 mg/dL với triệu chứng
    - Nhiễm toan nặng (pH <7.2) không đáp ứng điều trị
    - Suy giảm chức năng thận
    - Người cao tuổi với bệnh lý kèm theo
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Trong quá trình điều trị:**
    
    **Xét nghiệm:**
    - **Salicylate level:** Mỗi 2-4 giờ cho đến khi <30 mg/dL
    - **ABG:** Mỗi 2-4 giờ
    - **Điện giải:** Mỗi 4-6 giờ
    - **Urine pH:** Mỗi giờ (nếu kiềm hóa)
    - **Chức năng thận:** Mỗi 12-24 giờ
    
    **Triệu chứng:**
    - Mức độ ý thức
    - Tần số thở
    - Dấu hiệu mất nước
    - Dấu hiệu phù phổi
    
    **Dấu hiệu cảnh báo:**
    - 🚨 Rối loạn ý thức nặng hơn
    - 🚨 Co giật
    - 🚨 pH <7.2
    - 🚨 Phù phổi
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("salicylate_overdose"))


def render_mild_protocol():
    """Mild salicylate poisoning"""
    st.success("## ⚠️ MILD SALICYLATE POISONING")
    
    st.markdown("""
    **Đặc điểm:**
    - Salicylate level: 30-60 mg/dL
    - Triệu chứng nhẹ: Buồn nôn, ù tai
    - Không có rối loạn ý thức
    
    **Điều trị:**
    1. **Than hoạt:** 50-100g nếu <1 giờ
    2. **Bù dịch:** NS hoặc LR
    3. **Theo dõi:** Salicylate level mỗi 4 giờ
    4. **Kiềm hóa:** Có thể cân nhắc nếu level >40 mg/dL
    
    **Theo dõi:**
    - Nếu level giảm và không có triệu chứng → Có thể xuất viện sau 24 giờ
    - Nếu level tăng hoặc có triệu chứng → Điều trị tích cực hơn
    """)


def render_moderate_protocol():
    """Moderate salicylate poisoning"""
    st.warning("## 🚨 MODERATE SALICYLATE POISONING")
    
    st.markdown("""
    **Đặc điểm:**
    - Salicylate level: 60-100 mg/dL
    - Triệu chứng: Nôn, tăng thông khí, mất nước
    - Có thể có rối loạn ý thức nhẹ
    
    **Điều trị:**
    1. **Than hoạt:** 50-100g nếu <1 giờ
    2. **Bù dịch:** NS hoặc LR, 1-2L
    3. **Kiềm hóa nước tiểu:** Bắt buộc
       - NaHCO3: 1-2 mEq/kg bolus
       - Duy trì: 100-150 mEq trong 1L D5W
    4. **Bổ sung K+:** Nếu K+ <4.0 mEq/L
    5. **Theo dõi:** Salicylate level mỗi 2-4 giờ
    
    **Mục tiêu:**
    - Urine pH >7.5
    - Salicylate level <30 mg/dL
    - Cải thiện triệu chứng
    """)


def render_severe_protocol():
    """Severe salicylate poisoning"""
    st.error("## 🚨🚨 SEVERE SALICYLATE POISONING - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Salicylate level: >100 mg/dL
    - Rối loạn ý thức
    - Nhiễm toan nặng
    - Có thể có co giật
    
    **Điều trị ngay lập tức:**
    1. **ABC:** Đảm bảo đường thở, thở, tuần hoàn
    2. **Đặt nội khí quản:** Nếu cần (cẩn thận với tăng thông khí)
    3. **Bù dịch:** NS hoặc LR, 2-3L
    4. **Kiềm hóa nước tiểu:** Tích cực
    5. **Lọc máu:** Cân nhắc ngay lập tức
    
    **ICU Monitoring:**
    - Continuous monitoring
    - ABG mỗi 2 giờ
    - Salicylate level mỗi 2 giờ
    - Theo dõi chức năng thận
    
    **Cân nhắc lọc máu:**
    - Level >100 mg/dL → Lọc máu ngay
    - Level 60-100 mg/dL + triệu chứng nặng → Lọc máu
    """)


def render_critical_protocol():
    """Critical salicylate poisoning"""
    st.error("## 🚨🚨🚨 CRITICAL SALICYLATE POISONING - EMERGENCY DIALYSIS")
    
    st.markdown("""
    **Đặc điểm:**
    - Salicylate level: >100 mg/dL
    - Rối loạn ý thức nặng/coma
    - Co giật
    - Suy thận cấp
    - Phù phổi
    - Nhiễm toan nặng (pH <7.2)
    
    **Điều trị khẩn cấp:**
    1. **ABC:** Ngay lập tức
    2. **Đặt nội khí quản:** Nếu cần
    3. **Lọc máu:** NGAY LẬP TỨC
       - Không chờ điều trị nội khoa
       - Lọc máu là điều trị chính
    4. **Bù dịch:** Thận trọng (tránh quá tải)
    5. **Kiềm hóa:** Song song với lọc máu
    
    **Lọc máu:**
    - **Chế độ:** High-flux hemodialysis
    - **Thời gian:** 4-6 giờ hoặc đến khi level <30 mg/dL
    - **Theo dõi:** Level mỗi giờ
    
    **Tiên lượng:**
    - Tỷ lệ tử vong cao nếu không lọc máu
    - Cần điều trị tích cực ngay lập tức
    """)

