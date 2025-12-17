"""
RASS - Richmond Agitation-Sedation Scale Calculator
Đánh giá an thần/kích động (DÙNG HÀNG NGÀY)
"""

import streamlit as st
from scores.utils.anesthesia_validation import validate_rass_score
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def get_rass_interpretation(score):
    """
    Trả về thông tin về RASS
    
    Parameters:
    - score: Score -5 to +4
    
    Returns:
    - dict với description, level, và recommendation
    """
    interpretations = {
        +4: {
            "description": "Kích động nguy hiểm - Đánh, đá, cắn ống NKQ",
            "level": "Kích động nguy hiểm",
            "recommendation": "Cần tăng an thần ngay, có thể cần thuốc an thần mạnh",
            "color": "red"
        },
        +3: {
            "description": "Kích động mạnh - Kéo hoặc loại bỏ ống NKQ, catheter",
            "level": "Kích động mạnh",
            "recommendation": "Cần tăng an thần, đảm bảo an toàn bệnh nhân",
            "color": "red"
        },
        +2: {
            "description": "Kích động vừa - Cử động không mục đích, không hợp tác",
            "level": "Kích động vừa",
            "recommendation": "Cần tăng an thần nhẹ",
            "color": "orange"
        },
        +1: {
            "description": "Kích động nhẹ - Lo lắng, bồn chồn nhưng không kích động",
            "level": "Kích động nhẹ",
            "recommendation": "Có thể cần tăng an thần nhẹ",
            "color": "yellow"
        },
        0: {
            "description": "Tỉnh táo và yên tĩnh",
            "level": "Tỉnh táo",
            "recommendation": "Mức độ phù hợp cho bệnh nhân tỉnh",
            "color": "green"
        },
        -1: {
            "description": "Buồn ngủ - Không hoàn toàn tỉnh táo, nhưng đáp ứng với gọi tên (mở mắt >10 giây)",
            "level": "Buồn ngủ",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": "green"
        },
        -2: {
            "description": "An thần nhẹ - Đáp ứng với kích thích nhẹ (gọi tên, chạm nhẹ)",
            "level": "An thần nhẹ",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": "green"
        },
        -3: {
            "description": "An thần vừa - Đáp ứng với kích thích vật lý (lắc vai, kích thích đau nhẹ)",
            "level": "An thần vừa",
            "recommendation": "Mức độ phù hợp cho bệnh nhân thở máy",
            "color": "green"
        },
        -4: {
            "description": "An thần sâu - Đáp ứng với kích thích đau mạnh (ấn xương ức, kéo lông mày)",
            "level": "An thần sâu",
            "recommendation": "Có thể quá sâu, cân nhắc giảm liều",
            "color": "orange"
        },
        -5: {
            "description": "Không đáp ứng - Không đáp ứng với kích thích đau mạnh",
            "level": "An thần rất sâu",
            "recommendation": "Quá sâu, cần giảm liều an thần ngay",
            "color": "red"
        }
    }
    
    return interpretations.get(score, interpretations[0])


def render():
    """Render RASS interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'rass':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>😴 RASS - Richmond Agitation-Sedation Scale</h2>
    <p style='text-align: center;'><em>Đánh giá an thần/kích động (DÙNG HÀNG NGÀY)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về RASS"):
        st.markdown("""
        **RASS (Richmond Agitation-Sedation Scale)** là thang điểm tiêu chuẩn vàng để đánh giá 
        mức độ an thần và kích động trong ICU, được khuyến nghị sử dụng hàng ngày.
        
        **Thang điểm: -5 đến +4**
        
        **Kích động (+1 đến +4):**
        - **+1:** Kích động nhẹ - Lo lắng, bồn chồn
        - **+2:** Kích động vừa - Cử động không mục đích
        - **+3:** Kích động mạnh - Kéo ống NKQ, catheter
        - **+4:** Kích động nguy hiểm - Đánh, đá, cắn
        
        **Tỉnh táo (0):**
        - Tỉnh táo và yên tĩnh
        
        **An thần (-1 đến -5):**
        - **-1:** Buồn ngủ - Đáp ứng với gọi tên
        - **-2:** An thần nhẹ - Đáp ứng với kích thích nhẹ
        - **-3:** An thần vừa - Đáp ứng với kích thích vật lý
        - **-4:** An thần sâu - Đáp ứng với kích thích đau mạnh
        - **-5:** Không đáp ứng - Không đáp ứng với kích thích đau mạnh
        
        **Mục tiêu an thần:**
        - **Bệnh nhân thở máy:** RASS -2 đến -3 (an thần nhẹ-vừa)
        - **Bệnh nhân tỉnh:** RASS 0 (tỉnh táo)
        - **Tránh:** RASS >0 (kích động) hoặc RASS <-3 (quá sâu)
        
        **Ưu điểm:**
        - Đánh giá cả kích động và an thần
        - Có hướng dẫn kích thích rõ ràng
        - Độ tin cậy cao, dễ sử dụng
        - Được khuyến nghị bởi SCCM (Society of Critical Care Medicine)
        
        **Reference:** Sessler CN, et al. The Richmond Agitation-Sedation Scale: validity and 
        reliability in adult intensive care unit patients. Am J Respir Crit Care Med. 2002;166(10):1338-44.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Chọn mức độ RASS")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="rass",
            calculator_name="RASS - Richmond Agitation-Sedation Scale",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.markdown("**Hướng dẫn đánh giá:**")
    st.info("""
    1. Quan sát bệnh nhân (không kích thích)
    2. Nếu kích động → Đánh giá +1 đến +4
    3. Nếu yên tĩnh → Gọi tên
    4. Nếu đáp ứng → Đánh giá 0 hoặc -1
    5. Nếu không đáp ứng → Kích thích nhẹ (chạm nhẹ)
    6. Nếu đáp ứng → Đánh giá -2
    7. Nếu không đáp ứng → Kích thích vật lý (lắc vai)
    8. Nếu đáp ứng → Đánh giá -3
    9. Nếu không đáp ứng → Kích thích đau mạnh (ấn xương ức)
    10. Nếu đáp ứng → Đánh giá -4
    11. Nếu không đáp ứng → Đánh giá -5
    """)
    
    score = st.selectbox(
        "RASS Score:",
        options=[+4, +3, +2, +1, 0, -1, -2, -3, -4, -5],
        format_func=lambda x: {
            +4: "+4 - Kích động nguy hiểm (Đánh, đá, cắn ống NKQ)",
            +3: "+3 - Kích động mạnh (Kéo ống NKQ, catheter)",
            +2: "+2 - Kích động vừa (Cử động không mục đích)",
            +1: "+1 - Kích động nhẹ (Lo lắng, bồn chồn)",
            0: "0 - Tỉnh táo và yên tĩnh",
            -1: "-1 - Buồn ngủ (Đáp ứng với gọi tên)",
            -2: "-2 - An thần nhẹ (Đáp ứng với kích thích nhẹ)",
            -3: "-3 - An thần vừa (Đáp ứng với kích thích vật lý)",
            -4: "-4 - An thần sâu (Đáp ứng với kích thích đau mạnh)",
            -5: "-5 - Không đáp ứng (Không đáp ứng với kích thích đau mạnh)"
        }[x],
        key="rass_score"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Xem kết quả RASS", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_rass_score(score)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = get_rass_interpretation(score)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("RASS Score", f"{score:+d}")
            
            with col2:
                st.metric("Mức độ", result['level'])
            
            st.markdown("---")
            
            st.subheader("📋 Mô tả")
            st.info(f"**{result['description']}**")
            
            st.markdown("---")
            
            # Recommendation
            if result['color'] == "green":
                st.success(f"**Khuyến nghị:** {result['recommendation']}")
            elif result['color'] == "orange" or result['color'] == "yellow":
                st.warning(f"**Khuyến nghị:** {result['recommendation']}")
            else:
                st.error(f"**Khuyến nghị:** {result['recommendation']}")
            
            st.markdown("---")
            
            # Clinical guidance
            with st.expander("💡 Hướng dẫn lâm sàng"):
                st.markdown("""
            **Mục tiêu an thần theo tình huống:**
            
            **1. Bệnh nhân thở máy:**
            - Mục tiêu: RASS -2 đến -3 (an thần nhẹ-vừa)
            - Đảm bảo bệnh nhân hợp tác với máy thở
            - Tránh kích động (RASS >0) hoặc quá sâu (RASS <-3)
            - Đánh giá mỗi 1-2 giờ
            
            **2. Bệnh nhân tỉnh, không thở máy:**
            - Mục tiêu: RASS 0 (tỉnh táo)
            - Cho phép bệnh nhân giao tiếp và hợp tác
            
            **3. Bệnh nhân kích động (RASS +1 đến +4):**
            - Tăng liều an thần
            - Kiểm tra nguyên nhân kích động:
              * Đau (đánh giá bằng NRS/VAS)
              * Khó chịu (ống NKQ, catheter)
              * Thiếu oxy, tăng CO₂
              * Mê sảng
            - Cân nhắc dùng thuốc an thần:
              * Midazolam 0.02-0.1 mg/kg/h
              * Propofol 0.3-4 mg/kg/h
              * Dexmedetomidine 0.2-1.4 mcg/kg/h
            
            **4. Bệnh nhân quá sâu (RASS -4 đến -5):**
            - Giảm liều an thần
            - Đánh giá lại mức độ an thần thường xuyên
            - Cân nhắc ngừng hoặc giảm thuốc an thần
            - Tránh an thần quá sâu (tăng thời gian thở máy, tăng nguy cơ mê sảng)
            
            **Đánh giá thường xuyên:**
            - Mỗi 1-2 giờ trong ICU
            - Sau mỗi lần điều chỉnh liều an thần
            - Khi có thay đổi tình trạng bệnh nhân
            - Trước khi cai máy thở
            """)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
        
        # Comparison with Ramsay
        with st.expander("🔄 So sánh với Ramsay Sedation Scale"):
            st.markdown("""
            | RASS | Ramsay | Mô tả |
            |------|--------|-------|
            | +4 | 1 | Kích động nguy hiểm |
            | +3 | 1 | Kích động mạnh |
            | +2 | 1 | Kích động vừa |
            | +1 | 1 | Kích động nhẹ |
            | 0 | 2 | Tỉnh táo |
            | -1 | 3 | Buồn ngủ |
            | -2 | 3-4 | An thần nhẹ |
            | -3 | 4 | An thần vừa |
            | -4 | 5 | An thần sâu |
            | -5 | 6 | An thần rất sâu |
            
            **Ưu điểm RASS:**
            - Chi tiết hơn về mức độ kích động
            - Có thể đánh giá đáp ứng với kích thích
            - Được khuyến nghị nhiều hơn trong ICU hiện đại
            - Có hướng dẫn kích thích rõ ràng
            
            **Ưu điểm Ramsay:**
            - Đơn giản, dễ nhớ
            - Vẫn được sử dụng rộng rãi
            - Phù hợp khi không cần đánh giá chi tiết kích động
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "RASS Score": score
            }
            
            results_dict = {
                "RASS Score": f"{score:+d}",
                "Mức độ": result['level'],
                "Mô tả": result['description'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Save to history
            # Export section
            render_export_section(
                title="RASS - Richmond Agitation-Sedation Scale",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="RASS - Richmond Agitation-Sedation Scale"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="rass",
                calculator_name="RASS - Richmond Agitation-Sedation Scale",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="rass",
                calculator_name="RASS - Richmond Agitation-Sedation Scale",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="rass", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("RASS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

