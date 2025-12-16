"""
Ramsay Sedation Scale Calculator
Đánh giá mức độ an thần
"""

import streamlit as st
from scores.utils.anesthesia_validation import validate_ramsay_score
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def get_ramsay_interpretation(score):
    """
    Trả về thông tin về Ramsay Sedation Scale
    
    Parameters:
    - score: Score 1-6
    
    Returns:
    - dict với description, level, và recommendation
    """
    interpretations = {
        1: {
            "description": "Bệnh nhân lo lắng, kích động, hoặc bồn chồn",
            "level": "Không an thần / Kích động",
            "recommendation": "Cần tăng liều an thần",
            "color": "red"
        },
        2: {
            "description": "Bệnh nhân hợp tác, định hướng, và yên tĩnh",
            "level": "Tỉnh táo",
            "recommendation": "Mức độ phù hợp cho bệnh nhân tỉnh",
            "color": "green"
        },
        3: {
            "description": "Bệnh nhân chỉ đáp ứng với lệnh",
            "level": "An thần nhẹ",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": "green"
        },
        4: {
            "description": "Bệnh nhân đáp ứng nhanh với kích thích nhẹ hoặc gõ nhẹ",
            "level": "An thần vừa",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": "green"
        },
        5: {
            "description": "Bệnh nhân đáp ứng chậm với kích thích mạnh",
            "level": "An thần sâu",
            "recommendation": "Có thể quá sâu, cân nhắc giảm liều",
            "color": "orange"
        },
        6: {
            "description": "Bệnh nhân không đáp ứng",
            "level": "An thần rất sâu",
            "recommendation": "Quá sâu, cần giảm liều an thần ngay",
            "color": "red"
        }
    }
    
    return interpretations.get(score, interpretations[2])


def render():
    """Render Ramsay Sedation Scale interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'ramsay':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>😴 Ramsay Sedation Scale</h2>
    <p style='text-align: center;'><em>Đánh giá mức độ an thần</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Ramsay Sedation Scale"):
        st.markdown("""
        **Ramsay Sedation Scale** là thang điểm đánh giá mức độ an thần,
        được sử dụng rộng rãi trong ICU và phòng hồi tỉnh.
        
        **6 mức độ:**
        
        **1 - Kích động:** Bệnh nhân lo lắng, kích động, hoặc bồn chồn
        
        **2 - Tỉnh táo:** Bệnh nhân hợp tác, định hướng, và yên tĩnh
        
        **3 - An thần nhẹ:** Bệnh nhân chỉ đáp ứng với lệnh
        
        **4 - An thần vừa:** Bệnh nhân đáp ứng nhanh với kích thích nhẹ hoặc gõ nhẹ
        
        **5 - An thần sâu:** Bệnh nhân đáp ứng chậm với kích thích mạnh
        
        **6 - An thần rất sâu:** Bệnh nhân không đáp ứng
        
        **Mục tiêu an thần:**
        - **Bệnh nhân thở máy:** Ramsay 3-4 (an thần vừa)
        - **Bệnh nhân tỉnh:** Ramsay 2 (tỉnh táo)
        - **Tránh:** Ramsay 1 (kích động) hoặc Ramsay 5-6 (quá sâu)
        
        **So sánh với RASS:**
        - Ramsay đơn giản hơn nhưng ít chi tiết hơn RASS
        - RASS có thang điểm âm (kích động) và dương (an thần)
        - Ramsay chỉ có thang điểm dương (1-6)
        
        **Reference:** Ramsay MA, et al. Controlled sedation with alphaxalone-alphadolone. 
        Br Med J. 1974;2(5920):656-9.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Chọn mức độ an thần")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="ramsay",
            calculator_name="Ramsay Sedation Scale",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    score = st.radio(
        "Ramsay Sedation Scale:",
        options=[1, 2, 3, 4, 5, 6],
        format_func=lambda x: {
            1: "1 - Kích động (Lo lắng, kích động, bồn chồn)",
            2: "2 - Tỉnh táo (Hợp tác, định hướng, yên tĩnh)",
            3: "3 - An thần nhẹ (Chỉ đáp ứng với lệnh)",
            4: "4 - An thần vừa (Đáp ứng nhanh với kích thích nhẹ)",
            5: "5 - An thần sâu (Đáp ứng chậm với kích thích mạnh)",
            6: "6 - An thần rất sâu (Không đáp ứng)"
        }[x],
        key="ramsay_score",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Xem kết quả Ramsay", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_ramsay_score(score)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = get_ramsay_interpretation(score)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Điểm Ramsay", f"{score}/6")
            
            with col2:
                st.metric("Mức độ", result['level'])
            
            st.markdown("---")
            
            st.subheader("📋 Mô tả")
            st.info(f"**{result['description']}**")
            
            st.markdown("---")
            
            # Recommendation
            if result['color'] == "green":
                st.success(f"**Khuyến nghị:** {result['recommendation']}")
            elif result['color'] == "orange":
                st.warning(f"**Khuyến nghị:** {result['recommendation']}")
            else:
                st.error(f"**Khuyến nghị:** {result['recommendation']}")
            
            st.markdown("---")
            
            # Clinical guidance
            with st.expander("💡 Hướng dẫn lâm sàng"):
                st.markdown("""
            **Mục tiêu an thần theo tình huống:**
            
            **1. Bệnh nhân thở máy:**
            - Mục tiêu: Ramsay 3-4 (an thần vừa)
            - Đảm bảo bệnh nhân hợp tác với máy thở
            - Tránh kích động (Ramsay 1) hoặc quá sâu (Ramsay 5-6)
            
            **2. Bệnh nhân tỉnh, không thở máy:**
            - Mục tiêu: Ramsay 2 (tỉnh táo)
            - Cho phép bệnh nhân giao tiếp và hợp tác
            
            **3. Bệnh nhân kích động (Ramsay 1):**
            - Tăng liều an thần
            - Kiểm tra nguyên nhân kích động (đau, khó chịu, thiếu oxy)
            - Cân nhắc dùng thuốc an thần (midazolam, propofol, dexmedetomidine)
            
            **4. Bệnh nhân quá sâu (Ramsay 5-6):**
            - Giảm liều an thần
            - Đánh giá lại mức độ an thần thường xuyên
            - Cân nhắc ngừng hoặc giảm thuốc an thần
            
            **Đánh giá thường xuyên:**
            - Mỗi 1-2 giờ trong ICU
            - Sau mỗi lần điều chỉnh liều an thần
            - Khi có thay đổi tình trạng bệnh nhân
            """)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
        
        # Comparison with RASS
        with st.expander("🔄 So sánh với RASS"):
            st.markdown("""
            | Ramsay | RASS | Mô tả |
            |--------|------|-------|
            | 1 | +1 đến +4 | Kích động |
            | 2 | 0 | Tỉnh táo |
            | 3 | -1 đến -2 | An thần nhẹ |
            | 4 | -2 đến -3 | An thần vừa |
            | 5 | -4 | An thần sâu |
            | 6 | -5 | An thần rất sâu |
            
            **Ưu điểm RASS:**
            - Chi tiết hơn về mức độ kích động
            - Có thể đánh giá đáp ứng với kích thích
            - Được khuyến nghị nhiều hơn trong ICU hiện đại
            
            **Ưu điểm Ramsay:**
            - Đơn giản, dễ nhớ
            - Vẫn được sử dụng rộng rãi
            - Phù hợp khi không cần đánh giá chi tiết kích động
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Ramsay Score": score
            }
            
            results_dict = {
                "Ramsay Score": f"{score}/6",
                "Mức độ": result['level'],
                "Mô tả": result['description'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Save to history
            save_calculation_to_history(
                calculator_id="ramsay",
                calculator_name="Ramsay Sedation Scale",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="ramsay",
                calculator_name="Ramsay Sedation Scale",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="ramsay", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("Ramsay")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
