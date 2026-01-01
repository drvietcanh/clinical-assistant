"""
ICE (Immune Effector Cell Encephalopathy) Score
===============================================

Assessment tool for immune effector cell-associated neurotoxicity syndrome (ICANS)
in patients receiving CAR T-cell therapy or other immune effector cell therapies.

Reference:
- Lee DW, et al. ASTCT Consensus Grading for Cytokine Release Syndrome and 
  Neurologic Toxicity Associated with Immune Effector Cells. Biol Blood Marrow 
  Transplant. 2019;25(4):625-638.
- Neelapu SS, et al. Chimeric antigen receptor T-cell therapy - assessment and 
  management of toxicities. Nat Rev Clin Oncol. 2018;15(1):47-62.

ICE Score Components:
- Orientation (to year, month, city, hospital)
- Naming (ability to name 3 objects)
- Following commands (ability to follow simple commands)
- Writing (ability to write a standard sentence)
- Attention (ability to count backwards from 100 by 10)

Score Range: 0-10
- 10: No impairment
- 7-9: Mild impairment
- 3-6: Moderate impairment
- 0-2: Severe impairment

Clinical Utility:
- Early detection of ICANS
- Guides treatment decisions
- Monitors response to therapy
- Used in cellular therapy programs
"""

import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_ice_score(
    orientation: int,  # 0-4 (year, month, city, hospital)
    naming: int,  # 0-3 (3 objects)
    following_commands: int,  # 0-2 (simple commands)
    writing: int,  # 0-2 (standard sentence)
    attention: int  # 0-2 (count backwards from 100 by 10)
) -> dict:
    """
    Calculate ICE Score
    
    Args:
        orientation: Orientation score (0-4)
        naming: Naming score (0-3)
        following_commands: Following commands score (0-2)
        writing: Writing score (0-2)
        attention: Attention score (0-2)
    
    Returns:
        Dictionary with ICE score, grade, and interpretation
    """
    total_score = orientation + naming + following_commands + writing + attention
    
    # Determine grade based on score
    if total_score >= 7:
        grade = "Nhẹ (Mild)"
        grade_color = COLORS["success"]
        grade_icon = "🟢"
        severity = "Mức độ nhẹ"
    elif total_score >= 3:
        grade = "Trung bình (Moderate)"
        grade_color = COLORS["warning"]
        grade_icon = "🟡"
        severity = "Mức độ trung bình"
    else:
        grade = "Nặng (Severe)"
        grade_color = COLORS["error"]
        grade_icon = "🔴"
        severity = "Mức độ nặng"
    
    # Component breakdown
    components = {
        "Orientation": {"score": orientation, "max": 4, "description": "Định hướng (năm, tháng, thành phố, bệnh viện)"},
        "Naming": {"score": naming, "max": 3, "description": "Đặt tên (3 đồ vật)"},
        "Following Commands": {"score": following_commands, "max": 2, "description": "Thực hiện lệnh (lệnh đơn giản)"},
        "Writing": {"score": writing, "max": 2, "description": "Viết (câu chuẩn)"},
        "Attention": {"score": attention, "max": 2, "description": "Chú ý (đếm ngược từ 100, bước 10)"}
    }
    
    return {
        "total_score": total_score,
        "max_score": 10,
        "grade": grade,
        "grade_color": grade_color,
        "grade_icon": grade_icon,
        "severity": severity,
        "components": components
    }


def render():
    """Render ICE Score interface"""
    # st.set_page_config(page_title="ICE Score", layout="wide")
    
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 ICE Score (Immune Effector Cell Encephalopathy)</h3>
    <p style='text-align: center; color: #6B7280;'>
    Đánh giá độc tính thần kinh ở bệnh nhân điều trị CAR T-cell
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về ICE Score"):
        st.markdown("""
        **ICE (Immune Effector Cell Encephalopathy) Score** đánh giá độc tính thần kinh 
        ở bệnh nhân điều trị CAR T-cell hoặc các liệu pháp tế bào hiệu ứng miễn dịch khác.
        
        ### Các thành phần đánh giá:
        1. **Orientation (Định hướng) - 0-4 điểm:**
           - Năm hiện tại (1 điểm)
           - Tháng hiện tại (1 điểm)
           - Thành phố hiện tại (1 điểm)
           - Bệnh viện hiện tại (1 điểm)
        
        2. **Naming (Đặt tên) - 0-3 điểm:**
           - Đặt tên 3 đồ vật (mỗi đồ vật 1 điểm)
        
        3. **Following Commands (Thực hiện lệnh) - 0-2 điểm:**
           - Thực hiện lệnh đơn giản (mỗi lệnh 1 điểm)
        
        4. **Writing (Viết) - 0-2 điểm:**
           - Viết một câu chuẩn (2 điểm)
        
        5. **Attention (Chú ý) - 0-2 điểm:**
           - Đếm ngược từ 100, bước 10 (2 điểm)
        
        ### Phân loại:
        - **10 điểm:** Không suy giảm
        - **7-9 điểm:** Suy giảm nhẹ
        - **3-6 điểm:** Suy giảm trung bình
        - **0-2 điểm:** Suy giảm nặng
        
        ### Ứng dụng lâm sàng:
        - Phát hiện sớm ICANS
        - Hướng dẫn quyết định điều trị
        - Theo dõi đáp ứng điều trị
        - Dùng trong chương trình liệu pháp tế bào
        """)
    
    st.markdown("### 📊 Đánh giá từng thành phần")
    
    st.markdown("#### 1. Orientation (Định hướng) - Tối đa 4 điểm")
    orientation = st.slider(
        "Điểm định hướng",
        min_value=0,
        max_value=4,
        value=4,
        step=1,
        help="0 = Không định hướng được; 4 = Định hướng đầy đủ (năm, tháng, thành phố, bệnh viện)",
        key="ice_orientation"
    )
    
    st.markdown("#### 2. Naming (Đặt tên) - Tối đa 3 điểm")
    naming = st.slider(
        "Điểm đặt tên",
        min_value=0,
        max_value=3,
        value=3,
        step=1,
        help="0 = Không đặt tên được; 3 = Đặt tên đầy đủ 3 đồ vật",
        key="ice_naming"
    )
    
    st.markdown("#### 3. Following Commands (Thực hiện lệnh) - Tối đa 2 điểm")
    following_commands = st.slider(
        "Điểm thực hiện lệnh",
        min_value=0,
        max_value=2,
        value=2,
        step=1,
        help="0 = Không thực hiện được; 2 = Thực hiện đầy đủ lệnh đơn giản",
        key="ice_commands"
    )
    
    st.markdown("#### 4. Writing (Viết) - Tối đa 2 điểm")
    writing = st.slider(
        "Điểm viết",
        min_value=0,
        max_value=2,
        value=2,
        step=1,
        help="0 = Không viết được; 2 = Viết được câu chuẩn",
        key="ice_writing"
    )
    
    st.markdown("#### 5. Attention (Chú ý) - Tối đa 2 điểm")
    attention = st.slider(
        "Điểm chú ý",
        min_value=0,
        max_value=2,
        value=2,
        step=1,
        help="0 = Không đếm được; 2 = Đếm ngược từ 100, bước 10 đúng",
        key="ice_attention"
    )
    
    if st.button("🔬 Tính toán ICE Score", type="primary", use_container_width=True):
        result = calculate_ice_score(
            orientation=orientation,
            naming=naming,
            following_commands=following_commands,
            writing=writing,
            attention=attention
        )
        
        st.markdown("---")
        st.subheader("📋 Kết quả")
        
        render_score_result(
            title="ICE Score",
            score=result['total_score'],
            interpretation=f"{result['grade']}\n({result['severity']})",
            color=result['grade_color'],
            icon=result['grade_icon']
        )
        
        st.markdown("### 📊 Chi tiết từng thành phần")
        for component_name, component_data in result["components"].items():
            col1, col2, col3 = st.columns([2, 1, 3])
            with col1:
                st.markdown(f"**{component_name}:**")
            with col2:
                st.markdown(f"{component_data['score']}/{component_data['max']}")
            with col3:
                st.markdown(f"*{component_data['description']}*")
        
        # Clinical recommendations
        st.markdown("### 💡 Khuyến nghị lâm sàng")
        
        if result["total_score"] >= 7:
            st.markdown("""
            **ICE Score ≥7 (Nhẹ):**
            
            1. **Theo dõi:**
               - Đánh giá ICE Score mỗi 8-12 giờ
               - Theo dõi triệu chứng thần kinh
               - Đánh giá mức độ ý thức
            
            2. **Điều trị:**
               - Điều trị hỗ trợ nếu cần
               - Có thể tiếp tục điều trị CAR T-cell
            """)
        elif result["total_score"] >= 3:
            st.markdown("""
            **ICE Score 3-6 (Trung bình):**
            
            1. **Theo dõi chuyên sâu:**
               - Đánh giá ICE Score mỗi 4-8 giờ
               - Theo dõi sát dấu hiệu thần kinh
               - Đánh giá mức độ ý thức thường xuyên
            
            2. **Điều trị:**
               - Xem xét corticosteroid (dexamethasone)
               - Có thể cần giảm liều hoặc tạm dừng điều trị
               - Hỗ trợ hô hấp nếu cần
            """)
        else:
            st.markdown("""
            **ICE Score 0-2 (Nặng):**
            
            1. **Theo dõi rất chuyên sâu:**
               - Đánh giá ICE Score mỗi 2-4 giờ
               - Theo dõi liên tục dấu hiệu thần kinh
               - Đánh giá mức độ ý thức liên tục
            
            2. **Điều trị tích cực:**
               - Corticosteroid liều cao (dexamethasone)
               - Tạm dừng điều trị CAR T-cell
               - Hỗ trợ hô hấp (có thể cần đặt nội khí quản)
               - Tư vấn thần kinh
               - Xem xét điều trị chống co giật
               - Chăm sóc ICU nếu cần
            """)
        
        save_calculation_to_history(
            calculator_id="ice_score",
            calculator_name="ICE Score",
            inputs={
                "Orientation": f"{orientation}/4",
                "Naming": f"{naming}/3",
                "Following Commands": f"{following_commands}/2",
                "Writing": f"{writing}/2",
                "Attention": f"{attention}/2"
            },
            result={
                "ICE Score": f"{result['total_score']}/10",
                "Grade": result["grade"]
            }
        )
        
        render_share_section(
            calculator_id="ice_score",
            calculator_name="ICE Score"
        )
        
        render_export_section(
            calculator_id="ice_score",
            calculator_name="ICE Score",
            data={
                "inputs": {
                    "orientation": orientation,
                    "naming": naming,
                    "following_commands": following_commands,
                    "writing": writing,
                    "attention": attention
                },
                "result": result
            }
        )
    
    render_history_ui(calculator_id="ice_score", show_actions=True)
    
    references = get_references("ICE Score")
    if references:
        render_references_section(references)

