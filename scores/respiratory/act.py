"""
Asthma Control Test (ACT)
=========================

Assesses asthma control level

Reference:
- Nathan RA, et al. Development of the asthma control test: a survey for assessing 
  asthma control. J Allergy Clin Immunol. 2004;113(1):59-65.

ACT Components (5 questions, each 1-5 points):
1. In the past 4 weeks, how much of the time did your asthma keep you from getting 
   as much done at work, school or at home?
2. During the past 4 weeks, how often have you had shortness of breath?
3. During the past 4 weeks, how often did your asthma symptoms (wheezing, coughing, 
   shortness of breath, chest tightness or pain) wake you up at night or earlier than 
   usual in the morning?
4. During the past 4 weeks, how often have you used your rescue inhaler or nebulizer 
   medication (such as albuterol)?
5. How would you rate your asthma control during the past 4 weeks?

Total: 5-25 points

Interpretation:
- 25: Well controlled
- 20-24: Well controlled
- 16-19: Not well controlled
- 5-15: Poorly controlled

Clinical Utility:
- Assess asthma control (used daily in respiratory clinics)
- Guide treatment decisions
- Monitor treatment response
- Part of asthma management guidelines
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


ACT_QUESTIONS = [
    {
        "question": "Trong 4 tuần qua, hen phế quản đã ngăn cản bạn hoàn thành công việc ở cơ quan, trường học hoặc ở nhà bao nhiêu lần?",
        "options": [
            "Tất cả thời gian",
            "Hầu hết thời gian",
            "Một số thời gian",
            "Rất ít thời gian",
            "Không bao giờ"
        ],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "Trong 4 tuần qua, bạn đã bị khó thở bao nhiêu lần?",
        "options": [
            "Hơn 1 lần/ngày",
            "1 lần/ngày",
            "3-6 lần/tuần",
            "1-2 lần/tuần",
            "Không bao giờ"
        ],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "Trong 4 tuần qua, các triệu chứng hen (thở khò khè, ho, khó thở, tức ngực hoặc đau ngực) đã đánh thức bạn vào ban đêm hoặc sớm hơn bình thường vào buổi sáng bao nhiêu lần?",
        "options": [
            "4 đêm trở lên/tuần",
            "2-3 đêm/tuần",
            "1 lần/tuần",
            "1-2 lần/tháng",
            "Không bao giờ"
        ],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "Trong 4 tuần qua, bạn đã sử dụng thuốc cắt cơn (như salbutamol) bao nhiêu lần?",
        "options": [
            "3 lần trở lên/ngày",
            "1-2 lần/ngày",
            "2-3 lần/tuần",
            "1 lần/tuần hoặc ít hơn",
            "Không bao giờ"
        ],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "Bạn đánh giá mức độ kiểm soát hen của mình trong 4 tuần qua như thế nào?",
        "options": [
            "Không kiểm soát được",
            "Kiểm soát kém",
            "Kiểm soát một phần",
            "Kiểm soát tốt",
            "Kiểm soát hoàn toàn"
        ],
        "scores": [1, 2, 3, 4, 5]
    }
]


def render():
    """Render Asthma Control Test (ACT) calculator"""
    
    st.title("🫁 Asthma Control Test (ACT)")
    st.markdown("**Đánh giá mức độ kiểm soát hen phế quản (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'act':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Asthma Control Test (ACT)** đánh giá mức độ kiểm soát hen phế quản:
        - Dùng hàng ngày trong phòng khám hô hấp
        - 5 câu hỏi đơn giản, bệnh nhân tự đánh giá
        - Điểm từ 5-25
        
        ### 🎯 5 Câu hỏi
        
        1. Hen ảnh hưởng đến công việc/học tập/hoạt động hàng ngày
        2. Tần suất khó thở
        3. Triệu chứng đánh thức ban đêm
        4. Sử dụng thuốc cắt cơn
        5. Đánh giá chủ quan về kiểm soát hen
        
        ### 📊 Phân loại
        
        - **25 điểm:** Kiểm soát hoàn toàn
        - **20-24 điểm:** Kiểm soát tốt
        - **16-19 điểm:** Kiểm soát chưa tốt
        - **5-15 điểm:** Kiểm soát kém
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="act",
            calculator_name="Asthma Control Test",
            category="Hô hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Trả lời 5 câu hỏi")
    
    st.markdown("""
    **Hướng dẫn:** Bệnh nhân tự đánh giá dựa trên tình trạng trong 4 tuần qua.
    """)
    
    answers = []
    total_score = 0
    
    for i, q_data in enumerate(ACT_QUESTIONS):
        st.markdown(f"#### Câu {i+1}/5")
        st.markdown(f"**{q_data['question']}**")
        
        answer = st.radio(
            "Chọn câu trả lời:",
            options=q_data['options'],
            index=4,  # Default to best answer
            key=f"act_q{i+1}",
            label_visibility="collapsed"
        )
        
        # Get score for selected answer
        answer_index = q_data['options'].index(answer)
        score = q_data['scores'][answer_index]
        answers.append({
            'question': q_data['question'],
            'answer': answer,
            'score': score
        })
        total_score += score
        
        st.caption(f"Điểm: {score}/5")
        st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính ACT Score", type="primary", use_container_width=True):
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**ACT Score**",
                f"{total_score}/25"
            )
        
        with col_r2:
            if total_score == 25:
                control_level = "Kiểm soát hoàn toàn"
                color = "success"
                icon = "✅"
            elif total_score >= 20:
                control_level = "Kiểm soát tốt"
                color = "success"
                icon = "✅"
            elif total_score >= 16:
                control_level = "Kiểm soát chưa tốt"
                color = "warning"
                icon = "⚠️"
            else:
                control_level = "Kiểm soát kém"
                color = "error"
                icon = "🚨"
            
            st.markdown(f"### {icon} {control_level}")
        
        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for i, ans in enumerate(answers):
                st.markdown(f"**Câu {i+1}:** {ans['answer']} → {ans['score']}/5 điểm")
            st.markdown(f"**Tổng điểm:** {total_score}/25")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if total_score == 25:
            st.success("""
            **✅ Kiểm soát hoàn toàn (25 điểm):**
            - Không có triệu chứng hen
            - Không cần thuốc cắt cơn
            - Hoạt động bình thường
            - Khuyến cáo: Duy trì điều trị hiện tại
            """)
        elif total_score >= 20:
            st.success("""
            **✅ Kiểm soát tốt (20-24 điểm):**
            - Triệu chứng hen tối thiểu
            - Ít sử dụng thuốc cắt cơn
            - Hoạt động gần như bình thường
            - Khuyến cáo: Duy trì điều trị, theo dõi định kỳ
            """)
        elif total_score >= 16:
            st.warning("""
            **⚠️ Kiểm soát chưa tốt (16-19 điểm):**
            - Có triệu chứng hen thường xuyên
            - Sử dụng thuốc cắt cơn nhiều
            - Ảnh hưởng đến hoạt động hàng ngày
            - Khuyến cáo: 
              * Tăng liều thuốc kiểm soát (ICS)
              * Xem xét thêm LABA
              * Đánh giá kỹ thuật dùng thuốc
              * Kiểm tra tuân thủ điều trị
            """)
        else:
            st.error("""
            **🚨 Kiểm soát kém (5-15 điểm):**
            - Triệu chứng hen thường xuyên và nặng
            - Sử dụng thuốc cắt cơn nhiều
            - Ảnh hưởng nghiêm trọng đến hoạt động
            - Khuyến cáo:
              * Tăng liều thuốc kiểm soát ngay
              * Xem xét ICS/LABA liều cao
              * Đánh giá kỹ thuật dùng thuốc
              * Kiểm tra tuân thủ điều trị
              * Xem xét thêm thuốc (LTRA, theophylline)
              * Tái khám sớm (1-2 tuần)
            """)
        
        # Treatment recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị theo GINA")
        
        if total_score >= 20:
            st.info("""
            **Bước 1-2 (Kiểm soát tốt):**
            - SABA khi cần (Step 1)
            - Hoặc ICS liều thấp (Step 2)
            - Duy trì điều trị hiện tại
            """)
        elif total_score >= 16:
            st.warning("""
            **Bước 3 (Kiểm soát chưa tốt):**
            - ICS/LABA liều thấp-trung bình
            - Hoặc ICS liều trung bình-cao
            - Đánh giá lại sau 2-3 tháng
            """)
        else:
            st.error("""
            **Bước 4-5 (Kiểm soát kém):**
            - ICS/LABA liều trung bình-cao
            - Có thể thêm LTRA, theophylline
            - Xem xét kháng IgE (nếu dị ứng)
            - Tái khám sớm (1-2 tuần)
            """)
        
        # Prepare inputs and results
        inputs_dict = {}
        for i, ans in enumerate(answers):
            inputs_dict[f"Câu {i+1}"] = ans['answer']
        
        results_dict = {
            "ACT Score": f"{total_score}/25",
            "Control Level": control_level,
            "Recommendation": "Duy trì" if total_score >= 20 else "Tăng liều" if total_score >= 16 else "Điều trị tích cực"
        }
        
        # Export section
        render_export_section(
            title="Asthma Control Test",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Asthma Control Test"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="act",
            calculator_name="Asthma Control Test",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="act",
            calculator_name="Asthma Control Test",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="act", show_actions=True)
        
        # References section
        references = get_references("ACT")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['act_result'] = {
            'score': total_score,
            'control_level': control_level
        }
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("ACT")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **Asthma Control Test (ACT)**
            
            **Reference:**
            Nathan RA, Sorkness CA, Kosinski M, et al. Development of the asthma control test: 
            a survey for assessing asthma control. J Allergy Clin Immunol. 2004;113(1):59-65.
            
            **GINA Guidelines:**
            Global Initiative for Asthma (GINA). Global Strategy for Asthma Management and Prevention. 
            2024 Update.
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

