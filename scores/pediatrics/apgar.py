"""
APGAR Score - Newborn Assessment
Đánh giá trẻ sơ sinh ngay sau sinh
"""

import streamlit as st
from config.theme import COLORS
from components.ui.results import render_result_box
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def calculate_apgar(appearance, pulse, grimace, activity, respiration):
    """
    Calculate APGAR score
    
    Args:
        appearance: Skin color score (0-2)
        pulse: Heart rate score (0-2)
        grimace: Reflex irritability score (0-2)
        activity: Muscle tone score (0-2)
        respiration: Breathing effort score (0-2)
    
    Returns:
        int: Total APGAR score (0-10)
    """
    return appearance + pulse + grimace + activity + respiration


def interpret_apgar(score, time_point):
    """
    Interpret APGAR score
    
    Args:
        score: APGAR score (0-10)
        time_point: "1 minute" or "5 minutes" or "10 minutes"
    
    Returns:
        dict: Interpretation results
    """
    if score >= 7:
        return {
            "status": "Bình thường",
            "color": COLORS["success"],
            "icon": "🟢",
            "condition": "Trẻ khỏe mạnh, thích nghi tốt",
            "action": "Chăm sóc thường quy. Quan sát.",
            "prognosis": "Tiên lượng tốt",
            "level": "normal"
        }
    elif score >= 4:
        return {
            "status": "Ức chế vừa",
            "color": COLORS["warning"],
            "icon": "🟡",
            "condition": "Trẻ cần hỗ trợ, theo dõi sát",
            "action": "Kích thích, hút đờm, O2, theo dõi sát. Xem xét thông khí áp lực dương nếu cần.",
            "prognosis": "Tiên lượng thận trọng, cần theo dõi",
            "level": "moderate"
        }
    else:
        return {
            "status": "Ức chế nặng",
            "color": COLORS["error"],
            "icon": "🔴",
            "condition": "Trẻ nguy kịch, cần hồi sức tích cực",
            "action": "HỒI SỨC NGAY: Thông khí áp lực dương, ép tim nếu cần, đánh giá nguyên nhân.",
            "prognosis": "Nguy cơ cao tổn thương não và tử vong",
            "level": "severe"
        }


def render():
    """Render the APGAR Score calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'apgar':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>👶 APGAR Score</h2>", unsafe_allow_html=True)
    st.markdown("""
    ### Đánh giá trẻ Sơ Sinh Ngay Sau Sinh
    
    **APGAR Score (Virginia Apgar, 1952):**
    - Thang điểm phổ biến nhất đánh giá trẻ sơ sinh
    - 5 thông số: Appearance, Pulse, Grimace, Activity, Respiration
    - Mỗi thông số 0-2 điểm → Tổng 0-10 điểm
    
    **Thời điểm đánh giá:**
    - **1 phút:** Đánh giá ban đầu, cần can thiệp ngay không?
    - **5 phút:** Đánh giá đáp ứng, tiên lượng
    - **10, 15, 20 phút:** Nếu điểm 5 phút < 7 (tiếp tục theo dõi)
    
    **Ý nghĩa lâm sàng:**
    - **Quyết định can thiệp:** Hồi sức, thông khí, ép tim
    - **Tiên lượng:** Điểm 5 phút quan trọng nhất
    - **Giao tiếp:** Với gia đình, ghi nhận hồ sơ
    
    **Lưu ý:**
    - KHÔNG dùng để quyết định BẮT ĐẦU hồi sức (bắt đầu ngay nếu cần)
    - Dùng để đánh giá ĐÁP ỨNG với hồi sức
    - Điểm thấp ở 1 phút không có giá trị tiên lượng dài hạn
    - Điểm 5 phút < 7 → Nguy cơ cao tổn thương thần kinh
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Time point selection
        st.subheader("⏱️ Chọn Thời Điểm Đánh giá")
        
        time_point = st.radio(
            "**Thời điểm:**",
            ["1 phút", "5 phút", "10 phút"],
            horizontal=True,
            help="Chọn thời điểm đánh giá sau sinh"
        )
        
        st.markdown("---")
        
        # APGAR components
        st.subheader("📋 Đánh giá Các Thành phần APGAR")
        
        # A - Appearance (Skin Color)
        st.markdown("### 🎨 A - Appearance (Màu sắc da)")
        appearance = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2],
            format_func=lambda x: [
                "0 - Tím/xanh toàn thân",
                "1 - Hồng, tay chân xanh (acrocyanosis)",
                "2 - Hồng toàn thân"
            ][x],
            key="appearance",
            help="Đánh giá màu sắc da và niêm mạc"
        )
        
        st.markdown("---")
        
        # P - Pulse (Nhịp tim)
        st.markdown("### 💓 P - Pulse (Nhịp tim)")
        pulse = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2],
            format_func=lambda x: [
                "0 - Không có",
                "1 - < 100 bpm (chậm)",
                "2 - ≥ 100 bpm (bình thường)"
            ][x],
            key="pulse",
            help="Đánh giá tần số tim"
        )
        
        st.markdown("---")
        
        # G - Grimace (Reflex Irritability)
        st.markdown("### 😣 G - Grimace (Phản xạ kích thích)")
        grimace = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2],
            format_func=lambda x: [
                "0 - Không đáp ứng",
                "1 - Nhăn mặt/cử động nhẹ khi kích thích",
                "2 - Ho/hắt hơi/khóc khi kích thích"
            ][x],
            key="grimace",
            help="Đánh giá phản xạ khi hút mũi/họng"
        )
        
        st.markdown("---")
        
        # A - Activity (Muscle Tone)
        st.markdown("### 💪 A - Activity (Trương lực cơ)")
        activity = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2],
            format_func=lambda x: [
                "0 - Mềm nhũn (floppy)",
                "1 - Gập chi một số, trương lực cơ giảm",
                "2 - Gập chi chủ động, vận động mạnh"
            ][x],
            key="activity",
            help="Đánh giá trương lực cơ và vận động"
        )
        
        st.markdown("---")
        
        # R - Respiration (Breathing Effort)
        st.markdown("### 🫁 R - Respiration (Hô hấp)")
        respiration = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2],
            format_func=lambda x: [
                "0 - Không thở",
                "1 - Thở chậm, không đều, khóc yếu",
                "2 - Thở tốt, khóc mạnh"
            ][x],
            key="respiration",
            help="Đánh giá nỗ lực hô hấp"
        )
        
        st.markdown("---")
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="apgar",
            calculator_name="APGAR Score",
            category="Nhi Khoa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Calculate button
    if st.button("📊 Tính Điểm APGAR", type="primary", use_container_width=True):
        # Calculate total score
        total_score = calculate_apgar(appearance, pulse, grimace, activity, respiration)
        
        # Get interpretation
        result = interpret_apgar(total_score, time_point)
        
        st.markdown("---")
        st.subheader("📈 Kết quả APGAR")
        
        # Display score
        render_result_box(
            title="Kết quả APGAR",
            value=f"{total_score}/10",
            subtitle=f"{time_point} - {result['status']}",
            color=result['color'],
            icon=result['icon'],
            size="large"
        )
        
        st.markdown("---")
        
        # Score breakdown
        st.subheader("📊 Chi tiết từng thành phần")
        
        components = [
            ("🎨 Appearance (Màu sắc)", appearance),
            ("💓 Pulse (Nhịp tim)", pulse),
            ("😣 Grimace (Phản xạ)", grimace),
            ("💪 Activity (Trương lực cơ)", activity),
            ("🫁 Respiration (Hô hấp)", respiration)
        ]
        
        for label, score in components:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(label)
            with col2:
                if score == 0:
                    st.write("0")
                elif score == 1:
                    st.write("1")
                else:
                    st.write("2")
        
        st.markdown("---")
        
        # Interpretation and action
        st.subheader("🎯 Đánh giá & Xử trí")
        
        if result['level'] == "normal":
            st.success(f"""
            ### ✅ {result['status']}
            
            **Tình trạng:** {result['condition']}
            
            **Xử trí:** {result['action']}
            
            **Tiên lượng:** {result['prognosis']}
            """)
            
            if time_point == "5 phút":
                st.info("""
                **Chăm sóc thường quy:**
                - Tiếp xúc da kề da với mẹ (skin-to-skin)
                - Khởi động bú sớm
                - Vitamin K, nhỏ mắt
                - Cân nặng, đo chiều dài, vòng đầu
                - Screening (TSH, G6PD, v.v.)
                """)
        
        elif result['level'] == "moderate":
            st.warning(f"""
            ### ⚠️ {result['status']}
            
            **Tình trạng:** {result['condition']}
            
            **Xử trí:** {result['action']}
            
            **Tiên lượng:** {result['prognosis']}
            """)
            
            st.warning("""
            **Can thiệp cần thiết:**
            - Kích thích (chà xát lưng, bàn chân)
            - Làm ấm
            - Hút đờm mũi họng (nếu cần)
            - Oxy qua mask nếu SpO2 < 90%
            - Thông khí áp lực dương (CPAP/PPV) nếu thở không hiệu quả
            - Theo dõi sát, đánh giá lại sau 30 giây
            - Đánh giá APGAR 5 phút, 10 phút
            """)
        
        else:  # severe
            st.error(f"""
            ### 🚨 {result['status']}
            
            **Tình trạng:** {result['condition']}
            
            **Xử trí:** {result['action']}
            
            **Tiên lượng:** {result['prognosis']}
            """)
            
            st.error("""
            ### 🚨 HỒI SỨC TRẺ SƠ SINH NGAY LẬP TỨC
            
            **Theo NRP (Neonatal Resuscitation Program) 2020:**
            
            **1. Initial Steps (30 giây đầu):**
            - Làm ấm, đặt tư thế
            - Hút mũi họng (nếu cần)
            - Làm khô, kích thích
            
            **2. Thông khí (nếu không thở hoặc thở kém):**
            - PPV (Positive Pressure Ventilation)
            - 40-60 nhịp/phút
            - FiO2 21% (không đủ → tăng dần)
            - Kiểm tra ngực nở, HR tăng
            
            **3. Ép tim (nếu HR < 60 bpm sau PPV):**
            - Tỷ lệ 3:1 (3 ép tim : 1 nhịp thở)
            - 90 ép tim + 30 nhịp thở = 120 events/phút
            - Độ sâu: 1/3 đường kính trước-sau ngực
            
            **4. Thuốc (nếu HR < 60 sau 30 giây ép tim + PPV):**
            - Epinephrine IV/IO: 0.01-0.03 mg/kg (1:10,000)
            - Dịch truyền nếu nghi hypovolemia
            
            **5. Đánh giá nguyên nhân:**
            - Tắc đường thở
            - Khí màng phổi
            - Bệnh tim bẩm sinh
            - Thiếu oxy trước sinh
            - Nhiễm trùng
            - Thoát vị hoành bẩm sinh
            
            **6. Xem xét:**
            - Đặt nội khí quản nếu PPV không hiệu quả
            - Chuyển NICU
            - Hạ thân nhiệt điều trị nếu ngạt nặng
            """)
        
        # Additional recommendations based on time point
        st.markdown("---")
        
        if time_point == "1 phút":
            st.info("""
            ### 📝 Lưu ý Điểm 1 Phút
            
            - Điểm 1 phút phản ánh tình trạng ngay sau sinh
            - **KHÔNG** có giá trị tiên lượng dài hạn
            - Dùng để quyết định can thiệp tức thì
            - BẮT BUỘC đánh giá lại ở 5 phút
            - Điểm thấp ở 1 phút thường do:
              + Thuốc gây mê/giảm đau của mẹ
              + Đẻ mổ
              + Nhau bong non
              + Sinh non
            """)
        
        elif time_point == "5 phút":
            if total_score < 7:
                st.warning("""
                ### ⚠️ Điểm 5 Phút < 7 - Quan Trọng!
                
                **Ý nghĩa:**
                - Có giá trị tiên lượng
                - Nguy cơ cao tổn thương não
                - Nguy cơ tử vong tăng
                - Cần đánh giá tiếp ở 10, 15, 20 phút
                
                **Xử trí:**
                - Tiếp tục hồi sức tích cực
                - Chuyển NICU
                - Xem xét hạ thân nhiệt điều trị (nếu ngạt nặng)
                - ABG, glucose, lactate
                - Theo dõi multi-organ dysfunction
                
                **Xem xét hạ thân nhiệt nếu:**
                - ≥ 36 tuần tuổi thai
                - APGAR 5 phút ≤ 5
                - Cần hồi sức kéo dài
                - pH < 7.0 hoặc BE < -16
                - Bắt đầu trong 6 giờ đầu
                """)
            else:
                st.success("""
                ### ✅ Điểm 5 Phút ≥ 7
                
                **Ý nghĩa:**
                - Tiên lượng tốt
                - Nguy cơ thấp tổn thương thần kinh dài hạn
                - Có thể chăm sóc thường quy (nếu điểm 7-10)
                
                **Tiếp theo:**
                - Chuyển về phòng mẹ (nếu điểm 8-10)
                - Theo dõi thêm (nếu điểm 7)
                - Tiếp xúc da kề da
                - Bú sớm
                """)
        
        else:  # 10 minutes
            if total_score < 7:
                st.error("""
                ### 🚨 Điểm 10 Phút < 7 - NGHIÊM TRỌNG
                
                **Ý nghĩa:**
                - Tiên lượng rất xấu
                - Nguy cơ rất cao:
                  + Tổn thương não (HIE - Hypoxic-Ischemic Encephalopathy)
                  + Bại não (Cerebral Palsy)
                  + Chậm phát triển thần kinh
                  + Tử vong
                
                **Xử trí:**
                - NICU level III
                - Hạ thân nhiệt điều trị (nếu đủ tiêu chuẩn)
                - Hỗ trợ multi-organ
                - EEG monitoring
                - MRI não (sau 3-7 ngày)
                - Tư vấn gia đình về tiên lượng
                
                **Theo dõi dài hạn:**
                - Phát triển thần kinh
                - Vật lý trị liệu/phục hồi chức năng
                - Can thiệp sớm nếu có chậm phát triển
                """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Thời điểm": time_point,
            "Appearance": appearance,
            "Pulse": pulse,
            "Grimace": grimace,
            "Activity": activity,
            "Respiration": respiration
        }
        
        results_dict = {
            "Điểm APGAR": f"{total_score}/10",
            "Mức độ": result['status'],
            "Tình trạng": result['condition'],
            "Xử trí": result['action'],
            "Tiên lượng": result['prognosis']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="APGAR Score",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="APGAR Score"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="apgar",
            calculator_name="APGAR Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="apgar",
            calculator_name="APGAR Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="apgar", show_actions=True)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("📖 Lịch Sử APGAR Score"):
        st.markdown("""
        ### Virginia Apgar, MD (1909-1974):
        
        **1952:** Đề xuất APGAR Score
        - Bác sĩ gây mê tại Columbia University
        - Mục đích: Đánh giá nhanh trẻ sơ sinh
        - 5 thông số dễ đánh giá
        
        **APGAR mnemonic:**
        - **A**ppearance (màu sắc)
        - **P**ulse (nhịp tim)
        - **G**rimace (phản xạ)
        - **A**ctivity (trương lực cơ)
        - **R**espiration (hô hấp)
        
        **Tác động:**
        - Giảm tử vong sơ sinh đáng kể
        - Tiêu chuẩn toàn cầu
        - Được dùng ở mọi đẻ (đủ tháng, non tháng)
        - Hơn 300 triệu trẻ được đánh giá
        
        **Vinh danh:**
        - Tem bưu chính Mỹ (1994)
        - National Women's Hall of Fame
        - "Mother of Neonatology"
        """)
    
    with st.expander("🎯 Cách đánh giá APGAR Chính Xác"):
        st.markdown("""
        ### Hướng dẫn chi tiết từng thông số:
        
        **1. Appearance (Màu sắc da):**
        - **0:** Xanh/tím toàn thân, cả thân và chi
        - **1:** Thân hồng, tay chân xanh (acrocyanosis - BÌNH THƯỜNG trong vài giờ đầu)
        - **2:** Hồng toàn thân, không vùng nào xanh
        - Lưu ý: Khó đánh giá ở trẻ da sẫm → Xem niêm mạc miệng, lòng bàn tay/chân
        
        **2. Pulse (Nhịp tim):**
        - **0:** Không có mạch (nghe tim, sờ cuống rốn)
        - **1:** < 100 bpm (chậm, cần can thiệp)
        - **2:** ≥ 100 bpm (bình thường)
        - Đánh giá: Nghe tim bằng stethoscope hoặc sờ động mạch rốn
        
        **3. Grimace (Phản xạ kích thích):**
        - **0:** Không đáp ứng khi hút mũi/họng
        - **1:** Nhăn mặt, cử động nhẹ
        - **2:** Ho, hắt hơi, hoặc khóc mạnh khi kích thích
        - Đánh giá: Khi hút mũi/họng bằng catheter
        
        **4. Activity (Trương lực cơ):**
        - **0:** Mềm nhũn (floppy/limp), không vận động
        - **1:** Gập chi một số, trương lực giảm
        - **2:** Gập chi tốt, vận động mạnh, chống lại khi duỗi chi
        - Đánh giá: Quan sát tư thế và cử động tự nhiên
        
        **5. Respiration (Hô hấp):**
        - **0:** Không thở (apnea)
        - **1:** Thở chậm, không đều, nông, khóc yếu
        - **2:** Thở tốt, đều, sâu, khóc mạnh
        - Đánh giá: Quan sát bụng nở, nghe phổi, tiếng khóc
        """)
    
    with st.expander("⚠️ Giới Hạn Của APGAR Score"):
        st.markdown("""
        ### APGAR không phải là công cụ hoàn hảo:
        
        **Hạn chế:**
        
        **1. Bị ảnh hưởng bởi nhiều yếu tố:**
        - Tuổi thai (trẻ sinh non thường điểm thấp hơn)
        - Thuốc gây mê/giảm đau của mẹ
        - Loại đẻ (mổ thường điểm thấp hơn đẻ thường)
        - Dị tật bẩm sinh
        - Nhiễm trùng
        
        **2. Tính chủ quan:**
        - Khác biệt giữa các người đánh giá
        - Đặc biệt ở trẻ da sẫm (màu sắc da)
        - Phản xạ kích thích phụ thuộc kỹ thuật hút
        
        **3. Không dùng để:**
        - Quyết định BẮT ĐẦU hồi sức (không đợi APGAR!)
        - Chẩn đoán ngạt (cần thêm pH, BE, lactate)
        - Dự đoán chắc chắn về dài hạn (nhiều yếu tố khác)
        
        **4. Điểm 1 phút:**
        - Không có giá trị tiên lượng
        - Nhiều trẻ điểm thấp ở 1 phút nhưng bình thường ở 5 phút
        - Chỉ dùng để đánh giá cần can thiệp ngay
        
        **5. Không phản ánh:**
        - Tổn thương não trước sinh
        - Bệnh tim bẩm sinh
        - Các vấn đề chuyển hóa
        
        **Cần kết hợp:**
        - Tiền sử thai kỳ
        - Đánh giá lâm sàng toàn diện
        - ABG (pH, BE)
        - Lactate
        - Neurological examination
        """)
    
    with st.expander("📊 APGAR vs Tiên lượng"):
        st.markdown("""
        ### Mối liên hệ giữa APGAR và kết cục:
        
        **Điểm 5 phút:**
        
        | APGAR 5' | Tử vong sơ sinh | Bại não | Phát triển bình thường |
        |----------|----------------|---------|----------------------|
        | 0-3 | 30-50% | 10-20% | 50-70% |
        | 4-6 | 5-10% | 2-5% | 85-90% |
        | 7-10 | < 1% | < 1% | > 99% |
        
        **Điểm 10 phút:**
        
        **APGAR 10' < 7:**
        - Nguy cơ Cerebral Palsy: 20-60%
        - Nguy cơ epilepsy: 15-30%
        - Nguy cơ chậm phát triển: 40-70%
        
        **APGAR 10' ≥ 7:**
        - Tiên lượng thần kinh thường tốt
        - Nguy cơ biến chứng dài hạn thấp
        
        **Lưu ý quan trọng:**
        - Đa số trẻ có APGAR thấp KHÔNG bị bại não
        - Đa số trẻ bại não có APGAR bình thường (nguyên nhân trước sinh)
        - APGAR chỉ là một trong nhiều yếu tố tiên lượng
        
        **Yếu tố khác ảnh hưởng tiên lượng:**
        - pH máu dây rốn (< 7.0 = xấu)
        - Base excess (< -12 = xấu)
        - Thời gian cần hồi sức
        - Encephalopathy neonatal
        - MRI não findings
        - EEG patterns
        """)
    
    with st.expander("🚨 Hồi sức Trẻ Sơ Sinh (NRP 2020)"):
        st.markdown("""
        ### Thuật toán NRP cập nhật:
        
        **"The Golden Minute":**
        - 60 giây đầu là QUAN TRỌNG nhất
        - Initial steps + PPV nếu cần
        - Đánh giá và quyết định nhanh
        
        **Quyết định can thiệp dựa trên:**
        1. **Thở:** Không thở hoặc thở kém?
        2. **Nhịp tim:** < 100 bpm?
        3. **Muscle tone:** Mềm nhũn?
        
        → **KHÔNG ĐỢI** APGAR để bắt đầu!
        
        **Trình tự can thiệp:**
        
        **Block 1 - Initial Steps (30s):**
        - Warm, position, stimulate
        - Suction if needed (mouth → nose)
        - Dry
        
        **Block 2 - Ventilation:**
        - If apnea or HR < 100 → PPV
        - Rate: 40-60/min
        - Start with room air (21% O2)
        - Check: Chest rise, HR↑
        
        **Block 3 - Chest Compressions:**
        - If HR < 60 after 30s adequate PPV
        - 3:1 ratio (3 compressions : 1 breath)
        - 120 events/minute
        
        **Block 4 - Medications:**
        - If HR < 60 after 30s CC + PPV
        - Epinephrine: 0.01-0.03 mg/kg IV/IO
        - Repeat every 3-5 min if needed
        
        **Target SpO2 (preductal, right hand):**
        - 1 min: 60-65%
        - 2 min: 65-70%
        - 3 min: 70-75%
        - 4 min: 75-80%
        - 5 min: 80-85%
        - 10 min: 85-95%
        
        **Khi nào DỪNG hồi sức:**
        - HR < 60 bpm sau 20 phút → Xem xét dừng
        - Thảo luận với gia đình
        - Theo hướng dẫn đạo đức y khoa địa phương
        """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("APGAR Score")
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
        - Apgar V. A proposal for a new method of evaluation of the newborn infant. Curr Res Anesth Analg. 1953
        - American Academy of Pediatrics. Neonatal Resuscitation Program (NRP) 8th Edition. 2020
        - Ehrenstein V. Association of Apgar scores with death and neurologic disability. Clin Epidemiol. 2009
        - Wyckoff MH, et al. Neonatal Life Support: 2020 International Consensus on CPR. Circulation. 2020
        """)


if __name__ == "__main__":
    render()

