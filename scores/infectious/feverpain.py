"""
FeverPAIN Score Calculator
Đánh giá viêm amidan - Quyết định có cần kháng sinh
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def calculate_feverpain(fever, purulence, attend_rapidly, inflamed_tonsils, no_cough):
    """
    Tính điểm FeverPAIN
    
    Parameters: Mỗi thành phần = 1 nếu có, 0 nếu không
    - fever: Sốt trong 24h qua (≥ 38°C)
    - purulence: Có mủ trên amidan
    - attend_rapidly: Đến khám trong 3 ngày từ khi khởi phát
    - inflamed_tonsils: Amidan sưng/viêm rất nặng
    - no_cough_cold: Không ho hoặc viêm mũi
    
    Returns:
    - dict với total_score và interpretation
    """
    # Fever = 1 point, others = 1 point each
    total = fever + purulence + attend_rapidly + inflamed_tonsils + no_cough
    
    # Phân loại
    if total <= 1:
        risk = "Rất thấp"
        strep_probability = "13-18%"
        recommendation = "Không cần kháng sinh. Tư vấn điều trị triệu chứng"
        color = "green"
        antibiotic_advice = "KHÔNG khuyến cáo"
    elif total <= 3:
        risk = "Thấp-Trung bình"
        strep_probability = "34-40%"
        recommendation = "Cân nhắc kháng sinh hoặc đợi-quan sát (delayed prescription)"
        color = "orange"
        antibiotic_advice = "Cân nhắc hoặc kê đơn chờ"
    else:  # >= 4
        risk = "Cao"
        strep_probability = "62-65%"
        recommendation = "Khả năng cao nhiễm liên cầu. Nên dùng kháng sinh ngay"
        color = "red"
        antibiotic_advice = "KHUYẾN CÁO dùng"
    
    return {
        "total_score": total,
        "risk_level": risk,
        "strep_probability": strep_probability,
        "recommendation": recommendation,
        "antibiotic_advice": antibiotic_advice,
        "color": color
    }


def render():
    """Render FeverPAIN calculator interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'feverpain':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'FeverPAIN')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #EF4444;'>🤒 FeverPAIN Score</h2>
    <p style='text-align: center;'><em>Viêm amidan - Quyết định kháng sinh</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về FeverPAIN
    with st.expander("ℹ️ Giới thiệu về FeverPAIN"):
        st.markdown("""
        **FeverPAIN Score** là công cụ giúp bác sĩ quyết định có nên kê kháng sinh 
        cho bệnh nhân viêm họng/viêm amidan hay không.
        
        **Mục đích:**
        - Dự đoán nguy cơ nhiễm liên cầu (Streptococcus)
        - Giảm sử dụng kháng sinh không cần thiết
        - Cải thiện quản lý viêm họng cấp
        
        **Ưu điểm:**
        - Đơn giản, nhanh chóng (chỉ 5 tiêu chí)
        - Không cần xét nghiệm
        - Giúp giảm kháng kháng sinh
        
        **So sánh với Centor:**
        - FeverPAIN: Cho người lớn và trẻ em
        - Centor: Chủ yếu cho người lớn
        - FeverPAIN có độ chính xác tương đương hoặc tốt hơn
        
        **Lưu ý:**
        - Áp dụng cho viêm họng/amidan cấp
        - Chủ yếu dùng ở cộng đồng/phòng khám
        - Luôn kết hợp đánh giá lâm sàng tổng thể
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Đánh giá 5 Tiêu chí FeverPAIN")
    
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
        <p style='margin: 0;'>
            ✅ Đánh dấu nếu <strong>CÓ</strong> đặc điểm đó<br>
            ⬜ Bỏ trống nếu <strong>KHÔNG</strong> có
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    fever = st.checkbox(
        "**F**ever - Sốt trong 24 giờ qua (≥ 38°C / 100.4°F)",
        help="Có tiền sử sốt trong vòng 24 giờ"
    )
    
    purulence = st.checkbox(
        "**P**urulence - Có mủ trên amidan",
        help="Nhìn thấy mủ (exudate) trên bề mặt amidan"
    )
    
    attend_rapidly = st.checkbox(
        "**A**ttend rapidly - Đến khám trong ≤ 3 ngày từ lúc khởi phát",
        help="Bệnh nhân đến khám trong vòng 3 ngày kể từ khi có triệu chứng"
    )
    
    inflamed_tonsils = st.checkbox(
        "**I**nflamed tonsils - Amidan viêm rất nặng",
        help="Amidan sưng đỏ nặng, có thể phù to"
    )
    
    no_cough = st.checkbox(
        "**N**o cough or coryza - Không ho và không sổ mũi",
        help="Không có ho hoặc triệu chứng cảm lạnh (viêm mũi)"
    )
    
    st.markdown("---")
    
    # Convert to binary
    fever_val = 1 if fever else 0
    purulence_val = 1 if purulence else 0
    attend_val = 1 if attend_rapidly else 0
    inflamed_val = 1 if inflamed_tonsils else 0
    no_cough_val = 1 if no_cough else 0
    
    # Calculate button
    if st.button("🔬 Tính điểm FeverPAIN", type="primary", use_container_width=True):
        result = calculate_feverpain(fever_val, purulence_val, attend_val, inflamed_val, no_cough_val)
        
        # Display result
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
                FeverPAIN: {result['total_score']}/5
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Component breakdown
        st.markdown("### ✅ Tiêu chí có:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"{'✅' if fever_val else '⬜'} **F** - Fever (Sốt)")
            st.write(f"{'✅' if purulence_val else '⬜'} **P** - Purulence (Mủ)")
            st.write(f"{'✅' if attend_val else '⬜'} **A** - Attend rapidly (Đến sớm)")
        
        with col2:
            st.write(f"{'✅' if inflamed_val else '⬜'} **I** - Inflamed tonsils (Amidan viêm nặng)")
            st.write(f"{'✅' if no_cough_val else '⬜'} **N** - No cough/coryza (Không ho/sổ mũi)")
        
        st.markdown("---")
        
        # Risk and recommendation
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Nguy cơ nhiễm liên cầu: {result['risk_level']}</h3>
            <p style='font-size: 1.1em; margin: 10px 0;'>
                <strong>Xác suất nhiễm Streptococcus:</strong> {result['strep_probability']}
            </p>
            <p style='font-size: 1.2em; color: {score_color}; font-weight: bold; margin: 10px 0;'>
                💊 Kháng sinh: {result['antibiotic_advice']}
            </p>
            <p style='font-size: 1.1em; margin: 10px 0;'>
                {result['recommendation']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed management
        st.markdown("---")
        st.markdown("### 📋 Hướng dẫn xử trí")
        
        if result["total_score"] <= 1:
            st.success("""
            ✅ **Điểm 0-1: KHÔNG cần kháng sinh**
            
            **Xử trí:**
            - Giải thích cho bệnh nhân: Nhiễm virus, tự khỏi
            - Điều trị triệu chứng:
              - Giảm đau/hạ sốt: Paracetamol, Ibuprofen
              - Súc miệng nước muối ấm
              - Uống nhiều nước
              - Nghỉ ngơi
            
            **Tư vấn:**
            - Thường khỏi trong 3-7 ngày
            - Quay lại nếu:
              - Sốt kéo dài > 3 ngày
              - Triệu chứng nặng lên
              - Khó nuốt/thở
              - Xuất hiện phát ban
            
            **Giáo dục:**
            - Kháng sinh không hiệu quả với virus
            - Dùng kháng sinh không cần thiết gây kháng thuốc
            """)
        
        elif result["total_score"] <= 3:
            st.warning("""
            ⚠️ **Điểm 2-3: CÂN NHẮC kháng sinh**
            
            **Lựa chọn:**
            
            1. **"Đợi và xem" (Delayed prescription):** ✅ Khuyến cáo
               - Kê đơn nhưng hướng dẫn chỉ dùng nếu:
                 - Không khỏi sau 3-5 ngày
                 - Triệu chứng nặng lên đáng kể
               - Cho phép cơ thể tự chống nhiễm trùng
               - Giảm sử dụng kháng sinh không cần thiết
            
            2. **Dùng ngay:**
               - Nếu bệnh nhân có yếu tố nguy cơ cao
               - Triệu chứng nặng
               - Không thể tái khám
            
            **Kháng sinh nếu dùng:**
            - **Chọn lựa 1:** Phenoxymethylpenicillin (Penicillin V)
              - Liều: 500mg x 2-4 lần/ngày x 5-10 ngày
            - **Nếu dị ứng penicillin:** Clarithromycin hoặc Azithromycin
            
            **Điều trị triệu chứng:** Như trên
            """)
        
        else:  # >= 4
            st.error("""
            🔴 **Điểm 4-5: KHUYẾN CÁO dùng kháng sinh**
            
            **Lý do:**
            - Khả năng cao nhiễm Streptococcus β-hemolytic nhóm A
            - Nguy cơ biến chứng (tuy hiếm):
              - Áp xe quanh amidan
              - Sốt thấp khớp (hiếm ở nước phát triển)
              - Viêm cầu thận sau liên cầu
            
            **Kháng sinh:**
            - **Lựa chọn 1:** Phenoxymethylpenicillin (Penicillin V)
              - 500mg uống x 2-4 lần/ngày x 10 ngày
              - Hoặc: Amoxicillin 500mg x 3 lần/ngày x 10 ngày
            
            - **Nếu dị ứng penicillin:**
              - Clarithromycin 250-500mg x 2 lần/ngày x 5 ngày
              - Hoặc Azithromycin 500mg ngày 1, rồi 250mg x 4 ngày
            
            **Quan trọng:**
            - Uống đủ liều, đủ ngày
            - Không tự ý ngừng khi đỡ triệu chứng
            
            **Kết hợp:**
            - Giảm đau/hạ sốt: Paracetamol, Ibuprofen
            - Súc miệng nước muối
            - Uống nhiều nước, nghỉ ngơi
            
            **Theo dõi:**
            - Quay lại nếu không đỡ sau 3 ngày dùng kháng sinh
            - Hoặc nếu có dấu hiệu biến chứng
            """)
        
        # Score interpretation table
        with st.expander("📊 Bảng phân loại FeverPAIN"):
            st.markdown("""
            | Điểm | Nguy cơ | Xác suất Strep | Khuyến cáo kháng sinh |
            |:----:|:--------|:---------------|:----------------------|
            | 0-1 | Rất thấp | 13-18% | **Không** dùng |
            | 2-3 | Thấp-TB | 34-40% | **Cân nhắc** hoặc kê đơn chờ |
            | 4-5 | Cao | 62-65% | **Nên dùng** |
            
            **"Delayed prescription" (Kê đơn chờ):**
            - Chiến lược tốt cho điểm 2-3
            - Kê đơn nhưng hướng dẫn chỉ mua nếu không khỏi sau 3-5 ngày
            - Giảm 40% sử dụng kháng sinh
            - Độ hài lòng bệnh nhân cao
            """)
        
        # FeverPAIN vs Centor
        with st.expander("🔄 So sánh FeverPAIN vs Centor Score"):
            st.markdown("""
            ### FeverPAIN (5 tiêu chí):
            1. **F**ever - Sốt trong 24h (≥38°C)
            2. **P**urulence - Mủ trên amidan
            3. **A**ttend rapidly - Đến khám ≤ 3 ngày
            4. **I**nflamed tonsils - Amidan viêm rất nặng
            5. **N**o cough/coryza - Không ho/sổ mũi
            
            ### Centor Score (4 tiêu chí):
            1. Sốt (> 38°C)
            2. Mủ trên amidan
            3. Hạch cổ trước to đau
            4. Không ho
            *Điều chỉnh theo tuổi: +1 nếu 3-14 tuổi, -1 nếu ≥ 45 tuổi*
            
            ### So sánh:
            
            | Đặc điểm | FeverPAIN | Centor |
            |:---------|:----------|:-------|
            | Độ nhạy | ~90% | ~75% |
            | Độ đặc hiệu | ~80% | ~70% |
            | Áp dụng | Mọi lứa tuổi | Chủ yếu người lớn |
            | Tiện lợi | Dễ hơn (không cần đánh giá hạch) | Cần khám hạch |
            | Khuyến cáo | NICE, SIGN (UK) | Widespread |
            
            **Lưu ý:** Cả hai đều có giá trị, lựa chọn tùy theo từng phòng khám
            """)
        
        # Complications
        with st.expander("⚠️ Biến chứng viêm họng liên cầu"):
            st.markdown("""
            ### Biến chứng sớm (1-2 tuần):
            
            **Áp xe quanh amidan (Peritonsillar abscess):**
            - Triệu chứng:
              - Đau họng một bên rất nặng
              - Khó nuốt, chảy nước bọt
              - Tiếng nói ngậm ("hot potato voice")
              - Lệch thanh quản
            - Xử trí: Dẫn lưu + Kháng sinh tĩnh mạch
            
            **Áp xe sau hầu (Retropharyngeal abscess):**
            - Chủ yếu ở trẻ em < 5 tuổi
            - Khó thở, cổ cứng
            - Cần can thiệp khẩn cấp
            
            ### Biến chứng muộn (2-4 tuần):
            
            **Sốt thấp khớp (Rheumatic fever):**
            - Hiếm ở nước phát triển
            - Viêm khớp, viêm cơ tim, chorea
            - Phòng ngừa: Kháng sinh đúng và đủ
            
            **Viêm cầu thận cấp sau liên cầu:**
            - Phù, tăng huyết áp, nước tiểu sẫm màu
            - Thường tự khỏi
            - Kháng sinh không phòng ngừa được
            
            **Lưu ý:**
            - Biến chứng hiếm khi điều trị phù hợp
            - Kháng sinh giảm nguy cơ sốt thấp khớp
            - Theo dõi để phát hiện sớm biến chứng
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Little P, Hobbs FD, Moore M, et al.** Clinical score and rapid antigen detection test 
               to guide antibiotic use for sore throats: randomised controlled trial of PRISM (primary care 
               streptococcal management). BMJ. 2013;347:f5806.
            
            2. **Little P, Moore M, Hobbs FD, et al.** PRImary care Streptococcal Management (PRISM) study: 
               identifying clinical variables associated with Lancefield group A β-haemolytic streptococci and 
               Lancefield non-Group A streptococcal throat infections from two cohorts of patients presenting 
               with an acute sore throat. BMJ Open. 2013;3(10):e003943.
            
            3. **NICE Clinical Guideline 84.** Respiratory tract infections (self-limiting): 
               prescribing antibiotics. 2008 (updated 2015).
            
            4. **SIGN Guideline 117.** Management of sore throat and indications for tonsillectomy. 
               Scottish Intercollegiate Guidelines Network. 2010.
            
            5. **Spinks A, Glasziou PP, Del Mar CB.** Antibiotics for sore throat. 
               Cochrane Database Syst Rev. 2013;(11):CD000023.
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Fever": "Yes" if fever_val else "No",
            "Purulence": "Yes" if purulence_val else "No",
            "Attend Rapidly": "Yes" if attend_val else "No",
            "Inflamed Tonsils": "Yes" if inflamed_val else "No",
            "No Cough": "Yes" if no_cough_val else "No"
        }
        
        results_dict = {
            "FeverPAIN Score": f"{result['total_score']}/5",
            "Risk Level": result['risk_level'],
            "Strep Probability": result['strep_probability'],
            "Antibiotic Advice": result['antibiotic_advice']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="FeverPAIN",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="FeverPAIN"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="feverpain",
            calculator_name="FeverPAIN",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="feverpain",
            calculator_name="FeverPAIN",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="feverpain", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="feverpain",
            calculator_name="FeverPAIN",
            category="Nhiễm khuẩn",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Quick guide
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Mục tiêu:** Giảm sử dụng kháng sinh không cần thiết (antimicrobial stewardship)
    
    2. **Điểm 0-1:** KHÔNG dùng kháng sinh - hầu hết do virus
    
    3. **Điểm 2-3:** CÂN NHẮC - "Delayed prescription" là lựa chọn tốt
    
    4. **Điểm 4-5:** NÊN DÙNG kháng sinh - khả năng cao nhiễm liên cầu
    
    5. **Kháng sinh lựa chọn:** Penicillin V (hoặc Amoxicillin) - vẫn hiệu quả tốt
    
    6. **Điều trị triệu chứng:** Quan trọng ở mọi mức độ
    
    7. **Giáo dục bệnh nhân:** Giải thích lý do dùng/không dùng kháng sinh
    """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("FeverPAIN")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

