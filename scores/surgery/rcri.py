"""
RCRI - Revised Cardiac Risk Index Calculator
Đánh giá nguy cơ tim mạch phẫu thuật (Lee's Index)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_rcri(high_risk_surgery, ischemic_heart, chf, cvd, dm_insulin, creat):
    """
    Tính RCRI
    Mỗi yếu tố = 1 điểm
    """
    total = high_risk_surgery + ischemic_heart + chf + cvd + dm_insulin + creat
    
    if total == 0:
        risk = "Rất thấp"
        rate = "0.4-0.5%"
        color = "green"
    elif total == 1:
        risk = "Thấp"
        rate = "0.9-1.3%"
        color = "green"
    elif total == 2:
        risk = "Trung bình"
        rate = "4-7%"
        color = "orange"
    else:  # >= 3
        risk = "Cao"
        rate = "≥9-11%"
        color = "red"
    
    return {"total_score": total, "risk_level": risk, "cardiac_event_rate": rate, "color": color}


def render():
    """Render RCRI calculator interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'rcri':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #DC2626;'>❤️ RCRI - Revised Cardiac Risk Index</h2>
    <p style='text-align: center;'><em>Nguy cơ biến chứng tim mạch phẫu thuật (Lee's Index)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về RCRI"):
        st.markdown("""
        **RCRI (Revised Cardiac Risk Index)**, còn gọi là **Lee's Index**, đánh giá nguy cơ 
        biến chứng tim mạch lớn sau phẫu thuật không tim.
        
        **Biến chứng tim mạch lớn:**
        - Nhồi máu cơ tim
        - Ngưng tim
        - Phù phổi cấp
        - Block tim hoàn toàn
        - Rung thất
        
        **Mục đích:** Đánh giá nguy cơ tiền phẫu để tối ưu hóa quản lý
        
        **Thang điểm:** 0-6 điểm
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 6 yếu tố nguy cơ")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="rcri",
            calculator_name="RCRI - Revised Cardiac Risk Index",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    high_risk_surgery = st.checkbox(
        "Phẫu thuật nguy cơ cao",
        help="Phẫu thuật trong ổ bụng, ngực, mạch máu lớn"
    )
    
    ischemic_heart = st.checkbox(
        "Bệnh tim thiếu máu cục bộ",
        help="Tiền sử nhồi máu cơ tim, test gắng sức dương, đau thắt ngực, dùng nitrate, sóng Q bệnh lý trên ECG"
    )
    
    chf = st.checkbox(
        "Suy tim",
        help="Tiền sử suy tim, phù phổi, PND, ran ẩm, S3 tim, X-quang phù phổi"
    )
    
    cvd = st.checkbox(
        "Bệnh mạch não",
        help="Tiền sử đột quỵ hoặc TIA"
    )
    
    dm_insulin = st.checkbox(
        "Đái tháo đường dùng insulin",
        help="Đái tháo đường cần điều trị bằng insulin"
    )
    
    creat = st.checkbox(
        "Creatinine > 2 mg/dL (> 177 μmol/L)",
        help="Suy thận mạn"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính RCRI", type="primary", use_container_width=True):
        result = calculate_rcri(
            1 if high_risk_surgery else 0,
            1 if ischemic_heart else 0,
            1 if chf else 0,
            1 if cvd else 0,
            1 if dm_insulin else 0,
            1 if creat else 0
        )
        
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                RCRI: {result['total_score']}/6
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color};'>🎯 Nguy cơ: {result['risk_level']}</h3>
            <p style='font-size: 1.2em;'><strong>Tỷ lệ biến chứng tim mạch lớn:</strong> {result['cardiac_event_rate']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        if result["total_score"] <= 1:
            st.success("""
            ✅ **Nguy cơ thấp (0-1 điểm)**
            
            **Quản lý:**
            - Phẫu thuật tiến hành bình thường
            - Không cần xét nghiệm tim mạch thêm
            - Tiếp tục thuốc beta-blocker nếu đang dùng
            - Theo dõi ECG, Troponin sau mổ nếu có triệu chứng
            """)
        elif result["total_score"] == 2:
            st.warning("""
            ⚠️ **Nguy cơ trung bình (2 điểm)**
            
            **Quản lý:**
            - Cân nhắc xét nghiệm thêm (Echo, test gắng sức)
            - Beta-blocker nếu chưa có chống chỉ định
            - Tối ưu hóa điều trị nội khoa
            - Theo dõi sát sau mổ
            - ECG, Troponin sau mổ
            """)
        else:
            st.error("""
            🚨 **Nguy cơ cao (≥3 điểm)**
            
            **Quản lý:**
            - ⚠️ Đánh giá tim mạch toàn diện
            - Echo tim
            - Test gắng sức hoặc imaging stress
            - Cân nhắc chụp mạch vành nếu cần
            - Beta-blocker (nếu không chống chỉ định)
            - Statin
            - Aspirin (cân nhắc dừng trước mổ tùy loại phẫu thuật)
            - Theo dõi ICU sau mổ
            - ECG, Troponin định kỳ
            
            **Cân nhắc:**
            - Can thiệp tim trước (PCI, CABG) nếu cần
            - Hoãn phẫu thuật không cấp cứu để tối ưu hóa
            """)
        
        with st.expander("📊 Bảng phân loại RCRI"):
            st.markdown("""
            | Điểm | Nguy cơ | Biến chứng tim mạch lớn |
            |:----:|:--------|:------------------------|
            | 0 | Rất thấp | 0.4-0.5% |
            | 1 | Thấp | 0.9-1.3% |
            | 2 | Trung bình | 4-7% |
            | ≥3 | Cao | ≥9-11% |
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Phẫu thuật nguy cơ cao": "Có" if high_risk_surgery else "Không",
                "Bệnh tim thiếu máu": "Có" if ischemic_heart else "Không",
                "Suy tim": "Có" if chf else "Không",
                "Bệnh mạch não": "Có" if cvd else "Không",
                "ĐTĐ dùng insulin": "Có" if dm_insulin else "Không",
                "Creatinine > 2": "Có" if creat else "Không"
            }
            
            results_dict = {
                "RCRI Score": f"{result['total_score']}/6",
                "Nguy cơ": result['risk_level'],
                "Tỷ lệ biến chứng": result['cardiac_event_rate']
            }
            
            # Save to history
            save_calculation_to_history(
                calculator_id="rcri",
                calculator_name="RCRI - Revised Cardiac Risk Index",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="rcri",
                calculator_name="RCRI - Revised Cardiac Risk Index",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="rcri", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("RCRI")
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

