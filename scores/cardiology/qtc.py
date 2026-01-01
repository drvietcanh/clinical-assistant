"""
QTc - Corrected QT Interval Calculator
Tính QT điều chỉnh theo nhịp tim
"""

import streamlit as st
from config.theme import COLORS
import math
from scores.utils.validation import validate_heart_rate, validate_range
from components.ui.results import render_result_box
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def calculate_qtc_bazett(qt_ms, hr):
    """
    Calculate QTc using Bazett's formula (most common)
    QTc = QT / √RR
    
    Args:
        qt_ms: QT interval in milliseconds
        hr: Heart rate in bpm
    
    Returns:
        float: QTc in milliseconds
    """
    rr_sec = 60 / hr
    qtc = qt_ms / math.sqrt(rr_sec)
    return qtc


def calculate_qtc_fridericia(qt_ms, hr):
    """
    Calculate QTc using Fridericia's formula
    QTc = QT / ∛RR
    More accurate at extreme heart rates
    
    Args:
        qt_ms: QT interval in milliseconds
        hr: Heart rate in bpm
    
    Returns:
        float: QTc in milliseconds
    """
    rr_sec = 60 / hr
    qtc = qt_ms / (rr_sec ** (1/3))
    return qtc


def calculate_qtc_framingham(qt_ms, hr):
    """
    Calculate QTc using Framingham's formula
    QTc = QT + 154 × (1 - RR)
    
    Args:
        qt_ms: QT interval in milliseconds
        hr: Heart rate in bpm
    
    Returns:
        float: QTc in milliseconds
    """
    rr_sec = 60 / hr
    qtc = qt_ms + 154 * (1 - rr_sec)
    return qtc


def calculate_qtc_hodges(qt_ms, hr):
    """
    Calculate QTc using Hodges' formula
    QTc = QT + 1.75 × (HR - 60)
    
    Args:
        qt_ms: QT interval in milliseconds
        hr: Heart rate in bpm
    
    Returns:
        float: QTc in milliseconds
    """
    qtc = qt_ms + 1.75 * (hr - 60)
    return qtc


def interpret_qtc(qtc, gender):
    """
    Interpret QTc based on gender-specific cutoffs
    
    Args:
        qtc: QTc in milliseconds
        gender: "Nam" or "Nữ"
    
    Returns:
        dict: Interpretation results
    """
    if gender == "Nam":
        normal_upper = 450
        borderline = 450
        prolonged = 470
    else:  # Nữ
        normal_upper = 460
        borderline = 460
        prolonged = 480
    
    if qtc < normal_upper:
        return {
            "status": "Bình thường",
            "color": "🟢",
            "risk": "Nguy cơ thấp",
            "recommendation": "Không cần can thiệp đặc biệt",
            "severity": "normal"
        }
    elif qtc < prolonged:
        return {
            "status": "Giới hạn (Borderline)",
            "color": "🟡",
            "risk": "Nguy cơ trung bình rối loạn nhịp",
            "recommendation": "Theo dõi, xem xét nguyên nhân, điều chỉnh thuốc gây kéo dài QT",
            "severity": "borderline"
        }
    elif qtc < 500:
        return {
            "status": "Kéo dài",
            "color": "🟠",
            "risk": "Nguy cơ cao Torsades de Pointes",
            "recommendation": "Cần can thiệp: Dừng thuốc gây kéo dài QT, điều chỉnh điện giải, theo dõi sát",
            "severity": "prolonged"
        }
    else:
        return {
            "status": "Kéo dài nghiêm trọng",
            "color": "🔴",
            "risk": "Nguy cơ rất cao đột tử do rối loạn nhịp",
            "recommendation": "CẤP CỨU: Dừng ngay thuốc gây kéo dài QT, điều chỉnh K+/Mg2+, cân nhắc pacing tạm thời",
            "severity": "severe"
        }


def get_qtc_prolonging_drugs():
    """Return common QT-prolonging drugs by category"""
    return {
        "Kháng sinh": [
            "Macrolides (Azithromycin, Erythromycin, Clarithromycin)",
            "Fluoroquinolones (Moxifloxacin, Levofloxacin)",
            "Antifungals (Fluconazole, Voriconazole)"
        ],
        "Tim mạch": [
            "Amiodarone, Sotalol, Dronedarone",
            "Quinidine, Procainamide, Disopyramide",
            "Dofetilide, Ibutilide"
        ],
        "Tâm thần": [
            "Haloperidol, Droperidol",
            "Citalopram, Escitalopram",
            "Tricyclic antidepressants (Amitriptyline)",
            "Quetiapine, Ziprasidone"
        ],
        "Khác": [
            "Methadone, Cocaine",
            "Ondansetron (liều cao)",
            "Domperidone",
            "Hydroxychloroquine, Chloroquine"
        ]
    }


def calculate_rr_interval(hr):
    """Calculate RR interval from heart rate"""
    return 60 / hr


def render():
    """Render the QTc Calculator"""
    
    # st.title("💓 QTc - Corrected QT Interval")
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>💓 QTc - Corrected QT Interval</h3>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'qtc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    ### QT Điều chỉnh Theo Nhịp tim
    
    **QT interval:**
    - Thời gian từ bắt đầu sóng Q đến kết thúc sóng T
    - Phản ánh tái cực cơ tim
    - Bị ảnh hưởng bởi nhịp tim
    
    **QTc (QT corrected):**
    - QT điều chỉnh theo nhịp tim
    - Cho phép so sánh ở các nhịp tim khác nhau
    - Quan trọng để đánh giá nguy cơ rối loạn nhịp
    
    **Ý nghĩa lâm sàng:**
    - QTc kéo dài → Nguy cơ Torsades de Pointes (TdP)
    - TdP → Có thể tiến triển thành VF → Đột tử
    """)
    
    st.markdown("---")
    
    # Input section
    st.subheader("📊 Nhập thông số ECG")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # QT interval input
        qt_unit = st.radio(
            "**Đơn vị QT:**",
            ["milliseconds (ms)", "seconds (s)"],
            horizontal=True
        )
        
        if qt_unit == "milliseconds (ms)":
            qt_input = st.number_input(
                "**QT Interval (ms)**",
                min_value=200.0,
                max_value=800.0,
                value=400.0,
                step=10.0,
                format="%d",
                help="Đo từ đầu sóng Q đến cuối sóng T (bình thường: 350-450 ms)"
            )
            qt_ms = qt_input
        else:
            qt_input = st.number_input(
                "**QT Interval (s)**",
                min_value=0.20,
                max_value=0.80,
                value=0.40,
                step=0.01,
                format="%.2f",
                help="Đo từ đầu sóng Q đến cuối sóng T (bình thường: 0.35-0.45 s)"
            )
            qt_ms = qt_input * 1000
        
        # Heart rate input
        hr = st.number_input(
            "**Nhịp tim (bpm)**",
            min_value=30,
            max_value=200,
            value=75,
            step=1,
            format="%d",
            help="Tần số tim (bình thường: 60-100 bpm)"
        )
    
    with col2:
        # Gender selection
        gender = st.radio(
            "**Giới tính:**",
            ["Nam", "Nữ"],
            help="Ngưỡng QTc bình thường khác nhau theo giới"
        )
        
        # Formula selection
        formula = st.selectbox(
            "**Công thức tính QTc:**",
            [
                "Bazett (Phổ biến nhất)",
                "Fridericia (Chính xác hơn)",
                "Framingham (Linear)",
                "Hodges (Linear)"
            ],
            help="Bazett là phổ biến nhất nhưng kém chính xác ở nhịp nhanh/chậm"
        )
        
        # Display RR interval
        rr_interval = calculate_rr_interval(hr)
        st.metric(
            "RR Interval",
            f"{rr_interval:.2f} s",
            help="RR = 60 / HR"
        )
        
        # Smart Suggestions
        render_suggestions(
            calculator_id="qtc",
            calculator_name="QTc Calculator",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    if st.button("📈 Tính QTc", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Validate QT interval
        if qt_unit == "milliseconds (ms)":
            is_valid_qt, qt_error = validate_range(qt_input, 200.0, 800.0, "QT Interval (ms)")
        else:
            is_valid_qt, qt_error = validate_range(qt_input, 0.20, 0.80, "QT Interval (s)")
        if not is_valid_qt:
            validation_errors.append(qt_error)
        
        # Validate heart rate
        is_valid_hr, hr_error = validate_heart_rate(hr)
        if not is_valid_hr:
            validation_errors.append(hr_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        # Calculate QTc based on selected formula
        if "Bazett" in formula:
            qtc = calculate_qtc_bazett(qt_ms, hr)
            formula_text = "QTc = QT / √RR"
        elif "Fridericia" in formula:
            qtc = calculate_qtc_fridericia(qt_ms, hr)
            formula_text = "QTc = QT / ∛RR"
        elif "Framingham" in formula:
            qtc = calculate_qtc_framingham(qt_ms, hr)
            formula_text = "QTc = QT + 154 × (1 - RR)"
        else:  # Hodges
            qtc = calculate_qtc_hodges(qt_ms, hr)
            formula_text = "QTc = QT + 1.75 × (HR - 60)"
        
        # Get interpretation
        result = interpret_qtc(qtc, gender)
        
        st.markdown("---")
        st.markdown("## 📈 Kết quả")
        
        # Map severity to color
        color_map = {
            "normal": COLORS["success"],
            "borderline": COLORS["warning"],
            "prolonged": COLORS["error"],
            "severe": COLORS["error"]
        }
        box_color = color_map.get(result['severity'], COLORS["primary"])
        
        # Use render_result_box for main result
        # Use render_score_result for main result
        render_score_result(
            title="QTc (Corrected QT Interval)",
            score=f"{qtc:.0f} ms",
            interpretation=f"{result['status']} - {result['risk']}",
            mortality=result['recommendation'],
            color=box_color,
            icon=result['color'],
            size="large"
        )
        
        # Display input metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("QT Interval", f"{qt_ms:.0f} ms", help="QT đo được từ ECG")
        with col2:
            st.metric("Nhịp tim", f"{hr} bpm", help="Tần số tim")
        
        st.info(f"**Công thức:** {formula_text}")
        
        st.markdown("---")
        
        # Interpretation
        st.markdown("### 🎯 Phân tích & Đánh giá")
        
        interpretation_text = f"""
        **QTc = {qtc:.0f} ms**
        
        **Đánh giá:** {result['risk']}
        
        **Khuyến nghị:** {result['recommendation']}
        """
        
        if result['severity'] == "normal":
            st.success(interpretation_text)
        elif result['severity'] == "borderline":
            st.warning(interpretation_text)
        else:
            st.error(interpretation_text)
        
        # Reference values
        st.markdown("---")
        st.subheader("📋 Giá trị tham chiếu")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Nam:**
            - Bình thường: < 450 ms
            - Giới hạn: 450-469 ms
            - Kéo dài: 470-499 ms
            - Nghiêm trọng: ≥ 500 ms
            """)
        
        with col2:
            st.markdown("""
            **Nữ:**
            - Bình thường: < 460 ms
            - Giới hạn: 460-479 ms
            - Kéo dài: 480-499 ms
            - Nghiêm trọng: ≥ 500 ms
            """)
        
        # QT prolonging drugs
        st.markdown("---")
        st.subheader("💊 Thuốc gây kéo dài QT Thường gặp")
        
        drugs = get_qtc_prolonging_drugs()
        
        cols = st.columns(2)
        categories = list(drugs.keys())
        
        for idx, category in enumerate(categories):
            with cols[idx % 2]:
                st.markdown(f"**{category}:**")
                for drug in drugs[category]:
                    st.markdown(f"- {drug}")
        
        st.info("""
        ⚠️ **Lưu ý:** Danh sách không đầy đủ. Kiểm tra tương tác thuốc trên:
        - CredibleMeds.org
        - Micromedex
        - UpToDate Drug Interactions
        """)
        
        # Prepare inputs and results for export/history
        inputs_dict = {
            "QT Interval": f"{qt_ms:.0f} ms",
            "Heart Rate": f"{hr} bpm",
            "Gender": gender,
            "Formula": formula,
            "RR Interval": f"{rr_interval:.2f} s"
        }
        
        results_dict = {
            "QTc": f"{qtc:.0f} ms",
            "Status": result['status'],
            "Risk": result['risk'],
            "Recommendation": result['recommendation'],
            "Formula": formula_text
        }
        
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        render_export_section(
            title=f"QTc = {qtc:.0f} ms",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="QTc Calculator",
            filename="qtc_result"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="qtc",
            calculator_name="QTc Calculator",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="qtc",
            calculator_name="QTc Calculator",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="qtc", show_actions=True)
        
        # References section
        references = get_references("QTc")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Kiến thức bổ sung")
    
    with st.expander("📐 So sánh các công thức QTc"):
        st.markdown("""
        ### 1. Bazett's Formula (1920) - Phổ biến nhất
        ```
        QTc = QT / √RR
        ```
        - **Ưu điểm:** Đơn giản, được sử dụng rộng rãi
        - **Nhược điểm:** 
          + Overcorrect ở nhịp nhanh (→ QTc giả tăng)
          + Undercorrect ở nhịp chậm (→ QTc giả giảm)
        - **Khuyến cáo:** Sử dụng khi HR 60-90 bpm
        
        ### 2. Fridericia's Formula (1920) - Chính xác hơn
        ```
        QTc = QT / ∛RR
        ```
        - **Ưu điểm:** Chính xác hơn ở nhịp nhanh và chậm
        - **Nhược điểm:** Ít phổ biến, ít nghiên cứu
        - **Khuyến cáo:** Ưu tiên ở HR < 60 hoặc > 90 bpm
        
        ### 3. Framingham Formula (1992)
        ```
        QTc = QT + 154 × (1 - RR)
        ```
        - **Ưu điểm:** Linear, dễ tính
        - **Nhược điểm:** Ít validation
        - **Khuyến cáo:** Phù hợp cho population studies
        
        ### 4. Hodges Formula (1983)
        ```
        QTc = QT + 1.75 × (HR - 60)
        ```
        - **Ưu điểm:** Đơn giản, linear
        - **Nhược điểm:** Ít sử dụng trong practice
        - **Khuyến cáo:** Ít khuyến cáo
        
        **Khuyến nghị sử dụng:**
        - **HR 60-90 bpm:** Bazett
        - **HR < 60 hoặc > 90 bpm:** Fridericia
        - **Nghiên cứu:** Báo cáo cả Bazett và Fridericia
        """)
    
    with st.expander("🎯 Cách đo QT Interval chính xác"):
        st.markdown("""
        ### Kỹ thuật đo QT:
        
        **1. Chọn lead:**
        - Lead II hoặc V5/V6 (sóng T rõ nhất)
        - Tránh lead có sóng U lớn
        - Đo ở cùng một lead để so sánh
        
        **2. Xác định điểm bắt đầu (Q):**
        - Bắt đầu sóng Q (nếu có)
        - Hoặc bắt đầu sóng R (nếu không có Q)
        
        **3. Xác định điểm kết thúc (T):**
        - **Phương pháp Tangent (Khuyến cáo):**
          + Vẽ tiếp tuyến ở độ dốc xuống lớn nhất của sóng T
          + QT kết thúc khi tiếp tuyến cắt đường đẳng điện
        - **Lưu ý với sóng U:**
          + Nếu U < 50% amplitude của T → Kết thúc ở T
          + Nếu U lớn và sát T → Đo đến nadir giữa T và U
        
        **4. Tính trung bình:**
        - Đo ít nhất 3 nhịp liên tiếp
        - Lấy trung bình (hoặc trung vị nếu có outliers)
        
        **5. Điều kiện đo:**
        - Nhịp xoang đều
        - Không có extrasystoles
        - QRS bình thường (< 120 ms)
        
        **QRS wide (≥ 120 ms):**
        - Dùng công thức điều chỉnh:
          + **Bazett:** QTc = (QT - 155) / √RR + 155
          + **Hodges:** QTc = QT - (0.154 × QRS)
        """)
    
    with st.expander("⚠️ Nguyên nhân kéo dài QT"):
        st.markdown("""
        ### Nguyên nhân bẩm sinh:
        
        **Long QT Syndrome (LQTS):**
        - LQT1, LQT2, LQT3 (hay gặp nhất)
        - Đột biến gen kênh ion
        - Tiền sử gia đình ngất, đột tử
        - Trigger: stress, bơi lội, âm thanh đột ngột
        
        ### Nguyên nhân mắc phải:
        
        **1. Thuốc (Phổ biến nhất):**
        - Xem bảng thuốc phía trên
        - Tương tác thuốc (CYP3A4 inhibitors)
        - Liều cao, bolus IV
        
        **2. Rối loạn điện giải:**
        - **Hạ kali (Hypokalemia):** < 3.5 mmol/L
        - **Hạ magie (Hypomagnesemia):** < 0.7 mmol/L
        - **Hạ canxi (Hypocalcemia):** < 2.0 mmol/L
        
        **3. Bệnh tim:**
        - Nhồi máu cơ tim cấp
        - Cardiomyopathy (giãn, phì đại)
        - Viêm cơ tim
        - Bệnh mạch vành
        
        **4. Rối loạn chuyển hóa:**
        - Suy giáp (Hypothyroidism)
        - Hạ đường huyết
        - Nhịn đói kéo dài
        - Anorexia nervosa
        
        **5. Thần kinh:**
        - Xuất huyết dưới nhện
        - Tăng áp lực nội sọ
        - Đột quỵ
        
        **6. Khác:**
        - Hạ thân nhiệt
        - HIV/AIDS
        - Xơ gan
        - Bệnh thận mạn
        """)
    
    with st.expander("🚨 Torsades de Pointes (TdP)"):
        st.markdown("""
        ### Torsades de Pointes:
        
        **Đặc điểm:**
        - Nhịp nhanh thất đa hình
        - QRS "xoắn" quanh đường đẳng điện
        - Tần số 200-250 bpm
        - Thường tự giới hạn nhưng có thể → VF
        
        **Yếu tố nguy cơ cao:**
        - QTc ≥ 500 ms
        - Nữ giới (gấp 2-3 lần nam)
        - Tuổi cao
        - Bệnh tim kèm theo
        - Hạ K+, Hạ Mg2+
        - Nhịp tim chậm
        - Kéo dài QT bẩm sinh
        - Chuyển đổi gần đây từ AF về nhịp xoang
        
        **Triệu chứng:**
        - Hồi hộp, choáng váng
        - Ngất (syncope)
        - Đột tử (nếu tiến triển → VF)
        
        **Điều trị cấp cứu TdP:**
        1. **Nếu không ổn định huyết động:**
           - Sốc điện không đồng bộ ngay
           - CPR nếu không có mạch
        
        2. **Nếu ổn định:**
           - **Magnesium sulfate:** 2g IV trong 15 phút
           - Tiếp theo: 2-4 mg/phút infusion
           - Hiệu quả ngay cả khi Mg2+ bình thường
        
        3. **Điều chỉnh yếu tố nguy cơ:**
           - Dừng ngay thuốc kéo dài QT
           - Điều chỉnh K+ > 4.5 mmol/L
           - Điều chỉnh Mg2+ > 1.0 mmol/L
        
        4. **Nếu TdP tái phát:**
           - Tăng nhịp tim (ngăn pause-dependent TdP):
             + Isoproterenol infusion
             + Pacing tạm thời (90-110 bpm)
           - Lidocaine (ức chế depolarization sớm)
        
        **Phòng ngừa:**
        - Screening QTc trước khi dùng thuốc nguy cơ cao
        - Theo dõi điện giải đồ thường xuyên
        - Tránh kết hợp nhiều thuốc kéo dài QT
        - Giảm liều ở suy thận, suy gan
        """)
    
    with st.expander("💡 Quản lý kéo dài QT do thuốc"):
        st.markdown("""
        ### Khi phát hiện QTc kéo dài:
        
        **1. Đánh giá ban đầu:**
        - Xem xét tất cả thuốc đang dùng
        - Kiểm tra điện giải (K+, Mg2+, Ca2+)
        - Đánh giá chức năng thận, gan
        - Hỏi tiền sử gia đình LQTS
        
        **2. QTc 470-499 ms:**
        - Xem xét dừng/thay thế thuốc kéo dài QT
        - Điều chỉnh điện giải (K+ > 4.0, Mg2+ > 1.0)
        - Giảm liều nếu cần thiết dùng thuốc
        - Theo dõi ECG thường xuyên
        
        **3. QTc ≥ 500 ms:**
        - **Dừng ngay** thuốc kéo dài QT
        - Nhập viện theo dõi telemetry
        - Điều chỉnh tích cực K+ > 4.5, Mg2+ > 1.0
        - Tránh nhịp chậm (xem xét pacing tạm thời)
        - Hội chẩn tim mạch
        
        **4. Thay thế thuốc:**
        
        | Thuốc kéo dài QT | Thay thế an toàn hơn |
        |------------------|----------------------|
        | Azithromycin | Amoxicillin, Doxycycline |
        | Moxifloxacin | Levofloxacin (liều thấp) |
        | Fluconazole | Micafungin, Caspofungin |
        | Haloperidol | Olanzapine, Aripiprazole |
        | Citalopram | Sertraline, Vortioxetine |
        | Domperidone | Metoclopramide |
        | Ondansetron cao | Ondansetron ≤ 16mg/ngày |
        
        **5. Monitoring:**
        - Baseline ECG trước khi bắt đầu thuốc
        - Follow-up ECG:
          + Sau 1-2 tuần
          + Khi thay đổi liều
          + Khi thêm thuốc tương tác
        - Check điện giải nếu có nguy cơ (lợi tiểu, tiêu chảy)
        
        **6. Giáo dục bệnh nhân:**
        - Triệu chứng cảnh báo (ngất, hồi hộp)
        - Tránh tự ý dùng thuốc OTC
        - Thông báo với bác sĩ trước khi dùng thuốc mới
        - Website: CredibleMeds.org (kiểm tra thuốc)
        """)
    
    # Always show references at the bottom
    references = get_references("QTc")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        # Fallback to manual references
        st.markdown("---")
        st.caption("""
        **Tài liệu tham khảo:**
        - Rautaharju PM, et al. AHA/ACCF/HRS recommendations for QT interval measurement. Circulation. 2009
        - Drew BJ, et al. Prevention of TdP in hospital settings. Circulation. 2010
        - Giudicessi JR, et al. Genotype- and phenotype-guided management of LQTS. Circulation. 2018
        - Al-Khatib SM, et al. What clinicians should know about the QT interval. JAMA. 2003
        - www.CredibleMeds.org - QTdrugs List
        """)


if __name__ == "__main__":
    render()

