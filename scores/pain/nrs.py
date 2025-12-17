"""
NRS - Numeric Rating Scale
Thang điểm số đánh giá đau (0-10)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def render():
    """NRS Pain Scale Calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'nrs':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'NRS')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>😣 NRS - Numeric Rating Scale</h2>
    <p style='text-align: center;'><em>Thang điểm số đánh giá đau (0-10)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **NRS (Numeric Rating Scale)** là thang điểm đơn giản, phổ biến nhất để đánh giá mức độ đau.
        
        **Ưu điểm:**
        - Đơn giản, dễ hiểu
        - Nhanh chóng
        - Phù hợp cho người lớn có khả năng giao tiếp
        - Nhạy cảm với thay đổi mức độ đau
        
        **Sử dụng:**
        - Đánh giá đau cấp tính và mạn tính
        - Theo dõi đáp ứng điều trị
        - Đánh giá đau tại phòng cấp cứu, ICU, sau phẫu thuật
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá đau")
    
    # Pain level input
    pain_level = st.slider(
        "Mức độ đau (0-10):",
        min_value=0,
        max_value=10,
        value=0,
        step=1,
        help="0 = Không đau, 10 = Đau dữ dội nhất có thể tưởng tượng"
    )
    
    # Visual scale
    st.markdown("### 📊 Thang điểm")
    
    # Create visual representation
    scale_html = """
    <div style='background: linear-gradient(to right, #10b981 0%, #fbbf24 50%, #ef4444 100%); 
                height: 40px; border-radius: 20px; display: flex; align-items: center; 
                justify-content: center; margin: 20px 0; position: relative;'>
        <div style='position: absolute; left: 0; right: 0; top: 0; bottom: 0; 
                    display: flex; justify-content: space-between; padding: 0 10px;'>
    """
    for i in range(11):
        scale_html += f"<span style='font-weight: bold; color: white; text-shadow: 1px 1px 2px black;'>{i}</span>"
    scale_html += """
        </div>
        <div style='position: absolute; left: calc({}% - 10px); width: 20px; height: 20px; 
                    background: white; border: 3px solid #1f2937; border-radius: 50%; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.3);'></div>
    </div>
    """.format(pain_level * 10)
    
    st.markdown(scale_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("📊 Đánh giá", type="primary", use_container_width=True):
        st.markdown("## 📊 Kết quả")
        
        # Interpret pain level
        if pain_level == 0:
            severity = "Không đau"
            color = "#10b981"
            icon = "✅"
            interpretation = "Bệnh nhân không có đau"
        elif pain_level <= 3:
            severity = "Đau nhẹ"
            color = "#fbbf24"
            icon = "😐"
            interpretation = "Đau nhẹ, có thể chịu đựng được"
        elif pain_level <= 6:
            severity = "Đau vừa"
            color = "#f59e0b"
            icon = "😣"
            interpretation = "Đau vừa, ảnh hưởng đến hoạt động"
        else:
            severity = "Đau nặng"
            color = "#ef4444"
            icon = "😰"
            interpretation = "Đau nặng, ảnh hưởng nghiêm trọng"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} NRS = {pain_level}/10
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {severity}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Treatment recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến nghị điều trị")
        
        if pain_level == 0:
            st.success("""
            **✅ Không cần điều trị giảm đau**
            
            - Tiếp tục theo dõi
            - Đánh giá lại nếu có thay đổi
            """)
        elif pain_level <= 3:
            st.info("""
            **💊 Đau nhẹ (NRS 1-3):**
            
            **Điều trị:**
            - **Bước 1 (Non-opioid):**
              - Paracetamol: 500-1000 mg mỗi 4-6 giờ (max 4g/ngày)
              - Hoặc NSAID: Ibuprofen 400-600 mg mỗi 6-8 giờ
              - Hoặc Diclofenac 50 mg mỗi 8 giờ
            
            **Theo dõi:**
            - Đánh giá lại sau 30-60 phút
            - Mục tiêu: NRS ≤ 3
            """)
        elif pain_level <= 6:
            st.warning("""
            **💊 Đau vừa (NRS 4-6):**
            
            **Điều trị:**
            - **Bước 2 (Opioid yếu + Non-opioid):**
              - Paracetamol 1000 mg + Codeine 30-60 mg mỗi 4-6 giờ
              - Hoặc Tramadol 50-100 mg mỗi 6-8 giờ
              - Hoặc NSAID + Opioid yếu
            
            **Nếu không đáp ứng:**
            - Chuyển sang opioid mạnh (Morphine)
            
            **Theo dõi:**
            - Đánh giá lại sau 30 phút
            - Mục tiêu: NRS ≤ 3
            """)
        else:
            st.error("""
            **🚨 Đau nặng (NRS 7-10):**
            
            **Điều trị khẩn:**
            - **Bước 3 (Opioid mạnh):**
              - **Morphine IV:** 2-5 mg mỗi 5-10 phút đến khi đạt NRS ≤ 3
              - Sau đó: Morphine 5-10 mg mỗi 4 giờ
              - Hoặc Morphine truyền liên tục: 1-5 mg/h
              - Hoặc **Fentanyl IV:** 25-50 µg bolus, sau đó 0.5-2 µg/kg/h
            
            **Kết hợp:**
            - Paracetamol 1000 mg mỗi 6 giờ
            - NSAID nếu không chống chỉ định
            
            **Theo dõi:**
            - Đánh giá lại sau 15-30 phút
            - Mục tiêu: NRS ≤ 3 trong vòng 1 giờ
            - Theo dõi tác dụng phụ: ức chế hô hấp, buồn nôn, ngứa
            
            **Cảnh báo:**
            - Đau nặng cần điều trị ngay lập tức
            - Cân nhắc nguyên nhân đau (chấn thương, thiếu máu, nhiễm trùng...)
            """)
        
        # Pain assessment tips
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            1. **Giải thích cho bệnh nhân:**
               - "0 = Không đau"
               - "10 = Đau dữ dội nhất mà bạn có thể tưởng tượng"
               - "Hãy chọn số từ 0 đến 10 mô tả mức độ đau của bạn"
            
            2. **Đánh giá đau tại thời điểm:**
               - Đau hiện tại
               - Đau khi nghỉ ngơi
               - Đau khi vận động (nếu có)
            
            3. **Theo dõi:**
               - Đánh giá lại sau mỗi can thiệp điều trị
               - Ghi nhận NRS trước và sau điều trị
               - Mục tiêu: Giảm ≥2 điểm hoặc NRS ≤ 3
            
            ### 📋 Khi nào đánh giá:
            - Khi bệnh nhân vào viện
            - Trước và sau điều trị giảm đau
            - Mỗi 4 giờ ở bệnh nhân nội trú
            - Khi bệnh nhân than đau
            - Sau phẫu thuật: Mỗi 2-4 giờ trong 24 giờ đầu
            
            ### ⚠️ Lưu ý:
            - NRS chỉ dùng cho bệnh nhân có khả năng giao tiếp
            - Trẻ em < 7 tuổi: Dùng FLACC hoặc Wong-Baker Faces
            - Bệnh nhân không tỉnh táo: Dùng thang điểm hành vi (FLACC, BPS)
            - Bệnh nhân không nói được: Dùng thang điểm hành vi
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "NRS Score": pain_level
        }
        
        results_dict = {
            "NRS Score": f"{pain_level}/10",
            "Severity": severity,
            "Interpretation": interpretation
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="NRS",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="NRS"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="nrs",
            calculator_name="NRS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="nrs",
            calculator_name="NRS",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="nrs", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="nrs",
            calculator_name="NRS",
            category="Đau",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **NRS 0-3:** Đau nhẹ → Non-opioid (Paracetamol, NSAID)
    2. **NRS 4-6:** Đau vừa → Opioid yếu (Codeine, Tramadol)
    3. **NRS 7-10:** Đau nặng → Opioid mạnh (Morphine, Fentanyl)
    4. **Mục tiêu điều trị:** NRS ≤ 3
    5. **Đánh giá lại:** Sau 15-30 phút (đau nặng) hoặc 30-60 phút (đau nhẹ/vừa)
    """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("NRS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

