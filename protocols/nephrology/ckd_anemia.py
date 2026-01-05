"""
Anemia in Chronic Kidney Disease (CKD) Protocol
KDIGO 2026
Điều trị thiếu máu trong bệnh thận mạn - KDIGO 2026
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Anemia in CKD Protocol - KDIGO 2026"""
    st.subheader("🩸 Thiếu Máu Trong CKD (KDIGO 2026)")
    st.caption("KDIGO 2026 Clinical Practice Guideline for Anemia in Chronic Kidney Disease - Cập nhật từ KDIGO 2012")
    
    st.info("""
    **KDIGO 2026 - Cập nhật quan trọng:**
    - Cập nhật từ KDIGO 2012 với hơn một thập kỷ bằng chứng mới
    - Phương pháp nghiêm ngặt với GRADE
    - Tiếp cận cá nhân hóa điều trị
    - Bao gồm người lớn, trẻ em, bệnh nhân lọc máu và ghép thận
    
    **Thiếu máu trong CKD:**
    - Biến chứng phổ biến và gánh nặng
    - Liên quan đến giảm chất lượng cuộc sống, tăng nguy cơ tim mạch
    - Cần đánh giá và điều trị hệ thống
    """)
    
    st.markdown("---")
    
    # Patient information inputs
    col1, col2 = st.columns(2)
    
    with col1:
        ckd_stage = st.selectbox(
            "Giai đoạn CKD:",
            ["G1-G2", "G3a", "G3b", "G4", "G5 (không lọc máu)", "G5D (lọc máu)", "Ghép thận"],
            key="ckd_anemia_stage"
        )
        
        dialysis_status = st.radio(
            "Tình trạng lọc máu:",
            ["Không lọc máu", "Lọc máu chu kỳ", "Lọc màng bụng"],
            key="ckd_anemia_dialysis"
        )
    
    with col2:
        current_hb = st.number_input(
            "Hemoglobin hiện tại (g/dL):",
            min_value=5.0,
            max_value=20.0,
            value=9.0,
            step=0.1,
            key="ckd_anemia_hb"
        )
        
        tsat = st.number_input(
            "TSAT (%):",
            min_value=0.0,
            max_value=100.0,
            value=15.0,
            step=1.0,
            key="ckd_anemia_tsat"
        )
    
    ferritin = st.number_input(
        "Ferritin (ng/mL):",
        min_value=0.0,
        max_value=2000.0,
        value=50.0,
        step=10.0,
        key="ckd_anemia_ferritin"
    )
    
    st.markdown("---")
    
    # Scenario selection
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Đánh giá",
            "💊 Điều trị thiếu sắt",
            "💉 Điều trị ESA",
            "🆕 Điều trị HIF-PHI",
            "📊 Theo dõi & Điều chỉnh"
        ],
        key="ckd_anemia_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis(current_hb, tsat, ferritin, ckd_stage, dialysis_status)
    elif "thiếu sắt" in scenario:
        render_iron_therapy(tsat, ferritin, ckd_stage, dialysis_status)
    elif "ESA" in scenario:
        render_esa_therapy(current_hb, tsat, ferritin, ckd_stage, dialysis_status)
    elif "HIF-PHI" in scenario:
        render_hif_phi_therapy(current_hb, tsat, ferritin, ckd_stage, dialysis_status)
    else:
        render_monitoring(current_hb, tsat, ferritin, ckd_stage, dialysis_status)
    
    st.markdown("---")
    references = get_references("CKD_Anemia")
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
        1. **KDIGO 2026 Clinical Practice Guideline for Anemia in Chronic Kidney Disease**
           - Website: https://kdigo.org/guidelines/anemia-in-ckd/
           - Co-chairs: Jodie Babitt, MD (United States), Marcello Tonelli, MD, SM, MSc, FRCPC (Canada)
        
        2. **KDIGO 2012 Clinical Practice Guideline for Anemia in CKD**
           - Kidney Int Suppl. 2012;2(4):279-335
        
        3. **UpToDate:** Anemia in chronic kidney disease: Evaluation and management
           - Last updated: 2025
        """)


def render_diagnosis(current_hb, tsat, ferritin, ckd_stage, dialysis_status):
    """Diagnosis and evaluation"""
    st.success("## 🔍 Chẩn đoán & Đánh giá Thiếu Máu")
    
    st.markdown("### Tiêu chuẩn Chẩn đoán Thiếu Máu")
    st.info("""
    **Người lớn:**
    - **Nam giới:** Hb <13 g/dL
    - **Nữ giới:** Hb <12 g/dL
    
    **Trẻ em:**
    - Theo tuổi và giới tính (tham khảo bảng chuẩn WHO)
    """)
    
    # Evaluate current status
    st.markdown("---")
    st.markdown("### Đánh giá Tình Trạng Hiện Tại")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if current_hb < 10:
            st.error(f"**Hb: {current_hb} g/dL** - Thiếu máu nặng")
        elif current_hb < 12:
            st.warning(f"**Hb: {current_hb} g/dL** - Thiếu máu nhẹ-trung bình")
        else:
            st.success(f"**Hb: {current_hb} g/dL** - Bình thường")
    
    with col2:
        if tsat < 20:
            st.error(f"**TSAT: {tsat}%** - Thiếu sắt")
        else:
            st.success(f"**TSAT: {tsat}%** - Đủ sắt")
    
    with col3:
        if dialysis_status == "Lọc máu chu kỳ" or dialysis_status == "Lọc màng bụng":
            target_ferritin = 200
        else:
            target_ferritin = 100
        
        if ferritin < target_ferritin:
            st.error(f"**Ferritin: {ferritin} ng/mL** - Thiếu sắt (mục tiêu ≥{target_ferritin})")
        elif ferritin > 500:
            st.warning(f"**Ferritin: {ferritin} ng/mL** - Quá tải sắt")
        else:
            st.success(f"**Ferritin: {ferritin} ng/mL** - Đủ sắt")
    
    st.markdown("---")
    st.markdown("### Nguyên nhân Thiếu Máu trong CKD")
    
    st.markdown("""
    **1. Thiếu erythropoietin (EPO):**
    - Giảm sản xuất EPO từ thận
    - Tỷ lệ với mức độ suy thận
    
    **2. Thiếu sắt:**
    - Thiếu sắt tuyệt đối (giảm ferritin, giảm TSAT)
    - Thiếu sắt chức năng (ferritin bình thường nhưng TSAT thấp)
    - Mất máu mạn tính (lọc máu, xuất huyết tiêu hóa)
    
    **3. Viêm mạn tính:**
    - Tăng hepcidin
    - Giảm hấp thu và sử dụng sắt
    - Giảm đáp ứng với EPO
    
    **4. Nguyên nhân khác:**
    - Thiếu vitamin B12, folate
    - Tan máu
    - Bệnh lý tủy xương
    """)
    
    st.markdown("---")
    st.markdown("### Xét nghiệm Cần Thiết")
    
    st.warning("""
    **Xét nghiệm ban đầu:**
    - Hemoglobin (Hb), Hematocrit (Hct)
    - Ferritin, TSAT, TIBC
    - Vitamin B12, Folate
    - Reticulocyte count
    - Phân tích nước tiểu (nếu cần)
    
    **Tần suất theo dõi:**
    - **CKD G1-G3a:** Đánh giá nếu có triệu chứng
    - **CKD G3b-G5 (không lọc máu):** Mỗi 3-6 tháng
    - **CKD G5D (lọc máu):** Hb mỗi tháng, sắt mỗi 3 tháng
    """)


def render_iron_therapy(tsat, ferritin, ckd_stage, dialysis_status):
    """Iron therapy"""
    st.warning("## 💊 Điều trị Thiếu Sắt")
    
    # Determine iron deficiency
    if dialysis_status == "Lọc máu chu kỳ" or dialysis_status == "Lọc màng bụng":
        target_ferritin = 200
        preferred_route = "IV"
    else:
        target_ferritin = 100
        preferred_route = "Oral"
    
    iron_deficient = tsat < 20 or ferritin < target_ferritin
    
    if iron_deficient:
        st.error(f"**Chẩn đoán:** Thiếu sắt (TSAT <20% hoặc Ferritin <{target_ferritin} ng/mL)")
    else:
        st.success(f"**Chẩn đoán:** Đủ sắt (TSAT ≥20%, Ferritin ≥{target_ferritin} ng/mL)")
    
    st.markdown("---")
    st.markdown("### Chỉ định Bổ sung Sắt")
    
    st.info("""
    **Bổ sung sắt khi:**
    - TSAT <20% HOẶC
    - Ferritin <100 ng/mL (không lọc máu) HOẶC
    - Ferritin <200 ng/mL (lọc máu)
    
    **Mục tiêu:**
    - TSAT ≥20%
    - Ferritin ≥100 ng/mL (không lọc máu) hoặc ≥200 ng/mL (lọc máu)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Sắt Đường Uống")
        st.success("""
        **Chỉ định:**
        - Bệnh nhân CKD không lọc máu
        - Thiếu sắt nhẹ-trung bình
        - Bệnh nhân tuân thủ tốt
        
        **Liều lượng:**
        - **Sắt sulfate:** 325 mg × 2-3 lần/ngày
          (65-100 mg sắt nguyên tố/ngày)
        - **Sắt fumarate:** 200 mg × 2-3 lần/ngày
        - **Sắt gluconate:** 300 mg × 2-3 lần/ngày
        
        **Lưu ý:**
        - Uống khi đói (1 giờ trước hoặc 2 giờ sau ăn)
        - Tránh uống với trà, cà phê, sữa
        - Có thể dùng với vitamin C để tăng hấp thu
        - Tác dụng phụ: táo bón, buồn nôn, đau bụng
        """)
    
    with col2:
        st.markdown("### Sắt Tiêm Tĩnh Mạch (IV)")
        st.warning("""
        **Chỉ định:**
        - Bệnh nhân lọc máu (ưu tiên)
        - Thiếu sắt nặng hoặc không đáp ứng sắt uống
        - Cần tăng sắt nhanh trước khi bắt đầu ESA
        
        **Chế phẩm:**
        - **Iron sucrose:** 100-200 mg mỗi lần lọc máu, tổng 1000 mg
        - **Ferric carboxymaltose:** 500-1000 mg một lần, có thể lặp lại sau 1 tuần
        - **Iron dextran:** 500-1000 mg một lần (cần test liều trước)
        
        **Liều lượng:**
        - **Không lọc máu:** 500-1000 mg tổng cộng
        - **Lọc máu:** 1000 mg tổng cộng, sau đó duy trì
        
        **Theo dõi:**
        - Đánh giá lại sau 4-8 tuần
        - Tránh quá tải sắt (ferritin >500 ng/mL)
        """)
    
    st.markdown("---")
    
    # Recommendation based on current status
    if iron_deficient:
        if dialysis_status == "Không lọc máu":
            st.success("**Khuyến cáo:** Bắt đầu sắt đường uống. Nếu không đáp ứng sau 1-3 tháng, xem xét sắt IV.")
        else:
            st.success("**Khuyến cáo:** Bắt đầu sắt IV (ưu tiên cho bệnh nhân lọc máu).")


def render_esa_therapy(current_hb, tsat, ferritin, ckd_stage, dialysis_status):
    """ESA therapy"""
    st.warning("## 💉 Điều trị ESA (Erythropoiesis-Stimulating Agents)")
    
    # Check eligibility
    target_ferritin = 200 if (dialysis_status == "Lọc máu chu kỳ" or dialysis_status == "Lọc màng bụng") else 100
    iron_adequate = tsat >= 20 and ferritin >= target_ferritin
    
    st.markdown("### Chỉ định ESA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Bắt đầu ESA khi:**
        - Hb <10 g/dL VÀ
        - Đã điều chỉnh thiếu sắt
          (TSAT ≥20%, ferritin đạt mục tiêu) VÀ
        - Không có nguyên nhân khác gây thiếu máu
        """)
    
    with col2:
        st.error("""
        **Không bắt đầu ESA khi:**
        - Hb ≥10 g/dL (trừ khi có triệu chứng nặng)
        - Chưa điều chỉnh thiếu sắt
        - Có nguyên nhân khác gây thiếu máu chưa được điều trị
        """)
    
    st.markdown("---")
    st.markdown("### Mục tiêu Hemoglobin")
    
    st.success("""
    **KDIGO 2026 khuyến cáo:**
    - **Mục tiêu Hb:** 10-11.5 g/dL (không khuyến cáo >13 g/dL)
    - **Cá nhân hóa:** Cân nhắc triệu chứng, nguy cơ tim mạch, sở thích bệnh nhân
    
    **Lưu ý:**
    - Tránh Hb >13 g/dL (tăng nguy cơ đột quỵ, huyết khối)
    - Điều chỉnh theo triệu chứng và chất lượng cuộc sống
    """)
    
    # Current status evaluation
    st.markdown("---")
    st.markdown("### Đánh giá Tình Trạng Hiện Tại")
    
    if current_hb < 10:
        st.error(f"**Hb hiện tại: {current_hb} g/dL** - Cần điều trị")
        if iron_adequate:
            st.success("✅ Đủ sắt - Có thể bắt đầu ESA")
        else:
            st.warning("⚠️ Chưa đủ sắt - Cần bổ sung sắt trước")
    elif current_hb < 11.5:
        st.success(f"**Hb hiện tại: {current_hb} g/dL** - Trong mục tiêu")
    elif current_hb < 13:
        st.warning(f"**Hb hiện tại: {current_hb} g/dL** - Gần trên mục tiêu, cần giảm liều ESA")
    else:
        st.error(f"**Hb hiện tại: {current_hb} g/dL** - Quá cao, ngừng ESA tạm thời")
    
    st.markdown("---")
    st.markdown("### Chế phẩm ESA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Epoetin alfa/beta")
        st.info("""
        **Không lọc máu:**
        - 50-100 U/kg tiêm dưới da × 1-3 lần/tuần
        
        **Lọc máu:**
        - 50-150 U/kg tiêm tĩnh mạch × 3 lần/tuần
        """)
        
        st.markdown("#### Darbepoetin alfa")
        st.info("""
        **Không lọc máu:**
        - 0.45-0.75 mcg/kg tiêm dưới da × 1 lần/tuần hoặc 2 tuần/lần
        
        **Lọc máu:**
        - 0.45-0.75 mcg/kg tiêm tĩnh mạch × 1 lần/tuần
        """)
    
    with col2:
        st.markdown("#### Methoxy polyethylene glycol-epoetin beta (CERA)")
        st.info("""
        **Không lọc máu:**
        - 0.6 mcg/kg tiêm dưới da × 1 lần/tháng
        
        **Lọc máu:**
        - 0.6 mcg/kg tiêm tĩnh mạch × 1 lần/tháng
        """)
    
    st.markdown("---")
    st.markdown("### Điều chỉnh Liều ESA")
    
    st.warning("""
    **Tăng liều khi:**
    - Hb tăng <1 g/dL/tháng sau 4 tuần
    - Hb <10 g/dL sau khi đã điều chỉnh sắt
    
    **Giảm liều khi:**
    - Hb tăng >1 g/dL/tháng
    - Hb >11.5 g/dL
    
    **Ngừng tạm thời khi:**
    - Hb >13 g/dL
    - Tăng huyết áp nặng không kiểm soát
    - Huyết khối tĩnh mạch sâu hoặc thuyên tắc phổi
    """)
    
    st.markdown("---")
    st.markdown("### Biến chứng và Cảnh báo")
    
    st.error("""
    **Tăng nguy cơ:**
    - Đột quỵ (đặc biệt khi Hb >13 g/dL)
    - Huyết khối tĩnh mạch sâu
    - Thuyên tắc phổi
    - Tăng huyết áp
    - Tăng kali máu
    
    **Cảnh báo:**
    - Tránh Hb >13 g/dL
    - Theo dõi huyết áp thường xuyên
    - Cảnh giác với bệnh nhân có tiền sử đột quỵ hoặc huyết khối
    """)


def render_hif_phi_therapy(current_hb, tsat, ferritin, ckd_stage, dialysis_status):
    """HIF-PHI therapy"""
    st.info("## 🆕 Điều trị HIF-PHI (Hypoxia-Inducible Factor Prolyl Hydroxylase Inhibitors)")
    
    st.markdown("### Tổng quan")
    
    st.success("""
    **HIF-PHI là nhóm thuốc mới:**
    - Kích thích sản xuất EPO nội sinh
    - Cải thiện hấp thu và sử dụng sắt
    - Dùng đường uống
    
    **Chế phẩm:**
    - **Roxadustat:** Đã được phê duyệt ở một số quốc gia
    - **Daprodustat:** Đang trong nghiên cứu
    - **Vadadustat:** Đang trong nghiên cứu
    """)
    
    st.markdown("---")
    st.markdown("### Chỉ định và Liều lượng")
    
    st.info("""
    **Chỉ định:**
    - Bệnh nhân CKD không lọc máu hoặc lọc máu
    - Thiếu máu do CKD
    - Đã điều chỉnh thiếu sắt
    
    **Liều lượng (Roxadustat - ví dụ):**
    - **Không lọc máu:** 70-100 mg × 3 lần/tuần
    - **Lọc máu:** 100-150 mg × 3 lần/tuần
    - Điều chỉnh theo Hb và cân nặng
    """)
    
    st.markdown("---")
    st.markdown("### Lưu ý")
    
    st.warning("""
    **Theo dõi:**
    - Hb thường xuyên
    - Có thể cần bổ sung sắt
    
    **Tác dụng phụ:**
    - Tăng huyết áp
    - Phù
    - Tăng kali máu
    
    **Lưu ý:**
    - Chưa có sẵn rộng rãi tại Việt Nam
    - Cần theo dõi nghiên cứu và phê duyệt tại địa phương
    """)


def render_monitoring(current_hb, tsat, ferritin, ckd_stage, dialysis_status):
    """Monitoring and adjustment"""
    st.success("## 📊 Theo dõi & Điều chỉnh")
    
    st.markdown("### Tần suất Theo dõi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Hemoglobin")
        st.info("""
        **Không lọc máu:**
        - Mỗi 3-6 tháng
        - Thường xuyên hơn khi điều chỉnh liều ESA
        
        **Lọc máu:**
        - Mỗi tháng
        
        **Khi điều chỉnh liều ESA:**
        - Mỗi 2-4 tuần
        """)
    
    with col2:
        st.markdown("#### Sắt")
        st.info("""
        **Không lọc máu:**
        - Mỗi 3-6 tháng
        
        **Lọc máu:**
        - Mỗi 3 tháng
        - Thường xuyên hơn khi điều chỉnh
        
        **Chỉ số:**
        - TSAT: Mục tiêu ≥20%
        - Ferritin: Mục tiêu ≥100 ng/mL (không lọc máu) hoặc ≥200 ng/mL (lọc máu)
        """)
    
    st.markdown("---")
    st.markdown("### Điều chỉnh Điều trị")
    
    st.warning("""
    **Khi Hb không đáp ứng:**
    1. Kiểm tra lại thiếu sắt
    2. Đánh giá tuân thủ điều trị
    3. Tìm nguyên nhân khác (viêm, nhiễm trùng, xuất huyết)
    4. Điều chỉnh liều ESA
    
    **Khi Hb tăng quá nhanh:**
    - Giảm liều ESA ngay
    - Có thể ngừng tạm thời nếu Hb >13 g/dL
    """)
    
    st.markdown("---")
    st.markdown("### Truyền Máu")
    
    st.error("""
    **Chỉ định truyền máu khi:**
    - Thiếu máu nặng có triệu chứng (Hb <7-8 g/dL)
    - Thiếu máu cấp tính (xuất huyết)
    - Không đáp ứng với ESA hoặc chống chỉ định ESA
    - Trước phẫu thuật nếu Hb <10 g/dL
    
    **Tránh truyền máu khi:**
    - Có thể điều trị bằng ESA và sắt
    - Hb >10 g/dL và không có triệu chứng
    
    **Rủi ro truyền máu:**
    - Phản ứng truyền máu
    - Quá tải sắt
    - Kháng thể kháng HLA (ảnh hưởng ghép thận sau này)
    - Nhiễm trùng
    """)
    
    st.markdown("---")
    st.markdown("### Quá tải Sắt")
    
    st.warning("""
    **Dấu hiệu:**
    - Ferritin >500 ng/mL
    - TSAT >50%
    
    **Xử trí:**
    - Ngừng bổ sung sắt
    - Xem xét phlebotomy nếu cần
    - Theo dõi ferritin định kỳ
    """)
