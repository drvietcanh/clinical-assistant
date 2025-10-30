"""
Preeclampsia Severity Classification
Phân loại mức độ nặng của tiền sản giật
"""

import streamlit as st


def render():
    """Render Preeclampsia Severity interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🤰 Preeclampsia Severity</h2>
    <p style='text-align: center;'><em>Phân loại mức độ nặng của Tiền sản giật</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin
    with st.expander("ℹ️ Giới thiệu về Preeclampsia"):
        st.markdown("""
        **Tiền sản giật (Preeclampsia)** là biến chứng thai nghén nghiêm trọng, đặc trưng bởi:
        - Tăng huyết áp (≥140/90 mmHg) sau 20 tuần thai
        - Protein niệu HOẶC tổn thương cơ quan đích
        
        **Phân loại:**
        - **Preeclampsia không nặng** (mild)
        - **Preeclampsia nặng** (severe) - Nguy hiểm mẹ và thai
        
        **Tầm quan trọng:**
        - Phân loại hướng dẫn điều trị và theo dõi
        - Quyết định thời điểm đình chỉ thai nghén
        - Preeclampsia nặng cần can thiệp KHẨN
        """)
    
    st.markdown("---")
    
    # Input
    st.subheader("📝 Đánh giá bệnh nhân")
    
    # Basic criteria
    st.markdown("### 1️⃣ Chẩn đoán cơ bản Preeclampsia:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bp_sys = st.number_input("HA tâm thu (mmHg)", 100, 250, 140, 1)
        bp_dia = st.number_input("HA tâm trương (mmHg)", 60, 150, 90, 1)
    
    with col2:
        gestational_age = st.number_input("Tuổi thai (tuần)", 20, 42, 32, 1)
        st.caption(f"Thai {gestational_age} tuần")
    
    proteinuria = st.checkbox(
        "Protein niệu (≥300 mg/24h hoặc dipstick ≥1+)",
        help="Một trong các tiêu chí chẩn đoán"
    )
    
    # Check basic diagnosis
    has_htn = (bp_sys >= 140) or (bp_dia >= 90)
    gestational_ok = gestational_age >= 20
    
    if not (has_htn and gestational_ok):
        st.warning("⚠️ Chưa đủ tiêu chí chẩn đoán Preeclampsia (cần THA sau 20 tuần)")
    
    st.markdown("---")
    
    # Severity features
    st.markdown("### 2️⃣ Đánh giá mức độ NẶNG:")
    
    st.info("**Preeclampsia NẶNG nếu có ≥1 tiêu chí sau:**")
    
    severe_features = []
    
    # Severe hypertension
    st.markdown("#### 🩺 Tăng huyết áp nặng:")
    severe_htn = st.checkbox(
        f"HA ≥ 160/110 mmHg (Hiện tại: {bp_sys}/{bp_dia})",
        value=(bp_sys >= 160 or bp_dia >= 110)
    )
    if severe_htn:
        severe_features.append("THA nặng (≥160/110)")
    
    st.markdown("---")
    
    # Symptoms
    st.markdown("#### 💭 Triệu chứng thần kinh:")
    
    headache = st.checkbox("Đau đầu dữ dội, dai dẳng, không đáp ứng điều trị")
    visual = st.checkbox("Rối loạn thị giác (nhìn mờ, chớp sáng, giảm thị lực)")
    
    if headache:
        severe_features.append("Đau đầu dữ dội")
    if visual:
        severe_features.append("Rối loạn thị giác")
    
    st.markdown("---")
    
    # Labs
    st.markdown("#### 🧪 Xét nghiệm:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        plt = st.number_input(
            "Tiểu cầu (×10³/µL)",
            min_value=0.0,
            max_value=500.0,
            value=200.0,
            step=10.0,
            help="Bình thường: 150-400"
        )
        plt_low = plt < 100
        if plt_low:
            st.error(f"⚠️ Giảm TC nặng")
            severe_features.append(f"Tiểu cầu < 100 ({plt})")
    
    with col2:
        creat = st.number_input(
            "Creatinine (µmol/L)",
            min_value=0.0,
            max_value=1000.0,
            value=60.0,
            step=5.0,
            help="Bình thường thai: 40-90 µmol/L"
        )
        creat_high = creat > 97  # >1.1 mg/dL
        if creat_high:
            st.error(f"⚠️ Suy thận")
            severe_features.append(f"Creatinine tăng ({creat} µmol/L)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        alt = st.number_input(
            "ALT/AST (U/L)",
            min_value=0,
            max_value=2000,
            value=25,
            step=5,
            help="Bình thường: < 40 U/L"
        )
        liver_enzymes = alt > 70  # 2x bình thường
        if liver_enzymes:
            st.error(f"⚠️ Tổn thương gan")
            severe_features.append(f"Men gan tăng (>2x BT)")
    
    with col2:
        ldh = st.number_input(
            "LDH (U/L)",
            min_value=0,
            max_value=2000,
            value=200,
            step=10,
            help="Bình thường: 140-280 U/L"
        )
    
    # Epigastric/RUQ pain
    epigastric_pain = st.checkbox(
        "Đau thượng vị / hạ sườn phải (gợi ý tổn thương gan)",
        help="Triệu chứng quan trọng, có thể tiến triển HELLP"
    )
    if epigastric_pain:
        severe_features.append("Đau thượng vị/hạ sườn phải")
    
    st.markdown("---")
    
    # Pulmonary edema
    st.markdown("#### 🫁 Phù phổi:")
    pulmonary_edema = st.checkbox(
        "Phù phổi (khó thở, ran ẩm, X-quang bất thường)",
        help="Dấu hiệu nghiêm trọng"
    )
    if pulmonary_edema:
        severe_features.append("Phù phổi")
    
    st.markdown("---")
    
    # Fetal concerns
    st.markdown("#### 👶 Thai nhi:")
    fetal_growth = st.checkbox(
        "Thai chậm phát triển trong tử cung (IUGR)",
        help="Liên quan đến suy nhau thai"
    )
    if fetal_growth:
        severe_features.append("Thai chậm phát triển (IUGR)")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Đánh giá mức độ nặng", type="primary", use_container_width=True):
        is_severe = len(severe_features) > 0
        
        # Results
        st.markdown("## 📊 Kết quả")
        
        if is_severe:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #dc354522 0%, #dc354544 100%); 
                        padding: 40px; border-radius: 15px; border-left: 5px solid #dc3545; margin: 20px 0;'>
                <h1 style='color: #dc3545; margin: 0; text-align: center; font-size: 2.5em;'>
                    🚨 PREECLAMPSIA NẶNG
                </h1>
                <p style='text-align: center; font-size: 1.2em; margin-top: 15px;'>
                    Có {len(severe_features)} dấu hiệu nặng
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### ⚠️ Dấu hiệu nặng:")
            for feature in severe_features:
                st.markdown(f"- ❌ {feature}")
            
            st.markdown("---")
            
            st.error("""
            ### 🚨 XỬ TRÍ KHẨN CẤP
            
            **1️⃣ NHẬP VIỆN NGAY - Theo dõi sát:**
            - Monitor HA liên tục
            - Monitor thai nhi (NST, BPP)
            - Xét nghiệm: CBC, CMP, LFT, LDH hàng ngày
            - Lượng nước tiểu 24h
            
            **2️⃣ Điều trị huyết áp:**
            - **Mục tiêu:** HA < 160/110 mmHg
            - **Thuốc lựa chọn:**
              - **Labetalol** IV: 20 mg → 40 → 80 mg q10min
              - **Hydralazine** IV: 5-10 mg q20min
              - **Nifedipine** ngậm: 10 mg q20min
            - ⚠️ TRÁNH giảm HA quá nhanh (ảnh hưởng tưới máu thai)
            
            **3️⃣ Dự phòng co giật:**
            - **Magnesium sulfate** (MgSO₄):
              - Loading: 4-6 g IV trong 15-20 phút
              - Maintenance: 2 g/h IV
              - Theo dõi: phản xạ gân xương, nhịp thở, nước tiểu
              - Ngừng nếu: phản xạ gân xương mất, RR < 12, UOP < 100 mL/4h
            
            **4️⃣ Corticosteroids (nếu thai < 34 tuần):**
            - **Betamethasone** 12 mg IM x 2 liều cách 24h
            - HOẶC **Dexamethasone** 6 mg IM q12h x 4 liều
            - Mục đích: Trưởng thành phổi thai
            
            **5️⃣ Quyết định đình chỉ thai nghén:**
            
            **Chỉ định ĐÌNH CHỈ NGAY:**
            - Thai ≥ 34 tuần
            - Eclampsia (co giật)
            - HELLP syndrome
            - DIC
            - Suy nhau thai cấp
            - Suy thai cấp (NST category II/III dai dẳng)
            - Phù phổi
            - Suy thận cấp
            - Xuất huyết võng mạc/phù gai thị
            - Rau bong non
            
            **Có thể kéo dài nếu:**
            - Thai < 34 tuần + ổn định
            - Không tiêu chí đình chỉ khẩn cấp
            - Theo dõi sát tại viện
            - Đã tiêm corticosteroid
            
            **6️⃣ Theo dõi sau sanh:**
            - Tiếp tục MgSO₄ 24-48h
            - Monitor HA chặt
            - Theo dõi biến chứng: co giật, HELLP, DIC
            """)
        
        else:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #ffc10722 0%, #ffc10744 100%); 
                        padding: 40px; border-radius: 15px; border-left: 5px solid #ffc107; margin: 20px 0;'>
                <h1 style='color: #ff8800; margin: 0; text-align: center; font-size: 2.5em;'>
                    ⚠️ PREECLAMPSIA KHÔNG NẶNG
                </h1>
                <p style='text-align: center; font-size: 1.2em; margin-top: 15px;'>
                    Không có dấu hiệu nặng
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.warning("""
            ### ⚠️ XỬ TRÍ
            
            **1️⃣ Nhập viện hoặc theo dõi ngoại trú:**
            - **Nếu thai < 37 tuần:** Nhập viện quan sát
            - **Nếu thai ≥ 37 tuần:** Cân nhắc đình chỉ thai
            - Theo dõi ngoại trú nếu ổn định + tuân thủ tốt
            
            **2️⃣ Theo dõi:**
            - **HA:** 2 lần/ngày tại nhà hoặc hàng ngày tại viện
            - **Xét nghiệm:** 2 lần/tuần (CBC, CMP, LFT)
            - **Thai nhi:** NST 2 lần/tuần, siêu âm 1-2 lần/tuần
            - **Triệu chứng:** Hướng dẫn nhận biết dấu hiệu nặng
            
            **3️⃣ KHÔNG cần:**
            - Điều trị huyết áp (trừ khi HA ≥ 160/110)
            - Magnesium sulfate dự phòng
            - Hạn chế hoạt động nghiêm ngặt
            
            **4️⃣ Quyết định đình chỉ thai:**
            - **Thai ≥ 37 tuần:** Đình chỉ thai ngay
            - **Thai < 37 tuần:** Kéo dài đến 37 tuần nếu ổn định
            - Tiêm corticosteroid nếu thai < 34 tuần
            
            **5️⃣ Tái khám NGAY nếu:**
            - HA ≥ 160/110
            - Đau đầu dữ dội
            - Rối loạn thị giác
            - Đau thượng vị/hạ sườn phải
            - Khó thở
            - Giảm cử động thai
            """)
        
        # HELLP syndrome check
        st.markdown("---")
        st.markdown("### 🔴 Đánh giá HELLP Syndrome:")
        
        hellp_features = []
        if plt < 100:
            hellp_features.append("Thrombocytopenia")
        if alt > 70 or liver_enzymes:
            hellp_features.append("Elevated Liver enzymes")
        if ldh > 600:
            hellp_features.append("Hemolysis (LDH cao)")
        
        if len(hellp_features) >= 2:
            st.error(f"""
            **⚠️ NGHI NGỜ HELLP SYNDROME!**
            
            Có {len(hellp_features)}/3 tiêu chí: {', '.join(hellp_features)}
            
            **HELLP = Biến chứng NGUY HIỂM của preeclampsia:**
            - **H**emolysis (Tan máu)
            - **E**levated **L**iver enzymes
            - **L**ow **P**latelets
            
            **Xử trí:**
            - 🚨 Cấp cứu sản khoa NGAY
            - Đình chỉ thai nghén BẤT KỂ tuổi thai
            - Điều trị hỗ trợ: truyền TC, điều chỉnh đông máu
            - Biến chứng: vỡ gan, DIC, suy đa cơ quan
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **ACOG Practice Bulletin No. 202:** Gestational Hypertension and Preeclampsia. 
               *Obstet Gynecol.* 2019;133(1):e1-e25.
            
            2. **Magee LA, et al.** The 2021 International Society for the Study of Hypertension in Pregnancy classification, diagnosis & management recommendations for international practice. 
               *Pregnancy Hypertens.* 2022;27:148-169.
            
            3. **Sibai BM.** Diagnosis, controversies, and management of the syndrome of hemolysis, elevated liver enzymes, and low platelet count. 
               *Obstet Gynecol.* 2004;103(5 Pt 1):981-91.
            """)
    
    # Quick reference
    st.markdown("---")
    st.info("""
    💡 **Tiêu chí Preeclampsia NẶNG (có ≥1):**
    
    **Huyết áp:**
    - HA ≥ 160/110 mmHg
    
    **Triệu chứng:**
    - Đau đầu dữ dội dai dẳng
    - Rối loạn thị giác
    - Đau thượng vị/hạ sườn phải
    
    **Xét nghiệm:**
    - Tiểu cầu < 100,000
    - Creatinine > 1.1 mg/dL (>97 µmol/L)
    - Men gan > 2x bình thường
    
    **Cơ quan:**
    - Phù phổi
    - Thai chậm phát triển (IUGR)
    
    ⚠️ **Preeclampsia nặng = CẦN can thiệp tích cực!**
    """)


if __name__ == "__main__":
    render()

