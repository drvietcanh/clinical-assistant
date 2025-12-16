"""
HAS-BLED Score Calculator
Bleeding risk assessment in patients on anticoagulation
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def render():
    """HAS-BLED Score Calculator"""
    st.subheader("🩸 HAS-BLED Score")
    st.caption("Đánh giá Nguy cơ Chảy máu Khi Dùng Kháng đông")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'hasbled':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        htn_uncontrolled = st.checkbox(
            "**H** - Tăng huyết áp không kiểm soát",
            help="SBP >160 mmHg"
        )
        
        renal = st.checkbox("Chức năng thận bất thường", help="Lọc cầu thận <60 hoặc chạy thận")
        liver = st.checkbox("Chức năng gan bất thường", help="Xơ gan hoặc men gan tăng >2 lần")
        
        stroke_bled = st.checkbox(
            "**S** - Tiền sử đột quỵ",
            help="Đột quỵ trước đây"
        )
        
        bleeding = st.checkbox(
            "**B** - Tiền sử chảy máu hoặc thiểu máu",
            help="Chảy máu nặng hoặc thiểu máu trước đây"
        )
        
        labile_inr = st.checkbox(
            "**L** - INR không ổn định",
            help="TTR <60% nếu dùng warfarin"
        )
        
        age_hasbled = st.checkbox(
            "**E** - Tuổi cao (>65)",
            help="Tuổi >65"
        )
        
        drugs = st.checkbox("Dùng thuốc chống tiểu cầu/NSAID", help="Aspirin, NSAID")
        alcohol = st.checkbox("Lạm dụng rượu", help=">8 đơn vị/tuần")
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="hasbled",
            calculator_name="HAS-BLED Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🧮 Tính Điểm HAS-BLED", type="primary", key="hasbled_calc", use_container_width=True):
            score = 0
            details = []
            
            if htn_uncontrolled:
                score += 1
                details.append("✓ THA không kiểm soát (+1)")
            if renal:
                score += 1
                details.append("✓ Suy thận (+1)")
            if liver:
                score += 1
                details.append("✓ Suy gan (+1)")
            if stroke_bled:
                score += 1
                details.append("✓ Tiền sử đột quỵ (+1)")
            if bleeding:
                score += 1
                details.append("✓ Tiền sử chảy máu (+1)")
            if labile_inr:
                score += 1
                details.append("✓ INR không ổn định (+1)")
            if age_hasbled:
                score += 1
                details.append("✓ Tuổi >65 (+1)")
            if drugs:
                score += 1
                details.append("✓ Dùng chống tiểu cầu/NSAID (+1)")
            if alcohol:
                score += 1
                details.append("✓ Lạm dụng rượu (+1)")
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                if score <= 2:
                    st.success(f"## HAS-BLED = {score}")
                    st.success("✅ Nguy cơ chảy máu THẤP")
                elif score == 3:
                    st.warning(f"## HAS-BLED = {score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                else:
                    st.error(f"## HAS-BLED = {score}")
                    st.error("🚨 Nguy cơ chảy máu CAO")
            
            st.markdown("### 💡 Giải thích")
            
            if details:
                for d in details:
                    st.write(f"- {d}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo")
            
            if score <= 2:
                st.success("""
                **Nguy cơ chảy máu chấp nhận được**
                - Có thể dùng kháng đông an toàn
                - Theo dõi định kỳ
                """)
            elif score == 3:
                st.warning("""
                **Cẩn thận khi dùng kháng đông**
                - Kiểm soát các yếu tố nguy cơ có thể sửa
                - Theo dõi sát hơn
                - Cân nhắc NOAC thay vì warfarin
                """)
            else:
                st.error("""
                **Nguy cơ chảy máu cao - Thận trọng!**
                
                **KHÔNG PHẢI CHỐNG CHỈ ĐỊNH kháng đông!**
                
                **Cần làm:**
                - Kiểm soát THA tốt hơn
                - Ngừng NSAID/aspirin nếu được
                - Giảm rượu
                - Cân nhắc dùng PPI bảo vệ dạ dày
                - Ưu tiên NOAC hơn warfarin
                - Theo dõi sát sao
                """)
            
            # Prepare inputs and results for export/history
            inputs_dict = {
                "HTN Uncontrolled": "Có" if htn_uncontrolled else "Không",
                "Renal Dysfunction": "Có" if renal else "Không",
                "Liver Dysfunction": "Có" if liver else "Không",
                "Stroke History": "Có" if stroke_bled else "Không",
                "Bleeding History": "Có" if bleeding else "Không",
                "Labile INR": "Có" if labile_inr else "Không",
                "Age >65": "Có" if age_hasbled else "Không",
                "Drugs": "Có" if drugs else "Không",
                "Alcohol": "Có" if alcohol else "Không"
            }
            
            risk_level_text = "THẤP" if score <= 2 else "TRUNG BÌNH" if score == 3 else "CAO"
            results_dict = {
                "HAS-BLED Score": f"{score} điểm",
                "Risk Level": risk_level_text,
                "Details": "\n".join(details) if details else "Không có yếu tố nguy cơ"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"HAS-BLED = {score} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="HAS-BLED Score",
                filename="hasbled_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="hasbled",
                calculator_name="HAS-BLED Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="hasbled",
                calculator_name="HAS-BLED Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="hasbled", show_actions=True)
            
            # References section
            references = get_references("HAS-BLED")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            else:
                # Fallback to manual references if not in config
                with st.expander("📚 Tài liệu tham khảo"):
                    st.markdown("""
                    **HAS-BLED Score**
                    
                    **Tiêu chí (1 điểm mỗi mục):**
                    - **H**: Hypertension (SBP >160 mmHg)
                    - **A**: Abnormal renal/liver function (1-2 điểm)
                    - **S**: Stroke (tiền sử đột quỵ)
                    - **B**: Bleeding history/predisposition
                    - **L**: Labile INR (TTR <60%)
                    - **E**: Elderly (>65 tuổi)
                    - **D**: Drugs (antiplatelet/NSAID) or Alcohol
                    
                    **Reference:**
                    Pisters R, et al. Chest. 2010;138(5):1093-1100.
                    """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("HAS-BLED")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

