"""
IgA Nephropathy Protocol
KDIGO 2021
Quản lý bệnh thận IgA - Nguyên nhân phổ biến nhất viêm cầu thận mạn tại Việt Nam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """IgA Nephropathy Protocol - KDIGO 2021"""
    st.subheader("🔬 IgA Nephropathy (Bệnh Thận IgA)")
    st.caption("KDIGO 2021 Clinical Practice Guideline for Glomerular Diseases - IgA Nephropathy")
    
    st.info("""
    **IgA Nephropathy:**
    - Nguyên nhân phổ biến nhất của viêm cầu thận mạn tính trên toàn thế giới
    - Phổ biến tại Việt Nam và châu Á
    - 20-40% bệnh nhân tiến triển đến suy thận mạn giai đoạn cuối trong 20 năm
    
    **KDIGO 2021 cập nhật:**
    - SGLT2 inhibitors cho bệnh nhân CKD với protein niệu
    - Điều trị ức chế miễn dịch cho bệnh nhân nguy cơ cao
    """)
    
    st.markdown("---")
    
    # Patient information inputs
    col1, col2 = st.columns(2)
    
    with col1:
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²):",
            min_value=5.0,
            max_value=150.0,
            value=60.0,
            step=1.0,
            key="igan_egfr"
        )
        
        proteinuria_24h = st.number_input(
            "Protein niệu 24h (g/24h):",
            min_value=0.0,
            max_value=20.0,
            value=1.5,
            step=0.1,
            key="igan_proteinuria"
        )
    
    with col2:
        acr = st.number_input(
            "ACR (mg/g):",
            min_value=0.0,
            max_value=5000.0,
            value=150.0,
            step=10.0,
            key="igan_acr"
        )
        
        current_sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=80.0,
            max_value=250.0,
            value=140.0,
            step=5.0,
            key="igan_sbp"
        )
    
    has_biopsy = st.checkbox("Đã sinh thiết thận?", key="igan_biopsy")
    mestc_score = st.selectbox(
        "MEST-C Score (nếu có sinh thiết):",
        ["Chưa có", "M0E0S0T0C0", "M1", "E1", "S1", "T1", "T2", "C1", "C2"],
        key="igan_mestc"
    )
    
    st.markdown("---")
    
    # Scenario selection
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Đánh giá",
            "💊 Điều trị Bảo tồn",
            "💉 Điều trị Ức chế Miễn dịch",
            "📊 Theo dõi & Tiên lượng"
        ],
        key="igan_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis(egfr, proteinuria_24h, acr, has_biopsy)
    elif "Bảo tồn" in scenario:
        render_supportive_care(egfr, proteinuria_24h, acr, current_sbp)
    elif "Miễn dịch" in scenario:
        render_immunosuppression(egfr, proteinuria_24h, acr)
    else:
        render_monitoring(egfr, proteinuria_24h, acr)
    
    st.markdown("---")
    references = get_references("IgA_Nephropathy")
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
        1. **KDIGO 2021 Clinical Practice Guideline for Glomerular Diseases - IgA Nephropathy**
           - Kidney Int. 2021;100(4S):S1-S276
           - Website: https://kdigo.org/guidelines/glomerular-diseases/
        
        2. **KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease**
           - Kidney Int. 2021;99(3S):S1-S87
        
        3. **UpToDate:** IgA nephropathy: Treatment and prognosis
           - Last updated: 2025
        """)


def render_diagnosis(egfr, proteinuria_24h, acr, has_biopsy):
    """Diagnosis and evaluation"""
    st.success("## 🔍 Chẩn đoán & Đánh giá")
    
    st.markdown("### Tiêu chuẩn Chẩn đoán")
    
    st.info("""
    **IgA Nephropathy khi có:**
    1. **Lắng đọng IgA trong cầu thận** (sinh thiết thận)
    2. **Hồng cầu niệu** (đại thể hoặc vi thể)
    3. **Protein niệu** (từ nhẹ đến nặng)
    4. **Loại trừ bệnh hệ thống:**
       - Lupus nephritis
       - ANCA vasculitis
       - Henoch-Schönlein purpura
    """)
    
    st.markdown("---")
    st.markdown("### Đánh giá Tình Trạng Hiện Tại")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if egfr >= 60:
            st.success(f"**eGFR: {egfr} mL/min/1.73m²** - Bình thường/nhẹ")
        elif egfr >= 30:
            st.warning(f"**eGFR: {egfr} mL/min/1.73m²** - Giảm trung bình")
        else:
            st.error(f"**eGFR: {egfr} mL/min/1.73m²** - Giảm nặng")
    
    with col2:
        if proteinuria_24h < 0.5:
            st.success(f"**Protein niệu: {proteinuria_24h} g/24h** - Nhẹ")
        elif proteinuria_24h < 1.0:
            st.warning(f"**Protein niệu: {proteinuria_24h} g/24h** - Trung bình")
        elif proteinuria_24h < 3.5:
            st.error(f"**Protein niệu: {proteinuria_24h} g/24h** - Nặng")
        else:
            st.error(f"**Protein niệu: {proteinuria_24h} g/24h** - Rất nặng (hội chứng thận hư)")
    
    with col3:
        if acr < 30:
            st.success(f"**ACR: {acr} mg/g** - Bình thường")
        elif acr < 100:
            st.warning(f"**ACR: {acr} mg/g** - Tăng nhẹ-trung bình")
        elif acr < 300:
            st.error(f"**ACR: {acr} mg/g** - Tăng trung bình-nặng")
        else:
            st.error(f"**ACR: {acr} mg/g** - Tăng rất nặng")
    
    st.markdown("---")
    st.markdown("### Chỉ định Sinh thiết Thận")
    
    if has_biopsy:
        st.success("**Đã sinh thiết thận** - Có thể xác định chẩn đoán và đánh giá tiên lượng")
    else:
        st.warning("""
        **Chỉ định sinh thiết khi:**
        - Protein niệu >1 g/24h kéo dài >3 tháng
        - eGFR giảm không giải thích được
        - Hồng cầu niệu đại thể tái phát
        - Nghi ngờ nguyên nhân khác
        
        **Lưu ý:** Hầu hết bệnh nhân không cần sinh thiết nếu lâm sàng điển hình
        """)
    
    st.markdown("---")
    st.markdown("### Xét nghiệm Cần Thiết")
    
    st.info("""
    **Xét nghiệm cơ bản:**
    - Phân tích nước tiểu (hồng cầu niệu, protein niệu)
    - Creatinine, eGFR
    - Điện giải (Na, K)
    - IgA huyết thanh (có thể tăng)
    - Bổ thể C3 (thường bình thường)
    
    **Loại trừ bệnh hệ thống:**
    - ANA, ANCA, anti-GBM
    - C3, C4 (nếu nghi ngờ lupus)
    """)


def render_supportive_care(egfr, proteinuria_24h, acr, current_sbp):
    """Supportive care treatment"""
    st.warning("## 💊 Điều trị Bảo tồn")
    
    has_proteinuria = proteinuria_24h >= 0.5 or acr >= 50
    
    st.markdown("### 1. ACEi hoặc ARB")
    
    if has_proteinuria:
        st.success("""
        **Chỉ định: ƯU TIÊN** (protein niệu ≥0.5 g/24h hoặc ACR ≥50 mg/g)
        
        **Lựa chọn:**
        - **ACEi:** Lisinopril, Enalapril, Ramipril
        - **ARB:** Losartan, Valsartan, Irbesartan
        
        **Liều lượng:**
        - Bắt đầu liều thấp
        - Tăng dần đến liều tối đa dung nạp
        - Ví dụ: Lisinopril 10-40 mg/ngày, Losartan 50-100 mg/ngày
        
        **Mục tiêu:**
        - Giảm protein niệu >30%
        - Hoặc protein niệu <1 g/24h
        - Huyết áp <130/80 mmHg
        
        **Lưu ý:**
        - Theo dõi creatinine và kali máu sau 1-2 tuần
        - Creatinine tăng <30% là chấp nhận được
        - Tiếp tục ngay cả khi eGFR giảm nhẹ
        """)
    else:
        st.info("**Chỉ định:** Có thể dùng nếu có tăng huyết áp")
    
    st.markdown("---")
    st.markdown("### 2. Kiểm soát Huyết áp")
    
    st.info("""
    **Mục tiêu:** <130/80 mmHg (KDIGO 2021)
    
    **Phác đồ:**
    - ACEi/ARB là nền tảng
    - Phối hợp với CCB hoặc lợi tiểu nếu cần
    - Xem protocol "Quản Lý Huyết Áp Trong CKD"
    """)
    
    if current_sbp >= 130:
        st.warning(f"**Huyết áp hiện tại: {current_sbp} mmHg** - Chưa đạt mục tiêu, cần điều chỉnh")
    
    st.markdown("---")
    st.markdown("### 3. SGLT2 Inhibitors (KDIGO 2021 - MỚI)")
    
    can_use_sglt2 = egfr >= 25 and (proteinuria_24h >= 0.2 or acr >= 200)
    
    if can_use_sglt2:
        st.success("""
        **Chỉ định:** CKD với protein niệu ≥200 mg/g (hoặc ≥200 mg/24h), eGFR ≥25
        
        **Lựa chọn:**
        - **Dapagliflozin:** 10 mg/ngày
        - **Empagliflozin:** 10-25 mg/ngày
        
        **Lợi ích:**
        - Làm chậm tiến triển CKD
        - Giảm protein niệu
        - Giảm nguy cơ tim mạch
        - Không phụ thuộc vào đái tháo đường
        
        **Lưu ý:**
        - Có thể dùng ở bệnh nhân không đái tháo đường
        - Có thể dùng kết hợp với ACEi/ARB
        - Theo dõi eGFR và thể tích dịch
        """)
    else:
        st.info(f"""
        **Chưa đủ điều kiện:**
        - eGFR: {egfr} mL/min/1.73m² (cần ≥25)
        - Protein niệu: {proteinuria_24h} g/24h hoặc ACR {acr} mg/g (cần ≥0.2 g/24h hoặc ≥200 mg/g)
        """)
    
    st.markdown("---")
    st.markdown("### 4. Điều chỉnh Lối sống")
    
    st.info("""
    **Giảm muối:**
    - <2-3 g muối/ngày
    - Giúp giảm huyết áp và protein niệu
    
    **Chế độ ăn:**
    - Protein: 0.8-1.0 g/kg/ngày (nếu eGFR >30)
    - Protein: 0.6-0.8 g/kg/ngày (nếu eGFR <30)
    - Chất lượng cao (thịt, cá, trứng)
    
    **Tập thể dục:**
    - Tập thể dục đều đặn
    - Tránh tập nặng khi có hồng cầu niệu đại thể
    """)


def render_immunosuppression(egfr, proteinuria_24h, acr):
    """Immunosuppressive treatment"""
    st.error("## 💉 Điều trị Ức chế Miễn dịch")
    
    # Determine indication
    has_indication = (proteinuria_24h >= 1.0 or acr >= 100) and egfr > 30
    
    st.markdown("### Chỉ định Điều trị Ức chế Miễn dịch")
    
    st.info("""
    **KDIGO 2021 khuyến cáo khi:**
    - Protein niệu ≥1 g/24h (hoặc ACR ≥100 mg/g) DÙ ĐÃ ĐIỀU TRỊ BẢO TỒN TỐI ĐA ≥3 tháng
    - eGFR >30 mL/min/1.73m²
    - Nguy cơ tiến triển cao
    """)
    
    if has_indication:
        st.success("**Có chỉ định điều trị ức chế miễn dịch**")
    else:
        st.warning(f"""
        **Chưa đủ điều kiện:**
        - Protein niệu: {proteinuria_24h} g/24h (cần ≥1.0 g/24h)
        - eGFR: {egfr} mL/min/1.73m² (cần >30)
        - Cần điều trị bảo tồn tối đa ≥3 tháng trước
        """)
    
    st.markdown("---")
    st.markdown("### Corticosteroid")
    
    if has_indication and egfr > 50:
        st.success("""
        **Chỉ định:** Bệnh nhân nguy cơ cao, eGFR >50
        
        **Phác đồ:**
        - **Prednisone:** 0.6-0.8 mg/kg/ngày (tối đa 60 mg/ngày) × 2-4 tháng
        - Sau đó giảm dần trong 4-6 tháng
        - Tổng thời gian: 6-9 tháng
        
        **Lưu ý:**
        - Chống chỉ định nếu eGFR <30 mL/min/1.73m²
        - Theo dõi tác dụng phụ: tăng đường huyết, nhiễm trùng, loãng xương
        - Cân nhắc dự phòng PCP nếu dùng liều cao kéo dài
        """)
    elif has_indication:
        st.warning("""
        **eGFR 30-50:** Cân nhắc cẩn thận, hiệu quả có thể kém hơn
        
        **Chống chỉ định nếu eGFR <30**
        """)
    
    st.markdown("---")
    st.markdown("### Điều trị Kết hợp")
    
    st.info("""
    **Corticosteroid + Cyclophosphamide:**
    - Chỉ định: Bệnh nhân nguy cơ rất cao, tiến triển nhanh
    - Cyclophosphamide: 1.5-2 mg/kg/ngày × 3-6 tháng
    - Sau đó chuyển sang Azathioprine hoặc Mycophenolate
    
    **Mycophenolate Mofetil (MMF):**
    - Có thể dùng thay thế corticosteroid ở một số bệnh nhân
    - Liều: 1-2 g/ngày
    - Cần nghiên cứu thêm
    """)
    
    st.markdown("---")
    st.markdown("### Chống chỉ định")
    
    st.error("""
    **Tránh điều trị ức chế miễn dịch khi:**
    - eGFR <30 mL/min/1.73m² (hiệu quả kém, nguy cơ cao)
    - Nhiễm trùng đang hoạt động
    - Loãng xương nặng không kiểm soát
    - Đái tháo đường không kiểm soát
    - Bệnh nhân không tuân thủ
    """)


def render_monitoring(egfr, proteinuria_24h, acr):
    """Monitoring and prognosis"""
    st.success("## 📊 Theo dõi & Tiên lượng")
    
    st.markdown("### Theo dõi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Protein Niệu")
        st.info("""
        **Tần suất:**
        - Mỗi 3-6 tháng khi ổn định
        - Thường xuyên hơn khi điều chỉnh điều trị
        
        **Mục tiêu:**
        - Giảm >30% hoặc <1 g/24h
        - Hoặc ACR <100 mg/g
        """)
        
        st.markdown("#### Chức năng Thận")
        st.info("""
        **Xét nghiệm:**
        - Creatinine, eGFR: Mỗi 3-6 tháng
        - Điện giải (Na, K): Mỗi 3-6 tháng
        
        **Cảnh báo:**
        - eGFR giảm >5 mL/min/1.73m²/năm: Đánh giá lại điều trị
        - Creatinine tăng >30% sau điều chỉnh: Đánh giá lại
        """)
    
    with col2:
        st.markdown("#### Huyết áp")
        st.info("""
        **Tần suất:**
        - Mỗi 1-3 tháng
        
        **Mục tiêu:**
        - <130/80 mmHg
        """)
        
        st.markdown("#### Đánh giá Tiến triển")
        st.success("""
        **Cải thiện:**
        - Protein niệu giảm
        - eGFR ổn định hoặc cải thiện
        - Huyết áp kiểm soát tốt
        
        **Tiến triển:**
        - Protein niệu tăng hoặc dai dẳng >1 g/24h
        - eGFR giảm nhanh
        - Cân nhắc điều trị ức chế miễn dịch
        """)
    
    st.markdown("---")
    st.markdown("### Yếu tố Tiên lượng")
    
    st.warning("""
    **Yếu tố tiên lượng xấu:**
    - Protein niệu >1 g/24h
    - Tăng huyết áp không kiểm soát
    - eGFR giảm tại thời điểm chẩn đoán
    - eGFR giảm nhanh (>5 mL/min/1.73m²/năm)
    - Mô bệnh học nặng (MEST-C score: T1-T2, C1-C2)
    
    **Tiên lượng:**
    - 20-40% bệnh nhân tiến triển đến suy thận mạn giai đoạn cuối trong 20 năm
    - Yếu tố quan trọng nhất: protein niệu và eGFR
    """)
