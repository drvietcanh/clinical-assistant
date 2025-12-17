"""
Hypertensive Nephrosclerosis Protocol
KDIGO 2021, KDIGO 2024, AHA/ACC 2017
Quản lý bệnh thận do tăng huyết áp - Nguyên nhân hàng đầu CKD tại Việt Nam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hypertensive Nephrosclerosis Protocol"""
    st.subheader("📈 Bệnh Thận Do Tăng Huyết Áp")
    st.caption("KDIGO 2021, KDIGO 2024, AHA/ACC 2017 - Nguyên nhân hàng đầu gây CKD tại Việt Nam (20-30%)")
    
    st.info("""
    **Tình hình tại Việt Nam:**
    - 20-30% bệnh nhân CKD do tăng huyết áp
    - Tăng huyết áp ảnh hưởng đến 25-30% dân số
    - Bệnh thận do THA thường tiến triển chậm
    
    **Định nghĩa:**
    - Suy thận mạn (eGFR <60) HOẶC
    - Protein niệu nhẹ-trung bình (<1 g/24h)
    - Ở bệnh nhân tăng huyết áp mạn tính
    - Sau khi loại trừ nguyên nhân khác
    """)
    
    st.markdown("---")
    
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Đánh giá",
            "💊 Điều trị bảo tồn",
            "⚠️ Bệnh thận mạch máu nặng",
            "📊 Theo dõi & Phòng ngừa"
        ],
        key="hn_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis()
    elif "bảo tồn" in scenario:
        render_conservative()
    elif "mạch máu" in scenario:
        render_renovascular()
    else:
        render_monitoring()
    
    st.markdown("---")
    references = get_references("Hypertensive Nephrosclerosis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-15",
            show_evidence_level=True,
            show_links=True
        )


def render_diagnosis():
    """Diagnosis and evaluation"""
    st.success("## 🔍 Chẩn đoán & Đánh giá")
    
    st.markdown("### Tiêu chuẩn Chẩn đoán")
    st.info("""
    **Bệnh thận do tăng huyết áp khi có:**
    1. **Tăng huyết áp mạn tính:**
       - Huyết áp ≥140/90 mmHg kéo dài
       - Hoặc đang dùng thuốc hạ huyết áp
    
    2. **Tổn thương thận:**
       - eGFR <60 mL/min/1.73m² HOẶC
       - Protein niệu nhẹ-trung bình (<1 g/24h)
       - Thường không có hồng cầu niệu đáng kể
    
    3. **Loại trừ nguyên nhân khác:**
       - Không có bệnh thận khác (viêm cầu thận, tắc nghẽn)
       - Không có bệnh hệ thống
       - Không có đái tháo đường (nếu có → xem Diabetic Nephropathy)
    """)
    
    st.markdown("---")
    st.markdown("### Đặc Điểm Lâm Sàng")
    st.warning("""
    **Triệu chứng:**
    - Thường không có triệu chứng ở giai đoạn sớm
    - Suy thận tiến triển chậm
    - Protein niệu thường nhẹ (<1 g/24h)
    - Ít khi có hồng cầu niệu
    
    **Xét nghiệm:**
    - Creatinine tăng nhẹ-trung bình
    - eGFR giảm dần theo thời gian
    - Protein niệu: 150-1000 mg/24h
    - Siêu âm: Thận có thể nhỏ, nhu mô mỏng
    
    **Lưu ý:**
    - Chẩn đoán thường là loại trừ
    - Cần loại trừ nguyên nhân khác
    """)
    
    st.markdown("---")
    st.markdown("### Đánh giá Nguyên nhân Khác")
    st.success("""
    **Cần loại trừ:**
    - Đái tháo đường (HbA1c, đường huyết)
    - Viêm cầu thận (hồng cầu niệu, trụ hồng cầu, bổ thể)
    - Tắc nghẽn (siêu âm thận)
    - Bệnh thận đa nang (tiền sử gia đình, siêu âm)
    - Viêm thận kẽ (tiền sử thuốc, nhiễm trùng)
    - Hẹp động mạch thận (nếu nghi ngờ)
    
    **Khi nào nghi ngờ nguyên nhân khác:**
    - Protein niệu >1 g/24h
    - Hồng cầu niệu đáng kể
    - Suy thận tiến triển nhanh
    - Thận không nhỏ (nghi ngờ nguyên nhân khác)
    """)


def render_conservative():
    """Conservative management"""
    st.warning("## 💊 Điều trị Bảo Tồn")
    
    st.markdown("### 1. Kiểm Soát Huyết Áp")
    st.success("""
    **Mục tiêu:**
    - <130/80 mmHg (nếu protein niệu <30 mg/g)
    - <125/75 mmHg (nếu protein niệu ≥30 mg/g)
    - Không <120/70 (nguy cơ giảm tưới máu thận)
    
    **Thuốc ưu tiên:**
    - **ACEi/ARB:** Liều tối đa dung nạp
      * Lisinopril 20-40 mg/ngày
      * Losartan 50-100 mg/ngày
      * Telmisartan 40-80 mg/ngày
      * Ramipril 5-10 mg/ngày
    
    - **Bổ sung nếu cần:**
      * Thiazide: Hydrochlorothiazide 12.5-25 mg/ngày
      * Hoặc Furosemide nếu eGFR <30
      * Calcium channel blocker: Amlodipine 5-10 mg/ngày
      * Beta-blocker nếu có chỉ định
    
    **Lưu ý:**
    - ACEi/ARB làm chậm tiến triển, giảm protein niệu
    - Theo dõi creatinine sau 1-2 tuần
    - Tăng creatinine <30% là chấp nhận được
    - Tránh nếu hẹp động mạch thận 2 bên
    """)
    
    st.markdown("---")
    st.markdown("### 2. Giảm Protein Niệu")
    st.info("""
    **Mục tiêu:**
    - Giảm protein niệu >30% hoặc <150 mg/24h
    
    **Phương pháp:**
    - ACEi/ARB liều tối đa
    - Kiểm soát huyết áp tốt
    - Chế độ ăn hạn chế muối
    
    **Lưu ý:**
    - Protein niệu là yếu tố tiên lượng
    - Giảm protein niệu → làm chậm tiến triển
    """)
    
    st.markdown("---")
    st.markdown("### 3. Chế Độ Ăn & Lối Sống")
    st.warning("""
    **Muối:**
    - <2-3 g/ngày (giảm huyết áp, phù)
    - Tránh: đồ ăn mặn, nước mắm, bột canh
    
    **Protein:**
    - eGFR >30: 0.8-1.0 g/kg/ngày
    - eGFR <30: 0.6-0.8 g/kg/ngày
    
    **Lối sống:**
    - Giảm cân nếu béo phì
    - Tập thể dục đều đặn
    - Bỏ thuốc lá
    - Hạn chế rượu bia
    - Giảm stress
    """)
    
    st.markdown("---")
    st.markdown("### 4. Điều trị Biến Chứng CKD")
    st.success("""
    **Thiếu máu:**
    - Bổ sung sắt nếu ferritin <100 ng/mL
    - ESA nếu Hb <10 g/dL (eGFR <30)
    
    **Rối loạn xương-khoáng:**
    - Vitamin D, Calcitriol
    - Phosphate binders nếu PO₄ >5.5 mg/dL
    
    **Toan chuyển hóa:**
    - Bicarbonate nếu HCO₃ <22 mEq/L
    
    **Tăng lipid:**
    - Statin (mục tiêu LDL <100 mg/dL)
    """)


def render_renovascular():
    """Renovascular disease management"""
    st.error("## ⚠️ Bệnh Thận Mạch Máu Nặng")
    
    st.markdown("### Hẹp Động Mạch Thận")
    st.warning("""
    **Nghi ngờ khi:**
    - Tăng huyết áp kháng trị
    - Suy thận sau khi dùng ACEi/ARB
    - Tăng huyết áp ở người trẻ (<30 tuổi)
    - Tăng huyết áp ở người già (>60 tuổi) mới xuất hiện
    - Suy thận không rõ nguyên nhân
    - Phù phổi tái phát
    
    **Chẩn đoán:**
    - Siêu âm Doppler động mạch thận
    - CT/MRA động mạch thận
    - DSA (tiêu chuẩn vàng)
    
    **Điều trị:**
    - Stent động mạch thận (nếu phù hợp)
    - Phẫu thuật (nếu cần)
    - Thuốc hạ huyết áp
    """)
    
    st.markdown("---")
    st.markdown("### Tăng Huyết Áp Kháng Trị")
    st.info("""
    **Định nghĩa:**
    - Huyết áp ≥140/90 dù đã dùng ≥3 thuốc hạ huyết áp (bao gồm lợi tiểu)
    
    **Nguyên nhân:**
    - Hẹp động mạch thận
    - U tủy thượng thận
    - Cường aldosterone nguyên phát
    - Hẹp eo động mạch chủ
    - Thuốc (NSAID, steroid, thuốc tránh thai)
    
    **Xử trí:**
    - Đánh giá nguyên nhân
    - Điều trị nguyên nhân nếu có thể
    - Phối hợp nhiều thuốc hạ huyết áp
    """)
    
    st.markdown("---")
    st.markdown("### Suy thận Tiến Triển Nhanh")
    st.error("""
    **Nghi ngờ nguyên nhân khác khi:**
    - eGFR giảm >5 mL/min/năm
    - Creatinine tăng nhanh trong vài tháng
    - Protein niệu >1 g/24h
    - Hồng cầu niệu đáng kể
    
    **Cần đánh giá:**
    - Sinh thiết thận (nếu cần)
    - Loại trừ viêm cầu thận
    - Loại trừ nguyên nhân khác
    
    **Lưu ý:**
    - Bệnh thận do THA thường tiến triển chậm
    - Tiến triển nhanh → nghi ngờ nguyên nhân khác
    """)


def render_monitoring():
    """Monitoring and prevention"""
    st.info("## 📊 Theo dõi & Phòng ngừa")
    
    st.markdown("### Theo dõi Định Kỳ")
    st.success("""
    **Mỗi 1-3 tháng:**
    - Huyết áp (tại nhà và tại phòng khám)
    - Creatinine, eGFR
    - Protein niệu (ACR hoặc 24h)
    - Điện giải (Na, K)
    
    **Mỗi 6-12 tháng:**
    - Hemoglobin (nếu eGFR <30)
    - Ca, PO₄, PTH (nếu eGFR <30)
    - Lipid máu
    - Siêu âm thận (nếu cần)
    
    **Mỗi năm:**
    - Đánh giá toàn diện
    - Tư vấn lọc máu (nếu eGFR <30)
    """)
    
    st.markdown("---")
    st.markdown("### Phòng ngừa Tiến Triển")
    st.warning("""
    **Kiểm soát tốt:**
    - Huyết áp: <130/80 (hoặc <125/75 nếu protein niệu)
    - Protein niệu: Giảm >30% hoặc <150 mg/24h
    
    **Thuốc bảo vệ thận:**
    - ACEi/ARB liều tối đa
    - Kiểm soát huyết áp tốt
    
    **Lối sống:**
    - Chế độ ăn hạn chế muối
    - Tập thể dục đều đặn
    - Bỏ thuốc lá
    - Giảm cân nếu béo phì
    - Giảm stress
    """)
    
    st.markdown("---")
    st.markdown("### Khi Cần Hội Chẩn")
    st.error("""
    **Hội chẩn thận học khi:**
    - eGFR <30
    - Protein niệu >1 g/24h
    - Suy thận tiến triển nhanh
    - Tăng huyết áp kháng trị
    - Nghi ngờ hẹp động mạch thận
    - Cần chuẩn bị lọc máu
    - Biến chứng nặng
    
    **Hội chẩn tim mạch:**
    - Tăng huyết áp kháng trị
    - Bệnh tim mạch kèm theo
    """)

