"""
Chronic Kidney Disease (CKD) Protocol
KDIGO 2012, KDIGO 2021, KDIGO 2024
Quản lý suy thận mạn tính - Bệnh lý phổ biến tại Việt Nam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Chronic Kidney Disease Protocol"""
    st.subheader("🫘 Suy thận Mạn Tính (CKD)")
    st.caption("KDIGO 2012, 2021, 2024 - Quản lý suy thận mạn tính, ảnh hưởng >10 triệu người tại Việt Nam")
    
    st.info("""
    **Tình hình tại Việt Nam:**
    - Hơn 10 triệu người mắc CKD
    - ~26.000 bệnh nhân giai đoạn cuối cần lọc máu
    - Nguyên nhân chính: Đái tháo đường, tăng huyết áp, viêm cầu thận
    
    **Định nghĩa CKD (KDIGO):**
    - Tổn thương thận ≥3 tháng HOẶC
    - eGFR <60 mL/min/1.73m² ≥3 tháng
    """)
    
    st.markdown("---")
    
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Phân giai đoạn",
            "💊 Điều trị bảo tồn (Giai đoạn 1-4)",
            "🩸 Chuẩn bị lọc máu (Giai đoạn 4-5)",
            "📊 Theo dõi & Biến chứng"
        ],
        key="ckd_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis()
    elif "bảo tồn" in scenario:
        render_conservative()
    elif "lọc máu" in scenario:
        render_dialysis_prep()
    else:
        render_monitoring()
    
    st.markdown("---")
    references = get_references("CKD")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-15",
            show_evidence_level=True,
            show_links=True
        )


def render_diagnosis():
    """Diagnosis and staging"""
    st.success("## 🔍 Chẩn đoán & Phân Giai Đoạn")
    
    st.markdown("### Tiêu chuẩn Chẩn đoán CKD")
    st.info("""
    **CKD được định nghĩa khi có một trong hai:**
    1. **Tổn thương thận ≥3 tháng:**
       - Protein niệu (albumin niệu)
       - Hồng cầu niệu
       - Bất thường hình ảnh (siêu âm, CT)
       - Bất thường mô bệnh học (sinh thiết)
    
    2. **eGFR <60 mL/min/1.73m² ≥3 tháng:**
       - Tính bằng công thức CKD-EPI hoặc MDRD
       - Cần đo ≥2 lần cách nhau ≥3 tháng
    """)
    
    st.markdown("---")
    st.markdown("### Phân Giai Đoạn CKD (KDIGO 2012)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Theo eGFR:")
        st.warning("""
        **G1:** eGFR ≥90 (tổn thương thận, chức năng bình thường)
        
        **G2:** eGFR 60-89 (tổn thương thận, chức năng giảm nhẹ)
        
        **G3a:** eGFR 45-59 (suy thận mạn độ nhẹ-trung bình)
        
        **G3b:** eGFR 30-44 (suy thận mạn độ trung bình-nặng)
        
        **G4:** eGFR 15-29 (suy thận mạn độ nặng)
        
        **G5:** eGFR <15 (suy thận mạn giai đoạn cuối - ESKD)
        """)
    
    with col2:
        st.markdown("#### Theo Protein Niệu (A):")
        st.info("""
        **A1:** ACR <30 mg/g (<3 mg/mmol) - Bình thường/nhẹ
        
        **A2:** ACR 30-300 mg/g (3-30 mg/mmol) - Trung bình
        
        **A3:** ACR >300 mg/g (>30 mg/mmol) - Nặng
        
        **Hoặc:** Protein niệu 24h:
        - <150 mg/24h: Bình thường
        - 150-500 mg/24h: Nhẹ
        - 500-1000 mg/24h: Trung bình
        - >1000 mg/24h: Nặng
        """)
    
    st.markdown("---")
    st.markdown("### Nguyên nhân Thường gặp Tại Việt Nam")
    st.success("""
    **1. Đái tháo đường (30-40%):**
    - Diabetic nephropathy
    - Kiểm soát đường huyết kém
    
    **2. Tăng huyết áp (20-30%):**
    - Hypertensive nephrosclerosis
    - Huyết áp không kiểm soát
    
    **3. Viêm cầu thận (15-25%):**
    - IgA nephropathy (phổ biến nhất)
    - FSGS, Membranous
    - Lupus nephritis
    
    **4. Bệnh thận đa nang (5-10%):**
    - Di truyền
    - ADPKD
    
    **5. Nguyên nhân khác:**
    - Viêm thận kẽ (do thuốc)
    - Tắc nghẽn đường tiểu
    - Nhiễm trùng mạn tính
    """)


def render_conservative():
    """Conservative management for CKD stages 1-4"""
    st.warning("## 💊 Điều trị Bảo Tồn (CKD G1-G4)")
    
    st.markdown("### 1. Kiểm Soát Nguyên nhân")
    st.success("""
    **Đái tháo đường:**
    - HbA1c <7% (hoặc <8% nếu nguy cơ hạ đường huyết)
    - SGLT2 inhibitors: Dapagliflozin, Empagliflozin (nếu eGFR ≥25)
    - GLP-1 agonists: Liraglutide, Semaglutide
    
    **Tăng huyết áp:**
    - Mục tiêu: <130/80 mmHg (nếu protein niệu <1 g/24h)
    - Mục tiêu: <125/75 mmHg (nếu protein niệu >1 g/24h)
    - ACEi/ARB: Liều tối đa dung nạp
    
    **Viêm cầu thận:**
    - Điều trị theo nguyên nhân cụ thể
    - Xem protocol Viêm cầu thận mạn
    """)
    
    st.markdown("---")
    st.markdown("### 2. Làm Chậm Tiến Triển (KDIGO 2024)")
    st.info("""
    **ACEi/ARB:**
    - Giảm protein niệu 30-50%
    - Làm chậm tiến triển CKD
    - Liều tối đa dung nạp (Lisinopril 20-40 mg, Losartan 50-100 mg)
    
    **SGLT2 inhibitors (KDIGO 2024 - MỚI):**
    - **CKD với đái tháo đường:**
      * Dapagliflozin 10 mg/ngày (nếu eGFR ≥25)
      * Empagliflozin 10-25 mg/ngày
      * Làm chậm tiến triển, giảm biến cố tim mạch
    
    - **CKD KHÔNG đái tháo đường (KDIGO 2024):**
      * Dapagliflozin 10 mg/ngày (nếu eGFR ≥25, protein niệu ≥200 mg/g)
      * Empagliflozin 10-25 mg/ngày
      * Làm chậm tiến triển CKD, giảm nguy cơ tim mạch
    
    **GLP-1 receptor agonists (KDIGO 2024):**
    - Dulaglutide, Liraglutide, Semaglutide
    - CKD với đái tháo đường type 2
    - Cải thiện kiểm soát đường huyết, giảm nguy cơ tim mạch
    
    **Finerenone (KDIGO 2024 - MỚI):**
    - Chất đối kháng thụ thể mineralocorticoid không steroid
    - CKD với đái tháo đường type 2 (eGFR ≥25, ACR 30-5000 mg/g)
    - Liều: 10-20 mg/ngày
    - Làm chậm tiến triển CKD, giảm nguy cơ tim mạch
    - Theo dõi kali máu (nguy cơ tăng kali)
    
    **Lưu ý:**
    - Theo dõi creatinine sau 1-2 tuần khi bắt đầu ACEi/ARB
    - Tăng creatinine <30% là chấp nhận được
    - Tránh nếu hẹp động mạch thận 2 bên
    - SGLT2i có thể dùng kết hợp với ACEi/ARB
    """)
    
    st.markdown("---")
    st.markdown("### 3. Chế Độ Ăn")
    st.warning("""
    **Protein:**
    - eGFR >30: 0.8-1.0 g/kg/ngày
    - eGFR <30: 0.6-0.8 g/kg/ngày
    - Chất lượng cao (thịt, cá, trứng, sữa)
    
    **Muối:**
    - <2-3 g/ngày (giảm huyết áp, phù)
    
    **Phosphorus:**
    - Hạn chế nếu tăng (eGFR <30)
    - Tránh: phô mai, sữa, đậu, hạt, nước ngọt có ga
    
    **Kali:**
    - Theo dõi, hạn chế nếu tăng (eGFR <30)
    - Tránh: chuối, cam, khoai tây, cà chua
    
    **Nước:**
    - Bình thường trừ khi có chỉ định hạn chế
    """)
    
    st.markdown("---")
    st.markdown("### 4. Điều trị Biến Chứng")
    st.success("""
    **Thiếu máu (Hb <10 g/dL):**
    - Bổ sung sắt nếu ferritin <100 ng/mL
    - ESA (Erythropoietin) nếu Hb <10 và thiếu máu do CKD
    - Mục tiêu Hb: 10-12 g/dL (không >13)
    
    **Rối loạn xương-khoáng (CKD-MBD):**
    - Bổ sung Calcitriol/Vitamin D nếu thiếu
    - Phosphate binders nếu PO₄ >5.5 mg/dL (eGFR <30)
    - Theo dõi PTH, Ca, PO₄ mỗi 3-6 tháng
    
    **Tăng lipid:**
    - Statin nếu LDL >100 mg/dL
    - Mục tiêu LDL <100 mg/dL (hoặc <70 nếu nguy cơ tim mạch cao)
    
    **Toan chuyển hóa:**
    - Bicarbonate nếu HCO₃ <22 mEq/L
    - Sodium bicarbonate 650-1300 mg × 2-3 lần/ngày
    """)
    
    st.markdown("---")
    st.markdown("### 5. Tránh Thuốc Độc Thận")
    st.error("""
    **Tránh hoặc cẩn thận:**
    - NSAID (Ibuprofen, Diclofenac, Meloxicam)
    - Contrast (nếu có thể, dùng N-acetylcysteine trước)
    - Aminoglycoside (nếu cần, theo dõi nồng độ)
    - Một số kháng sinh (Vancomycin, cần điều chỉnh liều)
    
    **Điều chỉnh liều theo eGFR:**
    - Hầu hết thuốc cần điều chỉnh khi eGFR <30
    - Tham khảo bảng điều chỉnh liều theo CrCl
    """)


def render_dialysis_prep():
    """Preparation for dialysis (CKD stage 4-5)"""
    st.error("## 🩸 Chuẩn Bị Lọc Máu (CKD G4-G5)")
    
    st.markdown("### Khi Nào Bắt Đầu Chuẩn Bị")
    st.warning("""
    **Bắt đầu chuẩn bị khi:**
    - eGFR <30 (G4) - Chuẩn bị sớm
    - eGFR <20 - Chuẩn bị tích cực
    - eGFR <15 - Cần quyết định phương thức điều trị
    
    **Chỉ định lọc máu:**
    - eGFR <15 HOẶC
    - Triệu chứng urê huyết (buồn nôn, nôn, ngứa, rối loạn thần kinh)
    - Tăng kali máu kháng trị
    - Toan chuyển hóa nặng
    - Quá tải dịch không kiểm soát
    - Viêm màng ngoài tim do urê
    """)
    
    st.markdown("---")
    st.markdown("### Tư Vấn Lựa Chọn Phương Thức")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Lọc Máu Chu Kỳ (Hemodialysis)")
        st.info("""
        **Ưu điểm:**
        - 3 lần/tuần tại trung tâm
        - Nhân viên y tế hỗ trợ
        - Hiệu quả cao
        
        **Nhược điểm:**
        - Phụ thuộc lịch trình
        - Cần cầu nối mạch máu (AV fistula)
        - Hạn chế chế độ ăn giữa các lần lọc
        
        **Chuẩn bị:**
        - Tạo AV fistula sớm (eGFR 15-20)
        - Hoặc AV graft nếu tĩnh mạch không phù hợp
        - Hoặc catheter tạm thời nếu cấp cứu
        """)
    
    with col2:
        st.markdown("#### Lọc Màng Bụng (Peritoneal Dialysis)")
        st.info("""
        **Ưu điểm:**
        - Tự làm tại nhà
        - Linh hoạt thời gian
        - Bảo tồn chức năng thận còn lại
        - Không cần cầu nối mạch máu
        
        **Nhược điểm:**
        - Cần đặt catheter màng bụng
        - Nguy cơ viêm phúc mạc
        - Cần không gian sạch tại nhà
        
        **Chống chỉ định:**
        - Phẫu thuật bụng lớn trước đó
        - Thoát vị bụng
        - Bệnh phổi nặng
        """)
    
    st.markdown("---")
    st.markdown("### Ghép Thận")
    st.success("""
    **Chỉ định:**
    - eGFR <20 hoặc đang lọc máu
    - Không có chống chỉ định
    
    **Chống chỉ định tuyệt đối:**
    - Ung thư đang hoạt động
    - Nhiễm trùng đang hoạt động
    - Bệnh tim mạch nặng không phẫu thuật được
    
    **Chuẩn bị:**
    - Đánh giá đa chuyên khoa
    - Tìm người hiến (sống hoặc chết não)
    - Đăng ký danh sách chờ (nếu cần)
    """)
    
    st.markdown("---")
    st.markdown("### Chăm Sóc Bảo Tồn (Conservative Care)")
    st.warning("""
    **Lựa chọn cho:**
    - Bệnh nhân già, nhiều bệnh kèm
    - Tiên lượng sống <1 năm
    - Không muốn lọc máu
    
    **Mục tiêu:**
    - Kiểm soát triệu chứng
    - Chất lượng cuộc sống
    - Chăm sóc giảm nhẹ
    """)


def render_monitoring():
    """Monitoring and complications"""
    st.info("## 📊 Theo dõi & Biến Chứng")
    
    st.markdown("### Theo dõi Định Kỳ")
    st.success("""
    **Mỗi 1-3 tháng:**
    - Creatinine, eGFR
    - Protein niệu (ACR hoặc 24h)
    - Huyết áp
    - Điện giải (Na, K)
    - Hemoglobin (nếu eGFR <30)
    
    **Mỗi 6-12 tháng:**
    - Ca, PO₄, PTH, Vitamin D (nếu eGFR <30)
    - Lipid máu
    - Albumin
    - Siêu âm thận (nếu cần)
    
    **Mỗi năm:**
    - Đánh giá toàn diện
    - Tư vấn lọc máu (nếu eGFR <30)
    """)
    
    st.markdown("---")
    st.markdown("### Biến Chứng Cần Theo dõi")
    st.warning("""
    **1. Thiếu máu:**
    - Tăng khi eGFR <30
    - Điều trị: Sắt + ESA
    - Mục tiêu Hb: 10-12 g/dL
    
    **2. Rối loạn xương-khoáng:**
    - Tăng PTH, giảm Ca, tăng PO₄
    - Điều trị: Vitamin D, phosphate binders
    
    **3. Toan chuyển hóa:**
    - HCO₃ <22 mEq/L
    - Điều trị: Bicarbonate
    
    **4. Tăng kali máu:**
    - Nguy hiểm khi K >5.5
    - Điều trị: Kayexalate, lợi tiểu, hạn chế kali
    
    **5. Quá tải dịch:**
    - Phù, suy tim
    - Điều trị: Lợi tiểu, hạn chế muối/nước
    """)
    
    st.markdown("---")
    st.markdown("### Khi Cần Hội Chẩn")
    st.error("""
    **Hội chẩn thận học khi:**
    - eGFR <30 (G4)
    - Protein niệu >1 g/24h
    - Suy thận tiến triển nhanh
    - Biến chứng nặng (thiếu máu nặng, tăng kali, toan chuyển hóa)
    - Cần chuẩn bị lọc máu
    - Cần tư vấn ghép thận
    
    **Hội chẩn đa chuyên khoa:**
    - Tim mạch: Nếu có bệnh tim mạch
    - Nội tiết: Nếu đái tháo đường
    - Dinh dưỡng: Tư vấn chế độ ăn
    """)

