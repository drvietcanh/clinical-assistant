"""
FLACC - Face, Legs, Activity, Cry, Consolability
Thang điểm đánh giá đau ở trẻ em (2 tháng - 7 tuổi)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def render():
    """FLACC Pain Scale Calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'flacc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'FLACC')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>👶 FLACC - Face, Legs, Activity, Cry, Consolability</h2>
    <p style='text-align: center;'><em>Thang điểm đánh giá đau ở trẻ em (2 tháng - 7 tuổi)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **FLACC** là thang điểm quan sát hành vi để đánh giá đau ở trẻ em không thể tự báo cáo.
        
        **Chỉ định:**
        - Trẻ em 2 tháng - 7 tuổi
        - Trẻ không thể giao tiếp (hôn mê, thở máy, chậm phát triển)
        - Sau phẫu thuật, chấn thương
        
        **5 Tiêu chí (mỗi tiêu chí 0-2 điểm):**
        1. **Face (Khuôn mặt)**
        2. **Legs (Chân)**
        3. **Activity (Hoạt động)**
        4. **Cry (Khóc)**
        5. **Consolability (Có thể dỗ được)**
        
        **Tổng điểm: 0-10**
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá đau")
    
    # Face
    st.markdown("### 1️⃣ Face (Khuôn mặt)")
    face_score = st.radio(
        "Biểu hiện khuôn mặt:",
        [
            "0 - Vui vẻ, cười, không có biểu hiện đau",
            "1 - Nhăn mặt thỉnh thoảng, vẻ mặt lo lắng, cau mày",
            "2 - Nhăn mặt liên tục, rên rỉ, cau mày, cằm run"
        ],
        key="flacc_face"
    )
    face = int(face_score[0])
    
    # Legs
    st.markdown("### 2️⃣ Legs (Chân)")
    legs_score = st.radio(
        "Vị trí và cử động chân:",
        [
            "0 - Bình thường, tư thế thoải mái",
            "1 - Không yên, căng thẳng, co rút, duỗi thẳng",
            "2 - Đá, co rút, hoặc co cứng chân"
        ],
        key="flacc_legs"
    )
    legs = int(legs_score[0])
    
    # Activity
    st.markdown("### 3️⃣ Activity (Hoạt động)")
    activity_score = st.radio(
        "Hoạt động cơ thể:",
        [
            "0 - Nằm yên, tư thế bình thường, di chuyển dễ dàng",
            "1 - Không yên, cử động qua lại, căng thẳng",
            "2 - Cong lưng, cứng, hoặc giật mình"
        ],
        key="flacc_activity"
    )
    activity = int(activity_score[0])
    
    # Cry
    st.markdown("### 4️⃣ Cry (Khóc)")
    cry_score = st.radio(
        "Khóc:",
        [
            "0 - Không khóc (tỉnh táo hoặc ngủ)",
            "1 - Rên rỉ, khóc nhẹ, than vãn thỉnh thoảng",
            "2 - Khóc liên tục, gào thét, rên rỉ thường xuyên"
        ],
        key="flacc_cry"
    )
    cry = int(cry_score[0])
    
    # Consolability
    st.markdown("### 5️⃣ Consolability (Có thể dỗ được)")
    consolability_score = st.radio(
        "Khả năng dỗ dành:",
        [
            "0 - Dỗ được, thoải mái, không cần can thiệp",
            "1 - Dỗ được bằng cách nói chuyện, chạm nhẹ, ôm, hoặc phân tâm",
            "2 - Khó dỗ, không thể an ủi, không thể dỗ được"
        ],
        key="flacc_consolability"
    )
    consolability = int(consolability_score[0])
    
    st.markdown("---")
    
    if st.button("📊 Tính điểm FLACC", type="primary", use_container_width=True):
        total_score = face + legs + activity + cry + consolability
        
        st.markdown("## 📊 Kết quả")
        
        # Interpret score
        if total_score == 0:
            severity = "Không đau"
            color = "#10b981"
            icon = "✅"
            interpretation = "Trẻ không có dấu hiệu đau"
        elif total_score <= 3:
            severity = "Đau nhẹ"
            color = "#fbbf24"
            icon = "😐"
            interpretation = "Đau nhẹ, cần theo dõi"
        elif total_score <= 6:
            severity = "Đau vừa"
            color = "#f59e0b"
            icon = "😣"
            interpretation = "Đau vừa, cần điều trị giảm đau"
        else:
            severity = "Đau nặng"
            color = "#ef4444"
            icon = "😰"
            interpretation = "Đau nặng, cần điều trị ngay lập tức"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} FLACC = {total_score}/10
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {severity}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Chi tiết
        st.markdown("### 📋 Chi tiết điểm số:")
        st.markdown(f"""
        - **Face (Khuôn mặt):** {face}/2
        - **Legs (Chân):** {legs}/2
        - **Activity (Hoạt động):** {activity}/2
        - **Cry (Khóc):** {cry}/2
        - **Consolability (Dỗ được):** {consolability}/2
        
        **Tổng:** {total_score}/10
        """)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Treatment recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến nghị điều trị")
        
        if total_score == 0:
            st.success("**✅ Không cần điều trị giảm đau**")
        elif total_score <= 3:
            st.info("""
            **💊 Đau nhẹ (FLACC 1-3):**
            
            **Điều trị:**
            - Paracetamol: 15 mg/kg mỗi 4-6 giờ (max 60 mg/kg/ngày)
            - Ibuprofen: 10 mg/kg mỗi 6-8 giờ (nếu > 6 tháng tuổi)
            
            **Theo dõi:**
            - Đánh giá lại sau 30-60 phút
            - Mục tiêu: FLACC ≤ 3
            """)
        elif total_score <= 6:
            st.warning("""
            **💊 Đau vừa (FLACC 4-6):**
            
            **Điều trị:**
            - Paracetamol + Ibuprofen (nếu không chống chỉ định)
            - Hoặc Codeine: 0.5-1 mg/kg mỗi 4-6 giờ (nếu > 1 tuổi)
            - Hoặc Tramadol: 1-2 mg/kg mỗi 6-8 giờ (nếu > 1 tuổi)
            
            **Theo dõi:**
            - Đánh giá lại sau 30 phút
            - Mục tiêu: FLACC ≤ 3
            """)
        else:
            st.error("""
            **🚨 Đau nặng (FLACC 7-10):**
            
            **Điều trị khẩn:**
            - **Morphine IV:** 0.05-0.1 mg/kg mỗi 2-4 giờ
            - Hoặc **Fentanyl IV:** 1-2 µg/kg bolus, sau đó 0.5-1 µg/kg/h
            - Kết hợp Paracetamol và NSAID
            
            **Theo dõi:**
            - Đánh giá lại sau 15-30 phút
            - Mục tiêu: FLACC ≤ 3 trong vòng 1 giờ
            - Theo dõi tác dụng phụ: ức chế hô hấp, buồn nôn
            
            **Cảnh báo:**
            - Đau nặng ở trẻ em cần điều trị ngay lập tức
            - Cân nhắc nguyên nhân đau
            """)
        
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            1. **Quan sát trẻ trong 2-5 phút:**
               - Không làm trẻ chú ý
               - Quan sát khi trẻ nghỉ ngơi và khi vận động (nếu có thể)
            
            2. **Đánh giá từng tiêu chí:**
               - Chọn mức độ phù hợp nhất cho mỗi tiêu chí
               - Dựa trên quan sát hành vi, không phải hỏi trẻ
            
            3. **Tính tổng điểm:**
               - Cộng điểm của 5 tiêu chí
               - Tổng điểm: 0-10
            
            ### 📋 Khi nào đánh giá:
            - Khi trẻ vào viện
            - Trước và sau điều trị giảm đau
            - Mỗi 2-4 giờ ở trẻ nội trú
            - Sau phẫu thuật: Mỗi 1-2 giờ trong 24 giờ đầu
            - Khi có dấu hiệu đau (khóc, không yên, nhăn mặt...)
            
            ### ⚠️ Lưu ý:
            - FLACC dùng cho trẻ 2 tháng - 7 tuổi
            - Trẻ sơ sinh < 2 tháng: Dùng NIPS
            - Trẻ > 7 tuổi có thể giao tiếp: Dùng NRS hoặc Wong-Baker Faces
            - Đánh giá khi trẻ tỉnh táo (không ngủ sâu)
            - Cân nhắc các yếu tố khác: đói, sợ hãi, bệnh lý nền
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Merkel SI, Voepel-Lewis T, Shayevitz JR, Malviya S.** The FLACC: a behavioral scale for scoring postoperative pain in young children. 
               *Pediatr Nurs.* 1997;23(3):293-297.
            
            2. **Voepel-Lewis T, Zanotti J, Dammeyer JA, Merkel S.** Reliability and validity of the face, legs, activity, cry, consolability behavioral tool in assessing acute pain in critically ill patients. 
               *Am J Crit Care.* 2010;19(1):55-61.
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Face": face,
            "Legs": legs,
            "Activity": activity,
            "Cry": cry,
            "Consolability": consolability
        }
        
        results_dict = {
            "FLACC Score": f"{total_score}/10",
            "Severity": severity,
            "Interpretation": interpretation
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="flacc",
            calculator_name="FLACC",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="flacc",
            calculator_name="FLACC",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="flacc",
            calculator_name="FLACC",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="flacc", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="flacc",
            calculator_name="FLACC",
            category="Đau",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **FLACC 0:** Không đau
    2. **FLACC 1-3:** Đau nhẹ → Paracetamol/NSAID
    3. **FLACC 4-6:** Đau vừa → Opioid yếu
    4. **FLACC 7-10:** Đau nặng → Opioid mạnh ngay lập tức
    5. **Mục tiêu:** FLACC ≤ 3
    6. **Đánh giá lại:** Sau 15-30 phút (đau nặng) hoặc 30-60 phút (đau nhẹ/vừa)
    """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("FLACC")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

