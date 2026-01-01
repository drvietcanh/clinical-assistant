"""
4Ts Score for Heparin-Induced Thrombocytopenia (HIT)
=====================================================

Clinical prediction rule to estimate the probability of HIT

Reference:
- Lo GK, et al. Evaluation of pretest clinical score (4 T's) for the diagnosis of 
  heparin-induced thrombocytopenia in two clinical settings. J Thromb Haemost. 2006;4(4):759-765.
- Cuker A, et al. American Society of Hematology 2018 guidelines for management of 
  venous thromboembolism: heparin-induced thrombocytopenia. Blood Adv. 2018;2(22):3360-3392.

Four T's Categories:
1. Thrombocytopenia (severity and timing)
2. Timing of platelet count fall
3. Thrombosis or other sequelae
4. oTher causes of thrombocytopenia

Interpretation:
- 6-8 points: High probability (≥50-80% chance of HIT)
- 4-5 points: Intermediate probability (~10-30% chance of HIT)
- 0-3 points: Low probability (<5% chance of HIT)

Clinical Utility:
- High NPV (negative predictive value) for low scores
- Guides HIT antibody testing
- Informs decision to stop heparin and start alternative anticoagulant
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
from components.ui.scoring import render_score_result, render_score_breakdown, render_recommendation_box

from scores.utils.validation import validate_positive



def calculate_4ts_score(
    thrombocytopenia_category: int,
    timing_category: int,
    thrombosis_category: int,
    other_causes_category: int
) -> dict:
    """
    Calculate 4Ts Score for HIT
    
    Args:
        thrombocytopenia_category: Score for thrombocytopenia severity (0-2)
        timing_category: Score for timing of platelet fall (0-2)
        thrombosis_category: Score for thrombosis/sequelae (0-2)
        other_causes_category: Score for other causes (0-2)
    
    Returns:
        Dictionary containing score, probability, recommendations, and details
    """
    score = (thrombocytopenia_category + timing_category + 
             thrombosis_category + other_causes_category)
    
    # Determine probability and recommendations
    if score >= 6:
        probability = "XÁC SUẤT CAO (High Probability)"
        probability_range = "50-80%"
        risk_class = "HIGH"
        color = COLORS["error"]
        icon = "🔴"
        recommendation = """
        **🔴 Xử trí khuyến cáo - HIGH PROBABILITY:**
        
        1. **DỪNG Heparin NGAY LẬP TỨC:**
           - Dừng TẤT CẢ heparin (UFH, LMWH, heparin flush)
           - Kiểm tra tất cả thuốc/dịch truyền có chứa heparin
           - Không dùng heparin cho bất kỳ mục đích nào
        
        2. **Bắt đầu kháng đông thay thế:**
           - **Argatroban** (DTI - direct thrombin inhibitor):
             * Liều: 2 mcg/kg/min IV (giảm 0.5-1 mcg/kg/min nếu suy gan)
             * Theo dõi aPTT (mục tiêu: 1.5-3× baseline)
           - **HOẶC Fondaparinux** (nếu có):
             * <50 kg: 5 mg SC q24h
             * 50-100 kg: 7.5 mg SC q24h
             * >100 kg: 10 mg SC q24h
           - **HOẶC Danaparoid** (nếu có)
        
        3. **XÉT NGHIỆM Xác Định:**
           - **HIT antibody ELISA** (PF4/heparin antibodies)
           - **Serotonin Release Assay (SRA)** - functional assay (gold standard)
           - Đợi kết quả nhưng KHÔNG trì hoãn điều trị
        
        4. **KHÔNG Dùng:**
           - ❌ Warfarin cho đến khi tiểu cầu >150,000/μL (nguy cơ hoại tử da, gangrene)
           - ❌ Truyền tiểu cầu (trừ khi chảy máu đe dọa tính mạng)
        
        5. **Theo dõi:**
           - Đếm tiểu cầu hàng ngày cho đến khi >150,000
           - Đánh giá huyết khối mới (DVT, PE, động mạch)
           - Siêu âm doppler chi dưới nếu chưa làm
        
        6. **Chuyển đổi sang Warfarin:**
           - Chờ tiểu cầu >150,000/μL × 2 ngày
           - Overlap ≥5 ngày + INR 2-3 trong 24h
           - Duy trì kháng đông ≥3 tháng
        """
        
        education = """
        **💡 Diễn giải - High Probability:**
        - 4Ts ≥6 → HIT có khả năng cao (50-80%)
        - PPV ~70-90% (tùy population)
        - PHẢI dừng heparin và bắt đầu kháng đông thay thế NGAY
        - Đợi xét nghiệm xác nhận nhưng KHÔNG trì hoãn điều trị
        - Nguy cơ huyết khối cao (~30-50%) nếu không điều trị
        """
        
    elif score >= 4:
        probability = "XÁC SUẤT TRUNG BÌNH (Intermediate Probability)"
        probability_range = "10-30%"
        risk_class = "INTERMEDIATE"
        color = COLORS["warning"]
        icon = "🟡"
        recommendation = """
        **🟡 Xử trí khuyến cáo - INTERMEDIATE PROBABILITY:**
        
        1. **Đánh giá Kỹ & Quyết định:**
           - Xem xét DỪNG heparin (khuyến cáo mạnh nếu điểm 5)
           - Nếu điểm = 4 → cân nhắc rủi ro/lợi ích
           - Nếu không thể dừng → giám sát sát tiểu cầu
        
        2. **XÉT NGHIỆM Khẩn:**
           - **HIT antibody ELISA** NGAY
           - Nếu ELISA dương tính → làm functional assay (SRA)
           - Quyết định dựa trên kết quả xét nghiệm
        
        3. **Nếu Quyết định Dừng Heparin:**
           - Bắt đầu kháng đông thay thế (argatroban/fondaparinux)
           - Theo dõi tiểu cầu hàng ngày
           - Đánh giá huyết khối
        
        4. **Nếu Tiếp Tục Heparin:**
           - Đếm tiểu cầu ít nhất 2 lần/ngày
           - Nếu tiểu cầu giảm >50% hoặc <100,000 → DỪNG NGAY
           - Theo dõi sát triệu chứng huyết khối
        
        5. **Khi Có Kết quả ELISA:**
           - **Dương tính (OD >1.0):** Xử trí như HIGH probability
           - **Âm tính hoặc yếu (OD <0.4):** Có thể an toàn tiếp tục heparin
           - **Borderline (OD 0.4-1.0):** Cần functional assay
        
        6. **Theo dõi:**
           - Tiểu cầu hàng ngày cho đến khi có kết quả xét nghiệm
           - Tái đánh giá 4Ts nếu có thay đổi lâm sàng
        """
        
        education = """
        **💡 Diễn giải - Intermediate Probability:**
        - 4Ts = 4-5 → HIT có thể có (10-30%)
        - Không thể loại trừ hoàn toàn
        - Cần xét nghiệm ELISA để quyết định
        - Nếu ELISA dương tính → xử trí như HIGH
        - Nếu ELISA âm tính → an toàn tiếp tục heparin
        """
        
    else:  # score 0-3
        probability = "XÁC SUẤT THẤP (Low Probability)"
        probability_range = "<5%"
        risk_class = "LOW"
        color = COLORS["success"]
        icon = "🟢"
        recommendation = """
        **🟢 Xử trí khuyến cáo - LOW PROBABILITY:**
        
        1. **Đánh giá:**
           - HIT rất ít có khả năng (NPV ~95-99%)
           - Có thể AN TOÀN tiếp tục heparin
           - Tìm nguyên nhân KHÁC của giảm tiểu cầu
        
        2. **Xét nghiệm:**
           - Xét nghiệm HIT antibody KHÔNG khuyến cáo (trừ khi nghi ngờ đặc biệt)
           - Nếu vẫn lo lắng → có thể làm ELISA (thường âm tính)
           - Tìm nguyên nhân khác: sepsis, thuốc, DIC, etc.
        
        3. **Nguyên nhân Khác Cần Xem Xét:**
           - **Sepsis/Infection** (phổ biến nhất)
           - **Thuốc khác:** Vancomycin, linezolid, valproate, H2-blockers, etc.
           - **DIC** (Disseminated Intravascular Coagulation)
           - **TTP/HUS** (Thrombotic Thrombocytopenic Purpura)
           - **Giảm tiểu cầu sau phẫu thuật** (dilutional, consumption)
           - **ITP** (Immune Thrombocytopenic Purpura)
           - **Giảm tiểu cầu do gan/lách to**
        
        4. **Theo dõi:**
           - Đếm tiểu cầu theo clinical indication
           - Tái đánh giá 4Ts nếu có thay đổi lâm sàng
           - Nếu tiểu cầu tiếp tục giảm → xem xét lại
        
        5. **Lưu ý:**
           - 4Ts <4 có NPV rất cao → an toàn loại trừ HIT
           - NHƯNG nếu có thay đổi lâm sàng → tính lại 4Ts
           - Không dừng heparin chỉ dựa trên điểm thấp
        """
        
        education = """
        **💡 Diễn giải - Low Probability:**
        - 4Ts ≤3 → HIT rất ít có khả năng (<5%)
        - NPV ~95-99% → an toàn loại trừ
        - Không cần xét nghiệm HIT antibody
        - Có thể tiếp tục heparin an toàn
        - Tìm nguyên nhân khác của giảm tiểu cầu
        """
    
    # Map categories to descriptions
    category_descriptions = {
        'thrombocytopenia': [
            "0 điểm: Giảm tiểu cầu <30% hoặc nadir <10,000/μL",
            "1 điểm: Giảm 30-50% hoặc nadir 10,000-19,000/μL",
            "2 điểm: Giảm >50% và nadir ≥20,000/μL"
        ],
        'timing': [
            "0 điểm: ≤4 ngày không tiếp xúc heparin gần đây, hoặc không rõ, hoặc >100 ngày",
            "1 điểm: >10 ngày HOẶC ≤1 ngày với tiếp xúc heparin trong 30-100 ngày",
            "2 điểm: 5-10 ngày HOẶC ≤1 ngày với tiếp xúc heparin trong 30 ngày"
        ],
        'thrombosis': [
            "0 điểm: Không có huyết khối, hoại tử da, phản ứng cấp",
            "1 điểm: Huyết khối tiến triển/tái phát, hoặc tổn thương đỏ da không hoại tử, hoặc nghi ngờ huyết khối",
            "2 điểm: Huyết khối MỚI xác định, hoặc hoại tử da, hoặc phản ứng cấp sau bolus heparin"
        ],
        'other_causes': [
            "0 điểm: Có nguyên nhân rõ ràng khác",
            "1 điểm: Có thể có nguyên nhân khác",
            "2 điểm: Không có nguyên nhân nào khác rõ ràng"
        ]
    }
    
    selected_descriptions = [
        category_descriptions['thrombocytopenia'][thrombocytopenia_category],
        category_descriptions['timing'][timing_category],
        category_descriptions['thrombosis'][thrombosis_category],
        category_descriptions['other_causes'][other_causes_category]
    ]
    
    return {
        'score': score,
        'probability': probability,
        'probability_range': probability_range,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'education': education,
        'color': color,
        'icon': icon,
        'details': selected_descriptions
    }


def render():
    """Render 4Ts Score calculator in Streamlit"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'four_ts':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', '4Ts Score')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h3 style='text-align: center; color: {COLORS['success']};'>🩸 4Ts Score - Heparin-Induced Thrombocytopenia (HIT)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><em>Đánh giá xác suất giảm tiểu cầu do heparin</em></p>", unsafe_allow_html=True)
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **4Ts Score** là thang điểm lâm sàng để:
        - Đánh giá xác suất tiền test của HIT (Heparin-Induced Thrombocytopenia)
        - Hướng dẫn quyết định dừng heparin và xét nghiệm
        - Phân tầng nguy cơ trước khi có kết quả xét nghiệm
        
        **HIT** là biến chứng nghiêm trọng:
        - Tỷ lệ: 0.1-1% (UFH), 0.01-0.1% (LMWH)
        - Nguy cơ huyết khối: 30-50% nếu không điều trị
        - Tử vong: ~10-20%
        
        ### 🎯 4 Thành phần (4 T's)
        
        1. **T**hrombocytopenia: Mức độ giảm tiểu cầu
        2. **T**iming: Thời gian xuất hiện giảm tiểu cầu
        3. **T**hrombosis: Huyết khối hoặc biến chứng khác
        4. o**T**her causes: Các nguyên nhân khác
        
        ### 📊 Phân tầng Nguy cơ
        
        | Điểm 4Ts | Phân loại | Xác Suất HIT | Xử trí|
        |----------|-----------|--------------|--------|
        | 6-8 | High | 50-80% | Dừng heparin NGAY, kháng đông thay thế |
        | 4-5 | Intermediate | 10-30% | Cân nhắc dừng, xét nghiệm ELISA |
        | 0-3 | Low | <5% | An toàn tiếp tục, tìm nguyên nhân khác |
        
        ### ⚠️ Lưu ý quan trọng
        
        - **4Ts HIGH (≥6):** DỪNG heparin NGAY + bắt đầu alternative anticoagulant
        - **KHÔNG truyền tiểu cầu** (trừ chảy máu đe dọa tính mạng)
        - **KHÔNG dùng warfarin** cho đến khi tiểu cầu >150,000/μL
        - **Functional assay (SRA)** là gold standard nhưng mất thời gian
        
        ### 📚 Tài liệu tham khảo
        
        - Lo GK, et al. *J Thromb Haemost* 2006;4:759-765
        - Cuker A, et al. *Blood Adv* 2018;2:3360-3392
        - ASH 2018 Guidelines for Management of HIT
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập thông tin 4 thành phần")
    
    # 1. Thrombocytopenia
    st.markdown("#### 1️⃣ Thrombocytopenia - Mức độ giảm tiểu cầu")
    
    # Helper for Platelet Count
    with st.expander("🧮 Hỗ trợ tính điểm (Nhập số lượng tiểu cầu)"):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            baseline_plt = st.number_input("Tiểu cầu nền (x10⁹/L hoặc /μL)", min_value=0.0, step=1.0, key="4ts_baseline")
        with col_p2:
            nadir_plt = st.number_input("Tiểu cầu thấp nhất (Nadir)", min_value=0.0, step=1.0, key="4ts_nadir")
            
        suggested_thrombo_score = None
        
        if baseline_plt > 0 and nadir_plt >= 0:
            # Validate
            is_valid_base, msg_base = validate_positive(baseline_plt, "Tiểu cầu nền")
            is_valid_nadir, msg_nadir = validate_positive(nadir_plt, "Tiểu cầu thấp nhất")
            
            if is_valid_base and is_valid_nadir:
                drop_percent = ((baseline_plt - nadir_plt) / baseline_plt) * 100
                st.info(f"📉 Mức giảm: {drop_percent:.1f}% (Nadir: {nadir_plt})")
                
                # Logic calculation
                # 2 points: >50% drop AND nadir >= 20
                if drop_percent > 50 and nadir_plt >= 20: # Assuming unit consistency, usually cells/uL. If x10^9/L, 20 is Low. 
                    # Note: 20 x 10^9/L = 20,000 /uL. User needs to be consistent. 
                    # The UI says "x10^9/L hoặc /μL". 
                    # 20 k/uL = 20 x 10^9/L.
                    # 10 k/uL = 10 x 10^9/L.
                    # So checking >= 20 works for both if the user enters 20 for 20k or 20 for 20x10^9.
                    # BUT if user enters 20000, 20 is tiny.
                    # Let's assume input is consistent. 10,000 is a large number. 
                    # If input > 1000, assumes /uL. If < 1000, assumes x10^9/L.
                    # Normalizing to x10^9/L for threshold check?
                    # Thresholds are 10, 20.
                    # 20,000 is the threshold.
                    
                    # Heuristic normalization
                    nadir_check = nadir_plt
                    if nadir_plt > 1000: # User entered /uL (e.g. 150000)
                         nadir_check = nadir_plt / 1000 # Convert to k/uL (which is same magnitude as x10^9/L roughly?)
                         # Wait, standard is 150 x 10^9/L = 150,000 /uL.
                         # Code uses "20,000/uL". 
                         # So if input is 20 (x10^9/L), that is 20,000.
                         # If input is 20000, that is 20,000.
                         pass
                    
                    # Actually typically scores use absolute numbers like 20 and 100.
                    # Let's assume user enters roughly in the range of the thresholds or usual counts.
                    # Protocol implies 20,000. 
                    # If user enters 20, they likely mean 20k? No, 20 G/L. 20 G/L = 20,000 /mm3.
                    # The validation logic in text says "20,000/uL".
                    # I will normalize roughly.
                    
                    val_to_check = nadir_plt
                    if nadir_plt < 500: # Likely 10^9/L units (e.g., 20) -> Convert to absolute 20000
                        val_to_check = nadir_plt * 1000 
                    
                    if drop_percent > 50 and val_to_check >= 20000:
                        suggested_thrombo_score = 2
                        st.success("✅ Gợi ý: **2 điểm** (Giảm >50% và Nadir ≥20,000)")
                    elif (30 <= drop_percent <= 50) or (10000 <= val_to_check <= 19000):
                         suggested_thrombo_score = 1
                         st.success("✅ Gợi ý: **1 điểm** (Giảm 30-50% hoặc Nadir 10-19k)")
                    elif drop_percent < 30 or val_to_check < 10000:
                         suggested_thrombo_score = 0
                         st.success("✅ Gợi ý: **0 điểm** (Giảm <30% hoặc Nadir <10k)")
                    
    # Auto-select if suggested
    default_thrombo = 2
    if '4ts_thrombo_score_auto' in st.session_state and st.session_state['4ts_thrombo_score_auto'] is not None:
         default_thrombo = st.session_state['4ts_thrombo_score_auto']
    
    if suggested_thrombo_score is not None:
         # Update session state slightly hacky to set radio default but simple works too
         pass 

    thrombocytopenia_category = st.radio(

        "Chọn mức độ giảm tiểu cầu:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: Giảm >50% VÀ nadir ≥20,000/μL",
            "1 điểm: Giảm 30-50% HOẶC nadir 10,000-19,000/μL",
            "0 điểm: Giảm <30% HOẶC nadir <10,000/μL"
        ][2-x],
        key="thrombocytopenia",
        help="% giảm = (Tiểu cầu cao nhất - Tiểu cầu thấp nhất) / Tiểu cầu cao nhất × 100%"
    )
    
    st.divider()
    
    # 2. Timing
    st.markdown("#### 2️⃣ Timing - Thời gian xuất hiện giảm tiểu cầu")
    st.caption("Tính từ khi BẮT ĐẦU heparin đến khi tiểu cầu giảm")
    
    timing_category = st.radio(
        "Chọn thời gian xuất hiện:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: 5-10 ngày SAU khi bắt đầu heparin\nHOẶC ≤1 ngày (nếu có tiếp xúc heparin trong 30 ngày gần đây)",
            "1 điểm: >10 ngày sau khi bắt đầu heparin\nHOẶC ≤1 ngày (nếu có tiếp xúc heparin trong 30-100 ngày trước)",
            "0 điểm: ≤4 ngày (không có tiếp xúc heparin gần đây)\nHOẶC >100 ngày\nHOẶC không rõ thời gian"
        ][2-x],
        key="timing",
        help="Thời gian điển hình của HIT: 5-10 ngày. Nếu đã tiếp xúc heparin trước đó → có thể xuất hiện sớm hơn (<24h)"
    )
    
    st.divider()
    
    # 3. Thrombosis
    st.markdown("#### 3️⃣ Thrombosis - Huyết khối hoặc biến chứng khác")
    thrombosis_category = st.radio(
        "Chọn tình trạng huyết khối/biến chứng:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: Huyết khối MỚI được xác định (DVT, PE, động mạch)\nHOẶC hoại tử da tại vị trí tiêm\nHOẶC phản ứng cấp tính sau bolus heparin",
            "1 điểm: Huyết khối tiến triển/tái phát\nHOẶC tổn thương da đỏ (chưa hoại tử)\nHOẶC nghi ngờ huyết khối chưa xác định",
            "0 điểm: KHÔNG có huyết khối, hoại tử da, hoặc phản ứng cấp"
        ][2-x],
        key="thrombosis",
        help="HIT thường đi kèm huyết khối (30-50%). Huyết khối có thể xuất hiện TRƯỚC khi tiểu cầu giảm rõ rệt."
    )
    
    st.divider()
    
    # 4. Other causes
    st.markdown("#### 4️⃣ oTher Causes - Các nguyên nhân khác")
    st.caption("Đánh giá khả năng có nguyên nhân KHÁC gây giảm tiểu cầu")
    
    other_causes_category = st.radio(
        "Đánh giá các nguyên nhân khác:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: KHÔNG có nguyên nhân nào khác rõ ràng",
            "1 điểm: CÓ THỂ có nguyên nhân khác (sepsis, thuốc, DIC, etc.)",
            "0 điểm: CÓ nguyên nhân RÕ RÀNG khác (ví dụ: sepsis nặng, phẫu thuật lớn, thuốc gây giảm TC rõ)"
        ][2-x],
        key="other_causes",
        help="Nguyên nhân khác: Sepsis, thuốc (vancomycin, linezolid), DIC, TTP/HUS, phẫu thuật, dilutional"
    )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính toán 4Ts Score", type="primary", use_container_width=True):
        result = calculate_4ts_score(
            thrombocytopenia_category=thrombocytopenia_category,
            timing_category=timing_category,
            thrombosis_category=thrombosis_category,
            other_causes_category=other_causes_category
        )
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Use render_score_result for main score display
        render_score_result(
            title="4Ts Score",
            score=result['score'],
            interpretation=result['probability'],
            mortality=f"Xác suất HIT: {result['probability_range']}",
            color=result['color'],
            icon=result['icon'],
            size="large"
        )
        
        # Use render_score_breakdown for component scores
        render_score_breakdown(
            title="Điểm Từng Thành phần",
            subscores={
                "1️⃣ Thrombocytopenia": thrombocytopenia_category,
                "2️⃣ Timing": timing_category,
                "3️⃣ Thrombosis": thrombosis_category,
                "4️⃣ oTher causes": other_causes_category
            },
            total_score=result['score']
        )
        
        # Details
        with st.expander("📋 Chi tiết tính điểm", expanded=True):
            st.markdown("**Các thành phần đã chọn:**")
            for i, detail in enumerate(result['details'], 1):
                st.markdown(f"{i}. {detail}")
        
        # Recommendations
        render_recommendation_box(
            title="Khuyến cáo Xử trí 4Ts",
            content=result['recommendation'],
            type="error" if result['risk_class'] == "HIGH" else "warning" if result['risk_class'] == "INTERMEDIATE" else "success",
            icon=result['icon']
        )
        
        # Additional clinical context
        if result['risk_class'] in ['HIGH', 'INTERMEDIATE']:
            render_recommendation_box(
                title="CẢNH BÁO QUAN TRỌNG",
                content="""
                - HIT là cấp cứu huyết học - có thể gây huyết khối đe dọa tính mạng/chi
                - Nếu 4Ts ≥4 → cân nhắc DỪNG heparin và xét nghiệm NGAY
                - KHÔNG truyền tiểu cầu (có thể làm tăng nguy cơ huyết khối)
                - KHÔNG dùng warfarin khi tiểu cầu thấp (nguy cơ hoại tử da, gangrene tứ chi)
                """,
                type="error",
                icon="🚨"
            )
        
        st.info("""
        **🔬 Xét nghiệm HIT:**
        
        1. **ELISA (PF4/Heparin Antibodies):**
           - Nhanh (vài giờ), nhạy cao
           - OD >1.0: Dương tính mạnh
           - OD 0.4-1.0: Borderline (cần functional assay)
           - OD <0.4: Âm tính
        
        2. **Functional Assay (SRA - Serotonin Release Assay):**
           - Gold standard, đặc hiệu cao
           - Mất 1-3 ngày
           - Xác nhận chẩn đoán cuối cùng
        
        **Chiến Lược:**
        - 4Ts ≥6 → Dừng heparin NGAY + bắt đầu alternative (đợi ELISA để xác nhận)
        - 4Ts 4-5 → Làm ELISA, quyết định dựa trên kết quả
        - 4Ts ≤3 → Không cần xét nghiệm, tìm nguyên nhân khác
        """)
        
        # Save to session state
        st.session_state['four_ts_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Lưu ý y khoa:**
        - Thang điểm 4Ts là công cụ hỗ trợ, cần kết hợp với xét nghiệm và đánh giá lâm sàng
        - Quyết định dừng heparin và điều trị thay thế thuộc về bác sĩ điều trị
        - Khi nghi ngờ HIT → tư vấn huyết học ngay
        """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Thrombocytopenia": thrombocytopenia_category,
            "Timing": timing_category,
            "Thrombosis": thrombosis_category,
            "Other Causes": other_causes_category
        }
        
        results_dict = {
            "4Ts Score": f"{result['score']}/8",
            "Probability": result['probability'],
            "Risk Class": result['risk_class']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="4Ts Score",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="4Ts Score"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="four_ts",
            calculator_name="4Ts Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="four_ts",
            calculator_name="4Ts Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="four_ts", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="four_ts",
            calculator_name="4Ts Score",
            category="Huyết học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Quick reference
    with st.expander("📖 Bảng tham khảo Nhanh - Alternative Anticoagulants"):
        st.markdown("""
        ### Thuốc kháng đông thay thế cho HIT
        
        #### 1. Argatroban (DTI - Direct Thrombin Inhibitor)
        - **Liều:** 2 mcg/kg/min IV continuous
          - Suy gan: 0.5-1 mcg/kg/min
        - **Theo dõi:** aPTT (mục tiêu 1.5-3× baseline, thường 60-80s)
        - **Ưu điểm:** Phổ biến, bài tiết qua gan
        - **Nhược điểm:** Tăng INR → khó chuyển warfarin
        
        #### 2. Fondaparinux (Factor Xa Inhibitor)
        - **Liều:**
          - <50 kg: 5 mg SC q24h
          - 50-100 kg: 7.5 mg SC q24h
          - >100 kg: 10 mg SC q24h
        - **Ưu điểm:** SC, không cần monitor
        - **Nhược điểm:** Bài tiết thận (tránh nếu CrCl <30)
        
        #### 3. Danaparoid (nếu có)
        - **Liều:** 2,500 U IV bolus, sau đó 400 U/h × 4h, sau đó 300 U/h × 4h, sau đó 200 U/h
        - **Nhược điểm:** Khó kiếm, bài tiết thận
        
        #### 4. DOACs (Direct Oral Anticoagulants) - OFF-LABEL
        - **Rivaroxaban, Apixaban:** Một số evidence nhưng chưa approved chính thức
        - Có thể xem xét nếu không có alternative khác
        
        ### Chuyển đổi sang Warfarin
        
        1. **Chờ tiểu cầu >150,000/μL** × 2 ngày liên tiếp
        2. **Bắt đầu warfarin:** 5 mg/ngày (hoặc liều thấp hơn nếu người già)
        3. **Overlap ≥5 ngày** + INR 2-3 trong 24h
        4. **Duy trì kháng đông:** ≥3 tháng (6-12 tháng nếu có huyết khối)
        
        ### Lưu ý quan trọng
        
        - ❌ **KHÔNG dùng warfarin khi tiểu cầu thấp** → nguy cơ warfarin-induced limb gangrene
        - ❌ **KHÔNG truyền tiểu cầu** (trừ chảy máu đe dọa tính mạng)
        - ✅ **Theo dõi tiểu cầu hàng ngày** cho đến khi >150,000/μL
        - ✅ **Đánh giá huyết khối** (siêu âm doppler chi dưới, CT PE nếu cần)
        """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("4Ts Score")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

