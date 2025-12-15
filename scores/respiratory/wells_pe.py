"""
Wells Score for Pulmonary Embolism
Đánh giá xác suất tắc mạch phổi
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================
from scores.utils.validation import validate_heart_rate
from components.ui.scoring import render_score_result, render_score_breakdown


def render():
    """Wells PE Score Calculator"""
    st.subheader("🫁 Wells PE Score")
    st.caption("Wells Score - Xác Suất Tắc Mạch Phổi")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'wells_pe':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        # Pre-fill inputs from shared result (optional)
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **Wells PE Score** đánh giá xác suất tiền test của tắc mạch phổi (PE).
    
    - Sử dụng kết hợp với D-dimer để quyết định chụp CTPA
    - Validated rộng rãi trong thực hành lâm sàng
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí lâm sàng")
        
        # Pre-fill from shared result if available
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        # Clinical signs of DVT
        dvt_signs = st.checkbox(
            "**Dấu hiệu lâm sàng của huyết khối tĩnh mạch sâu (DVT)**",
            help="Chân sưng, đau, ấn đau dọc tĩnh mạch (+3 điểm)",
            value=shared_inputs.get('DVT Signs') == 'Có' if shared_inputs else False
        )
        
        # PE most likely diagnosis
        pe_likely = st.checkbox(
            "**Tắc mạch phổi là chẩn đoán khả năng nhất**",
            help="Không có chẩn đoán khác hợp lý hơn (+3 điểm)",
            value=shared_inputs.get('PE Likely') == 'Có' if shared_inputs else False
        )
        
        # Heart rate
        hr = st.number_input(
            "**Nhịp tim** (lần/phút)",
            min_value=0,
            max_value=250,
            value=int(shared_inputs.get('Heart Rate', 80)) if shared_inputs and shared_inputs.get('Heart Rate') else 80,
            step=5,
            help=">100/phút: +1.5 điểm"
        )
        
        # Immobilization/Surgery
        immobilization = st.checkbox(
            "**Nằm bất động ≥3 ngày HOẶC phẫu thuật trong 4 tuần qua**",
            help="+1.5 điểm",
            value=shared_inputs.get('Immobilization') == 'Có' if shared_inputs else False
        )
        
        # Previous DVT/PE
        previous_vte = st.checkbox(
            "**Tiền sử DVT hoặc PE**",
            help="+1.5 điểm",
            value=shared_inputs.get('Previous VTE') == 'Có' if shared_inputs else False
        )
        
        # Hemoptysis
        hemoptysis = st.checkbox(
            "**Ho ra máu**",
            help="+1 điểm",
            value=shared_inputs.get('Hemoptysis') == 'Có' if shared_inputs else False
        )
        
        # Malignancy
        malignancy = st.checkbox(
            "**Ung thư**",
            help="Đang điều trị hoặc điều trị trong 6 tháng qua, hoặc paLiative (+1 điểm)",
            value=shared_inputs.get('Malignancy') == 'Có' if shared_inputs else False
        )
        
        st.markdown("---")
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="wells_pe",
            calculator_name="Wells PE Score",
            category="Hô Hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🧮 Tính Wells PE Score", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_hr, hr_error = validate_heart_rate(hr)
            if not is_valid_hr:
                validation_errors.append(hr_error)
            
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
            
            # Calculate score
            score = 0.0
            details = []
            
            if dvt_signs:
                score += 3.0
                details.append("Dấu hiệu DVT: +3")
            
            if pe_likely:
                score += 3.0
                details.append("PE khả năng nhất: +3")
            
            if hr > 100:
                score += 1.5
                details.append(f"Nhịp tim >100 ({hr}): +1.5")
            
            if immobilization:
                score += 1.5
                details.append("Nằm bất động/Phẫu thuật: +1.5")
            
            if previous_vte:
                score += 1.5
                details.append("Tiền sử DVT/PE: +1.5")
            
            if hemoptysis:
                score += 1.0
                details.append("Ho ra máu: +1")
            
            if malignancy:
                score += 1.0
                details.append("Ung thư: +1")
            
            # Determine probability
            if score < 2:
                probability = "THẤP"
                pe_prevalence = "3.6%"
                color = "success"
                recommendation = "Xét nghiệm D-dimer"
                detail = "D-dimer âm tính → Loại trừ PE (không cần CTPA)"
            elif score <= 6:
                probability = "TRUNG BÌNH"
                pe_prevalence = "20.5%"
                color = "warning"
                recommendation = "Xét nghiệm D-dimer"
                detail = "D-dimer dương tính → Chụp CTPA"
            else:
                probability = "CAO"
                pe_prevalence = "66.7%"
                color = "error"
                recommendation = "Chụp CTPA ngay"
                detail = "Không cần D-dimer - chụp CTPA trực tiếp"
            
            # Map color names to hex
            color_map = {
                "success": "#28a745",  # green
                "warning": "#fd7e14",  # orange
                "error": "#dc3545"     # red
            }
            icon_map = {
                "success": "✅",
                "warning": "⚠️",
                "error": "🚨"
            }
            score_color = color_map[color]
            score_icon = icon_map[color]
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="Wells PE Score",
                    score=round(score, 1),
                    interpretation=f"Xác suất {probability} - PE: {pe_prevalence}",
                    mortality=None,
                    color=score_color,
                    icon=score_icon,
                    size="large"
                )
            
            # Build breakdown of criteria
            criteria_scores = {}
            if dvt_signs:
                criteria_scores["Dấu hiệu DVT"] = 3.0
            if pe_likely:
                criteria_scores["PE khả năng nhất"] = 3.0
            if hr > 100:
                criteria_scores["Nhịp tim >100"] = 1.5
            if immobilization:
                criteria_scores["Nằm bất động/Phẫu thuật"] = 1.5
            if previous_vte:
                criteria_scores["Tiền sử DVT/PE"] = 1.5
            if hemoptysis:
                criteria_scores["Ho ra máu"] = 1.0
            if malignancy:
                criteria_scores["Ung thư"] = 1.0
            
            if criteria_scores:
                render_score_breakdown(
                    title="Tiêu Chí Đánh Giá",
                    subscores=criteria_scores,
                    total_score=round(score, 1)
                )
            
            st.markdown("---")
            st.markdown("### 💡 Chi tiết tính điểm")
            
            if details:
                for d in details:
                    st.write(f"• {d}")
            else:
                st.write("• Không có tiêu chí nào (+0)")
            
            st.markdown(f"**Tổng điểm: {round(score, 1)}**")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo xét nghiệm")
            
            if color == "success":
                st.success(f"""
                **Xác suất THẤP (Score <2) - PE: {pe_prevalence}**
                
                **Khuyến cáo:**
                1. ✅ Xét nghiệm **D-dimer**
                2. ❌ **D-dimer âm tính** (<0.5 µg/mL):
                   → **Loại trừ PE** - Không cần CTPA
                   → Tìm chẩn đoán khác
                
                3. ✅ **D-dimer dương tính**:
                   → Chuyển sang xác suất trung bình
                   → Chụp CTPA
                
                **Lưu ý:** D-dimer có độ nhạy cao, độ đặc hiệu thấp
                """)
            elif color == "warning":
                st.warning(f"""
                **Xác suất TRUNG BÌNH (Score 2-6) - PE: {pe_prevalence}**
                
                **Khuyến cáo:**
                1. ✅ Xét nghiệm **D-dimer**
                2. ❌ **D-dimer âm tính** (<0.5 µg/mL):
                   → Xem xét loại trừ PE
                   → Đánh giá lại lâm sàng
                
                3. ✅ **D-dimer dương tính** (≥0.5 µg/mL):
                   → **Chụp CTPA** (CT Pulmonary Angiography)
                   → Hoặc V/Q scan nếu không chụp được CTPA
                
                4. ⚠️ Cân nhắc khởi đầu **heparin** trong khi chờ kết quả nếu:
                   - Bệnh nhân không ổn định
                   - Nguy cơ cao thực sự
                """)
            else:
                st.error(f"""
                **Xác suất CAO (Score >6) - PE: {pe_prevalence}**
                
                **Khuyến cáo:**
                1. 🚨 **Chụp CTPA NGAY** - KHÔNG cần D-dimer
                2. ✅ **Khởi đầu anticoagulation** trong khi chờ:
                   - LMWH (Enoxaparin) SC
                   - Hoặc Heparin IV nếu bệnh nhân nặng
                
                3. ⚠️ Nếu **không ổn định huyết động**:
                   → Xem xét **thrombolysis**
                   → ICU monitoring
                   → Echo đánh giá right heart strain
                
                4. 📋 **Contraindication tuyệt đối với CTPA:**
                   → V/Q scan
                   → Hoặc Echo + Lower extremity doppler
                
                **⚠️ MASSIVE PE - Dấu hiệu nguy hiểm:**
                - Shock (SBP <90 mmHg)
                - Cần vasopressor
                - Cardiac arrest
                → Xem xét thrombolysis ngay!
                """)
            
            st.markdown("---")
            st.markdown("### 🔬 Về D-dimer")
            
            st.info("""
            **D-dimer là gì?**
            - Sản phẩm phân hủy fibrin
            - Tăng trong huyết khối, DIC
            
            **Giá trị ngưỡng:**
            - **<0.5 µg/mL (FEU):** Âm tính
            - **≥0.5 µg/mL:** Dương tính
            - **Age-adjusted:** >50 tuổi: tuổi × 10 ng/mL
            
            **Độ nhạy & đặc hiệu:**
            - **Độ nhạy:** ~95-98% (rất cao)
            - **Độ đặc hiệu:** ~40-50% (thấp)
            
            **Ý nghĩa:**
            - ✅ **D-dimer âm + Wells thấp** → Loại trừ PE an toàn
            - ❌ **D-dimer dương tính** → Không chẩn đoán PE (cần imaging)
            
            **Nguyên nhân D-dimer tăng khác:**
            - Phẫu thuật, chấn thương gần đây
            - Ung thư
            - Thai kỳ
            - Nhiễm trùng, DIC
            - Cao tuổi
            - Nhồi máu cơ tim
            """)
            
            # Prepare inputs for export and history
            inputs_dict = {
                "DVT Signs": "Có" if dvt_signs else "Không",
                "PE Likely": "Có" if pe_likely else "Không",
                "Heart Rate": str(hr),
                "Immobilization": "Có" if immobilization else "Không",
                "Previous VTE": "Có" if previous_vte else "Không",
                "Hemoptysis": "Có" if hemoptysis else "Không",
                "Malignancy": "Có" if malignancy else "Không"
            }
            
            # Prepare results for export and history
            results_dict = {
                "Wells PE Score": f"{round(score, 1)} điểm",
                "Probability": probability,
                "PE Prevalence": pe_prevalence,
                "Recommendation": recommendation,
                "Details": "\n".join(details) if details else "Không có tiêu chí nào"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"Wells PE Score = {round(score, 1)} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="Wells PE Score",
                filename="wells_pe_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="wells_pe",
                calculator_name="Wells PE Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="wells_pe",
                calculator_name="Wells PE Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="wells_pe", show_actions=True)
            
            # References section
            references = get_references("Wells PE")
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
            
            - Wells Score CHỈ đánh giá **xác suất tiền test**
            - KHÔNG thay thế imaging để chẩn đoán xác định
            - Luôn kết hợp với **lâm sàng, D-dimer, imaging**
            - Với massive PE/instability → Chẩn đoán và điều trị ngay!
            - Anticoagulation có nguy cơ chảy máu → Đánh giá cẩn thận
            """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("Wells PE")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )


