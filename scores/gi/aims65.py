"""
AIMS65 Score
Đánh giá nguy cơ tử vong trong xuất huyết tiêu hóa trên

AIMS65 là thang điểm đơn giản để dự đoán tử vong ở bệnh nhân UGIB.
Mỗi yếu tố = 1 điểm, tổng điểm 0-5.

Reference:
Saltzman JR, Tabak YP, Hyett BH, Sun X, Travis AC, Johannes RS.
A simple risk score accurately predicts in-hospital mortality, length of stay, and cost in acute upper GI bleeding.
Gastrointest Endosc. 2011 Dec;74(6):1215-24.
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def calculate_aims65(albumin, inr, mental_status, sbp, age):
    """Calculate AIMS65 Score"""
    score = 0
    
    # Albumin < 3.0 g/dL
    if albumin < 3.0:
        score += 1
    
    # INR > 1.5
    if inr > 1.5:
        score += 1
    
    # Mental status altered
    if mental_status:
        score += 1
    
    # Systolic BP ≤ 90 mmHg
    if sbp <= 90:
        score += 1
    
    # Age > 65
    if age > 65:
        score += 1
    
    return score


def render():
    """Render AIMS65 Score Calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 AIMS65 Score</h3>
    """, unsafe_allow_html=True)
    st.caption("**Đánh giá nguy cơ tử vong trong xuất huyết tiêu hóa trên**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'aims65':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    **AIMS65 Score** là thang điểm đơn giản để dự đoán tử vong ở bệnh nhân 
    xuất huyết tiêu hóa trên (UGIB).
    
    **Ứng dụng:**
    - Dự đoán tử vong trong bệnh viện
    - Đánh giá độ nặng bệnh
    - Hỗ trợ quyết định điều trị
    - Dự đoán chi phí và thời gian nằm viện
    
    **AIMS65 = 5 yếu tố (mỗi yếu tố = 1 điểm):**
    - **A**lbumin < 3.0 g/dL
    - **I**NR > 1.5
    - **M**ental status altered (rối loạn ý thức)
    - **S**ystolic BP ≤ 90 mmHg
    - **65** = Age > 65 tuổi
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin bệnh nhân")
        
        # Age
        age = st.number_input(
            "**Tuổi:**",
            min_value=0,
            max_value=120,
            value=60,
            step=1,
            help="Tuổi > 65 = +1 điểm"
        )
        
        st.markdown("---")
        st.markdown("### 🔬 Xét nghiệm")
        
        # Albumin
        albumin = st.number_input(
            "**Albumin (g/dL):**",
            min_value=1.0,
            max_value=6.0,
            value=3.5,
            step=0.1,
            format="%.1f",
            help="Bình thường: 3.5-5.0 g/dL. < 3.0 g/dL = +1 điểm"
        )
        st.caption(f"≈ {round(albumin * 10)} g/L")
        
        # INR
        inr = st.number_input(
            "**INR (International Normalized Ratio):**",
            min_value=0.8,
            max_value=10.0,
            value=1.2,
            step=0.1,
            format="%.2f",
            help="Bình thường: 0.9-1.2. > 1.5 = +1 điểm"
        )
        
        st.markdown("---")
        st.markdown("### 🩺 Sinh hiệu & Lâm sàng")
        
        # Systolic BP
        sbp = st.number_input(
            "**Huyết áp tâm thu (mmHg):**",
            min_value=50,
            max_value=250,
            value=120,
            step=5,
            help="SBP ≤ 90 mmHg = +1 điểm"
        )
        
        # Mental status
        mental_status = st.checkbox(
            "**Rối loạn ý thức (Altered Mental Status)**",
            help="Rối loạn ý thức = +1 điểm"
        )
        
        if mental_status:
            st.caption("⚠️ Rối loạn ý thức: Lơ mơ, kích động, không hợp tác, hôn mê")
        
        st.markdown("---")
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="aims65",
            calculator_name="AIMS65 Score",
            category="Tiêu Hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    if st.button("🧮 Tính AIMS65 Score", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 0, 120)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            is_valid_alb, alb_error = validate_lab_value(albumin, "Albumin (g/dL)", 1.0, 6.0)
            if not is_valid_alb:
                validation_errors.append(alb_error)
            
            is_valid_inr, inr_error = validate_lab_value(inr, "INR", 0.8, 10.0)
            if not is_valid_inr:
                validation_errors.append(inr_error)
            
            is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
            
            if validation_errors:
                render_validation_errors(validation_errors)
            
            # Calculate score
            score = calculate_aims65(albumin, inr, mental_status, sbp, age)
            
            # Build breakdown of component scores
            component_scores = {}
            if albumin < 3.0:
                component_scores["Albumin <3.0"] = 1
            if inr > 1.5:
                component_scores["INR >1.5"] = 1
            if mental_status:
                component_scores["Rối loạn ý thức"] = 1
            if sbp <= 90:
                component_scores["HA tâm thu ≤90"] = 1
            if age > 65:
                component_scores["Tuổi >65"] = 1
            
            # Determine mortality risk based on literature
            # Saltzman et al. Gastrointest Endosc. 2011
            if score == 0:
                mortality = "<0.3%"
                risk = "RẤT THẤP"
                color = COLORS["success"]
                length_of_stay = "2-3 ngày"
                cost = "Thấp"
            elif score == 1:
                mortality = "~1%"
                risk = "THẤP"
                color = COLORS["success"]
                length_of_stay = "3-4 ngày"
                cost = "Trung bình thấp"
            elif score == 2:
                mortality = "~2-3%"
                risk = "TRUNG BÌNH"
                color = COLORS["primary"]
                length_of_stay = "4-5 ngày"
                cost = "Trung bình"
            elif score == 3:
                mortality = "~5-8%"
                risk = "TRUNG BÌNH CAO"
                color = COLORS["warning"]
                length_of_stay = "5-7 ngày"
                cost = "Trung bình cao"
            elif score == 4:
                mortality = "~15-20%"
                risk = "CAO"
                color = COLORS["error"]
                length_of_stay = "7-10 ngày"
                cost = "Cao"
            else:  # score == 5
                mortality = ">25%"
                risk = "RẤT CAO"
                color = COLORS["error"]
                length_of_stay = ">10 ngày"
                cost = "Rất cao"
            
            # Map color names to hex
            icon_map = {
                COLORS["success"]: "✅",
                COLORS["primary"]: "💡",
                COLORS["warning"]: "⚠️",
                COLORS["error"]: "🚨"
            }
            score_color = color
            score_icon = icon_map[color]
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="AIMS65 Score",
                    score=score,
                    interpretation=f"Nguy cơ {risk}",
                    mortality=f"Tử vong: {mortality}",
                    color=score_color,
                    icon=score_icon,
                    size="large"
                )
                
                st.markdown(f"""
                **Thời gian nằm viện:** {length_of_stay}
                
                **Chi phí:** {cost}
                """)
            
            # Use render_score_breakdown for component scores
            if component_scores:
                render_score_breakdown(
                    title="Tiêu chí AIMS65",
                    subscores=component_scores,
                    total_score=score
                )
            
            st.markdown("---")
            st.markdown("### 💊 KHUYẾN CÁO XỬ TRÍ")
            
            if score <= 1:
                st.success(f"""
                **🟢 AIMS65 = {score} - NGUY CƠ THẤP**
                
                **Tiên lượng:**
                - Tử vong: {mortality}
                - Thời gian nằm viện: {length_of_stay}
                - Chi phí: {cost}
                
                **Khuyến nghị:**
                
                1. **Nhập viện khoa thường:**
                   - Không cần ICU
                   - Theo dõi sát sinh hiệu
                
                2. **Điều trị ban đầu:**
                   - **PPI IV:** Pantoprazole 80mg IV bolus → 8mg/h × 72h
                   - **IV fluid:** Resuscitation nếu cần
                   - **Transfusion:** Nếu Hgb <7-8 g/dL
                
                3. **Nội soi:**
                   - Trong 24h (không khẩn cấp)
                   - Pre-endoscopy: Erythromycin 250mg IV nếu cần
                
                4. **Theo dõi:**
                   - Vital signs q4-6h
                   - CBC lặp lại sau 6-12h
                   - Đánh giá lại cho xuất viện nếu ổn định
                
                5. **Xuất viện:**
                   - PPI PO: Omeprazole 40mg BID × 14 ngày
                   - Tái khám sau 1 tuần
                   - H. pylori test & treat
                
                **Tiên lượng:** Tốt. Hầu hết bệnh nhân hồi phục tốt.
                """)
            
            elif score == 2:
                st.info(f"""
                **🟡 AIMS65 = {score} - NGUY CƠ TRUNG BÌNH**
                
                **Tiên lượng:**
                - Tử vong: {mortality}
                - Thời gian nằm viện: {length_of_stay}
                - Chi phí: {cost}
                
                **Khuyến nghị:**
                
                1. **NHẬP VIỆN - Khoa Tiêu Hóa:**
                   - Theo dõi sát
                   - Cân nhắc High-Dependency Unit nếu không ổn định
                
                2. **Hồi sức ban đầu:**
                   - **IV access:** 2 đường truyền cỡ lớn (18G)
                   - **IV fluid:** Crystalloid để duy trì BP
                   - **PPI IV:** Pantoprazole 80mg bolus → 8mg/h × 72h
                   - **NPO** ban đầu
                   - **Transfusion:** Nếu Hgb <7-8 g/dL
                     * Mục tiêu: Hgb >7 g/dL (hoặc >8 nếu CAD)
                
                3. **Nội soi:**
                   - **Nội soi trong 24h**
                   - Pre-endoscopy: Erythromycin 250mg IV
                
                4. **Theo dõi:**
                   - Vital signs q2-4h
                   - CBC mỗi 6-12h
                   - Đánh giá lại AIMS65 sau resuscitation
                
                5. **Can thiệp nội soi nếu cần:**
                   - **Variceal bleeding:** Band ligation, sclerotherapy
                   - **Peptic ulcer:** Epinephrine + (thermal/clip)
                
                6. **Điều trị sau nội soi:**
                   - PPI IV × 72h → chuyển PO
                   - H. pylori test & treat
                   - Điều trị theo nguyên nhân
                
                **Tiên lượng:** Trung bình. Phần lớn hồi phục tốt với điều trị.
                """)
            
            elif score >= 3:
                st.error(f"""
                **🔴 AIMS65 = {score} - NGUY CƠ CAO** 🚨
                
                **Tiên lượng:**
                - Tử vong: {mortality}
                - Thời gian nằm viện: {length_of_stay}
                - Chi phí: {cost}
                
                **Khuyến nghị:**
                
                1. **KHẨN CẤP - ICU hoặc High-Dependency Unit:**
                   - Monitoring liên tục
                   - Sẵn sàng can thiệp
                   - Cân nhắc intubation nếu altered mental status nặng
                
                2. **Hồi sức tích cực:**
                   
                   **ABC - Airway, Breathing, Circulation:**
                   - **Airway:** Cân nhắc intubation nếu:
                     * Altered mental status nặng
                     * Massive hematemesis
                     * Nguy cơ aspiration cao
                   - **Breathing:** O₂ để duy trì SpO₂ >94%
                   - **Circulation:**
                     * **2 IV lines 18G** (hoặc central line)
                     * **Crystalloid:** Bolus 500ml-1L nhanh
                     * Mục tiêu: MAP >65 mmHg, UO >0.5ml/kg/h
                   
                   **Truyền máu:**
                   - **PRBC:** Nếu Hgb <7 g/dL (hoặc <8 nếu CAD/instability)
                   - **Mục tiêu:** Hgb 7-9 g/dL
                   - **FFP:** Nếu INR >1.5-2.0 và chảy máu active
                   - **Platelet:** Nếu <50,000 và chảy máu active
                   
                   **PPI liều cao:**
                   - **Pantoprazole 80mg IV bolus** → 8mg/h infusion
                   - Bắt đầu NGAY, trước nội soi
                   
                   **Nếu nghi variceal bleeding:**
                   - **Octreotide:** 50µg IV bolus → 50µg/h infusion
                   - Hoặc Terlipressin 2mg IV q4h
                   - **Antibiotic prophylaxis:** Ceftriaxone 1g IV q24h
                   - **Vitamin K:** 10mg IV (nếu bệnh gan)
                
                3. **Nội soi KHẨN CẤP:**
                   - **Trong 12h** (hoặc sớm hơn nếu không ổn định)
                   - Pre-procedure:
                     * NGT aspiration (nếu cần)
                     * Erythromycin 250mg IV
                     * Consent + giải thích nguy cơ
                   - **Sẵn sàng can thiệp:**
                     * Endoscopic hemostasis (injection, thermal, clip)
                     * Band ligation/sclerotherapy (varix)
                
                4. **Nếu thất bại nội soi:**
                   - **Balloon tamponade** (Sengstaken-Blakemore) - tạm thời
                   - **Interventional radiology:** Embolization
                   - **TIPS** (nếu variceal bleeding không kiểm soát)
                   - **Phẫu thuật** (last resort)
                
                5. **Theo dõi sau can thiệp:**
                   - ICU × 24-48h
                   - Vital signs liên tục
                   - CBC q4-6h
                   - NGT output monitoring
                   - PPI IV × 72h
                
                6. **Prophylaxis thứ phát:**
                   - **Nếu variceal bleeding:**
                     * Beta-blocker (Propranolol, Carvedilol)
                     * Band ligation mỗi 2-4 tuần đến obliteration
                   - **Nếu peptic ulcer:**
                     * PPI dài hạn
                     * H. pylori eradication
                     * Tránh NSAIDs
                
                **Tiên lượng:** Xấu. Cần can thiệp tích cực và theo dõi sát.
                Nguy cơ tái chảy máu và tử vong cao.
                """)
            
            # Score breakdown
            st.markdown("---")
            with st.expander("📊 Chi tiết điểm số"):
                st.markdown(f"""
                **AIMS65 Score = {score}**
                
                **Thành phần:**
                - **A**lbumin: {albumin:.1f} g/dL {"(< 3.0 → +1 điểm)" if albumin < 3.0 else "(≥ 3.0 → 0 điểm)"}
                - **I**NR: {inr:.2f} {"(> 1.5 → +1 điểm)" if inr > 1.5 else "(≤ 1.5 → 0 điểm)"}
                - **M**ental status: {"Rối loạn ý thức (+1 điểm)" if mental_status else "Bình thường (0 điểm)"}
                - **S**ystolic BP: {sbp} mmHg {"(≤ 90 → +1 điểm)" if sbp <= 90 else "(> 90 → 0 điểm)"}
                - **65** = Age: {age} tuổi {"(> 65 → +1 điểm)" if age > 65 else "(≤ 65 → 0 điểm)"}
                """)
            
            with st.expander("📈 Bảng Chấm Điểm AIMS65"):
                st.markdown("""
                | Yếu tố | Tiêu chuẩn | Điểm |
                |--------|-----------|------|
                | **A**lbumin | < 3.0 g/dL | 1 |
                | | ≥ 3.0 g/dL | 0 |
                | **I**NR | > 1.5 | 1 |
                | | ≤ 1.5 | 0 |
                | **M**ental status | Rối loạn ý thức | 1 |
                | | Bình thường | 0 |
                | **S**ystolic BP | ≤ 90 mmHg | 1 |
                | | > 90 mmHg | 0 |
                | **65** = Age | > 65 tuổi | 1 |
                | | ≤ 65 tuổi | 0 |
                
                **Tổng điểm: 0-5**
                
                **Nguy cơ tử vong:**
                - **0 điểm:** <0.3%
                - **1 điểm:** ~1%
                - **2 điểm:** ~2-3%
                - **3 điểm:** ~5-8%
                - **4 điểm:** ~15-20%
                - **5 điểm:** >25%
                """)
            
            with st.expander("🔄 AIMS65 vs GBS vs Rockall"):
                st.markdown("""
                **So sánh các thang điểm UGIB:**
                
                | Đặc điểm | AIMS65 | Glasgow-Blatchford | Rockall |
                |----------|--------|-------------------|---------|
                | **Mục đích chính** | Tử vong | Can thiệp/Discharge | Tử vong |
                | **Thời điểm** | Pre-endoscopy | Pre-endoscopy | Pre + Post |
                | **Số yếu tố** | 5 | 8 | 5-8 |
                | **Điểm tối đa** | 5 | 23 | 11 |
                | **Đơn giản** | ✅✅ Rất đơn giản | ✅ Đơn giản | ❌ Phức tạp hơn |
                | **Dự đoán tử vong** | ✅✅ Tốt | ✅ Khá | ✅✅ Tốt |
                | **Dự đoán can thiệp** | ❌ Kém | ✅✅ Tốt | ❌ Kém |
                | **Discharge decision** | ❌ Không dùng | ✅✅ Tốt (GBS=0) | ❌ Không dùng |
                | **Chi phí/Thời gian** | ✅✅ Dự đoán tốt | ❌ Không | ❌ Không |
                
                **Khuyến nghị sử dụng:**
                - **AIMS65:** Dự đoán tử vong, đánh giá độ nặng, chi phí
                - **GBS:** Quyết định discharge (GBS=0), dự đoán can thiệp
                - **Rockall:** Dự đoán tử vong sau nội soi
                - **Kết hợp:** Dùng cả 3 để đánh giá toàn diện
                """)
            
            # Prepare inputs and results for export/history
            inputs_dict = {
                "Age": str(age),
                "Albumin": f"{albumin:.1f} g/dL",
                "INR": f"{inr:.2f}",
                "Mental Status": "Rối loạn ý thức" if mental_status else "Bình thường",
                "Systolic BP": f"{sbp} mmHg"
            }
            
            results_dict = {
                "AIMS65 Score": f"{score}/5",
                "Risk": risk,
                "Mortality": mortality,
                "Length of Stay": length_of_stay,
                "Cost": cost
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"AIMS65 Score = {score}/5",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="AIMS65 Score",
                filename="aims65_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="aims65",
                calculator_name="AIMS65 Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="aims65",
                calculator_name="AIMS65 Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="aims65", show_actions=True)
            
            # References section
            references = get_references("AIMS65")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            else:
                # Fallback to manual references
                with st.expander("📚 Tài liệu tham khảo"):
                    st.markdown("""
                    **Primary Reference:**
                    - Saltzman JR, Tabak YP, Hyett BH, Sun X, Travis AC, Johannes RS.
                      *A simple risk score accurately predicts in-hospital mortality, length of stay, and cost in acute upper GI bleeding.*
                      Gastrointest Endosc. 2011 Dec;74(6):1215-24. [PMID: 22000769]
                    
                    **Validation Studies:**
                    - Robertson M, Majumdar A, Boyapati R, et al.
                      *Risk stratification in acute upper GI bleeding: comparison of the AIMS65 score with the Glasgow-Blatchford and Rockall scoring systems.*
                      Gastrointest Endosc. 2016 Jun;83(6):1151-60.
                    
                    - Hyett BH, Abougergi MS, Charpentier JP, et al.
                      *The AIMS65 score compared with the Glasgow-Blatchford score in predicting outcomes in upper GI bleeding.*
                      Gastrointest Endosc. 2013 Apr;77(4):551-7.
                    
                    **Guidelines:**
                    - Gralnek IM, et al. *Nonvariceal upper gastrointestinal hemorrhage: ESGE Guideline.*
                      Endoscopy. 2015 Oct;47(10):a1-46.
                    
                    - Barkun AN, et al. *International consensus recommendations on the management of patients with nonvariceal upper gastrointestinal bleeding.*
                      Ann Intern Med. 2010 Jan 5;152(1):101-13.
                    """)
    
    # Always show references at the bottom
    references = get_references("AIMS65")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ AIMS65 Score là gì?"):
        st.markdown("""
        **AIMS65 Score** là thang điểm đơn giản để dự đoán tử vong ở bệnh nhân 
        xuất huyết tiêu hóa trên (UGIB).
        
        **Đặc điểm:**
        - Chỉ 5 yếu tố (mỗi yếu tố = 1 điểm)
        - Không cần nội soi (pre-endoscopy)
        - Điểm 0-5
        - Rất đơn giản, dễ tính
        
        **Ưu điểm:**
        - **Đơn giản:** Chỉ 5 yếu tố, dễ nhớ
        - **Dự đoán tử vong tốt:** AUC ~0.75-0.80
        - **Dự đoán chi phí và thời gian nằm viện**
        - **Validated rộng rãi**
        
        **Ứng dụng chính:**
        - **Dự đoán tử vong** trong bệnh viện
        - **Đánh giá độ nặng** bệnh
        - **Hỗ trợ quyết định** điều trị (ICU vs ward)
        - **Dự đoán chi phí** và thời gian nằm viện
        
        **So với GBS và Rockall:**
        - AIMS65: Đơn giản nhất, dự đoán tử vong tốt
        - GBS: Dự đoán can thiệp tốt, discharge decision
        - Rockall: Dự đoán tử vong tốt, cần nội soi
        """)
    
    with st.expander("🩸 Các Yếu Tố AIMS65 - Ý nghĩa Lâm sàng"):
        st.markdown("""
        **1. Albumin < 3.0 g/dL:**
        - Phản ánh tình trạng dinh dưỡng kém
        - Bệnh gan mạn, suy dinh dưỡng
        - Liên quan đến khả năng hồi phục kém
        
        **2. INR > 1.5:**
        - Rối loạn đông máu
        - Bệnh gan, dùng warfarin
        - Tăng nguy cơ chảy máu kéo dài
        
        **3. Mental Status Altered:**
        - Rối loạn ý thức (lơ mơ, kích động, hôn mê)
        - Phản ánh độ nặng bệnh
        - Có thể do shock, thiếu máu não, bệnh gan
        
        **4. Systolic BP ≤ 90 mmHg:**
        - Hạ huyết áp, shock
        - Phản ánh mất máu nhiều
        - Cần hồi sức tích cực
        
        **5. Age > 65:**
        - Tuổi cao
        - Comorbidities nhiều hơn
        - Khả năng hồi phục kém hơn
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Saltzman JR, et al. Gastrointest Endosc. 2011;74(6):1215-24")
    st.caption("⚠️ AIMS65 dự đoán tử vong tốt, nhưng không dùng để quyết định discharge")
    st.caption("🏥 Kết hợp với GBS để đánh giá toàn diện bệnh nhân UGIB")

