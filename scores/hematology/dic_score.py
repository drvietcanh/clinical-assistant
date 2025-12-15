"""
ISTH DIC Score (International Society on Thrombosis and Haemostasis)
====================================================================

Scoring system for diagnosis of overt Disseminated Intravascular Coagulation (DIC)

Reference:
- Taylor FB Jr, et al. Towards definition, clinical and laboratory criteria, 
  and a scoring system for disseminated intravascular coagulation. 
  Thromb Haemost. 2001;86(5):1327-1330.
- Levi M, et al. Guidelines for the diagnosis and management of disseminated 
  intravascular coagulation. Br J Haematol. 2009;145(1):24-33.

Scoring Components:
1. Platelet count
2. D-dimer/Fibrin degradation products (FDP)
3. Prothrombin time (PT) prolongation
4. Fibrinogen level

Interpretation:
- Score ≥5: Compatible with overt DIC
- Score <5: Suggestive but not affirmative for DIC (repeat test in 1-2 days)

Note: This score should only be calculated in patients with an underlying disorder 
known to be associated with DIC (sepsis, trauma, malignancy, obstetric complications, etc.)
"""

import streamlit as st
from scores.utils.validation import validate_lab_value, validate_range
from components.ui.validation import render_validation_errors


def calculate_dic_score(
    platelet_count: float,
    ddimer_level: int,
    pt_prolongation: float,
    fibrinogen: float
) -> dict:
    """
    Calculate ISTH DIC Score
    
    Args:
        platelet_count: Platelet count (×10³/μL or ×10⁹/L)
        ddimer_level: D-dimer level category (0=no increase, 1=moderate, 2=strong)
        pt_prolongation: PT prolongation in seconds above ULN
        fibrinogen: Fibrinogen level (mg/dL)
    
    Returns:
        Dictionary containing score, interpretation, recommendations, and details
    """
    score = 0
    details = []
    
    # 1. Platelet count
    if platelet_count >= 100:
        plt_score = 0
        details.append(f"Tiểu cầu: {platelet_count:.0f} ×10³/μL → 0 điểm (≥100)")
    elif platelet_count >= 50:
        plt_score = 1
        details.append(f"Tiểu cầu: {platelet_count:.0f} ×10³/μL → 1 điểm (50-99)")
    else:
        plt_score = 2
        details.append(f"Tiểu cầu: {platelet_count:.0f} ×10³/μL → 2 điểm (<50)")
    score += plt_score
    
    # 2. D-dimer / FDP
    ddimer_labels = [
        "Không tăng",
        "Tăng vừa (>ULN nhưng <3-4× ULN)",
        "Tăng mạnh (≥3-4× ULN)"
    ]
    if ddimer_level == 0:
        details.append(f"D-dimer/FDP: {ddimer_labels[0]} → 0 điểm")
    elif ddimer_level == 1:
        details.append(f"D-dimer/FDP: {ddimer_labels[1]} → 2 điểm")
    else:  # ddimer_level == 2
        details.append(f"D-dimer/FDP: {ddimer_labels[2]} → 3 điểm")
    
    ddimer_score = [0, 2, 3][ddimer_level]
    score += ddimer_score
    
    # 3. PT prolongation
    if pt_prolongation < 3:
        pt_score = 0
        details.append(f"PT kéo dài: {pt_prolongation:.1f}s → 0 điểm (<3s)")
    elif pt_prolongation < 6:
        pt_score = 1
        details.append(f"PT kéo dài: {pt_prolongation:.1f}s → 1 điểm (3-5.9s)")
    else:
        pt_score = 2
        details.append(f"PT kéo dài: {pt_prolongation:.1f}s → 2 điểm (≥6s)")
    score += pt_score
    
    # 4. Fibrinogen
    if fibrinogen >= 100:
        fib_score = 0
        details.append(f"Fibrinogen: {fibrinogen:.0f} mg/dL → 0 điểm (≥100)")
    else:
        fib_score = 1
        details.append(f"Fibrinogen: {fibrinogen:.0f} mg/dL → 1 điểm (<100)")
    score += fib_score
    
    # Determine interpretation and recommendations
    if score >= 5:
        interpretation = "TƯƠNG THÍCH VỚI DIC RÕ RÀNG (Overt DIC)"
        risk_class = "POSITIVE"
        color = "🔴"
        recommendation = """
        **🔴 Xử trí khuyến cáo - OVERT DIC:**
        
        ### 1️⃣ ĐIỀU TRỊ BỆNH NỀN - QUAN TRỌNG NHẤT
        
        **Không thể điều trị DIC nếu không điều trị nguyên nhân gốc!**
        
        - **Sepsis:** Kháng sinh phù hợp, kiểm soát nhiễm trùng, resuscitation
        - **Chấn thương:** Kiểm soát chảy máu, phẫu thuật, damage control
        - **Ung thư:** Hóa trị, điều trị ung thư gây DIC (promyelocytic leukemia)
        - **Sản khoa:** Lấy thai/nhau, điều trị pre-eclampsia/eclampsia
        - **Độc tố:** Gắp rắn, transfusion reaction → điều trị specific
        
        ### 2️⃣ HỖ TRỢ ĐÔNG MÁU
        
        **A. Truyền Thành phần Máu:**
        
        - **Tiểu cầu:**
          - Mục tiêu: >50,000/μL (nếu chảy máu hoặc thủ thuật xâm lấn)
          - Mục tiêu: >20,000/μL (nếu ổn định, không chảy máu)
          - Liều: 1 unit tiểu cầu (thường tăng ~5,000-10,000/μL)
        
        - **Fresh Frozen Plasma (FFP):**
          - Nếu PT/aPTT kéo dài + chảy máu hoặc cần thủ thuật
          - Liều: 10-15 mL/kg (thường 4 units)
          - Không khuyến cáo nếu không chảy máu
        
        - **Cryoprecipitate:**
          - Nếu fibrinogen <100 mg/dL + chảy máu
          - Liều: 10 units (tăng fibrinogen ~70-100 mg/dL)
        
        - **Packed Red Blood Cells:**
          - Duy trì Hb >7 g/dL (hoặc >9 g/dL nếu CAD, hoạt động chảy máu)
        
        **B. Kháng Đông (Heparin):**
        
        ⚠️ **Controversial!** Chỉ xem xét trong trường hợp đặc biệt:
        - **Có thể cân nhắc:**
          * DIC chủ yếu huyết khối (purpura fulminans, acral ischemia)
          * Acute promyelocytic leukemia (APL)
          * Retained dead fetus syndrome
          * Aortic aneurysm (Kasabach-Merritt)
        
        - **Liều:** UFH 5-10 U/kg/h (KHÔNG loading dose)
        - **KHÔNG dùng nếu:** Chảy máu hoạt động, tiểu cầu <50,000
        
        **C. Thuốc Khác:**
        
        - **Tranexamic acid:** ❌ TRÁNH trong DIC cấp (nguy cơ huyết khối)
        - **Antithrombin concentrate:** Có thể có lợi nhưng evidence hạn chế
        - **Recombinant Factor VIIa:** Chỉ trong trường hợp cực kỳ đặc biệt
        
        ### 3️⃣ THEO DÕI
        
        - **CBC, PT/INR, aPTT, fibrinogen:** Mỗi 6-12h ban đầu
        - **D-dimer:** Theo dõi xu hướng
        - **Tính lại DIC score:** Hàng ngày
        - **Đánh giá chảy máu:** Liên tục (da, niêm mạc, chỗ chích, catheter)
        - **Đánh giá huyết khối:** Acral cyanosis, purpura fulminans, organ failure
        
        ### 4️⃣ XỬ TRÍ BIẾN CHỨNG
        
        - **Chảy máu:** Truyền thành phần, điều trị tại chỗ
        - **Huyết khối vi mạch:** Heparin liều thấp (nếu phù hợp)
        - **Suy cơ quan:** Hỗ trợ gan/thận/hô hấp
        """
        
        education = """
        **💡 Diễn giải - OVERT DIC:**
        
        - **DIC Score ≥5:** Chẩn đoán DIC rõ ràng (với bệnh nền phù hợp)
        - **DIC** là hội chứng đông máu nội mạch lan tỏa → tiêu thụ tiểu cầu/yếu tố đông máu
        - **Cơ chế:** Kích hoạt đông máu → tiểu cầu/fibrinogen cạn kiệt → chảy máu paradoxical
        - **Biểu hiện:** Chảy máu + huyết khối + suy cơ quan
        - **Điều trị then chốt:** ĐIỀU TRỊ BỆNH NỀN (sepsis, trauma, etc.)
        - **Truyền máu:** Hỗ trợ, KHÔNG "điều trị" DIC
        """
        
    else:  # score < 5
        interpretation = "GỢI Ý NHƯNG CHƯA XÁC ĐỊNH DIC (Non-Overt DIC)"
        risk_class = "SUGGESTIVE"
        color = "🟡"
        recommendation = """
        **🟡 Xử trí khuyến cáo - NON-OVERT DIC:**
        
        ### 1️⃣ ĐÁNH GIÁ LẠI
        
        - **Tính lại DIC score sau 1-2 ngày**
        - Có thể đang ở giai đoạn SỚM của DIC
        - Theo dõi xu hướng các xét nghiệm đông máu
        
        ### 2️⃣ XEM XÉT CHẨN ĐOÁN KHÁC
        
        **Nếu DIC score thấp nhưng có rối loạn đông máu:**
        
        - **Suy gan:** PT kéo dài, giảm fibrinogen, NHƯNG D-dimer thường không tăng cao
        - **ITP (Immune Thrombocytopenic Purpura):** Giảm tiểu cầu ĐƠN THUẦN, PT/aPTT bình thường
        - **TTP/HUS:** Giảm tiểu cầu, thiếu máu tan máu, NHƯNG PT/aPTT bình thường
        - **Thiếu vitamin K:** PT kéo dài, fibrinogen bình thường, tiểu cầu bình thường
        - **Dilutional coagulopathy:** Sau truyền máu/dịch lớn
        - **Heparin/Warfarin effect:** Kéo dài PT/aPTT
        
        ### 3️⃣ TIẾP TỤC ĐIỀU TRỊ BỆNH NỀN
        
        - Dù DIC score <5, vẫn cần điều trị tích cực bệnh nền
        - Sepsis → kháng sinh, resuscitation
        - Chấn thương → kiểm soát chảy máu
        - Ung thư → hóa trị nếu phù hợp
        
        ### 4️⃣ THEO DÕI
        
        - **CBC, PT/INR, aPTT, fibrinogen, D-dimer:** Mỗi ngày
        - **Tái đánh giá DIC score:** Sau 24-48h
        - **Theo dõi triệu chứng:** Chảy máu, huyết khối, suy cơ quan
        
        ### 5️⃣ CHUẨN BỊ XỬ TRÍ
        
        - Nếu DIC score tăng lên ≥5 → xử trí như OVERT DIC
        - Sẵn sàng thành phần máu nếu cần
        - Tránh thủ thuật xâm lấn không cần thiết
        """
        
        education = """
        **💡 Diễn giải - NON-OVERT DIC:**
        
        - **DIC Score <5:** Gợi ý rối loạn đông máu nhưng chưa đủ tiêu chuẩn DIC rõ ràng
        - Có thể là:
          * DIC giai đoạn SỚM (cần theo dõi)
          * Rối loạn đông máu do nguyên nhân KHÁC (suy gan, ITP, TTP, etc.)
          * Bệnh nền đã gây rối loạn đông máu nhưng chưa phát triển thành DIC
        
        - **Khuyến cáo:**
          * Tính lại score sau 24-48h
          * Tiếp tục điều trị bệnh nền tích cực
          * Theo dõi xu hướng xét nghiệm
          * Xem xét chẩn đoán phân biệt
        """
    
    # Additional clinical notes
    clinical_notes = """
    **📌 LƯU Ý QUAN TRỌNG:**
    
    1. **ISTH DIC Score CHỈ ÁP DỤNG** khi có bệnh nền liên quan DIC:
       - Sepsis / Nhiễm trùng nặng
       - Chấn thương nặng / Đa chấn thương
       - Ung thư (đặc biệt APL, ung thư tụy, ung thư tiền liệt tuyến)
       - Biến chứng sản khoa (HELLP, thai chết lưu, nhau bong non, ối vào mạch)
       - Phản ứng truyền máu
       - Bệnh gan nặng
       - Rắn độc cắn
       - Phẫu thuật lớn (tim, gan, tụy)
    
    2. **KHÔNG tính DIC score nếu không có bệnh nền phù hợp!**
    
    3. **DIC là chẩn đoán lâm sàng + xét nghiệm:**
       - Score ≥5 + bệnh nền + biểu hiện lâm sàng → DIC
       - Score đơn thuần KHÔNG đủ để chẩn đoán
    """
    
    return {
        'score': score,
        'interpretation': interpretation,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'education': education,
        'details': details,
        'color': color,
        'clinical_notes': clinical_notes
    }


def render():
    """Render ISTH DIC Score calculator in Streamlit"""
    
    st.title("🩸 ISTH DIC Score")
    st.markdown("**Chẩn đoán rối loạn đông máu nội mạch lan tỏa (Disseminated Intravascular Coagulation)**")
    
    # Important warning at the top
    st.error("""
    ⚠️ **ĐIỀU KIỆN TIÊN QUYẾT:**
    
    Thang điểm này **CHỈ ÁP DỤNG** khi bệnh nhân có **BỆNH NỀN** liên quan đến DIC:
    - Sepsis / Nhiễm trùng huyết nặng
    - Chấn thương nặng / Polytrauma
    - Ung thư (APL, ung thư tụy, tiền liệt tuyến, etc.)
    - Biến chứng sản khoa (HELLP, thai chết lưu, nhau bong non, ối vào mạch)
    - Phản ứng truyền máu cấp
    - Bệnh gan nặng / Suy gan cấp
    - Rắn độc cắn
    
    **KHÔNG tính DIC score nếu không có bệnh nền phù hợp!**
    """)
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **DIC (Disseminated Intravascular Coagulation)** là hội chứng:
        - Kích hoạt đông máu lan tỏa → tạo huyết khối vi mạch
        - Tiêu thụ tiểu cầu và yếu tố đông máu
        - Kích hoạt fibrinolysis
        - Kết quả: Chảy máu + huyết khối + suy cơ quan
        
        **ISTH DIC Score** giúp:
        - Chẩn đoán DIC rõ ràng (overt DIC)
        - Theo dõi diễn tiến
        - Đánh giá đáp ứng điều trị
        
        ### 📊 Tiêu chí chẩn đoán
        
        | Xét nghiệm | 0 điểm | 1 điểm | 2 điểm | 3 điểm |
        |------------|--------|--------|--------|--------|
        | **Tiểu cầu (×10³/μL)** | ≥100 | 50-99 | <50 | - |
        | **D-dimer/FDP** | Không tăng | - | Tăng vừa | Tăng mạnh |
        | **PT kéo dài (s)** | <3 | 3-5.9 | ≥6 | - |
        | **Fibrinogen (mg/dL)** | ≥100 | <100 | - | - |
        
        **Phân Loại:**
        - **≥5 điểm:** Overt DIC (tương thích với DIC rõ ràng)
        - **<5 điểm:** Non-overt (gợi ý, cần theo dõi)
        
        ### 🎯 Cách Sử dụng
        
        1. **Xác định:** Bệnh nhân có bệnh nền liên quan DIC
        2. **Xét nghiệm:** CBC, PT/INR, aPTT, Fibrinogen, D-dimer
        3. **Tính điểm:** Nhập kết quả vào calculator
        4. **Diễn giải:** Score ≥5 + bệnh nền + lâm sàng → DIC
        5. **Theo dõi:** Tính lại score hàng ngày để đánh giá đáp ứng
        
        ### ⚠️ Lưu ý
        
        - DIC là chẩn đoán **LÂM SÀNG + XÉT NGHIỆM**
        - Score CHỈ là một phần trong đánh giá
        - Cần có: Bệnh nền + Biểu hiện lâm sàng + Score ≥5
        - Điều trị then chốt: **ĐIỀU TRỊ BỆNH NỀN**
        
        ### 📚 Tài liệu tham khảo
        
        - Taylor FB Jr, et al. *Thromb Haemost* 2001;86:1327-1330
        - Levi M, et al. *Br J Haematol* 2009;145:24-33
        - Wada H, et al. *J Intensive Care* 2014;2:15
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập kết quả xét nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🩺 Huyết học")
        platelet_count = st.number_input(
            "**Tiểu cầu (×10³/μL hoặc ×10⁹/L)**",
            min_value=0.0,
            max_value=1000.0,
            value=100.0,
            step=1.0,
            help="Số lượng tiểu cầu"
        )
        
        fibrinogen = st.number_input(
            "**Fibrinogen (mg/dL)**",
            min_value=0.0,
            max_value=1000.0,
            value=200.0,
            step=1.0,
            help="Nồng độ fibrinogen máu. Để chuyển từ g/L: g/L × 100 = mg/dL"
        )
        
        st.caption("💡 Chuyển đổi: g/L × 100 = mg/dL (ví dụ: 2 g/L = 200 mg/dL)")
    
    with col2:
        st.markdown("#### ⏱️ Đông Máu")
        pt_prolongation = st.number_input(
            "**PT kéo dài so với giới hạn trên (giây)**",
            min_value=0.0,
            max_value=60.0,
            value=0.0,
            step=0.1,
            help="Số giây PT vượt quá upper limit of normal (ULN). Ví dụ: PT = 18s, ULN = 13s → kéo dài 5s"
        )
        
        st.caption("💡 Tính: PT bệnh nhân - PT ULN của lab")
        
        ddimer_level = st.radio(
            "**D-dimer / FDP**",
            options=[0, 1, 2],
            format_func=lambda x: [
                "Không tăng (≤ULN)",
                "Tăng vừa (>ULN đến <3-4× ULN)",
                "Tăng mạnh (≥3-4× ULN)"
            ][x],
            help="Mức độ tăng D-dimer hoặc FDP so với giới hạn bình thường"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Toán ISTH DIC Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_platelet, platelet_error = validate_lab_value(platelet_count, "Platelet count (×10³/μL)", 0.0, 1000.0)
        if not is_valid_platelet:
            validation_errors.append(platelet_error)
        
        is_valid_fibrinogen, fibrinogen_error = validate_lab_value(fibrinogen, "Fibrinogen (mg/dL)", 0.0, 1000.0)
        if not is_valid_fibrinogen:
            validation_errors.append(fibrinogen_error)
        
        is_valid_pt, pt_error = validate_range(pt_prolongation, 0.0, 60.0, "PT prolongation (seconds)")
        if not is_valid_pt:
            validation_errors.append(pt_error)
        
        if validation_errors:
            render_validation_errors(validation_errors)
        
        result = calculate_dic_score(
            platelet_count=platelet_count,
            ddimer_level=ddimer_level,
            pt_prolongation=pt_prolongation,
            fibrinogen=fibrinogen
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Score box
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                label="**ISTH DIC Score**",
                value=f"{result['score']} điểm"
            )
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['interpretation']}")
        
        # Details
        with st.expander("📋 Chi tiết tính điểm", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Clinical notes
        st.info(result['clinical_notes'])
        
        # Recommendations
        st.markdown("---")
        st.markdown(result['recommendation'])
        
        # Education
        with st.expander("💡 Diễn giải kết quả"):
            st.markdown(result['education'])
        
        # Additional context
        st.info("""
        **🔬 Xét nghiệm bổ sung nên làm:**
        
        - **Huyết học:**
          * Peripheral blood smear (tìm schistocytes - RBC phân mảnh)
          * Reticulocyte count (đánh giá thiếu máu tan máu)
        
        - **Đông Máu:**
          * aPTT (thường kéo dài)
          * Thrombin time (kéo dài)
          * Fibrin degradation products (FDP) - nếu không có D-dimer
        
        - **Đánh giá Cơ Quan:**
          * Creatinine, BUN (suy thận)
          * ALT, AST, bilirubin (suy gan)
          * Lactate (tưới máu mô)
          * Blood gas (acidosis)
        
        **📈 Theo dõi Điều trị:**
        
        - Tính lại DIC score hàng ngày
        - Nếu điều trị hiệu quả: Score giảm, tiểu cầu/fibrinogen tăng
        - Nếu điều trị không đáp ứng: Xem xét lại bệnh nền, tăng cường hỗ trợ
        """)
        
        # Save to session state
        st.session_state['dic_score_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Cảnh báo Y Khoa:**
        - DIC là cấp cứu huyết học nghiêm trọng với tỷ lệ tử vong cao
        - Điều trị then chốt: **ĐIỀU TRỊ BỆNH NỀN** (sepsis, trauma, cancer, etc.)
        - Truyền máu CHỈ là hỗ trợ, KHÔNG "chữa" DIC
        - Heparin rất controversial - chỉ trong trường hợp đặc biệt
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
    
    # Quick reference
    with st.expander("📖 Nguyên nhân thường gặp của DIC"):
        st.markdown("""
        ### Nguyên nhân DIC theo tần suất
        
        #### 1. 🦠 Sepsis / Nhiễm trùng (phổ biến nhất - 30-50%)
        - Gram âm (endotoxin) > Gram dương
        - Fungal sepsis
        - Viral (HIV, CMV, EBV, hemorrhagic fever viruses)
        - Parasitic (malaria)
        
        #### 2. 🤕 Chấn thương / phẫu thuật (10-20%)
        - Chấn thương sọ não nặng
        - Polytrauma với tissue injury lớn
        - Fat embolism
        - Crush injury, burns
        - Phẫu thuật tim, gan, tụy
        
        #### 3. 🎗️ Ung thư (10-20%)
        - **Huyết học:**
          * Acute promyelocytic leukemia (APL) - cao nhất
          * AML, ALL
        - **Solid tumors:**
          * Adenocarcinoma (tụy, tuyến tiền liệt tuyến, phổi, dạ dày)
          * Mucin-producing tumors
        
        #### 4. 🤰 Sản khoa (5-10%)
        - Nhau bong non (Placental abruption)
        - Ối vào mạch (Amniotic fluid embolism)
        - Thai chết lưu >4 tuần (Retained dead fetus)
        - HELLP syndrome
        - Pre-eclampsia/Eclampsia nặng
        - Septic abortion
        
        #### 5. 🫀 Bệnh mạch máu
        - Kasabach-Merritt syndrome (giant hemangioma)
        - Aortic aneurysm (đặc biệt khi vỡ)
        
        #### 6. 🧪 Độc tố / miễn dịch
        - Rắn độc cắn (venom-induced consumptive coagulopathy)
        - Phản ứng truyền máu cấp (Acute hemolytic transfusion reaction)
        - Transplant rejection
        
        #### 7. 🫘 Bệnh gan
        - Acute liver failure / Fulminant hepatitis
        - Cirrhosis tiến triển
        - Budd-Chiari syndrome
        
        #### 8. 🌡️ Khác
        - Heat stroke
        - Hypothermia nặng
        - Massive transfusion (dilutional + consumptive)
        
        ### 🔍 Phân biệt DIC với bệnh khác
        
        | Đặc Điểm | DIC | Suy Gan | TTP/HUS | ITP |
        |----------|-----|---------|---------|-----|
        | Tiểu cầu | ↓↓ | ↓ | ↓↓ | ↓↓↓ |
        | PT | ↑↑ | ↑↑ | N | N |
        | aPTT | ↑ | ↑ | N | N |
        | Fibrinogen | ↓↓ | ↓ | N | N |
        | D-dimer | ↑↑↑ | ↑ | N/↑ | N |
        | Schistocytes | + | - | +++ | - |
        | Factor VIII | ↓ | ↓ | N | N |
        
        N = bình thường, ↑ = tăng, ↓ = giảm
        """)

