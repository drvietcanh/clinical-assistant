"""
Glasgow Outcome Scale (GOS) Calculator
=======================================

Assesses functional outcome after brain injury

Reference:
- Jennett B, Bond M. Assessment of outcome after severe brain damage. 
  Lancet. 1975;1(7905):480-484.

GOS Classification (5 levels):
- GOS 1: Death
- GOS 2: Vegetative state
- GOS 3: Severe disability
- GOS 4: Moderate disability
- GOS 5: Good recovery

Clinical Utility:
- Assess long-term outcome after brain injury
- Compare treatment outcomes
- Guide rehabilitation planning
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


def get_gos_info(gos_level: int) -> dict:
    """
    Get GOS level information
    
    Args:
        gos_level: GOS level (1-5)
    
    Returns:
        Dictionary with GOS information
    """
    gos_levels = {
        1: {
            'name': 'Death',
            'description': 'Tử vong',
            'details': 'Bệnh nhân đã tử vong',
            'color': COLORS['error']
        },
        2: {
            'name': 'Vegetative State',
            'description': 'Trạng thái sống thực vật',
            'details': 'Không có phản ứng có ý thức, mở mắt nhưng không nhận thức',
            'color': COLORS['error']
        },
        3: {
            'name': 'Severe Disability',
            'description': 'Tàn tật nặng',
            'details': 'Tỉnh táo nhưng phụ thuộc hoàn toàn vào người khác trong sinh hoạt hàng ngày',
            'color': COLORS['warning']
        },
        4: {
            'name': 'Moderate Disability',
            'description': 'Tàn tật trung bình',
            'details': 'Độc lập trong sinh hoạt nhưng không thể quay lại công việc hoặc hoạt động xã hội',
            'color': COLORS['warning']
        },
        5: {
            'name': 'Good Recovery',
            'description': 'Phục hồi tốt',
            'details': 'Có thể quay lại công việc và hoạt động xã hội, có thể có một số khuyết tật nhẹ',
            'color': COLORS['success']
        }
    }
    
    return gos_levels.get(gos_level, {})


def render():
    """Render Glasgow Outcome Scale calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 Glasgow Outcome Scale (GOS)</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá kết quả chức năng sau chấn thương não**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'gos':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Glasgow Outcome Scale (GOS)** đánh giá kết quả chức năng sau chấn thương não:
        - Đánh giá kết quả dài hạn sau chấn thương não
        - So sánh kết quả điều trị
        - Hướng dẫn kế hoạch phục hồi chức năng
        
        ### 🎯 Phân loại (5 mức độ)
        
        **GOS 1: Death (Tử vong)**
        - Bệnh nhân đã tử vong
        
        **GOS 2: Vegetative State (Trạng thái sống thực vật)**
        - Không có phản ứng có ý thức
        - Mở mắt nhưng không nhận thức
        
        **GOS 3: Severe Disability (Tàn tật nặng)**
        - Tỉnh táo nhưng phụ thuộc hoàn toàn
        - Cần hỗ trợ trong sinh hoạt hàng ngày
        
        **GOS 4: Moderate Disability (Tàn tật trung bình)**
        - Độc lập trong sinh hoạt
        - Không thể quay lại công việc hoặc hoạt động xã hội
        
        **GOS 5: Good Recovery (Phục hồi tốt)**
        - Có thể quay lại công việc và hoạt động xã hội
        - Có thể có một số khuyết tật nhẹ
        
        ### ⚠️ Lưu ý
        
        - Đánh giá thường được thực hiện sau 6 tháng
        - Kết hợp với các thang điểm khác (GCS, mRS)
        - Hướng dẫn kế hoạch phục hồi chức năng
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="gos",
            calculator_name="Glasgow Outcome Scale",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Chọn mức độ GOS")
    
    gos_level = st.selectbox(
        "Glasgow Outcome Scale",
        [
            (5, "GOS 5: Good Recovery (Phục hồi tốt)"),
            (4, "GOS 4: Moderate Disability (Tàn tật trung bình)"),
            (3, "GOS 3: Severe Disability (Tàn tật nặng)"),
            (2, "GOS 2: Vegetative State (Trạng thái sống thực vật)"),
            (1, "GOS 1: Death (Tử vong)")
        ],
        index=0,
        format_func=lambda x: x[1],
        help="Chọn mức độ GOS dựa trên tình trạng bệnh nhân"
    )
    gos_level = gos_level[0]
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Xác nhận GOS", type="primary", use_container_width=True):
        gos_info = get_gos_info(gos_level)
        
        if not gos_info:
            st.error("Mức độ GOS không hợp lệ")
            return
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            1: "💀",
            2: "😴",
            3: "⚠️",
            4: "🔄",
            5: "✅"
        }
        icon = icon_map.get(gos_level, "🧠")
        
        render_score_result(
            title=f"GOS {gos_level}: {gos_info['name']}",
            score=f"GOS {gos_level}",
            interpretation=f"{gos_info['description']} - {gos_info['details']}",
            mortality=None,
            color=gos_info['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if gos_level == 5:
            st.success(f"""
            **GOS {gos_level}: {gos_info['name']}** - Phục hồi tốt ✅
            
            - **Mô tả:** {gos_info['description']}
            - **Chi tiết:** {gos_info['details']}
            - Kết quả tốt nhất có thể đạt được
            - Bệnh nhân có thể quay lại cuộc sống bình thường
            """)
        elif gos_level == 4:
            st.warning(f"""
            **GOS {gos_level}: {gos_info['name']}** - Tàn tật trung bình ⚠️
            
            - **Mô tả:** {gos_info['description']}
            - **Chi tiết:** {gos_info['details']}
            - Cần phục hồi chức năng tiếp tục
            - Có thể cần hỗ trợ trong một số hoạt động
            """)
        elif gos_level == 3:
            st.warning(f"""
            **GOS {gos_level}: {gos_info['name']}** - Tàn tật nặng ⚠️
            
            - **Mô tả:** {gos_info['description']}
            - **Chi tiết:** {gos_info['details']}
            - Cần chăm sóc và hỗ trợ liên tục
            - Phục hồi chức năng tích cực có thể cải thiện
            """)
        elif gos_level == 2:
            st.error(f"""
            **GOS {gos_level}: {gos_info['name']}** - Trạng thái sống thực vật 🚨
            
            - **Mô tả:** {gos_info['description']}
            - **Chi tiết:** {gos_info['details']}
            - Tiên lượng rất kém
            - Cần chăm sóc lâu dài
            """)
        else:
            st.error(f"""
            **GOS {gos_level}: {gos_info['name']}** 💀
            
            - **Mô tả:** {gos_info['description']}
            - **Chi tiết:** {gos_info['details']}
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - GOS đánh giá kết quả chức năng sau chấn thương não
        - Đánh giá thường được thực hiện sau 6 tháng để đánh giá kết quả dài hạn
        - Kết hợp với các thang điểm khác (GCS ban đầu, mRS) để đánh giá toàn diện
        - GOS 4-5: Kết quả tốt, có thể quay lại cuộc sống
        - GOS 3: Cần phục hồi chức năng tích cực và hỗ trợ
        - GOS 1-2: Tiên lượng kém, cần chăm sóc lâu dài
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'gos',
            'calculator_name': 'Glasgow Outcome Scale',
            'inputs': {
                'gos_level': gos_level
            },
            'results': {
                'gos_level': gos_level,
                'name': gos_info['name'],
                'description': gos_info['description'],
                'details': gos_info['details']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('gos')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Jennett B, Bond M. Assessment of outcome after severe brain damage. 
          Lancet. 1975;1(7905):480-484.
        """)
    
    # History
    render_history_ui(calculator_id="gos", show_actions=True)
