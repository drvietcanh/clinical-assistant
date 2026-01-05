"""
Resistant Hypertension in Chronic Kidney Disease (CKD) Protocol
Clinical Kidney Journal 2025, KDIGO Blood Pressure Guidelines
Điều trị tăng huyết áp kháng trị trong bệnh thận mạn
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Resistant Hypertension in CKD Protocol"""
    st.subheader("💊 Tăng Huyết Áp Kháng Trị Trong CKD")
    st.caption("Clinical Kidney Journal 2025, KDIGO Blood Pressure Guidelines - Điều trị tăng huyết áp kháng trị")
    
    st.info("""
    **Định nghĩa tăng huyết áp kháng trị:**
    - Huyết áp ≥140/90 mmHg (hoặc ≥130/80 mmHg nếu có albumin niệu) DÙ ĐÃ DÙNG
    - ≥3 thuốc hạ huyết áp ở liều tối đa (bao gồm lợi tiểu) HOẶC
    - Huyết áp đạt mục tiêu nhưng cần ≥4 thuốc hạ huyết áp
    
    **Tỷ lệ:** 20-30% bệnh nhân CKD, tăng theo mức độ suy thận
    """)
    
    st.markdown("---")
    
    # Patient information inputs
    col1, col2 = st.columns(2)
    
    with col1:
        ckd_stage = st.selectbox(
            "Giai đoạn CKD:",
            ["G1-G2", "G3a", "G3b", "G4", "G5 (không lọc máu)", "G5D (lọc máu)"],
            key="resistant_htn_stage"
        )
        
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²):",
            min_value=5.0,
            max_value=150.0,
            value=45.0,
            step=1.0,
            key="resistant_htn_egfr"
        )
    
    with col2:
        current_sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=80.0,
            max_value=250.0,
            value=150.0,
            step=5.0,
            key="resistant_htn_sbp"
        )
        
        current_dbp = st.number_input(
            "Huyết áp tâm trương (mmHg):",
            min_value=40.0,
            max_value=150.0,
            value=95.0,
            step=5.0,
            key="resistant_htn_dbp"
        )
    
    num_medications = st.number_input(
        "Số thuốc hạ huyết áp đang dùng:",
        min_value=0,
        max_value=10,
        value=3,
        step=1,
        key="resistant_htn_meds"
    )
    
    potassium = st.number_input(
        "Kali máu (mEq/L):",
        min_value=2.0,
        max_value=7.0,
        value=4.2,
        step=0.1,
        key="resistant_htn_k"
    )
    
    st.markdown("---")
    
    # Scenario selection
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Đánh giá",
            "💊 Phác đồ Điều trị",
            "👥 Điều chỉnh theo eGFR",
            "📊 Theo dõi & Điều chỉnh"
        ],
        key="resistant_htn_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis(current_sbp, current_dbp, num_medications, ckd_stage)
    elif "Phác đồ" in scenario:
        render_medication_algorithm(current_sbp, current_dbp, num_medications, egfr, potassium, ckd_stage)
    elif "Điều chỉnh" in scenario:
        render_special_populations(egfr, potassium, ckd_stage)
    else:
        render_monitoring(current_sbp, current_dbp, egfr, potassium)
    
    st.markdown("---")
    references = get_references("Resistant_HTN_CKD")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2025-12-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **Clinical Kidney Journal 2025:** "2025 Update on resistant hypertension in CKD: where do we stand and where do we go?"
           - DOI: 10.1093/ckj/sfaf285
        
        2. **KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease**
           - Kidney Int. 2021;99(3S):S1-S87
        
        3. **AHA/ACC 2017 Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults**
           - Circulation. 2018;138(17):e484-e594
        
        4. **UpToDate:** Resistant hypertension
           - Last updated: 2025
        """)


def render_diagnosis(current_sbp, current_dbp, num_medications, ckd_stage):
    """Diagnosis and evaluation"""
    st.success("## 🔍 Chẩn đoán & Đánh giá")
    
    # Determine if resistant hypertension
    has_albuminuria = st.checkbox("Có albumin niệu/protein niệu?", key="resistant_htn_albuminuria")
    
    target_bp = 130 if has_albuminuria else 140
    target_dbp = 80
    
    is_resistant = (current_sbp >= target_bp or current_dbp >= target_dbp) and num_medications >= 3
    
    st.markdown("### Tiêu chuẩn Chẩn đoán")
    
    st.info("""
    **Tăng huyết áp kháng trị khi:**
    - Huyết áp ≥140/90 mmHg (hoặc ≥130/80 mmHg nếu có albumin niệu) DÙ ĐÃ DÙNG
    - ≥3 thuốc hạ huyết áp ở liều tối đa (bao gồm lợi tiểu) HOẶC
    - Huyết áp đạt mục tiêu nhưng cần ≥4 thuốc hạ huyết áp
    """)
    
    st.markdown("---")
    st.markdown("### Đánh giá Tình Trạng Hiện Tại")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if current_sbp >= target_bp or current_dbp >= target_dbp:
            st.error(f"**Huyết áp: {current_sbp}/{current_dbp} mmHg** - Chưa đạt mục tiêu (mục tiêu: <{target_bp}/{target_dbp} mmHg)")
        else:
            st.success(f"**Huyết áp: {current_sbp}/{current_dbp} mmHg** - Đạt mục tiêu")
    
    with col2:
        if num_medications >= 3:
            st.warning(f"**Số thuốc: {num_medications}** - Đủ tiêu chuẩn tăng huyết áp kháng trị")
        else:
            st.info(f"**Số thuốc: {num_medications}** - Chưa đủ tiêu chuẩn (cần ≥3 thuốc)")
    
    if is_resistant:
        st.error("**Chẩn đoán: Tăng huyết áp kháng trị**")
    else:
        st.info("**Chưa đủ tiêu chuẩn tăng huyết áp kháng trị**")
    
    st.markdown("---")
    st.markdown("### Đánh giá Nguyên nhân")
    
    st.warning("""
    **1. Tuân thủ kém:**
    - Đánh giá số lượng thuốc đang dùng
    - Liều lượng và tần suất
    - Tác dụng phụ
    - Chi phí và khả năng tiếp cận
    
    **2. White coat hypertension:**
    - Đo huyết áp tại nhà (HBPM)
    - ABPM nếu cần
    
    **3. Nguyên nhân thứ phát:**
    - Hẹp động mạch thận
    - Cường aldosterone nguyên phát
    - Hội chứng Cushing
    - U tủy thượng thận
    - Bệnh thận đa nang
    
    **4. Thuốc gây tăng huyết áp:**
    - NSAID
    - Corticosteroid
    - Thuốc tránh thai
    - Decongestant
    
    **5. Yếu tố lối sống:**
    - Ăn nhiều muối
    - Uống rượu nhiều
    - Béo phì
    - Thiếu vận động
    """)
    
    st.markdown("---")
    st.markdown("### Xét nghiệm Cần Thiết")
    
    st.info("""
    **Xét nghiệm cơ bản:**
    - Creatinine, eGFR
    - Điện giải (Na, K)
    - Aldosterone, renin (nếu nghi ngờ cường aldosterone)
    - Cortisol (nếu nghi ngờ Cushing)
    - Catecholamine (nếu nghi ngờ pheochromocytoma)
    
    **Hình ảnh:**
    - Siêu âm thận
    - CT/MRA thận (nếu nghi ngờ hẹp động mạch thận)
    - Siêu âm tuyến thượng thận (nếu nghi ngờ u)
    """)


def render_medication_algorithm(current_sbp, current_dbp, num_medications, egfr, potassium, ckd_stage):
    """Medication algorithm"""
    st.warning("## 💊 Phác đồ Điều trị")
    
    st.markdown("### Mục tiêu Huyết áp")
    
    has_albuminuria = st.checkbox("Có albumin niệu/protein niệu?", key="resistant_htn_albuminuria_alg")
    is_elderly = st.checkbox("Người cao tuổi (>65 tuổi) hoặc không dung nạp?", key="resistant_htn_elderly")
    
    if has_albuminuria:
        target_bp = 130
        target_dbp = 80
    elif is_elderly:
        target_bp = 140
        target_dbp = 90
    else:
        target_bp = 130
        target_dbp = 80
    
    st.success(f"**Mục tiêu huyết áp: <{target_bp}/{target_dbp} mmHg**")
    
    st.markdown("---")
    st.markdown("### Phác đồ Điều trị Từng Bước")
    
    # Step 1
    st.markdown("#### Bước 1: ACEi hoặc ARB")
    st.info("""
    **Chỉ định:** Ưu tiên nếu có albumin niệu hoặc protein niệu
    
    **Lựa chọn:**
    - **ACEi:** Lisinopril, Enalapril, Ramipril, Perindopril
    - **ARB:** Losartan, Valsartan, Irbesartan, Telmisartan
    
    **Liều:** Bắt đầu liều thấp, tăng dần đến liều tối đa
    
    **Lưu ý:** Theo dõi creatinine và kali máu
    """)
    
    # Step 2
    st.markdown("#### Bước 2: Thêm CCB (Calcium Channel Blocker)")
    st.info("""
    **Lựa chọn:** Amlodipine hoặc Nifedipine (dihydropyridine)
    
    **Liều:** Bắt đầu liều thấp, tăng dần đến liều tối đa
    
    **Lưu ý:** Có thể gây phù chân
    """)
    
    # Step 3
    st.markdown("#### Bước 3: Thêm Lợi tiểu")
    
    if egfr >= 30:
        st.success("""
        **eGFR ≥30: Thiazide hoặc Thiazide-like**
        - **Hydrochlorothiazide:** 12.5-25 mg × 1-2 lần/ngày
        - **Chlorthalidone:** 12.5-25 mg/ngày (ưu tiên trong tăng huyết áp kháng trị)
        
        **Lưu ý:** Chlorthalidone có thể hiệu quả hơn hydrochlorothiazide
        """)
    else:
        st.warning("""
        **eGFR <30: Loop diuretic**
        - **Furosemide:** 40-160 mg × 1-2 lần/ngày
        - **Torasemide:** 5-20 mg × 1-2 lần/ngày
        
        **Lưu ý:** Có thể cần liều cao hơn
        """)
    
    # Step 4
    st.markdown("#### Bước 4: Thêm MRA (Mineralocorticoid Receptor Antagonist)")
    
    can_use_mra = egfr >= 30 and potassium < 4.5
    
    if can_use_mra:
        st.success("""
        **Chỉ định:** eGFR ≥30, kali máu <4.5 mEq/L
        
        **Spironolactone:**
        - Liều: 12.5-25 mg/ngày, có thể tăng đến 50 mg/ngày
        - Tác dụng phụ: tăng kali máu, gynecomastia (nam giới)
        
        **Eplerenone:**
        - Liều: 25-50 mg × 2 lần/ngày
        - Ưu điểm: Ít tác dụng phụ nội tiết hơn spironolactone
        
        **Lưu ý:** Rất hiệu quả trong tăng huyết áp kháng trị. Theo dõi kali máu thường xuyên (mỗi 1-2 tuần khi bắt đầu).
        """)
    else:
        st.error(f"""
        **Chống chỉ định MRA:**
        - eGFR <30: {egfr} mL/min/1.73m²
        - Kali máu ≥4.5 mEq/L: {potassium} mEq/L
        
        **Khuyến cáo:** Tối ưu hóa các thuốc khác trước
        """)
    
    # Step 5
    st.markdown("#### Bước 5: Tối ưu hóa Lợi tiểu")
    
    if egfr >= 30:
        st.info("""
        **Cân nhắc chuyển sang Chlorthalidone:**
        - Tác dụng kéo dài hơn hydrochlorothiazide
        - Có thể hiệu quả hơn trong tăng huyết áp kháng trị
        - Liều: 12.5-25 mg/ngày
        """)
    else:
        st.info("""
        **Tăng liều Loop diuretic:**
        - Furosemide: Có thể cần đến 160-240 mg/ngày
        - Torasemide: Có thể cần đến 20-40 mg/ngày
        - Chia liều 2 lần/ngày nếu cần
        """)
    
    # Step 6
    st.markdown("#### Bước 6: Thuốc Bổ sung")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Beta-blocker:**")
        st.info("""
        Chỉ định: Suy tim, nhịp nhanh, sau nhồi máu cơ tim
        
        Lựa chọn:
        - Metoprolol
        - Bisoprolol
        - Carvedilol
        """)
        
        st.markdown("**Alpha-blocker:**")
        st.info("""
        Chỉ định: Phì đại tuyến tiền liệt
        
        Lựa chọn:
        - Doxazosin
        - Terazosin
        """)
    
    with col2:
        st.markdown("**Hydralazine:**")
        st.info("""
        Chỉ định: Tăng huyết áp kháng trị, suy tim
        
        Liều: 25-100 mg × 2-3 lần/ngày
        
        Lưu ý: Có thể gây nhịp nhanh phản xạ
        """)
        
        st.markdown("**Minoxidil:**")
        st.warning("""
        Chỉ định: Tăng huyết áp kháng trị nặng
        
        Liều: 5-40 mg/ngày
        
        Lưu ý: Tác dụng phụ nặng (phù, tăng nhịp tim, hirsutism)
        """)
    
    st.markdown("---")
    st.markdown("### Khuyến cáo Điều trị")
    
    if current_sbp >= target_bp or current_dbp >= target_dbp:
        if num_medications < 3:
            st.warning(f"**Khuyến cáo:** Bắt đầu hoặc tăng liều thuốc để đạt ≥3 thuốc ở liều tối đa")
        elif num_medications == 3:
            if can_use_mra:
                st.success("**Khuyến cáo:** Thêm MRA (Spironolactone hoặc Eplerenone)")
            else:
                st.warning("**Khuyến cáo:** Tối ưu hóa lợi tiểu và cân nhắc thuốc bổ sung")
        else:
            st.info("**Khuyến cáo:** Đánh giá lại tuân thủ và cân nhắc điều chỉnh lối sống")


def render_special_populations(egfr, potassium, ckd_stage):
    """Special populations based on eGFR"""
    st.success("## 👥 Điều chỉnh theo eGFR")
    
    st.markdown("### Điều chỉnh Thuốc theo Giai đoạn CKD")
    
    if egfr >= 45:
        st.info("""
        **CKD G1-G3a (eGFR ≥45):**
        - Có thể dùng tất cả các thuốc
        - Thiazide/Thiazide-like hiệu quả
        - MRA có thể dùng nếu kali máu <4.5 mEq/L
        """)
    elif egfr >= 30:
        st.warning("""
        **CKD G3b (eGFR 30-44):**
        - Thiazide kém hiệu quả, cân nhắc loop diuretic
        - MRA có thể dùng nếu kali máu <4.5 mEq/L
        - Theo dõi creatinine và kali máu thường xuyên
        """)
    elif egfr >= 15:
        st.error("""
        **CKD G4 (eGFR 15-29):**
        - Loop diuretic (có thể cần liều cao)
        - Tránh MRA nếu kali máu ≥4.5 mEq/L
        - Theo dõi creatinine và kali máu thường xuyên
        """)
    else:
        st.error("""
        **CKD G5 (eGFR <15, không lọc máu):**
        - Loop diuretic (có thể cần liều cao)
        - Tránh MRA nếu kali máu ≥4.5 mEq/L
        - Cân nhắc lọc máu nếu quá tải dịch không kiểm soát
        """)
    
    st.markdown("---")
    st.markdown("### Bệnh nhân Lọc máu (CKD G5D)")
    
    st.info("""
    **Điều trị:**
    - Điều chỉnh dịch là chính
    - Thuốc hạ huyết áp điều chỉnh theo huyết áp giữa các lần lọc máu
    - Tránh MRA nếu kali máu cao
    
    **Mục tiêu:**
    - Huyết áp trước lọc máu: <160/90 mmHg
    - Huyết áp sau lọc máu: Tránh hạ huyết áp
    """)
    
    st.markdown("---")
    st.markdown("### Điều chỉnh Lối sống")
    
    st.success("""
    **Giảm muối:**
    - <2-3 g muối/ngày (<5-6 g NaCl/ngày)
    - Giảm huyết áp 5-10 mmHg
    
    **Giảm cân:**
    - Giảm 5-10% cân nặng nếu thừa cân/béo phì
    - BMI mục tiêu: 18.5-24.9 kg/m²
    
    **Tập thể dục:**
    - ≥150 phút/tuần tập thể dục vừa phải
    
    **Hạn chế rượu:**
    - Nam: ≤2 đơn vị/ngày
    - Nữ: ≤1 đơn vị/ngày
    """)


def render_monitoring(current_sbp, current_dbp, egfr, potassium):
    """Monitoring and adjustment"""
    st.success("## 📊 Theo dõi & Điều chỉnh")
    
    st.markdown("### Theo dõi Huyết áp")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Tần suất")
        st.info("""
        **Khi điều chỉnh liều:**
        - Mỗi 1-2 tuần
        
        **Khi ổn định:**
        - Mỗi 1-3 tháng
        
        **Đo tại nhà:**
        - Khuyến khích để đánh giá hiệu quả
        """)
    
    with col2:
        st.markdown("#### Mục tiêu")
        st.success("""
        **Huyết áp tại phòng khám:**
        - <130/80 mmHg (nếu có albumin niệu)
        - <140/90 mmHg (người cao tuổi)
        
        **Huyết áp tại nhà:**
        - <125/75 mmHg
        - Hoặc <130/80 mmHg
        """)
    
    st.markdown("---")
    st.markdown("### Theo dõi Chức năng Thận")
    
    st.warning("""
    **Xét nghiệm:**
    - Creatinine, eGFR: Mỗi 3-6 tháng
    - Điện giải (Na, K): Mỗi 1-3 tháng
      (thường xuyên hơn khi dùng MRA hoặc ACEi/ARB)
    
    **Cảnh báo:**
    - Creatinine tăng >30% sau khi bắt đầu ACEi/ARB: Có thể chấp nhận được nếu ổn định
    - Kali máu >5.0 mEq/L: Giảm liều hoặc ngừng MRA, ACEi/ARB
    - eGFR giảm nhanh: Đánh giá lại nguyên nhân
    """)
    
    st.markdown("---")
    st.markdown("### Điều chỉnh Điều trị")
    
    st.info("""
    **Khi huyết áp không đạt mục tiêu:**
    1. Đánh giá lại tuân thủ
    2. Đo huyết áp tại nhà để loại trừ white coat hypertension
    3. Tối ưu hóa lợi tiểu (cân nhắc chlorthalidone, tăng liều loop diuretic)
    4. Thêm MRA (nếu chưa dùng và không chống chỉ định)
    5. Thêm thuốc bổ sung (beta-blocker, alpha-blocker)
    
    **Khi huyết áp quá thấp:**
    - Giảm liều hoặc ngừng một thuốc
    - Điều chỉnh theo triệu chứng
    """)
    
    st.markdown("---")
    st.markdown("### Đánh giá Hiện Tại")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Chức năng Thận")
        if egfr >= 60:
            st.success(f"**eGFR: {egfr} mL/min/1.73m²** - Bình thường/nhẹ")
        elif egfr >= 45:
            st.info(f"**eGFR: {egfr} mL/min/1.73m²** - Giảm nhẹ-trung bình")
        elif egfr >= 30:
            st.warning(f"**eGFR: {egfr} mL/min/1.73m²** - Giảm trung bình-nặng")
        else:
            st.error(f"**eGFR: {egfr} mL/min/1.73m²** - Giảm nặng")
    
    with col2:
        st.markdown("#### Kali máu")
        if potassium < 3.5:
            st.error(f"**Kali: {potassium} mEq/L** - Hạ kali máu")
        elif potassium < 4.5:
            st.success(f"**Kali: {potassium} mEq/L** - Bình thường (có thể dùng MRA)")
        elif potassium < 5.0:
            st.warning(f"**Kali: {potassium} mEq/L** - Tăng nhẹ (thận trọng với MRA)")
        else:
            st.error(f"**Kali: {potassium} mEq/L** - Tăng (tránh MRA, ACEi/ARB)")
