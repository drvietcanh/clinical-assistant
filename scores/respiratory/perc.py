"""
PERC Rule (Pulmonary Embolism Rule-out Criteria)
Loại trừ thuyên tắc phổi mà không cần D-dimer
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def render():
    """Render PERC Rule interface"""
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🫁 PERC Rule</h2>
    <p style='text-align: center; color: #6B7280;'><em>Pulmonary Embolism Rule-out Criteria</em></p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'perc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        # Pre-fill inputs from shared result (optional)
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Thông tin về PERC
    with st.expander("ℹ️ Giới thiệu về PERC Rule"):
        st.markdown("""
        **PERC Rule** giúp **LOẠI TRỪ** thuyên tắc phổi (PE) ở bệnh nhân **NGUY CƠ THẤP** 
        **MÀ KHÔNG CẦN** xét nghiệm D-dimer hay chụp CT.
        
        **Mục đích:**
        - Giảm xét nghiệm không cần thiết
        - Tránh phơi nhiễm radiation (CT)
        - Tránh kết quả dương tính giả của D-dimer
        - Tiết kiệm chi phí
        
        **Khi nào dùng:**
        - ✅ Bệnh nhân **nguy cơ thấp** nghi PE (ví dụ: Wells PE < 2)
        - ✅ Triệu chứng không điển hình
        - ✅ Muốn loại trừ PE nhanh không cần xét nghiệm
        
        **Khi KHÔNG dùng:**
        - ❌ Bệnh nhân nguy cơ trung bình/cao (Wells PE ≥ 2)
        - ❌ Triệu chứng điển hình PE
        - ❌ Đã có kết quả D-dimer dương tính
        
        **Nguyên tắc:**
        - **PERC = 0 (tất cả âm)** → Có thể loại trừ PE, KHÔNG cần D-dimer
        - **PERC ≥ 1** → Cần xét nghiệm thêm (D-dimer hoặc CT)
        
        **Độ chính xác:**
        - NPV (giá trị dự đoán âm): ~99.3%
        - Sensitivity: ~97-100%
        - Tỷ lệ PE nếu PERC = 0: <1.4%
        """)
    
    st.markdown("---")
    
    # Important warning
    st.warning("""
    ⚠️ **CHỈ ÁP DỤNG CHO BỆNH NHÂN NGUY CƠ THẤP!**
    
    - PERC chỉ dùng khi **xác suất lâm sàng PE < 15%**
    - Thường kết hợp với **Wells PE < 2** hoặc **Geneva < 2**
    - **KHÔNG** áp dụng cho bệnh nhân nguy cơ trung bình/cao
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Input form - 8 criteria
        st.subheader("📝 Đánh giá 8 tiêu chí PERC")
        
        st.markdown("""
        **PERC Rule bao gồm 8 tiêu chí. Trả lời CÓ/KHÔNG cho từng tiêu chí:**
        
        *(Nếu TẤT CẢ đều KHÔNG → PERC âm → Có thể loại trừ PE)*
        """)
        
        # Pre-fill from shared result if available
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        # Age
        st.markdown("### 1️⃣ Tuổi tác:")
        age_50 = st.checkbox(
            "Tuổi ≥ 50",
            help="Bệnh nhân từ 50 tuổi trở lên",
            value=shared_inputs.get('Age ≥ 50') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Heart rate
        st.markdown("### 2️⃣ Mạch:")
        hr_100 = st.checkbox(
            "Nhịp tim ≥ 100 nhịp/phút",
            help="Nhịp tim nhanh (tachycardia)",
            value=shared_inputs.get('HR ≥ 100') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Oxygen saturation
        st.markdown("### 3️⃣ Oxy hóa máu:")
        spo2_95 = st.checkbox(
            "SpO₂ < 95% (khí phòng)",
            help="Bão hòa oxy thấp khi thở khí phòng",
            value=shared_inputs.get('SpO₂ < 95%') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Unilateral leg swelling
        st.markdown("### 4️⃣ Phù chân:")
        leg_swelling = st.checkbox(
            "Phù chân một bên",
            help="Phù chân đơn độc (gợi ý DVT)",
            value=shared_inputs.get('Leg Swelling') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Hemoptysis
        st.markdown("### 5️⃣ Ho ra máu:")
        hemoptysis = st.checkbox(
            "Ho ra máu (Hemoptysis)",
            help="Ho ra máu tươi hoặc đờm lẫn máu",
            value=shared_inputs.get('Hemoptysis') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Recent surgery or trauma
        st.markdown("### 6️⃣ Phẫu thuật/Chấn thương gần đây:")
        surgery_trauma = st.checkbox(
            "Phẫu thuật hoặc chấn thương trong 4 tuần qua",
            help="Yêu cầu gây mê trong 4 tuần gần nhất",
            value=shared_inputs.get('Surgery/Trauma') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Prior PE or DVT
        st.markdown("### 7️⃣ Tiền sử huyết khối:")
        prior_vte = st.checkbox(
            "Tiền sử PE hoặc DVT",
            help="Từng bị thuyên tắc phổi hoặc huyết khối tĩnh mạch sâu",
            value=shared_inputs.get('Prior VTE') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
        
        # Hormone use
        st.markdown("### 8️⃣ Dùng hormone:")
        hormone = st.checkbox(
            "Đang dùng hormone (Estrogen)",
            help="Thuốc tránh thai, HRT, hoặc đang mang thai",
            value=shared_inputs.get('Hormone Use') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="perc",
            calculator_name="PERC Rule",
            category="Hô hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Calculate button
    if st.button("🔍 Đánh giá PERC", type="primary", use_container_width=True):
        # Count positive criteria
        criteria = [
            age_50,
            hr_100,
            spo2_95,
            leg_swelling,
            hemoptysis,
            surgery_trauma,
            prior_vte,
            hormone
        ]
        
        perc_score = sum(criteria)
        
        # Initialize positive_criteria list
        positive_criteria = []
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # PERC negative or positive
        from components.ui.scoring import render_score_result
        
        # PERC negative or positive
        if perc_score == 0:
            # PERC NEGATIVE
            render_score_result(
                title="PERC Âm Tính",
                score=perc_score,
                max_score=8,
                interpretation="Có thể loại trừ PE",
                recommendation="Nguy cơ PE < 1.4% - Không cần xét nghiệm thêm",
                color=COLORS['success'],
                icon="✅"
            )
            
            st.success("""
            ### ✅ CÓ THỂ LOẠI TRỪ PE!
            
            **Kết luận:**
            - Bệnh nhân **NGUY CƠ RẤT THẤP** bị PE (<1.4%)
            - **KHÔNG CẦN** xét nghiệm D-dimer
            - **KHÔNG CẦN** chụp CT phổi
            
            **Khuyến cáo:**
            - ✅ Có thể cho bệnh nhân về nhà
            - ✅ Tìm nguyên nhân khác gây triệu chứng
            - ✅ Theo dõi ngoại trú
            - ✅ Tư vấn bệnh nhân về dấu hiệu cần tái khám
            
            **Lưu ý:**
            - Chỉ áp dụng nếu đánh giá lâm sàng **nguy cơ thấp** (<15%)
            - Nếu triệu chứng tiến triển → tái đánh giá
            """)
        
        else:
            # PERC POSITIVE
            render_score_result(
                title="PERC Dương Tính",
                score=perc_score,
                max_score=8,
                interpretation=f"Có {perc_score} tiêu chí dương tính",
                recommendation="Cần xét nghiệm thêm (D-dimer/CT)",
                color=COLORS['error'],
                icon="⚠️"
            )
            
            # List positive criteria
            st.markdown("### 📋 Tiêu chí dương tính:")
            
            if age_50:
                positive_criteria.append("✓ Tuổi ≥ 50")
            if hr_100:
                positive_criteria.append("✓ Nhịp tim ≥ 100 nhịp/phút")
            if spo2_95:
                positive_criteria.append("✓ SpO₂ < 95%")
            if leg_swelling:
                positive_criteria.append("✓ Phù chân một bên")
            if hemoptysis:
                positive_criteria.append("✓ Ho ra máu")
            if surgery_trauma:
                positive_criteria.append("✓ Phẫu thuật/chấn thương gần đây")
            if prior_vte:
                positive_criteria.append("✓ Tiền sử PE/DVT")
            if hormone:
                positive_criteria.append("✓ Dùng hormone")
            
            for criterion in positive_criteria:
                st.markdown(f"- {criterion}")
            
            st.markdown("---")
            
            st.error("""
            ### ⚠️ KHÔNG THỂ LOẠI TRỪ PE!
            
            **Kết luận:**
            - **CẦN XÉT NGHIỆM THÊM** để đánh giá PE
            - PERC Rule không giúp loại trừ PE
            
            **Khuyến cáo tiếp theo:**
            
            1️⃣ **Đánh giá nguy cơ bằng Wells PE Score hoặc Geneva Score**
            
            2️⃣ **Nếu nguy cơ thấp (Wells < 4):**
            - Xét nghiệm **D-dimer**
            - Nếu D-dimer (-) → Loại trừ PE
            - Nếu D-dimer (+) → Chụp CTPA
            
            3️⃣ **Nếu nguy cơ trung bình/cao (Wells ≥ 4):**
            - Chụp **CTPA** (CT Pulmonary Angiography) ngay
            - HOẶC V/Q scan nếu không thể CTPA
            
            4️⃣ **Nếu không ổn định huyết động:**
            - Siêu âm tim cấp cứu (TTE)
            - Cân nhắc tiêu huyết khối
            
            **Trong khi chờ:**
            - Theo dõi SpO₂, huyết động
            - Oxy liệu pháp nếu cần
            - Cân nhắc chống đông (Heparin) nếu nguy cơ cao
            """)
        
        # Additional info
        st.markdown("---")
        st.markdown("### 📚 Thông tin thêm")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Điểm PERC",
                f"{perc_score}/8",
                help="Số tiêu chí dương tính"
            )
        
        with col2:
            pe_risk = "< 1.4%" if perc_score == 0 else "Cần đánh giá thêm"
            st.metric(
                "Nguy cơ PE",
                pe_risk,
                help="Xác suất bị PE nếu PERC = 0"
            )
        
        # Algorithm
        with st.expander("🔄 Thuật toán đánh giá PE với PERC"):
            st.markdown("""
            ```
            Nghi ngờ PE
                ↓
            Đánh giá lâm sàng
                ↓
            ┌─────────────────┐
            │  Nguy cơ thấp?  │ (Gestalt hoặc Wells < 2)
            └─────────────────┘
                    │
                    ├─── KHÔNG (nguy cơ trung bình/cao)
                    │         ↓
                    │    [BỎ QUA PERC]
                    │         ↓
                    │    Wells PE Score
                    │         ↓
                    │    Wells < 4: D-dimer
                    │    Wells ≥ 4: CTPA ngay
                    │
                    └─── CÓ (nguy cơ thấp)
                              ↓
                        Áp dụng PERC
                              ↓
                    ┌─────────────────┐
                    │   PERC = 0?     │
                    └─────────────────┘
                         │
                         ├─── CÓ (tất cả âm)
                         │       ↓
                         │   ✅ LOẠI TRỪ PE
                         │   Không cần xét nghiệm
                         │   Tìm nguyên nhân khác
                         │
                         └─── KHÔNG (≥1 dương)
                                 ↓
                            Wells PE Score
                                 ↓
                            Wells < 4: D-dimer
                            Wells ≥ 4: CTPA
            ```
            
            **Giải thích:**
            - PERC chỉ dùng cho bệnh nhân **nguy cơ thấp**
            - Nếu PERC = 0 → Loại trừ PE, không cần xét nghiệm
            - Nếu PERC ≥ 1 → Tiếp tục theo thuật toán (Wells → D-dimer/CTPA)
            """)
        
        # Clinical application
        with st.expander("💡 Ứng dụng lâm sàng"):
            st.markdown("""
            ### Kịch bản 1: PERC Âm tính ✅
            
            **Bệnh nhân:** Nữ 35 tuổi, khó thở nhẹ sau chuyến bay dài
            - Triệu chứng không điển hình
            - Wells PE = 1.5 (nguy cơ thấp)
            - **PERC = 0** (tất cả tiêu chí âm)
            
            **Xử trí:**
            - ✅ **Không cần D-dimer, không cần CT**
            - ✅ Tìm nguyên nhân khác (anxiety, musculoskeletal)
            - ✅ Cho về nhà với hướng dẫn tái khám
            
            ---
            
            ### Kịch bản 2: PERC Dương tính ⚠️
            
            **Bệnh nhân:** Nữ 52 tuổi, khó thở sau mổ
            - Triệu chứng không điển hình
            - Wells PE = 1.5 (nguy cơ thấp)
            - **PERC = 2** (tuổi ≥50 + mổ gần đây)
            
            **Xử trí:**
            - ⚠️ **Không thể loại trừ PE bằng PERC**
            - → Xét nghiệm D-dimer
            - Nếu D-dimer (+) → CTPA
            
            ---
            
            ### Kịch bản 3: KHÔNG dùng PERC ❌
            
            **Bệnh nhân:** Nam 60 tuổi, đau ngực + khó thở + ho ra máu
            - Triệu chứng điển hình PE
            - Wells PE = 7.5 (nguy cơ cao)
            
            **Xử trí:**
            - ❌ **KHÔNG áp dụng PERC** (nguy cơ không thấp)
            - → **CTPA ngay**, không cần D-dimer
            - Cân nhắc chống đông trong khi chờ
            """)
        
        # Limitations
        with st.expander("⚠️ Giới hạn của PERC"):
            st.markdown("""
            **PERC KHÔNG nên dùng khi:**
            
            1. **Nguy cơ KHÔNG thấp:**
               - Wells PE ≥ 2
               - Geneva ≥ 2
               - Gestalt > 15%
            
            2. **Triệu chứng điển hình PE:**
               - Khó thở đột ngột + đau ngực + ho ra máu
               - Syncope không rõ nguyên nhân
               - Huyết động không ổn định
            
            3. **Đã có xét nghiệm:**
               - D-dimer đã dương tính
               - ECG có S1Q3T3, RBBB mới
               - X-quang ngực bất thường gợi ý PE
            
            **Cẩn trọng ở:**
            - Thai phụ (nhiều tiêu chí PERC dương tính sinh lý)
            - Người rất cao tuổi (>80)
            - Bệnh phổi mạn tính (SpO₂ thường < 95%)
            
            **Lưu ý:**
            - PERC có độ nhạy cao (97-100%) nhưng độ đặc hiệu thấp
            - Mục đích: **Loại trừ** (rule-out), không phải chẩn đoán
            - Luôn kết hợp đánh giá lâm sàng tổng thể
            """)
        
        # Prepare inputs for export and history
        inputs_dict = {
            "Age ≥ 50": "Có" if age_50 else "Không",
            "HR ≥ 100": "Có" if hr_100 else "Không",
            "SpO₂ < 95%": "Có" if spo2_95 else "Không",
            "Leg Swelling": "Có" if leg_swelling else "Không",
            "Hemoptysis": "Có" if hemoptysis else "Không",
            "Surgery/Trauma": "Có" if surgery_trauma else "Không",
            "Prior VTE": "Có" if prior_vte else "Không",
            "Hormone Use": "Có" if hormone else "Không"
        }
        
        # Prepare results for export and history
        results_dict = {
            "PERC Score": f"{perc_score}/8",
            "Result": "PERC Âm Tính - Có thể loại trừ PE" if perc_score == 0 else "PERC Dương Tính - Cần xét nghiệm thêm",
            "PE Risk": "< 1.4%" if perc_score == 0 else "Cần đánh giá thêm",
            "Positive Criteria": ", ".join(positive_criteria) if perc_score > 0 else "Không có"
        }
        
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        render_export_section(
            title=f"PERC Score = {perc_score}/8",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="PERC Rule",
            filename="perc_result"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="perc",
            calculator_name="PERC Rule",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="perc",
            calculator_name="PERC Rule",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="perc", show_actions=True)
        
        # References section
        references = get_references("PERC")
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
                1. **Kline JA, Mitchell AM, Kabrhel C, Richman PB, Courtney DM.** 
                   Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism. 
                   *J Thromb Haemost.* 2004;2(8):1247-55.
                
                2. **Kline JA, Courtney DM, Kabrhel C, et al.** Prospective multicenter evaluation of the pulmonary embolism rule-out criteria. 
                   *J Thromb Haemost.* 2008;6(5):772-80.
                
                3. **Hugli O, Righini M, Le Gal G, et al.** The pulmonary embolism rule-out criteria (PERC) rule does not safely exclude pulmonary embolism. 
                   *J Thromb Haemost.* 2011;9(2):300-4.
                
                4. **Raja AS, Greenberg JO, Qaseem A, et al.** Evaluation of Patients With Suspected Acute Pulmonary Embolism: Best Practice Advice From the Clinical Guidelines Committee of the American College of Physicians. 
                   *Ann Intern Med.* 2015;163(9):701-11.
                
                5. **Konstantinides SV, Meyer G, Becattini C, et al.** 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism developed in collaboration with the European Respiratory Society (ERS). 
                   *Eur Heart J.* 2020;41(4):543-603.
                """)
    
    # Quick reference
    st.markdown("---")
    st.markdown("### 📋 Tóm tắt 8 tiêu chí PERC:")
    
    st.markdown("""
    | # | Tiêu chí | Dương tính khi |
    |:--|:---------|:---------------|
    | 1 | Tuổi | ≥ 50 tuổi |
    | 2 | Nhịp tim | ≥ 100 bpm |
    | 3 | SpO₂ | < 95% (khí phòng) |
    | 4 | Phù chân | Phù một bên |
    | 5 | Ho ra máu | Có hemoptysis |
    | 6 | Phẫu thuật/Chấn thương | Trong 4 tuần |
    | 7 | Tiền sử VTE | Có PE/DVT trước đây |
    | 8 | Hormone | Đang dùng estrogen |
    
    **Kết luận:**
    - **PERC = 0** → Loại trừ PE, không cần xét nghiệm
    - **PERC ≥ 1** → Cần xét nghiệm thêm
    """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **CHỈ dùng cho bệnh nhân NGUY CƠ THẤP** (<15%)
    
    2. **PERC = 0** → Tỷ lệ PE <1.4% → An toàn loại trừ
    
    3. **Tiết kiệm:** Không cần D-dimer, không cần CT (giảm chi phí, radiation)
    
    4. **Không thay thế** đánh giá lâm sàng và Wells PE Score
    
    5. **Khi nghi ngờ** → Làm xét nghiệm, đừng bỏ sót PE!
    """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("PERC")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

