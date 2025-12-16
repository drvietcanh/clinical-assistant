"""
Rockall Score for Upper GI Bleeding
Predicts mortality and rebleeding risk in UGIB

Two versions:
1. Pre-endoscopy Rockall (Clinical): Age + Shock + Comorbidities (0-7)
2. Complete Rockall: Add Diagnosis + Stigmata (0-11)

Reference:
Rockall TA, et al. Risk assessment after acute upper gastrointestinal haemorrhage.
Gut. 1996;38(3):316-21.
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_heart_rate
)
from components.ui.validation import render_validation_errors


def render():
    """Render Rockall Score Calculator"""
    
    shared = load_shared_result_from_url()
    shared_inputs = shared.get("inputs", {}) if shared and shared.get("calculator_id") == "rockall" else {}
    if shared_inputs:
        st.info("📥 Đã tải kết quả chia sẻ Rockall")
    
    st.subheader("🩸 Rockall Score")
    st.caption("Tiên lượng xuất huyết tiêu hóa trên")
    
    st.markdown("""
    **Rockall Score** dự đoán tử vong và tái chảy máu trong xuất huyết tiêu hóa trên.
    
    **Hai phiên bản:**
    - **Pre-endoscopy (Clinical) Rockall:** 0-7 điểm
    - **Complete Rockall:** 0-11 điểm (sau nội soi)
    """)
    
    render_suggestions(
        calculator_id="rockall",
        calculator_name="Rockall Score",
        category="Tiêu Hóa",
        show_related=True,
        show_category=True,
        limit=3
    )
    
    st.markdown("---")
    
    # Choose version
    version = st.radio(
        "**Chọn phiên bản:**",
        [
            "Pre-endoscopy Rockall (Clinical) - Chưa nội soi",
            "Complete Rockall - Đã có kết quả nội soi"
        ],
        help="Clinical Rockall dùng trước nội soi, Complete Rockall dùng sau nội soi"
    )
    
    is_complete = "Complete" in version
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    # Defaults for complete scoring
    diagnosis_score = 0
    stigmata_score = 0
    
    with col1:
        st.markdown("### 📋 Thông tin lâm sàng")
        
        # 1. Age
        st.markdown("#### 1. Tuổi")
        age = st.number_input(
            "Tuổi:",
            min_value=0,
            max_value=120,
            value=50,
            step=1
        )
        
        if age < 60:
            age_score = 0
        elif age < 80:
            age_score = 1
        else:
            age_score = 2
        
        st.caption(f"Điểm: {age_score}")
        
        # 2. Shock
        st.markdown("#### 2. Shock")
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=50,
            max_value=250,
            value=120,
            step=5
        )
        
        hr = st.number_input(
            "Nhịp tim (lần/phút):",
            min_value=30,
            max_value=200,
            value=80,
            step=5
        )
        
        if sbp >= 100 and hr < 100:
            shock_score = 0
            shock_level = "Không shock"
        elif sbp >= 100 and hr >= 100:
            shock_score = 1
            shock_level = "Tachycardia"
        else:  # SBP < 100
            shock_score = 2
            shock_level = "Hạ huyết áp (shock)"
        
        st.caption(f"{shock_level} → Điểm: {shock_score}")
        
        # 3. Comorbidities
        st.markdown("#### 3. Bệnh đi kèm")
        
        comorbidity_options = [
            "Không có hoặc nhẹ",
            "Suy tim, bệnh mạch vành, hoặc comorbidity lớn khác",
            "Suy thận, suy gan, ung thư di căn"
        ]
        
        comorbidity = st.radio(
            "Bệnh kèm theo:",
            comorbidity_options,
            help="Chọn mức độ nặng nhất nếu có nhiều bệnh"
        )
        
        if "Không" in comorbidity:
            comorbidity_score = 0
        elif "Suy tim" in comorbidity:
            comorbidity_score = 2
        else:
            comorbidity_score = 3
        
        st.caption(f"Điểm: {comorbidity_score}")
        
        # Calculate pre-endoscopy score
        pre_endo_score = age_score + shock_score + comorbidity_score
        
        if is_complete:
            st.markdown("---")
            st.markdown("### 🔬 Kết quả Nội soi")
            
            # 4. Diagnosis
            st.markdown("#### 4. Chẩn đoán")
            
            diagnosis_options = [
                "Mallory-Weiss tear, không có tổn thương, hoặc không có dấu hiệu chảy máu gần đây",
                "Tất cả các chẩn đoán khác",
                "Ung thư đường tiêu hóa trên"
            ]
            
            diagnosis = st.radio(
                "Chẩn đoán nội soi:",
                diagnosis_options
            )
            
            if "Mallory-Weiss" in diagnosis:
                diagnosis_score = 0
            elif "Ung thư" in diagnosis:
                diagnosis_score = 2
            else:
                diagnosis_score = 1
            
            st.caption(f"Điểm: {diagnosis_score}")
            
            # 5. Stigmata of recent hemorrhage
            st.markdown("#### 5. Dấu hiệu Chảy máu Gần Đây")
            
            stigmata_options = [
                "Không có dấu hiệu hoặc đốm đen (Forrest III)",
                "Cục máu đậm, mạch máu lộ, hoặc đốm đen ở đáy loét (Forrest IIa, IIb, IIc)",
                "Máu trong đường tiêu hóa trên, chảy máu mạch phun hoặc mạch lộ (Forrest Ia, Ib)"
            ]
            
            stigmata = st.radio(
                "Dấu hiệu chảy máu:",
                stigmata_options,
                help="Phân loại Forrest cho loét tiêu hóa"
            )
            
            if "Không" in stigmata:
                stigmata_score = 0
            elif "Cục máu" in stigmata:
                stigmata_score = 2
            else:
                stigmata_score = 2
            
            st.caption(f"Điểm: {stigmata_score}")
            
            # Calculate complete score
            complete_score = pre_endo_score + diagnosis_score + stigmata_score
        
        st.markdown("---")
        
        if st.button("🧮 Tính Rockall Score", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 0, 120)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
            
            is_valid_hr, hr_error = validate_heart_rate(hr)
            if not is_valid_hr:
                validation_errors.append(hr_error)
            
            if validation_errors:
                render_validation_errors(validation_errors)
            
            if is_complete:
                total_score = complete_score
                max_score = 11
            else:
                total_score = pre_endo_score
                max_score = 7
            
            # Determine risk
            if not is_complete:
                # Pre-endoscopy Rockall
                if total_score == 0:
                    mortality = "0.2%"
                    rebleed = "4.9%"
                    risk = "RẤT THẤP"
                    color = "green"
                elif total_score <= 2:
                    mortality = "0.2-0.5%"
                    rebleed = "5-11%"
                    risk = "THẤP"
                    color = "green"
                elif total_score <= 4:
                    mortality = "3-5%"
                    rebleed = "14%"
                    risk = "TRUNG BÌNH"
                    color = "orange"
                else:
                    mortality = "11-25%"
                    rebleed = "24%"
                    risk = "CAO"
                    color = "red"
            else:
                # Complete Rockall
                if total_score <= 2:
                    mortality = "0.2%"
                    rebleed = "5%"
                    risk = "RẤT THẤP"
                    color = "green"
                elif total_score <= 3:
                    mortality = "2.9%"
                    rebleed = "11%"
                    risk = "THẤP"
                    color = "green"
                elif total_score <= 5:
                    mortality = "5.3%"
                    rebleed = "14%"
                    risk = "TRUNG BÌNH"
                    color = "orange"
                elif total_score <= 7:
                    mortality = "10.8%"
                    rebleed = "24%"
                    risk = "CAO"
                    color = "red"
                else:
                    mortality = "26.7%"
                    rebleed = "42%"
                    risk = "RẤT CAO"
                    color = "red"
            
            # Map color names to hex
            color_map = {
                "green": "#28a745",  # green
                "orange": "#fd7e14",  # orange
                "red": "#dc3545"     # red
            }
            icon_map = {
                "green": "✅",
                "orange": "⚠️",
                "red": "🚨"
            }
            score_color = color_map.get(color, "#17a2b8")
            score_icon = icon_map.get(color, "💡")
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                from components.ui.scoring import render_score_result, render_score_breakdown
                
                render_score_result(
                    title="Rockall Score",
                    score=total_score,
                    interpretation=f"Nguy cơ {risk}",
                    mortality=f"Tử vong: {mortality}, Tái chảy máu: {rebleed}",
                    color=score_color,
                    icon=score_icon,
                    size="large"
                )
            
            st.markdown("---")
            st.markdown("### 💊 KHUYẾN CÁO")
            
            if not is_complete:
                st.info("""
                **ℹ️ Pre-endoscopy (Clinical) Rockall Score**
                
                Đây là điểm trước nội soi. Để đánh giá đầy đủ, cần thực hiện nội soi 
                và tính Complete Rockall Score.
                """)
            
            if total_score <= 2 and is_complete:
                st.success(f"""
                **🟢 Rockall ≤2 - NGUY CƠ RẤT THẤP**
                
                **Tiên lượng:**
                - Tử vong: {mortality}
                - Tái chảy máu: {rebleed}
                
                **Khuyến nghị:**
                
                1. **Có thể xuất viện sớm:**
                   - Sau nội soi 12-24h
                   - Nếu ổn định lâm sàng
                   - Không comorbidity nặng
                
                2. **Điều trị:**
                   - PPI: Omeprazole 20-40mg daily
                   - Thời gian tùy nguyên nhân
                
                3. **Theo dõi ngoại trú:**
                   - Tái khám 1-2 tuần
                   - H. pylori test & treat
                
                **Tiên lượng:** Xuất sắc
                """)
            
            elif total_score <= 5:
                st.warning(f"""
                **🟡 Rockall {total_score} - NGUY CƠ TRUNG BÌNH**
                
                **Tiên lượng:**
                - Tử vong: {mortality}
                - Tái chảy máu: {rebleed}
                
                **Khuyến nghị:**
                
                1. **Nhập viện theo dõi:**
                   - 2-3 ngày
                   - Theo dõi biến chứng
                
                2. **Điều trị:**
                   - PPI IV 72h → PO
                   - Theo dõi Hgb
                
                3. **Nội soi lại nếu:**
                   - Tái chảy máu
                   - Không cải thiện
                
                **Tiên lượng:** Tốt với điều trị
                """)
            
            else:
                st.error(f"""
                **🔴 Rockall {total_score} - NGUY CƠ CAO**
                
                **Tiên lượng:**
                - Tử vong: {mortality}
                - Tái chảy máu: {rebleed}
                
                **Khuyến nghị:**
                
                1. **ICU/HDU monitoring:**
                   - Theo dõi sát
                   - Sẵn sàng can thiệp
                
                2. **Điều trị tích cực:**
                   - PPI IV liều cao
                   - Truyền máu nếu cần
                   - Sẵn sàng nội soi lại
                
                3. **Cân nhắc:**
                   - IR embolization
                   - Phẫu thuật
                   - TIPS (nếu variceal)
                
                **Tiên lượng:** Xấu, cần theo dõi sát
                """)
            
            # Phase 1: save/share/history + references
            inputs_dict = {
                "version": "Complete" if is_complete else "Pre-endoscopy",
                "age": age,
                "sbp": sbp,
                "hr": hr,
                "comorbidity": comorbidity,
                "pre_endo_score": pre_endo_score,
                "diagnosis": diagnosis if is_complete else None,
                "stigmata": stigmata if is_complete else None
            }
            results_dict = {
                "Rockall Score": total_score,
                "Mortality": mortality,
                "Rebleed": rebleed
            }
            
            save_calculation_to_history(
                calculator_id="rockall",
                calculator_name="Rockall Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            render_share_section(
                calculator_id="rockall",
                calculator_name="Rockall Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            st.markdown("---")
            render_history_ui(calculator_id="rockall", show_actions=True)
            
            references = get_references("ROCKALL")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            
            # Score breakdown
            st.markdown("---")
            with st.expander("📊 Bảng Chấm Điểm Rockall"):
                st.markdown("""
                | Thành phần | 0 điểm | 1 điểm | 2 điểm | 3 điểm |
                |------------|--------|--------|--------|--------|
                | **Tuổi** | <60 | 60-79 | ≥80 | - |
                | **Shock** | SBP≥100, HR<100 | SBP≥100, HR≥100 | SBP<100 | - |
                | **Comorbidity** | Không/nhẹ | - | CHF, IHD, major | Renal/liver failure, cancer |
                | **Diagnosis*** | Mallory-Weiss, no lesion | Other | Malignancy | - |
                | **Stigmata*** | None/dark spot | - | Clot, visible vessel, blood | - |
                
                *Chỉ cho Complete Rockall (sau nội soi)
                
                **Pre-endoscopy Rockall:** 0-7 điểm
                **Complete Rockall:** 0-11 điểm
                """)
            
            with st.expander("📈 Bảng nguy cơ theo điểm"):
                if is_complete:
                    st.markdown("""
                    **Complete Rockall Score:**
                    
                    | Score | Tử vong | Tái chảy máu |
                    |-------|---------|--------------|
                    | 0-2 | 0.2% | 5% |
                    | 3 | 2.9% | 11% |
                    | 4-5 | 5.3% | 14% |
                    | 6-7 | 10.8% | 24% |
                    | ≥8 | 26.7% | 42% |
                    """)
                else:
                    st.markdown("""
                    **Pre-endoscopy (Clinical) Rockall:**
                    
                    | Score | Tử vong | Tái chảy máu |
                    |-------|---------|--------------|
                    | 0 | 0.2% | 4.9% |
                    | 1-2 | 0.2-0.5% | 5-11% |
                    | 3-4 | 3-5% | 14% |
                    | ≥5 | 11-25% | 24% |
                    """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **Primary Reference:**
                - Rockall TA, Logan RF, Devlin HB, Northfield TC. 
                  *Risk assessment after acute upper gastrointestinal haemorrhage.* 
                  Gut. 1996 Mar;38(3):316-21. [PMID: 8675081]
                
                **Validation:**
                - Vreeburg EM, Terwee CB, Snel P, et al. 
                  *Validation of the Rockall risk scoring system in upper gastrointestinal bleeding.* 
                  Gut. 1999 Sep;44(3):331-5.
                
                - Sanders DS, Carter MJ, Goodchap RJ, Cross SS, Gleeson DC, Lobo AJ. 
                  *Prospective validation of the Rockall risk scoring system for upper GI hemorrhage in subgroups of patients with varices and peptic ulcers.* 
                  Am J Gastroenterol. 2002 Mar;97(3):630-5.
                """)
    
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("🔄 Pre-endoscopy vs Complete Rockall"):
        st.markdown("""
        **Hai phiên bản Rockall Score:**
        
        **1. Pre-endoscopy (Clinical) Rockall (0-7):**
        - Dùng TRƯỚC nội soi
        - Chỉ cần: Tuổi + Shock + Comorbidities
        - Giúp phân tầng nguy cơ sớm
        - Dự đoán kém hơn Complete Rockall
        
        **2. Complete Rockall (0-11):**
        - Dùng SAU nội soi
        - Thêm: Diagnosis + Stigmata
        - Dự đoán chính xác hơn
        - Hướng dẫn điều trị tốt hơn
        
        **Khuyến nghị:**
        - Tính Clinical Rockall tại ED/admission
        - Tính Complete Rockall sau nội soi
        - Sử dụng cả hai để đánh giá đầy đủ
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Rockall TA, et al. Gut. 1996;38(3):316-21")
    st.caption("⚠️ Predicts mortality and rebleeding in UGIB")
    st.caption("🏥 Use Glasgow-Blatchford for discharge decision, Rockall for prognosis")

