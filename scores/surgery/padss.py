"""
PADSS - Post-Anesthesia Discharge Scoring System Calculator
Tiêu chuẩn xuất viện sau gây mê ngoại trú
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
from scores.utils.anesthesia_validation import validate_padss_components


def calculate_padss(vitals, ambulation, nausea_vomiting, pain, bleeding):
    """
    Tính điểm PADSS
    
    Parameters (mỗi thành phần 0-2 điểm):
    - vitals: Dấu hiệu sinh tồn (0=abnormal, 1=20% change, 2=baseline)
    - ambulation: Đi lại (0=no, 1=with assistance, 2=steady gait)
    - nausea_vomiting: Buồn nôn nôn (0=severe, 1=moderate, 2=minimal/none)
    - pain: Đau (0=severe, 1=moderate, 2=minimal/none)
    - bleeding: Chảy máu (0=severe, 1=moderate, 2=minimal/none)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = vitals + ambulation + nausea_vomiting + pain + bleeding
    
    # Interpretation
    if total >= 9:
        status = "Đủ tiêu chuẩn xuất viện"
        recommendation = "Có thể xuất viện về nhà (nếu phẫu thuật ngoại trú)"
        color = "green"
    else:
        status = "Chưa đủ tiêu chuẩn"
        recommendation = "Cần tiếp tục theo dõi tại phòng hồi tỉnh, đánh giá lại sau 30-60 phút"
        color = "orange"
    
    return {
        "total_score": total,
        "status": status,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render PADSS interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'padss':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'PADSS')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🏥 PADSS - Post-Anesthesia Discharge Scoring System</h2>
    <p style='text-align: center;'><em>Tiêu chuẩn xuất viện sau gây mê ngoại trú</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về PADSS"):
        st.markdown("""
        **PADSS (Post-Anesthesia Discharge Scoring System)** là thang điểm đánh giá khả năng 
        xuất viện sau gây mê ngoại trú, giúp quyết định khi nào bệnh nhân có thể về nhà an toàn.
        
        **5 thành phần (mỗi thành phần 0-2 điểm, tổng 10 điểm):**
        
        1. **Dấu hiệu sinh tồn (Vital Signs)**
           - 2 điểm: Trở về baseline (trước phẫu thuật)
           - 1 điểm: Thay đổi 20% so với baseline
           - 0 điểm: Bất thường
        
        2. **Đi lại (Ambulation)**
           - 2 điểm: Đi lại vững vàng
           - 1 điểm: Đi lại với hỗ trợ
           - 0 điểm: Không thể đi lại
        
        3. **Buồn nôn nôn (Nausea/Vomiting)**
           - 2 điểm: Tối thiểu/không có
           - 1 điểm: Trung bình
           - 0 điểm: Nặng
        
        4. **Đau (Pain)**
           - 2 điểm: Tối thiểu/không có
           - 1 điểm: Trung bình
           - 0 điểm: Nặng
        
        5. **Chảy máu (Bleeding)**
           - 2 điểm: Tối thiểu/không có
           - 1 điểm: Trung bình
           - 0 điểm: Nặng
        
        **Tiêu chuẩn xuất viện:**
        - **Điểm ≥9/10:** Đủ tiêu chuẩn xuất viện
        - **Điểm <9:** Cần tiếp tục theo dõi
        
        **So sánh với Aldrete Score:**
        - Aldrete: Đánh giá xuất phòng hồi tỉnh (PACU)
        - PADSS: Đánh giá xuất viện về nhà (sau khi đã xuất PACU)
        
        **Reference:** Chung F, et al. A post-anesthetic discharge scoring system for determining 
        readiness for discharge in ambulatory surgery patients. J Clin Anesth. 1995;7(6):500-6.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 5 thành phần (mỗi thành phần 0-2 điểm)")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="padss",
            calculator_name="PADSS",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Vital signs
    st.markdown("### 1️⃣ Dấu hiệu sinh tồn (Vital Signs)")
    vitals = st.radio(
        "So với baseline (trước phẫu thuật):",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Trở về baseline",
            1: "1 điểm - Thay đổi 20% so với baseline",
            0: "0 điểm - Bất thường (BP, HR, RR, SpO₂)"
        }[x],
        key="padss_vitals",
        horizontal=False
    )
    
    # Ambulation
    st.markdown("### 2️⃣ Đi lại (Ambulation)")
    ambulation = st.radio(
        "Khả năng đi lại:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Đi lại vững vàng (steady gait)",
            1: "1 điểm - Đi lại với hỗ trợ",
            0: "0 điểm - Không thể đi lại"
        }[x],
        key="padss_ambulation",
        horizontal=False
    )
    
    # Nausea/Vomiting
    st.markdown("### 3️⃣ Buồn nôn nôn (Nausea/Vomiting)")
    nausea_vomiting = st.radio(
        "Mức độ buồn nôn nôn:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Tối thiểu/không có",
            1: "1 điểm - Trung bình",
            0: "0 điểm - Nặng (nôn nhiều lần)"
        }[x],
        key="padss_nausea",
        horizontal=False
    )
    
    # Pain
    st.markdown("### 4️⃣ Đau (Pain)")
    pain = st.radio(
        "Mức độ đau:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Tối thiểu/không có (NRS 0-3)",
            1: "1 điểm - Trung bình (NRS 4-6)",
            0: "0 điểm - Nặng (NRS 7-10)"
        }[x],
        key="padss_pain",
        horizontal=False
    )
    
    # Bleeding
    st.markdown("### 5️⃣ Chảy máu (Bleeding)")
    bleeding = st.radio(
        "Mức độ chảy máu:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Tối thiểu/không có",
            1: "1 điểm - Trung bình (cần thay băng)",
            0: "0 điểm - Nặng (chảy máu nhiều, cần can thiệp)"
        }[x],
        key="padss_bleeding",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm PADSS", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_padss_components(vitals, ambulation, nausea_vomiting, pain, bleeding)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_padss(vitals, ambulation, nausea_vomiting, pain, bleeding)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/10")
            
            with col2:
                st.metric("Tình trạng", result['status'])
            
            st.markdown("---")
            
            # Status interpretation
            if result['color'] == "green":
                st.success(f"**{result['status']}**")
            else:
                st.warning(f"**{result['status']}**")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Breakdown
            st.subheader("📋 Chi tiết điểm số")
            components = [
                ("Dấu hiệu sinh tồn", vitals, 2),
                ("Đi lại", ambulation, 2),
                ("Buồn nôn nôn", nausea_vomiting, 2),
                ("Đau", pain, 2),
                ("Chảy máu", bleeding, 2)
            ]
            
            for name, score, max_score in components:
                percentage = (score / max_score) * 100
                st.progress(percentage / 100, text=f"{name}: {score}/{max_score}")
            
            # Prepare data for history and share
            inputs_dict = {
                "Dấu hiệu sinh tồn": f"{vitals}/2",
                "Đi lại": f"{ambulation}/2",
                "Buồn nôn nôn": f"{nausea_vomiting}/2",
                "Đau": f"{pain}/2",
                "Chảy máu": f"{bleeding}/2"
            }
            
            results_dict = {
                "Tổng điểm": f"{result['total_score']}/10",
                "Tình trạng": result['status'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Export section
            render_export_section(
                calculator_id="padss",
                calculator_name="PADSS",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="padss",
                calculator_name="PADSS",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="padss",
                calculator_name="PADSS",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="padss", show_actions=True)
            
            st.markdown("---")
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # Additional information
    with st.expander("📚 Thông tin bổ sung"):
            st.markdown("""
            **Quy trình xuất viện sau gây mê ngoại trú:**
            
            1. **Xuất phòng hồi tỉnh (PACU):**
               - Sử dụng Aldrete Score (≥9/10)
               - Bệnh nhân ổn định về dấu hiệu sinh tồn
            
            2. **Xuất viện về nhà:**
               - Sử dụng PADSS (≥9/10)
               - Bệnh nhân có thể tự chăm sóc
               - Có người đưa về nhà
            
            **Yêu cầu trước khi xuất viện:**
            - Điểm PADSS ≥9/10
            - Có người đưa về nhà
            - Đã được hướng dẫn chăm sóc sau phẫu thuật
            - Có số điện thoại liên hệ trong trường hợp khẩn cấp
            - Không lái xe trong 24 giờ
            - Không làm việc quan trọng trong 24 giờ
            
            **Chống chỉ định xuất viện:**
            - Điểm PADSS <9
            - Có biến chứng nghiêm trọng
            - Không có người đưa về nhà
            - Bệnh nhân từ chối xuất viện
            """)
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("padss")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

