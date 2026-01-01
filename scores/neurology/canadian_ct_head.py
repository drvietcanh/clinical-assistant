"""
Canadian CT Head Rule
Quyết định chụp CT đầu ở chấn thương đầu nhẹ (người lớn)
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def evaluate_canadian_ct_head(age, gcs, dangerous_mechanism, amnesia_antegrade, 
                              amnesia_retrograde, vomiting, suspected_open_skull_fracture,
                              suspected_basilar_skull_fracture, multiple_depressed_fracture,
                              age_65_plus, gcs_below_15_2h, suspected_open_depressed_fracture,
                              palpable_skull_fracture, signs_of_basilar_fracture):
    """
    Evaluate Canadian CT Head Rule
    
    High-risk criteria (need CT):
    1. GCS < 15 at 2 hours post injury
    2. Suspected open or depressed skull fracture
    3. Signs of basilar skull fracture
    4. Vomiting ≥ 2 episodes
    5. Age ≥ 65 years
    
    Medium-risk criteria (consider CT):
    1. Dangerous mechanism
    2. Amnesia before impact ≥ 30 minutes
    
    Returns:
        dict with risk assessment and recommendations
    """
    high_risk_criteria = []
    medium_risk_criteria = []
    
    # High-risk criteria
    if gcs_below_15_2h:
        high_risk_criteria.append("GCS < 15 tại 2 giờ sau chấn thương")
    
    if suspected_open_depressed_fracture or palpable_skull_fracture:
        high_risk_criteria.append("Nghi ngờ vỡ xương sọ hở hoặc lún")
    
    if signs_of_basilar_fracture:
        high_risk_criteria.append("Dấu hiệu vỡ nền sọ")
    
    if vomiting >= 2:
        high_risk_criteria.append(f"Nôn ≥ 2 lần ({vomiting} lần)")
    
    if age_65_plus:
        high_risk_criteria.append("Tuổi ≥ 65 tuổi")
    
    # Medium-risk criteria
    if dangerous_mechanism:
        medium_risk_criteria.append("Cơ chế chấn thương nguy hiểm")
    
    if amnesia_retrograde >= 30:
        medium_risk_criteria.append(f"Mất trí nhớ trước chấn thương ≥ 30 phút ({amnesia_retrograde} phút)")
    
    # Determine recommendation
    if high_risk_criteria:
        return {
            "risk": "high",
            "status": "🔴 Nguy cơ cao",
            "recommendation": "Cần chụp CT đầu",
            "risk_color": COLORS["error"],
            "high_risk": high_risk_criteria,
            "medium_risk": medium_risk_criteria,
            "details": "Có tiêu chuẩn nguy cơ cao → Chụp CT đầu để loại trừ tổn thương nội sọ"
        }
    elif medium_risk_criteria:
        return {
            "risk": "medium",
            "status": "🟡 Nguy cơ trung bình",
            "recommendation": "Cân nhắc chụp CT đầu",
            "risk_color": COLORS["warning"],
            "high_risk": [],
            "medium_risk": medium_risk_criteria,
            "details": "Có tiêu chuẩn nguy cơ trung bình → Cân nhắc chụp CT đầu"
        }
    else:
        return {
            "risk": "low",
            "status": "🟢 Nguy cơ thấp",
            "recommendation": "Không cần chụp CT đầu",
            "risk_color": COLORS["success"],
            "high_risk": [],
            "medium_risk": [],
            "details": "Không có tiêu chuẩn nguy cơ → Có thể xuất viện với hướng dẫn theo dõi"
        }


def render():
    """Render Canadian CT Head Rule calculator interface"""
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🧠 Canadian CT Head Rule</h2>
    <p style='text-align: center;'><em>Quyết định chụp CT đầu ở chấn thương đầu nhẹ (người lớn)</em></p>
    """, unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "canadian_ct_head":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Canadian CT Head Rule')}")
    
    with st.expander("ℹ️ Giới thiệu về Canadian CT Head Rule"):
        st.markdown("""
        **Canadian CT Head Rule** là quy tắc quyết định chụp CT đầu ở bệnh nhân chấn thương đầu nhẹ (người lớn).
        
        **Tiêu chuẩn nguy cơ cao (cần CT):**
        1. GCS < 15 tại 2 giờ sau chấn thương
        2. Nghi ngờ vỡ xương sọ hở hoặc lún
        3. Dấu hiệu vỡ nền sọ
        4. Nôn ≥ 2 lần
        5. Tuổi ≥ 65 tuổi
        
        **Tiêu chuẩn nguy cơ trung bình (cân nhắc CT):**
        1. Cơ chế chấn thương nguy hiểm
        2. Mất trí nhớ trước chấn thương ≥ 30 phút
        
        **Lưu ý:**
        - Áp dụng cho chấn thương đầu nhẹ (GCS 13-15)
        - Giảm phơi nhiễm bức xạ không cần thiết
        - Luôn kết hợp với đánh giá lâm sàng
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    age = st.number_input(
        "Tuổi (năm)",
        min_value=16,
        max_value=120,
        value=40,
        step=1
    )
    
    age_65_plus = age >= 65
    
    col1, col2 = st.columns(2)
    
    with col1:
        gcs = st.number_input(
            "GCS hiện tại",
            min_value=3,
            max_value=15,
            value=15,
            step=1
        )
        
        gcs_below_15_2h = st.checkbox(
            "GCS < 15 tại 2 giờ sau chấn thương",
            help="GCS vẫn < 15 sau 2 giờ"
        )
    
    with col2:
        vomiting = st.number_input(
            "Số lần nôn",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )
        
        dangerous_mechanism = st.checkbox(
            "Cơ chế chấn thương nguy hiểm",
            help="Tai nạn xe cộ tốc độ cao, ngã từ độ cao > 1m, va chạm với vật cứng"
        )
    
    st.markdown("#### Dấu hiệu vỡ xương sọ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        suspected_open_depressed_fracture = st.checkbox(
            "Nghi ngờ vỡ xương sọ hở",
            help="Vết thương hở ở đầu"
        )
        
        palpable_skull_fracture = st.checkbox(
            "Sờ thấy vỡ xương sọ",
            help="Sờ thấy bất thường hoặc lún xương sọ"
        )
    
    with col2:
        signs_of_basilar_fracture = st.checkbox(
            "Dấu hiệu vỡ nền sọ",
            help="Rỉ dịch não tủy, máu sau tai, dấu hiệu Battle, dấu hiệu Raccoon eyes"
        )
    
    st.markdown("#### Mất trí nhớ")
    
    amnesia_retrograde = st.number_input(
        "Mất trí nhớ trước chấn thương (phút)",
        min_value=0,
        max_value=1440,
        value=0,
        step=5,
        help="Thời gian mất trí nhớ trước khi chấn thương xảy ra"
    )
    
    st.markdown("---")
    
    # Evaluate
    if st.button("🧮 Đánh giá Canadian CT Head Rule", type="primary", use_container_width=True):
        result = evaluate_canadian_ct_head(
            age, gcs, dangerous_mechanism, False, amnesia_retrograde,
            vomiting, False, signs_of_basilar_fracture, False,
            age_65_plus, gcs_below_15_2h, suspected_open_depressed_fracture,
            palpable_skull_fracture, signs_of_basilar_fracture
        )
        
        st.subheader("📊 Kết quả")
        
        render_result_box(
            title="Đánh giá nguy cơ",
            value=result["status"],
            unit="",
            status=result["risk_color"]
        )
        
        st.info(f"**Khuyến cáo:** {result['recommendation']}")
        st.info(f"**Chi tiết:** {result['details']}")
        
        if result["high_risk"]:
            st.subheader("🔴 Tiêu chuẩn nguy cơ cao")
            for criterion in result["high_risk"]:
                st.markdown(f"- ⚠️ {criterion}")
        
        if result["medium_risk"]:
            st.subheader("🟡 Tiêu chuẩn nguy cơ trung bình")
            for criterion in result["medium_risk"]:
                st.markdown(f"- ⚠️ {criterion}")
        
        # Recommendations
        st.subheader("💡 Khuyến cáo lâm sàng")
        if result["risk"] == "high":
            st.error("""
            - ⚠️ **Cần chụp CT đầu ngay lập tức**
            - Theo dõi sát dấu hiệu thần kinh
            - Chuẩn bị can thiệp nếu cần
            """)
        elif result["risk"] == "medium":
            st.warning("""
            - ⚠️ **Cân nhắc chụp CT đầu**
            - Theo dõi tại khoa cấp cứu
            - Chụp CT nếu tình trạng xấu đi
            """)
        else:
            st.success("""
            - ✅ **Nguy cơ thấp - Không cần chụp CT đầu**
            - Có thể xuất viện với hướng dẫn theo dõi
            - Hướng dẫn bệnh nhân theo dõi dấu hiệu cảnh báo
            - Tái khám nếu có triệu chứng mới
            """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "canadian_ct_head",
            "calculator_name": "Canadian CT Head Rule",
            "inputs": {
                "Tuổi": f"{age} tuổi",
                "GCS": str(gcs),
                "Nôn": f"{vomiting} lần"
            },
            "results": {
                "Đánh giá": result["status"],
                "Khuyến cáo": result["recommendation"]
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
        
        # Suggestions
        render_suggestions("canadian_ct_head", result["risk"])
    
    # History
    render_history_ui("canadian_ct_head", "Canadian CT Head Rule")
    
    # References
    references = get_references("canadian_ct_head")
    if references:
        render_references_section(references)

