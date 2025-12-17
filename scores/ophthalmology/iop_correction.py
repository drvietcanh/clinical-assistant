"""
IOP Correction Calculator
Điều chỉnh nhãn áp theo độ dày giác mạc trung tâm (CCT)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_corrected_iop(measured_iop, cct):
    """
    Điều chỉnh IOP theo CCT
    
    Công thức: Corrected IOP = Measured IOP - (CCT - 545) × 0.007
    
    Parameters:
    - measured_iop: Nhãn áp đo được (mmHg)
    - cct: Độ dày giác mạc trung tâm (μm)
    
    Returns:
    - dict với IOP điều chỉnh và interpretation
    """
    # Standard CCT = 545 μm
    standard_cct = 545
    correction_factor = 0.007  # mmHg per μm
    
    # Calculate correction
    correction = (cct - standard_cct) * correction_factor
    corrected_iop = measured_iop - correction
    
    # Interpret
    if corrected_iop <= 21:
        status = "Bình thường"
        interpretation = "Nhãn áp trong giới hạn bình thường"
        color = "green"
    else:
        status = "Cao"
        interpretation = "Nhãn áp cao - Nguy cơ glaucoma"
        color = "red"
    
    # CCT interpretation
    if cct < 500:
        cct_status = "Mỏng (< 500 μm)"
        cct_note = "Giác mạc mỏng → IOP đo thường THẤP hơn thực tế → Nguy cơ glaucoma cao hơn"
    elif cct > 590:
        cct_status = "Dày (> 590 μm)"
        cct_note = "Giác mạc dày → IOP đo thường CAO hơn thực tế → Nguy cơ glaucoma thấp hơn"
    else:
        cct_status = "Bình thường (500-590 μm)"
        cct_note = "Giác mạc độ dày bình thường"
    
    return {
        "measured_iop": measured_iop,
        "cct": cct,
        "correction": correction,
        "corrected_iop": corrected_iop,
        "status": status,
        "interpretation": interpretation,
        "color": color,
        "cct_status": cct_status,
        "cct_note": cct_note
    }


def render():
    """Render IOP Correction calculator interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'iop_correction':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        # Pre-fill inputs from shared result (optional)
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #3B82F6;'>👁️ IOP Correction</h2>
    <p style='text-align: center;'><em>Điều chỉnh nhãn áp theo độ dày giác mạc (CCT)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về IOP Correction"):
        st.markdown("""
        **IOP (Intraocular Pressure) Correction** điều chỉnh nhãn áp đo được 
        dựa trên độ dày giác mạc trung tâm (Central Corneal Thickness - CCT).
        
        **Tại sao cần điều chỉnh?**
        - Tonometry đo áp lực qua giác mạc
        - Giác mạc dày → đo IOP CAO hơn thực tế
        - Giác mạc mỏng → đo IOP THẤP hơn thực tế
        
        **Ý nghĩa lâm sàng:**
        - **CCT mỏng:** Nguy cơ glaucoma cao hơn
        - **CCT dày:** IOP thực tế thấp hơn đo được
        
        **Lưu ý:**
        - Công thức này chỉ là ước tính
        - CCT là yếu tố nguy cơ độc lập của glaucoma
        - Quyết định điều trị dựa trên nhiều yếu tố, không chỉ IOP
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Nhập số liệu")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="iop_correction",
            calculator_name="IOP Correction",
            category="Mắt",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ Nhãn áp đo được (IOP)")
        
        measured_iop = st.number_input(
            "IOP (mmHg)",
            min_value=5.0,
            max_value=60.0,
            value=18.0,
            step=0.5,
            help="Nhãn áp đo bằng tonometer"
        )
        
        st.info("""
        💡 **Giá trị bình thường:**
        - 10-21 mmHg (trung bình ~15 mmHg)
        - > 21 mmHg: Nghi ngờ glaucoma
        - Biến động trong ngày: 2-6 mmHg
        """)
    
    with col2:
        st.markdown("### 2️⃣ Độ dày giác mạc trung tâm (CCT)")
        
        cct = st.number_input(
            "CCT (μm - micrometers)",
            min_value=400,
            max_value=700,
            value=545,
            step=5,
            help="Đo bằng pachymetry"
        )
        
        st.info("""
        💡 **Giá trị bình thường:**
        - 500-590 μm (trung bình 540-545 μm)
        - < 500 μm: Giác mạc mỏng
        - > 590 μm: Giác mạc dày
        """)
    
    st.markdown("---")
    
    # Pre-fill from shared result if available
    shared_inputs = st.session_state.get('shared_inputs', {})
    
    if st.button("🔬 Điều chỉnh IOP", type="primary", use_container_width=True):
        result = calculate_corrected_iop(measured_iop, cct)
        
        st.markdown("## 📊 Kết quả")
        
        # IOP values
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("IOP đo được", f"{result['measured_iop']:.1f} mmHg")
        
        with col2:
            if result['correction'] > 0:
                st.metric("Hiệu chỉnh", f"+{result['correction']:.1f} mmHg", 
                         delta="Giác mạc dày", delta_color="inverse")
            else:
                st.metric("Hiệu chỉnh", f"{result['correction']:.1f} mmHg",
                         delta="Giác mạc mỏng" if result['correction'] < 0 else "Chuẩn")
        
        with col3:
            score_color = "#28a745" if result["color"] == "green" else "#dc3545"
            st.markdown(f"""
            <div style='text-align: center; padding: 10px; background-color: {score_color}22; border-radius: 10px; border: 2px solid {score_color};'>
                <p style='margin: 0; font-size: 0.9em; color: #666;'>IOP điều chỉnh</p>
                <p style='margin: 5px 0; font-size: 2em; font-weight: bold; color: {score_color};'>
                    {result['corrected_iop']:.1f}
                </p>
                <p style='margin: 0; font-size: 0.9em; color: #666;'>mmHg</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # CCT status
        st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 4px solid #3B82F6;'>
            <h3 style='margin-top: 0;'>📏 Độ dày giác mạc (CCT)</h3>
            <p style='font-size: 1.2em;'><strong>{result['cct']} μm</strong> - {result['cct_status']}</p>
            <p style='font-size: 1.1em;'>{result['cct_note']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Interpretation
        score_color_map = {
            "green": "#28a745",
            "red": "#dc3545"
        }
        final_color = score_color_map[result["color"]]
        
        st.markdown(f"""
        <div style='background-color: {final_color}22; padding: 20px; border-radius: 10px; border: 2px solid {final_color};'>
            <h3 style='color: {final_color}; margin-top: 0;'>🎯 Đánh giá nhãn áp</h3>
            <p style='font-size: 1.2em; font-weight: bold;'>{result['status']}</p>
            <p style='font-size: 1.1em;'>{result['interpretation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Recommendations
        if result["corrected_iop"] > 21:
            st.warning("""
            ⚠️ **IOP cao - Nghi ngờ Glaucoma**
            
            **Đánh giá thêm:**
            - Khám đáy mắt (ghi hình gai thị)
            - Đo thị trường (visual field)
            - OCT gai thị & lớp sợi thần kinh
            - Góc tiền phòng (gonioscopy)
            - IOP nhiều lần, nhiều thời điểm
            
            **Yếu tố nguy cơ glaucoma:**
            - IOP cao
            - **CCT mỏng** (yếu tố nguy cơ quan trọng)
            - Tuổi cao
            - Tiền sử gia đình
            - Cận thị cao
            - Da màu (gốc Phi)
            
            **Điều trị:**
            - Thuốc nhỏ mắt hạ nhãn áp (prostaglandin analog, beta-blocker...)
            - Laser (SLT, LPI)
            - Phẫu thuật (trabeculectomy) nếu cần
            - Mục tiêu: Giảm IOP 20-30% hoặc < 18 mmHg
            """)
        else:
            st.success("""
            ✅ **IOP trong giới hạn bình thường**
            
            **Theo dõi:**
            - Khám mắt định kỳ hàng năm (nếu > 40 tuổi)
            - Nếu có yếu tố nguy cơ: Khám thường xuyên hơn
            
            **Lưu ý:**
            - IOP bình thường không loại trừ glaucoma (normal-tension glaucoma)
            - Vẫn cần khám đáy mắt & thị trường định kỳ
            """)
        
        # CCT significance
        with st.expander("📊 Ý nghĩa CCT trong Glaucoma"):
            st.markdown("""
            ### CCT là yếu tố nguy cơ độc lập:
            
            **OHTS (Ocular Hypertension Treatment Study):**
            - CCT mỏng → Nguy cơ glaucoma tăng 3-4 lần
            - Mỗi giảm 40 μm CCT → Tăng 70% nguy cơ
            
            **Tại sao CCT quan trọng?**
            
            1. **Ảnh hưởng đến đo IOP:**
               - Giác mạc dày → GAT đo cao hơn IOP thật
               - Giác mạc mỏng → GAT đo thấp hơn IOP thật
            
            2. **Yếu tố nguy cơ sinh học:**
               - CCT mỏng có thể phản ánh nhược điểm cấu trúc
               - Gai thị dễ tổn thương hơn
            
            ### Phân loại theo CCT:
            
            | CCT (μm) | Phân loại | Ý nghĩa |
            |:---------|:----------|:--------|
            | < 500 | Rất mỏng | Nguy cơ glaucoma cao |
            | 500-520 | Mỏng | Tăng nguy cơ |
            | 520-590 | Bình thường | Nguy cơ trung bình |
            | 590-620 | Dày | IOP có thể overestimate |
            | > 620 | Rất dày | Cân nhắc bệnh lý giác mạc |
            
            ### Quyết định điều trị:
            
            **CCT mỏng + IOP cao:**
            - Nguy cơ rất cao → Điều trị tích cực
            - Mục tiêu IOP thấp hơn
            
            **CCT dày + IOP cao:**
            - IOP thật thấp hơn đo được
            - Đánh giá gai thị & thị trường quan trọng
            - Cân nhắc điều trị hoặc theo dõi chặt
            
            **Lưu ý:**
            - CCT không thay đổi quyết định điều trị dựa trên tổn thương gai thị
            - Nếu đã có tổn thương → Điều trị bất kể CCT
            """)
        
        with st.expander("🔬 Các công thức điều chỉnh IOP"):
            st.markdown("""
            ### Công thức thường dùng:
            
            **1. Dresden Study (công thức này):**
            ```
            Corrected IOP = Measured IOP - (CCT - 545) × 0.007
            ```
            - Chuẩn CCT: 545 μm
            - Hệ số: 0.007 mmHg/μm
            
            **2. OHTS:**
            ```
            Corrected IOP = Measured IOP - (CCT - 544) × 0.0071
            ```
            - Tương tự Dresden
            
            **3. Doughty & Zaman:**
            ```
            Corrected IOP = Measured IOP - 0.0046 × (CCT - 520)
            ```
            - Hệ số khác
            
            **Lưu ý:**
            - Các công thức chỉ là ước tính
            - Mối quan hệ IOP-CCT không hoàn toàn tuyến tính
            - Hiện nay không khuyến cáo "điều chỉnh" IOP trong quyết định lâm sàng
            - CCT được dùng như yếu tố nguy cơ, không phải để điều chỉnh IOP
            
            ### Khuyến cáo hiện tại (AAO):
            - Ghi nhận cả IOP đo được VÀ CCT
            - Không "điều chỉnh" IOP theo công thức
            - Sử dụng CCT như yếu tố nguy cơ độc lập
            - Quyết định điều trị dựa trên:
              - IOP đo được
              - CCT
              - Tình trạng gai thị
              - Thị trường
              - Yếu tố nguy cơ khác
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Gordon MO, Beiser JA, Brandt JD, et al.** The Ocular Hypertension Treatment Study: 
               baseline factors that predict the onset of primary open-angle glaucoma. 
               Arch Ophthalmol. 2002;120(6):714-20.
            
            2. **Doughty MJ, Zaman ML.** Human corneal thickness and its impact on intraocular pressure measures: 
               a review and meta-analysis approach. Surv Ophthalmol. 2000;44(5):367-408.
            
            3. **Shih CY, Graff Zivin JS, Trokel SL, Tsai JC.** Clinical significance of central corneal thickness 
               in the management of glaucoma. Arch Ophthalmol. 2004;122(9):1270-5.
            
            4. **Herndon LW, Choudhri SA, Cox T, et al.** Central corneal thickness in normal, glaucomatous, 
               and ocular hypertensive eyes. Arch Ophthalmol. 1997;115(9):1137-41.
            
            5. **American Academy of Ophthalmology.** Primary Open-Angle Glaucoma Preferred Practice Pattern. 2020.
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "IOP đo được": f"{measured_iop:.1f} mmHg",
            "CCT": f"{cct} μm"
        }
        
        results_dict = {
            "IOP điều chỉnh": f"{result['corrected_iop']:.1f} mmHg",
            "Hiệu chỉnh": f"{result['correction']:.1f} mmHg",
            "Trạng thái": result['status'],
            "Đánh giá": result['interpretation'],
            "CCT": result['cct_status']
        }
        
        # Save to history
        # Export section
        render_export_section(
                title="IOP Correction",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="IOP Correction"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="iop_correction",
            calculator_name="IOP Correction",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="iop_correction",
            calculator_name="IOP Correction",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="iop_correction", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("IOP Correction")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **CCT ảnh hưởng đo IOP** - Giác mạc dày → đo cao hơn, mỏng → đo thấp hơn
    
    2. **CCT là yếu tố nguy cơ độc lập** - Không chỉ ảnh hưởng đo lường
    
    3. **CCT mỏng (< 500 μm)** - Nguy cơ glaucoma cao, cần theo dõi chặt
    
    4. **Quyết định điều trị** - Dựa trên nhiều yếu tố: IOP, CCT, gai thị, thị trường
    
    5. **Không khuyến cáo "điều chỉnh" IOP theo công thức** trong thực hành lâm sàng hiện đại
    
    6. **Glaucoma có thể xảy ra với IOP bình thường** (normal-tension glaucoma)
    """)


if __name__ == "__main__":
    render()

