"""
NIHSS - NIH Stroke Scale
Đánh giá mức độ nặng của đột quỵ
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
    """NIHSS Calculator"""
    st.subheader("🧠 NIHSS - NIH Stroke Scale")
    st.caption("Thang điểm Đánh giá Mức Độ Nặng Đột Quỵ")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'nihss':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **NIHSS** là thang điểm chuẩn vàng đánh giá mức độ nặng của đột quỵ não.
    
    - Được sử dụng để quyết định điều trị (thrombolysis, thrombectomy)
    - Theo dõi diễn biến lâm sàng
    - Tiên lượng kết cục
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="nihss",
            calculator_name="NIHSS",
            category="Thần Kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    with col1:
        st.markdown("### 📋 Đánh giá 11 Hạng mục")
        
        # 1a. Level of Consciousness
        st.markdown("#### 1a. Mức độ ý thức")
        loc = st.radio(
            "Đánh giá:",
            [
                "0 - Tỉnh táo, phản ứng tốt",
                "1 - Không hoàn toàn tỉnh táo, nhưng kích thích nhẹ là tỉnh",
                "2 - Phải kích thích lặp lại hoặc kích thích đau mới tỉnh",
                "3 - Hôn mê, không phản ứng hoặc chỉ phản xạ"
            ],
            key="loc"
        )
        loc_score = int(loc[0])
        
        # 1b. LOC Questions
        st.markdown("#### 1b. Câu hỏi định hướng")
        st.caption("Hỏi: Tháng này là tháng mấy? Bao nhiêu tuổi?")
        loc_questions = st.radio(
            "Trả lời đúng:",
            [
                "0 - Cả 2 câu đúng",
                "1 - 1 câu đúng",
                "2 - Cả 2 câu sai hoặc không trả lời được"
            ],
            key="loc_q"
        )
        loc_q_score = int(loc_questions[0])
        
        # 1c. LOC Commands
        st.markdown("#### 1c. Làm theo lệnh")
        st.caption("Yêu cầu: Mở/nhắm mắt, nắm/mở bàn tay")
        loc_commands = st.radio(
            "Thực hiện đúng:",
            [
                "0 - Cả 2 động tác đúng",
                "1 - 1 động tác đúng",
                "2 - Cả 2 động tác sai"
            ],
            key="loc_c"
        )
        loc_c_score = int(loc_commands[0])
        
        st.markdown("---")
        
        # 2. Best Gaze
        st.markdown("#### 2. Vận nhãn (Eye Movement)")
        gaze = st.radio(
            "Nhìn theo ngón tay ngang:",
            [
                "0 - Bình thường",
                "1 - Liệt một phần (bất thường 1 hoặc cả 2 mắt)",
                "2 - Lệch cưỡng bức (không chủ động được)"
            ],
            key="gaze"
        )
        gaze_score = int(gaze[0])
        
        # 3. Visual Fields
        st.markdown("#### 3. Thị trường")
        visual = st.radio(
            "Kiểm tra bằng cách đếm ngón tay 4 góc:",
            [
                "0 - Không mất thị trường",
                "1 - Mất thị trường từng phần (quadrantanopia)",
                "2 - Mất hoàn toàn nửa thị trường (hemianopia)",
                "3 - Mù 2 bên (bilateral hemianopia hoặc mù)"
            ],
            key="visual"
        )
        visual_score = int(visual[0])
        
        # 4. Facial Palsy
        st.markdown("#### 4. Liệt mặt")
        st.caption("Yêu cầu: Cười, nhăn mặt")
        facial = st.radio(
            "Đánh giá:",
            [
                "0 - Bình thường, đối xứng",
                "1 - Liệt nhẹ (nếp mũi má mất, miệng méo nhẹ)",
                "2 - Liệt rõ (liệt hoàn toàn phần dưới mặt)",
                "3 - Liệt hoàn toàn một hoặc cả 2 bên mặt"
            ],
            key="facial"
        )
        facial_score = int(facial[0])
        
        st.markdown("---")
        
        # 5. Motor Arm (Left)
        st.markdown("#### 5a. Vận động Tay TRÁI")
        st.caption("Giơ tay lên 90° (ngồi) hoặc 45° (nằm), giữ 10 giây")
        arm_left = st.radio(
            "Tay trái:",
            [
                "0 - Giữ được 10 giây, không sa",
                "1 - Sa xuống trước 10 giây, nhưng không chạm giường",
                "2 - Có cố gắng chống trọng lực, nhưng sa xuống giường",
                "3 - Không chống được trọng lực, rơi ngay",
                "4 - Không cử động"
            ],
            key="arm_l"
        )
        arm_l_score = int(arm_left[0])
        
        # 5. Motor Arm (Right)
        st.markdown("#### 5b. Vận động Tay PHẢI")
        arm_right = st.radio(
            "Tay phải:",
            [
                "0 - Giữ được 10 giây, không sa",
                "1 - Sa xuống trước 10 giây, nhưng không chạm giường",
                "2 - Có cố gắng chống trọng lực, nhưng sa xuống giường",
                "3 - Không chống được trọng lực, rơi ngay",
                "4 - Không cử động"
            ],
            key="arm_r"
        )
        arm_r_score = int(arm_right[0])
        
        # 6. Motor Leg (Left)
        st.markdown("#### 6a. Vận động Chân TRÁI")
        st.caption("Nâng chân lên 30°, giữ 5 giây")
        leg_left = st.radio(
            "Chân trái:",
            [
                "0 - Giữ được 5 giây, không sa",
                "1 - Sa xuống trước 5 giây, nhưng không chạm giường",
                "2 - Có cố gắng chống trọng lực, nhưng sa xuống giường",
                "3 - Không chống được trọng lực, rơi ngay",
                "4 - Không cử động"
            ],
            key="leg_l"
        )
        leg_l_score = int(leg_left[0])
        
        # 6. Motor Leg (Right)
        st.markdown("#### 6b. Vận động Chân PHẢI")
        leg_right = st.radio(
            "Chân phải:",
            [
                "0 - Giữ được 5 giây, không sa",
                "1 - Sa xuống trước 5 giây, nhưng không chạm giường",
                "2 - Có cố gắng chống trọng lực, nhưng sa xuống giường",
                "3 - Không chống được trọng lực, rơi ngay",
                "4 - Không cử động"
            ],
            key="leg_r"
        )
        leg_r_score = int(leg_right[0])
        
        st.markdown("---")
        
        # 7. Limb Ataxia
        st.markdown("#### 7. Mất điều hòa chi (Ataxia)")
        st.caption("Test: Ngón tay chạm mũi, gót chân chạm đầu gối")
        ataxia = st.radio(
            "Đánh giá:",
            [
                "0 - Không có",
                "1 - Có ở 1 chi",
                "2 - Có ở 2 chi hoặc nhiều hơn"
            ],
            key="ataxia"
        )
        ataxia_score = int(ataxia[0])
        
        # 8. Sensory
        st.markdown("#### 8. Cảm giác")
        st.caption("Test kim châm nhẹ, so sánh 2 bên")
        sensory = st.radio(
            "Đánh giá:",
            [
                "0 - Bình thường, không giảm",
                "1 - Giảm nhẹ đến trung bình",
                "2 - Giảm nặng hoặc mất hoàn toàn"
            ],
            key="sensory"
        )
        sensory_score = int(sensory[0])
        
        # 9. Best Language (Aphasia)
        st.markdown("#### 9. Ngôn ngữ (Aphasia)")
        st.caption("Mô tả tranh, đọc câu, đặt tên vật")
        language = st.radio(
            "Đánh giá:",
            [
                "0 - Bình thường, không aphasia",
                "1 - Aphasia nhẹ đến trung bình (khó hiểu một phần)",
                "2 - Aphasia nặng (giao tiếp rất khó)",
                "3 - Câm hoặc hoàn toàn không hiểu/không nói được"
            ],
            key="language"
        )
        language_score = int(language[0])
        
        # 10. Dysarthria
        st.markdown("#### 10. Khó phát âm (Dysarthria)")
        st.caption("Đọc danh sách từ: Mẹ, Bà, Cầu...")
        dysarthria = st.radio(
            "Đánh giá:",
            [
                "0 - Bình thường, phát âm rõ ràng",
                "1 - Khó phát âm nhẹ đến trung bình",
                "2 - Khó phát âm nặng, không hiểu được"
            ],
            key="dysarthria"
        )
        dysarthria_score = int(dysarthria[0])
        
        # 11. Extinction/Inattention (Neglect)
        st.markdown("#### 11. Bỏ qua/Không chú ý (Neglect)")
        st.caption("Test kích thích đồng thời 2 bên (xúc giác, thị giác)")
        neglect = st.radio(
            "Đánh giá:",
            [
                "0 - Không có",
                "1 - Bỏ qua 1 giác quan (xúc giác HOẶC thị giác)",
                "2 - Bỏ qua nhiều hơn 1 giác quan"
            ],
            key="neglect"
        )
        neglect_score = int(neglect[0])
        
        st.markdown("---")
        
        if st.button("🧮 Tính NIHSS Score", type="primary", use_container_width=True):
            # Calculate total
            total_score = (
                loc_score + loc_q_score + loc_c_score +
                gaze_score + visual_score + facial_score +
                arm_l_score + arm_r_score +
                leg_l_score + leg_r_score +
                ataxia_score + sensory_score +
                language_score + dysarthria_score + neglect_score
            )
            
            # Determine severity
            if total_score == 0:
                severity = "KHÔNG CÓ ĐỘT QUỴ"
                color = "success"
                thrombolysis = "Không"
            elif total_score <= 4:
                severity = "ĐỘT QUỴ NHẸ"
                color = "info"
                thrombolysis = "Cân nhắc (nếu triệu chứng disabling)"
            elif total_score <= 15:
                severity = "ĐỘT QUỴ TRUNG BÌNH"
                color = "warning"
                thrombolysis = "Có chỉ định (nếu trong thời gian vàng)"
            elif total_score <= 20:
                severity = "ĐỘT QUỴ TRUNG BÌNH - NẶNG"
                color = "warning"
                thrombolysis = "Có chỉ định cao"
            else:
                severity = "ĐỘT QUỴ NẶNG"
                color = "error"
                thrombolysis = "Có chỉ định cao + xem xét thrombectomy"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                if color == "success":
                    st.success(f"## NIHSS = {total_score}")
                    st.success(f"**{severity}**")
                elif color == "info":
                    st.info(f"## NIHSS = {total_score}")
                    st.info(f"**{severity}**")
                elif color == "warning":
                    st.warning(f"## NIHSS = {total_score}")
                    st.warning(f"**{severity}**")
                else:
                    st.error(f"## NIHSS = {total_score}")
                    st.error(f"**{severity}**")
            
            st.markdown("---")
            st.markdown("### 💡 Chi tiết điểm số")
            
            details = [
                f"1a. Ý thức: {loc_score}",
                f"1b. Câu hỏi: {loc_q_score}",
                f"1c. Làm theo lệnh: {loc_c_score}",
                f"2. Vận nhãn: {gaze_score}",
                f"3. Thị trường: {visual_score}",
                f"4. Liệt mặt: {facial_score}",
                f"5a. Tay trái: {arm_l_score}",
                f"5b. Tay phải: {arm_r_score}",
                f"6a. Chân trái: {leg_l_score}",
                f"6b. Chân phải: {leg_r_score}",
                f"7. Ataxia: {ataxia_score}",
                f"8. Cảm giác: {sensory_score}",
                f"9. Ngôn ngữ: {language_score}",
                f"10. Phát âm: {dysarthria_score}",
                f"11. Neglect: {neglect_score}",
            ]
            
            cols = st.columns(3)
            for idx, detail in enumerate(details):
                with cols[idx % 3]:
                    st.write(f"• {detail}")
            
            st.markdown(f"**→ Tổng điểm: {total_score}/42**")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo điều trị")
            
            if total_score == 0:
                st.success("""
                **NIHSS = 0 - Không có đột quỵ**
                
                - Xem xét chẩn đoán khác
                - Có thể là TIA (Transient Ischemic Attack)
                - Theo dõi, đánh giá nguy cơ đột quỵ
                """)
            elif total_score <= 4:
                st.info(f"""
                **NIHSS = {total_score} - Đột Quỵ Nhẹ**
                
                **Thrombolysis (rt-PA):**
                - {thrombolysis}
                - Cân nhắc nếu triệu chứng gây bất lực (disabling)
                - Cân nhắc nguy cơ/lợi ích
                
                **Thời gian vàng:**
                - IV rt-PA: Trong 4.5 giờ từ khởi phát
                - Càng sớm càng tốt!
                
                **Điều trị:**
                - Aspirin 300mg sau 24h (nếu có thrombolysis)
                - Hoặc ngay nếu không thrombolysis
                - Kiểm soát huyết áp
                - Tìm nguyên nhân (Echo, Doppler cảnh, ECG)
                """)
            elif total_score <= 15:
                st.warning(f"""
                **NIHSS = {total_score} - Đột Quỵ Trung Bình**
                
                **Thrombolysis:**
                - ✅ **{thrombolysis}**
                - Nếu trong **4.5 giờ** từ khởi phát
                - Không có chống chỉ định
                
                **Liều rt-PA:**
                - 0.9 mg/kg (max 90mg)
                - 10% IV bolus trong 1 phút
                - 90% IV infusion trong 60 phút
                
                **Thrombectomy:**
                - Xem xét nếu tắc mạch lớn (LVO)
                - Trong 6 giờ (có thể kéo dài đến 24h nếu có imaging phù hợp)
                
                **Chăm sóc:**
                - Stroke unit
                - Monitoring BP, glucose, O2
                - Phòng biến chứng
                """)
            elif total_score <= 20:
                st.warning(f"""
                **NIHSS = {total_score} - Đột Quỵ Trung Bình - Nặng**
                
                **Thrombolysis:**
                - ✅ **{thrombolysis}**
                - URGENT - Trong 4.5 giờ
                
                **Thrombectomy:**
                - ✅ **Chỉ định cao** nếu tắc mạch lớn
                - CTA/MRA để xác định
                - Trong 6-24 giờ tùy imaging
                
                **Chăm sóc ICU:**
                - Monitoring sát
                - Quản lý ICP nếu có phù não
                - Phòng biến chứng
                """)
            else:
                st.error(f"""
                **NIHSS = {total_score} - Đột Quỵ NẶNG** 🚨
                
                **Điều trị URGENT:**
                
                **1. Thrombolysis:**
                - ✅ Chỉ định cao (nếu trong 4.5h)
                - Đánh giá nguy cơ chảy máu kỹ
                
                **2. Thrombectomy:**
                - ✅ **Chỉ định cao** nếu LVO (Large Vessel Occlusion)
                - Transfer to Stroke Center ngay nếu không có DSA
                - Time is brain!
                
                **3. ICU Management:**
                - Monitoring sát (BP, ICP, glucose)
                - Intubation nếu GCS ≤8 hoặc không bảo vệ được đường thở
                - Quản lý phù não (Mannitol, Hypertonic saline)
                - Xem xét decompressive craniectomy nếu MCA lớn
                
                **4. Biến chứng:**
                - Chảy máu chuyển dạng (5-10%)
                - Phù não (24-48h sau)
                - Suy hô hấp
                - Aspiration pneumonia
                
                **Tiên lượng:** Xấu, tỷ lệ tử vong và tàn phế cao
                """)
            
            st.markdown("---")
            st.markdown("### 📊 Diễn giải & Tiên lượng")
            
            st.info(f"""
            **NIHSS = {total_score} - {severity}**
            
            **Phân tầng mức độ:**
            - 0: Không triệu chứng
            - 1-4: Đột quỵ nhẹ
            - 5-15: Đột quỵ trung bình
            - 16-20: Đột quỵ trung bình - nặng
            - 21-42: Đột quỵ nặng
            
            **Giá trị tiên lượng:**
            - NIHSS ≤10: 60-70% hồi phục tốt (mRS 0-2)
            - NIHSS >10: Chỉ 15-30% hồi phục tốt
            - NIHSS >20: Tỷ lệ tử vong cao (20-40%)
            
            **Cải thiện điểm:**
            - Giảm 4-8 điểm: Cải thiện lâm sàng có ý nghĩa
            - Giảm ≥10 điểm: Cải thiện xuất sắc
            
            **Chỉ định Thrombolysis:**
            - Thường: NIHSS 5-25
            - NIHSS <5: Cân nhắc nếu disabling
            - NIHSS >25: Cân nhắc (nguy cơ chảy máu cao hơn)
            """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown(f"""
                **NIHSS - NIH Stroke Scale**
                
                **Kết quả của bạn:** {total_score}/42 - {severity}
                
                **Cấu trúc thang điểm:**
                - 11 hạng mục
                - Tổng điểm: 0-42
                - Điểm càng cao, đột quỵ càng nặng
                
                **Ưu điểm:**
                - Thang điểm chuẩn vàng toàn cầu
                - Validated rộng rãi
                - Dễ thực hiện (5-10 phút)
                - Tương quan tốt với kết cục
                - Quyết định thrombolysis/thrombectomy
                
                **Hạn chế:**
                - Cần training để đánh giá chính xác
                - Ít nhạy với posterior circulation stroke
                - Không đánh giá chi tiết aphasia
                
                **Thời gian vàng điều trị:**
                - **IV rt-PA:** 0-4.5 giờ (càng sớm càng tốt!)
                - **Thrombectomy:** 0-6 giờ (có thể đến 24h với imaging phù hợp)
                - **"Time is Brain":** Mỗi phút mất đi 1.9 triệu neuron!
                
                **Chống chỉ định Thrombolysis (một số):**
                - Thời gian >4.5h (hoặc không rõ thời gian khởi phát)
                - BP >185/110 mmHg (không kiểm soát được)
                - Glucose <50 hoặc >400 mg/dL
                - INR >1.7, đang dùng NOAC <48h
                - Tiểu cầu <100,000
                - Phẫu thuật lớn <14 ngày
                - Đột quỵ nặng hoặc chảy máu não <3 tháng
                - Chảy máu tiêu hóa/tiết niệu <21 ngày
                
                """)
            
            # Prepare inputs and results for export/history
            inputs_dict = {
                "1a. LOC": loc,
                "1b. LOC Questions": loc_questions,
                "1c. LOC Commands": loc_commands,
                "2. Best Gaze": gaze,
                "3. Visual Fields": visual,
                "4. Facial Palsy": facial,
                "5a. Motor Arm Left": motor_arm_l,
                "5b. Motor Arm Right": motor_arm_r,
                "6a. Motor Leg Left": motor_leg_l,
                "6b. Motor Leg Right": motor_leg_r,
                "7. Limb Ataxia": ataxia,
                "8. Sensory": sensory,
                "9. Language": language,
                "10. Dysarthria": dysarthria,
                "11. Extinction": extinction
            }
            
            results_dict = {
                "NIHSS Score": f"{total_score}/42",
                "Severity": severity,
                "Components": f"LOC:{loc_score}+{loc_q_score}+{loc_c_score} Gaze:{gaze_score} Visual:{visual_score} Facial:{facial_score} Motor:{motor_arm_l_score}+{motor_arm_r_score}+{motor_leg_l_score}+{motor_leg_r_score} Ataxia:{ataxia_score} Sensory:{sensory_score} Language:{language_score} Dysarthria:{dysarthria_score} Extinction:{extinction_score}"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"NIHSS = {total_score}/42",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="NIHSS",
                filename="nihss_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="nihss",
                calculator_name="NIHSS",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="nihss",
                calculator_name="NIHSS",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="nihss", show_actions=True)
            
            # References section
            references = get_references("NIHSS")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            
            st.markdown("---")
            st.warning("""
            ⚠️ **Lưu ý quan trọng:**
            
            - **TIME IS BRAIN!** - Đột quỵ là cấp cứu tuyệt đối
            - **Đánh giá NIHSS** phải chính xác, có training
            - **Imaging** (CT/MRI) để loại trừ chảy máu trước thrombolysis
            - **Chống chỉ định** thrombolysis phải được đánh giá kỹ
            - **Monitoring** sau thrombolysis: BP, neuro check q15min × 2h, q30min × 6h, q1h × 16h
            - **Biến chứng** chảy máu não: 5-10%, thường trong 24-36h đầu
            
            **ABC của đột quỵ:**
            - **A**irway - Bảo vệ đường thở
            - **B**lood pressure - Quản lý BP cẩn thận
            - **C**T scan - CT não ASAP để loại trừ chảy máu
            """)
    
    # Always show references at the bottom
    references = get_references("NIHSS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )


