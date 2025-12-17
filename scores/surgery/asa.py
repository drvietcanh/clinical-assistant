"""
ASA Physical Status Classification
Phân loại nguy cơ phẫu thuật của Hội Gây mê Hoa Kỳ
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def get_asa_classification():
    """Get ASA physical status classification criteria"""
    return {
        "ASA I": {
            "status": "Bệnh nhân khỏe mạnh hoàn toàn",
            "description": "Không có bệnh lý toàn thân. Không hút thuốc. Không hoặc uống rượu tối thiểu.",
            "examples": [
                "Người khỏe mạnh, tập thể dục đều đặn",
                "Không có bệnh mạn tính",
                "BMI < 30",
                "Không thuốc men thường xuyên"
            ],
            "color": "🟢",
            "mortality": "< 0.1%",
            "risk": "Nguy cơ thấp nhất"
        },
        "ASA II": {
            "status": "Bệnh lý toàn thân nhẹ",
            "description": "Bệnh lý toàn thân nhẹ, không hạn chế hoạt động. Kiểm soát tốt.",
            "examples": [
                "Hút thuốc hiện tại (không COPD)",
                "Uống rượu nhiều thường xuyên",
                "Thai kỳ",
                "BMI 30-40",
                "DM/THA kiểm soát tốt",
                "Bệnh phổi nhẹ (asthma, COPD nhẹ)",
                "Tuổi rất trẻ hoặc rất cao"
            ],
            "color": "🟡",
            "mortality": "0.1-0.2%",
            "risk": "Nguy cơ thấp"
        },
        "ASA III": {
            "status": "Bệnh lý toàn thân nặng",
            "description": "Bệnh lý toàn thân nặng. Hạn chế hoạt động đáng kể nhưng không mất khả năng hoạt động.",
            "examples": [
                "DM hoặc THA kiểm soát kém",
                "COPD trung bình-nặng",
                "BMI ≥ 40",
                "Suy thận mạn",
                "Suy tim CHF (NYHA II-III)",
                "Nhồi máu cơ tim > 3 tháng trước",
                "Đột quỵ > 3 tháng trước, không di chứng",
                "Bệnh gan mạn",
                "Lọc máu thường xuyên",
                "Rối loạn đông máu vừa"
            ],
            "color": "🟠",
            "mortality": "1.8-5.4%",
            "risk": "Nguy cơ trung bình-cao"
        },
        "ASA IV": {
            "status": "Bệnh lý toàn thân nặng đe dọa tính mạng",
            "description": "Bệnh lý toàn thân nặng, đe dọa tính mạng thường xuyên. Không thể tự chăm sóc.",
            "examples": [
                "Nhồi máu cơ tim < 3 tháng",
                "Đột quỵ < 3 tháng",
                "TIA < 3 tháng",
                "Suy tim tiến triển (NYHA IV)",
                "Sepsis",
                "DIC",
                "ARDS",
                "Suy thận cấp",
                "Suy gan cấp",
                "Không phẫu thuật sẽ tử vong"
            ],
            "color": "🔴",
            "mortality": "7.8-25.9%",
            "risk": "Nguy cơ rất cao"
        },
        "ASA V": {
            "status": "Hấp hối",
            "description": "Bệnh nhân hấp hối, không mong đợi sống sót mà không phẫu thuật. Phẫu thuật là nỗ lực cuối cùng cứu sống.",
            "examples": [
                "Vỡ phình động mạch chủ bụng",
                "Chấn thương đa cơ quan nặng",
                "Xuất huyết nội sọ với mass effect",
                "Tắc ruột hoại tử với septic shock",
                "Suy đa cơ quan"
            ],
            "color": "🔴",
            "mortality": "> 50%",
            "risk": "Nguy cơ cực cao"
        },
        "ASA VI": {
            "status": "Tử vong não - Hiến tặng cơ quan",
            "description": "Bệnh nhân tử vong não đang được hiến tặng cơ quan.",
            "examples": [
                "Tử vong não đã xác định",
                "Được duy trì để lấy cơ quan",
                "Phẫu thuật lấy cơ quan"
            ],
            "color": "⚫",
            "mortality": "N/A",
            "risk": "Chỉ áp dụng cho hiến tặng cơ quan"
        }
    }


def get_emergency_modifier_info():
    """Get information about emergency modifier (E)"""
    return {
        "definition": "Phẫu thuật cấp cứu - Không thể trì hoãn > 6 giờ",
        "notation": "Thêm chữ 'E' sau ASA (ví dụ: ASA III-E)",
        "impact": "Nguy cơ tử vong tăng 1.5-3 lần so với phẫu thuật chương trình",
        "examples": [
                "Vỡ tạng trong ổ bụng",
                "Tắc ruột có thiếu máu",
                "Chấn thương nặng cần phẫu thuật ngay",
                "Nhiễm trùng nặng cần dẫn lưu",
                "ACS cần can thiệp",
                "Đẻ mổ cấp cứu"
        ]
    }


def render():
    """Render the ASA Physical Status calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'asa':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🔪 ASA Physical Status Classification")
    st.markdown("""
    ### Phân loại Nguy cơ Phẫu Thuật
    
    **ASA Physical Status (American Society of Anesthesiologists):**
    - Hệ thống phân loại được sử dụng toàn cầu
    - Đánh giá tình trạng sức khỏe trước phẫu thuật/gây mê
    - Từ ASA I (khỏe mạnh) đến ASA VI (hiến tặng cơ quan)
    
    **Ý nghĩa lâm sàng:**
    - **Dự đoán nguy cơ:** Tử vong và biến chứng phẫu thuật
    - **Lập kế hoạch:** Chuẩn bị, giám sát, chăm sóc sau mổ
    - **Giao tiếp:** Với bệnh nhân, gia đình, đồng nghiệp
    - **Nghiên cứu:** Phân tầng nguy cơ trong trials
    
    **Lưu ý quan trọng:**
    - ASA không dự đoán nguy cơ phẫu thuật cụ thể
    - Phụ thuộc vào loại phẫu thuật (nhỏ/lớn)
    - Phụ thuộc vào kỹ thuật gây mê
    - Phẫu thuật cấp cứu (E) tăng nguy cơ đáng kể
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Selection section
        st.subheader("📋 Chọn ASA Physical Status")
        
        st.info("""
        **Hướng dẫn:** Chọn phân loại phù hợp nhất với tình trạng sức khỏe hiện tại của bệnh nhân
        """)
        
        asa_options = get_asa_classification()
        
        # Create selection with detailed descriptions
        selected_asa = st.radio(
            "**Chọn ASA Classification:**",
            options=list(asa_options.keys()),
            format_func=lambda x: f"{x}: {asa_options[x]['status']}",
            help="Chọn mức độ phù hợp nhất dựa trên tình trạng sức khỏe tổng thể"
        )
        
        # Emergency modifier
        is_emergency = st.checkbox(
            "**Phẫu thuật cấp cứu (Emergency) - Thêm 'E'**",
            help="Phẫu thuật không thể trì hoãn > 6 giờ"
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="asa",
            calculator_name="ASA Physical Status",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Display selected status details
    selected_info = asa_options[selected_asa]
    
    st.markdown("---")
    st.subheader("📊 Mô tả Chi tiết")
    
    # Main classification
    if selected_asa in ["ASA I", "ASA II"]:
        st.success(f"""
        **{selected_info['color']} {selected_asa}: {selected_info['status']}**
        
        **Mô tả:** {selected_info['description']}
        """)
    elif selected_asa == "ASA III":
        st.warning(f"""
        **{selected_info['color']} {selected_asa}: {selected_info['status']}**
        
        **Mô tả:** {selected_info['description']}
        """)
    else:
        st.error(f"""
        **{selected_info['color']} {selected_asa}: {selected_info['status']}**
        
        **Mô tả:** {selected_info['description']}
        """)
    
    # Examples
    st.markdown("**Ví dụ:**")
    for example in selected_info['examples']:
        st.markdown(f"- {example}")
    
    # Show all levels for comparison
    with st.expander("👀 Xem tất cả ASA Classifications"):
        for asa, info in asa_options.items():
            st.markdown(f"""
            **{info['color']} {asa}: {info['status']}**
            - {info['description']}
            - Tỷ lệ tử vong: {info['mortality']}
            """)
            st.markdown("---")
    
    # Emergency modifier details
    if is_emergency:
        st.markdown("---")
        emergency_info = get_emergency_modifier_info()
        
        st.warning(f"""
        ### ⚠️ Phẫu Thuật Cấp cứu (Emergency)
        
        **Phân loại:** {selected_asa}-E
        
        **Định nghĩa:** {emergency_info['definition']}
        
        **Ảnh hưởng:** {emergency_info['impact']}
        """)
    
    if st.button("📈 Phân tích Nguy cơ Chi tiết", type="primary", use_container_width=True):
        st.markdown("---")
        st.subheader("🎯 Đánh giá Nguy cơ & Khuyến nghị")
        
        # Display final classification
        final_classification = f"{selected_asa}{'-E' if is_emergency else ''}"
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "ASA Classification",
                final_classification,
                help="Phân loại cuối cùng"
            )
        
        with col2:
            mortality_base = selected_info['mortality']
            st.metric(
                "Tỷ lệ tử vong",
                mortality_base,
                delta="×1.5-3" if is_emergency else None,
                delta_color="inverse",
                help="Tỷ lệ tử vong chu phẫu"
            )
        
        with col3:
            st.metric(
                "Mức độ nguy cơ",
                selected_info['risk'],
                help="Đánh giá tổng thể"
            )
        
        st.markdown("---")
        
        # Risk assessment and recommendations
        st.subheader("💡 Khuyến nghị Lâm sàng")
        
        if selected_asa == "ASA I":
            st.success("""
            ### ✅ ASA I - Nguy cơ Thấp Nhất
            
            **Chuẩn bị trước mổ:**
            - Xét nghiệm tối thiểu (theo loại phẫu thuật)
            - Không cần tư vấn chuyên khoa đặc biệt
            - Nhịn đói tiêu chuẩn
            
            **Trong mổ:**
            - Tất cả kỹ thuật gây mê đều an toàn
            - Monitoring tiêu chuẩn
            
            **Sau mổ:**
            - Hồi tỉnh thông thường
            - Theo dõi tiêu chuẩn
            - Xuất viện sớm nếu phẫu thuật nhỏ
            """)
            
        elif selected_asa == "ASA II":
            st.info("""
            ### ✅ ASA II - Nguy cơ Thấp
            
            **Chuẩn bị trước mổ:**
            - Xét nghiệm cơ bản + đặc hiệu cho bệnh lý
            - Tối ưu hóa bệnh lý nền (DM, THA)
            - Xem xét tư vấn chuyên khoa nếu cần
            
            **Lưu ý đặc biệt:**
            - **Hút thuốc:** Ngừng ≥ 4-8 tuần trước mổ
            - **BMI 30-40:** Cân nhắc khó đặt nội khí quản
            - **DM/THA:** Kiểm soát tốt trước mổ
            
            **Trong mổ:**
            - Chọn kỹ thuật gây mê phù hợp
            - Monitoring cơ bản + đặc hiệu
            
            **Sau mổ:**
            - Theo dõi tiêu chuẩn
            - Kiểm soát đau tốt
            - Phục hồi sớm thường tốt
            """)
            
        elif selected_asa == "ASA III":
            st.warning("""
            ### ⚠️ ASA III - Nguy cơ Trung Bình-Cao
            
            **Chuẩn bị trước mổ:**
            - Xét nghiệm toàn diện
            - **BẮT BUỘC:** Tối ưu hóa bệnh lý nền
            - Tư vấn chuyên khoa (tim, thận, hô hấp)
            - Đánh giá chức năng cơ quan đích
            
            **Các bệnh lý cần chú ý:**
            - **COPD:** SpO2 baseline, xem xét ABG
            - **CKD:** eGFR, K+, tránh nephrotoxic drugs
            - **CHF:** Echo, BNP, tối ưu thuốc
            - **Suy gan:** PT/INR, albumin, NH3
            
            **Trong mổ:**
            - Monitoring xâm lấn (A-line, CVP) nếu cần
            - Dự phòng biến chứng
            - Cân nhắc ICU sau mổ
            
            **Sau mổ:**
            - Theo dõi sát (HDU/ICU nếu phẫu thuật lớn)
            - Kiểm soát đau multimodal
            - Theo dõi chức năng cơ quan
            - Hồi phục chậm hơn
            """)
            
        elif selected_asa == "ASA IV":
            st.error("""
            ### 🚨 ASA IV - Nguy cơ Rất Cao
            
            **Chuẩn bị trước mổ:**
            - Xét nghiệm toàn diện + chuyên sâu
            - **BẮT BUỘC:** Tư vấn đa chuyên khoa
            - Tối ưu hóa tối đa trong giới hạn thời gian
            - Thảo luận nguy cơ-lợi ích với gia đình
            
            **Cân nhắc:**
            - Phẫu thuật có thật sự cần thiết?
            - Có thể trì hoãn để tối ưu không?
            - Có phương án ít xâm lấn hơn không?
            - ICU bed có sẵn không?
            
            **Trong mổ:**
            - Monitoring xâm lấn (A-line, CVP/Swan-Ganz)
            - Đội ngũ gây mê có kinh nghiệm
            - Chuẩn bị máu, thuốc vận mạch
            - Phẫu thuật viên có kinh nghiệm
            
            **Sau mổ:**
            - **BẮT BUỘC:** ICU
            - Monitoring liên tục
            - Hỗ trợ đa cơ quan
            - Tiên lượng thận trọng
            """)
            
        elif selected_asa == "ASA V":
            st.error("""
            ### 🚨 ASA V - Hấp Hối
            
            **Đây là phẫu thuật cứu sống cuối cùng:**
            - Nguy cơ tử vong > 50%
            - Không phẫu thuật → Tử vong chắc chắn
            - Phẫu thuật → Cơ hội sống sót nhỏ
            
            **Chuẩn bị:**
            - Resuscitation tích cực
            - Mobilize toàn bộ resources
            - Thông báo gia đình về tiên lượng
            - Damage control surgery
            
            **Trong mổ:**
            - Đội ngũ có kinh nghiệm cao nhất
            - Monitoring đầy đủ
            - Massive transfusion protocol
            - Damage control approach
            
            **Sau mổ:**
            - ICU với hỗ trợ tối đa
            - Tiên lượng rất xấu
            - Thảo luận với gia đình
            """)
            
        else:  # ASA VI
            st.info("""
            ### ⚫ ASA VI - Hiến Tặng Cơ quan
            
            **Áp dụng:**
            - Bệnh nhân tử vong não
            - Phẫu thuật lấy cơ quan để hiến tặng
            
            **Đặc điểm:**
            - Không áp dụng các tiêu chí ASA thông thường
            - Mục tiêu: Bảo tồn cơ quan tốt nhất
            - Gây mê để phẫu thuật lấy cơ quan
            """)
        
        # Emergency modifier impact
        if is_emergency:
            st.markdown("---")
            st.error("""
            ### ⚠️ Tác Động Của Phẫu Thuật Cấp cứu
            
            **Nguy cơ tăng:**
            - Tử vong tăng 1.5-3 lần
            - Biến chứng tăng 2-4 lần
            - Thời gian nằm viện kéo dài
            
            **Lý do:**
            - Không thời gian tối ưu hóa
            - Bệnh nhân chưa nhịn đói → Nguy cơ hít
            - Tình trạng huyết động không ổn định
            - Stress sinh lý cao
            - Thường phẫu thuật ban đêm (mệt mỏi)
            
            **Giảm thiểu nguy cơ:**
            - Resuscitation tối ưu trước mổ
            - Đội ngũ có kinh nghiệm
            - Monitoring đầy đủ
            - Kỹ thuật rapid sequence intubation (RSI)
            - Chuẩn bị biến chứng
            """)
        
        # Prepare data for history and share
        final_classification = f"{selected_asa}{'-E' if is_emergency else ''}"
        selected_info = asa_options[selected_asa]
        
        inputs_dict = {
            "ASA Classification": selected_asa,
            "Emergency": is_emergency
        }
        
        results_dict = {
            "Phân loại cuối cùng": final_classification,
            "Tỷ lệ tử vong": selected_info['mortality'],
            "Mức độ nguy cơ": selected_info['risk'],
            "Tình trạng": selected_info['status']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="ASA Physical Status",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="ASA Physical Status"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="asa",
            calculator_name="ASA Physical Status",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="asa",
            calculator_name="ASA Physical Status",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="asa", show_actions=True)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("📖 Lịch Sử & Phát Triển ASA"):
        st.markdown("""
        ### Lịch sử ASA Physical Status:
        
        **1941:** Đề xuất lần đầu bởi ASA
        - 5 phân loại (I-V)
        - Mục đích: Thống kê, nghiên cứu
        
        **1963:** Thêm ASA VI (hiến tặng cơ quan)
        
        **2014:** Cập nhật ví dụ và làm rõ tiêu chí
        - BMI cutoffs
        - Functional status
        - Controlled vs uncontrolled disease
        
        **Hiện tại:** Được sử dụng toàn cầu
        - > 40 triệu phẫu thuật/năm ở Mỹ
        - Tiêu chuẩn quốc tế
        - Bắt buộc ghi trong hồ sơ
        
        **Giá trị:**
        - Dự đoán tử vong chu phẫu
        - Phân tầng nguy cơ
        - Giao tiếp giữa các chuyên khoa
        - Audit và quality improvement
        """)
    
    with st.expander("🎯 Cách Xác Định ASA Chính Xác"):
        st.markdown("""
        ### Nguyên tắc chung:
        
        **1. Đánh giá tổng thể:**
        - Xem xét TẤT CẢ bệnh lý toàn thân
        - Bệnh nặng nhất quyết định ASA
        - Functional status rất quan trọng
        
        **2. Controlled vs Uncontrolled:**
        - **Controlled = ASA II**
          + DM: HbA1c < 8%, không biến chứng
          + THA: BP < 140/90 với thuốc
          + Asthma: Triệu chứng ít, không cấp cứu
        
        - **Uncontrolled = ASA III**
          + DM: HbA1c > 8%, có biến chứng
          + THA: BP > 140/90 dù dùng thuốc
          + Asthma: Triệu chứng thường xuyên
        
        **3. Functional status:**
        - **ASA II:** Tự chăm sóc hoàn toàn, đi bộ > 1 block
        - **ASA III:** Hạn chế hoạt động, METs < 4
        - **ASA IV:** Không tự chăm sóc, bed/chair bound
        
        **4. Timeline của bệnh cấp:**
        - **< 3 tháng:** ASA IV (MI, CVA, TIA)
        - **> 3 tháng, không di chứng:** ASA III
        - **> 3 tháng, có di chứng:** ASA III-IV
        
        **5. BMI:**
        - 30-40: ASA II
        - ≥ 40: ASA III
        
        **6. Hút thuốc:**
        - Hiện tại, không COPD: ASA II
        - COPD nhẹ: ASA II
        - COPD trung bình-nặng: ASA III
        """)
    
    with st.expander("📊 ASA vs Nguy cơ tử vong"):
        st.markdown("""
        ### Tỷ lệ tử vong theo ASA:
        
        **Dữ liệu từ > 1 triệu phẫu thuật:**
        
        | ASA | Tử vong 48h (%) | Tử vong 7 ngày (%) | Tử vong 30 ngày (%) |
        |-----|----------------|-------------------|-------------------|
        | I | 0.03 | 0.06 | 0.1 |
        | II | 0.13 | 0.24 | 0.4 |
        | III | 1.2 | 2.1 | 3.5 |
        | IV | 7.8 | 12.3 | 18.3 |
        | V | 26.4 | 39.1 | 51.2 |
        
        **Lưu ý:**
        - Tỷ lệ thay đổi theo loại phẫu thuật
        - Phẫu thuật cấp cứu (E): ×2-3
        - Phẫu thuật tim: Tỷ lệ cao hơn
        - Laparoscopy: Tỷ lệ thấp hơn
        
        **Các yếu tố ảnh hưởng:**
        - Loại phẫu thuật (nhỏ/lớn)
        - Kỹ thuật (mở/laparoscopy)
        - Kinh nghiệm phẫu thuật viên
        - Kinh nghiệm gây mê
        - Cơ sở vật chất (ICU, thiết bị)
        - Tuổi bệnh nhân
        """)
    
    with st.expander("⚠️ Giới Hạn Của ASA"):
        st.markdown("""
        ### ASA không phải là công cụ hoàn hảo:
        
        **Hạn chế:**
        
        **1. Tính chủ quan cao:**
        - Khác biệt giữa các bác sĩ gây mê
        - Inter-rater reliability vừa phải (κ = 0.5-0.6)
        - Cùng bệnh nhân có thể được cho ASA khác nhau
        
        **2. Không đặc hiệu cho phẫu thuật:**
        - ASA III + phẫu thuật nhỏ: Nguy cơ thấp
        - ASA II + phẫu thuật lớn: Nguy cơ cao hơn
        - Không tính loại phẫu thuật vào
        
        **3. Không tính yếu tố khác:**
        - Tuổi (trẻ em, người cao tuổi)
        - Dinh dưỡng
        - Frailty
        - Social support
        
        **4. Vùng xám:**
        - Nhiều bệnh nhân nằm giữa ASA II/III
        - Khó phân loại khi có nhiều bệnh lý nhẹ
        
        **Công cụ bổ sung tốt hơn:**
        - **RCRI** (Revised Cardiac Risk Index): Tim mạch
        - **ACS NSQIP Calculator:** Đa yếu tố
        - **P-POSSUM:** Phẫu thuật tổng quát
        - **Frailty scores:** Người cao tuổi
        """)
    
    with st.expander("🔧 ASA trong Thực Hành"):
        st.markdown("""
        ### Ứng dụng thực tế:
        
        **1. Tư vấn trước mổ:**
        ```
        Bác sĩ: "Anh được xếp ASA III do THA và COPD không 
                kiểm soát tốt. Điều này có nghĩa nguy cơ phẫu 
                thuật cao hơn bình thường, khoảng 3-5% tử vong 
                trong 30 ngày. Chúng tôi sẽ theo dõi sát trong 
                và sau mổ."
        ```
        
        **2. Lập kế hoạch:**
        - ASA I-II + phẫu thuật nhỏ → Outpatient, local
        - ASA III + phẫu thuật trung bình → Overnight, Ward
        - ASA III-IV + phẫu thuật lớn → ICU booking
        - ASA IV-V → ICU mandatory, family meeting
        
        **3. Xét nghiệm:**
        - ASA I: Tối thiểu (nữ: β-hCG)
        - ASA II: Cơ bản (CBC, lytes, glucose)
        - ASA III: Toàn diện (+ organ-specific)
        - ASA IV: Chuyên sâu (+ ABG, lactate, echo)
        
        **4. Monitoring:**
        - ASA I-II: Tiêu chuẩn (ECG, SpO2, BP)
        - ASA III: + A-line nếu phẫu thuật lớn
        - ASA IV: A-line + CVP/cardiac output
        
        **5. Gây mê:**
        - ASA I-II: Resident độc lập
        - ASA III: Attending supervision
        - ASA IV-V: Attending trực tiếp
        
        **6. Hồi tỉnh:**
        - ASA I-II: PACU standard
        - ASA III: Extended PACU hoặc step-down
        - ASA IV-V: ICU
        """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("ASA Physical Status")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.caption("""
        **Tài liệu tham khảo:**
        - ASA Physical Status Classification System. Updated October 2014
        - Wolters U, et al. ASA classification and perioperative variables. Br J Anaesth. 1996
        - Daabiss M. American Society of Anesthesiologists physical status classification. Indian J Anaesth. 2011
        - Sankar A, et al. Reliability of the ASA physical status scale. Anaesthesia. 2014
        """)


if __name__ == "__main__":
    render()

