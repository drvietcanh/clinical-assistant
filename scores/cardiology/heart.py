"""
HEART Score Calculator
"""

import streamlit as st
from components.ui.scoring import render_score_result, render_score_breakdown
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions


def render():
    """HEART Score Calculator"""
    st.subheader("❤️ HEART Score")
    st.caption("Đánh giá Nguy cơ ACS Trong Đau Ngực Cấp")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'heart':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **HEART Score** dự đoán nguy cơ MACE (Major Adverse Cardiac Events) trong 6 tuần ở bệnh nhân đau ngực cấp.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        # History
        st.markdown("#### H - History (Tiền sử)")
        history_score = st.radio(
            "Đặc điểm đau ngực:",
            [
                "0 - Ít nguy cơ (không điển hình)",
                "1 - Nguy cơ trung bình (hơi điển hình)",
                "2 - Nguy cơ cao (rất điển hình cho ACS)"
            ],
            key="heart_history"
        )
        history = int(history_score[0])
        
        # ECG
        st.markdown("#### E - ECG")
        ecg_score = st.radio(
            "Kết quả ECG:",
            [
                "0 - Bình thường",
                "1 - Bất thường không đặc hiệu (đảo T, ST chênh không đặc hiệu)",
                "2 - ST chênh đặc hiệu (ST chênh ≥1mm hoặc LBBB mới)"
            ],
            key="heart_ecg"
        )
        ecg = int(ecg_score[0])
        
        # Age
        st.markdown("#### A - Age (Tuổi)")
        age_score = st.radio(
            "Nhóm tuổi:",
            [
                "0 - < 45 tuổi",
                "1 - 45-64 tuổi",
                "2 - ≥ 65 tuổi"
            ],
            key="heart_age"
        )
        age = int(age_score[0])
        
        # Risk factors
        st.markdown("#### R - Risk Factors (Yếu tố nguy cơ)")
        st.caption("Đếm số lượng: THA, ĐTĐ, hút thuốc, cholesterol cao, béo phì, tiền sử gia đình")
        
        risk_factors = []
        col_rf1, col_rf2 = st.columns(2)
        with col_rf1:
            if st.checkbox("Tăng huyết áp", key="rf_htn"):
                risk_factors.append("THA")
            if st.checkbox("Đái tháo đường", key="rf_dm"):
                risk_factors.append("ĐTĐ")
            if st.checkbox("Hút thuốc", key="rf_smoke"):
                risk_factors.append("Hút thuốc")
        
        with col_rf2:
            if st.checkbox("Cholesterol cao", key="rf_chol"):
                risk_factors.append("Cholesterol")
            if st.checkbox("Béo phì", key="rf_obesity"):
                risk_factors.append("Béo phì")
            if st.checkbox("Tiền sử gia đình", key="rf_fhx"):
                risk_factors.append("TSGĐ")
        
        if st.checkbox("Tiền sử bệnh mạch vành đã biết", key="rf_cad"):
            risk_factors.append("CAD")
        
        num_rf = len(risk_factors)
        if num_rf == 0 or (num_rf == 1 and "CAD" not in risk_factors):
            risk = 0
        elif num_rf >= 3 or "CAD" in risk_factors:
            risk = 2
        else:
            risk = 1
        
        # Troponin
        st.markdown("#### T - Troponin")
        troponin_score = st.radio(
            "Troponin:",
            [
                "0 - Bình thường (≤ ngưỡng bình thường)",
                "1 - Tăng nhẹ (1-3 lần giới hạn trên)",
                "2 - Tăng cao (> 3 lần giới hạn trên)"
            ],
            key="heart_troponin"
        )
        troponin = int(troponin_score[0])
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="heart",
            calculator_name="HEART Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🧮 Tính HEART Score", type="primary", key="heart_calc", use_container_width=True):
            total_score = history + ecg + age + risk + troponin
            
            # Determine risk level and color
            if total_score <= 3:
                risk_level = "Nguy cơ THẤP"
                mace_risk = "0.9-1.7%"
                color = "#28a745"  # green
                icon = "✅"
            elif total_score <= 6:
                risk_level = "Nguy cơ TRUNG BÌNH"
                mace_risk = "12-16.6%"
                color = "#fd7e14"  # orange
                icon = "⚠️"
            else:
                risk_level = "Nguy cơ CAO"
                mace_risk = "50-65%"
                color = "#dc3545"  # red
                icon = "🚨"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="HEART Score",
                    score=total_score,
                    interpretation=risk_level,
                    mortality=f"MACE 6 tuần: {mace_risk}",
                    color=color,
                    icon=icon,
                    size="large"
                )
            
            # Use render_score_breakdown for component scores
            render_score_breakdown(
                title="Chi Tiết Điểm Số",
                subscores={
                    "H - History": history,
                    "E - ECG": ecg,
                    "A - Age": age,
                    "R - Risk factors": risk,
                    "T - Troponin": troponin
                },
                total_score=total_score
            )
            
            st.markdown("---")
            st.markdown(f"**R - Risk factors:** {risk} điểm ({num_rf} yếu tố: {', '.join(risk_factors) if risk_factors else 'Không có'})")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo xử trí")
            
            if total_score <= 3:
                st.success("""
                **Nguy cơ MACE thấp ({})** trong 6 tuần
                
                **Khuyến cáo:**
                - ✅ Có thể xuất viện an toàn
                - Theo dõi ngoại trú
                - Giáo dục bệnh nhân về các triệu chứng cần tái khám
                - Kiểm soát yếu tố nguy cơ
                - Cân nhắc stress test ngoại trú
                """.format(mace_risk))
            
            elif total_score <= 6:
                st.warning("""
                **Nguy cơ MACE trung bình ({})** trong 6 tuần
                
                **Khuyến cáo:**
                - ⚠️ Theo dõi tại bệnh viện
                - Serial troponin (0h, 3h, 6h)
                - Cân nhắc stress test hoặc CT coronary angiography
                - Hội chẩn tim mạch
                - Điều trị kháng kết tập tiểu cầu nếu được
                """.format(mace_risk))
            
            else:
                st.error("""
                **Nguy cơ MACE cao ({})** trong 6 tuần
                
                **Khuyến cáo:**
                - 🚨 Nhập viện ngay
                - Xử trí theo protocol ACS
                - DAPT (Aspirin + P2Y12 inhibitor)
                - Anticoagulation (heparin/LMWH)
                - Hội chẩn tim mạch khẩn cấp
                - Cân nhắc can thiệp mạch vành sớm
                - ICU/CCU monitoring
                """.format(mace_risk))
            
            # Prepare inputs for export and history
            inputs_dict = {
                "History": history_score,
                "ECG": ecg_score,
                "Age": age_score,
                "Risk Factors": f"{risk} điểm ({num_rf} yếu tố: {', '.join(risk_factors) if risk_factors else 'Không có'})",
                "Troponin": troponin_score
            }
            
            # Prepare results for export and history
            results_dict = {
                "HEART Score": f"{total_score} điểm",
                "Risk Level": risk_level,
                "MACE Risk": mace_risk,
                "Components": f"H:{history} E:{ecg} A:{age} R:{risk} T:{troponin}"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"HEART Score = {total_score} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="HEART Score",
                filename="heart_score_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="heart",
                calculator_name="HEART Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="heart",
                calculator_name="HEART Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="heart", show_actions=True)
            
            # References section
            references = get_references("HEART")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
    
    # Always show references at the bottom (even before calculation)
    references = get_references("HEART")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
