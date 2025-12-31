"""
Killip Classification
Phân loại suy tim cấp trong nhồi máu cơ tim
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ========== PHASE 1: CALCULATOR ENHANCEMENTS ==========
try:
    from components.calculator_enhancements import (
        render_calculator_explanation,
        render_evidence_citation,
        render_result_interpretation
    )
    CALCULATOR_ENHANCEMENTS_AVAILABLE = True
except ImportError:
    CALCULATOR_ENHANCEMENTS_AVAILABLE = False
# ======================================


def render():
    """Render Killip Classification interface"""
    
    shared = load_shared_result_from_url()
    shared_inputs = {}
    if shared and shared.get("calculator_id") == "killip":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Killip Classification')}")
        shared_inputs = shared.get("inputs", {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>❤️ Killip Classification</h2>
    <p style='text-align: center;'><em>Phân loại suy tim cấp trong AMI</em></p>
    """, unsafe_allow_html=True)
    
    render_suggestions(
        calculator_id="killip",
        calculator_name="Killip Classification",
        category="Tim Mạch",
        show_related=True,
        show_category=True,
        limit=3
    )
    
    # Educational information - Enhanced with Phase 1
    if CALCULATOR_ENHANCEMENTS_AVAILABLE:
        render_calculator_explanation(
            title="Về Killip Classification",
            content="""
            **Killip Classification** phân loại mức độ nặng của suy tim cấp trong nhồi máu cơ tim (AMI):
            
            - Dựa trên lâm sàng đơn giản, không cần xét nghiệm phức tạp
            - Tiên lượng tử vong chính xác
            - Hướng dẫn điều trị
            - Sử dụng từ 1967, vẫn còn giá trị trong thực hành lâm sàng
            
            **4 Class:**
            - **Class I:** Không suy tim (tử vong ~6%)
            - **Class II:** Suy tim nhẹ - ran ẩm ½ dưới phổi, S3, có thể tĩnh mạch cảnh nổi (tử vong ~17%)
            - **Class III:** Phù phổi cấp - ran ẩm cả 2 phổi (tử vong ~38%)
            - **Class IV:** Shock tim - hạ huyết áp, thiểu niệu, lạnh chi (tử vong ~81%)
            """,
            when_to_use="""
            **Sử dụng Killip Classification khi:**
            - Bệnh nhân có nhồi máu cơ tim (AMI)
            - Cần đánh giá mức độ nặng của suy tim cấp
            - Tiên lượng tử vong
            - Hướng dẫn điều trị và theo dõi
            """,
            limitations="""
            **Hạn chế:**
            - Chỉ áp dụng cho bệnh nhân AMI
            - Cần đánh giá lâm sàng chính xác
            - Không thay thế đánh giá lâm sàng cá thể hóa
            - Một số bệnh nhân có thể không rõ ràng giữa các class
            """,
            clinical_context="""
            **Bối cảnh lâm sàng:**
            - Killip Class I-II: Tiên lượng tốt, điều trị chuẩn
            - Killip Class III: Cần điều trị tích cực phù phổi, có thể cần hỗ trợ hô hấp
            - Killip Class IV: Cần hồi sức tích cực, hỗ trợ tuần hoàn, tiên lượng xấu
            - Killip Class cao liên quan đến tử vong và biến cố tim mạch cao hơn
            """
        )
        
        # Evidence citation
        render_evidence_citation(
            citation_text="Killip T 3rd, Kimball JT. Treatment of myocardial infarction in a coronary care unit. A two year experience with 250 patients. Am J Cardiol. 1967;20(4):457-64.",
            doi="10.1016/0002-9149(67)90023-9",
            pmid="6059183"
        )
    else:
        # Fallback to original expander
        with st.expander("ℹ️ Giới thiệu về Killip Classification"):
            st.markdown("""
            **Killip Classification** phân loại **mức độ nặng** của suy tim cấp trong **nhồi máu cơ tim (AMI)** 
            dựa trên **lâm sàng đơn giản**.
            
            **Ưu điểm:**
            - Cực kỳ đơn giản - chỉ cần khám lâm sàng
            - Tiên lượng tử vong chính xác
            - Hướng dẫn điều trị
            - Sử dụng từ 1967, vẫn còn giá trị
            
            **4 Class:**
            - **Class I:** Không suy tim
            - **Class II:** Suy tim nhẹ (ran ẩm, S3, phù phổi nhẹ)
            - **Class III:** Phù phổi cấp
            - **Class IV:** Shock tim
            """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá bệnh nhân")
    
    # Vital signs
    col1, col2, col3 = st.columns(3)
    with col1:
        sbp = st.number_input("HA tâm thu (mmHg)", 60, 220, value=int(shared_inputs.get("sbp", 120)), step=1, format="%d")
    with col2:
        hr = st.number_input("Nhịp tim (bpm)", 40, 180, value=int(shared_inputs.get("hr", 80)), step=1, format="%d")
    with col3:
        rr = st.number_input("Nhịp thở (/phút)", 10, 50, value=int(shared_inputs.get("rr", 16)), step=1, format="%d")
    
    # Clinical findings
    st.markdown("### 🩺 Khám lâm sàng:")
    
    option = st.radio(
        "Chọn tình trạng lâm sàng phù hợp nhất:",
        options=["class1", "class2", "class3", "class4"],
        format_func=lambda x: {
            "class1": "Class I - Không có dấu hiệu suy tim",
            "class2": "Class II - Ran ẩm ½ dưới phổi, S3, có thể tĩnh mạch cảnh nổi",
            "class3": "Class III - Ran ẩm cả 2 phổi (phù phổi cấp)",
            "class4": "Class IV - Shock tim (da lạnh, ẩm, giảm HA, giảm nước tiểu)"
        }[x],
        index=["class1", "class2", "class3", "class4"].index(shared_inputs.get("option", "class1"))
    )
    
    st.markdown("---")
    
    if st.button("📊 Phân loại Killip", type="primary", use_container_width=True):
        classes = {
            "class1": {
                "class": "I",
                "name": "Class I",
                "description": "Không suy tim",
                "findings": "- Không ran ẩm\n- Không S3\n- Huyết động ổn định",
                "mortality": "~5-6%",
                "prevalence": "~40-50%",
                "color": "#28a745"
            },
            "class2": {
                "class": "II",
                "name": "Class II",
                "description": "Suy tim nhẹ-trung bình",
                "findings": "- Ran ẩm ≤ ½ dưới phổi\n- S3 gallop\n- Tĩnh mạch cảnh nổi (JVP tăng)\n- Phù phổi nhẹ trên X-quang",
                "mortality": "~15-20%",
                "prevalence": "~30-40%",
                "color": "#ffc107"
            },
            "class3": {
                "class": "III",
                "name": "Class III",
                "description": "Phù phổi cấp",
                "findings": "- Ran ẩm toàn bộ 2 phổi\n- Khó thở nặng\n- Ho bọt hồng\n- SpO₂ thấp",
                "mortality": "~30-40%",
                "prevalence": "~5-10%",
                "color": "#fd7e14"
            },
            "class4": {
                "class": "IV",
                "name": "Class IV",
                "description": "Shock tim",
                "findings": "- HA tâm thu < 90 mmHg\n- Da lạnh, ẩm\n- Giảm nước tiểu (< 20 mL/h)\n- Lú lẫn\n- Lactate tăng",
                "mortality": "~60-80%",
                "prevalence": "~5-10%",
                "color": "#dc3545"
            }
        }
        
        result = classes[option]
        
        st.markdown("## 📊 Kết quả")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {result['color']}22 0%, {result['color']}44 100%); 
                    padding: 40px; border-radius: 15px; border-left: 5px solid {result['color']}; margin: 20px 0;'>
            <h1 style='color: {result['color']}; margin: 0; text-align: center; font-size: 3.5em;'>
                Killip Class {result['class']}
            </h1>
            <p style='text-align: center; font-size: 1.3em; margin-top: 15px; font-weight: bold;'>
                {result['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tử vong trong viện", result['mortality'])
        with col2:
            st.metric("Tỷ lệ gặp", result['prevalence'])
        
        st.markdown(f"### 📋 Đặc điểm lâm sàng:")
        st.markdown(result['findings'])
        
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị:")
        
        if option == "class1":
            st.success("""
            **Killip Class I - Tiên lượng tốt**
            
            - ✅ Điều trị AMI chuẩn:
              - Aspirin + P2Y12i (Clopidogrel/Ticagrelor)
              - Heparin
              - Statin liều cao
              - ACEi/ARB
              - Beta-blocker (sau 24h nếu ổn định)
            - PCI sớm nếu STEMI
            - Theo dõi dấu sinh tồn
            - Vận động sớm
            """)
        elif option == "class2":
            st.warning("""
            **Killip Class II - Suy tim nhẹ**
            
            - Điều trị AMI + suy tim:
              - **Lợi tiểu:** Furosemide 20-40 mg IV
              - **ACEi:** Bắt đầu sớm (Ramipril, Lisinopril)
              - **Beta-blocker:** Cẩn thận, liều thấp
              - O₂ nếu SpO₂ < 90%
            - Theo dõi sát: HA, nhịp thở, cân nặng
            - Hạn chế dịch
            """)
        elif option == "class3":
            st.error("""
            **Killip Class III - Phù phổi cấp - CẤP CỨU!**
            
            - 🚨 **ICU/CCU ngay**
            - **Oxy/CPAP/Thông khí:**
              - O₂ 100%, CPAP/BiPAP
              - Đặt nội khí quản nếu suy hô hấp
            - **Lợi tiểu mạnh:**
              - Furosemide 40-80 mg IV bolus
              - Có thể infusion 5-10 mg/h
            - **Giãn mạch:**
              - Nitroglycerin 10-200 mcg/min IV
              - Morphine 2-4 mg IV (giảm lo âu)
            - **PCI khẩn** nếu STEMI
            - **Theo dõi:** ABG, lactate, UOP
            """)
        else:  # class4
            st.error("""
            **Killip Class IV - SHOCK TIM - CỰC KỲ NGHIÊM TRỌNG!**
            
            - 🚨 **ICU + Hội chẩn tim mạch NGAY**
            
            **Hồi sức:**
            - **Monitor xâm nhập:** Arterial line, PA catheter
            - **Inotropes:**
              - Dobutamine 2.5-10 mcg/kg/min (nếu HA > 90)
              - Dopamine 5-15 mcg/kg/min (nếu HA thấp)
              - Norepinephrine (nếu cần)
            - **Dịch:** Cẩn thận! Bolus nhỏ 250 mL
            
            **PCI/CABG khẩn:**
            - **PCI ngay lập tức** nếu STEMI
            - Cân nhắc **IABP** (bơm bóng đối xung động mạch chủ)
            - Cân nhắc **CABG khẩn** nếu đa nhánh, thân chung trái
            - Cân nhắc **ECMO/Impella** nếu shock kháng trị
            
            **Theo dõi:**
            - ABG, lactate q1-2h
            - Cardiac output, SVR
            - Nước tiểu (Foley catheter)
            - Echo để đánh giá EF, biến chứng cơ học
            
            **Tìm biến chứng cơ học:**
            - Thủng vách liên thất (VSD)
            - Vỡ cơ nhú (MR cấp)
            - Vỡ thành tự do
            - Tamponade
            → Echo khẩn cấp!
            """)
        
        with st.expander("📊 Bảng tổng hợp Killip Classification"):
            st.markdown("""
            | Class | Lâm sàng | Tử vong | Tỷ lệ | Xử trí |
            |:------|:---------|:--------|:------|:-------|
            | **I** | Không suy tim | ~5-6% | 40-50% | Điều trị AMI chuẩn |
            | **II** | Ran ẩm, S3 | ~15-20% | 30-40% | + Lợi tiểu, ACEi |
            | **III** | Phù phổi cấp | ~30-40% | 5-10% | ICU, O₂, lợi tiểu mạnh |
            | **IV** | Shock tim | ~60-80% | 5-10% | ICU, inotropes, PCI khẩn, IABP |
            """)
        
        with st.expander("📚 Tài liệu"):
            st.markdown("""
            1. **Killip T 3rd, Kimball JT.** Treatment of myocardial infarction in a coronary care unit. 
               A two year experience with 250 patients. *Am J Cardiol.* 1967;20(4):457-64.
            
            2. **Khot UN, et al.** Prognostic importance of physical examination for heart failure in non-ST-elevation acute coronary syndromes. 
               *JAMA.* 2003;290(16):2174-81.
            """)
        
        inputs_dict = {
            "SBP": f"{sbp} mmHg",
            "HR": f"{hr} bpm",
            "RR": f"{rr} /phút",
            "Killip class": result["class"]
        }
        results_dict = {
            "Diagnosis": result["name"],
            "Mortality": result["mortality"],
            "Prevalence": result["prevalence"]
        }
        
        # Export section
        render_export_section(
                title="Killip Classification",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Killip Classification"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="killip",
            calculator_name="Killip Classification",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="killip",
            calculator_name="Killip Classification",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        st.markdown("---")
        render_history_ui(calculator_id="killip", show_actions=True)
        
        references = get_references("KILLIP")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    - **Killip càng cao → Tử vong càng cao**
    - **Killip III-IV:** Cần ICU, can thiệp mạnh
    - **Đơn giản:** Chỉ cần khám lâm sàng
    - **Vẫn có giá trị** trong kỷ nguyên PCI
    """)


if __name__ == "__main__":
    render()

