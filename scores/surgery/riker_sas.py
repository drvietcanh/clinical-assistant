"""
Riker SAS - Sedation-Agitation Scale Calculator
Thang điểm an thần/kích động
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
from scores.utils.anesthesia_validation import validate_riker_sas_score


def get_riker_sas_interpretation(score):
    """
    Trả về thông tin về Riker SAS
    
    Parameters:
    - score: Score 1-7
    
    Returns:
    - dict với description, level, và recommendation
    """
    interpretations = {
        1: {
            "description": "Không đáp ứng - Không đáp ứng với kích thích đau mạnh",
            "level": "An thần rất sâu",
            "recommendation": "Quá sâu, cần giảm liều an thần ngay",
            "color": COLORS["error"]
        },
        2: {
            "description": "Đáp ứng rất chậm - Đáp ứng với kích thích đau mạnh nhưng không mở mắt hoặc cử động",
            "level": "An thần sâu",
            "recommendation": "Có thể quá sâu, cân nhắc giảm liều",
            "color": COLORS["warning"]
        },
        3: {
            "description": "Đáp ứng chậm - Đáp ứng với kích thích vật lý hoặc lệnh bằng lời",
            "level": "An thần vừa",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": COLORS["success"]
        },
        4: {
            "description": "Yên tĩnh và hợp tác - Dễ đánh thức, hợp tác với máy thở",
            "level": "An thần nhẹ",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": COLORS["success"]
        },
        5: {
            "description": "Kích động nhẹ - Lo lắng hoặc bồn chồn nhưng không kích động",
            "level": "Kích động nhẹ",
            "recommendation": "Có thể cần tăng an thần nhẹ",
            "color": COLORS["warning"]
        },
        6: {
            "description": "Kích động vừa - Kích động, không hợp tác, cần thuốc an thần",
            "level": "Kích động vừa",
            "recommendation": "Cần tăng an thần",
            "color": COLORS["warning"]
        },
        7: {
            "description": "Kích động nguy hiểm - Kích động mạnh, kéo ống NKQ, đánh nhân viên",
            "level": "Kích động nguy hiểm",
            "recommendation": "Cần tăng an thần ngay, có thể cần thuốc an thần mạnh",
            "color": COLORS["error"]
        }
    }
    
    return interpretations.get(score, interpretations[4])


def render():
    """Render Riker SAS interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'riker_sas':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Riker SAS')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>😴 Riker SAS - Sedation-Agitation Scale</h2>
    <p style='text-align: center;'><em>Thang điểm an thần/kích động</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Riker SAS"):
        st.markdown("""
        **Riker SAS (Sedation-Agitation Scale)** là thang điểm đánh giá mức độ an thần và kích động,
        được sử dụng trong ICU.
        
        **7 mức độ:**
        
        **1 - An thần rất sâu:** Không đáp ứng với kích thích đau mạnh
        
        **2 - An thần sâu:** Đáp ứng rất chậm với kích thích đau mạnh
        
        **3 - An thần vừa:** Đáp ứng chậm với kích thích vật lý hoặc lệnh bằng lời
        
        **4 - An thần nhẹ:** Yên tĩnh và hợp tác, dễ đánh thức
        
        **5 - Kích động nhẹ:** Lo lắng hoặc bồn chồn nhưng không kích động
        
        **6 - Kích động vừa:** Kích động, không hợp tác
        
        **7 - Kích động nguy hiểm:** Kích động mạnh, kéo ống NKQ
        
        **Mục tiêu an thần:**
        - **Bệnh nhân thở máy:** Riker SAS 3-4 (an thần vừa-nhẹ)
        - **Bệnh nhân tỉnh:** Riker SAS 4 (yên tĩnh và hợp tác)
        - **Tránh:** Riker SAS 1-2 (quá sâu) hoặc 5-7 (kích động)
        
        **So sánh với RASS:**
        - Riker SAS đơn giản hơn RASS
        - RASS được khuyến nghị nhiều hơn trong ICU hiện đại
        - Riker SAS vẫn được sử dụng ở một số nơi
        
        **Reference:** Riker RR, et al. Prospective evaluation of the Sedation-Agitation Scale 
        for adult critically ill patients. Crit Care Med. 1999;27(7):1325-9.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Chọn mức độ Riker SAS")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="riker_sas",
            calculator_name="Riker SAS",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    score = st.radio(
        "Riker SAS Score:",
        options=[1, 2, 3, 4, 5, 6, 7],
        format_func=lambda x: {
            1: "1 - An thần rất sâu (Không đáp ứng với kích thích đau mạnh)",
            2: "2 - An thần sâu (Đáp ứng rất chậm với kích thích đau mạnh)",
            3: "3 - An thần vừa (Đáp ứng chậm với kích thích vật lý/lệnh)",
            4: "4 - An thần nhẹ (Yên tĩnh và hợp tác, dễ đánh thức)",
            5: "5 - Kích động nhẹ (Lo lắng, bồn chồn nhưng không kích động)",
            6: "6 - Kích động vừa (Kích động, không hợp tác)",
            7: "7 - Kích động nguy hiểm (Kích động mạnh, kéo ống NKQ)"
        }[x],
        key="riker_sas_score",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Xem kết quả Riker SAS", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_riker_sas_score(score)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = get_riker_sas_interpretation(score)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Riker SAS", f"{score}/7")
            
            with col2:
                st.metric("Mức độ", result['level'])
            
            st.markdown("---")
            
            st.subheader("📋 Mô tả")
            st.info(f"**{result['description']}**")
            
            st.markdown("---")
            
            # Recommendation
            if result['color'] == COLORS["success"]:
                st.success(f"**Khuyến nghị:** {result['recommendation']}")
            elif result['color'] == COLORS["warning"]:
                st.warning(f"**Khuyến nghị:** {result['recommendation']}")
            else:
                st.error(f"**Khuyến nghị:** {result['recommendation']}")
            
            st.markdown("---")
            
            # Clinical guidance
            with st.expander("💡 Hướng dẫn lâm sàng"):
                st.markdown("""
            **Mục tiêu an thần theo tình huống:**
            
            **1. Bệnh nhân thở máy:**
            - Mục tiêu: Riker SAS 3-4 (an thần vừa-nhẹ)
            - Đảm bảo bệnh nhân hợp tác với máy thở
            - Tránh kích động (Riker SAS 5-7) hoặc quá sâu (Riker SAS 1-2)
            
            **2. Bệnh nhân tỉnh, không thở máy:**
            - Mục tiêu: Riker SAS 4 (yên tĩnh và hợp tác)
            - Cho phép bệnh nhân giao tiếp và hợp tác
            
            **3. Bệnh nhân kích động (Riker SAS 5-7):**
            - Tăng liều an thần
            - Kiểm tra nguyên nhân kích động (đau, khó chịu, thiếu oxy)
            - Cân nhắc dùng thuốc an thần
            
            **4. Bệnh nhân quá sâu (Riker SAS 1-2):**
            - Giảm liều an thần
            - Đánh giá lại mức độ an thần thường xuyên
            - Cân nhắc ngừng hoặc giảm thuốc an thần
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Riker SAS Score": str(score)
            }
            
            results_dict = {
                "Mức độ": result['level'],
                "Mô tả": result['description'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Export section
            render_export_section(
                title="Riker SAS",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="Riker SAS"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="riker_sas",
                calculator_name="Riker SAS",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="riker_sas",
                calculator_name="Riker SAS",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="riker_sas", show_actions=True)
            
            st.markdown("---")
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # Comparison with other scales
    with st.expander("🔄 So sánh với các thang điểm khác"):
            st.markdown("""
            | Riker SAS | RASS | Ramsay | Mô tả |
            |-----------|------|--------|-------|
            | 7 | +4 | 1 | Kích động nguy hiểm |
            | 6 | +3 | 1 | Kích động mạnh |
            | 5 | +1 đến +2 | 1 | Kích động nhẹ-vừa |
            | 4 | 0 | 2 | Tỉnh táo/Yên tĩnh |
            | 3 | -2 đến -3 | 3-4 | An thần vừa |
            | 2 | -4 | 5 | An thần sâu |
            | 1 | -5 | 6 | An thần rất sâu |
            
            **Khuyến nghị:**
            - RASS được khuyến nghị nhiều nhất trong ICU hiện đại
            - Riker SAS đơn giản nhưng ít chi tiết hơn RASS
            - Ramsay vẫn được sử dụng rộng rãi
            """)
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("riker_sas")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

