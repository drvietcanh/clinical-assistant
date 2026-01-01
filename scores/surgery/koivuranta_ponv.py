"""
Koivuranta PONV Risk Score Calculator
Nguy cơ buồn nôn nôn sau mổ - Phiên bản mở rộng
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
from scores.utils.validation import validate_input_range


def calculate_koivuranta_ponv(female, non_smoker, history_ponv, duration_surgery, type_anesthesia):
    """
    Tính điểm Koivuranta PONV Risk Score
    
    Parameters:
    - female: Nữ giới
    - non_smoker: Không hút thuốc
    - history_ponv: Tiền sử PONV
    - duration_surgery: Thời gian phẫu thuật (phút)
    - type_anesthesia: Loại gây mê (0=regional, 1=general)
    
    Returns:
    - dict với risk_score, risk_percentage, và recommendations
    """
    risk_factors = 0
    
    if female:
        risk_factors += 1
    if non_smoker:
        risk_factors += 1
    if history_ponv:
        risk_factors += 1
    if duration_surgery >= 60:  # ≥60 phút
        risk_factors += 1
    if type_anesthesia == 1:  # General anesthesia
        risk_factors += 1
    
    # Risk percentages based on Koivuranta et al. 1997
    risk_percentages = {
        0: 6,    # 6% risk
        1: 18,   # 18% risk
        2: 32,   # 32% risk
        3: 50,   # 50% risk
        4: 65,   # 65% risk
        5: 78    # 78% risk
    }
    
    risk_pct = risk_percentages.get(risk_factors, 6)
    
    # Recommendations
    if risk_factors <= 1:
        recommendation = "Nguy cơ thấp - Không cần dự phòng thường quy"
        prophylaxis = "Không cần thiết hoặc dự phòng đơn giản"
    elif risk_factors == 2:
        recommendation = "Nguy cơ trung bình - Cân nhắc dự phòng"
        prophylaxis = "Dùng 1-2 thuốc chống nôn (ondansetron hoặc dexamethasone)"
    elif risk_factors == 3:
        recommendation = "Nguy cơ cao - Nên dự phòng"
        prophylaxis = "Dùng 2 thuốc chống nôn kết hợp (ondansetron + dexamethasone)"
    else:  # 4-5 factors
        recommendation = "Nguy cơ rất cao - Bắt buộc dự phòng đa thuốc"
        prophylaxis = "Dùng 2-3 thuốc chống nôn kết hợp:\n- Ondansetron 4mg IV\n- Dexamethasone 4-8mg IV\n- Cân nhắc droperidol hoặc TIVA"
    
    return {
        "risk_factors": risk_factors,
        "risk_percentage": risk_pct,
        "recommendation": recommendation,
        "prophylaxis": prophylaxis
    }


def render():
    """Render Koivuranta PONV Risk Score interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'koivuranta_ponv':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🤢 Koivuranta PONV Risk Score</h2>
    <p style='text-align: center;'><em>Nguy cơ buồn nôn nôn sau mổ - Phiên bản mở rộng</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Koivuranta PONV Risk Score"):
        st.markdown("""
        **Koivuranta PONV Risk Score** là thang điểm mở rộng để dự đoán nguy cơ PONV,
        bao gồm thêm yếu tố thời gian phẫu thuật và loại gây mê so với Apfel Score.
        
        **5 yếu tố nguy cơ:**
        1. **Nữ giới**
        2. **Không hút thuốc**
        3. **Tiền sử PONV**
        4. **Thời gian phẫu thuật ≥60 phút**
        5. **Gây mê toàn thân** (thay vì gây tê vùng)
        
        **Nguy cơ theo số yếu tố:**
        - **0 yếu tố:** 6% nguy cơ
        - **1 yếu tố:** 18% nguy cơ
        - **2 yếu tố:** 32% nguy cơ
        - **3 yếu tố:** 50% nguy cơ
        - **4 yếu tố:** 65% nguy cơ
        - **5 yếu tố:** 78% nguy cơ
        
        **So sánh với Apfel Score:**
        - Koivuranta bao gồm thêm thời gian phẫu thuật và loại gây mê
        - Hữu ích khi cần đánh giá chi tiết hơn
        
        **Reference:** Koivuranta M, et al. A survey of postoperative nausea and vomiting. 
        Anaesthesia. 1997;52(5):443-9.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 5 yếu tố nguy cơ")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="koivuranta_ponv",
            calculator_name="Koivuranta PONV Risk Score",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Risk factors
    female = st.checkbox("1️⃣ Nữ giới", key="koivuranta_female")
    non_smoker = st.checkbox("2️⃣ Không hút thuốc", key="koivuranta_nonsmoker")
    history_ponv = st.checkbox("3️⃣ Tiền sử PONV", key="koivuranta_history")
    
    duration_surgery = st.number_input(
        "4️⃣ Thời gian phẫu thuật (phút)",
        min_value=0,
        max_value=600,
        value=60,
        step=5,
        key="koivuranta_duration"
    )
    
    type_anesthesia = st.radio(
        "5️⃣ Loại gây mê",
        options=[0, 1],
        format_func=lambda x: {
            0: "Gây tê vùng (Regional anesthesia)",
            1: "Gây mê toàn thân (General anesthesia)"
        }[x],
        key="koivuranta_anesthesia"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Koivuranta PONV", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_input_range(duration_surgery, "Thời gian phẫu thuật", 0, 600, "phút")
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_koivuranta_ponv(female, non_smoker, history_ponv, duration_surgery, type_anesthesia)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Số yếu tố nguy cơ", f"{result['risk_factors']}/5")
            
            with col2:
                st.metric("Nguy cơ PONV", f"{result['risk_percentage']}%")
            
            st.markdown("---")
            
            # Risk interpretation
            if result['risk_factors'] <= 1:
                st.success(f"**{result['recommendation']}**")
            elif result['risk_factors'] == 2:
                st.info(f"**{result['recommendation']}**")
            elif result['risk_factors'] == 3:
                st.warning(f"**{result['recommendation']}**")
            else:
                st.error(f"**{result['recommendation']}**")
            
            st.markdown("---")
            
            st.subheader("💊 Khuyến nghị dự phòng")
            st.markdown(f"""
            {result['prophylaxis']}
            """)
            
            st.markdown("---")
            
            # Show which factors are present
            st.subheader("📋 Yếu tố nguy cơ hiện tại")
            factors_list = []
            if female:
                factors_list.append("✅ Nữ giới")
            if non_smoker:
                factors_list.append("✅ Không hút thuốc")
            if history_ponv:
                factors_list.append("✅ Tiền sử PONV")
            if duration_surgery >= 60:
                factors_list.append(f"✅ Thời gian phẫu thuật ≥60 phút ({duration_surgery} phút)")
            if type_anesthesia == 1:
                factors_list.append("✅ Gây mê toàn thân")
            
            if factors_list:
                for factor in factors_list:
                    st.markdown(f"- {factor}")
            else:
                st.markdown("- Không có yếu tố nguy cơ")
            
            # Prepare data for history and share
            inputs_dict = {
                "Nữ giới": "Có" if female else "Không",
                "Không hút thuốc": "Có" if non_smoker else "Không",
                "Tiền sử PONV": "Có" if history_ponv else "Không",
                "Thời gian phẫu thuật": f"{duration_surgery} phút",
                "Loại gây mê": "Gây mê toàn thân" if type_anesthesia == 1 else "Gây tê vùng"
            }
            
            results_dict = {
                "Số yếu tố nguy cơ": f"{result['risk_factors']}/5",
                "Nguy cơ PONV": f"{result['risk_percentage']}%",
                "Khuyến nghị": result['recommendation'],
                "Dự phòng": result['prophylaxis']
            }
            
            # Export section
            render_export_section(
                title="Koivuranta PONV Risk Score",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="Koivuranta PONV Risk Score"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="koivuranta_ponv",
                calculator_name="Koivuranta PONV Risk Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="koivuranta_ponv",
                calculator_name="Koivuranta PONV Risk Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="koivuranta_ponv", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("koivuranta_ponv")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

