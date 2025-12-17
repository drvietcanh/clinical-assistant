"""
El-Ganzouri Risk Index Calculator
Đánh giá nguy cơ đặt nội khí quản khó
"""

import streamlit as st
from scores.utils.anesthesia_validation import validate_el_ganzouri_score
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_el_ganzouri(
    mouth_opening, thyromental_distance, mallampati, neck_movement,
    jaw_protrusion, weight, history_difficult_intubation
):
    """
    Tính điểm El-Ganzouri Risk Index
    
    Parameters:
    - mouth_opening: Mở miệng (0=≥4cm, 1=3-4cm, 2=<3cm)
    - thyromental_distance: Khoảng cách thyromental (0=≥6.5cm, 1=6-6.5cm, 2=<6cm)
    - mallampati: Mallampati class (0=I-II, 1=III, 2=IV)
    - neck_movement: Cử động cổ (0=normal, 1=limited, 2=severe)
    - jaw_protrusion: Đưa hàm ra (0=normal, 1=limited, 2=impossible)
    - weight: Cân nặng (0=normal, 1=obese)
    - history_difficult_intubation: Tiền sử đặt NKQ khó (0=no, 1=yes)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = (mouth_opening + thyromental_distance + mallampati + 
             neck_movement + jaw_protrusion + weight + history_difficult_intubation)
    
    # Interpretation based on El-Ganzouri et al. 1996
    if total <= 3:
        risk = "Nguy cơ thấp"
        probability = "5-10%"
        recommendation = "Gây mê tiêu chuẩn, bác sĩ gây mê thường quy"
        color = "green"
    elif total <= 5:
        risk = "Nguy cơ trung bình"
        probability = "20-30%"
        recommendation = "Chuẩn bị dụng cụ đường thở khó, có bác sĩ gây mê giàu kinh nghiệm"
        color = "orange"
    else:  # ≥6
        risk = "Nguy cơ cao"
        probability = "40-60%"
        recommendation = "Bắt buộc có bác sĩ gây mê giàu kinh nghiệm, chuẩn bị đầy đủ dụng cụ, cân nhắc đặt NKQ tỉnh"
        color = "red"
    
    return {
        "total_score": total,
        "risk": risk,
        "probability": probability,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render El-Ganzouri Risk Index interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'el_ganzouri':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🔍 El-Ganzouri Risk Index</h2>
    <p style='text-align: center;'><em>Đánh giá nguy cơ đặt nội khí quản khó</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về El-Ganzouri Risk Index"):
        st.markdown("""
        **El-Ganzouri Risk Index** là thang điểm chi tiết để đánh giá nguy cơ đặt nội khí quản khó,
        bao gồm 7 yếu tố quan trọng.
        
        **7 yếu tố đánh giá:**
        1. **Mở miệng** (Inter-incisor gap)
        2. **Khoảng cách thyromental** (Thyromental distance)
        3. **Mallampati classification**
        4. **Cử động cổ** (Neck movement)
        5. **Đưa hàm ra** (Jaw protrusion)
        6. **Cân nặng** (Weight)
        7. **Tiền sử đặt NKQ khó** (History of difficult intubation)
        
        **Điểm số và nguy cơ:**
        - **≤3 điểm:** Nguy cơ thấp (5-10% đặt NKQ khó)
        - **4-5 điểm:** Nguy cơ trung bình (20-30% đặt NKQ khó)
        - **≥6 điểm:** Nguy cơ cao (40-60% đặt NKQ khó)
        
        **Ưu điểm:**
        - Bao gồm tiền sử đặt NKQ khó (yếu tố dự đoán mạnh nhất)
        - Đánh giá chi tiết hơn Wilson Score
        
        **Reference:** El-Ganzouri AR, et al. Preoperative airway assessment: predictive value of a 
        multivariate risk index. Anesth Analg. 1996;82(6):1197-204.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 7 yếu tố")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="el_ganzouri",
            calculator_name="El-Ganzouri Risk Index",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Mouth opening
    st.markdown("### 1️⃣ Mở miệng (Inter-incisor gap)")
    mouth_opening = st.radio(
        "Khoảng cách giữa 2 răng cửa:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - ≥4cm",
            1: "1 điểm - 3-4cm",
            2: "2 điểm - <3cm"
        }[x],
        key="elganzouri_mouth",
        horizontal=False
    )
    
    # Thyromental distance
    st.markdown("### 2️⃣ Khoảng cách thyromental")
    thyromental_distance = st.radio(
        "Khoảng cách từ xương giáp đến cằm:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - ≥6.5cm",
            1: "1 điểm - 6-6.5cm",
            2: "2 điểm - <6cm"
        }[x],
        key="elganzouri_thyromental",
        horizontal=False
    )
    
    # Mallampati
    st.markdown("### 3️⃣ Mallampati Classification")
    mallampati = st.radio(
        "Phân loại Mallampati:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Class I-II",
            1: "1 điểm - Class III",
            2: "2 điểm - Class IV"
        }[x],
        key="elganzouri_mallampati",
        horizontal=False
    )
    st.caption("Xem Mallampati Classification calculator để đánh giá")
    
    # Neck movement
    st.markdown("### 4️⃣ Cử động cổ")
    neck_movement = st.radio(
        "Khả năng duỗi cổ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường",
            1: "1 điểm - Hạn chế",
            2: "2 điểm - Nghiêm trọng"
        }[x],
        key="elganzouri_neck",
        horizontal=False
    )
    
    # Jaw protrusion
    st.markdown("### 5️⃣ Đưa hàm ra (Jaw protrusion)")
    jaw_protrusion = st.radio(
        "Khả năng đưa hàm dưới ra trước:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường",
            1: "1 điểm - Hạn chế",
            2: "2 điểm - Không thể"
        }[x],
        key="elganzouri_jaw",
        horizontal=False
    )
    
    # Weight
    st.markdown("### 6️⃣ Cân nặng")
    weight = st.radio(
        "BMI:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (BMI <30)",
            1: "1 điểm - Béo phì (BMI ≥30)"
        }[x],
        key="elganzouri_weight",
        horizontal=False
    )
    
    # History
    st.markdown("### 7️⃣ Tiền sử đặt NKQ khó")
    history_difficult_intubation = st.radio(
        "Có tiền sử đặt nội khí quản khó:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Không",
            1: "1 điểm - Có (YẾU TỐ QUAN TRỌNG NHẤT)"
        }[x],
        key="elganzouri_history",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm El-Ganzouri", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_el_ganzouri_score(
            mouth_opening, thyromental_distance, mallampati, neck_movement,
            jaw_protrusion, weight, history_difficult_intubation
        )
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_el_ganzouri(
                mouth_opening, thyromental_distance, mallampati, neck_movement,
                jaw_protrusion, weight, history_difficult_intubation
            )
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/11")
            
            with col2:
                st.metric("Nguy cơ", result['risk'])
            
            with col3:
                st.metric("Xác suất", result['probability'])
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == "green":
                st.success(f"**{result['risk']}** - Xác suất đặt NKQ khó: {result['probability']}")
            elif result['color'] == "orange":
                st.warning(f"**{result['risk']}** - Xác suất đặt NKQ khó: {result['probability']}")
            else:
                st.error(f"**{result['risk']}** - Xác suất đặt NKQ khó: {result['probability']}")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Warning if history present
            if history_difficult_intubation == 1:
                st.warning("""
            ⚠️ **CẢNH BÁO:** Bệnh nhân có tiền sử đặt NKQ khó - Đây là yếu tố dự đoán mạnh nhất!
            
            **Bắt buộc:**
            - Xem lại hồ sơ gây mê trước đó
            - Chuẩn bị đầy đủ dụng cụ đường thở khó
            - Có bác sĩ gây mê giàu kinh nghiệm
            - Cân nhắc đặt NKQ tỉnh với fiberoptic
            - Thông báo cho đội ngũ phẫu thuật
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Mở miệng": {0: "≥4cm", 1: "3-4cm", 2: "<3cm"}[mouth_opening],
                "Khoảng cách thyromental": {0: "≥6.5cm", 1: "6-6.5cm", 2: "<6cm"}[thyromental_distance],
                "Mallampati": {0: "I-II", 1: "III", 2: "IV"}[mallampati],
                "Cử động cổ": {0: "Bình thường", 1: "Hạn chế", 2: "Nghiêm trọng"}[neck_movement],
                "Đưa hàm ra": {0: "Bình thường", 1: "Hạn chế", 2: "Không thể"}[jaw_protrusion],
                "Cân nặng": "Béo phì" if weight == 1 else "Bình thường",
                "Tiền sử đặt NKQ khó": "Có" if history_difficult_intubation == 1 else "Không"
            }
            
            results_dict = {
                "Tổng điểm": f"{result['total_score']}/11",
                "Nguy cơ": result['risk'],
                "Xác suất": result['probability'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Save to history
            # Export section
            render_export_section(
                title="El-Ganzouri Risk Index",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="El-Ganzouri Risk Index"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="el_ganzouri",
                calculator_name="El-Ganzouri Risk Index",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="el_ganzouri",
                calculator_name="El-Ganzouri Risk Index",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="el_ganzouri", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("El-Ganzouri")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

