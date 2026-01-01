"""
Surgical Apgar Score Calculator
Đánh giá nguy cơ biến chứng sau mổ dựa trên 3 yếu tố trong mổ
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


def calculate_surgical_apgar(hr_min, sbp_min, blood_loss):
    """
    Tính điểm Surgical Apgar Score
    
    Parameters:
    - hr_min: Nhịp tim tối thiểu trong mổ (0-2 điểm)
    - sbp_min: Huyết áp tâm thu tối thiểu trong mổ (0-2 điểm)
    - blood_loss: Mất máu ước tính (0-2 điểm)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = hr_min + sbp_min + blood_loss
    
    # Interpretation based on Gawande et al. 2007
    if total >= 7:
        risk = "Nguy cơ thấp"
        complication_rate = "3-5%"
        recommendation = "Tiên lượng tốt, theo dõi thường quy"
        color = COLORS["success"]
    elif total >= 4:
        risk = "Nguy cơ trung bình"
        complication_rate = "15-20%"
        recommendation = "Theo dõi sát, chuẩn bị xử trí biến chứng"
        color = COLORS["warning"]
    else:  # 0-3
        risk = "Nguy cơ cao"
        complication_rate = "30-40%"
        recommendation = "Theo dõi tích cực, có thể cần ICU, chuẩn bị xử trí biến chứng nghiêm trọng"
        color = COLORS["error"]
    
    return {
        "total_score": total,
        "risk": risk,
        "complication_rate": complication_rate,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render Surgical Apgar Score interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'surgical_apgar':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Surgical Apgar Score')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🏥 Surgical Apgar Score</h2>
    <p style='text-align: center;'><em>Đánh giá nguy cơ biến chứng sau mổ dựa trên 3 yếu tố trong mổ</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Surgical Apgar Score"):
        st.markdown("""
        **Surgical Apgar Score** là thang điểm đánh giá nguy cơ biến chứng sau phẫu thuật,
        dựa trên 3 yếu tố quan trọng trong quá trình phẫu thuật.
        
        **3 yếu tố đánh giá (mỗi yếu tố 0-2 điểm, tổng 10 điểm):**
        
        1. **Nhịp tim tối thiểu trong mổ (HR min)**
           - 2 điểm: ≥56 bpm
           - 1 điểm: 41-55 bpm
           - 0 điểm: ≤40 bpm
        
        2. **Huyết áp tâm thu tối thiểu trong mổ (SBP min)**
           - 2 điểm: ≥100 mmHg
           - 1 điểm: 70-99 mmHg
           - 0 điểm: <70 mmHg
        
        3. **Mất máu ước tính (Blood loss)**
           - 2 điểm: ≤100 mL
           - 1 điểm: 101-500 mL
           - 0 điểm: >500 mL
        
        **Điểm số và nguy cơ:**
        - **7-10 điểm:** Nguy cơ thấp (3-5% biến chứng)
        - **4-6 điểm:** Nguy cơ trung bình (15-20% biến chứng)
        - **0-3 điểm:** Nguy cơ cao (30-40% biến chứng)
        
        **Biến chứng được đánh giá:**
        - Nhiễm trùng vết mổ
        - Suy thận cấp
        - Suy hô hấp
        - Tử vong trong 30 ngày
        
        **Ưu điểm:**
        - Đơn giản, dễ tính toán
        - Đánh giá ngay sau mổ
        - Dự đoán tốt biến chứng sau mổ
        
        **Reference:** Gawande AA, et al. An Apgar score for surgery. 
        J Am Coll Surg. 2007;204(2):201-8.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 3 yếu tố trong mổ (mỗi yếu tố 0-2 điểm)")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="surgical_apgar",
            calculator_name="Surgical Apgar Score",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # HR min
    st.markdown("### 1️⃣ Nhịp tim tối thiểu trong mổ (HR min)")
    hr_min = st.radio(
        "Nhịp tim tối thiểu:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - ≥56 bpm",
            1: "1 điểm - 41-55 bpm",
            0: "0 điểm - ≤40 bpm"
        }[x],
        key="surgical_apgar_hr",
        horizontal=False
    )
    
    # SBP min
    st.markdown("### 2️⃣ Huyết áp tâm thu tối thiểu trong mổ (SBP min)")
    sbp_min = st.radio(
        "Huyết áp tâm thu tối thiểu:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - ≥100 mmHg",
            1: "1 điểm - 70-99 mmHg",
            0: "0 điểm - <70 mmHg"
        }[x],
        key="surgical_apgar_sbp",
        horizontal=False
    )
    
    # Blood loss
    st.markdown("### 3️⃣ Mất máu ước tính (Blood loss)")
    blood_loss = st.radio(
        "Mất máu ước tính:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - ≤100 mL",
            1: "1 điểm - 101-500 mL",
            0: "0 điểm - >500 mL"
        }[x],
        key="surgical_apgar_blood",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Surgical Apgar", type="primary", use_container_width=True):
        try:
            result = calculate_surgical_apgar(hr_min, sbp_min, blood_loss)
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/10")
            
            with col2:
                st.metric("Nguy cơ", result['risk'])
            
            with col3:
                st.metric("Tỷ lệ biến chứng", result['complication_rate'])
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == COLORS["success"]:
                st.success(f"**{result['risk']}** - Tỷ lệ biến chứng: {result['complication_rate']}")
            elif result['color'] == COLORS["warning"]:
                st.warning(f"**{result['risk']}** - Tỷ lệ biến chứng: {result['complication_rate']}")
            else:
                st.error(f"**{result['risk']}** - Tỷ lệ biến chứng: {result['complication_rate']}")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Breakdown
            st.subheader("📋 Chi tiết điểm số")
            components = [
                ("Nhịp tim tối thiểu", hr_min, 2),
                ("Huyết áp tối thiểu", sbp_min, 2),
                ("Mất máu", blood_loss, 2)
            ]
            
            for name, score, max_score in components:
                percentage = (score / max_score) * 100
                st.progress(percentage / 100, text=f"{name}: {score}/{max_score}")
            
            st.markdown("---")
            
            # Additional information
            with st.expander("📚 Thông tin bổ sung"):
                st.markdown("""
                **Biến chứng sau mổ thường gặp:**
                
                1. **Nhiễm trùng vết mổ**
                   - Theo dõi vết mổ hàng ngày
                   - Phát hiện sớm: đỏ, sưng, chảy mủ
                
                2. **Suy thận cấp**
                   - Theo dõi lượng nước tiểu
                   - Xét nghiệm creatinine, BUN
                
                3. **Suy hô hấp**
                   - Theo dõi SpO₂, nhịp thở
                   - Có thể cần hỗ trợ thở
                
                4. **Tử vong trong 30 ngày**
                   - Theo dõi sát dấu hiệu sinh tồn
                   - Xử trí kịp thời các biến chứng
                
                **Theo dõi sau mổ:**
                - Điểm 7-10: Theo dõi thường quy
                - Điểm 4-6: Theo dõi sát, có thể cần monitoring
                - Điểm 0-3: Theo dõi tích cực, cân nhắc ICU
                """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Nhịp tim tối thiểu": f"{hr_min}/2",
                "Huyết áp tối thiểu": f"{sbp_min}/2",
                "Mất máu": f"{blood_loss}/2"
            }
            
            results_dict = {
                "Tổng điểm": f"{result['total_score']}/10",
                "Nguy cơ": result['risk'],
                "Tỷ lệ biến chứng": result['complication_rate'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Export section
            render_export_section(
                title="Surgical Apgar Score",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="Surgical Apgar Score"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="surgical_apgar",
                calculator_name="Surgical Apgar Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="surgical_apgar",
                calculator_name="Surgical Apgar Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="surgical_apgar", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("surgical_apgar")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

