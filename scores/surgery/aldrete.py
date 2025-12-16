"""
Aldrete Score Calculator
Đánh giá hồi tỉnh sau gây mê
"""

import streamlit as st
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from scores.references_config import get_references
from components.references import render_references_section


def calculate_aldrete(activity, respiration, circulation, consciousness, color):
    """
    Tính điểm Aldrete
    
    Parameters: Mỗi thành phần 0-2 điểm
    - activity: Hoạt động vận động
    - respiration: Hô hấp
    - circulation: Tuần hoàn (BP)
    - consciousness: Ý thức
    - color: Màu sắc da/SpO₂
    
    Returns:
    - dict với total_score và interpretation
    """
    total = activity + respiration + circulation + consciousness + color
    
    # Phân loại
    if total >= 9:
        status = "Đủ tiêu chuẩn xuất phòng hồi tỉnh"
        recommendation = "Có thể chuyển về phòng/xuất viện (nếu phẫu thuật ngoại trú)"
        color_display = "green"
    elif total >= 7:
        status = "Cần theo dõi thêm"
        recommendation = "Tiếp tục theo dõi tại phòng hồi tỉnh"
        color_display = "orange"
    else:
        status = "Chưa đủ tiêu chuẩn"
        recommendation = "Tiếp tục hồi sức, đánh giá lại"
        color_display = "red"
    
    return {
        "total_score": total,
        "status": status,
        "recommendation": recommendation,
        "color": color_display
    }


def render():
    """Render Aldrete Score interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'aldrete':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🏥 Aldrete Score</h2>
    <p style='text-align: center;'><em>Đánh giá hồi tỉnh sau gây mê</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Aldrete Score"):
        st.markdown("""
        **Aldrete Score** là thang điểm đánh giá khả năng hồi tỉnh sau gây mê, 
        giúp quyết định khi nào bệnh nhân có thể rời phòng hồi tỉnh (PACU).
        
        **Mục đích:**
        - Đánh giá an toàn sau gây mê
        - Quyết định xuất phòng hồi tỉnh
        - Đảm bảo bệnh nhân ổn định
        
        **Tiêu chuẩn xuất PACU:**
        - **Điểm ≥ 9/10:** Đủ tiêu chuẩn
        - Đánh giá mỗi 15-30 phút
        
        **Phiên bản:**
        - Aldrete gốc (1970): Màu sắc da
        - Aldrete sửa đổi (1995): SpO₂ thay màu da
        - Hiện nay dùng phiên bản sửa đổi
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 5 thành phần")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="aldrete",
            calculator_name="Aldrete Score",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Activity
    st.markdown("### 1️⃣ Hoạt động vận động (Activity)")
    activity = st.radio(
        "Chọn mức độ:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Cử động 4 chi theo lệnh",
            1: "1 điểm - Cử động 2 chi theo lệnh",
            0: "0 điểm - Không cử động được"
        }[x],
        key="aldrete_activity",
        horizontal=False
    )
    
    # Respiration
    st.markdown("### 2️⃣ Hô hấp (Respiration)")
    respiration = st.radio(
        "Chọn mức độ:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Thở sâu, ho được",
            1: "1 điểm - Thở nông/hạn chế, khó thở",
            0: "0 điểm - Ngừng thở hoặc cần hỗ trợ thở"
        }[x],
        key="aldrete_resp",
        horizontal=False
    )
    
    # Circulation
    st.markdown("### 3️⃣ Tuần hoàn - Huyết áp (Circulation)")
    circulation = st.radio(
        "So với huyết áp trước mổ:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - BP ± 20% so với trước mổ",
            1: "1 điểm - BP ± 20-50% so với trước mổ",
            0: "0 điểm - BP ± > 50% so với trước mổ"
        }[x],
        key="aldrete_bp",
        horizontal=False
    )
    
    # Consciousness
    st.markdown("### 4️⃣ Ý thức (Consciousness)")
    consciousness = st.radio(
        "Chọn mức độ:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - Tỉnh hoàn toàn",
            1: "1 điểm - Đánh thức được",
            0: "0 điểm - Không đáp ứng"
        }[x],
        key="aldrete_consc",
        horizontal=False
    )
    
    # Color / SpO2
    st.markdown("### 5️⃣ Độ bão hòa oxy (SpO₂) - Phiên bản sửa đổi")
    color = st.radio(
        "Chọn mức độ:",
        options=[2, 1, 0],
        format_func=lambda x: {
            2: "2 điểm - SpO₂ > 92% (không cần O₂)",
            1: "1 điểm - Cần O₂ để duy trì SpO₂ > 90%",
            0: "0 điểm - SpO₂ < 90% dù có O₂"
        }[x],
        key="aldrete_spo2",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Aldrete", type="primary", use_container_width=True):
        result = calculate_aldrete(activity, respiration, circulation, consciousness, color)
        
        st.markdown("## 📊 Kết quả")
        
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                Aldrete Score: {result['total_score']}/10
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Component breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("🏃 Vận động", f"{activity}/2")
            st.metric("🫁 Hô hấp", f"{respiration}/2")
            st.metric("💓 Tuần hoàn", f"{circulation}/2")
        
        with col2:
            st.metric("🧠 Ý thức", f"{consciousness}/2")
            st.metric("🩸 SpO₂", f"{color}/2")
        
        st.markdown("---")
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Kết luận</h3>
            <p style='font-size: 1.2em; font-weight: bold;'>{result['status']}</p>
            <p style='font-size: 1.1em;'>💡 {result['recommendation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Clinical implications
        if result["total_score"] >= 9:
            st.success("""
            ✅ **Điểm ≥ 9: ĐỦ TIÊU CHUẨN XUẤT PACU**
            
            **Tiêu chuẩn xuất phòng hồi tỉnh:**
            - Aldrete ≥ 9/10 ✓
            - Dấu hiệu sinh tồn ổn định
            - Không chảy máu bất thường
            - Không buồn nôn/nôn nghiêm trọng
            - Đau được kiểm soát
            
            **Phẫu thuật ngoại trú - Tiêu chuẩn xuất viện:**
            - Aldrete ≥ 9
            - Đi lại được (nếu gây tê tủy sống/ngoài màng cứng)
            - Dung nạp nước/thức ăn
            - Đái được (tùy loại phẫu thuật)
            - Có người nhà đưa về
            - Hiểu hướng dẫn sau mổ
            """)
        elif result["total_score"] >= 7:
            st.warning("""
            ⚠️ **Điểm 7-8: CẦN THEO DÕI THÊM**
            
            **Hành động:**
            - Tiếp tục theo dõi tại PACU
            - Đánh giá lại sau 15-30 phút
            - Xử trí vấn đề còn tồn tại:
              - Đau: Tăng giảm đau
              - Buồn nôn: Thuốc chống nôn
              - Hô hấp: O₂, hỗ trợ thở
              - BP bất ổn: Truyền dịch, thuốc vận mạch
            """)
        else:
            st.error("""
            🔴 **Điểm < 7: CHƯA ĐỦ TIÊU CHUẨN**
            
            **Hành động:**
            - Tiếp tục hồi sức tích cực
            - Xác định và xử trí vấn đề:
              - **Ý thức kém:** Reversal (Flumazenil, Naloxone), kích thích
              - **Hô hấp kém:** Hỗ trợ thở, kiểm tra khí máu
              - **Tuần hoàn không ổn:** Truyền dịch, thuốc
              - **SpO₂ thấp:** Tăng O₂, hút đờm, CPAP
            - Đánh giá lại thường xuyên
            - Cân nhắc chuyển ICU nếu không cải thiện
            """)
        
        with st.expander("📋 Tiêu chuẩn xuất PACU đầy đủ"):
            st.markdown("""
            ### Tiêu chuẩn chuẩn xuất phòng hồi tỉnh:
            
            **1. Aldrete Score ≥ 9/10** ✓
            
            **2. Dấu hiệu sinh tồn ổn định:**
            - Huyết áp, mạch, nhiệt độ trong giới hạn bình thường
            - SpO₂ > 92% (hoặc bằng baseline)
            - Không loạn nhịp tim đáng kể
            
            **3. Đường thở:**
            - Tự thở hiệu quả
            - Bảo vệ đường thở tốt
            - Không tắc nghẽn
            
            **4. Ý thức:**
            - Tỉnh táo hoặc về mức baseline
            - Định hướng (nếu phù hợp)
            
            **5. Kiểm soát đau:**
            - Đau được kiểm soát ở mức chấp nhận được
            - VAS < 4
            
            **6. Buồn nôn/nôn:**
            - Không hoặc kiểm soát được
            
            **7. Vị trí phẫu thuật:**
            - Không chảy máu bất thường
            - Băng khô
            
            **8. Nước tiểu:**
            - Đái được (tùy loại phẫu thuật)
            - Đặc biệt: Phẫu thuật tiết niệu, tê tủy sống
            
            ### Phẫu thuật ngoại trú - Tiêu chuẩn thêm:
            
            **9. Dung nạp đường uống:**
            - Uống nước/thức ăn nhẹ không nôn
            
            **10. Di chuyển:**
            - Đi lại được (nếu gây tê vùng)
            - Ngồi dậy không chóng mặt
            
            **11. Điều kiện nhà:**
            - Có người nhà chăm sóc 24h
            - Hiểu hướng dẫn sau mổ
            - Có phương tiện về nhà
            - Có số điện thoại liên lạc
            """)
        
        with st.expander("⚠️ Biến chứng thường gặp PACU"):
            st.markdown("""
            ### 1. Hô hấp:
            - **Tắc nghẽn đường thở:** Nâng hàm, đặt ống thông hầu
            - **Giảm thông khí:** Reversal, hỗ trợ thở
            - **Thanh quản co thắt:** O₂, adrenaline, tái đặt NKQ
            - **Hít sặc:** Hút, kháng sinh
            
            ### 2. Tuần hoàn:
            - **Tăng huyết áp:** Giảm đau, thuốc hạ áp
            - **Hạ huyết áp:** Truyền dịch, vasopressor
            - **Loạn nhịp:** Theo dõi, điều trị phù hợp
            - **Nhồi máu cơ tim:** ECG, Troponin, điều trị
            
            ### 3. Đau:
            - Đánh giá thường xuyên (VAS/NRS)
            - Multimodal analgesia
            - Opioid nếu cần (theo dõi hô hấp)
            
            ### 4. Buồn nôn/nôn (PONV):
            - Ondansetron, Metoclopramide
            - Dexamethasone
            - Truyền dịch đầy đủ
            
            ### 5. Run (Shivering):
            - Chăn ấm, không khí ấm
            - Pethidine liều thấp nếu cần
            
            ### 6. Mê sảng (Delirium):
            - Đặc biệt ở người cao tuổi
            - Định hướng, môi trường yên tĩnh
            - Tránh BZD (trừ cai rượu)
            
            ### 7. Chậm tỉnh:
            - Kiểm tra đường huyết
            - Reversal nếu do thuốc (Flumazenil, Naloxone)
            - CT sọ não nếu nghi biến chứng thần kinh
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Activity": activity,
            "Respiration": respiration,
            "Circulation": circulation,
            "Consciousness": consciousness,
            "SpO2": color
        }
        
        results_dict = {
            "Điểm Aldrete": f"{result['total_score']}/10",
            "Tình trạng": result['status'],
            "Khuyến nghị": result['recommendation']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="aldrete",
            calculator_name="Aldrete Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="aldrete",
            calculator_name="Aldrete Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="aldrete",
            calculator_name="Aldrete Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="aldrete", show_actions=True)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Aldrete Score")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

