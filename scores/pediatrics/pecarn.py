"""
PECARN Pediatric Head Injury/Trauma Algorithm
Dự đoán nhu cầu chụp CT đầu ở trẻ chấn thương đầu
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


def evaluate_pecarn(age_months, gcs, mental_status, signs_of_basilar_skull_fracture,
                    palpable_skull_fracture, severe_mechanism, severe_headache,
                    vomiting, amnesia, loss_of_consciousness):
    """
    Evaluate PECARN criteria
    
    PECARN has different criteria for:
    - < 2 years old
    - ≥ 2 years old
    
    Returns:
        dict with risk assessment and recommendations
    """
    is_under_2 = age_months < 24
    
    # High-risk criteria (need CT)
    high_risk_found = False
    high_risk_reasons = []
    
    # Medium-risk criteria (observation vs CT)
    medium_risk_found = False
    medium_risk_reasons = []
    
    if is_under_2:
        # < 2 years old criteria
        if gcs < 15:
            high_risk_found = True
            high_risk_reasons.append("GCS < 15")
        
        if signs_of_basilar_skull_fracture:
            high_risk_found = True
            high_risk_reasons.append("Dấu hiệu vỡ nền sọ")
        
        if palpable_skull_fracture:
            high_risk_found = True
            high_risk_reasons.append("Sờ thấy vỡ xương sọ")
        
        if severe_mechanism:
            medium_risk_found = True
            medium_risk_reasons.append("Cơ chế chấn thương nặng")
        
        if severe_headache or vomiting:
            medium_risk_found = True
            if severe_headache:
                medium_risk_reasons.append("Đau đầu dữ dội")
            if vomiting:
                medium_risk_reasons.append("Nôn")
    else:
        # ≥ 2 years old criteria
        if gcs < 15:
            high_risk_found = True
            high_risk_reasons.append("GCS < 15")
        
        if signs_of_basilar_skull_fracture:
            high_risk_found = True
            high_risk_reasons.append("Dấu hiệu vỡ nền sọ")
        
        if palpable_skull_fracture:
            high_risk_found = True
            high_risk_reasons.append("Sờ thấy vỡ xương sọ")
        
        if severe_mechanism:
            medium_risk_found = True
            medium_risk_reasons.append("Cơ chế chấn thương nặng")
        
        if severe_headache:
            medium_risk_found = True
            medium_risk_reasons.append("Đau đầu dữ dội")
        
        if vomiting:
            medium_risk_found = True
            medium_risk_reasons.append("Nôn")
        
        if amnesia or loss_of_consciousness:
            medium_risk_found = True
            if amnesia:
                medium_risk_reasons.append("Mất trí nhớ")
            if loss_of_consciousness:
                medium_risk_reasons.append("Mất ý thức")
    
    # Determine recommendation
    if high_risk_found:
        return {
            "risk": "high",
            "status": "Nguy cơ cao",
            "color": COLORS["error"],
            "icon": "🔴",
            "recommendation": "Cần chụp CT đầu ngay",
            "reasons": high_risk_reasons,
            "details": "Có tiêu chuẩn nguy cơ cao → Chụp CT đầu để loại trừ tổn thương nội sọ"
        }
    elif medium_risk_found:
        return {
            "risk": "medium",
            "status": "Nguy cơ trung bình",
            "color": COLORS["warning"],
            "icon": "🟡",
            "recommendation": "Cân nhắc chụp CT đầu hoặc theo dõi sát",
            "reasons": medium_risk_reasons,
            "details": "Có tiêu chuẩn nguy cơ trung bình → Có thể chụp CT hoặc theo dõi sát tại khoa cấp cứu"
        }
    else:
        return {
            "risk": "low",
            "status": "Nguy cơ thấp",
            "color": COLORS["success"],
            "icon": "🟢",
            "recommendation": "Không cần chụp CT đầu",
            "reasons": [],
            "details": "Không có tiêu chuẩn nguy cơ → Có thể xuất viện với hướng dẫn theo dõi"
        }


def render():
    """Render PECARN calculator interface"""
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>👶 PECARN Pediatric Head Injury Algorithm</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Dự đoán nhu cầu chụp CT đầu ở trẻ chấn thương đầu</p>", unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "pecarn":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'PECARN')}")
    
    with st.expander("ℹ️ Giới thiệu về PECARN"):
        st.markdown("""
        **PECARN (Pediatric Emergency Care Applied Research Network)** là thuật toán đánh giá chấn thương đầu ở trẻ em.
        
        **Mục đích:**
        - Xác định trẻ nào cần chụp CT đầu sau chấn thương đầu
        - Giảm phơi nhiễm bức xạ không cần thiết
        - Phát hiện tổn thương nội sọ quan trọng
        
        **Tiêu chuẩn nguy cơ cao (cần CT ngay):**
        - GCS < 15
        - Dấu hiệu vỡ nền sọ
        - Sờ thấy vỡ xương sọ
        
        **Tiêu chuẩn nguy cơ trung bình (cân nhắc CT hoặc theo dõi):**
        - Cơ chế chấn thương nặng
        - Đau đầu dữ dội
        - Nôn
        - Mất trí nhớ (≥ 2 tuổi)
        - Mất ý thức (≥ 2 tuổi)
        
        **Lưu ý:**
        - Tiêu chuẩn khác nhau cho trẻ < 2 tuổi và ≥ 2 tuổi
        - Luôn kết hợp với đánh giá lâm sàng
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    age_months = st.number_input(
        "Tuổi (tháng)",
        min_value=0,
        max_value=216,  # 18 years
        value=60,
        step=1,
        help="Tuổi trẻ tính bằng tháng"
    )
    
    age_years = age_months / 12
    is_under_2 = age_months < 24
    
    if is_under_2:
        st.info(f"👶 Trẻ < 2 tuổi ({age_years:.1f} tuổi) - Áp dụng tiêu chuẩn cho trẻ nhỏ")
    else:
        st.info(f"👦 Trẻ ≥ 2 tuổi ({age_years:.1f} tuổi) - Áp dụng tiêu chuẩn cho trẻ lớn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gcs = st.number_input(
            "GCS (Glasgow Coma Scale)",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            help="Thang điểm hôn mê Glasgow"
        )
        
        mental_status = st.selectbox(
            "Tình trạng tinh thần",
            options=["Bình thường", "Bất thường (kích động, lú lẫn)"],
            index=0
        )
    
    with col2:
        signs_of_basilar_skull_fracture = st.checkbox(
            "Dấu hiệu vỡ nền sọ",
            help="Rỉ dịch não tủy, máu sau tai, dấu hiệu Battle, dấu hiệu Raccoon eyes"
        )
        
        palpable_skull_fracture = st.checkbox(
            "Sờ thấy vỡ xương sọ",
            help="Sờ thấy bất thường hoặc lún xương sọ"
        )
    
    st.markdown("#### Tiêu chuẩn nguy cơ trung bình")
    
    severe_mechanism = st.checkbox(
        "Cơ chế chấn thương nặng",
        help="Tai nạn xe cộ tốc độ cao, ngã từ độ cao > 1.5m (trẻ < 2 tuổi) hoặc > 0.9m (trẻ ≥ 2 tuổi), va chạm với vật cứng"
    )
    
    severe_headache = st.checkbox("Đau đầu dữ dội")
    vomiting = st.checkbox("Nôn")
    
    if not is_under_2:
        amnesia = st.checkbox("Mất trí nhớ (≥ 2 tuổi)")
        loss_of_consciousness = st.checkbox("Mất ý thức (≥ 2 tuổi)")
    else:
        amnesia = False
        loss_of_consciousness = False
    
    st.markdown("---")
    
    # Evaluate
    if st.button("🧮 Đánh giá PECARN", type="primary", use_container_width=True):
        result = evaluate_pecarn(
            age_months, gcs, mental_status, signs_of_basilar_skull_fracture,
            palpable_skull_fracture, severe_mechanism, severe_headache,
            vomiting, amnesia, loss_of_consciousness
        )
        
        st.subheader("📊 Kết quả")
        
        render_result_box(
            title="Đánh giá nguy cơ",
            value=result["status"],
            subtitle=result["recommendation"],
            color=result["color"],
            icon=result["icon"],
            size="large"
        )
        
        st.info(f"**Khuyến cáo:** {result['recommendation']}")
        st.info(f"**Chi tiết:** {result['details']}")
        
        if result["reasons"]:
            st.subheader("📋 Tiêu chuẩn phát hiện")
            for reason in result["reasons"]:
                st.markdown(f"- ✅ {reason}")
        
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
            - ⚠️ **Cân nhắc chụp CT đầu hoặc theo dõi sát**
            - Theo dõi tại khoa cấp cứu 4-6 giờ
            - Chụp CT nếu tình trạng xấu đi hoặc không cải thiện
            - Có thể xuất viện nếu theo dõi ổn định
            """)
        else:
            st.success("""
            - ✅ **Nguy cơ thấp - Không cần chụp CT đầu**
            - Có thể xuất viện với hướng dẫn theo dõi
            - Hướng dẫn phụ huynh theo dõi dấu hiệu cảnh báo
            - Tái khám nếu có triệu chứng mới
            """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "pecarn",
            "calculator_name": "PECARN Pediatric Head Injury Algorithm",
            "inputs": {
                "Tuổi": f"{age_months} tháng ({age_years:.1f} tuổi)",
                "GCS": str(gcs),
                "Dấu hiệu vỡ nền sọ": "Có" if signs_of_basilar_skull_fracture else "Không",
                "Sờ thấy vỡ xương sọ": "Có" if palpable_skull_fracture else "Không"
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
        render_suggestions("pecarn", result["risk"])
    
    # History
    render_history_ui("pecarn", "PECARN Pediatric Head Injury Algorithm")
    
    # References
    references = get_references("pecarn")
    if references:
        render_references_section(references)

