"""
Blood Pressure Management in Chronic Kidney Disease (CKD) Protocol
KDIGO 2021
Quản lý huyết áp trong bệnh thận mạn - KDIGO 2021
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Blood Pressure Management in CKD Protocol - KDIGO 2021"""
    st.subheader("📊 Quản Lý Huyết Áp Trong CKD (KDIGO 2021)")
    st.caption("KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease")
    
    st.info("""
    **KDIGO 2021 - Cập nhật quan trọng:**
    - Cập nhật từ KDIGO 2012 với bằng chứng mới
    - Phương pháp GRADE
    - Khuyến nghị cá nhân hóa
    
    **Mục tiêu huyết áp:**
    - <130/80 mmHg cho hầu hết bệnh nhân CKD
    - Điều chỉnh theo albumin niệu và nguy cơ tim mạch
    - <140/90 mmHg cho người cao tuổi hoặc không dung nạp
    """)
    
    st.markdown("---")
    
    # Patient information inputs
    col1, col2 = st.columns(2)
    
    with col1:
        ckd_stage = st.selectbox(
            "Giai đoạn CKD:",
            ["G1-G2", "G3a", "G3b", "G4", "G5 (không lọc máu)", "G5D (lọc máu)", "Ghép thận"],
            key="bp_ckd_stage"
        )
        
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²):",
            min_value=5.0,
            max_value=150.0,
            value=60.0,
            step=1.0,
            key="bp_ckd_egfr"
        )
    
    with col2:
        current_sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=80.0,
            max_value=250.0,
            value=140.0,
            step=5.0,
            key="bp_ckd_sbp"
        )
        
        current_dbp = st.number_input(
            "Huyết áp tâm trương (mmHg):",
            min_value=40.0,
            max_value=150.0,
            value=90.0,
            step=5.0,
            key="bp_ckd_dbp"
        )
    
    acr = st.number_input(
        "Albumin/Creatinine niệu - ACR (mg/g):",
        min_value=0.0,
        max_value=5000.0,
        value=0.0,
        step=10.0,
        key="bp_ckd_acr"
    )
    
    has_diabetes = st.checkbox("Có đái tháo đường?", key="bp_ckd_dm")
    is_elderly = st.checkbox("Người cao tuổi (>65 tuổi)?", key="bp_ckd_elderly")
    
    st.markdown("---")
    
    # Scenario selection
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🎯 Mục tiêu Huyết áp",
            "💊 Phác đồ Điều trị",
            "📈 Theo dõi & Điều chỉnh",
            "👥 Đặc biệt theo Nhóm Bệnh nhân"
        ],
        key="bp_ckd_scenario"
    )
    
    st.markdown("---")
    
    if "Mục tiêu" in scenario:
        render_targets(current_sbp, current_dbp, acr, has_diabetes, is_elderly, ckd_stage)
    elif "Phác đồ" in scenario:
        render_treatment_algorithm(current_sbp, current_dbp, acr, egfr, has_diabetes, ckd_stage)
    elif "Theo dõi" in scenario:
        render_monitoring(current_sbp, current_dbp, egfr)
    else:
        render_special_populations(acr, has_diabetes, is_elderly, ckd_stage)
    
    st.markdown("---")
    references = get_references("BP_CKD")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2026-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease**
           - Kidney Int. 2021;99(3S):S1-S87
           - Website: https://kdigo.org/guidelines/blood-pressure-in-ckd/
        
        2. **KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease**
           - Kidney Int Suppl. 2013;3(1):1-150
        
        3. **AHA/ACC 2017 Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults**
           - Circulation. 2018;138(17):e484-e594
        
        4. **UpToDate:** Management of hypertension in chronic kidney disease
           - Last updated: 2025
        """)


def render_targets(current_sbp, current_dbp, acr, has_diabetes, is_elderly, ckd_stage):
    """Blood pressure targets"""
    st.success("## 🎯 Mục tiêu Huyết áp")
    
    # Determine target based on patient characteristics
    has_albuminuria = acr >= 30
    has_cv_risk = has_diabetes or has_albuminuria or ckd_stage in ["G4", "G5 (không lọc máu)", "G5D (lọc máu)"]
    
    if is_elderly and not has_cv_risk:
        target_sbp = 140
        target_dbp = 90
        target_reason = "Người cao tuổi, không có nguy cơ tim mạch cao"
    elif has_albuminuria or has_diabetes or has_cv_risk:
        target_sbp = 130
        target_dbp = 80
        target_reason = "Có albumin niệu, đái tháo đường, hoặc nguy cơ tim mạch cao"
    else:
        target_sbp = 130
        target_dbp = 80
        target_reason = "Bệnh nhân CKD"
    
    st.markdown("### Mục tiêu Huyết áp theo KDIGO 2021")
    
    st.info(f"""
    **Mục tiêu: <{target_sbp}/{target_dbp} mmHg**
    
    **Lý do:** {target_reason}
    
    **Điều chỉnh:**
    - Người cao tuổi (>65 tuổi) hoặc không dung nạp: <140/90 mmHg có thể chấp nhận được
    - Cân nhắc cá nhân hóa theo tình trạng sức khỏe
    """)
    
    st.markdown("---")
    st.markdown("### Mục tiêu theo Albumin Niệu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### A2-A3 (ACR ≥30 mg/g)")
        st.success("""
        **Mục tiêu: <130/80 mmHg**
        
        **Lý do:**
        - Albumin niệu là yếu tố nguy cơ độc lập
        - Kiểm soát huyết áp làm chậm tiến triển CKD
        - Ưu tiên ACEi/ARB ở liều tối đa
        """)
    
    with col2:
        st.markdown("#### A1 (ACR <30 mg/g)")
        st.info("""
        **Mục tiêu:**
        - <130/80 mmHg (nếu có nguy cơ tim mạch)
        - <140/90 mmHg (nếu không có nguy cơ tim mạch)
        
        **Cân nhắc cá nhân hóa**
        """)
    
    st.markdown("---")
    st.markdown("### Đánh giá Tình Trạng Hiện Tại")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if current_sbp < target_sbp and current_dbp < target_dbp:
            st.success(f"**Huyết áp: {current_sbp}/{current_dbp} mmHg** - Đạt mục tiêu (<{target_sbp}/{target_dbp} mmHg)")
        elif current_sbp < target_sbp + 10 and current_dbp < target_dbp + 5:
            st.warning(f"**Huyết áp: {current_sbp}/{current_dbp} mmHg** - Gần mục tiêu, cần điều chỉnh")
        else:
            st.error(f"**Huyết áp: {current_sbp}/{current_dbp} mmHg** - Chưa đạt mục tiêu (<{target_sbp}/{target_dbp} mmHg)")
    
    with col2:
        if has_albuminuria:
            st.warning(f"**ACR: {acr} mg/g** - Có albumin niệu (mục tiêu <130/80 mmHg)")
        else:
            st.info(f"**ACR: {acr} mg/g** - Không có albumin niệu")


def render_treatment_algorithm(current_sbp, current_dbp, acr, egfr, has_diabetes, ckd_stage):
    """Treatment algorithm"""
    st.warning("## 💊 Phác đồ Điều trị")
    
    has_albuminuria = acr >= 30
    
    st.markdown("### Nguyên tắc Điều trị")
    
    st.info("""
    **Bước 1: Điều chỉnh Lối sống**
    - Giảm muối (<2-3 g/ngày)
    - Giảm cân nếu thừa cân/béo phì
    - Tập thể dục đều đặn
    - Hạn chế rượu
    - Bỏ thuốc lá
    """)
    
    st.markdown("---")
    st.markdown("### Phác đồ Thuốc")
    
    # Step 1: ACEi/ARB
    st.markdown("#### Bước 1: ACEi hoặc ARB")
    
    if has_albuminuria or has_diabetes:
        st.success("""
        **Chỉ định: ƯU TIÊN** (có albumin niệu hoặc đái tháo đường)
        
        **Lựa chọn:**
        - **ACEi:** Lisinopril, Enalapril, Ramipril, Perindopril
        - **ARB:** Losartan, Valsartan, Irbesartan, Telmisartan
        
        **Liều lượng:**
        - Bắt đầu liều thấp
        - Tăng dần đến liều tối đa dung nạp
        - Ví dụ: Lisinopril 10-40 mg/ngày, Losartan 50-100 mg/ngày
        
        **Lưu ý:**
        - Theo dõi creatinine và kali máu sau 1-2 tuần
        - Creatinine tăng <30% là chấp nhận được
        - Tránh nếu hẹp động mạch thận 2 bên
        """)
    else:
        st.info("""
        **Chỉ định:** Có thể dùng (không có albumin niệu)
        
        **Lựa chọn và liều:** Tương tự như trên
        """)
    
    # Step 2: CCB
    st.markdown("#### Bước 2: Thêm CCB (Calcium Channel Blocker)")
    
    st.info("""
    **Chỉ định:** Phối hợp với ACEi/ARB
    
    **Lựa chọn:**
    - **Dihydropyridine:** Amlodipine, Nifedipine (ưu tiên)
    - **Non-dihydropyridine:** Diltiazem, Verapamil (ít dùng trong CKD)
    
    **Liều lượng:**
    - Amlodipine: 5-10 mg/ngày
    - Nifedipine: 30-60 mg/ngày
    
    **Lưu ý:**
    - Có thể gây phù chân
    - Không làm chậm tiến triển CKD như ACEi/ARB
    """)
    
    # Step 3: Diuretic
    st.markdown("#### Bước 3: Thêm Lợi tiểu")
    
    if egfr >= 30:
        st.success("""
        **eGFR ≥30: Thiazide hoặc Thiazide-like**
        
        **Lựa chọn:**
        - **Hydrochlorothiazide:** 12.5-25 mg × 1-2 lần/ngày
        - **Chlorthalidone:** 12.5-25 mg/ngày (ưu tiên trong tăng huyết áp kháng trị)
        
        **Lưu ý:** Thiazide kém hiệu quả khi eGFR <30
        """)
    else:
        st.warning("""
        **eGFR <30: Loop diuretic**
        
        **Lựa chọn:**
        - **Furosemide:** 40-160 mg × 1-2 lần/ngày
        - **Torasemide:** 5-20 mg × 1-2 lần/ngày
        
        **Lưu ý:** Có thể cần liều cao ở CKD nặng
        """)
    
    st.markdown("---")
    st.markdown("### Phác đồ Phối hợp")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Phác đồ 2 thuốc")
        st.info("""
        - ACEi/ARB + CCB
        - ACEi/ARB + Thiazide (nếu eGFR ≥30)
        """)
        
        st.markdown("#### Phác đồ 3 thuốc")
        st.warning("""
        - ACEi/ARB + CCB + Thiazide/Loop diuretic
        
        **Chỉ định:** Khi phác đồ 2 thuốc không đạt mục tiêu
        """)
    
    with col2:
        st.markdown("#### Phác đồ 4 thuốc")
        st.error("""
        - ACEi/ARB + CCB + Lợi tiểu + MRA
        
        **Chỉ định:** Tăng huyết áp kháng trị
        
        **Xem protocol:** "Tăng Huyết Áp Kháng Trị Trong CKD"
        """)
    
    st.markdown("---")
    st.markdown("### Khuyến cáo Điều trị")
    
    if current_sbp >= 130 or current_dbp >= 80:
        if has_albuminuria or has_diabetes:
            st.success("**Khuyến cáo:** Bắt đầu với ACEi/ARB (ưu tiên), sau đó thêm CCB và lợi tiểu nếu cần")
        else:
            st.info("**Khuyến cáo:** Có thể bắt đầu với ACEi/ARB hoặc CCB, sau đó phối hợp")
    else:
        st.success("**Huyết áp đạt mục tiêu** - Tiếp tục điều trị hiện tại")


def render_monitoring(current_sbp, current_dbp, egfr):
    """Monitoring and adjustment"""
    st.success("## 📈 Theo dõi & Điều chỉnh")
    
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
        - Đo 2 lần sáng, 2 lần tối
        - Trong ít nhất 3-7 ngày
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
      (thường xuyên hơn khi dùng ACEi/ARB)
    
    **Cảnh báo:**
    - Creatinine tăng >30% sau khi bắt đầu ACEi/ARB: Đánh giá lại
    - Kali máu >5.0 mEq/L: Giảm liều hoặc ngừng ACEi/ARB
    - eGFR giảm nhanh: Đánh giá lại nguyên nhân
    """)
    
    st.markdown("---")
    st.markdown("### Điều chỉnh Điều trị")
    
    st.info("""
    **Khi huyết áp không đạt mục tiêu:**
    1. Đánh giá lại tuân thủ điều trị
    2. Đo huyết áp tại nhà để loại trừ white coat hypertension
    3. Tăng liều thuốc hiện tại đến liều tối đa
    4. Thêm thuốc thứ 2, thứ 3
    5. Cân nhắc thuốc bổ sung (MRA, beta-blocker)
    
    **Khi huyết áp quá thấp:**
    - Giảm liều hoặc ngừng một thuốc
    - Điều chỉnh theo triệu chứng
    - Đặc biệt cẩn thận ở người cao tuổi
    """)


def render_special_populations(acr, has_diabetes, is_elderly, ckd_stage):
    """Special populations"""
    st.success("## 👥 Đặc biệt theo Nhóm Bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Người cao tuổi (>65 tuổi)")
        st.info("""
        **Mục tiêu:**
        - <140/90 mmHg có thể chấp nhận được
        - Cân nhắc <130/80 mmHg nếu dung nạp tốt
        
        **Điều trị:**
        - Bắt đầu liều thấp
        - Tăng liều từ từ
        - Theo dõi hạ huyết áp tư thế đứng
        - Tránh hạ huyết áp quá mức
        """)
        
        st.markdown("### Đái tháo đường")
        st.warning("""
        **Mục tiêu:**
        - <130/80 mmHg
        
        **Điều trị:**
        - ACEi hoặc ARB là nền tảng
        - Phối hợp với CCB và lợi tiểu
        - SGLT2 inhibitors có thể giúp giảm huyết áp
        """)
    
    with col2:
        st.markdown("### Bệnh nhân Lọc máu")
        st.error("""
        **Mục tiêu:**
        - <140/90 mmHg trước lọc máu
        - Tránh hạ huyết áp sau lọc máu
        
        **Điều trị:**
        - Điều chỉnh dịch là chính
        - Thuốc hạ huyết áp điều chỉnh theo huyết áp giữa các lần lọc máu
        - Có thể cần giảm liều hoặc ngừng trước lọc máu
        """)
        
        st.markdown("### Ghép thận")
        st.success("""
        **Mục tiêu:**
        - <130/80 mmHg
        
        **Điều trị:**
        - ACEi/ARB có thể dùng sau ghép
        - Điều chỉnh theo chức năng thận ghép
        - Cân nhắc tương tác với thuốc ức chế miễn dịch
        """)
    
    st.markdown("---")
    st.markdown("### Điều chỉnh Lối sống")
    
    st.info("""
    **Giảm muối:**
    - <2-3 g muối/ngày (<5-6 g NaCl/ngày)
    - Giảm huyết áp 5-10 mmHg
    - Tăng hiệu quả thuốc hạ huyết áp
    
    **Giảm cân:**
    - Giảm 5-10% cân nặng nếu thừa cân/béo phì
    - BMI mục tiêu: 18.5-24.9 kg/m²
    
    **Tập thể dục:**
    - ≥150 phút/tuần tập thể dục vừa phải
    
    **Hạn chế rượu:**
    - Nam: ≤2 đơn vị/ngày
    - Nữ: ≤1 đơn vị/ngày
    """)
