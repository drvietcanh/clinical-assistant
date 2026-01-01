"""
Wilson Risk Score Calculator
Dự đoán đặt nội khí quản khó
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
from scores.utils.anesthesia_validation import validate_wilson_score


def calculate_wilson_risk(weight, head_neck_movement, jaw_movement, receding_mandible, buck_teeth):
    """
    Tính điểm Wilson Risk Score
    
    Parameters (mỗi yếu tố 0-2 điểm):
    - weight: Cân nặng (0=normal, 1=obese, 2=morbidly obese)
    - head_neck_movement: Cử động đầu cổ (0=normal, 1=limited, 2=severe)
    - jaw_movement: Cử động hàm (0=normal, 1=limited, 2=severe)
    - receding_mandible: Hàm lùi (0=no, 1=moderate, 2=severe)
    - buck_teeth: Răng hô (0=no, 1=moderate, 2=severe)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = weight + head_neck_movement + jaw_movement + receding_mandible + buck_teeth
    
    # Interpretation
    if total <= 1:
        risk = "Nguy cơ thấp"
        difficulty = "Đặt NKQ dễ dàng"
        recommendation = "Gây mê tiêu chuẩn, bác sĩ gây mê thường quy"
        color = COLORS["success"]
    elif total == 2:
        risk = "Nguy cơ trung bình"
        difficulty = "Có thể đặt NKQ khó"
        recommendation = "Chuẩn bị dụng cụ đường thở khó, có bác sĩ gây mê giàu kinh nghiệm"
        color = COLORS["warning"]
    else:  # ≥3
        risk = "Nguy cơ cao"
        difficulty = "Đặt NKQ khó - Cần chuẩn bị đặc biệt"
        recommendation = "Bắt buộc có bác sĩ gây mê giàu kinh nghiệm, chuẩn bị đầy đủ dụng cụ đường thở khó (video laryngoscope, LMA, fiberoptic), cân nhắc đặt NKQ tỉnh"
        color = COLORS["error"]
    
    return {
        "total_score": total,
        "risk": risk,
        "difficulty": difficulty,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render Wilson Risk Score interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'wilson_risk':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Wilson Risk Score')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🔍 Wilson Risk Score</h2>
    <p style='text-align: center;'><em>Dự đoán đặt nội khí quản khó</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Wilson Risk Score"):
        st.markdown("""
        **Wilson Risk Score** là thang điểm đánh giá nguy cơ đặt nội khí quản khó,
        giúp bác sĩ gây mê chuẩn bị trước phẫu thuật.
        
        **5 yếu tố đánh giá (mỗi yếu tố 0-2 điểm):**
        1. **Cân nặng** - Béo phì làm tăng nguy cơ
        2. **Cử động đầu cổ** - Hạn chế cử động làm tăng nguy cơ
        3. **Cử động hàm** - Hạn chế mở miệng làm tăng nguy cơ
        4. **Hàm lùi (Receding mandible)** - Hàm nhỏ/lùi làm tăng nguy cơ
        5. **Răng hô (Buck teeth)** - Răng hô làm tăng nguy cơ
        
        **Điểm số:**
        - **0-1 điểm:** Nguy cơ thấp - Đặt NKQ dễ dàng
        - **2 điểm:** Nguy cơ trung bình - Có thể đặt NKQ khó
        - **≥3 điểm:** Nguy cơ cao - Đặt NKQ khó, cần chuẩn bị đặc biệt
        
        **Reference:** Wilson ME, et al. Predicting difficult intubation. 
        Br J Anaesth. 1988;61(2):211-6.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 5 yếu tố (mỗi yếu tố 0-2 điểm)")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="wilson_risk",
            calculator_name="Wilson Risk Score",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Weight
    st.markdown("### 1️⃣ Cân nặng")
    weight = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (BMI <30)",
            1: "1 điểm - Béo phì (BMI 30-40)",
            2: "2 điểm - Béo phì nặng (BMI >40)"
        }[x],
        key="wilson_weight",
        horizontal=False
    )
    
    # Head/Neck movement
    st.markdown("### 2️⃣ Cử động đầu cổ")
    head_neck_movement = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (≥90° extension)",
            1: "1 điểm - Hạn chế (30-90° extension)",
            2: "2 điểm - Nghiêm trọng (<30° extension)"
        }[x],
        key="wilson_head_neck",
        horizontal=False
    )
    
    # Jaw movement
    st.markdown("### 3️⃣ Cử động hàm (mở miệng)")
    jaw_movement = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (IGD ≥5cm)",
            1: "1 điểm - Hạn chế (IGD 3-5cm)",
            2: "2 điểm - Nghiêm trọng (IGD <3cm)"
        }[x],
        key="wilson_jaw",
        horizontal=False
    )
    st.caption("IGD = Inter-incisor gap distance (khoảng cách giữa 2 răng cửa)")
    
    # Receding mandible
    st.markdown("### 4️⃣ Hàm lùi (Receding mandible)")
    receding_mandible = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Không",
            1: "1 điểm - Trung bình",
            2: "2 điểm - Nghiêm trọng"
        }[x],
        key="wilson_mandible",
        horizontal=False
    )
    
    # Buck teeth
    st.markdown("### 5️⃣ Răng hô (Buck teeth/Protruding teeth)")
    buck_teeth = st.radio(
        "Chọn mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - Không",
            1: "1 điểm - Trung bình",
            2: "2 điểm - Nghiêm trọng"
        }[x],
        key="wilson_teeth",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Wilson Risk", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_wilson_score(weight, head_neck_movement, jaw_movement, receding_mandible, buck_teeth)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_wilson_risk(weight, head_neck_movement, jaw_movement, receding_mandible, buck_teeth)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/10")
            
            with col2:
                st.metric("Nguy cơ", result['risk'])
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == COLORS["success"]:
                st.success(f"**{result['risk']}** - {result['difficulty']}")
            elif result['color'] == COLORS["warning"]:
                st.warning(f"**{result['risk']}** - {result['difficulty']}")
            else:
                st.error(f"**{result['risk']}** - {result['difficulty']}")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Additional information
            with st.expander("📚 Dụng cụ đường thở khó"):
                st.markdown("""
            **Chuẩn bị dụng cụ khi nguy cơ cao:**
            
            1. **Video laryngoscope** (Glidescope, C-MAC, etc.)
               - Tầm nhìn tốt hơn laryngoscope thường
               - Dễ sử dụng hơn fiberoptic
            
            2. **Laryngeal Mask Airway (LMA)**
               - Dự phòng nếu không đặt được NKQ
               - Có thể dùng để đặt NKQ qua LMA
            
            3. **Fiberoptic bronchoscope**
               - Đặt NKQ tỉnh hoặc dưới gây mê
               - Cần kỹ năng đặc biệt
            
            4. **Bougie/Gum elastic bougie**
               - Hỗ trợ đặt NKQ khi tầm nhìn hạn chế
            
            5. **Cricothyrotomy kit**
               - Dự phòng cuối cùng nếu không đặt được NKQ
               - Cần có sẵn trong phòng mổ
            
            **Chiến lược:**
            - Điểm ≥3: Cân nhắc đặt NKQ tỉnh với fiberoptic
            - Luôn có kế hoạch B và C
            - Thông báo trước cho đội ngũ phẫu thuật
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Cân nặng": f"{weight}/2",
                "Cử động đầu cổ": f"{head_neck_movement}/2",
                "Cử động hàm": f"{jaw_movement}/2",
                "Hàm lùi": f"{receding_mandible}/2",
                "Răng hô": f"{buck_teeth}/2"
            }
            
            results_dict = {
                "Tổng điểm": f"{result['total_score']}/10",
                "Nguy cơ": result['risk'],
                "Độ khó": result['difficulty'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Export section
            render_export_section(
                title="Wilson Risk Score",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="Wilson Risk Score"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="wilson_risk",
                calculator_name="Wilson Risk Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="wilson_risk",
                calculator_name="Wilson Risk Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="wilson_risk", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("wilson_risk")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

