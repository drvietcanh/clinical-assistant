"""
HINTS Exam Calculator
======================

Differentiates central vs peripheral causes of vertigo

Reference:
- Kattah JC, et al. HINTS to diagnose stroke in the acute vestibular syndrome: 
  three-step bedside oculomotor examination more sensitive than early MRI diffusion-weighted imaging. 
  Stroke. 2009;40(11):3504-3510.

HINTS Components (3 tests):
- Head Impulse Test (HIT)
- Nystagmus
- Test of Skew (cover test)

Interpretation:
- All 3 tests normal = Peripheral (vestibular) cause likely
- Any abnormal = Central (stroke) cause possible, need imaging

Clinical Utility:
- Rapid bedside assessment
- Identify stroke in acute vestibular syndrome
- Guide imaging decisions
- Avoid missing posterior circulation stroke
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


def calculate_hints_exam(
    hit_normal: bool,
    nystagmus_type: str,
    skew_normal: bool
) -> dict:
    """
    Calculate HINTS Exam interpretation
    
    Args:
        hit_normal: Head Impulse Test normal (True) or abnormal (False)
        nystagmus_type: Type of nystagmus ("unidirectional", "bidirectional", "none")
        skew_normal: Test of Skew normal (True) or abnormal (False)
    
    Returns:
        Dictionary with interpretation and recommendations
    """
    abnormal_findings = []
    details = []
    
    # Head Impulse Test
    if hit_normal:
        details.append("✅ Head Impulse Test: Bình thường (corrective saccade)")
    else:
        abnormal_findings.append("Head Impulse Test bất thường")
        details.append("❌ Head Impulse Test: Bất thường (không có corrective saccade)")
    
    # Nystagmus
    if nystagmus_type == "unidirectional":
        details.append("✅ Nystagmus: Một chiều (unidirectional) - Gợi ý ngoại biên")
    elif nystagmus_type == "bidirectional":
        abnormal_findings.append("Nystagmus hai chiều")
        details.append("❌ Nystagmus: Hai chiều (bidirectional) - Gợi ý trung ương")
    else:  # none
        details.append("✅ Nystagmus: Không có")
    
    # Test of Skew
    if skew_normal:
        details.append("✅ Test of Skew: Bình thường (không có skew)")
    else:
        abnormal_findings.append("Test of Skew bất thường")
        details.append("❌ Test of Skew: Bất thường (có skew) - Gợi ý trung ương")
    
    # Interpretation
    if len(abnormal_findings) == 0:
        interpretation = "Nguyên nhân ngoại biên (vestibular) có thể"
        risk_class = "PERIPHERAL"
        recommendation = "Có thể là nguyên nhân ngoại biên (viêm tiền đình, BPPV). Cân nhắc điều trị triệu chứng."
        color = COLORS["success"]
        need_imaging = "Không cần thiết ngay, trừ khi triệu chứng không cải thiện"
    else:
        interpretation = "Nguyên nhân trung ương (stroke) có thể - Cần chụp hình"
        risk_class = "CENTRAL"
        recommendation = "Có thể là nguyên nhân trung ương (stroke). Cần chụp hình ngay (CT/MRI) để loại trừ stroke."
        color = COLORS["error"]
        need_imaging = "Cần thiết ngay - CT/MRI để loại trừ stroke"
    
    return {
        'abnormal_findings': abnormal_findings,
        'interpretation': interpretation,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'need_imaging': need_imaging,
        'color': color,
        'details': details
    }


def render():
    """Render HINTS Exam calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 HINTS Exam</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Phân biệt nguyên nhân trung ương vs ngoại biên của chóng mặt**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'hints':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **HINTS Exam** phân biệt nguyên nhân trung ương vs ngoại biên của chóng mặt:
        - Đánh giá nhanh tại giường bệnh
        - Xác định stroke trong hội chứng tiền đình cấp
        - Hướng dẫn quyết định chụp hình
        
        ### 🎯 3 bước đánh giá
        
        **1. Head Impulse Test (HIT)**
        - Bình thường: Có corrective saccade → Gợi ý ngoại biên
        - Bất thường: Không có corrective saccade → Gợi ý trung ương
        
        **2. Nystagmus**
        - Một chiều (unidirectional): Gợi ý ngoại biên
        - Hai chiều (bidirectional): Gợi ý trung ương
        
        **3. Test of Skew (cover test)**
        - Bình thường: Không có skew → Gợi ý ngoại biên
        - Bất thường: Có skew → Gợi ý trung ương
        
        ### 📊 Phân loại
        
        | Kết quả | Nguyên nhân | Khuyến nghị |
        |---------|-------------|-------------|
        | Tất cả bình thường | Ngoại biên | Điều trị triệu chứng |
        | Có bất thường | Trung ương (stroke) | Chụp hình ngay |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân hội chứng tiền đình cấp
        - HINTS bất thường = Cần chụp hình ngay để loại trừ stroke
        - Không thay thế đánh giá lâm sàng toàn diện
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="hints",
            calculator_name="HINTS Exam",
            category="Thần Kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập kết quả HINTS Exam")
    
    st.markdown("### 1. Head Impulse Test (HIT)")
    hit_normal = st.radio(
        "Head Impulse Test",
        ["Bình thường (có corrective saccade)", "Bất thường (không có corrective saccade)"],
        index=0,
        help="Xoay đầu nhanh sang một bên và quan sát mắt"
    )
    hit_normal = (hit_normal == "Bình thường (có corrective saccade)")
    
    st.markdown("### 2. Nystagmus")
    nystagmus_type = st.selectbox(
        "Loại nystagmus",
        [
            ("none", "Không có nystagmus"),
            ("unidirectional", "Một chiều (unidirectional)"),
            ("bidirectional", "Hai chiều (bidirectional)")
        ],
        index=0,
        format_func=lambda x: x[1],
        help="Quan sát nystagmus khi nhìn thẳng và nhìn sang hai bên"
    )
    nystagmus_type = nystagmus_type[0]
    
    st.markdown("### 3. Test of Skew (Cover Test)")
    skew_normal = st.radio(
        "Test of Skew",
        ["Bình thường (không có skew)", "Bất thường (có skew)"],
        index=0,
        help="Che một mắt và quan sát mắt kia khi mở ra"
    )
    skew_normal = (skew_normal == "Bình thường (không có skew)")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Đánh giá HINTS Exam", type="primary", use_container_width=True):
        result = calculate_hints_exam(
            hit_normal=hit_normal,
            nystagmus_type=nystagmus_type,
            skew_normal=skew_normal
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "PERIPHERAL": "✅",
            "CENTRAL": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🧠")
        
        render_score_result(
            title="HINTS Exam",
            score=f"{len(result['abnormal_findings'])}/3",
            interpretation=f"{result['interpretation']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Details
        with st.expander("📋 Chi tiết đánh giá", expanded=False):
            st.markdown("### Kết quả các test:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            if result['abnormal_findings']:
                st.markdown("### ⚠️ Phát hiện bất thường:")
                for finding in result['abnormal_findings']:
                    st.markdown(f"- **{finding}**")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "PERIPHERAL":
            st.success(f"""
            **Nguyên nhân ngoại biên có thể** ✅
            
            - **Khuyến nghị:** {result['recommendation']}
            - **Chụp hình:** {result['need_imaging']}
            - Có thể là viêm tiền đình, BPPV, hoặc nguyên nhân ngoại biên khác
            - Điều trị triệu chứng và theo dõi
            """)
        else:
            st.error(f"""
            **Nguyên nhân trung ương (stroke) có thể** 🚨
            
            - **Khuyến nghị:** {result['recommendation']}
            - **Chụp hình:** {result['need_imaging']}
            - Có thể là stroke hệ thống tiền đình trung ương
            - **Cần chụp hình ngay (CT/MRI)** để loại trừ stroke
            - Không được bỏ sót stroke hệ tuần hoàn sau
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - HINTS Exam giúp phân biệt nguyên nhân trung ương vs ngoại biên của chóng mặt
        - **Tất cả bình thường:** Có thể là nguyên nhân ngoại biên, điều trị triệu chứng
        - **Có bất thường:** Có thể là stroke, cần chụp hình ngay
        - HINTS bất thường có độ nhạy cao để phát hiện stroke trong hội chứng tiền đình cấp
        - Kết hợp với đánh giá lâm sàng và các dấu hiệu thần kinh khác
        - Không thay thế đánh giá lâm sàng toàn diện
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'hints',
            'calculator_name': 'HINTS Exam',
            'inputs': {
                'hit_normal': hit_normal,
                'nystagmus_type': nystagmus_type,
                'skew_normal': skew_normal
            },
            'results': {
                'abnormal_findings_count': len(result['abnormal_findings']),
                'interpretation': result['interpretation'],
                'risk_class': result['risk_class'],
                'recommendation': result['recommendation']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('hints')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Kattah JC, et al. HINTS to diagnose stroke in the acute vestibular syndrome: 
          three-step bedside oculomotor examination more sensitive than early MRI diffusion-weighted imaging. 
          Stroke. 2009;40(11):3504-3510.
        """)
    
    # History
    render_history_ui(calculator_id="hints", show_actions=True)
