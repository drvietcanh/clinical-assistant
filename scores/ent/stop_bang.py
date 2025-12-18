"""
STOP-BANG Score Calculator
Sàng lọc nguy cơ Obstructive Sleep Apnea (OSA)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def calculate_stop_bang(snoring, tired, observed, pressure, bmi, age, neck, gender):
    """
    Tính điểm STOP-BANG
    
    Parameters: Mỗi thành phần = 1 nếu có, 0 nếu không
    - snoring: Ngáy to
    - tired: Mệt mỏi ban ngày
    - observed: Người khác thấy ngừng thở
    - pressure: Tăng huyết áp
    - bmi: BMI > 35
    - age: Tuổi > 50
    - neck: Chu vi cổ > 40cm (nam) hoặc > 41cm (nữ ở Châu Á)
    - gender: Giới tính nam
    
    Returns:
    - dict với total_score, risk_level và interpretation
    """
    total = (snoring + tired + observed + pressure + 
             bmi + age + neck + gender)
    
    # Phân loại nguy cơ OSA
    if total <= 2:
        risk = "Thấp"
        osa_probability = "< 15%"
        action = "Nguy cơ OSA thấp, không cần đánh giá thêm trừ khi có triệu chứng rõ"
        color = "green"
    elif total <= 4:
        risk = "Trung bình"
        osa_probability = "15-30%"
        action = "Nguy cơ OSA trung bình, cân nhắc polysomnography"
        color = "orange"
    else:  # >= 5
        risk = "Cao"
        osa_probability = "> 30%"
        action = "Nguy cơ OSA cao, khuyến cáo làm polysomnography"
        color = "red"
    
    return {
        "total_score": total,
        "risk_level": risk,
        "osa_probability": osa_probability,
        "action": action,
        "color": color
    }


def render():
    """Render STOP-BANG calculator interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'stop_bang':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'STOP-BANG')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #6366F1;'>😴 STOP-BANG Score</h2>
    <p style='text-align: center;'><em>Sàng lọc nguy cơ Obstructive Sleep Apnea (OSA)</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về STOP-BANG
    with st.expander("ℹ️ Giới thiệu về STOP-BANG"):
        st.markdown("""
        **STOP-BANG Score** là công cụ sàng lọc đơn giản và nhanh chóng để đánh giá nguy cơ 
        Obstructive Sleep Apnea (OSA - ngưng thở khi ngủ do tắc nghẽn).
        
        **Mục đích:**
        - Sàng lọc nhanh OSA trong cộng đồng
        - Đánh giá nguy cơ trước phẫu thuật
        - Quyết định có cần làm polysomnography
        
        **Ưu điểm:**
        - Đơn giản, dễ nhớ (STOP-BANG)
        - Độ nhạy cao (> 90% với OSA trung bình-nặng)
        - Không cần thiết bị đặc biệt
        
        **Giới hạn:**
        - Độ đặc hiệu không cao
        - Không thay thế polysomnography để chẩn đoán xác định
        - Chủ yếu để sàng lọc, không phải chẩn đoán
        
        **Áp dụng:**
        - Đánh giá tiền phẫu
        - Sàng lọc trong cộng đồng
        - Bệnh nhân có triệu chứng nghi ngờ OSA
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Trả lời 8 câu hỏi STOP-BANG")
    
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
        <p style='margin: 0; font-size: 0.9em;'>
            ✅ Đánh dấu vào ô nếu <strong>CÓ</strong> đặc điểm đó<br>
            ⬜ Bỏ trống nếu <strong>KHÔNG</strong> có
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # STOP section
    st.markdown("### 🛑 STOP")
    
    col1, col2 = st.columns(2)
    
    with col1:
        snoring = st.checkbox(
            "**S**noring - Ngáy to",
            help="Ngáy đủ lớn để nghe qua cửa đóng hoặc người khác phải nhắc nhở"
        )
        
        tired = st.checkbox(
            "**T**ired - Mệt mỏi ban ngày",
            help="Thường xuyên cảm thấy mệt, buồn ngủ ban ngày hoặc ngủ gật"
        )
    
    with col2:
        observed = st.checkbox(
            "**O**bserved - Người khác thấy ngừng thở",
            help="Có ai đó chứng kiến bạn ngừng thở khi ngủ không?"
        )
        
        pressure = st.checkbox(
            "Blood **P**ressure - Tăng huyết áp",
            help="Đang điều trị tăng huyết áp hoặc có tiền sử THA"
        )
    
    st.markdown("---")
    
    # BANG section
    st.markdown("### 💥 BANG")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # BMI input
        st.markdown("**B**MI > 35 kg/m²")
        
        col_bmi1, col_bmi2 = st.columns(2)
        with col_bmi1:
            height = st.number_input(
                "Chiều cao (cm)",
                min_value=100.0,
                max_value=250.0,
                value=160.0,
                step=1.0,
                help="Nhập chiều cao"
            )
        
        with col_bmi2:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=300.0,
                value=50.0,
                step=0.1,
                help="Nhập cân nặng"
            )
        
        calculated_bmi = weight / ((height/100) ** 2)
        bmi_over_35 = 1 if calculated_bmi > 35 else 0
        
        if calculated_bmi > 35:
            st.success(f"✅ BMI = {calculated_bmi:.1f} (> 35)")
        else:
            st.info(f"BMI = {calculated_bmi:.1f}")
        
        age_over_50 = st.checkbox(
            "**A**ge > 50 tuổi",
            help="Tuổi lớn hơn 50"
        )
    
    with col2:
        # Neck circumference
        st.markdown("**N**eck - Chu vi cổ")
        
        neck_circ = st.number_input(
            "Chu vi cổ (cm)",
            min_value=20.0,
            max_value=60.0,
            value=38.0,
            step=0.5,
            help="Đo vòng cổ ở vị trí nổi nhất của sụn giáp"
        )
        
        gender_male = st.checkbox(
            "**G**ender - Giới tính Nam",
            help="Giới tính nam có nguy cơ OSA cao hơn"
        )
        
        # Neck criteria based on gender
        if gender_male:
            neck_large = 1 if neck_circ > 43 else 0
            if neck_large:
                st.success(f"✅ Chu vi cổ {neck_circ} cm (> 43 cm với nam)")
            else:
                st.info(f"Chu vi cổ {neck_circ} cm")
        else:
            neck_large = 1 if neck_circ > 41 else 0
            if neck_large:
                st.success(f"✅ Chu vi cổ {neck_circ} cm (> 41 cm với nữ)")
            else:
                st.info(f"Chu vi cổ {neck_circ} cm")
    
    st.markdown("---")
    
    # Convert checkboxes to binary
    snoring_val = 1 if snoring else 0
    tired_val = 1 if tired else 0
    observed_val = 1 if observed else 0
    pressure_val = 1 if pressure else 0
    age_val = 1 if age_over_50 else 0
    gender_val = 1 if gender_male else 0
    
    # Calculate button
    if st.button("🔬 Tính điểm STOP-BANG", type="primary", use_container_width=True):
        result = calculate_stop_bang(
            snoring_val, tired_val, observed_val, pressure_val,
            bmi_over_35, age_val, neck_large, gender_val
        )
        
        # Display result
        st.markdown("## 📊 Kết quả đánh giá")
        
        # Score display
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                STOP-BANG: {result['total_score']}/8
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Component breakdown
        st.markdown("### 📋 Chi tiết các thành phần")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**STOP:**")
            st.write(f"{'✅' if snoring_val else '⬜'} S - Ngáy to")
            st.write(f"{'✅' if tired_val else '⬜'} T - Mệt mỏi ban ngày")
            st.write(f"{'✅' if observed_val else '⬜'} O - Quan sát ngừng thở")
            st.write(f"{'✅' if pressure_val else '⬜'} P - Tăng huyết áp")
        
        with col2:
            st.markdown("**BANG:**")
            st.write(f"{'✅' if bmi_over_35 else '⬜'} B - BMI > 35 (hiện tại: {calculated_bmi:.1f})")
            st.write(f"{'✅' if age_val else '⬜'} A - Tuổi > 50")
            st.write(f"{'✅' if neck_large else '⬜'} N - Chu vi cổ lớn ({neck_circ} cm)")
            st.write(f"{'✅' if gender_val else '⬜'} G - Giới tính Nam")
        
        st.markdown("---")
        
        # Risk level
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Nguy cơ OSA: {result['risk_level']}</h3>
            <p style='font-size: 1.1em; margin: 10px 0;'>
                <strong>Xác suất OSA trung bình-nặng:</strong> {result['osa_probability']}
            </p>
            <p style='font-size: 1.2em; color: {score_color}; font-weight: bold; margin: 10px 0;'>
                {result['action']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed recommendations
        st.markdown("---")
        st.markdown("### 📋 Khuyến cáo chi tiết")
        
        if result["total_score"] <= 2:
            st.success("""
            ✅ **Nguy cơ OSA thấp (0-2 điểm)**
            
            **Khuyến cáo:**
            - Không cần làm polysomnography ngay
            - Tư vấn về giấc ngủ lành mạnh
            - Kiểm soát cân nặng nếu thừa cân
            - Tái đánh giá nếu có triệu chứng mới
            
            **Lưu ý:**
            - Nếu có triệu chứng rõ ràng, vẫn cân nhắc đánh giá thêm
            - Theo dõi các yếu tố nguy cơ khác
            """)
        
        elif result["total_score"] <= 4:
            st.warning("""
            ⚠️ **Nguy cơ OSA trung bình (3-4 điểm)**
            
            **Khuyến cáo:**
            - Cân nhắc làm polysomnography (nghiên cứu giấc ngủ)
            - Đặc biệt nếu có triệu chứng ảnh hưởng chất lượng sống
            - Tư vấn giảm cân nếu BMI cao
            - Tránh rượu, thuốc an thần trước khi ngủ
            
            **Trước phẫu thuật:**
            - Thông báo bác sĩ gây mê về nguy cơ OSA
            - Có thể cần theo dõi hậu phẫu chặt chẽ hơn
            - Cân nhắc CPAP sau mổ nếu có OSA
            """)
        
        else:
            st.error("""
            🚨 **Nguy cơ OSA cao (≥ 5 điểm)**
            
            **Khuyến cáo:**
            - ⚠️ Nên làm polysomnography để chẩn đoán xác định
            - Khả năng cao có OSA trung bình đến nặng
            - Cần điều trị nếu được chẩn đoán OSA
            
            **Can thiệp:**
            - CPAP (Continuous Positive Airway Pressure) - điều trị chính
            - Giảm cân (quan trọng nhất)
            - Ngủ nghiêng (tránh ngửa)
            - Tránh rượu, thuốc an thần
            - Điều trị viêm mũi họng nếu có
            - Cân nhắc phẫu thuật nếu không đáp ứng CPAP
            
            **Trước phẫu thuật:**
            - ⚠️ Bắt buộc thông báo bác sĩ gây mê
            - Nguy cơ cao biến chứng gây mê
            - Có thể cần CPAP sau mổ
            - Theo dõi hậu phẫu tích cực
            """)
        
        # Score interpretation table
        with st.expander("📊 Bảng phân loại STOP-BANG"):
            st.markdown("""
            | Điểm | Nguy cơ OSA | Xác suất OSA TB-nặng | Khuyến cáo |
            |:----:|:-----------|:---------------------|:-----------|
            | 0-2 | Thấp | < 15% | Không cần PSG trừ khi có triệu chứng |
            | 3-4 | Trung bình | 15-30% | Cân nhắc PSG |
            | 5-8 | Cao | > 30% | Khuyến cáo làm PSG |
            
            **PSG:** Polysomnography (nghiên cứu giấc ngủ)
            
            **Độ nhạy & đặc hiệu:**
            - Với ≥ 3 điểm: Độ nhạy ~84% cho OSA bất kỳ mức độ
            - Với ≥ 5 điểm: Độ nhạy ~93% cho OSA trung bình-nặng
            - Độ đặc hiệu thấp hơn (~40-50%) → nhiều dương tính giả
            
            **Lưu ý:**
            - STOP-BANG là công cụ sàng lọc, không phải chẩn đoán
            - Chẩn đoán xác định cần polysomnography
            - Độ nhạy cao → ít bỏ sót ca bệnh
            - Độ đặc hiệu thấp → cần xác nhận bằng PSG
            """)
        
        # Risk factors explanation
        with st.expander("🔍 Giải thích các yếu tố nguy cơ"):
            st.markdown("""
            ### 🛑 STOP - Triệu chứng lâm sàng
            
            **S - Snoring (Ngáy):**
            - Ngáy to, đặc biệt ngáy không đều
            - Tiếng ngáy ngắt quãng khi ngừng thở
            - Ngáy ảnh hưởng người khác
            
            **T - Tired (Mệt mỏi):**
            - Buồn ngủ ban ngày bất thường
            - Ngủ gật khi lái xe, xem TV, họp
            - Mệt mỏi dù ngủ đủ giờ
            - Điểm Epworth > 10
            
            **O - Observed apnea (Ngừng thở):**
            - Người khác thấy bạn ngưng thở khi ngủ
            - Thở hổn hển, thở gấp sau khi ngừng thở
            - Thức giấc với cảm giác nghẹt thở
            
            **P - Pressure (Tăng huyết áp):**
            - THA khó kiểm soát
            - THA đặc biệt vào buổi sáng
            - OSA là nguyên nhân thường gặp của THA kháng trị
            
            ### 💥 BANG - Đặc điểm cơ thể
            
            **B - BMI > 35:**
            - Béo phì là yếu tố nguy cơ chính
            - Mô mỡ vùng cổ họng gây hẹp đường thở
            - Giảm cân có thể giảm đáng kể OSA
            
            **A - Age > 50:**
            - Tuổi càng cao, nguy cơ OSA càng tăng
            - Do giảm trương lực cơ đường thở
            - Tăng mô mỡ vùng hầu họng
            
            **N - Neck circumference (Chu vi cổ):**
            - Nam: > 43 cm
            - Nữ: > 41 cm (hoặc > 40cm ở một số tiêu chuẩn)
            - Cổ to → đường thở dễ xẹp khi ngủ
            
            **G - Gender (Giới tính Nam):**
            - Nam giới có nguy cơ cao hơn 2-3 lần
            - Do khác biệt giải phẫu đường thở
            - Phân bố mô mỡ khác nhau
            - Nữ sau mãn kinh nguy cơ tăng
            """)
        
        # OSA complications
        with st.expander("⚠️ Biến chứng của OSA không điều trị"):
            st.markdown("""
            ### Tim mạch:
            - Tăng huyết áp
            - Rối loạn nhịp tim (đặc biệt rung nhĩ)
            - Bệnh tim thiếu máu cục bộ
            - Suy tim
            - Đột quỵ
            
            ### Chuyển hóa:
            - Đái tháo đường type 2
            - Hội chứng chuyển hóa
            - Béo phì (vòng xoắn ác tính)
            
            ### Thần kinh - Tâm thần:
            - Buồn ngủ ban ngày nguy hiểm
            - Giảm tập trung, trí nhớ
            - Trầm cảm
            - Tai nạn giao thông (tăng 2-7 lần)
            
            ### Khác:
            - Giảm chất lượng cuộc sống
            - Rối loạn tình dục
            - Tăng nguy cơ biến chứng phẫu thuật
            - Tử vong sớm nếu OSA nặng không điều trị
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Snoring": "Yes" if snoring_val else "No",
            "Tired": "Yes" if tired_val else "No",
            "Observed": "Yes" if observed_val else "No",
            "Pressure": "Yes" if pressure_val else "No",
            "BMI": f"{calculated_bmi:.1f}",
            "BMI > 35": "Yes" if bmi_over_35 else "No",
            "Age > 50": "Yes" if age_val else "No",
            "Neck Circumference": f"{neck_circ} cm",
            "Neck Large": "Yes" if neck_large else "No",
            "Gender": "Male" if gender_val else "Female"
        }
        
        results_dict = {
            "STOP-BANG Score": f"{result['total_score']}/8",
            "Risk Level": result['risk_level'],
            "OSA Probability": result['osa_probability']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="STOP-BANG",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="STOP-BANG"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="stop_bang",
            calculator_name="STOP-BANG",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="stop_bang",
            calculator_name="STOP-BANG",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="stop_bang", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="stop_bang",
            calculator_name="STOP-BANG",
            category="Tai mũi họng",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("STOP-BANG")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    
    # Quick tips
    st.markdown("---")
    st.info("""
    💡 **Lưu ý quan trọng:**
    
    1. **STOP-BANG là công cụ sàng lọc** - Không thay thế chẩn đoán chính thức bằng polysomnography
    
    2. **Độ nhạy cao** - Ít bỏ sót OSA, nhưng nhiều dương tính giả
    
    3. **Đặc biệt hữu ích:**
       - Đánh giá tiền phẫu (nguy cơ gây mê)
       - Sàng lọc nhanh trong phòng khám
       - Quyết định có cần polysomnography
    
    4. **Điều trị OSA hiệu quả:**
       - CPAP là điều trị chính
       - Giảm cân rất quan trọng
       - Thay đổi lối sống
       - Cải thiện đáng kể chất lượng sống và giảm biến chứng
    
    5. **Trước phẫu thuật:** Điểm cao cần thông báo bác sĩ gây mê để có kế hoạch quản lý phù hợp
    """)


if __name__ == "__main__":
    render()

