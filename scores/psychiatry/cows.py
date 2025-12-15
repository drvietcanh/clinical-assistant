"""
COWS - Clinical Opiate Withdrawal Scale
Đánh giá cai opioid
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions

def calculate_cows(pulse, sweating, restlessness, pupil, bone_pain, runny, gi, tremor, yawning, anxiety, gooseflesh):
    """Tính COWS score"""
    total = pulse + sweating + restlessness + pupil + bone_pain + runny + gi + tremor + yawning + anxiety + gooseflesh
    
    if total <= 4:
        severity = "Nhẹ"; management = "Hỗ trợ triệu chứng"; color = "green"
    elif total <= 12:
        severity = "Trung bình"; management = "Clonidine, hỗ trợ triệu chứng"; color = "orange"
    elif total <= 24:
        severity = "Trung bình-Nặng"; management = "Buprenorphine/Methadone"; color = "orange"
    else:
        severity = "Nặng"; management = "Điều trị tích cực, Buprenorphine/Methadone"; color = "red"
    
    return {"total_score": total, "severity": severity, "management": management, "color": color}

def render():
    """Render COWS calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'cows':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("💊 COWS - Clinical Opiate Withdrawal Scale")
    st.caption("Đánh giá cai opioid")
    
    st.markdown("""
    **COWS (Clinical Opiate Withdrawal Scale):**
    - Đánh giá mức độ nặng cai opioid
    - Hướng dẫn điều trị
    - Thang điểm: 0-48
    - Đánh giá lại mỗi 2-4 giờ
    """)
    
    with st.expander("ℹ️ Giới thiệu COWS"):
        st.markdown("""
        **COWS** đánh giá mức độ nặng cai opioid.
        
        **Thang điểm:** 0-48
        
        **Phân loại:**
        - ≤ 4: Nhẹ - Hỗ trợ triệu chứng
        - 5-12: Trung bình - Clonidine, hỗ trợ triệu chứng
        - 13-24: Trung bình-Nặng - Buprenorphine/Methadone
        - > 24: Nặng - Điều trị tích cực
        """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Đánh giá triệu chứng")
    
    # Define format functions using dicts
    pulse_dict = {0: "0: ≤80", 1: "1: 81-100", 2: "2: 101-120", 4: "4: >120"}
    sweating_dict = {0: "0: Không", 1: "1: Lòng bàn tay ẩm", 2: "2: Đổ mồ hôi trán", 3: "3: Đổ mồ hôi cả người", 4: "4: Đổ mồ hôi ướt quần áo"}
    restlessness_dict = {0: "0: Bình thường", 1: "1: Nhẹ", 3: "3: Trung bình", 5: "5: Nặng"}
    pupil_dict = {0: "0: Bình thường", 1: "1: Hơi to", 2: "2: Giãn trung bình", 5: "5: Giãn rất to"}
    bone_pain_dict = {0: "0: Không", 1: "1: Nhẹ", 2: "2: Trung bình", 4: "4: Nặng"}
    runny_dict = {0: "0: Không", 1: "1: Nhẹ", 2: "2: Trung bình", 4: "4: Nặng"}
    gi_dict = {0: "0: Không", 2: "2: Có", 5: "5: Nặng"}
    tremor_dict = {0: "0: Không", 1: "1: Thấy khi giơ tay", 2: "2: Thấy khi để tay", 4: "4: Run toàn thân"}
    yawning_dict = {0: "0: 0 lần", 1: "1: 1-2 lần", 2: "2: 3-4 lần", 4: "4: >4 lần"}
    anxiety_dict = {0: "0: Không", 1: "1: Nhẹ", 2: "2: Trung bình", 4: "4: Nặng"}
    gooseflesh_dict = {0: "0: Không", 3: "3: Da gà", 5: "5: Da gà + rét run"}
    
    pulse = st.radio("1. Mạch (nhịp/phút)", [0,1,2,4], format_func=lambda x: pulse_dict.get(x, ""))
    sweating = st.radio("2. Đổ mồ hôi", [0,1,2,3,4], format_func=lambda x: sweating_dict.get(x, ""))
    restlessness = st.radio("3. Bồn chồn", [0,1,3,5], format_func=lambda x: restlessness_dict.get(x, ""))
    pupil = st.radio("4. Giãn đồng tử", [0,1,2,5], format_func=lambda x: pupil_dict.get(x, ""))
    bone_pain = st.radio("5. Đau xương/khớp", [0,1,2,4], format_func=lambda x: bone_pain_dict.get(x, ""))
    runny = st.radio("6. Sổ mũi/chảy nước mắt", [0,1,2,4], format_func=lambda x: runny_dict.get(x, ""))
    gi = st.radio("7. Tiêu chảy", [0,2,5], format_func=lambda x: gi_dict.get(x, ""))
    tremor = st.radio("8. Run", [0,1,2,4], format_func=lambda x: tremor_dict.get(x, ""))
    yawning = st.radio("9. Ngáp (trong 1 lần đánh giá)", [0,1,2,4], format_func=lambda x: yawning_dict.get(x, ""))
    anxiety = st.radio("10. Lo âu/kích động", [0,1,2,4], format_func=lambda x: anxiety_dict.get(x, ""))
    gooseflesh = st.radio("11. Da gà (Gooseflesh)", [0,3,5], format_func=lambda x: gooseflesh_dict.get(x, ""))
    
    if st.button("🔬 Tính COWS", type="primary", use_container_width=True):
        result = calculate_cows(pulse, sweating, restlessness, pupil, bone_pain, runny, gi, tremor, yawning, anxiety, gooseflesh)
        score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[result["color"]]
            
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                COWS: {result['total_score']}/48
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color};'>🎯 Mức độ: {result['severity']}</h3>
            <p style='font-size: 1.2em;'><strong>Điều trị:</strong> {result['management']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **Điều trị:**
        - **≤ 4:** Nhẹ - Hỗ trợ triệu chứng
        - **5-12:** Trung bình - Clonidine, hỗ trợ triệu chứng
        - **13-24:** Trung bình-Nặng - Buprenorphine 4-8mg hoặc Methadone 20-30mg
        - **> 24:** Nặng - Buprenorphine liều cao hoặc Methadone 30-40mg
        """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Mạch": pulse,
            "Đổ mồ hôi": sweating,
            "Bồn chồn": restlessness,
            "Giãn đồng tử": pupil,
            "Đau xương/khớp": bone_pain,
            "Sổ mũi/chảy nước mắt": runny,
            "Tiêu chảy": gi,
            "Run": tremor,
            "Ngáp": yawning,
            "Lo âu/kích động": anxiety,
            "Da gà": gooseflesh
        }
        
        results_dict = {
            "Tổng điểm COWS": f"{result['total_score']}/48",
            "Mức độ": result['severity'],
            "Điều trị": result['management']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="cows",
            calculator_name="COWS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="cows",
            calculator_name="COWS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="cows",
            calculator_name="COWS",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="cows", show_actions=True)
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="cows",
            calculator_name="COWS",
            category="Tâm Thần",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("💊 Điều trị chi tiết"):
        st.markdown("""
        **Buprenorphine:**
        - 4-8mg SL ngày đầu
        - Tăng dần đến 12-16mg/ngày
        - Duy trì hoặc giảm dần
        
        **Methadone:**
        - 20-30mg PO ngày đầu
        - Tăng dần đến 40-60mg/ngày
        - Duy trì hoặc giảm dần
        
        **Clonidine:**
        - 0.1-0.3mg PO q6-8h
        - Giảm triệu chứng tự chủ
        - Theo dõi huyết áp
        """)
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("COWS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.caption("""
        **Tài liệu tham khảo:**
        - Wesson DR, Ling W. The Clinical Opiate Withdrawal Scale (COWS). J Psychoactive Drugs. 2003;35(2):253-9.
        - Degenhardt L, et al. Global patterns of opioid use and dependence: harms to populations, interventions, and future action. Lancet. 2019;394(10208):1560-79.
        """)

if __name__ == "__main__":
    render()

